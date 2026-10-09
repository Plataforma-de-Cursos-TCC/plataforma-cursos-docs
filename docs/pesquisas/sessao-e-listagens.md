---
id: pesquisa-sessao-e-listagens
titulo: "Pesquisa — sessão JWT em cookie e estado de listagens"
tipo: pesquisa
status: referência das ADR-0008 e ADR-0009
atualizado: 2026-10-09
---
# Pesquisa — sessão JWT em cookie e estado de listagens

Base para ADR-0008 (sessão e autenticação) e ADR-0009 (listagens, paginação e contrato de API). Esta pesquisa diz **como** implementar as decisões já tomadas. Não rediscute as decisões.

Stack de referência (ADR-0007): Laravel 13 com PHP 8.3 na API REST, Next.js em SPA (sem Server Components e sem Server Actions), React Query, MySQL 8, Redis e RabbitMQ.

Decisões já tomadas, usadas como premissa:

1. JWT com expiração de 1 h, em cookie HttpOnly (nunca `localStorage`). Opção "manter conectado" para não pedir novo login.
2. Filtros, ordenação e página das listagens na URL (query string), com React Query. Deve sobreviver a F5 e a link compartilhado.
3. Paginação obrigatória em toda listagem.
4. Nada que o back devolve pode ficar sem uso no front (sem over-fetching).

Convenção deste documento:

- **Fonte**: afirmação com URL e data de consulta (2026-10-09).
- **(inferência)**: raciocínio meu sobre a stack, sem fonte direta. Precisa de validação.
- **(não verificado)**: ponto que não consegui checar nesta rodada.

---

## 1. Sessão JWT em cookie HttpOnly

### 1.1 Guard e pacote JWT

Laravel 13 exige PHP 8.3 como mínimo e não traz breaking changes em relação ao 12 ([Laravel 13 release notes](https://laravel.com/framework/docs/releases), consultado 2026-10-09; [Laravel News — Laravel 13 released](https://laravel-news.com/laravel-13-released), consultado 2026-10-09).

Duas opções:

| Opção | O que entrega | Custo |
|---|---|---|
| `php-open-source-saver/jwt-auth` | Guard para `auth:api`, geração e validação de JWT, TTL configurável, blacklist, customização do nome do cookie. Fork do `tymondesigns/jwt-auth` com a mesma API ([repositório](https://github.com/PHP-Open-Source-Saver/jwt-auth), consultado 2026-10-09; [docs](https://laravel-jwt-auth.readthedocs.io), consultado 2026-10-09) | Dependência de terceiro. O próprio repositório removeu Laravel 10 e 11 do CI em fev/2026, então é preciso confirmar no `composer.json` o suporte ao Laravel 13 antes de adotar |
| `lcobucci/jwt` | Biblioteca de baixo nível para montar, assinar e validar JWT (RFC 7519). Não traz guard para Laravel ([repositório](https://github.com/lcobucci/jwt), consultado 2026-10-09) | Exige guard próprio, middleware próprio, blacklist própria e refresh próprio. Mais código para manter |

**Recomendação:** `php-open-source-saver/jwt-auth`. O guard, o TTL e a blacklist já existem, e o que sobra para o projeto é a leitura do token a partir do cookie. O repositório tem commit "Add cookie key name customization and documentation" na pasta `docs/` ([repositório](https://github.com/PHP-Open-Source-Saver/jwt-auth), consultado 2026-10-09), o que indica suporte a nome de cookie customizado. Confirmar a chave de configuração na documentação antes de implementar (não verificado).

`lcobucci/jwt` fica como alternativa se o pacote não suportar Laravel 13. Nesse caso o custo de implementar guard e blacklist sobe.

### 1.2 Atributos do cookie

Fonte: [MDN — Using HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies), última modificação 2026-09-17, consultado 2026-10-09.

- **HttpOnly**: JavaScript não lê o cookie. Mitiga roubo por XSS. Por isso o token nunca vai para `localStorage`.
- **Secure**: cookie só trafega em HTTPS.
- **SameSite**: controla envio em requisições cross-site.
  - `Strict`: envia apenas em requisições originadas no mesmo site. Indicado para cookies de autenticação, segundo a própria MDN.
  - `Lax`: também envia em navegação de topo (clique em link vindo de outro site). Útil para links de e-mail (UC011, recuperação de senha), mas aceita um pouco mais de exposição.
  - `None`: exige `Secure` e envia em qualquer contexto. Evitar.
  - Sem atributo, o navegador trata como `Lax` (MDN).
- **Max-Age** em vez de **Expires**: MDN informa que `Max-Age` tem precedência e evita erro de relógio entre cliente e servidor.
- **Prefixo `__Host-`**: exige `Secure`, `Path=/` e ausência de `Domain`. Impede que outro subdomínio sobrescreva o cookie. OWASP também recomenda esse prefixo ([OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), consultado 2026-10-09).

**Recomendação de cookie de acesso:**

```
Set-Cookie: __Host-access=<jwt>; Path=/; Secure; HttpOnly; SameSite=Strict; Max-Age=3600
```

Em Laravel, o helper `cookie()` aceita os mesmos atributos (`cookie($nome, $valor, $minutos, $path, $domain, $secure, $httpOnly, $raw, $sameSite)`). (inferência: confirmar na doc de cookies do Laravel 13 que `EncryptCookies` não criptografa esse cookie, ou excluí-lo via `$except`. Criptografar o JWT por cima dele não traz ganho e confunde a leitura.)

**Por que `Strict` e não `Lax`:** a SPA e a API ficam no mesmo site (ver 1.3), então as chamadas `fetch` da SPA para a API são same-site e o cookie sempre é enviado. `Strict` só deixa de enviar em navegação de topo vinda de outro site, que não acontece em chamadas de API. (inferência.) Se a fluxo de UC011 (link de redefinição) precisar que o cookie exista logo na chegada à SPA, usar `Lax` no cookie de refresh, e não no de acesso.

### 1.3 Mesmo site × subdomínios × CORS

Fonte: [MDN — Using HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies), consultado 2026-10-09.

- **Site** é o domínio registrável mais o esquema. Requisição cross-site é aquela em que site ou esquema difere da página atual (MDN).
- `app.exemplo.com` e `api.exemplo.com` são **mesmo site** (mesmo domínio registrável), mas **origens diferentes**. Por isso precisam de CORS, mesmo com SameSite funcionando.
- Sem atributo `Domain`, o cookie vai só para o host que o criou. Com `__Host-`, isso é obrigatório e funciona bem: o cookie é criado por `api.exemplo.com` e enviado para `api.exemplo.com`, que é o único consumidor.
- Se app e API estiverem em domínios registráveis diferentes (ex.: `*.vercel.app` e outro domínio para a API), o cookie vira third-party. Navegadores restringem third-party cookies e `SameSite=None` deixa de ser opção segura. (inferência.) Para `*.vercel.app`, cada projeto é um site separado pela Public Suffix List. (não verificado: confirmar antes de decidir a topologia de hospedagem.)

**Recomendação:** app e API no mesmo domínio registrável, por exemplo `app.exemplo.com` e `api.exemplo.com`.

**CORS com credenciais** (Laravel): em `config/cors.php`, `supports_credentials` deve ser `true`, e `allowed_origins` deve listar a origem exata da SPA, nunca `*`. A documentação do Sanctum para SPA usa esse mesmo ajuste ([Laravel Sanctum — SPA authentication](https://laravel.com/framework/docs/sanctum), consultado 2026-10-09).

No front, toda chamada à API usa `credentials: 'include'` (ou `withCredentials: true` se usar Axios):

```ts
fetch(`${API}/api/v1/cursos`, { credentials: 'include' })
```

### 1.4 CSRF em API com cookie

Com cookie de autenticação, um site malicioso pode disparar requisição de escrita que carrega o cookie. OWASP recomenda token CSRF, e não só SameSite. SameSite é defesa em profundidade, não substitui o token ([OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html), consultado 2026-10-09). OWASP indica o double-submit com token assinado como padrão.

**Recomendação (dupla submissão assinada):**

- O servidor emite cookie `__Host-csrf` não-HttpOnly, com valor HMAC ligado ao `jti` da sessão. Não-HttpOnly porque a SPA precisa ler o valor para enviar no header.
- A SPA envia o valor em `X-CSRF-Token` em `POST`, `PUT`, `PATCH` e `DELETE`.
- Um middleware compara o header com o cookie e recalcula o HMAC. Divergência gera 419 ou 403.
- Para requisições não-seguras, validar também o header `Origin` contra a lista de origens permitidas. (inferência: é defesa extra, barata.)
- Header customizado sem CORS liberado gera preflight, que bloqueia requisição cross-origin não autorizada. (inferência.)

Alternativa mais simples: o Sanctum usa o padrão `XSRF-TOKEN` (cookie lido pela SPA) + header `X-XSRF-TOKEN`, com `withXSRFToken` ([Laravel Sanctum](https://laravel.com/framework/docs/sanctum), consultado 2026-10-09). Se o pacote JWT não encaixar, usar esse padrão.

### 1.5 Login, logout e revogação

- `POST /api/v1/auth/login`: valida credenciais, emite access token e refresh token, grava os dois cookies. Regenerar identificador de sessão a cada login (MDN: prevenir session fixation).
- `POST /api/v1/auth/logout`: remove os dois cookies com o mesmo nome, path e domínio, com `Max-Age=0` (MDN: para apagar, recriar o cookie com `Max-Age` zero ou negativo). Adicionalmente, grava o `jti` do access token na blacklist.

**Blacklist no Redis por `jti`:**

```
SET jwt:revoked:<jti> 1 EX <segundos_ate_exp>
```

Na validação do guard, consultar `EXISTS jwt:revoked:<jti>`. O TTL da chave é o tempo restante do token, então a blacklist nunca passa de 1 h (decisão 1). (inferência: custo de uma consulta Redis por requisição autenticada. Aceitável para o porte do projeto.)

### 1.6 Refresh com rotação e detecção de reuso

Com access token de 1 h e opção "manter conectado", o refresh token é o segredo de longa duração. Por isso ele deve ser opaco, não JWT, e rotacionado.

Fonte: [RFC 9700 — OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/info/rfc9700/), seção 4.14, consultado 2026-10-09. Para clientes públicos, o refresh token deve ser sender-constrained ou usar rotação. Na rotação, cada uso emite um novo refresh token e invalida o anterior. Se um refresh token já usado for apresentado de novo, o servidor deve revogar a família inteira. Ver também [OAuth 2.0 Best Current Practice](https://oauth.net/2/oauth-best-practice/), consultado 2026-10-09.

O RFC trata de OAuth, mas o problema é o mesmo para a SPA (inferência: aplicar o padrão ao login próprio).

**Modelo:**

- Tabela MySQL `sessoes_refresh`: `id`, `usuario_id`, `familia_id`, `hash_token` (SHA-256 do token, nunca o token em texto), `usado_em`, `revogado_em`, `expira_em`.
- Cookie `__Host-refresh`: `Path=/api/v1/auth/refresh`, `Secure`, `HttpOnly`, `SameSite=Strict`.
  - `Path` restringe o envio, mas MDN é explícita: `Path` não é medida de segurança. A proteção vem de `HttpOnly` e da rotação.
- `POST /api/v1/auth/refresh`:
  1. Procura o hash do token. Se não existe: 401.
  2. Se o token já foi usado (`usado_em` preenchido): revoga toda a `familia_id` e retorna 401. Isso é reuso, e indica roubo.
  3. Caso normal: marca o token como usado, cria um novo na mesma família, emite novo access token e novo cookie de refresh.

**Trade-off com o Vault:** a nota de arquitetura do Lucas no Obsidian fala em "TTL curto 15-30 min". A decisão atual é 1 h mais "manter conectado". Não consegui ler o Vault nesta rodada, porque ele só é lido sob pedido. A rotação com detecção de reuso permite manter o access de 1 h, porque o risco de um access roubado fica limitado a 1 h, e o refresh roubado é detectado no próximo uso. Vale conciliar explicitamente com a nota antes de fechar o ADR-0008.

### 1.7 Duração do cookie "manter conectado"

- **Com a opção marcada:** cookie `__Host-refresh` com `Max-Age=2592000` (30 dias). Recomendação do documento, por ser um prazo comum para "manter conectado" e curto o bastante para não ficar indefinido. (inferência: 30 dias é convenção, não requisito de norma.)
- **Sem a opção:** cookie sem `Max-Age` e sem `Expires`, ou seja, cookie de sessão. MDN: é apagado quando a sessão termina, e o navegador define quando isso acontece. Algumas configurações de navegador restauram sessões ao reabrir, então não é garantia de logout ao fechar.
- Em ambos os casos, o access token de 1 h é o mesmo. O que muda é a validade do refresh.

### 1.8 Next.js SPA: saber se está logado e proteger rotas

- O cookie é HttpOnly, então o React não consegue ler o token. A SPA descobre o estado de autenticação perguntando à API.
- `GET /api/v1/auth/me`: 200 com dados do usuário, ou 401. Essa chamada é o único ponto de verdade no cliente.
- Via React Query: `useQuery({ queryKey: ['me'], queryFn: getMe, retry: false })`. O estado `isError` com 401 significa deslogado.
- Proteção de rota no cliente: componente de layout que espera `['me']` e redireciona para o login se 401. Esse guard é de experiência, não de segurança. A segurança fica na API, que valida o token em cada rota.
- `middleware.ts` do Next pode checar só a presença do cookie para redirecionar mais cedo. (inferência.) Não pode validar o JWT, porque não tem acesso à chave e a validação não é seu papel.
- Como o ADR-0007 proíbe Server Components e Server Actions, não há renderização no servidor autenticada. Tudo passa pela API.

---

## 2. Estado de listagem na URL (Next.js App Router + React Query)

### 2.1 Princípio

A URL é a fonte de verdade do estado da listagem: `?page=2&q=python&ordem=recente`. React Query usa os mesmos parâmetros na chave de cache. Assim:

- F5 mantém a página e os filtros, porque o estado está na URL.
- Link compartilhado abre a mesma visão.
- Voltar do navegador volta ao estado anterior.

Para a SPA, `useSearchParams` e `useRouter` do `next/navigation` fazem a leitura e a escrita. Em rota estática ou CSR, `useSearchParams` precisa de um `<Suspense>` ao redor, senão o build reclama. Fonte: [Next.js — missing-suspense-with-csr-bailout](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout), consultado 2026-10-09.

### 2.2 Chave de cache e paginação sem piscar

Fonte para `placeholderData`: [TanStack Query — Paginated Queries](https://tanstack.com/query/latest/docs/framework/react/guides/paginated-queries), consultado 2026-10-09. A doc diz que `placeholderData: keepPreviousData` (ou `(prev) => prev`) mantém os dados da última busca bem-sucedida enquanto a nova chave carrega. `isPlaceholderData` indica que o dado exibido é provisório. Em TanStack v5, `keepPreviousData` virou função exportada de `@tanstack/react-query`, e a opção antiga `keepPreviousData: true` não existe mais (fonte: [GitHub discussion 6460](https://github.com/TanStack/query/discussions/6460), consultado 2026-10-09).

Sem `placeholderData`, a lista some e volta a cada mudança de página, o que pisca na tela.

### 2.3 Hook de parâmetros (exemplo)

Pseudocódigo para fixar o padrão. Não é implementação final.

```ts
// useListParams.ts
const DEFAULTS = { page: 1, q: '', ordem: 'recente' } as const;

export function useListParams() {
  const router = useRouter();
  const sp = useSearchParams();

  // zod: valor inválido ou ausente vira default. Não vira erro de tela.
  const params = parseListParams(sp, DEFAULTS);

  const setParams = (patch: Partial<ListParams>) => {
    const next = { ...params, ...patch };
    if (!('page' in patch)) next.page = 1; // mudou filtro ou ordem: volta à página 1
    router.replace(`?${serializeListParams(next, DEFAULTS)}`, { scroll: false });
  };

  return { params, setParams };
}
```

Uso na tela:

```ts
const { params, setParams } = useListParams();
const query = useQuery({
  queryKey: ['cursos', params],
  queryFn: () => api.get('/api/v1/cursos', { params }),
  placeholderData: keepPreviousData,
});
```

### 2.4 Regras

| Regra | Motivo | Origem |
|---|---|---|
| Parâmetros com valor default **não** aparecem na URL (`page=1`, `ordem=recente` somem) | URL canônica; um mesmo estado tem uma única URL | (inferência) |
| Mudança de filtro ou ordenação volta `page` para 1 | Página 7 de um filtro antigo pode não existir no novo | (inferência, convenção comum) |
| `router.replace` para mudança de filtro; `push` só para mudança de página | Evita poluir o histórico com cada tecla digitada | (inferência) |
| Busca textual com debounce (sugestão 300 ms) antes de atualizar a URL | Evita uma requisição por tecla | (inferência; valor a validar) |
| Validação com zod: `page` inteiro ≥ 1, `ordem` em lista fechada, `q` com tamanho máximo | Parâmetro inválido não quebra a tela nem chega ao back | (não verificado: zod não foi pesquisado nesta rodada) |
| Parâmetros da URL são o mesmo nome enviado à API | Evita camada de mapeamento que esconde divergência | (inferência) |

**Atenção:** o link compartilhado mostra a mesma página, mas o back decide o que o usuário pode ver. A URL não é controle de acesso.

---

## 3. Paginação no Laravel

### 3.1 Três métodos

Fonte: [Laravel 13 — Database: Pagination](https://laravel.com/framework/docs/pagination), consultado 2026-10-09.

| Método | Consulta | Retorna | Quando |
|---|---|---|---|
| `paginate` | Conta o total e usa `LIMIT`/`OFFSET` | Total, última página, links por número de página | Quando a UI mostra número de páginas ou permite pular para a página N |
| `simplePaginate` | Só `LIMIT`/`OFFSET`, sem contagem | Apenas próxima e anterior | Quando não se exibe total. Evita o `COUNT` |
| `cursorPaginate` | `WHERE` sobre colunas ordenadas, com cursor codificado | Próxima e anterior, sem número de página | Grandes volumes e dados que mudam com frequência |

Pontos da doc que importam aqui:

- `paginate` usa OFFSET. Com escrita frequente, pode repetir ou pular registros entre páginas. A doc diz isso sobre offset em geral.
- `cursorPaginate` exige `orderBy` em coluna **única** ou combinação única, sem valores `null`, e as colunas precisam pertencer à tabela paginada. Não suporta número de página.
- Com índice nas colunas ordenadas, o cursor tem desempenho melhor, porque o OFFSET não percorre registros anteriores.

### 3.2 Formato JSON

A doc mostra o formato padrão de um paginator serializado: `total`, `per_page`, `current_page`, `last_page`, `first_page_url`, `last_page_url`, `next_page_url`, `prev_page_url`, `path`, `from`, `to` e `data` ([Laravel — Converting Results to JSON](https://laravel.com/framework/docs/pagination), consultado 2026-10-09).

Para um contrato mais limpo, usar API Resource com coleção paginada, que separa `data`, `links` e `meta`. (não verificado nesta rodada: confirmar o formato exato de `links` e `meta` na doc de Resources do Laravel 13.)

Formato proposto para toda listagem:

```json
{
  "data": [ { "id": 12, "titulo": "..." } ],
  "meta": { "page": 2, "per_page": 20, "total": 143, "last_page": 8 },
  "links": { "next": "...", "prev": "..." }
}
```

Se o método for `cursorPaginate`, `meta` traz `next_cursor` e `prev_cursor` no lugar de `total` e `last_page`.

### 3.3 Limites e validação

- `per_page` padrão 20 e máximo 100. (inferência: convenção comum. Evita requisição que devolve milhares de linhas, o que também é over-fetching.)
- `page` inteiro ≥ 1. `per_page` inteiro entre 1 e 100.
- Validar no `FormRequest` da listagem, não no controller. Valor fora da faixa retorna 422, e o front já trata esse caso junto com a validação zod da seção 2.
- Ordenação estável: sempre `orderBy(<campo>)->orderBy('id')`. O `id` desempata registros com o mesmo valor e evita duplicação entre páginas. (inferência.)
- Índices: para cada combinação de filtro e ordenação usada na listagem, criar índice composto que começa pelas colunas de filtro e termina pela ordenação com `id`. (inferência.)

### 3.4 Recomendação por listagem

Listagens levantadas no projeto:

| Listagem | Método | perPage | Justificativa | Ordenação e índice sugeridos |
|---|---|---|---|---|
| Catálogo de cursos (público) | `paginate` | 20 | Usuário navega por páginas numeradas. Volume de catálogo é moderado | `(publicado, created_at, id)` |
| Meus cursos (aluno) | `paginate` | 10 | Pouco volume por aluno. Número de páginas é útil | `(usuario_id, created_at, id)` |
| Usuários (admin, UC008) | `paginate` | 20 | Admin pula para página N e precisa do total | `(papel, nome, id)` |
| Avaliações de um curso (UC010) | `paginate` | 10 | Volume cresce, mas a leitura é por páginas. Mantém `page` na URL, como a decisão 2 pede | `(curso_id, created_at, id)` |
| Mensagens do tutor de IA (UC001) | `cursorPaginate` | 20 | Histórico de chat recebe mensagem nova o tempo todo. OFFSET repetiria ou pularia mensagens | `(conversa_id, created_at, id)` |

**Conflito a decidir:** a decisão 2 pede página na URL. O histórico de mensagens usa cursor, que não tem número de página. Recomendo exceção explícita para essa listagem. O cursor vai na URL como `?cursor=...`, o que mantém o estado compartilhável. Não é uma rediscussão da decisão, é um caso que ela não previu.

---

## 4. Contrato sem over-fetching

### 4.1 API Resources

Fonte: [Laravel 13 — Eloquent: API Resources](https://laravel.com/framework/docs/13.x/eloquent-resources), consultado 2026-10-09. O doc mostra `make:resource`, `JsonResource` e `toArray`, e o atributo `#[PreserveKeys]` para coleções que preservam chaves.

Regras:

- **Um Resource por tela ou uso**, não um Resource gordo para o modelo inteiro. Exemplo: `CursoCatalogoResource` (id, título, capa, professor) e `CursoDetalheResource` (além dos anteriores, ementa e módulos). Um único `CursoResource` com todos os campos é a principal causa de over-fetching.
- **Campos de relação só com carregamento explícito.** `whenLoaded('professor')` (não verificado nesta rodada: confirmar na doc de Resources) evita N+1 e campo vazio.
- **Nenhum campo "para o futuro".** Campo sem consumidor sai.

### 4.2 Sparse fieldsets

A doc do Laravel 13 tem a seção "Sparse Fieldsets and Includes", dentro do suporte a JSON:API ([Laravel — API Resources](https://laravel.com/framework/docs/13.x/eloquent-resources), consultado 2026-10-09).

**Recomendação: não usar.** (inferência.) Motivos:

- É um mecanismo de JSON:API. Não é necessário para o contrato simples do projeto.
- Exige parâmetros `fields[tipo]=...` na requisição. Esses parâmetros iriam para a URL da SPA, que já carrega o estado de listagem (seção 2). Misturar os dois polui a URL.
- O objetivo (não devolver campos que ninguém usa) é atendido pelo Resource por tela.

### 4.3 Checklist de PR

Incluir no template de PR que altera endpoint:

- [ ] Cada campo novo em Resource tem ao menos um consumidor no front (componente ou tipo que o lê).
- [ ] Nenhum campo removido do front continua no Resource. Se o campo foi removido do componente, removê-lo do Resource no mesmo PR.
- [ ] Listagem nova usa `paginate` ou `cursorPaginate` e valida `page`/`per_page` no FormRequest.
- [ ] Teste de contrato atualizado.

### 4.4 Verificação

- **Teste de contrato no back** (Laravel feature test): `assertJsonStructure` com a lista exata de chaves do Resource. Se alguém adicionar campo, o teste falha e obriga a revisão. (inferência: método de `TestResponse` do Laravel; confirmar assinatura na versão 13.)
- **Revisão com consumidor no front:** o revisor abre o componente que consome o endpoint e confirma que cada campo do JSON aparece nele. É manual, mas barato.
- **Tipos TypeScript gerados a partir do contrato** (não pesquisado nesta rodada) podem apoiar a checagem. Não é obrigatório.

---

## 5. Decisões recomendadas (base para ADR-0008 e ADR-0009)

### 5.1 ADR-0008 — Sessão e autenticação

| Decisão recomendada | Alternativa descartada | Motivo |
|---|---|---|
| JWT de acesso em cookie `__Host-access`, `HttpOnly`, `Secure`, `SameSite=Strict`, `Path=/` | Token em `localStorage` | JavaScript lê o token em `localStorage`, então XSS o rouba. `HttpOnly` impede isso (MDN) |
| `php-open-source-saver/jwt-auth` como guard | `lcobucci/jwt` puro | Guard, TTL e blacklist prontos. `lcobucci/jwt` exige implementar tudo isso (confirmar suporte ao Laravel 13) |
| Access de 1 h + refresh opaco rotacionado | Access de 1 h sem refresh (novo login a cada hora) | Atende "manter conectado" sem refresh de longa duração em JWT |
| Refresh com detecção de reuso revogando a família | Rotação sem detecção | Reuso de token já usado indica roubo. RFC 9700, seção 4.14 |
| Refresh em `__Host-refresh` com `Path=/api/v1/auth/refresh` e `Max-Age=2592000` quando "manter conectado" | Cookie sem `Max-Age` para todos | `Max-Age` evita erro de relógio. `Path` reduz envio, sem ser medida de segurança (MDN) |
| Blacklist em Redis por `jti`, com TTL igual ao tempo restante | Logout só apagando cookie | Cookie apagado não invalida um token copiado. Blacklist limitada a 1 h |
| CSRF por dupla submissão assinada (`__Host-csrf` + `X-CSRF-Token`) e validação de `Origin` | Confiar só em `SameSite` | OWASP: SameSite é defesa em profundidade, não substitui token |
| App e API no mesmo domínio registrável (ex.: `app.` e `api.` do mesmo domínio) | Domínios diferentes com `SameSite=None` | Cookie third-party é bloqueado por navegadores e exige `SameSite=None` |
| CORS com `supports_credentials=true` e origem exata | `allowed_origins` com `*` | Credenciais não funcionam com `*`, e `*` abriria a API a qualquer origem |
| `GET /api/v1/auth/me` como fonte do estado logado | Ler cookie no cliente | Cookie é HttpOnly, o JS não lê. A API é o único ponto de verdade |

### 5.2 ADR-0009 — Listagens, paginação e contrato

| Decisão recomendada | Alternativa descartada | Motivo |
|---|---|---|
| Página, filtros e ordenação na URL, com `queryKey` contendo os parâmetros normalizados | Estado em store global (Zustand, Context) | Decisão 2: F5 e link compartilhado. Store global se perde no reload e não vai na URL |
| `placeholderData: keepPreviousData` em toda listagem | Lista que some a cada página | Evita piscar. Doc do TanStack Query |
| Parâmetros com valor default fora da URL | Todos os parâmetros sempre explícitos | URL canônica. Um estado, uma URL |
| Mudança de filtro volta à página 1 | Manter a página atual | Página pode não existir no novo filtro |
| `paginate` para catálogo, meus cursos, admin e avaliações | `simplePaginate` em todas | UI precisa de número de páginas e de pular para página N |
| `cursorPaginate` para mensagens do tutor | `paginate` com OFFSET | Histórico com escrita frequente repete ou pula itens com OFFSET (doc do Laravel). Exceção à decisão 2, a confirmar |
| `per_page` padrão 20, máximo 100, validado no FormRequest | Sem limite de `per_page` | Limite evita devolver milhares de linhas. Over-fetching |
| Ordenação sempre com desempate por `id` | Ordenar só pela coluna de interesse | Sem desempate, páginas repetem ou pulam registros com valores iguais |
| Um API Resource por tela ou uso | Um `Resource` com todos os campos do modelo | Decisão 4. Campo sem consumidor fica fora do contrato |
| Sem sparse fieldsets | `fields[tipo]=` na requisição | Parâmetro extra polui a URL que já carrega o estado de listagem |
| Checklist de PR + teste de contrato | Confiar só na revisão | Torna o over-fetching visível em cada PR |

---

## 6. Pontos em aberto

- Confirmar suporte do `php-open-source-saver/jwt-auth` ao Laravel 13 no `composer.json` antes de fechar o ADR-0008.
- Reconciliar o TTL de 1 h com a nota "TTL curto 15-30 min" do Vault (não lido nesta rodada).
- Confirmar a exceção de cursor nas mensagens do tutor (conflito com decisão 2).
- Confirmar se `*.vercel.app` ou outro domínio de hospedagem coloca app e API no mesmo site.
- Não pesquisado nesta rodada: zod, debounce (valor de 300 ms), `whenLoaded`, formato exato de `links`/`meta` em coleções paginadas e assinatura de `assertJsonStructure` no Laravel 13.

---

## Fontes consultadas

Todas consultadas em 2026-10-09.

- Laravel 13 — release notes: https://laravel.com/framework/docs/releases
- Laravel News — Laravel 13 released: https://laravel-news.com/laravel-13-released
- Laravel 13 — Database: Pagination: https://laravel.com/framework/docs/pagination
- Laravel 13 — Eloquent: API Resources: https://laravel.com/framework/docs/13.x/eloquent-resources
- Laravel Sanctum — SPA authentication: https://laravel.com/framework/docs/sanctum
- php-open-source-saver/jwt-auth — repositório: https://github.com/PHP-Open-Source-Saver/jwt-auth
- php-open-source-saver/jwt-auth — documentação: https://laravel-jwt-auth.readthedocs.io
- lcobucci/jwt — repositório: https://github.com/lcobucci/jwt
- RFC 9700 — OAuth 2.0 Security Best Current Practice: https://www.rfc-editor.org/info/rfc9700/
- OAuth 2.0 Best Current Practice (resumo): https://oauth.net/2/oauth-best-practice/
- MDN — Using HTTP cookies: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies
- OWASP — CSRF Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- OWASP — Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- TanStack Query — Paginated Queries: https://tanstack.com/query/latest/docs/framework/react/guides/paginated-queries
- TanStack Query — discussão 6460: https://github.com/TanStack/query/discussions/6460
- Next.js — missing-suspense-with-csr-bailout: https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout

---
id: pesquisa-hospedagem-e-jwt
titulo: "Pesquisa — hospedagem (Vercel, Railway, Cloudflare R2) e JWT RS256 no Laravel 13"
tipo: pesquisa
status: referência da ADR-0010 e da atualização da ADR-0008
atualizado: 2026-10-09
---
# Pesquisa — hospedagem e JWT RS256

Base para a [ADR-0010](../adr/0010-hospedagem-e-armazenamento.md) e para a atualização da [ADR-0008](../adr/0008-sessao-jwt-em-cookie.md). Pesquisa feita em 09/10/2026 nas páginas oficiais listadas em cada seção. Preços e limites mudam; onde não houve fonte confiável, o texto diz **a confirmar**.

## 1. Biblioteca JWT: `php-open-source-saver/jwt-auth`

- Fork mantido do `tymon/jwt-auth`. Versão 2.9.3 (21/08/2026), requer `illuminate/console` ^12 ou ^13, portanto suporta Laravel 13. Cerca de 12,9 milhões de instalações. Fonte: <https://packagist.org/packages/php-open-source-saver/jwt-auth>.
- Assinatura assimétrica: configurar `JWT_ALGO=RS256` e as chaves `JWT_PRIVATE_KEY` e `JWT_PUBLIC_KEY` (caminho ou conteúdo). O comando `jwt:secret` gera apenas segredo HS; o par RSA é gerado com `openssl genrsa` e `openssl rsa -pubout`. **A confirmar** na documentação (<https://laravel-jwt-auth.readthedocs.io>, página de configuração ainda marcada como «Coming soon») e em teste no projeto.
- Publicação da chave pública aos microsserviços: arquivo montado ou variável de ambiente. JWKS e rotação de chaves: **a confirmar**; a biblioteca não documenta rotação, então a troca de chave exige janela com duas chaves públicas aceitas pelos validadores.

## 2. Railway (back-end Laravel, `ai-service`, `media-service`, bancos)

- Planos: Hobby a US$ 5/mês com US$ 5 de uso incluído e consumo excedente cobrado à parte; Pro a US$ 20/mês; gratuito apenas como trial de 30 dias (US$ 5 em créditos), depois recursos limitados (até 1 vCPU e 0,5 GB de RAM). Fonte oficial: <https://railway.com/pricing>.
- Bancos: templates oficiais para PostgreSQL, MySQL e Redis, privados por padrão (acesso público em Settings > Networking). Backups e PITR (Postgres e MySQL) são ligados pelo usuário; atualização de versão maior é manual. Fontes: <https://docs.railway.com/databases>, <https://docs.railway.com/databases/postgresql>, <https://docs.railway.com/databases/reference>, <https://docs.railway.com/cli/deploy>.
- `pgvector` e RabbitMQ: não há template oficial confirmado; exigem imagem ou template da comunidade (`pgvector/pgvector:pg16` como imagem Docker própria). **A confirmar** antes de implementar.
- Consequência: o custo deixa de ser fixo (VPS) e passa a ser por uso; com 5 serviços e 3 bancos o consumo pode passar do crédito do Hobby. Estimativa de custo mensal: **a confirmar** após o primeiro deploy de teste.

## 3. Cloudflare R2 (vídeos, imagens e arquivos)

- Sem taxa de saída (egress). Camada gratuita: 10 GB-mês, 1 milhão de operações Classe A e 10 milhões Classe B por mês. Acima disso, Standard a US$ 0,015/GB-mês. Fontes: <https://developers.cloudflare.com/r2/pricing/>, <https://www.cloudflare.com/products/r2/>.
- URLs assinadas (API S3; GET, PUT, HEAD, DELETE; validade de 1 s a 7 dias) funcionam apenas no domínio `<ACCOUNT_ID>.r2.cloudflarestorage.com`, **não** em domínio customizado. Fonte: <https://developers.cloudflare.com/r2/api/s3/presigned-urls/>.
- CORS no bucket é obrigatório para upload e leitura pelo navegador (origens, métodos PUT/GET, cabeçalho `Content-Type`, `ExposeHeaders: ETag`, `MaxAgeSeconds`). URL expirada responde 403 sem cabeçalhos CORS. Fonte: <https://developers.cloudflare.com/r2/buckets/cors/>.
- Upload de até 500 MB por aula (RNF018): PUT único versus multipart e leitura parcial com `Range` para streaming: **a confirmar**. Alternativa mais cara apenas citada: Cloudflare Stream.
- A camada gratuita de 10 GB comporta poucos vídeos; o volume real depende do catálogo e deve ser reavaliado.

## 4. Vercel (front-end Next.js em SPA)

- `rewrites` em `vercel.json` encaminham para origem externa sem mudar a URL do navegador, funcionando como proxy reverso. Exemplo oficial: `/api/:path*` para `https://api.example.com/:path*`. A Vercel repassa `x-forwarded-for`, `x-forwarded-host` e `x-forwarded-proto` e permite um cabeçalho secreto (`x-origin-secret`) para a origem recusar acesso direto. Respostas externas podem ser cacheadas conforme `Cache-Control`; para a API autenticada, desligar com `x-vercel-enable-rewrite-caching: 0`. Fonte: <https://vercel.com/docs/routing/rewrites>.
- Limite de tempo do proxy: 120 s segundo <https://vercel.com/docs/limits> (fontes antigas diziam 30 s; conferir no momento do deploy). Corpo máximo e repasse de `Set-Cookie` com prefixo `__Host-` pelo rewrite: **a confirmar** em teste.
- Upload de vídeo não passa pelo rewrite: o navegador envia direto ao R2 por URL assinada.
- Plano Hobby é de uso não comercial; para uso real do produto, **a confirmar** o plano necessário.

## 5. Domínio e DNS

- Cookie `__Host-` e `SameSite=Strict` (ADR-0008) exigem que o navegador veja um único host. Com o rewrite da Vercel, o navegador fala só com o domínio do front-end, e a API aparece em `/api/*` sob o mesmo host. Alternativa sem `__Host-`: subdomínios do mesmo domínio registrável (`app.` e `api.`) com `Domain=` explícito.
- Domínio: comprar (`.com.br` ou `.com`) ou reaproveitar um existente. **Decisão pendente do Lucas.** Nenhuma compra foi feita. DNS pode ficar na Cloudflare; para o MVP, o domínio padrão da Vercel serve de substituto temporário.

## 6. Resumo das incertezas

| Ponto | Situação |
|---|---|
| `JWT_ALGO=RS256` com a biblioteca | a confirmar em teste |
| Rotação de chaves | sem suporte documentado |
| `pgvector` e RabbitMQ no Railway | a confirmar |
| Custo mensal no Railway | a confirmar |
| Upload de 500 MB no R2 (PUT único ou multipart) | a confirmar |
| `Set-Cookie` `__Host-` através do rewrite | a confirmar |
| Plano da Vercel para uso comercial | a confirmar |
| Domínio | decisão do Lucas |

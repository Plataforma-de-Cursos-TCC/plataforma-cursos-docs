---
id: adr-0009
titulo: "ADR-0009 — Listagens com estado na URL, paginação obrigatória e resposta mínima"
tipo: decisao
decisao: D9
status: aceita
data: 2026-10-09
decisor: Grupo
itens_template: [5, 11]
areas: [A, B, C, D]
relacionados: [adr-0007, adr-0008]
---
# ADR-0009 — Listagens com estado na URL, paginação obrigatória e resposta mínima

- **Status:** aceita · **Data:** 09/10/2026 · **Decisor:** Grupo

## Contexto

- Telas de listagem (catálogo, cursos do instrutor, matrículas, avaliações, usuários, mensagens do Tutor) têm filtros, ordenação e páginas. Se esse estado vive só em memória do componente, o F5 e o botão voltar o perdem e o link não pode ser compartilhado.
- O RNF009 pede desempenho em listagens. Listas sem paginação crescem sem limite e sobrecarregam a API e o MySQL.
- Respostas da API que carregam campos que a tela não usa desperdiçam banda e expõem dados sem necessidade.
- Detalhes, comparações e fontes estão em [sessao-e-listagens.md](../pesquisas/sessao-e-listagens.md).

## Opções consideradas

- **Estado em `useState` ou em store global:** descartado. Perde-se no F5 e não é compartilhável.
- **Estado em `localStorage`:** descartado. Não vai no link e conflita entre abas.
- **Estado na URL (query string) como fonte única, com React Query lendo da URL:** escolhida.
- **Paginação por cursor em todas as listagens:** descartada como regra geral, pois impede mostrar número de páginas. Fica como exceção.
- **Sparse fieldsets ou GraphQL:** descartados pelo custo de complexidade; um API Resource por tela resolve o over-fetching.

## Decisão

1. Filtros, ordenação e página de toda listagem ficam na query string da rota (`?page=2&sort=-createdAt&category=dados`). A URL é a fonte única do estado; o front-end deriva dela a `queryKey` do React Query, normalizada (ordem das chaves estável, valores padrão omitidos).
2. A paginação nas listagens usa `placeholderData: keepPreviousData` para evitar piscar a tela. Mudar qualquer filtro ou ordenação volta à página 1. A busca por texto usa debounce antes de escrever na URL.
3. **Toda listagem é paginada.** O back-end usa `paginate` quando a tela mostra o número de páginas. `cursorPaginate` é permitida apenas para fluxos de rolagem infinita, como o histórico de mensagens do Tutor, mediante registro da exceção no TDD.
4. Parâmetros padronizados: `page` (padrão 1), `per_page` (padrão 20, máximo 100, validado em `FormRequest`), `sort` (lista branca de campos, prefixo `-` para decrescente) e filtros por nome. Toda ordenação tem desempate por `id`. O envelope segue o formato do TDD, seção 3.2.
5. **Resposta mínima:** cada tela de listagem tem seu API Resource, que devolve somente os campos que a tela usa. Nada que o back-end devolve fica sem uso no front-end. Isso entra no checklist de PR.

## Consequências

- Links de listagem são compartilháveis e sobrevivem ao F5 e ao botão voltar.
- Todo endpoint de listagem novo precisa de FormRequest com limites, lista branca de ordenação e API Resource dedicado; o TDD (seção 3.2 e tabela de endpoints) passa a documentar `page`, `per_page`, `sort` e filtros.
- O RNF009 é atendido pela combinação de paginação, índices nas colunas de filtro e ordenação e cache no Redis, sem criar RNF novo.
- Mais de um API Resource por entidade aumenta o número de classes; o custo é aceito em troca de payload previsível.

---

## Ligações

- **Pesquisa:** [sessao-e-listagens.md](../pesquisas/sessao-e-listagens.md)
- **TDD (paginação):** [tdd.md](../tdd.md) · **Stack:** [ADR-0007](0007-stack-e-bancos.md) · **Sessão:** [ADR-0008](0008-sessao-jwt-em-cookie.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

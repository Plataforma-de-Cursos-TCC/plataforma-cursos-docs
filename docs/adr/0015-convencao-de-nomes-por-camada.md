---
id: adr-0015
titulo: "ADR-0015 — Convenção de nomes por camada: banco em snake_case, API e código em camelCase"
tipo: decisao
decisao: D15
status: aceita
data: 2026-11-20
decisor: Grupo
itens_template: [12, 13, 14, 15]
areas: [A, B, C, D]
relacionados: [adr-0007, adr-0009]
---
# ADR-0015 — Convenção de nomes por camada

- **Status:** aceita · **Data:** 20/11/2026 · **Decisor:** Grupo · **Substitui:** o nome `per_page` do item 4 da [ADR-0009](0009-listagens-na-url-e-paginacao.md)

## Contexto

- Os documentos misturavam convenções: a ADR-0009 e o TDD usavam `per_page`; os itens 12 usavam colunas em camelCase (`videoKey`, `courseId`); o dashboard misturava português e inglês (`inicio`, `curso_id`).
- [Fato] O Eloquent usa snake_case nas colunas (`created_at`, `deleted_at`, chaves estrangeiras `course_id`) e o paginator do Laravel serializa em snake_case (`per_page`, `current_page`).
- [Inferência] Para a API JSON, a especificação JSON:API e o guia de estilo JSON do Google recomendam camelCase nos nomes de membros, que também é o padrão do front-end em TypeScript.

## Opções consideradas

- **snake_case em tudo:** descartada. A API ficaria fora do padrão do front-end.
- **camelCase em tudo, inclusive no banco:** descartada. Briga com as convenções do Eloquent (`created_at`, `deleted_at`, chaves estrangeiras).
- **Cada camada no seu padrão, com conversão na fronteira:** escolhida.

## Decisão

1. **Banco (item 12):** tabelas e colunas em inglês e snake_case (`course_id`, `video_key`, `created_at`, `deleted_at`).
2. **API (query string, corpo e resposta JSON):** inglês e camelCase (`page`, `perPage`, `sort`, `startDate`, `endDate`, `courseId`, `groupBy`). O envelope de paginação também: `meta.currentPage`, `meta.perPage`, `meta.total`, `meta.lastPage`.
3. **Código PHP e TypeScript (itens 13 e 14):** inglês, classes em PascalCase, métodos e propriedades em camelCase.
4. A conversão fica na fronteira: o `FormRequest` valida os nomes em camelCase e o DTO os recebe; o API Resource escreve a resposta em camelCase. Os Models continuam com os nomes das colunas.
5. Valores enumerados são gravados em inglês (ex.: `draft`, `published`, `active`) e o rótulo em pt-BR fica no mapeamento do item 12.

## Consequências

- O item 4 da ADR-0009 continua valendo (padrão 20, máximo 100, validado no `FormRequest`), mas com o nome `perPage`. Fora de 1 a 100, a resposta é 422 `VALIDATION_FAILED` com o campo em `fields`.
- Os itens 12 das quatro áreas e os `.drawio` relacionais passam as colunas para snake_case. Os itens 13 a 15 ficam em camelCase.
- O TDD (seção 3.2 e tabela de rotas) e os casos de teste usam os nomes da API.

---

## Ligações

- **Listagens:** [ADR-0009](0009-listagens-na-url-e-paginacao.md) · **Pesquisa:** [sessao-e-listagens.md](../pesquisas/sessao-e-listagens.md) · **TDD:** [tdd.md](../tdd.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

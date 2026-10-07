---
id: adr-0001
titulo: "ADR-0001 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área"
tipo: decisao
decisao: D1
status: aceita
data: 2026-10-07
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [6, 7, 8, 9, 10]
areas: [A, B, C, D]
relacionados: [adr-0006]
---
# ADR-0001 — Mínimo de 4 por integrante, sem máximo; numeração provisória por área

- **Status:** aceita · **Data:** 07/10/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- A rubrica do RA1 pede, nos itens que dependem da quantidade de integrantes (6, 7, 8 e 10), **no mínimo** 4 itens por integrante. Com 4 integrantes, o mínimo é 16. Não há máximo.
- Faixas fixas por área (A = RF001 a RF004, B = RF005 a RF008…) transformam o mínimo em máximo: quem precisa de um quinto RF quebra a numeração das outras áreas.
- O documento final precisa de numeração sequencial e sem lacunas.

## Opções consideradas

- **(a)** Numeração fixa por área e limite de 4 itens.
- **(b)** Faixas maiores por área (ex.: A = RF001 a RF010), aceitando lacunas.
- **(c)** Numeração **provisória por área** durante a escrita e **renumeração sequencial única** antes da revisão final.

## Decisão

**(c)**:

1. **Mínimo de 4 por integrante, sem máximo,** nos itens 6, 7, 8 e 10.
2. **IDs provisórios por área** durante a escrita:

   | Item | Formato provisório | Exemplo |
   |---|---|---|
   | 6 — RFs | `RF-<área><n>` | RF-A1, RF-D5 |
   | 7 — Estórias | `US-<área><n>`, com o mesmo número do RF | US-D5 ↔ RF-D5 |
   | 8 — RNFs | `RNF-<área><n>` | RNF-B1 |
   | 9 e 10 — Casos de uso | `UC-<área><n>` | UC-C2 |

3. **Renumeração única** no início da revisão cruzada, com todas as áreas na `main`: áreas na ordem A, B, C, D e, dentro de cada área, na ordem do arquivo. RF-A1… vira RF001…; cada estória recebe o número do seu RF (US001…); RNF001…; UC001…. A correspondência provisório → final fica em `entregas/ra1-renumeracao.md`.
4. Um RF extra pode ser coberto por um caso de uso já existente, por «include» ou «extend», sem exigir especificação nova.

## Consequências

- Cada RF a mais exige uma estória com pelo menos 2 critérios de aceite ([ADR-0002](0002-formato-de-estoria-e-criterios.md)).
- Até a renumeração, as referências cruzadas (estória → RF, caso de uso → RF) usam os IDs provisórios.
- As issues citam a área e o mínimo, não faixas de números.

---

## Ligações

- **Itens da especificação:** itens 6, 7, 8, 9 e 10 em [especificacao/](../../especificacao/)
- **Plano e critérios:** [ra1-tarefas](../../entregas/ra1-tarefas.md), [ra1-criterios-de-aceite](../../entregas/ra1-criterios-de-aceite.md)
- **Outras decisões:** [D6](0006-divisao-por-areas.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

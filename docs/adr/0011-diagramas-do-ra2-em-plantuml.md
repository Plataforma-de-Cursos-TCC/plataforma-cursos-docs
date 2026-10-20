---
id: adr-0011
titulo: "ADR-0011 — Diagramas do RA2 em PlantUML"
tipo: decisao
decisao: D11
status: aceita
data: 2026-10-20
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [12, 13, 14]
areas: [A, B, C, D]
relacionados: [adr-0004]
---
# ADR-0011 — Diagramas do RA2 em PlantUML

- **Status:** aceita · **Data:** 20/10/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- A [ADR-0004](0004-diagramas-como-codigo.md) cobre os itens 4, 9 e 11. Os itens 12 (modelo lógico), 13 (diagrama de classes) e 14 (diagramas de sequência) do RA2 não tinham decisão.
- Os rascunhos atuais estão em Mermaid, em `docs/tdd.md` e `docs/ssd/`. O Mermaid não vai ao PDF (ADR-0004) e não desenha a notação que a disciplina cobra: no item 12, a coluna de PK/FK e os campos obrigatórios em negrito (TE4); no item 13, visibilidade e multiplicidade (TE5_1); no item 14, estereótipos boundary, control e entity e os fragmentos `alt` e `opt` (TE5_2).

## Opções consideradas

- **(a)** Manter Mermaid e exportar PNG com `mmdc` (não instalado, notação limitada).
- **(b)** Imagens exportadas de ferramenta gráfica.
- **(c)** **PlantUML nos itens 12, 13 e 14**, mesmo padrão do item 9.

## Decisão

**(c)**:

- Um `.puml` por diagrama em `especificacao/diagramas/`, com o PNG gerado ao lado e versionado, nunca editado à mão: `12-modelo-de-dados-area-a.puml`, `13-classes-area-a.puml`, `14-sequencia-uc005.puml` e assim por diante.
- O Mermaid de `docs/tdd.md` e `docs/ssd/` continua como apoio de leitura, fora do PDF. Em divergência, vale o `.puml`.
- Item 15 (casos de teste) não leva diagrama: é tabela Markdown no padrão do TE6.

## Consequências

- Todo diagrama do RA2 tem fonte versionada e revisada por PR.
- Para regerar: `PLANTUML_LIMIT_SIZE=8192 plantuml -tpng <arquivo>.puml` (sem o limite maior o PlantUML corta a imagem em 4096 px), dentro de `especificacao/diagramas/`.
- A ADR-0004 continua valendo para os itens 4, 9 e 11.

---

## Ligações

- **Itens da especificação:** itens 12 a 14 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D4](0004-diagramas-como-codigo.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

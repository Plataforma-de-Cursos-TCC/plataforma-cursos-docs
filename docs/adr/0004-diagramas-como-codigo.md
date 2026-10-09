---
id: adr-0004
titulo: "ADR-0004 — Diagramas como código"
tipo: decisao
decisao: D4
status: aceita
data: 2026-10-08
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [4, 5, 9, 10, 11]
areas: [A, B, C, D]
relacionados: [adr-0003]
---
# ADR-0004 — Diagramas como código

- **Status:** aceita · **Data:** 08/10/2026 (revisão da versão de 07/10/2026) · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- O documento tem diagrama de processo (item 4), de casos de uso (item 9) e de atividades (item 11).
- Diagramas em imagem não mostram diferença no PR, não se revisam linha a linha e se perdem entre versões.
- A versão de 07/10/2026 usava Mermaid nos três. O Mermaid não desenha a notação que a disciplina cobra: no item 4 não há BPMN 2.0 (gateway com "+", pool e lanes), no item 9 não há boneco, elipse nem generalização de atores, e no item 11 as raias e guardas ficam fora do padrão UML.

## Opções consideradas

- **(a)** Imagens exportadas de ferramenta gráfica (draw.io, Lucidchart).
- **(b)** Mermaid em todos os diagramas.
- **(c)** **Diagramas como código, com a ferramenta que desenha a notação exigida:** BPMN 2.0 no item 4 e PlantUML nos itens 9 e 11.

## Decisão

**(c)**:

- **Item 4:** BPMN 2.0 em `especificacao/diagramas/04-mapeamento-de-negocios.bpmn`, com diagrama (DI), editável no bpmn.io ou no Camunda Modeler.
- **Itens 9 e 11:** PlantUML no item 9 (`especificacao/diagramas/09-casos-de-uso.puml`); no item 11, script Python determinístico (`scripts/gen_activity_diagram.py`) gerando SVG e PNG com raias horizontais nativas e controle ortogonal de arestas (os testes anteriores com PlantUML, Mermaid e Graphviz dot ficam preservados em `11-atividades.puml` e `11-atividades.dot` como registro).
- **Mermaid** fica só nos documentos de apoio em `docs/` (fora do PDF do RA1).
- A imagem PNG usada no documento é gerada a partir do código e versionada ao lado da fonte, nunca editada à mão.

## Consequências

- Todo diagrama tem fonte versionada e revisada por PR.
- Para regerar: `plantuml -tpng <arquivo>.puml`; o `.bpmn` é renderizado com bpmn-js; o item 11 é regerado com `python3 scripts/gen_activity_diagram.py`.
- O sentido do «extend» segue a [ADR-0003](0003-extend-no-sentido-do-te3-3.md).

---

## Ligações

- **Itens da especificação:** itens 4, 9 e 11 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D3](0003-extend-no-sentido-do-te3-3.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

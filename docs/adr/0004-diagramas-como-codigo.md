---
id: adr-0004
titulo: "ADR-0004 — Diagramas como código"
tipo: decisao
decisao: D4
status: aceita
data: 2026-10-07
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [4, 5, 9, 10]
areas: [A, B, C, D]
relacionados: [adr-0003]
---
# ADR-0004 — Diagramas como código

- **Status:** aceita · **Data:** 07/10/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- O documento tem diagrama de processo (item 4), de contexto ou atores (item 5) e de casos de uso (itens 9 e 10).
- Diagramas em imagem não mostram diferença no PR, não se revisam linha a linha e se perdem entre versões. As versões anteriores já usavam Mermaid.

## Opções consideradas

- **(a)** Imagens exportadas de ferramenta gráfica (draw.io, Lucidchart).
- **(b)** **Diagramas como código**: Mermaid em geral e BPMN 2.0 (`.bpmn`) para o processo.

## Decisão

**(b)**:

- **Mermaid** em arquivo `.mmd` em `especificacao/diagramas/` ou em bloco ```mermaid no próprio Markdown.
- **BPMN 2.0** em arquivo `.bpmn` no item 4, editável no bpmn.io ou no Camunda Modeler.
- A imagem (PNG ou SVG) usada no `.docx` final é gerada a partir do código, nunca editada à mão.

## Consequências

- Todo diagrama tem fonte versionada e revisada por PR.
- O sentido do «extend» segue a [ADR-0003](0003-extend-no-sentido-do-te3-3.md).

---

## Ligações

- **Itens da especificação:** itens 4, 5, 9 e 10 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D3](0003-extend-no-sentido-do-te3-3.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

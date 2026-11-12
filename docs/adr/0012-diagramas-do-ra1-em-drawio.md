---
id: adr-0012
titulo: "ADR-0012 — Diagramas do RA1 em draw.io"
tipo: decisao
decisao: D4
status: aceita
data: 2026-11-12
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [4, 9, 11]
areas: [A, B, C, D]
relacionados: [adr-0003, adr-0004]
---
# ADR-0012 — Diagramas do RA1 em draw.io

- **Status:** aceita · **Data:** 12/11/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski · **Substitui:** [ADR-0004](0004-diagramas-como-codigo.md)

## Contexto

- A [ADR-0004](0004-diagramas-como-codigo.md) definiu BPMN 2.0 (`.bpmn`) no item 4, PlantUML no item 9 e um script Python no item 11.
- O leiaute automático dessas ferramentas não deixa controlar a posição de cada elemento: sobram cruzamentos de linhas, rótulos encostados em arestas e proporções ruins na página do documento.
- Eram três ferramentas e três formas de regerar a imagem (bpmn-js, PlantUML e script com Chrome headless), o que dificulta a manutenção pelo grupo.
- O draw.io grava o diagrama em XML de texto e exporta a imagem pela linha de comando, então a fonte continua versionada e revisável por PR.

## Opções consideradas

- **(a)** Manter a ADR-0004 e ajustar o leiaute dentro do limite de cada ferramenta.
- **(b)** **draw.io nos três diagramas do RA1**, com fonte `.drawio` em XML não comprimido e PNG exportado da fonte.
- **(c)** Ferramenta gráfica sem fonte de texto (imagem solta).

## Decisão

**(b)**:

- **Itens 4, 9 e 11:** fonte em `especificacao/diagramas/04-mapeamento-de-negocios.drawio`, `09-casos-de-uso.drawio` e `11-atividades.drawio`, em XML não comprimido.
- **Notação:** continua a exigida pela disciplina: BPMN 2.0 no item 4 (pool, raias, gateways e eventos), UML de casos de uso no item 9 e UML de atividades com raias no item 11. O sentido do «extend» segue a [ADR-0003](0003-extend-no-sentido-do-te3-3.md).
- **Padrão de desenho:** grade de 10 px, arestas ortogonais com pontos de saída e entrada fixos, Helvetica 12 (título 14 em negrito), traço de 1,5 px, preto e branco com cinza `#F2F2F2` no cabeçalho das raias, sem cruzamento de linhas.
- **Imagem:** o PNG do documento é exportado da fonte e versionado ao lado dela, nunca editado à mão.
- **Fontes antigas** (`.bpmn`, `.puml`, `.dot`, `.svg` e `scripts/gen_activity_diagram.py`) saem do repositório; ficam no histórico do Git.
- **Diagramas do RA2 (itens 12 a 14):** fora desta decisão; seguem a ADR-0011 (PlantUML).

## Consequências

- Uma ferramenta só para os três diagramas do RA1, com posição de cada elemento sob controle.
- Para regerar: `draw.io -x -f png -s 2 -b 20 -o <arquivo>.png <arquivo>.drawio` (no macOS, o binário fica em `/Applications/draw.io.app/Contents/MacOS/draw.io`).
- O diff do `.drawio` mostra coordenadas e estilos, menos legível que o do PlantUML; a revisão do PR passa a olhar também o PNG.
- Mudança de conteúdo no diagrama é feita na fonte `.drawio`, com o PNG reexportado no mesmo PR.

---

## Ligações

- **Itens da especificação:** [item 4](../../especificacao/04-mapeamento-de-negocios.md), [item 9](../../especificacao/09-diagrama-geral-de-casos-de-uso.md) e [item 11](../../especificacao/11-diagrama-de-atividades.md)
- **Outras decisões:** [D3](0003-extend-no-sentido-do-te3-3.md), [ADR-0004](0004-diagramas-como-codigo.md) (substituída)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

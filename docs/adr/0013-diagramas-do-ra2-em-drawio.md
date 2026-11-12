---
id: adr-0013
titulo: "ADR-0013 — Diagramas do RA2 em draw.io"
tipo: decisao
decisao: D4
status: aceita
data: 2026-11-12
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [12, 13, 14]
areas: [A, B, C, D]
relacionados: [adr-0011, adr-0012]
---
# ADR-0013 — Diagramas do RA2 em draw.io

- **Status:** aceita · **Data:** 12/11/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski · **Substitui:** [ADR-0011](0011-diagramas-do-ra2-em-plantuml.md)

## Contexto

- A [ADR-0011](0011-diagramas-do-ra2-em-plantuml.md) definiu PlantUML nos itens 12 (modelo de dados), 13 (classes) e 14 (sequência). A [ADR-0012](0012-diagramas-do-ra1-em-drawio.md) levou os diagramas do RA1 para o draw.io, porque o leiaute automático do PlantUML não deixa controlar a posição dos elementos.
- Os diagramas do RA2 têm o mesmo problema: linhas cruzadas, rótulos encostados em arestas e imagens com proporção ruim na página do documento.
- Duas ferramentas para o mesmo documento (draw.io no RA1, PlantUML no RA2) obrigam o grupo a manter dois fluxos de regeração da imagem.
- A análise do professor sobre o item 14 apontou o cancelamento desenhado em `opt`, com o fluxo seguindo depois dele. Corrigir isso é uma redação de diagrama que cabe melhor na versão nova do que no `.puml`.

## Opções consideradas

- **(a)** Manter o PlantUML nos itens 12 a 14 (ADR-0011).
- **(b)** **draw.io nos itens 12 a 14**, mesmo padrão da ADR-0012: fonte `.drawio` em XML não comprimido e PNG exportado da fonte.
- **(c)** Ferramenta gráfica sem fonte de texto (imagem solta).

## Decisão

**(b)**:

- Um `.drawio` por diagrama em `especificacao/diagramas/`, com o PNG exportado ao lado e versionado, nunca editado à mão: `12-modelo-de-dados-area-a.drawio`, `13-classes-area-a-negocial.drawio`, `14-sequencia-uc005.drawio` e assim por diante.
- **Notação:** continua a exigida pela disciplina. Item 12: coluna de PK/FK e campos obrigatórios em negrito (TE4). Item 13: visibilidade e multiplicidade (TE5_1). Item 14: estereótipos boundary, control e entity e fragmentos `alt`, `opt` e `loop` (TE5_2).
- **Padrão de desenho:** o da [ADR-0012](0012-diagramas-do-ra1-em-drawio.md): grade de 10 px, arestas ortogonais com pontos de saída e entrada fixos, Helvetica 12, traço de 1,5 px, preto e branco, sem cruzamento de linhas.
- **Fragmentos do item 14:** cancelar e confirmar são `alt` (cancelar encerra o diagrama), nunca `opt` seguido de continuação.
- **Fontes antigas:** os `.puml` saem do repositório e ficam no histórico do Git.
- O Mermaid de `docs/tdd.md` e `docs/ssd/` continua como apoio de leitura, fora do PDF. Em divergência, vale o `.drawio`.
- Item 15 (casos de teste) não leva diagrama: é tabela Markdown no padrão do TE6.

## Consequências

- Uma ferramenta só para todos os diagramas do documento, com a posição de cada elemento sob controle.
- Para regerar: `draw.io -x -f png -s 2 -b 20 -o <arquivo>.png <arquivo>.drawio` (no macOS, o binário fica em `/Applications/draw.io.app/Contents/MacOS/draw.io`).
- O diff do `.drawio` mostra coordenadas e estilos, menos legível que o do PlantUML; a revisão do PR passa a olhar também o PNG.
- Os integrantes das Áreas B, C e D entregam os diagramas em `.drawio`, tomando a Área A como modelo.

---

## Ligações

- **Itens da especificação:** itens 12 a 14 em [especificacao/](../../especificacao/)
- **Outras decisões:** [ADR-0011](0011-diagramas-do-ra2-em-plantuml.md) (substituída), [ADR-0012](0012-diagramas-do-ra1-em-drawio.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

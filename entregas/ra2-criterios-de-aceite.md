---
id: ra2-criterios-de-aceite
titulo: "Critérios de aceite do RA2 (itens 12 a 15)"
tipo: processo
status: rascunho, aguardando conferência do enunciado no Canvas
atualizado: 2026-10-16
relacionados: [ra2-tarefas, ra1-criterios-de-aceite]
---

# Critérios de Aceite do RA2 (itens 12 a 15)

> Derivados do plano de ensino (TE4 a TE6). Conferir pesos e rubrica na página da tarefa do Canvas antes da entrega, como foi feito no RA1. Evidência de cada critério: arquivo e seção.

## Item 12 — Modelo lógico do banco

- [ ] **C12.1** Diagrama em notação UML, perspectiva relacional.
- [ ] **C12.2** Toda tabela tem PK, FKs, tipos e nulabilidade; cardinalidades nos relacionamentos.
- [ ] **C12.3** Extra da equipe (a disciplina não exige): normalizado até 3FN, ou desvio justificado.
- [ ] **C12.4** Cobre as entidades dos itens 6 e 10 (relação Módulo–Quiz resolvida).
- [ ] **C12.5** Pagamento só como registro simulado, sem `payoutInfo` nem dado de cartão.
- [ ] **C12.6** Fonte do diagrama versionada (ADR-0004).

## Item 13 — Diagrama de classes

- [ ] **C13.1** Notação UML correta: atributos, métodos, visibilidade, multiplicidade, associação, composição, herança.
- [ ] **C13.2** Elementos negociais e de implementação presentes e distinguíveis; classes referenciam tipos, nunca o id de uma FK como atributo (regra do TE5_1).
- [ ] **C13.3** Coerente com o item 12 e com atores e glossário do `CONTEXT.md`.
- [ ] **C13.4** Fonte versionada.

## Item 14 — Diagramas de sequência

- [ ] **C14.1** No mínimo 4 casos de uso (meta: pelo menos 1 por integrante).
- [ ] **C14.2** Fluxo principal e `alt` para os fluxos de exceção do item 10.
- [ ] **C14.3** Mensagens usam classes do item 13 e endpoints do TDD; uma arquitetura única.
- [ ] **C14.4** Notação UML correta (lifelines, ativação, `alt`/`opt`/`loop`). Fonte versionada.

## Item 15 — Planilha de casos de teste

- [ ] **C15.1** No mínimo 4 casos de uso (meta: pelo menos 1 por integrante).
- [ ] **C15.2** Cada caso de uso cobre fluxo básico, alternativo e de exceção.
- [ ] **C15.3** Colunas da disciplina: ID, objetivo, pré-condição, passos, dado de entrada, resultado esperado (conferir no enunciado).
- [ ] **C15.4** Rastreável a UC, US e RF.

## Gerais

- [ ] **G.1** Termos e atores idênticos aos do RA1 (K.1).
- [ ] **G.2** Itens 12 a 15 consistentes entre si (tabela, classe, sequência, teste).
- [ ] **G.3** DOCX/PDF gerados por `scripts/build_doc.py` e enviados no Canvas até 28/11.

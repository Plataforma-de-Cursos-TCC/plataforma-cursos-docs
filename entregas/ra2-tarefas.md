---
id: ra2-tarefas
titulo: "Quebra de tarefas: RA2 (Especificação do Projeto, itens 12 a 15)"
tipo: processo
status: rascunho, aguardando aprovação do grupo
atualizado: 2026-10-16
relacionados: [ra2-criterios-de-aceite, ra1-tarefas, contexto, adr-0004, adr-0006]
---

# Quebra de Tarefas: RA2 (itens 12 a 15)

> Entrega da Avaliação do RA 2 em 28/11/2026. Mesmo padrão do [RA1](ra1-tarefas.md): uma tarefa-mãe por item e uma sub-issue por área (A a D), atribuída ao dono da área ([ADR-0006](../docs/adr/0006-divisao-por-areas.md)). Critérios em [ra2-criterios-de-aceite](ra2-criterios-de-aceite.md).

## 1. Itens e prazos

| Item | Entrega | Prazo da tarefa formativa | Mãe | Filhas (A, B, C, D) |
|---|---|---|---|---|
| 12 | Modelo lógico do banco (UML, relacional) | 15/10 (TE4) | #90 | #91, #92, #93, #94 |
| 13 | Diagrama de classes | 29/10 (TE5) | #95 | #96, #97, #98, #99 |
| 14 | Diagramas de sequência, >= 4 casos de uso | 05/11 (TE5) | #100 | #101, #102, #103, #104 |
| 15 | Planilha de casos de teste, >= 4 casos de uso | 12/11 (TE6) | #105 | #106, #107, #108, #109 |
| Geral | Revisão cruzada, DOCX/PDF, envio no Canvas | 28/11 | sem issue; fazer depois das mães | |

## 2. Responsáveis

| Área | Responsável | GitHub |
|---|---|---|
| A Acesso e conta | Lucas Stopinski da Silva | `LucasStop` |
| B Autoria do instrutor | Adrian Antônio de Souza Gomes | `adrian69-droid` |
| C Aprendizagem do aluno | Lucas Bruno e Silva | `Luc-Bruno` |
| D Tutor de IA, analytics e administração | Vinicius Lima Teider | `Teider011` |

## 3. Fontes existentes por item

- 12 e 13: `docs/tdd.md` seção 2 (modelo, dicionário, diagrama de classes); pendências #6 (normalização, Módulo–Quiz).
- 14: `docs/ssd/UC001` a `UC020`; pendência #7 (arquitetura única, `alt` nas exceções).
- 15: `docs/testes/`; pendência #8 (colunas da disciplina, UC011, US017 a US020).
- Decisão a respeitar: pagamento simulado (#51).

## 4. Ordem

12 -> 13 -> 14. O 15 parte dos fluxos do item 10 e roda em paralelo. A mãe de cada item integra as 4 áreas antes de fechar. A revisão cruzada e o envio vêm depois das quatro mães.

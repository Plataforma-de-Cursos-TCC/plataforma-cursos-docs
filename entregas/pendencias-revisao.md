---
id: pendencias-revisao
titulo: "Inventário de Pendências para Revisão do Grupo"
tipo: processo
status: rascunho
atualizado: 2026-10-08
origem: repo grep + _lacunas.md + revisão de conformidade de 08/10/2026
relacionados: [ra1-criterios-de-aceite, ra1-tarefas, propostas-lacunas, contexto, adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006]
---

# Inventário de Pendências para Revisão do Grupo

> Consolida os comentários `<!-- revisar ... -->` que ainda existem em `especificacao/`, as lacunas de `_lacunas.md` e o que a revisão de conformidade de 08/10/2026 encontrou. A versão de 07/10/2026 listava 42 marcações; as de `docs/` (SSD, TDD, testes) e as da declaração de IA já foram resolvidas ou viraram issue do RA2.
>
> **Classificação:**
> - **(M) Mecânico:** resolvível com regra já decidida (ADR ou template), sem deliberação.
> - **(G) Grupo:** exige decisão ou conteúdo novo do grupo.

## 1. O que mudou com as decisões de 08/10/2026

- **Mínimo por integrante:** "4 por integrante" passou a ser meta interna ([ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md)). O mínimo oficial do plano de ensino é de 8 especificações de caso de uso. As marcações "abaixo do mínimo de 4" deixam de bloquear a entrega.
- **Numeração:** fica a da v11 (RF001, US001, RNF001, UC001). Os IDs provisórios (RF-A1, US-A1…) saem do texto, e os IDs novos entram no fim (RF017, RF018, RNF017, RNF018).
- **Pagamento:** a proposta RF-A4 (pagamento simulado na área A) foi descartada, porque repete o RF014, que já está na área C. O pagamento continua simulado, como diz o item 2.
- **«extend»:** a seta sai do caso de uso opcional e aponta para o base ([ADR-0003](../docs/adr/0003-extend-no-sentido-do-te3-3.md)).
- **Diagramas:** item 4 em BPMN 2.0 (`.bpmn`), itens 9 e 11 em PlantUML ([ADR-0004](../docs/adr/0004-diagramas-como-codigo.md)).
- **Protótipos:** cobrem todos os fluxos de cada caso de uso, e não só uma tela.

## 2. Marcações `<!-- revisar -->` que ainda existem

Nenhuma marcação pendente.

## 3. Pendências que não estão em marcação

| Pendência | Tipo | Encaminhamento |
|---|:---:|---|
| Declaração de uso de IA | **G** | Cada integrante confere se a lista de ferramentas cobre o que usou. |
| Documento final (capa, cabeçalho, rodapé, sumário) | **M** | Gerado por script a partir do Template.docx (issue #25). |

## 4. Fora do PDF do RA1 (issues do RA2)

Os pontos abaixo são de `docs/` (TDD, SSD, casos de teste) e ficam para a entrega do RA2, em issues próprias:

- modelo de dados no formato do TE4, normalização e relação Módulo–Quiz (#6);
- SSDs com uma arquitetura única e `alt` nos fluxos de exceção (#7);
- casos de teste com as colunas da disciplina e casos para o UC011 e as US017–US020 (#8);
- entidade `Payment` e campo `payoutInfo`, que contradizem o pagamento simulado (#51).

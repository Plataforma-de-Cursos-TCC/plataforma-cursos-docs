---
id: adr-0001
titulo: "ADR-0001 — Meta interna de 4 por integrante e numeração final da v11"
tipo: decisao
decisao: D1
status: aceita
data: 2026-10-08
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [6, 7, 8, 9, 10]
areas: [A, B, C, D]
relacionados: [adr-0006]
---
# ADR-0001 — Meta interna de 4 por integrante e numeração final da v11

- **Status:** aceita · **Data:** 08/10/2026 (revisão da versão de 07/10/2026) · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- A versão de 07/10/2026 tratava "no mínimo 4 por integrante" como regra da rubrica. O plano de ensino vigente não traz esse número: o mínimo oficial é de 8 especificações de caso de uso no item 10. O "4 por integrante" é uma meta do grupo para dividir o trabalho.
- A mesma versão previa IDs provisórios por área (RF-A1, US-A1, RNF-A1, UC-A1) e uma renumeração sequencial única antes da entrega. A versão 11 do documento (`.docx`) já usa a numeração final RF001…RF016, US001…, RNF001…RNF016 e UC001…UC016, e os textos do repositório citam as duas formas.
- Renumerar tudo de novo a dois dias da entrega muda todos os IDs que o professor já viu na v11.

## Opções consideradas

- **(a)** Renumerar na ordem das áreas A, B, C, D, como previa a versão anterior.
- **(b)** **Manter a numeração da v11** e acrescentar os IDs novos no fim da sequência.

## Decisão

**(b)**:

1. **Meta interna** de 4 RFs, 4 estórias, 4 RNFs e 4 casos de uso por integrante, sem máximo. O mínimo oficial continua sendo o do plano de ensino (8 especificações de caso de uso).
2. **Numeração final da v11:** RF001…RF016, US001…, RNF001…RNF016, UC001…UC016. Os IDs provisórios (RF-A1, US-A1, RNF-A1, UC-A1) saem do texto.
3. **IDs novos no fim da sequência:** RF017, RF018, RNF017, RNF018 e assim por diante, sem reaproveitar número.
4. Um RF extra pode ser coberto por um caso de uso já existente, por «include» ou «extend», sem exigir especificação nova.

## Consequências

- Cada RF tem pelo menos uma estória com pelo menos 2 critérios de aceite ([ADR-0002](0002-formato-de-estoria-e-criterios.md)).
- A área de cada ID fica registrada na rastreabilidade (item 9), e não no próprio ID.

## Adendo (08/10/2026)

Os requisitos RF017 (login), RF018 (controle de acesso), RNF017 (link de recuperação de senha), RNF018 (limite e formato de vídeo de aula) e os casos de uso UC017–UC020 foram adicionados posteriormente, no final da numeração sequencial, sem renumerar os itens anteriores da v11. A inclusão de UC017–UC019 foi registrada pelo PR #58 e UC020 pelo PR #60.

---

## Ligações

- **Itens da especificação:** itens 6, 7, 8, 9 e 10 em [especificacao/](../../especificacao/)
- **Plano e critérios:** [ra1-tarefas](../../entregas/ra1-tarefas.md), [ra1-criterios-de-aceite](../../entregas/ra1-criterios-de-aceite.md)
- **Outras decisões:** [D6](0006-divisao-por-areas.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

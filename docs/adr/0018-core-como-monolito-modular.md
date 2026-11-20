---
id: adr-0018
titulo: "ADR-0018 — Core como monólito modular, sem microsserviços novos"
tipo: decisao
decisao: D18
status: aceita
data: 2026-11-20
decisor: Grupo
itens_template: [11, 13]
areas: [A, B, C, D]
relacionados: [adr-0006, adr-0007, adr-0017]
---
# ADR-0018 — Core como monólito modular, sem microsserviços novos

- **Status:** aceita · **Data:** 20/11/2026 · **Decisor:** Grupo

## Contexto

- O sistema já tem três serviços: o core (API Laravel), o `ai-service` e o `media-service`. Os dois últimos existem por motivo concreto: carga e streaming da IA, e upload de arquivos grandes para o R2.
- O grupo avaliou quebrar o core em mais serviços. Cursos, matrículas, pagamentos e usuários se consultam na mesma operação; separá-los exigiria chamadas por rede, consistência entre bancos e um deploy por serviço.

## Opções consideradas

- **Microsserviço por área (A a D):** descartada. Custo de operação e de consistência alto demais para uma equipe de quatro pessoas, sem ganho de carga.
- **Monólito sem fronteiras internas:** descartada. Mistura o código das áreas e dificulta extrair um módulo depois.
- **Monólito modular:** escolhida.

## Decisão

1. O core é um único deploy Laravel dividido em módulos: Auth (Área A), Authoring (Área B), Learning (Área C), Admin e Analytics (Área D).
2. Cada módulo tem seus Controllers, Services, Repositories e Models. Um módulo usa outro só pelos Services públicos dele, nunca lendo as tabelas do outro diretamente.
3. Os serviços continuam três: core, `ai-service` e `media-service`. Um módulo só vira serviço próprio se tiver carga ou ritmo de deploy muito diferente dos outros, registrado em ADR nova.

## Consequências

- O diagrama de classes (item 13) indica o módulo de cada classe, como já faz com "[Área X]".
- Uma transação de banco cobre a matrícula e o pagamento juntos, sem saga entre serviços.
- Extrair um módulo depois custa pouco, porque as fronteiras já existem.

---

## Ligações

- **Áreas:** [ADR-0006](0006-divisao-por-areas.md) · **Stack:** [ADR-0007](0007-stack-e-bancos.md) · **Banco:** [ADR-0017](0017-core-em-postgresql.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

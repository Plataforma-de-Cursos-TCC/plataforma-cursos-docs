---
id: adr-0017
titulo: "ADR-0017 — Core em PostgreSQL 16, na mesma instância do Tutor de IA"
tipo: decisao
decisao: D17
status: aceita
data: 2026-11-20
decisor: Grupo
itens_template: [5, 11, 12]
areas: [A, B, C, D]
relacionados: [adr-0007, adr-0010, adr-0014, adr-0016]
---
# ADR-0017 — Core em PostgreSQL 16, na mesma instância do Tutor de IA

- **Status:** aceita · **Data:** 20/11/2026 · **Decisor:** Grupo · **Substitui:** o banco do core (MySQL 8) da [ADR-0007](0007-stack-e-bancos.md)

## Contexto

- A ADR-0007 usava dois motores: MySQL 8 no core e PostgreSQL 16 com pgvector no `ai-service`. São duas tecnologias para operar, fazer backup e aprender.
- As decisões novas pedem recursos que o MySQL não tem ou faz de forma limitada: índice único parcial para o e-mail das contas não anonimizadas (ADR-0014) e particionamento simples da auditoria (ADR-0016).

## Opções consideradas

- **Manter o MySQL 8 no core:** descartada. Não tem índice parcial e mantém dois motores.
- **PostgreSQL num banco único para o core e a IA:** descartada. Mistura a carga vetorial com a transacional e dá ao `ai-service` acesso às tabelas do core.
- **PostgreSQL 16 numa instância, com os databases `core` e `ai` separados:** escolhida.

## Decisão

1. O core usa PostgreSQL 16. O `ai-service` continua com PostgreSQL 16 e pgvector.
2. Os dois ficam na mesma instância gerenciada do Railway (ADR-0010), em databases separados (`core` e `ai`), cada um com usuário e permissões próprios. O `ai-service` não acessa o database `core`; recebe da API só o necessário (`course_id`, `lesson_id`, texto).
3. Tipos usados no item 12: `uuid` para identificadores, `jsonb` para campos compostos (ex.: `details` da auditoria, `social_links`), `timestamptz` para data e hora, e `text` com `CHECK` para valores enumerados.
4. Se a carga da IA crescer, o database `ai` vai para outra instância sem mudar código, só a conexão.

## Consequências

- Uma tecnologia de banco, um backup e uma imagem no ambiente local.
- O TDD (tabela de stack) e os itens 12 passam a citar PostgreSQL e os tipos acima.
- O Redis continua para cache, limite de taxa, contador de login e blocklist (ADR-0007 e ADR-0008).

---

## Ligações

- **Stack anterior:** [ADR-0007](0007-stack-e-bancos.md) · **Hospedagem:** [ADR-0010](0010-hospedagem-e-armazenamento.md) · **Arquitetura:** [ADR-0018](0018-core-como-monolito-modular.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

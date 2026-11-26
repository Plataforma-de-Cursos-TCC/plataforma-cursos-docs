---
id: adr-0016
titulo: "ADR-0016 — Retenção de logs e da trilha de auditoria"
tipo: decisao
decisao: D16
status: aceita
data: 2026-11-20
decisor: Grupo
itens_template: [8, 12, 14]
areas: [D]
relacionados: [adr-0007, adr-0010, adr-0014, adr-0017]
---
# ADR-0016 — Retenção de logs e da trilha de auditoria

- **Status:** aceita · **Data:** 20/11/2026 · **Decisor:** Grupo

> **Nota de atualização (25/11/2026 — Revisão LGPD L10 e L14 e F02):**
> - **Registros de acesso vs. logs técnicos (L10 — Marco Civil da Internet, art. 15):** a retenção de 90 dias do item 3 aplica-se exclusivamente aos **logs técnicos/operacionais de aplicação** (erros, diagnóstico e telemetria sem finalidade de registro de acesso). Os **registros de acesso a aplicações de internet** (autenticação, logout, renovação de sessão, falhas de login, endereço IP, data e hora UTC e identificador de conta) são retidos sob sigilo e em ambiente controlado pelo prazo mínimo legal de **6 meses (180 dias)**, em atendimento ao art. 15 da Lei nº 12.965/2014 (Marco Civil da Internet).
> - **Dados pessoais indiretos em `audit_logs` (L14):** `ip_address`, `user_agent` e os identificadores (`user_id`, `target_id`) são tratados como dados pessoais indiretos/pseudonimizados (art. 5º, I da LGPD), mantidos sob base legal de cumprimento de obrigação legal/regulatória (art. 7º, II da LGPD; art. 15 do Marco Civil) e prevenção à fraude/segurança (art. 7º, IX), com acesso restrito, registro imutável (*append-only*) e proibição de dados cadastrais diretos (nome, e-mail, CPF, telefone) em `details`.
> - **Chave primária composta (F02):** por exigência do particionamento declarativo `PARTITION BY RANGE (created_at)` no PostgreSQL 16, `audit_logs` utiliza chave primária composta `(id, created_at)`.

## Contexto

- O RNF016 exige registro auditável de 100% das ações administrativas, retido por 12 meses. A Área D previa um job que apagava o que passasse disso.
- O grupo quer guardar o máximo possível de logs, sem apagar a auditoria, mas sem deixar a tabela crescer sem limite no banco transacional.

## Opções consideradas

- **Apagar a auditoria depois de 12 meses:** descartada. Cumpre só o mínimo do RNF016.
- **Guardar tudo no banco para sempre:** descartada. A tabela cresce sem limite e pesa nas consultas.
- **PostgreSQL por 12 meses e arquivo frio no Cloudflare R2 até 5 anos:** escolhida.

## Decisão

1. A tabela `audit_logs` fica no PostgreSQL 16 do core (ADR-0017), com particionamento declarativo por mês (`PARTITION BY RANGE (created_at)`) e chave primária composta `(id, created_at)`. Registra autor, ação, alvo, IP, user agent e detalhes técnicos (sem dados cadastrais diretos em `details`).
2. A rotina diária `audit:archive` exporta as partições com mais de 12 meses para o Cloudflare R2 (ADR-0010), em JSON Lines compactado e criptografado, e só então desanexa e remove a partição (`DETACH PARTITION`). O arquivo fica no R2 por 5 anos e é eliminado ao fim do prazo.
3. Os logs técnicos/operacionais da aplicação (erros e diagnóstico) saem em JSON estruturado, com o `requestId` de cada requisição, e ficam 90 dias. Os registros de acesso à aplicação (data e hora UTC, endereço IP e eventos de autenticação/sessão), exigidos pelo art. 15 da Lei nº 12.965/2014 (Marco Civil da Internet), são mantidos sob sigilo em ambiente controlado por no mínimo 6 meses (180 dias).
4. Nenhum log grava senha, token, cookie ou número de documento (CPF); `ip_address`, `user_agent` e identificadores em `audit_logs` são tratados como dados pessoais indiretos sob acesso restrito (LGPD, art. 5º, I e art. 7º, II).

## Consequências

- O RNF016 é cumprido com folga: 12 meses consultáveis no banco e 5 anos no arquivo.
- Consultar auditoria com mais de 12 meses exige baixar o arquivo do R2, e não é uma tela do sistema.
- O item 12 da Área D descreve o particionamento e a rotina `audit:archive`, no lugar do antigo `audit:purge-expired`.

---

## Ligações

- **Banco:** [ADR-0017](0017-core-em-postgresql.md) · **Armazenamento:** [ADR-0010](0010-hospedagem-e-armazenamento.md) · **Exclusão:** [ADR-0014](0014-exclusao-logica-e-anonimizacao.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

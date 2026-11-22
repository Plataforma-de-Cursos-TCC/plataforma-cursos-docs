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

## Contexto

- O RNF016 exige registro auditável de 100% das ações administrativas, retido por 12 meses. A Área D previa um job que apagava o que passasse disso.
- O grupo quer guardar o máximo possível de logs, sem apagar a auditoria, mas sem deixar a tabela crescer sem limite no banco transacional.

## Opções consideradas

- **Apagar a auditoria depois de 12 meses:** descartada. Cumpre só o mínimo do RNF016.
- **Guardar tudo no banco para sempre:** descartada. A tabela cresce sem limite e pesa nas consultas.
- **PostgreSQL por 12 meses e arquivo frio no Cloudflare R2 até 5 anos:** escolhida.

## Decisão

1. A tabela `audit_logs` fica no PostgreSQL 16 do core (ADR-0017), com particionamento declarativo por mês (`PARTITION BY RANGE (created_at)`). Registra autor, ação, alvo, IP, user agent e detalhes.
2. A rotina diária `audit:archive` exporta as partições com mais de 12 meses para o Cloudflare R2 (ADR-0010), em JSON Lines compactado, e só então desanexa e remove a partição (`DETACH PARTITION`). O arquivo fica no R2 por 5 anos.
3. Os logs da aplicação (erros e requisições) saem em JSON estruturado, com o `requestId` de cada requisição, e ficam 90 dias.
4. Nenhum log grava senha, token, cookie ou número de documento.

## Consequências

- O RNF016 é cumprido com folga: 12 meses consultáveis no banco e 5 anos no arquivo.
- Consultar auditoria com mais de 12 meses exige baixar o arquivo do R2, e não é uma tela do sistema.
- O item 12 da Área D descreve o particionamento e a rotina `audit:archive`, no lugar do antigo `audit:purge-expired`.

---

## Ligações

- **Banco:** [ADR-0017](0017-core-em-postgresql.md) · **Armazenamento:** [ADR-0010](0010-hospedagem-e-armazenamento.md) · **Exclusão:** [ADR-0014](0014-exclusao-logica-e-anonimizacao.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

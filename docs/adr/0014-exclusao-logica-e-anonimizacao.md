---
id: adr-0014
titulo: "ADR-0014 — Exclusão lógica em todo o sistema e anonimização separada"
tipo: decisao
decisao: D14
status: aceita
data: 2026-11-20
decisor: Grupo
itens_template: [10, 12, 13, 14, 15]
areas: [A, B, C, D]
relacionados: [adr-0008, adr-0016, adr-0017]
---
# ADR-0014 — Exclusão lógica em todo o sistema e anonimização separada

- **Status:** aceita · **Data:** 20/11/2026 · **Decisor:** Grupo

## Contexto

- O UC018 anonimizava a conta no momento da exclusão. Isso não tem volta, e o grupo quer poder reativar uma conta excluída por engano.
- Nenhum registro do sistema deve sumir do banco: o histórico de matrícula, pagamento, progresso e auditoria precisa continuar consultável.
- A LGPD continua exigindo que os dados pessoais possam ser eliminados a pedido do titular.

## Opções consideradas

- **Exclusão física (`DELETE`):** descartada. Perde o histórico e impede reativar.
- **Anonimização imediata (como estava no UC018):** descartada. É irreversível e impede reativar.
- **Exclusão lógica em todas as tabelas de negócio, com anonimização como passo separado:** escolhida.

## Decisão

1. Toda tabela de negócio tem a coluna `deleted_at` (trait `SoftDeletes` do Eloquent). Nenhuma operação do sistema faz `DELETE` físico. As consultas padrão ignoram as linhas excluídas.
2. As regras que bloqueiam a exclusão quando há histórico de alunos (UC006 R-2, UC014 R-4 e UC015 R-5) continuam valendo e devolvem 409 `CONFLICT`.
3. **Exclusão de usuário (UC018):** `status = deleted` e `deleted_at` preenchido. Os dados são mantidos, o acesso é revogado (blocklist do `jti` e revogação das sessões de refresh, ADR-0008) e o Administrador pode reativar a conta.
4. **Anonimização:** é um passo separado e irreversível. Acontece a pedido do titular ou 30 dias depois da exclusão sem reativação, por uma rotina agendada. Ela apaga nome, e-mail, telefone, documento, data de nascimento, foto e endereços e preenche `anonymized_at`. O histórico continua ligado ao mesmo `user_id`. Conta anonimizada não pode ser reativada.
5. **Exclusão de Instrutor:** o Administrador escolhe o que acontece com os cursos: despublicá-los (`status = archived`) ou excluí-los logicamente em cascata, junto com módulos, aulas e quizzes.
6. Login de conta excluída ou anonimizada devolve 401 `UNAUTHENTICATED` genérico, igual a senha errada, para não revelar que a conta existiu.

## Consequências

- O modelo de dados (item 12) das quatro áreas ganha `deleted_at` nas tabelas de negócio, e `User` ganha `anonymized_at`.
- O UC018 (item 10) passa a ter os fluxos de reativação e de anonimização, e o item 15 testa os dois.
- Unicidade de e-mail: índice único parcial do PostgreSQL (`UNIQUE (email) WHERE anonymized_at IS NULL`, ADR-0017); a anonimização troca o e-mail por um valor sintético.
- O banco cresce sem apagar linhas. O volume do projeto é pequeno, e as listagens já usam índice e paginação (ADR-0009).

---

## Ligações

- **Sessão e revogação:** [ADR-0008](0008-sessao-jwt-em-cookie.md) · **Auditoria:** [ADR-0016](0016-retencao-de-logs-e-auditoria.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)

# Pendências da Área D

Registro das dúvidas e dos casos de teste retirados da Área D na rodada de correção da revisão cruzada (#135). Regra 10 do `CONTEXT.md`: caso de teste sem regra no item 10 sai, ou a dúvida vai para este arquivo. Nada aqui foi decidido pela Área D: cada item depende de uma decisão do grupo.

## 1. Casos de teste retirados (item 15)

| TC | Caso retirado | O que o caso supunha | Por que saiu |
|---|---|---|---|
| TC243 | Acesso com JWT antigo após promoção (403) | Que o token emitido antes da promoção seja rejeitado até nova autenticação ou renovação | O item 10 (UC008, R-5) diz só que o novo perfil vale a partir do próximo acesso. O mecanismo (rejeitar o token antigo ou apenas recarregar o perfil) não está definido em nenhum documento. |
| TC244 | Auto-desbloqueio (403) | Que um Administrador não possa desbloquear a própria conta | O item 10 (UC008, R-1 e E1) cobre só o bloqueio da própria conta. Sem regra para o desbloqueio. |
| TC245 | Limite de paginação em `per_page=999` (422 ou truncamento em 100) | Que o servidor recuse ou trunque valores acima do limite | A TDD (seção de paginação, ADR-0009) fixa o máximo de 100, mas não define a resposta quando o valor passa do limite. O item 10 não trata de paginação. |
| TC246 | Envio de `status: deleted` na rota de status (422) | Que a exclusão só possa ocorrer pelo UC018 | Nenhum caso de uso do item 10 proíbe `status: deleted` na rota de status. |
| TC265 | Histórico de `QuizAttempt` e `LessonProgress` após exclusão | Que notas e progresso do Aluno excluído permaneçam ligados ao `userId` anonimizado | O item 10 (UC018, R-1) cita só matrículas e pagamentos. Notas e progresso são da Área C, e a regra deve ser confirmada por ela. |
| TC266 | Exclusão de Instrutor com cursos publicados (204, cursos mantidos, nome "Instrutor Desativado") | Que os cursos continuem disponíveis e que o nome do Instrutor seja substituído | Nenhuma regra no item 10 trata de cursos de Instrutor excluído. Depende de decisão da Área B. |
| TC267 | Exclusão sem confirmação explícita pela API (422 em `fields.confirmed`) | Que a API exija um campo de confirmação | O item 10 (UC018, R-3) exige confirmação explícita, mas o item 13 não declara campo de confirmação em `DELETE /api/v1/admin/users/{id}`. Ver item 2 abaixo. |
| TC268 | Reativação de conta anonimizada via rota de status (422) | Que a anonimização seja irreversível também pela API | O item 10 (UC018, R-3) fala em irreversibilidade, mas não define a resposta da API a uma tentativa de reativação. |

## 2. Detalhes retirados dos casos de teste mantidos

Os casos continuam válidos sem estes detalhes, que não têm regra no item 10 nem na TDD.

- **TC216 e TC217:** valor fixo de `Retry-After` (300 s) e estado do contador de Redis. O item 10 (UC001, E2) não fixa o tempo de espera; o caso agora só verifica que o cabeçalho existe.
- **TC218:** valor fixo de `Retry-After` (60 s). Mesma razão.
- **TC232:** invalidação de sessões no Redis. O caso agora diz "acesso revogado imediatamente", que é o texto do item 10.
- **TC236:** criação de linha vazia em `InstructorProfile` ao promover a Instrutor. O item 10 não prevê isso; a Área A precisa dizer se essa linha existe.
- **TC237:** retenção de 12 meses no próprio caso. A retenção é um requisito do sistema, não um resultado do caso de teste (ver item 3).
- **TC258:** blocklist de tokens em Redis. A TDD (seção de revogação) diz que a blocklist entra na Sprint 2; o caso agora verifica só `RefreshSession.revokedAt`.

## 3. Dúvidas de decisão

1. **Retenção do AuditLog.** O item 12 da Área D descreve uma rotina diária (`audit:purge-expired`, cron à meia-noite) que apaga registros com mais de 12 meses. O RNF016 fixa a retenção mínima, não o mecanismo. Confirmar se o job é a forma de cumprir a regra e se a rotina entra no escopo da entrega.
2. **Confirmação da exclusão na API (TC267).** O R-3 do UC018 exige confirmação explícita. O item 13 não tem campo de confirmação. Decidir se a confirmação é só da interface (UC018, A1) ou se a API precisa de um campo (por exemplo, `DeleteUserRequest` com `confirmed`).
3. **Nomes de parâmetros do dashboard.** A TDD (tabela de rotas, `GET /api/v1/analytics/dashboard`) usa `inicio`, `fim` e `curso_id`. Os itens 13, 14 e 15 da Área D usam `startDate`, `endDate` e `courseId`. Os casos de teste seguem o item 13. A TDD precisa ser alinhada pelo grupo (não foi alterada aqui). O item 13 também ganhou `groupBy` (dia, semana, mês), com base no UC007, R-3.
4. **Rota de troca de perfil.** `PUT /api/v1/admin/users/{id}/role` aparece nos itens 13 e 14 e nos casos TC236, TC240 e TC241, mas não consta na tabela de rotas da TDD. Incluir na TDD.
5. **Resposta acima do limite de `per_page`.** Ver TC245 acima.
6. **Campo de segundo do vídeo na pergunta.** O item 13 tem `AskTutorRequest.videoTimestampSeconds`, mas o item 10 (UC001) não diz se o Aluno informa o segundo do vídeo ao perguntar. O TC212 assume que sim; se não, o campo sai do item 13.
7. **Revogação por blocklist.** A TDD prevê blocklist em Redis na Sprint 2. Decidir se a revogação imediata do UC008 e do UC018 entra nesta sprint ou só na Sprint 2.
8. **Login de conta anonimizada.** O TC262 supõe resposta 401 genérica, porque a pós-condição do UC018 diz "acesso revogado" e o e-mail é anonimizado. Confirmar com a Área A.
9. **Auto-desbloqueio e reativação.** Ver TC244 e TC268 acima. Se o grupo quiser essas regras, elas precisam entrar no item 10 do UC008 e do UC018 antes de voltar como casos de teste.

## 4. Dependências de outras áreas

- **JwtGuard (Área A).** Os itens 13 e 14 da Área D usam `JwtGuard.parseToken(token)` e `JwtGuard.authorize(user, role)`. Esses métodos precisam entrar no item 13 da Área A (coordenador). Hoje o item 13 da Área A só declara `issue` e `issueRefresh`.
- **Lesson.indexStatus (Área B).** O campo `pending`, `indexed` ou `failed` pertence à Área B. A Área D só lê o campo para o código `LESSON_NOT_INDEXED`.
- **UserRepository (Área A).** O item 13 da Área D usa `UserRepository (Área A)` com `paginate` e `anonymize`, além dos métodos da Área A. Confirmar se esses métodos devem entrar no item 13 da Área A.

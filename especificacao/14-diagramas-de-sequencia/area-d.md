## 1. UC001 – Conversar com Tutor de IA

Fluxo básico e tratamento contextual de dúvidas pedagógicas na página da aula. O Aluno matriculado envia a pergunta via `POST /api/v1/ai/tutor/chat`, acompanhada opcionalmente de `videoTimestampSeconds` (D6). O `TutorService` valida a cota de mensagens no Redis com o `TutorRateLimiter` (20 mensagens por hora em janela deslizante, D-cota). Se a cota horária for ultrapassada, o serviço verifica no `TutorCreditPackRepository` a disponibilidade de pacotes de créditos extras adquiridos pelo aluno (D-cota-extra, RF020); havendo créditos, decrementa um crédito da tabela `tutor_credit_packs` e dá seguimento à resposta. Se não houver saldo extra nem cota, responde 429 `TOO_MANY_REQUESTS` com o cabeçalho `Retry-After` (E2). Para requisições autorizadas, delega a geração ao `CourseTutorClient`, que consome o pipeline RAG do `ai-service` via streaming SSE em menos de 3 segundos (RNF003) considerando o `User.locale` (RNF013). Exceções adicionais modeladas em blocos `alt`: aluno não matriculado (E4, 403 `FORBIDDEN`); aula ainda não indexada (E1, 409 `LESSON_NOT_INDEXED`); e indisponibilidade do microsserviço de inteligência artificial (E3, 503 `SERVICE_UNAVAILABLE` com `Retry-After`). Respostas com trechos e timestamps são enviadas ao front-end por SSE, e a pergunta e a resposta são gravadas no histórico por chamadas `MessageRepository.create(MessageDTO)`, cada uma com o seu `INSERT`.

![Diagrama de sequência do UC001](../diagramas/14-sequencia-uc001.png)

*Figura 0 – UC001, diagrama de sequência: conversar com Tutor de IA*

## 2. UC007 – Ver Dashboard com Filtro

Consulta de métricas e gráficos de progresso e engajamento via `GET /api/v1/analytics/dashboard` pelo Instrutor ou Administrador. Os parâmetros de consulta são fornecidos em inglês: `startDate`, `endDate`, `courseId` opcional e `groupBy` com valores aceitos `day`, `week` ou `month` (D3). A validação dos parâmetros pelo Form Request (`DashboardFilterRequest`) assegura que `startDate <= endDate` e que `groupBy` seja válido, retornando 422 `VALIDATION_FAILED` em caso de inconsistência (E1). O `DashboardAnalyticsService` valida a propriedade dos cursos (UC007 R-2, retornando 403 `FORBIDDEN` caso um Instrutor tente visualizar dados de cursos pertencentes a terceiros) e executa consultas agregadas dinâmicas sobre matrículas e progresso de aulas via `AnalyticsQueryRepository.aggregateProgressAndEnrollments(courseIds, start, end, groupBy)`. Se não houver atividade no período filtrado, a API responde 200 OK com métricas zeradas (E2), exibindo um estado vazio amigável na interface via `DashboardResource`.

![Diagrama de sequência do UC007](../diagramas/14-sequencia-uc007.png)

*Figura 0 – UC007, diagrama de sequência: ver dashboard com filtro*

## 3. UC008 – Gerenciar Usuários

Busca e governança de usuários pelo Administrador via `GET /api/v1/admin/users`, bloqueio/desbloqueio via `PUT /api/v1/admin/users/{id}/status` e alteração de perfil de acesso via `PUT /api/v1/admin/users/{id}/role` (A4, US016). Na listagem, o parâmetro de paginação segue camelCase (`perPage: int`, entre 1 e 100, C10/ADR-0015); valores fora desse intervalo retornam 422 `VALIDATION_FAILED` (D-TC245). O serviço `UserAdminService` executa `paginateUsers(filters: UserFiltersDTO)` delegando a `UserRepository.paginate(filters: UserFiltersDTO): LengthAwarePaginator`. O diagrama adota exclusivamente fragmentos `alt`: a confirmação ou cancelamento da ação é decidida em um bloco `alt` onde o cancelamento (A2) encerra a sequência sem mutações. Na alteração de status, tentativas de definir `status: deleted` são rejeitadas com 422 `VALIDATION_FAILED`, pois a exclusão deve utilizar a rota dedicada de exclusão lógica (D-TC246, UC018). Tentativas de auto-bloqueio (E1) ou auto-desbloqueio (D-TC244/D9) são barradas com 403 `FORBIDDEN`. Em caso de bloqueio bem-sucedido, o status é persistido no banco, o token JWT ativo do usuário é revogado no Redis via `JwtGuard.revoke(jti, ttl)` (D7) e as sessões de refresh são invalidadas no PostgreSQL (TC232), gravando o evento em `audit_logs` (RNF016). Na alteração de perfil (A4), o `UserAdminService` impede que o Administrador altere o próprio perfil com 403 `FORBIDDEN` (E3); para outros usuários, atualiza a role, cria o registro em `instructor_profiles` caso o usuário esteja sendo promovido a Instrutor (TC236), invalida o token JWT anterior no Redis via `JwtGuard.revoke(jti, ttl)` (D-TC243) e aciona obrigatoriamente o `AuditService.logAction` para registrar a ação `ROLE_CHANGE` em `audit_logs` (RNF016).

![Diagrama de sequência do UC008](../diagramas/14-sequencia-uc008.png)

*Figura 0 – UC008, diagrama de sequência: gerenciar usuários*

## 4. UC016 – Acessar Área Protegida por Perfil

Verificação de autorização e controle de acesso a rotas privadas pelo middleware `EnsureUserHasRole` e `ProtectedAreaController`. A leitura e validação do token por `JwtGuard.parseToken(token)` verifica a integridade criptográfica e consulta a lista de revogação (`jti`) no Redis (D7); se a sessão estiver ausente, expirada ou constar na blocklist (E1), responde 401 `UNAUTHENTICATED` e redireciona ao login (UC005). Se `JwtGuard.authorize(user, role)` indicar que o usuário autenticado não possui o perfil exigido para a rota (E2), o middleware aciona `AuditService.logAccessDenied` para registrar a tentativa de violação na trilha de auditoria `audit_logs` com a ação `ACCESS_DENIED` (RNF016) e responde 403 `FORBIDDEN`, redirecionando o usuário à área inicial do seu próprio perfil. Quando autorizado, libera o acesso e direciona para a página inicial do perfil após o login (A1) ou exibe a área protegida solicitada via `PermissionsResource`.

![Diagrama de sequência do UC016](../diagramas/14-sequencia-uc016.png)

*Figura 0 – UC016, diagrama de sequência: acessar área protegida por perfil*

## 5. UC018 – Excluir e Anonimizar Usuário

Exclusão lógica de conta pelo Administrador via `DELETE /api/v1/admin/users/{id}`, em conformidade com a ADR-0014, estendendo o UC008. O fluxo inicia com a apresentação do modal de confirmação com aviso de exclusão: o cancelamento (A1) encerra a operação em bloco `alt`. Na confirmação da exclusão, o `UserAdminService` impede a autoexclusão da conta do Administrador com 403 `FORBIDDEN` (E1, R-2) e trata usuário inexistente ou já excluído com 404 `NOT_FOUND` (E2). Para usuário válido, `UserRepository (Área A)` aplica a exclusão lógica preenchendo `deleted_at = NOW()`; se o usuário for um instrutor com cursos ativos, esses cursos são arquivados (`status = 'archived'`) para preservar o histórico dos alunos matriculados (TC266); o serviço invalida o token JWT ativo no Redis via `JwtGuard.revoke(jti, ttl)` (D7, TC258), revoga sessões de refresh ativas no banco e grava o evento em `audit_logs` com a ação `USER_DELETE` via `AuditService` (RNF016), respondendo 204 `No Content`. Tentativas subsequentes de autenticação por contas excluídas retornam HTTP 401 unauthenticated genérico (D8, TC262). O histórico acadêmico permanece preservado vinculado ao mesmo `userId` (TC265), e o usuário excluído pode ser reativado pelo Administrador via rota de restauração (TC268).

![Diagrama de sequência do UC018](../diagramas/14-sequencia-uc018.png)

*Figura 0 – UC018, diagrama de sequência: excluir e anonimizar usuário*

### Resolução das pendências cruzadas da Área A (Issue #123)

Em conformidade com a regra 8 do `AGENTS.md`, seguem resolvidas as pendências cruzadas deixadas pela Área A para a Área D no item 14:

1. **Códigos de erro `CONFLICT` e `SERVICE_UNAVAILABLE` do catálogo (`docs/tdd.md` seção 3.1):** Alinhados e confirmados para a Área D com base nos requisitos **RF009**, **RF012** e **RNF003**:
   - Nenhuma sequência da Área D usa `CONFLICT` (HTTP 409): a TDD 3.1 o aplica a estado de negócio impeditivo, como curso com alunos matriculados no `DELETE` (Área B). Na interação com o Tutor de IA, aula ainda não indexada usa o código específico `LESSON_NOT_INDEXED` (HTTP 409, fluxo de exceção E1 do UC001).
   - O código `SERVICE_UNAVAILABLE` (HTTP 503) aparece no fluxo de exceção E3 do UC001, com o cabeçalho HTTP `Retry-After` (TDD 3.1), quando há falha de comunicação ou timeout do microsserviço `ai-service` ou da API do provedor de inteligência artificial.
2. **RNF016 nas ações administrativas do UC008 e UC018:** Atendido por **RNF016**, **RF012**, **ADR-0016** e regras de negócio do **UC008** (R-4) e **UC018** (R-4). Os diagramas de sequência da Área D modelam expressamente o acionamento síncrono de `AuditService.logAction(...)` e a execução da inserção em banco de dados (`INSERT INTO audit_logs`) nas alterações de status, alterações de perfil de acesso, exclusão lógica de usuários e negação de acesso do UC016 (`AuditService.logAccessDenied`). A retenção é de 5 anos via particionamento mensal no PostgreSQL e expurgo contínuo para Cloudflare R2 pelo job agendado `audit:archive` (D1, ADR-0016).

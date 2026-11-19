## 4. Área D – Tutor de IA, analytics e administração

Tabelas que sustentam a interação do Aluno com o assistente pedagógico no contexto da aula, a visualização analítica de progresso e engajamento e a gestão administrativa de usuários e perfis com registro auditável (UC001, UC007, UC008, UC016 e UC018; RF009, RF010, RF012 e RF018; RNF003, RNF004 e RNF016). `Conversation` e `Message` estruturam o histórico contextual do chat pedagógico; `AuditLog` assegura a rastreabilidade e a responsabilização das operações administrativas e de segurança. As métricas do Dashboard (UC007) são calculadas dinamicamente via agregação das tabelas transacionais de matrícula e progresso (`Enrollment` e `LessonProgress`, da Área C), sem necessidade de tabelas redundantes de consolidação.

![Modelo lógico da Área D](../diagramas/12-modelo-de-dados-area-d.png)

*Figura 0 – Modelo lógico relacional da Área D (Tutor de IA, analytics e administração)*

Decisões do modelo:

- `Conversation` e `Message` estruturam a persistência relacional do histórico do Tutor de IA no banco primário MySQL (ADR-0007). Cada conversa é estritamente vinculada a um Aluno (`userId`), a um curso (`courseId`) e à aula assistida (`lessonId`). A persistência vetorial de trechos e embeddings gerados uma única vez (RNF004) reside no microsserviço físico `ai-service` em banco PostgreSQL 16 com extensão `pgvector` (tabela de chunks particionada por `course_id`), desacoplando o pipeline RAG e o streaming SSE (RNF003) do core relacional.
- `AuditLog` implementa o registro auditável de 100% das ações administrativas do Administrador e eventos de controle de acesso (RNF016), abrangendo bloqueio e desbloqueio de usuários (UC008), alteração de perfil de acesso (UC008 A4), tentativas de acesso indevido a áreas protegidas (UC016 E2) e exclusão/anonimização de contas (UC018). Os registros possuem política de retenção mínima de 12 meses (RNF016).
- Normalização e integridade: as tabelas `Conversation` e `Message` estão normalizadas em 3FN, sem dependências transitivas. Na tabela `AuditLog`, o campo `details` utiliza o tipo JSON para armazenar metadados variáveis do evento (como perfil anterior e novo, ou motivo do bloqueio), o que constitui uma exceção deliberada à 1FN justificada pela natureza heterogênea dos eventos de auditoria (análoga a `InstructorProfile.socialLinks` na Área A).
- Privacidade e LGPD na exclusão (UC018 R-4): na exclusão de conta de usuário, os dados pessoais na tabela `User` são limpos ou anonimizados (`anonymizedAt` preenchido), e o evento registrado em `AuditLog` referencia o identificador (`targetId`) sem manter dados pessoais sensíveis (como nome, CPF ou e-mail) no registro de auditoria ou no campo `details`.

| ATRIBUTO | CLASSE | DOMÍNIO | TAMANHO | DESCRIÇÃO |
|---|---|---|---|---|
| **Tabela: Conversation** | | | | Conversa do Aluno com o Tutor de IA contextualizada na aula (UC001, RF009). |
| id | Determinante | UUID | - | Identificador único da conversa. |
| userId | Simples | UUID | - | FK para `User.id` (Área A), identificando o Aluno dono da conversa. |
| courseId | Simples | UUID | - | FK para `Course.id` (Área B), curso ao qual a conversa pertence. |
| lessonId | Simples | UUID | - | FK para `Lesson.id` (Área B), aula específica que fornece o contexto pedagógico. |
| createdAt | Simples | Data e hora | - | Data e hora de criação da conversa. |
| **Tabela: Message** | | | | Mensagem individual trocada na conversa com o Tutor de IA (UC001). |
| id | Determinante | UUID | - | Identificador único da mensagem. |
| conversationId | Simples | UUID | - | FK para `Conversation.id`, indicando a conversa à qual a mensagem pertence. |
| role | Simples | Texto | - | Papel do emissor: `user` (pergunta do Aluno) ou `assistant` (resposta do Tutor de IA). |
| content | Simples | Texto longo | TEXT | Conteúdo textual da pergunta ou da resposta gerada pelo Tutor. |
| videoTimestampSeconds | Simples | Inteiro | - | Segundo exato do vídeo da aula referenciado na resposta (opcional; nulo em perguntas do Aluno). |
| createdAt | Simples | Data e hora | - | Data e hora de envio ou geração da mensagem. |
| **Tabela: AuditLog** | | | | Trilha de auditoria das ações administrativas e de segurança (RNF016). Retenção de 12 meses. |
| id | Determinante | UUID | - | Identificador único do registro de auditoria. |
| userId | Simples | UUID | - | FK para `User.id` (Área A), identificando o autor da ação (nulo em tentativas não autenticadas). |
| action | Simples | Texto | 60 | Identificador estável da ação: `USER_BLOCK`, `USER_UNBLOCK`, `ROLE_CHANGE`, `USER_DELETE`, `ACCESS_DENIED`. |
| targetType | Simples | Texto | 40 | Tipo da entidade ou recurso alvo da ação auditada (ex.: `User`, `AreaProtegida`). |
| targetId | Simples | Texto | 36 | Identificador UUID do recurso afetado (opcional; preservado na exclusão LGPD). |
| ipAddress | Simples | Texto | 45 | Endereço IP de origem da requisição (compatível com IPv4 e IPv6). |
| userAgent | Simples | Texto | 255 | Identificação do cliente HTTP/navegador que originou a requisição. |
| details | Composto | JSON | - | Metadados contextuais estruturados da operação (ex.: papéis anterior e novo); sem dados pessoais sensíveis (UC018 R-4). |
| createdAt | Simples | Data e hora | - | Data e hora exata da ocorrência do evento auditado. |

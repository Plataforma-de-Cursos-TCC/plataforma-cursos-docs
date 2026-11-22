## 4. Área D – Tutor de IA, analytics e administração

Tabelas que sustentam a interação do Aluno com o assistente pedagógico no contexto da aula, a visualização analítica de progresso e engajamento e a gestão administrativa de usuários e perfis com registro auditável (UC001, UC007, UC008, UC016 e UC018; RF009, RF010, RF012, RF018 e RF020; RNF003, RNF004, RNF016 e RNF022). As tabelas `conversations` e `messages` estruturam o histórico contextual do chat pedagógico; `tutor_credit_packs` armazena os pacotes de créditos extras adquiridos pelo Aluno via pagamento simulado para extensão do uso do Tutor de IA além da cota regular (D-cota-extra); e `audit_logs` assegura a rastreabilidade e a responsabilização das operações administrativas e de segurança no PostgreSQL 16 (ADR-0016, ADR-0017). As métricas do Dashboard (UC007) são calculadas dinamicamente via agregação das tabelas transacionais de matrícula e progresso (`enrollments` e `lesson_progress`, da Área C), sem necessidade de tabelas redundantes de consolidação.

![Modelo lógico da Área D](../diagramas/12-modelo-de-dados-area-d.png)

*Figura 0 – Modelo lógico relacional da Área D (Tutor de IA, analytics e administração)*

Decisões do modelo:

- **Banco unificado em PostgreSQL 16 (ADR-0017):** todo o armazenamento transacional do core reside no PostgreSQL 16 (database `core`), unificando a tecnologia de banco com a instância gerenciada do microsserviço físico `ai-service` (database `ai` com extensão `pgvector`). Cada serviço mantém seu banco lógico, usuário e permissões isoladas.
- **Convenção de nomes por camada (ADR-0015 / C10):** todas as tabelas e colunas relacionais são estruturadas em inglês e no padrão `snake_case` (`user_id`, `course_id`, `created_at`, `deleted_at`).
- **Exclusão lógica em todo o sistema (ADR-0014):** todas as tabelas de negócio (`conversations`, `messages`, `tutor_credit_packs`) possuem a coluna `deleted_at` (`timestamptz` nulo por padrão, trait `SoftDeletes` do Eloquent). Nenhuma operação de domínio executa `DELETE` físico.
- **Histórico e cota do Tutor de IA (UC001, RF009, RF020, RNF003):** cada conversa é estritamente vinculada a um Aluno (`user_id`), a um curso (`course_id`) e à aula assistida (`lesson_id`). A tabela `conversations` possui a restrição de unicidade `UNIQUE(user_id, lesson_id)`, garantindo exatamente uma conversa aberta por aluno em cada aula. A presença redundante de `course_id` em `conversations` é um desvio deliberado e justificado da 3FN: viabiliza filtragem relacional imediata no pipeline RAG do `ai-service` (`where('course_id', $courseId)`, RNF004) sem necessidade de junções de múltiplas tabelas transacionais a cada mensagem enviada.
- **Créditos extras do Tutor de IA (`tutor_credit_packs`, D-cota-extra):** tabela que registra pacotes adicionais de mensagens (ex.: 50 mensagens, RNF022) comprados pelo Aluno através de pagamento simulado (`payment_id` referenciando `payments`, com `purpose = 'tutor_credits'`). A cota horária regular de 20 mensagens por Aluno é controlada por janela deslizante no Redis (D-cota); ao esgotar a cota horária, o sistema debita automaticamente os envios do pacote de créditos extras ativo (`messages_used`).
- **Trilha de auditoria e retenção (`audit_logs`, RNF016, ADR-0016, D1):** registra 100% das ações administrativas do Administrador e eventos de controle de acesso (bloqueio e desbloqueio no UC008, alteração de perfil no UC008 A4, negação de acesso no UC016 E2 e exclusão/reativação no UC018). A tabela é particionada mensalmente por data (`PARTITION BY RANGE (created_at)`). A retenção ativa no PostgreSQL 16 é de 12 meses; a rotina agendada diária `audit:archive` (cron à meia-noite) exporta as partições com mais de 12 meses para o Cloudflare R2 em JSON Lines compactado e desanexa a partição (`DETACH PARTITION`), mantendo o arquivo seguro por até 5 anos. Na exclusão de usuário (UC018 R-4), `target_id` armazena o UUID sem incluir dados pessoais no campo `details` (LGPD). A anonimização (UC018 A3) grava `USER_ANONYMIZE` com a mesma regra: sem dados pessoais no log.
- **Exclusão de Instrutor com cursos publicados (UC018 A4, D-TC266):** o Administrador escolhe entre despublicar os cursos (`courses.status = 'archived'`, que preserva o acesso dos alunos matriculados) ou aplicar exclusão lógica em cascata (`deleted_at`) nos cursos, módulos, aulas e quizzes. Nenhuma das duas opções apaga registro.
- **Normalização de `audit_logs`:** exceção deliberada à 1FN no campo `details` (`jsonb`) para metadados contextuais flexíveis (ex.: perfil anterior e novo), e dependência funcional transitiva mantida de propósito em `target_type` para evitar junções com tabelas auxiliares em consultas pontuais de eventos.
- **Campo lido de outra área:** `lessons.index_status` (`pending`, `indexed`, `failed`) pertence à Área B, que o grava. A Área D apenas lê o campo para responder com `LESSON_NOT_INDEXED` (UC001 E1).
- **Mapeamento de valores enumerados (persistidos em inglês, mapeados para pt-BR na interface):**
  - `messages.role`: `user` (Aluno) e `assistant` (Tutor de IA).
  - `audit_logs.action`: `USER_BLOCK` (Bloqueio de usuário), `USER_UNBLOCK` (Desbloqueio de usuário), `ROLE_CHANGE` (Alteração de perfil de acesso), `USER_DELETE` (Exclusão lógica de usuário), `USER_RESTORE` (Reativação de usuário excluído), `USER_ANONYMIZE` (Anonimização irreversível conforme LGPD), `ACCESS_DENIED` (Tentativa de acesso não autorizada a área protegida).
  - Enums referenciados de `users`: `role` (`student` = Aluno, `instructor` = Instrutor, `admin` = Administrador); `status` (`active` = Ativo, `blocked` = Bloqueado, `deleted` = Excluído); `theme` (`light` = Claro, `dark` = Escuro, `system` = Sistema).

### Resolução das pendências cruzadas da Área A (Issue #122)

Em conformidade com a regra 8 do `AGENTS.md`, seguem resolvidas as pendências cruzadas deixadas pela Área A para a Área D no item 12:

1. **Primeiro Administrador (seed):** Atendido por **RF012** e **RNF016**. Como o cadastro público (UC012) restringe a criação de contas aos papéis de Aluno e Instrutor, o primeiro usuário com perfil `admin` (`users.role = 'admin'`) é provisionado diretamente na inicialização do sistema por meio de seed de banco de dados (`DatabaseSeeder`), com credenciais administrativas seguras definidas em variáveis de ambiente. Novos administradores são criados posteriormente por administradores já autenticados por meio da alteração de perfil prevista no UC008 (A4).
2. **User.status bloqueado:** Atendido por **RF012** e regra R-1 do **UC008**. O UC008 é a autoridade responsável por atualizar `users.status` para o valor `blocked` (bloqueio administrativo) ou restaurar para `active` (desbloqueio). Isso garante compatibilidade total com o fluxo de autenticação do UC005 (E3), onde a tentativa de login de uma conta bloqueada com credenciais corretas resulta na resposta HTTP 403 com o código de erro estável `ACCOUNT_BLOCKED` (`docs/tdd.md` seção 3.1).
3. **Trilha de auditoria:** Atendido por **RNF016**, **RF012**, **RF018** e regras de negócio do **UC008** (R-4), **UC016** (R-3) e **UC018** (R-4). Foi incorporada a tabela `audit_logs` ao modelo relacional da Área D no PostgreSQL 16 (ADR-0016, ADR-0017), registrando autor (`user_id`), ação administrativa (`action`), tipo e identificador do alvo (`target_type`, `target_id`), endereço IP (`ip_address`), cliente (`user_agent`), metadados contextuais (`details` em JSONB, resguardando a privacidade conforme a LGPD) e timestamp (`created_at`), particionada mensalmente com retenção de 12 meses no banco e arquivamento de 5 anos no Cloudflare R2 pelo job `audit:archive`.
4. **Idioma:** Atendido por **RNF013**, **RF009** e **RF010**. O Tutor de IA (UC001) e o Dashboard analítico (UC007) utilizam o campo `users.locale` (persistido na tabela `users`, com padrão `pt-BR`) para determinar o idioma do prompt pedagógico e das respostas geradas pelo agente RAG, bem como para aplicar a formatação localizada de datas (DD/MM/AAAA) e números decimais nos gráficos e relatórios, mantendo conformidade com o padrão multilíngue estabelecido pela Área A para suporte futuro a `en` e `es`.

| ATRIBUTO | CLASSE | DOMÍNIO | TAMANHO | DESCRIÇÃO |
|---|---|---|---|---|
| **Tabela: conversations** | | | | Conversa do Aluno com o Tutor de IA contextualizada na aula (UC001, RF009). Restrição de unicidade: `UNIQUE(user_id, lesson_id)`. |
| id | Determinante | UUID | - | Identificador único da conversa. |
| user_id | Simples | UUID | - | FK para `users.id` (Área A), identificando o Aluno dono da conversa. |
| course_id | Simples | UUID | - | FK para `courses.id` (Área B), curso ao qual a conversa pertence (desvio justificado da 3FN para isolamento RAG). |
| lesson_id | Simples | UUID | - | FK para `lessons.id` (Área B), aula específica que fornece o contexto pedagógico. |
| created_at | Simples | Data e hora | TIMESTAMPTZ | Data e hora de criação da conversa. |
| deleted_at | Simples | Data e hora | TIMESTAMPTZ | Data e hora de exclusão lógica (nulo para conversas ativas, ADR-0014). |
| **Tabela: messages** | | | | Mensagem individual trocada na conversa com o Tutor de IA (UC001). |
| id | Determinante | UUID | - | Identificador único da mensagem. |
| conversation_id | Simples | UUID | - | FK para `conversations.id`, indicando a conversa à qual a mensagem pertence. |
| role | Simples | Texto | CHECK | Papel do emissor: `user` (pergunta do Aluno) ou `assistant` (resposta do Tutor de IA). |
| content | Simples | Texto longo | TEXT | Conteúdo textual da pergunta ou da resposta gerada pelo Tutor. |
| video_timestamp_seconds | Simples | Inteiro | INTEGER | Segundo exato do vídeo da aula referenciado na resposta ou na pergunta (opcional, D6). |
| created_at | Simples | Data e hora | TIMESTAMPTZ | Data e hora de envio ou geração da mensagem. |
| deleted_at | Simples | Data e hora | TIMESTAMPTZ | Data e hora de exclusão lógica (nulo para mensagens ativas, ADR-0014). |
| **Tabela: tutor_credit_packs** | | | | Pacote de créditos extras do Tutor de IA adquirido por Aluno com pagamento simulado (RF020, RNF022, D-cota-extra). |
| id | Determinante | UUID | - | Identificador único do pacote de créditos extras. |
| user_id | Simples | UUID | - | FK para `users.id` (Área A), identificando o Aluno proprietário do pacote. |
| payment_id | Simples | UUID | - | FK para `payments.id` (Área C), identificando o pagamento simulado da aquisição. |
| messages_total | Simples | Inteiro | INTEGER | Quantidade total de mensagens contratadas no pacote (ex.: 50). |
| messages_used | Simples | Inteiro | INTEGER | Quantidade de mensagens consumidas do pacote (padrão 0). |
| created_at | Simples | Data e hora | TIMESTAMPTZ | Data e hora da aquisição e ativação do pacote. |
| deleted_at | Simples | Data e hora | TIMESTAMPTZ | Data e hora de exclusão lógica (nulo para registros ativos, ADR-0014). |
| **Tabela: audit_logs** | | | | Trilha de auditoria das ações administrativas e de segurança no PostgreSQL 16 (RNF016, ADR-0016). Particionada por mês (`PARTITION BY RANGE (created_at)`) com exportação para R2 por 5 anos via `audit:archive`. |
| id | Determinante | UUID | - | Identificador único do registro de auditoria. |
| user_id | Simples | UUID | - | FK para `users.id` (Área A), identificando o autor da ação (nulo em tentativas não autenticadas e na rotina automática de anonimização, UC018 A3). |
| action | Simples | Texto | CHECK | Identificador estável da ação: `USER_BLOCK`, `USER_UNBLOCK`, `ROLE_CHANGE`, `USER_DELETE`, `USER_RESTORE`, `USER_ANONYMIZE`, `ACCESS_DENIED`. |
| target_type | Simples | Texto | TEXT | Tipo da entidade ou recurso alvo da ação auditada (ex.: `User`, `ProtectedArea`). |
| target_id | Simples | UUID | - | Identificador UUID do recurso afetado (opcional; preservado na exclusão LGPD). |
| ip_address | Simples | Texto | TEXT | Endereço IP de origem da requisição (compatível com IPv4 e IPv6). |
| user_agent | Simples | Texto | TEXT | Identificação do cliente HTTP/navegador que originou a requisição. |
| details | Composto | JSONB | - | Metadados contextuais estruturados da operação (ex.: papéis anterior e novo); sem dados pessoais sensíveis (UC018 R-4). |
| created_at | Simples | Data e hora | TIMESTAMPTZ | Data e hora exata da ocorrência do evento auditado (chave de particionamento). |

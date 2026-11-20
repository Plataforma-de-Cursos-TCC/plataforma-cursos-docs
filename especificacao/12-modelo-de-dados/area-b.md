## 2. Área B – Autoria do instrutor

Tabelas que sustentam a criação e gestão de cursos, módulos, aulas com materiais complementares e quizzes com gabarito pelo Instrutor (UC004, UC006, UC014 e UC015; RF002, RF003, RF004 e RF007; US004, US005, US006 e US010). As entidades `Category`, `Course`, `Module`, `Lesson`, `LessonMaterial`, `Quiz`, `Question` e `QuestionOption` derivam do plano técnico, do modelo do TDD e das decisões arquiteturais vigentes (PostgreSQL 16 sob ADR-0017, convenção de nomes snake_case no banco sob ADR-0015 e exclusão lógica sob ADR-0014). A relação entre `Course` e `User` (Área A) expressa a autoria via chave estrangeira `instructor_id`. As regras de integridade com as tabelas de progresso e tentativas de alunos da Área C (`LessonProgress`, `QuizAttempt` e `Enrollment`) garantem que cursos com matrículas ativas (UC006 R-2), módulos com histórico de aulas assistidas ou respostas a quizzes (UC014 R-4) e aulas com registros de progresso (UC015 R-5) tenham sua exclusão estritamente bloqueada, preservando o histórico acadêmico.

![Modelo lógico da Área B](../diagramas/12-modelo-de-dados-area-b.png)

*Figura 0 – Modelo lógico relacional da Área B (Autoria do instrutor)*

Decisões do modelo:

- **Convenção por camada e banco PostgreSQL 16 (ADR-0015, ADR-0017):** todas as tabelas e colunas são persistidas em língua inglesa e no padrão `snake_case` (ex.: `course_id`, `video_key`, `created_at`, `deleted_at`). Os tipos de dados utilizam os recursos nativos do PostgreSQL 16: identificadores primários e estrangeiros em `uuid`, strings em `varchar(n)` ou `text`, valores monetários e contadores em `integer` e `bigint`, datas com fuso horário em `timestamptz` e enumerações validadas via restrição `CHECK` (ex.: `level`, `status`, `index_status`).
- **Exclusão lógica em todo o sistema (ADR-0014):** toda tabela de negócio da Área B contém a coluna `deleted_at: timestamptz` (trait `SoftDeletes` do Eloquent). Nenhuma exclusão realiza `DELETE` físico no banco de dados. As consultas operacionais ignoram registros onde `deleted_at IS NOT NULL`.
- **Relação Módulo–Quiz resolvida (TDD seção 2):** cada `Quiz` pertence a exatamente um `Module` (`Quiz.module_id` obrigatório), e cada `Module` pode conter zero ou mais quizzes (`0..n`). Isso resolve a hierarquia pedagógica do curso, permitindo avaliações modulares pontuais ou finais de módulo.
- **Normalização até a 3ª Forma Normal (3FN):** todas as tabelas da Área B encontram-se rigorosamente na 3FN. As chaves primárias são UUIDs únicos, todos os atributos não-chave dependem exclusivamente da chave primária inteira (sem dependências parciais) e não há dependências transitivas entre atributos não-chave.
- **Bloqueio de exclusão e integridade com a Área C:**
  - A exclusão de um `Course` é bloqueada se houver alunos com matrículas ativas em `Enrollment` (UC006 R-2 e E2, retornando HTTP `409 Conflict`), permitindo apenas a alteração de status para despublicado / rascunho (`draft`) ou arquivado (`archived`).
  - A exclusão de um `Module` é bloqueada se houver histórico de alunos registrado em `LessonProgress` (para qualquer aula do módulo) ou em `QuizAttempt` (para qualquer quiz do módulo) (UC014 R-4 e E4, retornando HTTP `409 Conflict`). Caso não haja histórico, a exclusão lógica em cascata marca `deleted_at` no módulo, em suas aulas e nos seus quizzes.
  - A exclusão de uma `Lesson` é bloqueada se houver qualquer registro em `LessonProgress` (UC015 R-5 e E4, retornando HTTP `409 Conflict`). Caso contrário, a exclusão lógica preenche `deleted_at` na aula e em seus materiais complementares e aciona a remoção física dos arquivos de vídeo e materiais no storage Cloudflare R2 via `media-service`.
- **Upload via API e gestão de vídeo (UC015, RNF004, RNF018, decisões B2 e B3):** o arquivo de vídeo é enviado diretamente à API em requisição `multipart/form-data`. O backend repassa o binário ao serviço de mídia (`media-service`), que grava o objeto no Cloudflare R2 e retorna a chave persistida (`video_key: varchar(255)`), a duração em segundos (`duration_seconds: integer`), o tipo MIME (`video_mime_type: varchar(100)`) e o tamanho em bytes (`video_size_bytes: bigint`). A aula só é salva após a confirmação do upload, tornando `video_key` estritamente obrigatório. O envio de novo vídeo dispara o job assíncrono de transcrição e indexação vetorial no `ai-service` via fila RabbitMQ (RNF004), com o estado acompanhado pelo campo `index_status: text CHECK (pending, indexed, failed)`.
- **Materiais complementares da aula (decisão B4):** a tabela `LessonMaterial` (0..n por aula) armazena os anexos de apoio (ex.: apostilas em PDF com até 50 MB), guardando `title: varchar(150)`, a chave no storage (`file_key: varchar(255)`), `mime_type: varchar(100)`, `size_bytes: bigint`, a posição sequencial (`order: integer`) e `deleted_at: timestamptz`. O upload segue o mesmo fluxo da API intermediando a gravação no R2 via `media-service`.
- **Ciclo de vida do curso e status arquivado (decisão D-TC266):** a coluna `Course.status` aceita os valores `draft`, `published` e `archived`. Na exclusão de uma conta de Instrutor pelo Administrador (UC018), é oferecida a opção de arquivar seus cursos (`status = 'archived'`), o que os oculta do catálogo público para novas matrículas, preservando o acesso irrestrito aos alunos já matriculados.
- **Estrutura de Quiz, Gabarito e Retentativas (UC004 R-1, R-2):** cada `Quiz` possui status de publicação (`status: text CHECK (draft, published)`) e controle de novas tentativas (`allow_retake: boolean`, padrão `true`). Cada `Question` possui enunciado próprio e associa-se a pelo menos duas alternativas em `QuestionOption`, das quais exatamente uma possui `is_correct = true` (R-1). A edição de enunciados ou do gabarito preserva o histórico de respostas e as notas já atribuídas em `QuizAttempt` (R-2).
- **Mapeamento de Enums e Internacionalização:** conforme a arquitetura do sistema (ADR-0015), todos os valores enumerados são persistidos no banco de dados em língua inglesa (ex.: `status` em `Course` como `draft`, `published`, `archived`; `status` em `Quiz` como `draft` e `published`; `level` em `Course` como `beginner`, `intermediate` e `advanced`; `index_status` em `Lesson` como `pending`, `indexed` e `failed`). As camadas de apresentação (frontend) e de contrato da API realizam o mapeamento bidirecional desses valores para os respectivos rótulos em português exibidos ao usuário (ex.: `draft` → 'Rascunho', `published` → 'Publicado', `archived` → 'Arquivado'; `pending` → 'Pendente', `indexed` → 'Indexado', `failed` → 'Falhou'; `beginner` → 'Iniciante', `intermediate` → 'Intermediário', `advanced` → 'Avançado').
- **Valores monetários e localização:** `Course.price_cents` armazena o preço em centavos como número inteiro para evitar imprecisões de arredondamento de ponto flutuante, com `Course.currency` fixada no código ISO 4217 (`BRL` por padrão).

| ATRIBUTO | CLASSE | DOMÍNIO | TAMANHO | DESCRIÇÃO |
|---|---|---|---|---|
| **Tabela: Category** | | | | Categorias temáticas de classificação dos cursos. |
| id | Determinante | UUID | - | Identificador único da categoria (chave primária). |
| name | Simples | Texto | 80 | Nome descritivo da categoria de curso (obrigatório). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |
| **Tabela: Course** | | | | Catálogo de cursos criados por instrutores (UC006, RF002). |
| id | Determinante | UUID | - | Identificador único do curso (chave primária). |
| instructor_id | Simples | UUID | - | FK para `User.id` (Área A), identificando o instrutor proprietário do curso. |
| category_id | Simples | UUID | - | FK para `Category.id`, categorização temática do curso. |
| title | Simples | Texto | 150 | Título oficial do curso (obrigatório). |
| description | Simples | Texto longo | TEXT | Descrição detalhada do conteúdo programático (obrigatório). |
| price_cents | Simples | Inteiro | - | Preço do curso expresso em centavos (inteiro, obrigatório). |
| currency | Simples | Texto | 3 | Código ISO 4217 da moeda (padrão 'BRL', obrigatório). |
| level | Simples | Texto | 20 | Nível de dificuldade: 'beginner', 'intermediate', 'advanced' (opcional). |
| status | Simples | Texto | 20 | Estado de publicação: 'draft', 'published' ou 'archived' (obrigatório, padrão 'draft'). |
| thumbnail_key | Simples | Texto | 255 | Chave da imagem de capa no storage Cloudflare R2 (opcional). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |
| **Tabela: Module** | | | | Módulos de conteúdo programático ordenados dentro do curso (UC014, RF003). |
| id | Determinante | UUID | - | Identificador único do módulo (chave primária). |
| course_id | Simples | UUID | - | FK para `Course.id`, curso ao qual o módulo pertence. |
| title | Simples | Texto | 150 | Título descritivo do módulo (obrigatório). |
| order | Simples | Inteiro | - | Posição sequencial do módulo dentro do curso (única por curso, obrigatório). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |
| **Tabela: Lesson** | | | | Unidade de aula em vídeo com metadados e indexação vetorial (UC015, RF004). |
| id | Determinante | UUID | - | Identificador único da aula (chave primária). |
| module_id | Simples | UUID | - | FK para `Module.id`, módulo ao qual a aula pertence. |
| title | Simples | Texto | 150 | Título da aula (obrigatório). |
| description | Simples | Texto longo | TEXT | Descrição do conteúdo da aula (opcional). |
| video_key | Simples | Texto | 255 | Chave do arquivo de vídeo no storage Cloudflare R2 (obrigatório após upload). |
| duration_seconds | Simples | Inteiro | - | Duração total do vídeo em segundos (opcional). |
| video_mime_type | Simples | Texto | 100 | Tipo MIME do arquivo de vídeo (ex.: 'video/mp4', 'video/webm'). |
| video_size_bytes | Simples | Inteiro grande | - | Tamanho do arquivo de vídeo em bytes (até 500 MB). |
| order | Simples | Inteiro | - | Posição sequencial da aula dentro do módulo (obrigatório). |
| is_preview | Simples | Booleano | - | Flag indicando se a aula pode ser assistida gratuitamente como degustação (padrão false). |
| index_status | Simples | Texto | 20 | Status da indexação vetorial para o Tutor de IA: 'pending', 'indexed', 'failed' (obrigatório, padrão 'pending'). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |
| **Tabela: LessonMaterial** | | | | Arquivos complementares de apoio vinculados à aula (UC015, RF004, decisão B4). |
| id | Determinante | UUID | - | Identificador único do material complementar (chave primária). |
| lesson_id | Simples | UUID | - | FK para `Lesson.id`, aula à qual o material pertence. |
| title | Simples | Texto | 150 | Título descritivo do material (obrigatório). |
| file_key | Simples | Texto | 255 | Chave do arquivo de documento no storage Cloudflare R2 (obrigatório). |
| mime_type | Simples | Texto | 100 | Tipo MIME do arquivo (ex.: 'application/pdf', obrigatório). |
| size_bytes | Simples | Inteiro grande | - | Tamanho do arquivo em bytes (até 50 MB, obrigatório). |
| order | Simples | Inteiro | - | Posição sequencial do material dentro da aula (obrigatório). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |
| **Tabela: Quiz** | | | | Avaliações objetivas vinculadas aos módulos do curso (UC004, RF007). |
| id | Determinante | UUID | - | Identificador único do quiz (chave primária). |
| module_id | Simples | UUID | - | FK para `Module.id`, vinculando o quiz ao módulo correspondente. |
| title | Simples | Texto | 150 | Título do quiz (obrigatório). |
| status | Simples | Texto | 20 | Estado de publicação do quiz: 'draft' ou 'published' (obrigatório, padrão 'draft'). |
| allow_retake | Simples | Booleano | - | Flag indicando se novas tentativas de resolução são permitidas após submissão (padrão true, obrigatório). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |
| **Tabela: Question** | | | | Questões avaliativas que compõem o quiz (UC004, RF007). |
| id | Determinante | UUID | - | Identificador único da questão (chave primária). |
| quiz_id | Simples | UUID | - | FK para `Quiz.id`, quiz proprietário da questão. |
| text | Simples | Texto longo | TEXT | Enunciado da questão (obrigatório). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |
| **Tabela: QuestionOption** | | | | Alternativas de resposta e gabarito oficial da questão (UC004, RF007). |
| id | Determinante | UUID | - | Identificador único da alternativa (chave primária). |
| question_id | Simples | UUID | - | FK para `Question.id`, questão à qual a alternativa pertence. |
| text | Simples | Texto longo | TEXT | Texto descritivo da alternativa (obrigatório). |
| is_correct | Simples | Booleano | - | Indica se a alternativa compõe o gabarito oficial (obrigatório). |
| deleted_at | Simples | Data e hora | - | Timestamp de exclusão lógica (ADR-0014); nulo se ativo. |

---
id: sdd
titulo: "SDD — Software Design Document"
tipo: documento-projeto
status: rascunho
atualizado: 2026-10-07
---
# SDD — Software Design Document

> Rascunho. Regras de escrita no [CONTEXT.md](../CONTEXT.md). O que não vem da especificação, das ADRs ou da pesquisa vai marcado como proposta (`<!-- proposta: motivo -->`). Modelo de dados detalhado no TDD.

## 1. Visão da arquitetura

A Plataforma de Cursos é um sistema web com front-end separado de uma API central. A API concentra as regras de negócio das quatro áreas (A a D) e é a única a falar com o banco, com o armazenamento de vídeo e com os serviços externos. A especificação sustenta três pontos de arquitetura: autenticação por token JWT com rotas protegidas por perfil (RNF001), upload e entrega de vídeo por URL assinada (RNF002) e um Tutor de IA que consulta só o material do próprio curso (RAG restrito por `course_id`).

A arquitetura adota o estilo monólito modular (API única dividida por áreas A a D com Laravel 13) integrado a um front-end SPA em Next.js e microsserviços físicos dedicados para IA e mídia, conforme definido no [ADR-0007](adr/0007-stack-e-bancos.md). Motivo: equipe de 4 integrantes (uma área por integrante, conforme [ADR-0006](adr/0006-divisao-por-areas.md)) e alta coesão de domínio no core, isolando fisicamente apenas serviços com cargas computacionais e dependências especializadas (`ai-service` e `media-service`).

O Tutor de IA é ator sistêmico (ADR-0005): recebe a pergunta do Aluno com o contexto da aula e devolve a resposta.

### 1.1 C4 nível 1 — Contexto

```mermaid
flowchart TB
    visitante["Visitante<br/>navega pelo catálogo, cadastra-se e faz login"]
    aluno["Aluno<br/>matricula-se, assiste, responde quizzes, avalia e conversa com o Tutor de IA"]
    instrutor["Instrutor<br/>cadastra cursos, módulos, aulas e quizzes; vê o dashboard"]
    admin["Administrador<br/>gerencia usuários e vê o dashboard da plataforma"]

    plataforma["Plataforma de Cursos<br/>sistema web de cursos online"]

    tutor["Tutor de IA<br/>ator sistêmico: responde com base no conteúdo do curso"]
    storage["Armazenamento de vídeo<br/>externo"]
    email["Serviço de e-mail<br/>externo"]

    visitante -->|"usa"| plataforma
    aluno -->|"usa"| plataforma
    instrutor -->|"usa"| plataforma
    admin -->|"usa"| plataforma
    plataforma -->|"pergunta + trechos do curso"| tutor
    tutor -->|"resposta com aula e timestamp"| plataforma
    plataforma -->|"URL assinada, vídeo"| storage
    plataforma -->|"link de redefinição de senha"| email
```

O pagamento é simulado dentro da própria plataforma, sem gateway externo (RF014), por isso não aparece como sistema externo.

## 2. Contêineres

### 2.1 C4 nível 2

```mermaid
flowchart TB
    usuario["Visitante, Aluno, Instrutor, Administrador"]

    subgraph plataforma["Plataforma de Cursos"]
        web["Front-end web<br/>SPA responsiva, pt-BR e en, modo claro/escuro"]
        api["API<br/>regras de negócio das áreas A a D, JWT, documentação OpenAPI"]
        tutorsvc["Serviço do Tutor de IA<br/>transcrição, embeddings, busca por similaridade, geração de resposta"]
        db[("Banco de dados<br/>dados relacionais e índice de embeddings")]
        fila["RabbitMQ<br/>mensageria AMQP: jobs de transcrição e ingestão vetorial"]
    end

    r2["Armazenamento de vídeo (R2)<br/>externo"]
    llm["Provedor do modelo de linguagem<br/>externo"]
    mail["Serviço de e-mail<br/>externo"]

    usuario -->|"HTTPS"| web
    web -->|"HTTPS/JSON, token JWT"| api
    web -->|"upload e reprodução por URL assinada"| r2
    api -->|"URL assinada (15 min)"| r2
    api -->|"leitura e escrita"| db
    api -->|"pergunta do Aluno e contexto da aula"| tutorsvc
    api -->|"publica jobs de transcrição e ingestão"| fila
    fila -->|"consome jobs"| tutorsvc
    tutorsvc -->|"trechos indexados do curso"| db
    tutorsvc -->|"leitura do vídeo, transcrição"| r2
    tutorsvc -->|"prompt com trechos, resposta em streaming"| llm
    api -->|"envio de e-mail"| mail
```

| Contêiner | Responsabilidade | Origem da definição |
|---|---|---|
| Front-end web | Telas de todos os perfis; chat do Tutor de IA ao lado do vídeo; validação de campo obrigatório com mensagem de erro (RNF005); layout de 360 a 1920 px (RNF019); textos em pt-BR e en (RNF013); modo escuro (RNF014) | especificação (RNF005, RNF013, RNF014, RNF019, UC001) |
| API | Autenticação e perfis, cursos, módulos, aulas, matrícula, pagamento simulado, progresso, quiz com correção automática, avaliação, dashboard, administração; documentação OpenAPI online (RNF015) | especificação |
| Serviço do Tutor de IA | Transcrever a aula, gerar embeddings uma única vez por aula (RNF004), buscar trechos restritos ao curso, gerar resposta com aula e timestamp, responder em streaming (RNF003) | especificação |
| Mensageria (RabbitMQ) | Fila AMQP entre a API e o Serviço do Tutor de IA para os jobs de transcrição e ingestão vetorial, executados em background | Proposta (TDD, seção de tecnologias) |
| Banco de dados | Entidades do dicionário de dados da especificação (seção 5); histórico de conversa do Tutor de IA | especificação |
| Armazenamento de vídeo | Arquivos de vídeo, referenciados por `videoKey` (storage R2) | especificação (dicionário de dados) |

A stack tecnológica e os bancos de dados seguem a decisão do grupo registrada no [ADR-0007](adr/0007-stack-e-bancos.md):
- **Front-end:** Next.js com TypeScript arquitetado como SPA (sem Server Components ou Server Actions).
- **API (Core):** Laravel 13 / PHP 8.3 estruturado como monólito modular (módulos auth, catalog, learning e analytics).
- **Banco de dados do Core:** MySQL 8 como SGBD relacional primário para todas as entidades do sistema.
- **Serviço do Tutor de IA (`ai-service`):** Serviço físico separado rodando em seu próprio container (Laravel 13 / PHP 8.3) com banco de dados dedicado **PostgreSQL 16 com extensão pgvector** para índice vetorial HNSW e busca restrita a `course_id`. A separação física isola a dependência de LLM, pipelines assíncronos de transcrição/embeddings e a carga pesada de cálculo vetorial.
- **Armazenamento de mídia (`media-service`):** Serviço separado com storage Cloudflare R2 para vídeos (`videoKey`).
- **Mensageria:** RabbitMQ 3.13+ com protocolo AMQP, para os jobs assíncronos de transcrição e ingestão vetorial entre a API e o `ai-service`.

## 3. Componentes

C4 nível 3 da API, organizada por área (ADR-0006).

```mermaid
flowchart TB
    web["Front-end web"]

    subgraph api["API"]
        subgraph areaA["Área A: Acesso e conta"]
            auth["Autenticação<br/>cadastro, login, recuperar senha"]
            perfil["Perfil do usuário<br/>dados cadastrais e endereços"]
        end
        subgraph areaB["Área B: Autoria do instrutor"]
            cursos["Cursos e categorias"]
            modaulas["Módulos e aulas<br/>upload por URL assinada"]
            quizaut["Quiz e gabarito"]
            perfinstr["Perfil do instrutor"]
        end
        subgraph areaC["Área C: Aprendizagem do aluno"]
            catalogo["Catálogo e busca"]
            matricula["Matrícula e pagamento simulado"]
            progresso["Progresso e retomada de aula"]
            quizresp["Resposta de quiz e nota"]
            avaliacao["Avaliação do curso"]
        end
        subgraph areaD["Área D: Tutor de IA, analytics e administração"]
            chat["Conversa com o Tutor de IA<br/>limite de mensagens, histórico"]
            dash["Dashboard com filtro de período e curso"]
            usuarios["Gerenciamento de usuários e auditoria"]
            guarda["Controle de acesso por perfil"]
        end
    end

    web --> guarda
    guarda --> auth
    guarda --> cursos
    guarda --> matricula
    guarda --> chat
    guarda --> dash
    guarda --> usuarios
    matricula --> cursos
    quizresp --> quizaut
    progresso --> modaulas
    avaliacao --> matricula
    dash --> progresso
    dash --> quizresp
```

| Área | Componente | Casos de uso e RFs que atende (especificação) |
|---|---|---|
| A | Autenticação | UC005 Realizar Login, UC012 (cadastro), UC011 Recuperar Senha; RF001, RF013, RF017 |
| A | Perfil do usuário | UC013 Editar Dados do Perfil, UC017 Alterar Senha; RF001, RF019 |
| B | Cursos e categorias | UC006 Cadastrar Curso; RF002 |
| B | Módulos e aulas | UC014, UC015; RF003, RF004 |
| B | Quiz e gabarito | UC004 Cadastrar Quiz com Gabarito; RF007 |
| B | Perfil do instrutor | UC013 (fluxo A1); RF016 |
| C | Catálogo e busca | UC020 Consultar Catálogo de Cursos; RF015 |
| C | Matrícula e pagamento simulado | UC003 Matricular-se em Curso, UC019 Processar Pagamento Simulado; RF005, RF014 |
| C | Progresso | UC009 Assistir Aula; RF006 |
| C | Resposta de quiz | UC002 Responder Quiz; RF008 |
| C | Avaliação do curso | UC010 Avaliar Curso; RF011 |
| D | Conversa com o Tutor de IA | UC001 Conversar com Tutor de IA; RF009 |
| D | Dashboard | UC007 Ver Dashboard com Filtro; RF010 |
| D | Usuários e auditoria | UC008 Gerenciar Usuários, UC018 Excluir e Anonimizar Usuário; RF012; RNF016 |
| D | Controle de acesso por perfil | UC016 Acessar Área Protegida por Perfil; RF018; RNF001 |

<!-- proposta: a divisão em componentes, os nomes e as dependências entre eles não constam na especificação, que traz só casos de uso e diagramas de sequência. Foram derivados dos RFs e das regras de negócio dos casos de uso. Motivo: C4 nível 3 exige componentes -->

### 3.1 Fluxo principal do Tutor de IA

Baseado no fluxo básico e nas exceções do UC001.

```mermaid
sequenceDiagram
    actor Aluno
    participant Web as Front-end web
    participant API
    participant Tutor as Serviço do Tutor de IA
    participant DB as Banco de dados
    participant LLM as Provedor do modelo de linguagem

    Aluno->>Web: digita a pergunta na página da aula
    Web->>API: pergunta (token JWT, curso, aula)
    API->>API: verifica perfil, matrícula e limite de mensagens
    API->>Tutor: pergunta e course_id
    Tutor->>DB: busca por similaridade restrita ao course_id
    alt aula sem embeddings (E-1)
        Tutor-->>API: conteúdo ainda em preparação
        API-->>Web: aviso para tentar mais tarde
    else sem correspondência no material (A-1)
        Tutor-->>API: sem informação no material do curso
        API-->>Web: aviso e sugestão de reformular
    else com trechos relevantes
        Tutor->>LLM: pergunta e trechos do curso
        LLM-->>Tutor: resposta em streaming
        Tutor-->>API: resposta com aula e timestamp de origem
        API->>DB: salva mensagem e resposta no histórico
        API-->>Web: resposta em streaming
        Web-->>Aluno: bolha de resposta com aula e timestamp
    end
```

### 3.2 Matrícula com pagamento simulado

Baseado no UC003 e no RF014.

```mermaid
sequenceDiagram
    actor Aluno
    participant Web as Front-end web
    participant API
    participant DB as Banco de dados

    Aluno->>Web: aciona Matricular-se na página do curso
    Web->>API: solicita matrícula (token JWT, curso)
    API->>DB: verifica curso publicado e matrícula existente
    alt curso em rascunho (E-1)
        API-->>Web: curso não encontrado
    else já matriculado (A-1)
        API-->>Web: exibe Continuar assistindo
    else curso gratuito (A-2)
        API->>DB: registra matrícula ativa, sem pagamento
        API-->>Web: curso em meus cursos
    else curso pago
        API->>DB: registra matrícula pendente
        API->>API: processa pagamento simulado, sem gateway externo
        alt pagamento recusado (E-2)
            API->>DB: registra Payment recusado, matrícula segue pendente
            API-->>Web: 422 PAYMENT_DECLINED, nova tentativa permitida
        else pagamento aprovado
            API->>DB: registra Payment aprovado e muda a matrícula para ativa
            API-->>Web: curso em meus cursos
        end
    end
```

## 4. Integrações externas

| Integração | O que trafega | Falha | Fallback |
|---|---|---|---|
| Provedor do modelo de linguagem (Tutor de IA) | Pergunta do Aluno e trechos do curso recuperados por similaridade; resposta em streaming | Sem fonte na especificação para o comportamento em indisponibilidade | Sem fonte na especificação. |
| Armazenamento e entrega de vídeo (R2) | Arquivo de vídeo, por URL assinada de envio com validade de 15 min (RNF002); `videoKey` guardada no banco; reprodução por URL assinada | Upload com URL expirada ou indisponível: o sistema informa o erro e gera nova URL assinada (UC015, E-2); falha na entrega do vídeo na reprodução (UC009) | Nova URL assinada para nova tentativa (especificação, UC015) |
| Envio de e-mail (recuperar senha) | Link de redefinição, com validade de 30 minutos (UC011) | Sem fonte na especificação | Sem fonte na especificação. |
| Pagamento | Não há integração externa: o pagamento é simulado (RF014; entidade Payment com status aprovado ou recusado) | Pagamento recusado: fica registrado como recusado, a matrícula segue pendente (sem acesso) e a API responde 422 PAYMENT_DECLINED; nova tentativa permitida (UC019, E-1) | Nova tentativa pelo Aluno |

<!-- proposta: provedor de e-mail transacional (por exemplo, serviço SMTP ou API de e-mail) com envio assíncrono e nova solicitação pelo usuário em caso de falha. A especificação diz que o e-mail é enviado, mas não escolhe serviço nem trata falha. Motivo: o fluxo de recuperar senha depende do envio -->

<!-- proposta: provedor do modelo de linguagem ainda não escolhido; a escolha deve considerar custo por token, região de processamento (LGPD) e suporte a streaming (RNF003). Fallback proposto: mensagem de indisponibilidade ao Aluno, sem resposta gerada fora do material do curso. Motivo: a especificação define o comportamento do tutor, não o fornecedor -->

<!-- proposta: transcrição das aulas feita por serviço de reconhecimento de fala (a escolher), executada uma vez por aula após o upload (RNF004). A especificação diz que a plataforma transcreve e indexa as aulas, sem indicar o mecanismo. Motivo: sem a transcrição não há timestamp de origem na citação -->

## 5. Dados e armazenamento

O detalhamento completo dos campos, tipos, tamanhos e regras de normalização de cada entidade está documentado no [Dicionário de dados do TDD](tdd.md#dicionário-de-dados).

| Dado | Onde fica | Observação |
|---|---|---|
| Usuário, endereços, perfil do instrutor | Banco de dados | Entidades User, Address, InstructorProfile. `passwordHash` guarda só o hash da senha (RNF007). `documentNumber` (CPF) e `birthDate` são dados pessoais. `socialLinks` é campo JSON, exceção conhecida à 1FN por decisão do Plano Técnico |
| Curso, módulo, aula, categoria | Banco de dados | Entidades Category, Course, Module, Lesson. Preço em centavos e moeda ISO 4217 |
| Vídeo da aula e imagem de capa | Armazenamento de vídeo (R2) | Banco guarda só `videoKey` e `thumbnailKey` |
| Matrícula, pagamento simulado, progresso | Banco de dados | Entidades Enrollment, Payment, LessonProgress (`watchedSeconds` para retomar de onde parou) |
| Quiz, perguntas, alternativas, gabarito, tentativas, respostas | Banco de dados | Entidades Quiz, Question, QuestionOption (`isCorrect` é o gabarito), QuizAttempt, QuizAnswer |
| Avaliação do curso | Banco de dados | Entidade Review, nota de 1 a 5 e comentário |
| Transcrição, embeddings e histórico de conversa do Tutor de IA | Banco de dados | Gerados uma única vez por aula (RNF004); busca restrita por `course_id`. O histórico de mensagens e respostas por Aluno é guardado nas entidades Conversation e Message (UC001, seção 5.1). Entidades ainda não constam no dicionário de dados da especificação |
| Trilha de auditoria das ações administrativas | Banco de dados | Registro de 100% das ações, retido por 12 meses (RNF016) |
| Backup | Banco de dados | Backup diário, com restauração testada mensalmente (RNF011) |

<!-- proposta: tabelas LessonTranscript (transcrição com marcação de tempo), LessonEmbedding (vetor, trecho, timestamp, course_id) e AuditLog (autor, ação, data). O dicionário da especificação não traz essas entidades, embora o UC001 e o RNF004 exijam os dados. Motivo: dar lugar aos dados que a especificação manda gerar e guardar -->

<!-- proposta: retenção de dados pessoais após exclusão da conta. A especificação diz, na estória US016, que os dados pessoais são removidos e o histórico de matrícula e pagamento permanece anonimizado, mas não fixa prazo. Prazos de retenção do histórico de conversa e dos arquivos de vídeo ficam para decisão do grupo -->

### 5.1 Modelo de classes de domínio

Transcrito do dicionário de dados da especificação original (seção 12). O diagrama de classes da especificação original (figura 14) é imagem e não foi reproduzido; este diagrama é uma reconstrução a partir dos atributos e das referências do dicionário. As entidades `Conversation` e `Message` (histórico do Tutor de IA, UC001) e os campos `userId`, `courseId` e `enrollmentId` de `Payment` não constam no dicionário da especificação; seguem o TDD.

```mermaid
classDiagram
    class User {
        +id
        +name
        +email
        +passwordHash
        +role
        +photo
        +theme
        +phone
        +documentNumber
        +birthDate
        +status
    }
    class Address {
        +id
        +type
        +street
        +number
        +city
        +state
        +zipCode
        +country
        +isDefault
    }
    class InstructorProfile {
        +bio
        +headline
        +socialLinks
    }
    class Category {
        +id
        +name
    }
    class Course {
        +id
        +title
        +description
        +priceCents
        +currency
        +level
        +status
        +thumbnailKey
    }
    class Module {
        +id
        +title
        +order
    }
    class Lesson {
        +id
        +title
        +videoKey
        +durationSeconds
        +order
        +isPreview
    }
    class Enrollment {
        +id
        +pricePaidCents
        +currency
        +status
    }
    class LessonProgress {
        +id
        +completed
        +watchedSeconds
        +completedAt
    }
    class Quiz {
        +id
        +title
    }
    class Question {
        +id
        +text
    }
    class QuestionOption {
        +id
        +text
        +isCorrect
    }
    class QuizAttempt {
        +id
        +score
        +submittedAt
    }
    class QuizAnswer {
        +id
    }
    %% Payment: referencia a matrícula pendente criada antes do pagamento
    class Payment {
        +id
        +userId
        +courseId
        +enrollmentId
        +amountCents
        +currency
        +status
        +paidAt
    }
    class Review {
        +id
        +rating
        +comment
    }
    class Conversation {
        +id
        +userId
        +courseId
        +lessonId
        +createdAt
    }
    class Message {
        +id
        +conversationId
        +role
        +content
        +timestampRef
        +createdAt
    }

    User "1" --> "*" Address
    User "1" --> "0..1" InstructorProfile
    User "1" --> "*" Course : instrutor
    Category "1" --> "*" Course
    Course "1" --> "*" Module
    Module "1" --> "*" Lesson
    Module "1" --> "*" Quiz
    Quiz "1" --> "*" Question
    Question "1" --> "*" QuestionOption
    User "1" --> "*" Enrollment : aluno
    Course "1" --> "*" Enrollment
    Enrollment "1" --> "*" LessonProgress
    Lesson "1" --> "*" LessonProgress
    Enrollment "1" --> "*" QuizAttempt
    Quiz "1" --> "*" QuizAttempt
    QuizAttempt "1" --> "*" QuizAnswer
    Question "1" --> "*" QuizAnswer
    QuestionOption "1" --> "*" QuizAnswer
    Payment "1" --> "1" Enrollment
    User "1" --> "*" Review
    Course "1" --> "*" Review
    User "1" --> "*" Conversation
    Conversation "1" --> "*" Message
```

<!-- proposta: multiplicidades do diagrama (por exemplo, InstructorProfile 0..1 por User, Payment 1 para 1 Enrollment, pois a matrícula pendente existe antes do pagamento). O dicionário da especificação só informa as chaves de referência, não a cardinalidade. Motivo: o classDiagram exige multiplicidade -->

## 6. Segurança

| Tema | Decisão | Origem |
|---|---|---|
| Autenticação | Token JWT de acesso com expiração de 1 h, assinado com RS256 (biblioteca `php-open-source-saver/jwt-auth`; os serviços de mídia e de IA validam com a chave pública, ADR-0008), em cookie HttpOnly, Secure e SameSite. Com a opção "manter conectado" marcada no login, a sessão é renovada por refresh token com rotação, em cookie HttpOnly de vida longa, sem novo login. Sem a opção, a sessão termina ao expirar o token de acesso | especificação (RNF001, UC005); cookie, refresh token e opção "manter conectado": decisão arquitetural deste SDD, detalhe em ADR a criar |
| Perfis e área protegida (área D) | Perfis aluno, instrutor e administrador; 100% das rotas protegidas verificam o perfil; acesso negado redireciona o usuário à própria área | especificação (RNF001, US015, UC016) |
| Senhas | Armazenadas só com hash; mínimo de 8 caracteres, com letra e número | especificação (RNF007, UC012) |
| Enumeração de usuários | Mensagem de login inválido e de recuperação de senha não revela se o e-mail existe | especificação (UC005, UC011) |
| Bloqueio de login | 15 min após 5 tentativas inválidas consecutivas | especificação (RNF008) |
| Recuperação de senha | Link de redefinição com validade de 30 minutos | especificação (UC011) |
| Vídeo | Upload e reprodução só por URL assinada, com expiração de 15 min; sem acesso direto ao armazenamento | especificação (RNF002) |
| Matrícula | Só o Aluno matriculado acessa as aulas, salvo aula marcada como prévia (`isPreview`) | especificação (US006, UC003) |
| Tutor de IA | Responde só com base no material do próprio curso (RAG restrito por `course_id`); limite de mensagens por Aluno por período | especificação (UC001) |
| LGPD | Aceite de termos e política de privacidade registrado em 100% dos cadastros; dados pessoais removidos na exclusão da conta, com histórico anonimizado | especificação (RNF020, UC012, US016) |
| Administração | Registro de 100% das ações administrativas, retido por 12 meses; o administrador não bloqueia a própria conta | especificação (RNF016, US016) |

<!-- proposta: a API envia política de CORS restrita ao domínio do front-end. A especificação não trata de CORS. Motivo: limita quais origens podem usar a sessão do usuário no navegador -->

<!-- proposta: mensagens ao provedor do modelo de linguagem não incluem nome, e-mail, CPF nem outros dados pessoais do Aluno; seguem só a pergunta e os trechos do curso. Motivo: a especificação pede LGPD (RNF020), mas não trata do envio de dados a terceiros -->

## 7. Qualidade

Como a arquitetura atende os RNFs do item 8 (ISO/IEC 25010). RNFs conforme o item 8.

| RNF | Característica | Meta | Como a arquitetura atende |
|---|---|---|---|
| RNF001 | Segurança | Token de 1 h; 100% das rotas verificam perfil | Controle de acesso por perfil na API (componente da área D), antes de qualquer componente de negócio |
| RNF002 | Segurança | URL assinada de 15 min; 0 acessos diretos | A API gera a URL; o front-end nunca recebe credencial do armazenamento |
| RNF003 | Eficiência de desempenho | Primeiro trecho da resposta do Tutor de IA em até 3 s (p95) | Resposta em streaming do provedor até o chat |
| RNF004 | Eficiência de desempenho | 0 reprocessamentos por aula | Transcrição e embeddings guardados no banco e gerados uma vez, após o upload |
| RNF005 | Capacidade de interação | 100% dos campos obrigatórios validados com mensagem de erro clara | Front-end SPA com validação nos formulários |
| RNF006 | Manutenibilidade | Cobertura de testes de 75% no backend, com merge bloqueado abaixo | Verificação de cobertura no pipeline de integração contínua |
| RNF007 | Segurança | 0 senhas em texto puro (armazenadas com hash) | Hash de senha na área A |
| RNF008 | Segurança | Bloqueio de 15 min após 5 tentativas | Contador de tentativas na autenticação (área A) |
| RNF009 | Eficiência de desempenho | p95 das listagens de até 2 s com 1000 usuários simultâneos | API sem estado (JWT), que permite várias instâncias; toda listagem é paginada; a API não devolve campo que o front-end não use |
| RNF010 | Confiabilidade | Disponibilidade mensal mínima de 99% | Sem fonte na especificação para o mecanismo |
| RNF011 | Confiabilidade | Backup diário; restauração testada mensalmente | Backup do banco de dados, que concentra os dados da plataforma |
| RNF012 | Capacidade de interação (inclusividade) | WCAG 2.1 AA; contraste 4,5:1; navegação por teclado | Front-end com componentes acessíveis e revisão de contraste |
| RNF013 | Capacidade de interação | pt-BR e en em 100% dos textos; datas e valores por idioma | Textos em arquivos de tradução e formatação por localidade |
| RNF014 | Capacidade de interação | Claro/escuro em 100% das telas, preferência salva por usuário | Tema no front-end; preferência persistida no perfil |
| RNF015 | Manutenibilidade | 100% dos endpoints em OpenAPI, online | API documentada em OpenAPI e publicada |
| RNF016 | Segurança | 100% das ações administrativas registradas, por 12 meses | Registro de auditoria no componente de gerenciamento de usuários |
| RNF017 | Segurança | Link de redefinição de senha de uso único, com expiração de 30 min | Token de uso único com validade de 30 min, gerado na área A e enviado por e-mail |
| RNF018 | Eficiência de desempenho | Vídeo de aula aceito somente em mp4 ou webm, com até 500 MB por arquivo | Validação de tipo e tamanho na emissão da URL assinada de envio (área B) |
| RNF019 | Flexibilidade | Layout funcional de 360 a 1920 px de largura | Front-end SPA responsiva, mesmo componente de layout do RNF005 |
| RNF020 | Segurança | Aceite de termos e da política de dados pessoais (LGPD) registrado em 100% dos cadastros | Campo de aceite no cadastro (área A) |
| RNF021 | Manutenibilidade | Cobertura de testes de 75% no frontend, com merge bloqueado abaixo | Verificação de cobertura (Vitest) no pipeline de integração contínua |

<!-- proposta: balanceador e mais de uma instância da API, cache de listagens e hospedagem com réplica ou reinício automático para atingir 1000 usuários simultâneos (RNF009) e 99% de disponibilidade (RNF010). A especificação define as metas, não o mecanismo. Motivo: a API sem estado permite escalar horizontalmente -->

<!-- proposta: preferência de tema (RNF014: claro, escuro ou sistema) persistida no perfil do usuário, em campo `theme` que o dicionário de dados da especificação não traz (a entidade User da especificação tem `locale`, removido porque o sistema é monoidioma). Motivo: a meta exige preferência salva por usuário -->

<!-- proposta: matriz de rastreabilidade RNF para componente fica para o TDD. Motivo: o item 8 está dividido por área (ADR-0006) e a renumeração definitiva dos RNFs ainda não foi feita (ADR-0001) -->

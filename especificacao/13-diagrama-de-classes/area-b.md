## 2. Área B – Autoria do instrutor

Classes dos casos de uso UC004, UC006, UC014 e UC015 (RF002, RF003, RF004 e RF007), estruturadas em perspectiva negocial e perspectivas de implementação técnica aderentes à arquitetura MVC do Laravel.

Na perspectiva negocial, `Instructor` herda da classe base abstrata `User` (Área A) e mantém a relação de autoria com `Course`. Um `Course` categoriza-se via `Category` e compõe recursivamente sua árvore pedagógica através de `Module`, o qual compõe suas unidades de conteúdo `Lesson` e suas avaliações `Quiz`. Cada `Quiz` é composto por instâncias de `Question`, que por sua vez compõem suas alternativas em `QuestionOption`. As classes referenciam estritamente tipos fortes de domínio (`level: CourseLevel`, `status: CourseStatus`, `course: Course`, `module: Module`), em total conformidade com as diretrizes do TE5_1, banindo referências a IDs escalares de chaves estrangeiras nos atributos de domínio.

Nas perspectivas de implementação, os controladores REST recebem requisições HTTP mapeadas nos endpoints do TDD (seção 3.3), validadas por Form Requests dedicados (`CreateCourseRequest`, `UpdateCourseRequest`, `CreateModuleRequest`, `UpdateModuleRequest`, `CreateLessonRequest`, `UpdateLessonRequest`, `AddLessonMaterialRequest`, `CreateQuizRequest`, `UpdateQuizRequest`) que encapsulam regras de validação e convertem entradas em DTOs imutáveis (`CourseDTO`, `ModuleDTO`, `LessonDTO`, `LessonMaterialDTO`, `StoredFileDTO`, `QuizDTO`, `QuestionDTO`, `QuestionOptionDTO`). Todas as exceções de negócio e validação seguem o padrão unificado `ApiException(code: ErrorCode, httpStatus, fields)` utilizando os códigos de erro padronizados do TDD (seção 3.1). Os controladores (`InstructorCourseController`, `ModuleController`, `InstructorLessonController`, `InstructorQuizController`) delegam a lógica de negócio aos serviços de domínio (`CourseService`, `ModuleService`, `LessonService`, `QuizAuthoringService`), que orquestram as operações e aplicam as travas de integridade:
- `CourseService.delete()` valida a ausência de matrículas ativas (`hasActiveEnrollments`), bloqueando a remoção de cursos já consumidos por alunos (UC006 R-2). Os cursos suportam os estados de ciclo de vida definidos em `CourseStatus` (`DRAFT`, `PUBLISHED`, `ARCHIVED`), além de exclusão lógica via `deleted_at` (ADR-0014).
- `ModuleService.delete()` inspeciona se há histórico acadêmico (`hasStudentHistory`) antes de autorizar a exclusão, bloqueando a destruição de módulos com progresso em aulas ou respostas a quizzes (UC014 R-4).
- `LessonService.delete()` verifica registros de progresso de alunos (`hasStudentProgress`), impedindo a exclusão de aulas assistidas (UC015 R-5). Em caso de exclusão autorizada, a remoção lógica da aula (`deleted_at`) remove também os materiais vinculados e apaga os arquivos de mídia no storage.
- `LessonService.uploadVideo()` realiza o envio direto do vídeo à API multipart (`media-service`), armazenando o arquivo via `MediaStorageInterface.uploadFile()` e retornando os metadados do arquivo (`StoredFileDTO`). A chave do vídeo (`videoKey`) é obrigatória na criação da aula (`LessonService.create()`), disparando o job assíncrono de transcrição e indexação via `TranscriptionQueueInterface` (RNF004).
- `LessonService.addMaterial()` e `LessonService.deleteMaterial()` gerenciam os materiais complementares em PDF (até 50 MB) da aula através da entidade `LessonMaterial`.
- `QuizAuthoringService.validateQuestions()` assegura que toda questão possua ao menos 2 opções e exatamente uma correta (UC004 R-1), garantindo que alterações de gabarito preservem o histórico de tentativas e notas já calculadas (UC004 R-2).

As respostas para a camada cliente são padronizadas através de API Resources (`CourseResource`, `ModuleResource`, `LessonResource`, `LessonMaterialResource`, `QuizResource`).

![Classes negociais da Área B](../diagramas/13-classes-area-b-negocial.png)

*Figura 0 – Diagrama de classes da Área B: perspectiva negocial*

![Classes de implementação da Área B: cursos e módulos](../diagramas/13-classes-area-b-implementacao-cursos-modulos.png)

*Figura 0 – Diagrama de classes da Área B: implementação (MVC) de cursos e módulos*

![Classes de implementação da Área B: aulas](../diagramas/13-classes-area-b-implementacao-aulas.png)

*Figura 0 – Diagrama de classes da Área B: implementação (MVC) de aulas e upload de vídeo*

![Classes de implementação da Área B: quizzes e gabarito](../diagramas/13-classes-area-b-implementacao-quizzes.png)

*Figura 0 – Diagrama de classes da Área B: implementação (MVC) de quizzes e gabarito*

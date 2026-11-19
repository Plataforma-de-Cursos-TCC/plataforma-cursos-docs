## 3. Área C – Aprendizagem do aluno

Tabelas que sustentam a matrícula do aluno, o processamento de pagamento simulado, o registro contínuo de progresso nas aulas, a realização de quizzes com correção automática e a avaliação de cursos (UC002, UC003, UC009, UC010, UC019 e UC020; RF005, RF006, RF008, RF011, RF014 e RF015). `Enrollment`, `Payment`, `LessonProgress`, `QuizAttempt`, `QuizAnswer` e `Review` derivam do TDD (seção 2) e das regras de negócio do item 10. Chaves estrangeiras conectam este núcleo aos domínios de Acesso (`User`, Área A) e Autoria (`Course`, `Lesson`, `Quiz`, `Question` e `QuestionOption`, Área B).

![Modelo lógico da Área C](../diagramas/12-modelo-de-dados-area-c.png)

*Figura 0 – Modelo lógico relacional da Área C (Aprendizagem do aluno)*

Decisões do modelo:

- `Enrollment.status` estrutura formalmente o ciclo de vida da matrícula nos valores `pending`, `active`, `cancelled` e `completed` (UC003, UC019; US007, US018). Em curso gratuito, a matrícula nasce diretamente com status `active` (UC003 R-4). Em curso pago, nasce como `pending` e passa a `active` somente após a confirmação e aprovação do pagamento simulado (UC003 R-3, UC019). A tabela possui chave única composta sobre `(userId, courseId)`, impedindo matrículas duplicadas para o mesmo curso (UC003 R-2, UC019 E3).
- `Payment` materializa o registro transacional do pagamento simulado (decisão #51, ADR-0007), sem campos de cartão de crédito, dados bancários ou `payoutInfo`. Armazena o valor (`amountCents`), moeda (`currency`), data (`paidAt`), referências ao aluno (`userId`), ao curso (`courseId`) e à matrícula associada (`enrollmentId`). Relação: uma `Enrollment` tem 0..* `Payment` (tentativas recusadas e aprovadas ficam registradas), e cada `Payment` pertence a exatamente uma `Enrollment`. O campo `status` recebe `approved` ou `declined`: em caso de recusa (UC019 E1), o registro é persistido para auditoria e a matrícula em `Enrollment` permanece `pending`, sem liberação do acesso às aulas.
- `LessonProgress` registra os segundos assistidos (`watchedSeconds`) e a conclusão (`completed`) de cada aula pelo aluno matriculado, desacoplado do quiz (atendendo à análise do professor sobre o fluxo de progresso no RA1). Permite retomar a reprodução no ponto exato em que o aluno parou (UC009 A2), persistido independentemente do dispositivo utilizado (UC009 R-3). Possui restrição de unicidade sobre `(enrollmentId, lessonId)`.
- `QuizAttempt` e `QuizAnswer` registram o histórico de submissão do quiz vinculado à matrícula (`enrollmentId`) e as respostas assinaladas para cada questão. A nota calculada imediatamente por comparação com o gabarito é armazenada em `score` (UC002 R-2). `QuizAttempt.status` recebe `draft` (rascunho, UC002 A2, quando o aluno salva respostas parciais) ou `submitted` (enviada); enquanto estiver em `draft`, `score` e `submittedAt` são nulos. Se o instrutor permitir refazer o quiz (UC002 A1, R-3), uma nova tentativa (`QuizAttempt`) é gerada, mantendo o histórico de tentativas anteriores inalterado (UC004 R-2).
- `Review` consolida a nota de 1 a 5 (`rating`) e o comentário opcional (`comment`) do aluno sobre o curso (UC010 R-3). Exige como pré-requisito de negócio a conclusão de ao menos uma aula no curso (UC010 R-1). Possui restrição de unicidade sobre `(userId, courseId)`: cada aluno mantém exatamente uma avaliação por curso, de modo que uma nova avaliação substitui a anterior (UC010 R-2, A1).
- Valores persistidos em inglês, com rótulo em pt-BR para a interface e o texto: `Enrollment.status`: pending = pendente, active = ativa, cancelled = cancelada, completed = concluída; `Payment.status`: approved = aprovado, declined = recusado; `QuizAttempt.status`: draft = rascunho, submitted = enviada.
- Normalização: `Enrollment`, `LessonProgress`, `QuizAttempt`, `QuizAnswer` e `Review` estão na 3FN (Terceira Forma Normal): as chaves primárias são UUIDs únicos, cada atributo não chave depende da chave primária e não há atributos multivalorados. `Payment` tem um desvio deliberado da 3FN: `userId` e `courseId` derivam de `Enrollment` (via `enrollmentId`), logo dependem de forma transitiva da chave primária. As duas colunas ficam no registro de pagamento porque ele é o comprovante da transação e precisa identificar o aluno e o curso que pagaram mesmo que a matrícula mude depois; a consistência entre essas colunas e a matrícula precisa ser garantida pela aplicação ao criar o pagamento.

| ATRIBUTO | CLASSE | DOMÍNIO | TAMANHO | DESCRIÇÃO |
|---|---|---|---|---|
| **Tabela: Enrollment** | | | | |
| id | Determinante | UUID | - | Identificador único da matrícula. |
| userId | Simples | UUID | - | FK para `User.id` (Área A), aluno matriculado. |
| courseId | Simples | UUID | - | FK para `Course.id` (Área B), curso da matrícula. |
| pricePaidCents | Simples | Numérico | - | Valor pago pela matrícula, em centavos (0 para cursos gratuitos). |
| currency | Simples | Texto | 3 | Código da moeda da transação (ISO 4217, ex.: BRL). |
| status | Simples | Texto | - | Status da matrícula: `pending`, `active`, `cancelled` ou `completed` (UC003, UC019). |
| createdAt | Simples | Data e hora | - | Data e hora de criação da matrícula. |
| updatedAt | Simples | Data e hora | - | Data e hora da última alteração de status (opcional). |
| **Tabela: Payment** | | | | |
| id | Determinante | UUID | - | Identificador único do pagamento simulado. |
| userId | Simples | UUID | - | FK para `User.id` (Área A), aluno pagador. |
| courseId | Simples | UUID | - | FK para `Course.id` (Área B), curso adquirido. |
| enrollmentId | Simples | UUID | - | FK para `Enrollment.id`, matrícula associada ao pagamento (0..* pagamentos por matrícula). |
| amountCents | Simples | Numérico | - | Valor cobrado no pagamento simulado, em centavos. |
| currency | Simples | Texto | 3 | Código da moeda (ISO 4217, ex.: BRL). |
| status | Simples | Texto | - | Status do pagamento: `approved` ou `declined` (UC019). |
| paidAt | Simples | Data e hora | - | Data e hora do processamento da tentativa de pagamento. |
| **Tabela: LessonProgress** | | | | |
| id | Determinante | UUID | - | Identificador único do progresso da aula. |
| enrollmentId | Simples | UUID | - | FK para `Enrollment.id`, matrícula do aluno. |
| lessonId | Simples | UUID | - | FK para `Lesson.id` (Área B), aula assistida. |
| completed | Simples | Booleano | - | Indica se a aula foi concluída pelo aluno (true/false). |
| watchedSeconds | Simples | Numérico | - | Posição em segundos assistidos para retomada da aula (UC009 R-2). |
| completedAt | Simples | Data e hora | - | Data e hora em que a aula foi concluída (nulo se não concluída). |
| updatedAt | Simples | Data e hora | - | Data e hora da última sincronização do progresso. |
| **Tabela: QuizAttempt** | | | | |
| id | Determinante | UUID | - | Identificador único da tentativa de resolução do quiz. |
| enrollmentId | Simples | UUID | - | FK para `Enrollment.id`, matrícula do aluno. |
| quizId | Simples | UUID | - | FK para `Quiz.id` (Área B), quiz respondido. |
| status | Simples | Texto | - | Status da tentativa: `draft` (rascunho) ou `submitted` (enviada) (UC002 A2). |
| score | Simples | Numérico | - | Nota calculada da tentativa (escala decimal de 0,00 a 100,00), nula enquanto `draft` (UC002 R-2). |
| submittedAt | Simples | Data e hora | - | Data e hora de submissão e correção das respostas; nula enquanto `draft`. |
| **Tabela: QuizAnswer** | | | | |
| id | Determinante | UUID | - | Identificador único da resposta individual do quiz. |
| attemptId | Simples | UUID | - | FK para `QuizAttempt.id`, tentativa à qual a resposta pertence. |
| questionId | Simples | UUID | - | FK para `Question.id` (Área B), pergunta respondida. |
| optionId | Simples | UUID | - | FK para `QuestionOption.id` (Área B), alternativa assinalada pelo aluno. |
| **Tabela: Review** | | | | |
| id | Determinante | UUID | - | Identificador único da avaliação do curso. |
| userId | Simples | UUID | - | FK para `User.id` (Área A), aluno autor da avaliação. |
| courseId | Simples | UUID | - | FK para `Course.id` (Área B), curso avaliado. |
| rating | Simples | Inteiro | - | Nota atribuída ao curso pelo aluno, de 1 a 5 (UC010 R-3). |
| comment | Simples | Texto | - | Comentário textual opinativo sobre o curso (opcional) (UC010 R-3). |
| createdAt | Simples | Data e hora | - | Data e hora de publicação ou substituição da avaliação. |

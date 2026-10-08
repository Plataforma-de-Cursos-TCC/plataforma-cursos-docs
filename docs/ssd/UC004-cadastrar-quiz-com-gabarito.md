# UC004 — Cadastrar Quiz com Gabarito

Diagrama de sequência do sistema para o caso de uso UC004 (Cadastrar Quiz com Gabarito). Representa a criação de um quiz pelo Instrutor, o cadastro iterativo de perguntas com gabarito e sua publicação.

<!-- revisar: diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original. -->
```mermaid
sequenceDiagram
    actor Instrutor
    participant QuizView as Front-end web
    participant QuizController as API
    participant DB as Banco de Dados

    Instrutor->>QuizView: acessa o módulo do curso
    Instrutor->>QuizView: cria um novo quiz
    QuizView->>QuizController: criarQuiz(moduloId, titulo)
    QuizController->>DB: sp_Criar_Quiz
    DB-->>QuizController: quiz criado
    loop para cada pergunta
        Instrutor->>QuizView: cadastra pergunta com alternativas
        Instrutor->>QuizView: marca a alternativa correta
        QuizView->>QuizController: adicionarPergunta(quizId, pergunta, alternativas)
        alt alguma alternativa marcada como correta
            QuizController->>DB: sp_Salvar_Pergunta
            DB-->>QuizController: pergunta salva
            QuizController-->>QuizView: pergunta adicionada
        else nenhuma alternativa marcada como correta
            QuizController-->>QuizView: erro - gabarito ausente
            QuizView-->>Instrutor: bloqueia salvamento, pede pra marcar o gabarito
        end
    end
    Instrutor->>QuizView: salva o quiz
    QuizView->>QuizController: publicarQuiz(quizId)
    QuizController-->>QuizView: quiz disponível pros alunos do módulo
```

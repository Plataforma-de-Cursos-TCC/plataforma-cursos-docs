# UC002 — Responder Quiz

Diagrama de sequência do sistema para o caso de uso UC002 (Responder Quiz). Representa a obtenção das questões do quiz pelo Aluno, o envio das respostas, a validação de preenchimento, o cálculo da nota e a persistência da tentativa.

<!-- revisar: diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original. -->
```mermaid
sequenceDiagram
    actor Aluno
    participant QuizView as Front-end web
    participant QuizController as API
    participant DB as Banco de Dados

    Aluno->>QuizView: acessa o quiz do módulo
    QuizView->>QuizController: obterQuiz(moduloId)
    QuizController->>DB: sp_Buscar_Quiz
    DB-->>QuizController: perguntas e alternativas
    QuizController-->>QuizView: renderiza formulário do quiz
    QuizView-->>Aluno: exibe perguntas
    Aluno->>QuizView: responde as perguntas
    Aluno->>QuizView: clica em enviar
    QuizView->>QuizController: enviarRespostas(respostas)
    alt todas as questões respondidas
        QuizController->>DB: sp_Calcular_Nota(respostas, gabarito)
        DB-->>QuizController: nota calculada
        QuizController->>DB: sp_Salvar_Tentativa
        DB-->>QuizController: resultado (nota)
        QuizController-->>QuizView: exibe nota e resultado
        QuizView-->>Aluno: resultado salvo e exibido
    else questão pendente
        QuizController-->>QuizView: erro - questão pendente
        QuizView-->>Aluno: bloqueia envio, indica questão faltante
    end
```

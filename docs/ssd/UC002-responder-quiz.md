# UC002 — Responder Quiz

Diagrama de sequência do sistema para o caso de uso UC002 (Responder Quiz). Representa a obtenção das questões do quiz pelo Aluno, o envio das respostas, a validação de preenchimento, o cálculo da nota e a persistência da tentativa.

```mermaid
sequenceDiagram
    actor Aluno
    participant QuizView
    participant QuizController
    participant Banco de Dados

    Aluno->>QuizView: acessa o quiz do módulo
    QuizView->>+QuizController: obterQuiz(moduloId)
    QuizController->>+Banco de Dados: sp_Buscar_Quiz
    Banco de Dados-->>-QuizController: perguntas e alternativas
    QuizController-->>QuizView: renderiza formulário do quiz
    QuizView-->>Aluno: exibe perguntas
    Aluno->>QuizView: responde as perguntas
    Aluno->>QuizView: clica em enviar
    QuizView->>QuizController: enviarRespostas(respostas[])
    alt todas as questões respondidas
        QuizController->>+Banco de Dados: sp_Calcular_Nota(respostas, gabarito)
        Banco de Dados-->>-QuizController: nota calculada
        QuizController->>Banco de Dados: sp_Salvar_Tentativa
        QuizController-->>QuizView: resultado (nota)
        QuizView-->>Aluno: exibe nota e resultado
    else questão pendente
        QuizController-->>QuizView: erro — questão pendente
        QuizView-->>Aluno: bloqueia envio, indica questão faltante
    end
    deactivate QuizController
```

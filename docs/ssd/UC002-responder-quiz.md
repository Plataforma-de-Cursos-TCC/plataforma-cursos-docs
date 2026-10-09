# UC002 — Responder Quiz

Diagrama de sequência do sistema para o caso de uso UC002 (Responder Quiz). Representa a verificação de acesso ao quiz pelo Aluno (aulas do módulo concluídas), a retomada de tentativa já enviada, o salvamento de rascunho, o envio das respostas, a validação de preenchimento, o cálculo da nota e a persistência da tentativa.

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Acessa o quiz do módulo
    FE->>API: GET /api/v1/quizzes/{id}/attempt/result
    API->>DB: Verifica aulas do módulo concluídas e tentativa anterior
    DB-->>API: Situação das aulas e tentativa (ou vazio)
    alt aulas do módulo não concluídas
        API-->>FE: Quiz indisponível
        FE-->>Aluno: Exibe aviso para concluir as aulas do módulo
    else tentativa já enviada (A1)
        API-->>FE: 200 OK + resultado salvo
        FE-->>Aluno: Exibe resultado salvo
    else primeiro acesso
        API-->>FE: 200 OK + perguntas e alternativas
        FE-->>Aluno: Exibe formulário do quiz
        opt salvar rascunho (A2)
            Aluno->>FE: Aciona "Salvar rascunho"
            FE->>API: PUT /api/v1/quizzes/{id}/attempt/draft (respostas parciais)
            API->>DB: Salva respostas parciais
            API-->>FE: 200 OK
        end
        Aluno->>FE: Responde e aciona "Enviar respostas"
        alt questões pendentes (E1)
            FE-->>Aluno: Bloqueia envio e indica questões pendentes
        else todas as questões respondidas
            FE->>API: POST /api/v1/quizzes/{id}/attempt (respostas)
            API->>DB: Compara respostas com o gabarito
            DB-->>API: Gabarito completo ou incompleto
            alt gabarito incompleto (E2)
                API->>DB: Registra falha para o Instrutor responsável
                API-->>FE: Erro, nota não calculada
                FE-->>Aluno: Informa erro ao Aluno
            else gabarito completo
                API->>DB: Salva tentativa e nota
                DB-->>API: OK
                API-->>FE: 201 Created (nota)
                FE-->>Aluno: Exibe nota e resultado
            end
        end
    end
```

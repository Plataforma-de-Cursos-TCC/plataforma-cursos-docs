# UC004 — Cadastrar Quiz com Gabarito

Diagrama de sequência do sistema para o caso de uso UC004 (Cadastrar Quiz com Gabarito). Representa a criação do quiz pelo Instrutor dono do curso, o cadastro das perguntas com alternativas e gabarito, a edição de pergunta existente (A1), o salvamento como rascunho (A2), a validação do gabarito (E1 e E2) e a publicação.

```mermaid
sequenceDiagram
    actor Instrutor
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Instrutor->>FE: Acessa o módulo do curso e cria um quiz
    Instrutor->>FE: Cadastra perguntas, alternativas e marca a correta
    Instrutor->>FE: Aciona "Salvar quiz"
    alt salvar como rascunho (A2)
        FE->>API: POST /api/v1/instructor/modules/{id}/quiz (status rascunho)
    else publicar
        FE->>API: POST /api/v1/instructor/modules/{id}/quiz (status publicado)
    end
    API->>DB: Verifica se o módulo pertence a curso do Instrutor
    DB-->>API: Proprietário do curso
    alt Instrutor não é dono do curso (R-1)
        API-->>FE: 403 Forbidden (FORBIDDEN)
        FE-->>Instrutor: Exibe aviso de acesso negado
    else Instrutor é dono do curso
        alt pergunta com menos de 2 alternativas (E1)
            API-->>FE: 422 Unprocessable Entity (VALIDATION_FAILED)
            FE-->>Instrutor: Indica a pergunta e pede ao menos 2 alternativas
        else pergunta sem alternativa correta (E2)
            API-->>FE: 422 Unprocessable Entity (VALIDATION_FAILED)
            FE-->>Instrutor: Bloqueia o salvamento e pede para marcar o gabarito
        else quiz válido
            API->>DB: Salva quiz, perguntas, alternativas e gabarito
            DB-->>API: OK
            API-->>FE: 201 Created (quiz)
            alt status publicado
                FE-->>Instrutor: Informa quiz disponível aos Alunos do módulo
            else status rascunho (A2)
                FE-->>Instrutor: Informa rascunho salvo, sem visibilidade para os Alunos
            end
        end
    end
    opt editar pergunta de quiz existente (A1)
        Instrutor->>FE: Altera pergunta, alternativas ou gabarito
        FE->>API: PUT /api/v1/instructor/quizzes/{id} (perguntas, gabarito e status)
        API->>DB: Verifica proprietário e atualiza o quiz preservando tentativas e notas já registradas (R-2)
        DB-->>API: OK
        API-->>FE: 200 OK (quiz)
        FE-->>Instrutor: Exibe quiz atualizado
    end
```

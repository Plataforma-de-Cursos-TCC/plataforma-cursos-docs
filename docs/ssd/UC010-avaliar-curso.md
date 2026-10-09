# UC010 — Avaliar Curso

Diagrama de sequência do sistema para o caso de uso UC010 (Avaliar Curso). Representa a avaliação com nota de 1 a 5 e comentário opcional realizada pelo Aluno matriculado, com verificação de aula concluída, pré-preenchimento da avaliação anterior, validação de nota obrigatória e recálculo da nota média.

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Acessa página do curso
    Aluno->>FE: Aciona "Avaliar curso"
    FE->>API: GET /api/v1/courses/{id}/reviews/me
    API->>DB: Verifica aula concluída e busca avaliação existente do Aluno
    DB-->>API: Situação do Aluno e avaliação (ou vazio)
    alt nenhuma aula do curso concluída (E1)
        API-->>FE: Erro, é preciso concluir ao menos uma aula
        FE-->>Aluno: Bloqueia avaliação e informa que é preciso concluir uma aula
    else elegível
        API-->>FE: 200 OK + avaliação anterior (A1, se houver)
        FE-->>Aluno: Exibe formulário, preenchido se houver avaliação anterior
        Aluno->>FE: Informa nota (1 a 5) e comentário opcional
        alt Aluno fecha sem confirmar (A2)
            FE-->>Aluno: Descarta alterações e mantém avaliação anterior
        else Aluno confirma envio
            Aluno->>FE: Confirma envio
            alt nota não selecionada (E2)
                FE-->>Aluno: Bloqueia envio, indica que a nota é obrigatória
            else nota selecionada
                FE->>API: POST /api/v1/courses/{id}/reviews (nota, comentário)
                alt aluno matriculado no curso
                    API->>DB: Salva ou substitui avaliação
                    DB-->>API: OK
                    API->>DB: Recalcula nota média do curso
                    DB-->>API: OK
                    API-->>FE: 200 OK
                    FE-->>Aluno: Avaliação salva e exibida na página do curso
                else aluno não matriculado
                    API-->>FE: 403 Forbidden
                    FE-->>Aluno: Só alunos matriculados podem avaliar
                end
            end
        end
    end
```

# UC003 — Matricular-se em Curso

Diagrama de sequência do sistema para o caso de uso UC003 (Matricular-se em Curso). Representa a consulta do curso pelo Aluno, a verificação de matrícula prévia, a criação da matrícula pendente, o pagamento simulado do UC019 (aprovado ou recusado) e a ativação da matrícula apenas com pagamento aprovado. Curso gratuito ativa a matrícula diretamente.

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Acessa página de um curso
    FE->>API: GET /api/v1/catalog/courses/{id}
    API->>DB: Busca curso e matrícula do Aluno
    DB-->>API: Dados do curso e matrícula (ou vazio)
    alt aluno já matriculado (A1)
        API-->>FE: 200 OK + matrícula existente
        FE-->>Aluno: Exibe botão "Continuar assistindo"
    else curso publicado e aluno não matriculado
        API-->>FE: 200 OK + dados do curso
        FE-->>Aluno: Exibe botão "Matricular-se"
        Aluno->>FE: Aciona "Matricular-se"
        FE->>API: POST /api/v1/courses/{id}/enroll
        API->>DB: Verifica se o curso continua publicado
        DB-->>API: Status do curso
        alt curso despublicado (E1)
            API-->>FE: Erro, curso não está mais disponível
            FE-->>Aluno: Exibe aviso, sem matrícula registrada
        else curso disponível
            API->>DB: Cria matrícula (ou reaproveita a pendente de tentativa anterior recusada)
            alt curso gratuito (A2)
                API->>DB: Matrícula com status ativa
                DB-->>API: OK
                API-->>FE: 201 Created (ativa)
                FE-->>Aluno: Curso aparece em "Meus cursos"
            else curso pago (A3)
                API->>DB: Matrícula com status pendente (única por Aluno e curso)
                DB-->>API: OK
                API-->>FE: 201 Created (pendente)
                FE-->>Aluno: Exibe resumo do pagamento (UC019)
                alt Aluno cancela no resumo (UC019 A1)
                    FE-->>Aluno: Fecha resumo, matrícula continua pendente
                else Aluno confirma pagamento
                    FE->>API: POST /api/v1/enrollments/{id}/pay
                    API->>DB: Processa pagamento simulado
                    alt pagamento aprovado
                        API->>DB: Registra pagamento aprovado e ativa matrícula
                        DB-->>API: OK
                        API-->>FE: 200 OK (matrícula ativa)
                        FE-->>Aluno: Curso aparece em "Meus cursos"
                    else pagamento recusado (E2)
                        API->>DB: Registra pagamento com status recusado
                        DB-->>API: OK
                        API-->>FE: 422 PAYMENT_DECLINED
                        FE-->>Aluno: Exibe aviso "Pagamento recusado" e volta à página do curso (passo 2), com o botão "Matricular-se"
                    end
                end
            end
        end
    end
```

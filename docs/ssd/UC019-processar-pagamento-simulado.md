# UC019 — Processar Pagamento Simulado

Diagrama de sequência do sistema para o caso de uso UC019 (Processar Pagamento Simulado). Representa a matrícula pendente criada no UC003, a confirmação do pagamento simulado pelo Aluno, sem gateway externo, e o registro de pagamento aprovado (matrícula ativa) ou recusado (matrícula pendente).

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Aciona "Matricular-se" (UC003)
    FE->>API: POST /api/v1/courses/{id}/enroll
    API->>DB: Cria matrícula pendente
    DB-->>API: OK
    API-->>FE: 201 Created
    FE-->>Aluno: Exibe resumo com título do curso e valor
    alt aluno cancela
        Aluno->>FE: Aciona "Cancelar"
        FE-->>Aluno: Fecha resumo sem registrar pagamento
    else aluno confirma
        Aluno->>FE: Aciona "Confirmar pagamento"
        FE->>API: POST /api/v1/enrollments/{id}/pay
        API->>DB: Processa pagamento simulado
        alt pagamento aprovado
            DB-->>API: OK
            API->>DB: Registra pagamento aprovado
            API->>DB: Ativa matrícula
            DB-->>API: OK
            API-->>FE: 200 OK
            FE-->>Aluno: Pagamento confirmado e curso liberado
        else pagamento simulado recusado
            API->>DB: Registra Payment.status = recusado
            DB-->>API: Recusa registrada
            API-->>FE: 422 PAYMENT_DECLINED
            FE-->>Aluno: Aviso "Pagamento recusado." e botão Matricular-se
        end
    end
```

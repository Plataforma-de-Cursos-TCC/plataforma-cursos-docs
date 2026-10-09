# UC019 — Processar Pagamento Simulado

Diagrama de sequência do sistema para o caso de uso UC019 (Processar Pagamento Simulado). Representa a confirmação do pagamento simulado pelo Aluno, estendendo o fluxo de matrícula do UC003, sem gateway externo, com tratamento de recusa e nova tentativa.

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Aciona pagamento da matrícula (extensão do UC003)
    FE-->>Aluno: Exibe resumo com título do curso e valor
    alt aluno cancela
        Aluno->>FE: Aciona "Cancelar"
        FE-->>Aluno: Retorna sem cobrança
    else aluno confirma
        Aluno->>FE: Aciona "Confirmar pagamento"
        FE->>API: POST /api/v1/enrollments/{id}/pay
        API->>DB: Processa pagamento simulado
        alt pagamento aprovado
            DB-->>API: OK
            API->>DB: Libera acesso ao curso
            DB-->>API: OK
            API-->>FE: 200 OK
            FE-->>Aluno: Pagamento confirmado e acesso liberado
        else pagamento simulado recusado
            DB-->>API: Recusa registrada
            API-->>FE: 422 VALIDATION_FAILED
            FE-->>Aluno: Exibe aviso de recusa e permite nova tentativa
        end
    end
```

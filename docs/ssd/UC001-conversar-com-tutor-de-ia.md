# UC001 — Conversar com Tutor de IA

Diagrama de sequência do sistema para o caso de uso UC001 (Conversar com Tutor de IA). Representa a conversa do Aluno matriculado com o Tutor de IA (ator sistêmico, ADR-0005) na página da aula: reabertura do histórico (A2), busca por similaridade nos embeddings do material do curso, resposta em streaming SSE com citação de aula e timestamp, pergunta fora do escopo (A1), aula ainda não indexada (E1) e limite de mensagens (E2).

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant AI as ai-service (Tutor de IA)
    participant DB as Banco de Dados

    Aluno->>FE: Abre o chat na página da aula
    opt reabrir conversa anterior (A2)
        FE->>API: GET /api/v1/ai/tutor/conversations/{id}/messages (cursor)
        API->>DB: Busca mensagens da conversa do Aluno
        DB-->>API: Mensagens
        API-->>FE: 200 OK + mensagens e próximo cursor
        FE-->>Aluno: Exibe o histórico no chat
    end
    Aluno->>FE: Digita a pergunta e aciona "Enviar"
    FE->>API: POST /api/v1/ai/tutor/chat (aula_id, pergunta)
    API->>DB: Verifica matrícula no curso, indexação da aula e contagem de mensagens do período
    DB-->>API: Matrícula, situação da aula e contagem
    alt Aluno não matriculado
        API-->>FE: 403 Forbidden (FORBIDDEN)
        FE-->>Aluno: Exibe aviso de acesso negado
    else limite de mensagens atingido (E2)
        API-->>FE: 429 Too Many Requests (TOO_MANY_REQUESTS) + tempo de espera
        FE-->>Aluno: Bloqueia o envio e informa o tempo de espera restante
    else aula sem transcrição e embeddings (E1)
        API-->>FE: 409 Conflict (LESSON_NOT_INDEXED)
        FE-->>Aluno: Informa que o conteúdo está em preparo e sugere tentar mais tarde
    else pergunta permitida
        API->>AI: Pergunta, aula e curso
        AI->>DB: Busca por similaridade nos trechos do curso
        DB-->>AI: Trechos relevantes (aula e timestamp) ou vazio
        alt trechos relevantes encontrados
            AI-->>API: Resposta em streaming com trechos de origem
            API->>DB: Salva pergunta e resposta na conversa
            API-->>FE: 200 OK (SSE) com resposta, aula e timestamp citados
            FE-->>Aluno: Exibe a resposta no chat com a citação
        else sem informação no material (A1)
            AI-->>API: Sem trechos relevantes
            API-->>FE: 200 OK (SSE) com aviso de que não há essa informação
            FE-->>Aluno: Informa que não tem a informação e sugere reformular
        end
    end
```

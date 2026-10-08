# UC001 — Conversar com Tutor de IA

Diagrama de sequência do sistema para o caso de uso UC001 (Conversar com Tutor de IA). Representa a interação entre o Aluno, a interface de chat, a API de controle e o serviço do Tutor de IA com busca por similaridade em embeddings do material do curso.

```mermaid
sequenceDiagram
    actor Aluno
    participant ChatView
    participant TutorController
    participant ai as ai-service (BD + embeddings)

    Aluno->>ChatView: abre chat na página da aula
    Aluno->>ChatView: digita a pergunta
    ChatView->>+TutorController: perguntar(aulaId, pergunta)
    TutorController->>+ai: similarity_search(pergunta, courseId)
    alt trecho relevante encontrado no material do curso
        ai-->>-TutorController: trechos relevantes (aula + timestamp)
        TutorController-->>ChatView: resposta com citação de aula e timestamp
        ChatView-->>Aluno: exibe resposta no chat
    else pergunta fora do escopo do curso
        ai-->>TutorController: sem informação no material do curso
        TutorController-->>ChatView: exibe aviso "não tenho essa informação"
    end
    deactivate TutorController

    Note over ChatView,ai: exceção — aula ainda sem embeddings
    TutorController-->>ChatView: conteúdo ainda sendo preparado
    ChatView-->>Aluno: exibe aviso de processamento

    Note over Aluno,TutorController: exceção — rate limit por período
    TutorController-->>ChatView: limite de mensagens atingido
    ChatView-->>Aluno: bloqueia novo envio e informa tempo de espera
```

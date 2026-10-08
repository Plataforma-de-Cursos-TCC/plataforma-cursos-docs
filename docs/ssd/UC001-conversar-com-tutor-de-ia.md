# UC001 — Conversar com Tutor de IA

Diagrama de sequência do sistema para o caso de uso UC001 (Conversar com Tutor de IA). Representa a interação entre o Aluno, a interface de chat, a API de controle e o serviço do Tutor de IA com busca por similaridade em embeddings do material do curso.

<!-- revisar: diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original. -->
```mermaid
sequenceDiagram
    actor Aluno
    participant ChatView as Front-end web
    participant TutorController as API
    participant ai as Tutor de IA

    Aluno->>ChatView: abre chat na página da aula
    Aluno->>ChatView: digita a pergunta
    ChatView->>TutorController: perguntar(aulaId, pergunta)
    TutorController->>ai: similarity_search(pergunta, courseId)
    alt trecho relevante encontrado no material do curso
        ai-->>TutorController: trechos relevantes (aula + timestamp)
        TutorController-->>ChatView: resposta com citação de aula e timestamp
        ChatView-->>Aluno: exibe resposta no chat
    else pergunta fora do escopo do curso
        ai-->>TutorController: sem informação no material do curso
        TutorController-->>ChatView: exibe aviso "não tenho essa informação"
    else exceção - aula ainda sem embeddings
        ai-->>TutorController: conteúdo ainda sendo preparado
        TutorController-->>ChatView: exibe aviso de processamento
    else exceção - rate limit por período
        TutorController->>TutorController: limite de mensagens atingido
        TutorController-->>ChatView: bloqueia novo envio e informa tempo de espera
    end
```

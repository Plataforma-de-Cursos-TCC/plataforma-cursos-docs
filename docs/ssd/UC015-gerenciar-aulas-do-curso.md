# UC015 — Gerenciar Aulas do Curso

Diagrama de sequência do sistema para o caso de uso UC015 (Gerenciar Aulas do Curso). Representa a criação de aula por um Instrutor dono do curso, a obtenção de URL assinada para envio do vídeo no Cloudflare R2 com validade de 15 minutos, a validação de formato e tamanho do vídeo, a edição de dados e a exclusão de aula.

```mermaid
sequenceDiagram
    actor Instrutor
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados
    participant R2 as Cloudflare R2

    Instrutor->>FE: Acessa o módulo
    Instrutor->>FE: Aciona "Nova aula"
    Instrutor->>FE: Informa título, descrição, ordem e se é prévia, e seleciona o vídeo
    FE->>API: POST /api/v1/instructor/modules/{id}/lessons (dados da aula, formato e tamanho do vídeo)
    alt vídeo mp4 ou webm até 500 MB
        API->>DB: Verifica que o Instrutor é dono do curso e cria a aula
        DB-->>API: Aula criada
        API-->>FE: URL assinada de envio, válida por 15 min
        FE->>R2: Envia o vídeo pela URL assinada
        R2-->>FE: Recebimento confirmado
        FE-->>Instrutor: Confirma o recebimento do vídeo
        Note over API,DB: transcrição e indexação iniciadas uma única vez por aula (fluxo assíncrono a verificar no TDD)
    else formato ou tamanho inválido (E1)
        API-->>FE: 422 VALIDATION_FAILED (formato ou tamanho)
        FE-->>Instrutor: Recusa o arquivo e informa os limites aceitos
    end
    opt Falha no envio ou link expirado (E2)
        FE->>R2: Envio do vídeo falha
        Note over FE,API: pedido de novo link de envio não consta no TDD (a definir)
        FE-->>Instrutor: Informa o erro e oferece nova tentativa
    end
    opt Edita aula ou substitui vídeo (A1)
        Instrutor->>FE: Seleciona uma aula e altera os dados ou escolhe novo vídeo
        FE->>API: PUT /api/v1/instructor/lessons/{id} (dados da aula, isPreview)
        API->>DB: Atualiza a aula
        DB-->>API: Aula atualizada
        API-->>FE: 200 OK
        FE-->>Instrutor: Atualiza a lista de aulas
    end
    opt Exclui aula (A2)
        Instrutor->>FE: Aciona "Excluir" e confirma
        Note over FE,API: endpoint de exclusão de aula não consta no TDD (a definir)
        API->>DB: Remove a aula e o seu vídeo
        DB-->>API: Exclusão concluída
        API-->>FE: Aula removida
        FE-->>Instrutor: Atualiza a lista de aulas
    end
```

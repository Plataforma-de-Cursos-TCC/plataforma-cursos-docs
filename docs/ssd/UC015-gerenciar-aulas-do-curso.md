# UC015 — Gerenciar Aulas do Curso

Diagrama de sequência do sistema para o caso de uso UC015 (Gerenciar Aulas do Curso). Representa a criação de aula por um Instrutor dono do curso, a obtenção de URL assinada para envio do vídeo no Cloudflare R2 com validade de 15 minutos, a validação de formato e tamanho do vídeo, a geração de novo link após falha no envio (E2), a edição de dados e a exclusão de aula. Todas as operações verificam o dono do curso (R-1).

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
    alt Instrutor não é dono do curso (R-1)
        API-->>FE: 403 FORBIDDEN
        FE-->>Instrutor: Informa que a aula não pode ser criada
    else formato ou tamanho inválido (E1)
        API-->>FE: 422 VALIDATION_FAILED (formato ou tamanho)
        FE-->>Instrutor: Recusa o arquivo e informa os limites aceitos
    else vídeo mp4 ou webm até 500 MB
        API->>DB: Cria a aula
        DB-->>API: Aula criada
        API-->>FE: 201 Created (URL assinada de envio, válida por 15 min)
        FE->>R2: Envia o vídeo pela URL assinada
        R2-->>FE: Recebimento confirmado
        FE-->>Instrutor: Confirma o recebimento do vídeo
        Note over API,DB: transcrição e indexação iniciadas uma única vez por aula (RNF004)
    end
    opt Falha no envio ou link expirado (E2)
        FE->>R2: Envio do vídeo falha
        FE-->>Instrutor: Informa o erro e oferece nova tentativa
        Instrutor->>FE: Aciona "Tentar novamente"
        FE->>API: POST /api/v1/instructor/lessons/{id}/upload-url
        API->>DB: Verifica que o Instrutor é dono do curso
        API-->>FE: 200 OK (novo link de envio, válido por 15 min)
        FE->>R2: Reenvia o vídeo pela nova URL assinada
        R2-->>FE: Recebimento confirmado
    end
    opt Edita aula ou substitui vídeo (A1)
        Instrutor->>FE: Seleciona uma aula e altera os dados ou escolhe novo vídeo
        FE->>API: PUT /api/v1/instructor/lessons/{id} (dados da aula, isPreview)
        alt Instrutor é dono do curso
            API->>DB: Atualiza a aula
            DB-->>API: Aula atualizada
            API-->>FE: 200 OK
            FE-->>Instrutor: Atualiza a lista de aulas
        else Instrutor não é dono do curso (R-1)
            API-->>FE: 403 FORBIDDEN
            FE-->>Instrutor: Informa que a aula não pode ser alterada
        end
        opt Novo vídeo escolhido
            FE->>API: POST /api/v1/instructor/lessons/{id}/upload-url
            API-->>FE: 200 OK (URL assinada de envio)
            FE->>R2: Envia o novo vídeo pela URL assinada
            R2-->>FE: Recebimento confirmado
        end
    end
    opt Exclui aula (A2)
        Instrutor->>FE: Aciona "Excluir" e confirma
        FE->>API: DELETE /api/v1/instructor/lessons/{id}
        alt Instrutor é dono do curso
            API->>DB: Remove a aula
            API->>R2: Remove o vídeo da aula
            DB-->>API: Exclusão concluída
            API-->>FE: 204 No Content
            FE-->>Instrutor: Atualiza a lista de aulas
        else Instrutor não é dono do curso (R-1)
            API-->>FE: 403 FORBIDDEN
            FE-->>Instrutor: Informa que a aula não pode ser excluída
        end
    end
```

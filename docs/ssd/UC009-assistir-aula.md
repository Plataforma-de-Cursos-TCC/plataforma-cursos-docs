# UC009 — Assistir Aula

Diagrama de sequência do sistema para o caso de uso UC009 (Assistir Aula). Representa a verificação de acesso à aula (matrícula ou aula prévia), o carregamento dos dados e a reprodução do vídeo pelo Aluno, e o registro do progresso por conclusão ou segundos assistidos.

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Acessa a aula dentro do curso
    FE->>API: GET /api/v1/lessons/{id}/stream
    API->>DB: Verifica matrícula do Aluno ou se a aula é prévia
    DB-->>API: Situação de acesso
    alt sem matrícula e aula não é prévia (E1)
        API-->>FE: Acesso negado
        FE-->>Aluno: Aula bloqueada, sugere matrícula no curso (UC003)
    else acesso permitido
        API->>DB: Busca dados da aula (vídeo, URL assinada) e progresso
        alt falha ao carregar o vídeo (E2)
            DB-->>API: Erro na entrega do vídeo
            API-->>FE: Erro na entrega do vídeo
            FE-->>Aluno: Exibe erro e opção de tentar carregar novamente
        else vídeo disponível
            DB-->>API: Dados da aula
            API-->>FE: 200 OK + URL assinada
            FE-->>Aluno: Reproduz vídeo (A2 a partir do ponto salvo)
            alt vídeo assistido até o fim
                FE->>API: POST /api/v1/lessons/{id}/progress (concluído)
                API->>DB: Marca aula concluída e atualiza progresso
                DB-->>API: OK
                API-->>FE: 200 OK
                FE-->>Aluno: Aula marcada como concluída
            else aluno sai antes do fim (A1)
                FE->>API: POST /api/v1/lessons/{id}/progress (segundos assistidos)
                API->>DB: Salva segundos assistidos
                DB-->>API: OK
                API-->>FE: 200 OK
            end
        end
    end
    Note over Aluno,FE: A3 aluno aciona o Tutor de IA (UC001) e retorna ao vídeo
```

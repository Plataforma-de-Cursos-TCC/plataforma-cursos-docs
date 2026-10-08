# UC009 — Assistir Aula

Diagrama de sequência do sistema para o caso de uso UC009 (Assistir Aula). Representa o carregamento dos dados e reprodução do vídeo pelo Aluno, acompanhando o progresso por conclusão ou segundos assistidos.

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Acessa a aula
    FE->>API: GET /aulas/{id}
    API->>DB: Busca dados da aula (vídeo, URL assinada)
    DB-->>API: Dados da aula
    API-->>FE: 200 OK
    FE-->>Aluno: Reproduz vídeo
    alt vídeo assistido até o fim
        FE->>API: POST /progresso (concluído)
        API->>DB: Marca aula concluída, atualiza progresso
        DB-->>API: OK
        API-->>FE: 200 OK
        FE-->>Aluno: Aula marcada como concluída
    else aluno sai antes do fim
        FE->>API: POST /progresso (segundos assistidos)
        API->>DB: Salva segundos assistidos
        DB-->>API: OK
        API-->>FE: 200 OK
    end
```

# UC007 — Ver Dashboard com Filtro

Diagrama de sequência do sistema para o caso de uso UC007 (Ver Dashboard com Filtro). Representa a consulta de métricas e gráficos filtrados por período e curso por parte do Instrutor ou Administrador.

```mermaid
sequenceDiagram
    actor User as Instrutor / Administrador
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    User->>FE: Acessa dashboard
    User->>FE: Seleciona intervalo de datas
    User->>FE: (Opcional) filtra por curso
    FE->>API: GET /dashboard?inicio&fim&curso_id
    alt intervalo válido
        API->>DB: Agrega progresso e engajamento do período
        DB-->>API: Dados agregados
        alt existem dados no período
            API-->>FE: 200 OK + métricas
            FE-->>User: Exibe gráficos atualizados
        else sem atividade no período
            API-->>FE: 200 OK (vazio)
            FE-->>User: Exibe estado vazio claro
        end
    else intervalo inválido
        API-->>FE: 400 Bad Request
        FE-->>User: Exibe erro e mantém último intervalo válido
    end
```

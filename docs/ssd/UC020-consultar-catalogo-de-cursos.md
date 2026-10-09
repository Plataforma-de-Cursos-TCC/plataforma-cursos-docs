# UC020 — Consultar Catálogo de Cursos

Diagrama de sequência do sistema para o caso de uso UC020 (Consultar Catálogo de Cursos). Representa a listagem paginada de cursos publicados, o filtro por categoria e a abertura da página pública de um curso, acessíveis a Visitante e Aluno.

```mermaid
sequenceDiagram
    actor User as Visitante / Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    User->>FE: Acessa catálogo
    FE->>API: GET /api/v1/catalog/courses
    API->>DB: Busca cursos publicados
    DB-->>API: Lista de cursos
    alt existem cursos publicados
        API-->>FE: 200 OK (lista paginada)
        FE-->>User: Exibe cursos
        opt usuário filtra por categoria
            User->>FE: Seleciona categoria
            FE->>API: GET /api/v1/catalog/courses?categoria=
            alt categoria com cursos
                API-->>FE: 200 OK (lista paginada)
                FE-->>User: Exibe cursos da categoria
            else categoria sem cursos
                API-->>FE: 200 OK (lista vazia)
                FE-->>User: "Nenhum curso encontrado nesta categoria." e "Ver todos os cursos"
            end
        end
        User->>FE: Abre página de um curso
        FE->>API: GET /api/v1/catalog/courses/{id}
        API->>DB: Busca dados públicos do curso
        DB-->>API: Curso com módulos e aulas prévias
        API-->>FE: 200 OK
        FE-->>User: Exibe página do curso
    else nenhum curso publicado
        API-->>FE: 200 OK (lista vazia)
        FE-->>User: "Nenhum curso disponível no momento."
    end
```

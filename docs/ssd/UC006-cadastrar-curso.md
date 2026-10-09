# UC006 — Cadastrar Curso

Diagrama de sequência do sistema para o caso de uso UC006 (Cadastrar Curso). Representa a criação de curso em estado de rascunho pelo Instrutor e posterior publicação no catálogo.

```mermaid
sequenceDiagram
    actor Instrutor
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Instrutor->>FE: Acessa "Meus cursos"
    Instrutor->>FE: Aciona "Novo curso"
    Instrutor->>FE: Preenche título, descrição, preço, categoria
    FE->>API: POST /api/v1/instructor/courses
    alt campos válidos
        API->>DB: Insere curso (status = rascunho)
        DB-->>API: Curso criado
        API-->>FE: 201 Created
        FE-->>Instrutor: Exibe curso salvo como rascunho
    else campo obrigatório ausente
        API-->>FE: 422 Unprocessable Entity (VALIDATION_FAILED)
        FE-->>Instrutor: Indica campo pendente
    end

    Instrutor->>FE: Aciona "Publicar"
    FE->>API: PUT /api/v1/instructor/courses/{id} (status = publicado)
    API->>DB: Atualiza status do curso
    DB-->>API: OK
    API-->>FE: 200 OK
    FE-->>Instrutor: Curso visível no catálogo
```

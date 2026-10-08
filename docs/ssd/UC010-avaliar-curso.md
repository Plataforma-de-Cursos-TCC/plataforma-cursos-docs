# UC010 — Avaliar Curso

Diagrama de sequência do sistema para o caso de uso UC010 (Avaliar Curso). Representa a avaliação com nota e comentário realizada pelo Aluno matriculado, com validação de matrícula e recálculo da nota média.

```mermaid
sequenceDiagram
    actor Aluno
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Aluno->>FE: Acessa página do curso
    Aluno->>FE: Aciona "Avaliar curso"
    FE->>API: GET /avaliacoes/minha?curso_id
    API->>DB: Busca avaliação existente do aluno
    DB-->>API: Avaliação (ou vazio)
    API-->>FE: 200 OK
    Aluno->>FE: Informa nota e comentário
    Aluno->>FE: Confirma envio
    FE->>API: POST /avaliacoes (nota, comentário)
    alt aluno matriculado no curso
        API->>DB: Salva/atualiza avaliação
        DB-->>API: OK
        API->>DB: Recalcula nota média do curso
        DB-->>API: OK
        API-->>FE: 200 OK
        FE-->>Aluno: Avaliação salva
    else aluno não matriculado
        API-->>FE: 403 Forbidden
        FE-->>Aluno: Só alunos matriculados podem avaliar
    end
```

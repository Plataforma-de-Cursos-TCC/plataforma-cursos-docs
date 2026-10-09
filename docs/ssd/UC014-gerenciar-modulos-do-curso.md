# UC014 — Gerenciar Módulos do Curso

Diagrama de sequência do sistema para o caso de uso UC014 (Gerenciar Módulos do Curso). Representa a criação, a edição e a reordenação de módulos por um Instrutor dono do curso, a validação de título e de posição única e a exclusão de módulo com remoção das suas aulas e do seu quiz.

```mermaid
sequenceDiagram
    actor Instrutor
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Instrutor->>FE: Acessa o curso
    Note over FE,API: leitura do curso e da lista de módulos não consta no TDD (a definir)
    alt Novo módulo
        Instrutor->>FE: Aciona "Novo módulo"
        Instrutor->>FE: Informa título e posição
        Instrutor->>FE: Aciona "Salvar"
        FE->>API: POST /api/v1/instructor/courses/{id}/modules (título, posição)
        alt título informado e posição livre
            API->>DB: Verifica que o Instrutor é dono do curso
            DB-->>API: Dono confirmado
            API->>DB: Salva o módulo
            DB-->>API: Módulo salvo
            API-->>FE: 200 OK
            FE-->>Instrutor: Atualiza a lista de módulos
        else título ausente (E1)
            API-->>FE: 422 VALIDATION_FAILED (título obrigatório)
            FE-->>Instrutor: Bloqueia o salvamento e indica o campo obrigatório
        else posição já utilizada (E2)
            API-->>FE: 422 VALIDATION_FAILED (posição em uso)
            FE-->>Instrutor: Informa o conflito e solicita outra posição
        end
    else Editar ou reordenar módulo (A1)
        Instrutor->>FE: Seleciona um módulo e altera título ou posição
        FE->>API: PUT /api/v1/instructor/modules/{id} (título, posição)
        API->>DB: Atualiza o módulo
        DB-->>API: Módulo atualizado
        API-->>FE: 200 OK
        FE-->>Instrutor: Atualiza a lista de módulos
    else Excluir módulo (A2)
        Instrutor->>FE: Aciona "Excluir" e confirma
        Note over FE,API: endpoint de exclusão de módulo não consta no TDD (a definir)
        API->>DB: Remove o módulo, suas aulas e seu quiz
        DB-->>API: Exclusão concluída
        API-->>FE: Módulo removido
        FE-->>Instrutor: Atualiza a lista de módulos
    end
```

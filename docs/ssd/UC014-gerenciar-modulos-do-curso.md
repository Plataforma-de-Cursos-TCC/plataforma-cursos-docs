# UC014 — Gerenciar Módulos do Curso

Diagrama de sequência do sistema para o caso de uso UC014 (Gerenciar Módulos do Curso). Representa a criação, a edição e a reordenação de módulos por um Instrutor dono do curso, a validação de título e de posição única e a exclusão de módulo com remoção das suas aulas e do seu quiz. Editar e excluir verificam o dono do curso (R-1).

```mermaid
sequenceDiagram
    actor Instrutor
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Instrutor->>FE: Acessa o curso
    FE->>API: GET /api/v1/instructor/courses/{id}
    API->>DB: Busca o curso e os seus módulos
    DB-->>API: Curso e módulos
    API-->>FE: 200 OK (curso com módulos)
    FE-->>Instrutor: Exibe a lista de módulos
    alt Novo módulo
        Instrutor->>FE: Aciona "Novo módulo"
        Instrutor->>FE: Informa título e posição
        Instrutor->>FE: Aciona "Salvar"
        FE->>API: POST /api/v1/instructor/courses/{id}/modules (título, posição)
        API->>DB: Verifica que o Instrutor é dono do curso
        DB-->>API: Dono do curso
        alt Instrutor não é dono do curso (R-1)
            API-->>FE: 403 FORBIDDEN
            FE-->>Instrutor: Informa que o módulo não pode ser criado
        else título ausente (E1)
            API-->>FE: 422 VALIDATION_FAILED (título obrigatório)
            FE-->>Instrutor: Bloqueia o salvamento e indica o campo obrigatório
        else posição já utilizada (E2)
            API-->>FE: 422 VALIDATION_FAILED (posição em uso)
            FE-->>Instrutor: Informa o conflito e solicita outra posição
        else título informado e posição livre
            API->>DB: Salva o módulo
            DB-->>API: Módulo salvo
            API-->>FE: 201 Created
            FE-->>Instrutor: Atualiza a lista de módulos
        end
    else Editar ou reordenar módulo (A1)
        Instrutor->>FE: Seleciona um módulo e altera título ou posição
        FE->>API: PUT /api/v1/instructor/modules/{id} (título, posição)
        alt Instrutor é dono do curso e dados válidos
            API->>DB: Atualiza o módulo
            DB-->>API: Módulo atualizado
            API-->>FE: 200 OK
            FE-->>Instrutor: Atualiza a lista de módulos
        else Instrutor não é dono do curso (R-1)
            API-->>FE: 403 FORBIDDEN
            FE-->>Instrutor: Informa que o módulo não pode ser alterado
        else título ausente ou posição em uso (E1 e E2)
            API-->>FE: 422 VALIDATION_FAILED
            FE-->>Instrutor: Indica o erro e solicita a correção
        end
    else Excluir módulo (A2)
        Instrutor->>FE: Aciona "Excluir"
        FE-->>Instrutor: Avisa que as aulas e o quiz do módulo também serão removidos e pede confirmação
        Instrutor->>FE: Confirma a exclusão
        FE->>API: DELETE /api/v1/instructor/modules/{id}
        alt Instrutor é dono do curso
            API->>DB: Remove o módulo, as suas aulas e o seu quiz
            DB-->>API: Exclusão concluída
            API-->>FE: 204 No Content
            FE-->>Instrutor: Atualiza a lista de módulos
        else Instrutor não é dono do curso (R-1)
            API-->>FE: 403 FORBIDDEN
            FE-->>Instrutor: Informa que o módulo não pode ser excluído
        end
    end
```

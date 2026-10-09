# UC008 — Gerenciar Usuários

Diagrama de sequência do sistema para o caso de uso UC008 (Gerenciar Usuários). Representa a consulta de usuários pelo Administrador, a alteração de status (bloqueio e desbloqueio) com revogação ou restauração imediata do acesso, e a prevenção de bloqueio da própria conta logada. A exclusão não é uma ação de status: é o UC018, acionado a partir desta lista.

```mermaid
sequenceDiagram
    actor Administrador
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Administrador->>FE: Busca usuário (nome/e-mail/perfil)
    FE->>API: GET /api/v1/admin/users?filtro
    API->>DB: Consulta usuários
    DB-->>API: Lista de usuários
    API-->>FE: 200 OK
    FE-->>Administrador: Exibe lista de usuários
    Note over Administrador,FE: A1 filtro por perfil (Aluno, Instrutor ou Administrador) retorna ao passo de busca
    Administrador->>FE: Seleciona ação bloquear ou desbloquear
    Administrador->>FE: Confirma ação
    FE->>API: PUT /api/v1/admin/users/{id}/status
    alt usuário-alvo é a própria conta (E1)
        API-->>FE: 403 Forbidden
        FE-->>Administrador: Exibe aviso, não é possível bloquear a própria conta
    else usuário-alvo não existe mais (E2)
        API->>DB: Consulta usuário-alvo
        DB-->>API: Não encontrado
        API-->>FE: 404 Not Found
        FE-->>Administrador: Exibe "Usuário não encontrado" e atualiza a lista
    else usuário-alvo válido
        API->>DB: Atualiza status do usuário
        DB-->>API: OK
        API-->>FE: 200 OK
        FE-->>Administrador: Acesso revogado ou restaurado imediatamente
    end
    Note over Administrador,FE: A2 cancelar na confirmação descarta a ação, sem alterar o status
    Note over Administrador,FE: A3 "Excluir" aciona o UC018 (DELETE /api/v1/admin/users/{id}, 204 No Content)
```

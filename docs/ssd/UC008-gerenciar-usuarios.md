# UC008 — Gerenciar Usuários

Diagrama de sequência do sistema para o caso de uso UC008 (Gerenciar Usuários). Representa a consulta e atualização de status/perfil de usuários pelo Administrador, prevenindo alteração da própria conta logada.

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
    Administrador->>FE: Seleciona ação (bloquear/desbloquear/excluir)
    alt usuário-alvo != administrador logado
        Administrador->>FE: Confirma ação
        FE->>API: PUT /api/v1/admin/users/{id}/status
        API->>DB: Atualiza status do usuário
        DB-->>API: OK
        API-->>FE: 200 OK
        FE-->>Administrador: Acesso revogado/restaurado imediatamente
    else usuário-alvo é a própria conta
        API-->>FE: 403 Forbidden
        FE-->>Administrador: Exibe aviso de bloqueio impedido
    end
```

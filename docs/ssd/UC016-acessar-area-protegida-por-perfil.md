# UC016 — Acessar Área Protegida por Perfil

Diagrama de sequência do sistema para o caso de uso UC016 (Acessar Área Protegida por Perfil). Representa a verificação de sessão e de permissão do perfil antes de exibir uma área restrita, com negação de acesso registrada em trilha de auditoria.

```mermaid
sequenceDiagram
    actor Usuário
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Usuário->>FE: Acessa área protegida
    FE->>API: GET /api/v1/me/permissions
    alt sessão válida e perfil com permissão
        API->>DB: Busca perfil e permissões do usuário
        DB-->>API: Perfil e permissões
        API-->>FE: 200 OK
        FE-->>Usuário: Exibe a área
    else sessão ausente ou expirada
        API-->>FE: 401 UNAUTHENTICATED
        FE-->>Usuário: Redireciona para login (UC005)
    else perfil sem permissão
        API->>DB: Registra tentativa na trilha de auditoria
        DB-->>API: OK
        API-->>FE: 403 FORBIDDEN
        FE-->>Usuário: Exibe acesso negado
    end
```

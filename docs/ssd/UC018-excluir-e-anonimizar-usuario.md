# UC018 — Excluir e Anonimizar Usuário

Diagrama de sequência do sistema para o caso de uso UC018 (Excluir e Anonimizar Usuário). Representa a exclusão de conta pelo Administrador após confirmação com aviso de ação irreversível, com anonimização dos dados conforme LGPD e bloqueio da exclusão da própria conta.

```mermaid
sequenceDiagram
    actor Administrador
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Administrador->>FE: Aciona "Excluir" em um usuário
    FE-->>Administrador: Exibe "Excluir usuário?" com aviso de ação irreversível
    alt administrador cancela
        Administrador->>FE: Aciona "Cancelar"
        FE-->>Administrador: Fecha a confirmação sem alterações
    else administrador confirma
        Administrador->>FE: Confirma exclusão
        FE->>API: DELETE /api/v1/admin/users/{id}
        alt usuário-alvo é a própria conta
            API-->>FE: 403 FORBIDDEN
            FE-->>Administrador: Exibe aviso de exclusão impedida
        else usuário não encontrado ou já removido
            API->>DB: Consulta usuário
            DB-->>API: Não encontrado
            API-->>FE: 404 NOT_FOUND
            FE-->>Administrador: Exibe "Usuário não encontrado"
        else usuário válido
            API->>DB: Anonimiza dados pessoais e exclui conta
            DB-->>API: OK
            API-->>FE: 200 OK
            FE-->>Administrador: Exibe confirmação e atualiza a lista
        end
    end
```

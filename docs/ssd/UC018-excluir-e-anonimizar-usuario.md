# UC018 — Excluir e Anonimizar Usuário

Diagrama de sequência do sistema para o caso de uso UC018 (Excluir e Anonimizar Usuário, RF012). Estende o UC008 e é acionado pela ação "Excluir" da lista de usuários. Representa a exclusão de conta pelo Administrador após confirmação com aviso de ação irreversível, com anonimização dos dados conforme LGPD, bloqueio da exclusão da própria conta e atualização da lista após a exclusão.

```mermaid
sequenceDiagram
    actor Administrador
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Administrador->>FE: Aciona "Excluir" em um usuário
    FE-->>Administrador: Exibe "Excluir usuário?" com aviso de ação irreversível
    alt administrador cancela (A1)
        Administrador->>FE: Aciona "Cancelar"
        FE-->>Administrador: Fecha a confirmação sem alterações
    else administrador confirma
        Administrador->>FE: Confirma exclusão
        FE->>API: DELETE /api/v1/admin/users/{id}
        alt usuário-alvo é a própria conta (E1)
            API-->>FE: 403 FORBIDDEN
            FE-->>Administrador: Exibe "Não é possível excluir a própria conta"
        else usuário não encontrado ou já removido (E2)
            API->>DB: Consulta usuário
            DB-->>API: Não encontrado
            API-->>FE: 404 NOT_FOUND
            FE-->>Administrador: Exibe "Usuário não encontrado" e atualiza a lista
        else usuário válido
            API->>DB: Anonimiza dados pessoais, mantém histórico anonimizado e revoga acesso
            DB-->>API: OK
            API->>DB: Registra a exclusão na trilha de auditoria (RNF016)
            API-->>FE: 204 No Content
            FE-->>Administrador: Exibe "Usuário excluído" e retira o usuário da lista
        end
    end
```

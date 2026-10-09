# UC017 — Alterar Senha

Diagrama de sequência do sistema para o caso de uso UC017 (Alterar Senha). Representa a alteração de senha pelo Usuário logado, no bloco da tela Meu perfil, com validação da senha atual e da nova senha pela API.

```mermaid
sequenceDiagram
    actor Usuário
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Usuário->>FE: Acessa Meu perfil e aciona "Alterar senha"
    Usuário->>FE: Informa senha atual, nova senha e confirmação
    alt usuário cancela
        Usuário->>FE: Aciona "Cancelar"
        FE-->>Usuário: Descarta os campos preenchidos
    else usuário confirma
        Usuário->>FE: Confirma alteração
        FE->>API: PUT /api/v1/profile/password (senha atual, nova senha)
        API->>DB: Busca senha atual do usuário logado
        DB-->>API: Senha atual
        alt senha atual correta e nova senha válida
            API->>DB: Atualiza senha do usuário
            DB-->>API: OK
            API-->>FE: 200 OK
            FE-->>Usuário: Exibe confirmação de alteração
        else senha atual incorreta ou nova senha fora da política
            API-->>FE: 422 VALIDATION_FAILED
            FE-->>Usuário: Exibe erro no campo correspondente
        end
    end
```

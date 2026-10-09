# UC017 — Alterar Senha

Diagrama de sequência do sistema para o caso de uso UC017 (Alterar Senha, RF019), acionado a partir da tela Meu perfil (UC013). Representa a alteração de senha pelo Usuário logado, com conferência local de confirmação (R-3), validação da senha atual e da nova senha pela API e erro exibido no campo correspondente.

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
        alt confirmação diferente da nova senha (R-3)
            FE-->>Usuário: Exibe erro no campo de confirmação, sem chamar a API
        else confirmação igual à nova senha
            FE->>API: PUT /api/v1/profile/password (senha atual, nova senha)
            API->>DB: Busca senha atual do usuário logado
            DB-->>API: Senha atual
            alt senha atual correta e nova senha válida
                API->>DB: Atualiza senha do usuário
                DB-->>API: OK
                API-->>FE: 200 OK
                FE-->>Usuário: Exibe confirmação de alteração
            else senha atual incorreta ou nova senha fora da política (E1 e E2)
                API-->>FE: 422 VALIDATION_FAILED
                FE-->>Usuário: Exibe erro no campo correspondente
            end
        end
    end
```

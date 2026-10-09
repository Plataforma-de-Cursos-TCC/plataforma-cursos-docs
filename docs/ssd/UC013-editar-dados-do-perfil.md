# UC013 — Editar Dados do Perfil

Diagrama de sequência do sistema para o caso de uso UC013 (Editar Dados do Perfil). Representa a leitura e a atualização dos dados do perfil do Usuário autenticado, a validação de campos, o acesso ao fluxo de Instrutor e o encaminhamento para a alteração de senha (UC017).

```mermaid
sequenceDiagram
    actor Usuário
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Usuário->>FE: Acessa a tela "Meu perfil"
    FE->>API: GET /api/v1/profile
    API->>DB: Busca dados do perfil do usuário logado
    DB-->>API: Dados do perfil
    API-->>FE: 200 OK (dados do perfil)
    FE-->>Usuário: Exibe nome, foto e opção "Alterar senha"
    Usuário->>FE: Altera nome ou foto
    opt Instrutor edita minibiografia e links (A1)
        Usuário->>FE: Altera minibiografia ou links
    end
    Usuário->>FE: Aciona "Salvar"
    FE->>API: PUT /api/v1/profile (nome, foto)
    alt dados válidos
        API->>DB: Atualiza o perfil
        DB-->>API: Perfil atualizado
        API-->>FE: 200 OK
        FE-->>Usuário: Exibe "Alterações salvas"
    else campo inválido (E1)
        API-->>FE: 422 VALIDATION_FAILED (nome vazio ou imagem fora do formato)
        FE-->>Usuário: Indica o campo e solicita a correção
    end
    opt Usuário aciona "Alterar senha" (A2)
        Usuário->>FE: Aciona "Alterar senha"
        FE->>API: PUT /api/v1/profile/password (UC017)
    end
```

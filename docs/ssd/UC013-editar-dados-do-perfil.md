# UC013 — Editar Dados do Perfil

Diagrama de sequência do sistema para o caso de uso UC013 (Editar Dados do Perfil). Representa a leitura e a atualização dos dados do perfil do Usuário autenticado (nome, telefone, endereço, CPF, data de nascimento, foto e tema), a validação de campos, a edição de minibiografia e links do Instrutor (A1) e o encaminhamento para a alteração de senha (A2, UC017).

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
    FE-->>Usuário: Exibe os campos do perfil, o tema e a opção "Alterar senha"
    opt Usuário é Instrutor (A1)
        FE->>API: GET /api/v1/instructor/profile
        API-->>FE: 200 OK (minibiografia e links)
        FE-->>Usuário: Exibe minibiografia e links
    end
    Usuário->>FE: Altera um ou mais dados (nome, telefone, endereço, CPF, data de nascimento, foto ou tema)
    Usuário->>FE: Aciona "Salvar"
    FE->>API: PUT /api/v1/profile (nome, telefone, endereço, CPF, data de nascimento, foto, tema)
    alt dados válidos
        API->>DB: Atualiza o perfil
        DB-->>API: Perfil atualizado
        API-->>FE: 200 OK
        FE-->>Usuário: Exibe "Alterações salvas"
    else campo inválido (E1)
        API-->>FE: 422 VALIDATION_FAILED (campo e regra não atendida)
        FE-->>Usuário: Indica o campo e solicita a correção
    end
    opt Instrutor altera minibiografia ou links (A1)
        FE->>API: PUT /api/v1/instructor/profile (minibiografia, links)
        API->>DB: Atualiza o perfil de Instrutor
        DB-->>API: OK
        API-->>FE: 200 OK
    end
    opt Usuário aciona "Alterar senha" (A2)
        Usuário->>FE: Aciona "Alterar senha"
        Note over FE,API: executa o UC017 – Alterar Senha (PUT /api/v1/profile/password)
    end
```

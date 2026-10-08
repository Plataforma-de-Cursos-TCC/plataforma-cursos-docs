# UC011 — Recuperar Senha

Diagrama de sequência do sistema para o caso de uso UC011 (Recuperar Senha). Representa a solicitação de redefinição de senha pelo Visitante, geração segura do link de expiração e posterior atualização da senha com validação de token.

```mermaid
sequenceDiagram
    actor Visitante
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Visitante->>FE: Aciona "Esqueci minha senha"
    Visitante->>FE: Informa e-mail
    FE->>API: POST /recuperar-senha (email)
    API->>DB: Busca usuário pelo e-mail
    DB-->>API: Usuário (ou não encontrado)
    alt e-mail cadastrado
        API->>API: Gera link de redefinição com expiração
        API-->>FE: 200 OK (e-mail enviado)
    else e-mail não cadastrado
        API-->>FE: 200 OK (mesma mensagem genérica)
    end
    FE-->>Visitante: Exibe confirmação de envio
    Visitante->>FE: Acessa link e informa nova senha
    FE->>API: POST /redefinir-senha (token, nova_senha)
    alt token válido
        API->>DB: Atualiza senha do usuário
        DB-->>API: OK
        API-->>FE: 200 OK
        FE-->>Visitante: Senha redefinida, redireciona pro login
    else token expirado
        API-->>FE: 400 Bad Request (token expirado)
        FE-->>Visitante: Oferece solicitar novo link
    end
```

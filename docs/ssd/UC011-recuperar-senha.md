# UC011 — Recuperar Senha

Diagrama de sequência do sistema para o caso de uso UC011 (Recuperar Senha). Representa a solicitação de redefinição de senha pelo Usuário que não lembra a senha, geração segura do link de uso único com expiração de 30 minutos, invalidação de link anterior ainda válido e atualização da senha com validação de token.

```mermaid
sequenceDiagram
    actor Usuário
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Usuário->>FE: Aciona "Esqueci minha senha" na tela de login
    Usuário->>FE: Informa e-mail cadastrado
    FE->>API: POST /api/v1/auth/forgot-password (email)
    API->>DB: Busca usuário pelo e-mail
    DB-->>API: Usuário (ou não encontrado)
    alt e-mail cadastrado
        opt link anterior ainda válido (A1)
            API->>DB: Invalida link anterior
            DB-->>API: OK
        end
        API->>API: Gera link de uso único com expiração de 30 min
        API-->>FE: 200 OK (e-mail enviado)
    else e-mail não cadastrado (E1)
        API-->>FE: 200 OK (mesma mensagem genérica)
    end
    FE-->>Usuário: Exibe confirmação de envio
    Note over Usuário,FE: A2 o Usuário fecha a tela sem informar nova senha, senha atual mantida
    Usuário->>FE: Acessa link e informa nova senha
    FE->>API: POST /api/v1/auth/reset-password (token, nova_senha)
    alt token válido
        API->>DB: Atualiza senha do usuário
        DB-->>API: OK
        API-->>FE: 200 OK
        FE-->>Usuário: Senha redefinida, redireciona para o login
    else link expirado ou já utilizado (E2)
        API-->>FE: 422 Unprocessable Entity VALIDATION_FAILED (token expirado ou já utilizado)
        FE-->>Usuário: Informa expiração e oferece solicitar novo link
    end
```

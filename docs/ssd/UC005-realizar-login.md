# UC005 — Realizar Login

Diagrama de sequência do sistema para o caso de uso UC005 (Realizar Login). Representa a autenticação de credenciais de um Visitante através do front-end web, emissão da sessão (JWT em cookie HttpOnly, ADR-0008) pela API ou resposta de erro genérica.

```mermaid
sequenceDiagram
    actor Visitante
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Visitante->>FE: Acessa tela de login
    Visitante->>FE: Informa e-mail e senha
    FE->>API: POST /api/v1/auth/login (email, senha, rememberMe)
    API->>DB: Busca usuário pelo e-mail
    DB-->>API: Retorna usuário
    alt credenciais válidas
        API->>API: Valida senha e gera JWT e cookie de sessão
        API-->>FE: 200 OK + cookie de sessão
        FE-->>Visitante: Redireciona para área do perfil
    else credenciais inválidas
        API-->>FE: 401 Unauthorized
        FE-->>Visitante: Exibe mensagem de erro genérica
    end
```

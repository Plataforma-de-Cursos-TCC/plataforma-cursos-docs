# UC005 — Realizar Login

Diagrama de sequência do sistema para o caso de uso UC005 (Realizar Login). Representa a autenticação de credenciais de um Usuário (Aluno, Instrutor ou Administrador) através do front-end web, emissão da sessão (JWT em cookie HttpOnly, ADR-0008) pela API, direcionamento à área do perfil ou resposta de erro genérica.

```mermaid
sequenceDiagram
    actor Usuário
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Usuário->>FE: Acessa tela de login
    alt sessão ainda válida no navegador (A2)
        FE->>API: GET /api/v1/auth/me
        API-->>FE: 200 OK + usuário autenticado
        FE-->>Usuário: Direciona para a área do perfil
    else sem sessão válida
        Usuário->>FE: Informa e-mail e senha
        Usuário->>FE: Aciona "Entrar"
        FE->>API: POST /api/v1/auth/login (email, senha, rememberMe)
        API->>DB: Busca usuário pelo e-mail
        DB-->>API: Retorna usuário (ou vazio)
        alt credenciais válidas
            API->>API: Valida senha e gera JWT e cookie de sessão
            API-->>FE: 200 OK + cookie de sessão
            FE->>API: GET /api/v1/me/permissions
            API-->>FE: Perfil do Usuário
            FE-->>Usuário: Direciona para a área do perfil (UC016)
        else credenciais inválidas (E1)
            API-->>FE: 401 Unauthorized
            FE-->>Usuário: Exibe mensagem de erro genérica
        end
    end
    Note over Usuário,FE: A1 "Esqueci minha senha" inicia UC011
    Note over FE,API: E2 sessão expirada em área protegida redireciona para a tela de login
```

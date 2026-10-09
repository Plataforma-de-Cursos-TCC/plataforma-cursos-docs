# UC012 — Cadastrar-se na Plataforma

Diagrama de sequência do sistema para o caso de uso UC012 (Cadastrar-se na Plataforma). Representa o cadastro de um Visitante com e-mail e senha, a validação de unicidade do e-mail e dos critérios da senha, a criação da conta com perfil Aluno ou Instrutor e o direcionamento ao login.

```mermaid
sequenceDiagram
    actor Visitante
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    Visitante->>FE: Acessa a tela de cadastro
    Visitante->>FE: Informa e-mail e senha, e aceita termos e política de privacidade
    opt Escolhe perfil de Instrutor (A1)
        Visitante->>FE: Seleciona cadastro como Instrutor
    end
    Visitante->>FE: Aciona "Criar conta"
    FE->>API: POST /api/v1/auth/register (e-mail, senha, aceite, perfil)
    API->>DB: Verifica unicidade do e-mail
    DB-->>API: Resultado da busca
    alt e-mail livre e senha dentro dos critérios
        API->>DB: Cria conta com perfil Aluno (ou Instrutor) e senha com hash
        DB-->>API: Conta criada
        API-->>FE: Cadastro confirmado
        FE-->>Visitante: Exibe "Conta criada. Entre para continuar"
        FE-->>Visitante: Direciona ao login (UC005)
    else e-mail já cadastrado (E1)
        API-->>FE: 422 VALIDATION_FAILED (e-mail em uso)
        FE-->>Visitante: Informa e-mail em uso e sugere login ou recuperação de senha (UC011)
    else senha fora dos critérios (E2)
        API-->>FE: 422 VALIDATION_FAILED (critérios da senha)
        FE-->>Visitante: Exibe os critérios e solicita nova senha
    end
```

# UC018 — Excluir e Anonimizar Usuário

Diagrama de sequência do sistema para o caso de uso UC018 (Excluir e Anonimizar Usuário, RF012), atualizado conforme a [ADR-0014](../adr/0014-exclusao-logica-e-anonimizacao.md). Estende o UC008 e é acionado pela ação "Excluir" da lista de usuários (inclusive no atendimento a pedido de exclusão/anonimização feito pelo próprio titular via perfil/DPO, LGPD art. 18, VI). Representa a exclusão lógica reversível pelo Administrador (`status = deleted`, `deleted_at = NOW()`), o tratamento dos cursos de Instrutor (A4: arquivamento ou exclusão lógica em cascata), a revogação imediata de acessos (blocklist de `jti` no Redis e revogação de sessões de refresh), a reativação antes da anonimização (A2, bloqueada em E3 se já anonimizada) e a anonimização irreversível como passo separado (A3, a pedido do titular ou após 30 dias de carência).

```mermaid
sequenceDiagram
    actor Administrador
    participant FE as Front-end web
    participant API
    participant DB as Banco de Dados

    alt Fluxo básico — Exclusão lógica (ADR-0014)
        Administrador->>FE: Aciona "Excluir" em um usuário
        FE-->>Administrador: Exibe "Excluir usuário?" com aviso de exclusão lógica reversível
        alt administrador cancela (A1)
            Administrador->>FE: Aciona "Cancelar"
            FE-->>Administrador: Fecha a confirmação sem alterações
        else administrador confirma
            Administrador->>FE: Confirma exclusão (e opção de cursos se Instrutor, A4)
            FE->>API: DELETE /api/v1/admin/users/{id}
            alt usuário-alvo é a própria conta (E1)
                API-->>FE: 403 FORBIDDEN
                FE-->>Administrador: Exibe "Não é possível excluir a própria conta"
            else usuário não encontrado ou já excluído (E2)
                API->>DB: Consulta usuário
                DB-->>API: Não encontrado
                API-->>FE: 404 NOT_FOUND
                FE-->>Administrador: Exibe "Usuário não encontrado" e atualiza a lista
            else usuário válido
                API->>DB: Aplica exclusão lógica (status=deleted, deleted_at=NOW()), preserva histórico
                opt Instrutor com cursos publicados (A4)
                    API->>DB: Arquiva cursos (status=archived) ou aplica exclusão lógica em cascata
                end
                API->>DB: Revoga sessões de refresh e adiciona jti na blocklist do Redis
                API->>DB: Registra USER_DELETE em audit_logs (RNF016)
                DB-->>API: OK
                API-->>FE: 204 No Content
                FE-->>Administrador: Exibe "Usuário excluído" e retira da listagem ativa
            end
        end
    else A2 — Reativação de conta excluída antes da anonimização
        Administrador->>FE: Aciona "Reativar" na conta excluída e confirma
        FE->>API: PATCH /api/v1/admin/users/{id}/restore
        API->>DB: Consulta usuário (verifica anonymized_at)
        alt conta já anonimizada (E3)
            API-->>FE: 422 VALIDATION_FAILED (fields.user)
            FE-->>Administrador: Informa que a anonimização é irreversível (LGPD)
        else conta elegível
            API->>DB: Restaura status=active e deleted_at=NULL
            API->>DB: Registra USER_RESTORE em audit_logs (RNF016)
            DB-->>API: OK
            API-->>FE: 200 OK (UserAdminResource)
            FE-->>Administrador: Conta reativada na listagem ativa
        end
    else A3 — Anonimização irreversível (pedido do titular ou 30 dias sem reativação)
        Administrador->>FE: Aciona "Anonimizar" na conta excluída e confirma
        FE->>API: POST /api/v1/admin/users/{id}/anonymize
        API->>DB: Limpa/substitui PII (nome, e-mail sintético, CPF, telefone, foto no R2, endereços) e preenche anonymized_at=NOW()
        API->>DB: Registra USER_ANONYMIZE em audit_logs (RNF016)
        DB-->>API: OK
        API-->>FE: 204 No Content
        FE-->>Administrador: Confirma anonimização irreversível mantendo integridade histórica
    end
```

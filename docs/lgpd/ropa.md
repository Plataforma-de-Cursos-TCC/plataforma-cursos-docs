---
id: lgpd-ropa
titulo: "ROPA — Registro de Operações de Tratamento de Dados Pessoais"
tipo: documento-projeto
status: rascunho
atualizado: 2026-11-25
relacionados: [pesquisa-lgpd, lgpd-ripd, lgpd-encarregado, tdd, sdd, adr-0010, adr-0014, adr-0016, adr-0019]
---
# ROPA — Registro de Operações de Tratamento de Dados Pessoais

> Artefato de conformidade exigido pelo art. 37 da LGPD (Lei nº 13.709/2018) e pelo RNF024. Derivado do modelo lógico de dados (Item 12) e do [TDD](../tdd.md). Deve ser revisado a cada mudança de entidade, fluxo de dados ou operador externo.

## 1. Identificação do controlador

- **Produto:** Plataforma de Cursos
- **Controlador:** Equipe responsável pela Plataforma de Cursos (identificação formal da pessoa jurídica ou entidade controladora a definir antes de entrada em produção).
- **Encarregado (DPO):** a definir pelo grupo (detalhes em [encarregado-e-canais.md](encarregado-e-canais.md)).
- **Base legal de referência:** [pesquisa/lgpd.md](../../pesquisa/lgpd.md) (F81 a F89).

---

## 2. Matriz de operações de tratamento (por área e entidade)

### 2.1 Área A — Acesso e conta (módulo Auth)

| Operação / Tabela | Dados pessoais tratados | Finalidade | Base legal (LGPD) | Operadores envolvidos | Retenção e término | Compartilhamento |
|---|---|---|---|---|---|---|
| Cadastro e gestão de conta (`users`) | `name`, `email`, `password_hash`, `role`, `status`, `theme`, `locale`, `terms_accepted_at`, `phone`, `document_number` (CPF), `birth_date`, `photo` | Criar e autenticar conta de Usuário (Aluno, Instrutor, Administrador), personalizar interface e registrar aceite de termos | Execução de contrato (art. 7º, V); cumprimento de obrigação legal para registro de aceite e verificação etária (art. 7º, II); consentimento específico quando aplicável a opcionais ou menores (arts. 7º, I, e 14) | Railway (API e PostgreSQL 16 `core`), Vercel (front-end SPA), Cloudflare R2 (foto de perfil via `media-service`) | Enquanto a conta estiver ativa; após exclusão lógica (`deleted_at`), carência de até 30 dias ou anonimização imediata a pedido do titular (`anonymized_at`, ADR-0014) | Sem compartilhamento comercial; acesso restrito aos operadores de infraestrutura |
| Endereços cadastrais (`addresses`) | `type`, `street`, `number`, `complement`, `district`, `city`, `state`, `zip_code`, `country` | Registro cadastral opcional do Usuário *(nota de minimização: revisar obrigatoriedade frente ao art. 6º, III, já que não há entrega física nem cobrança real)* | Execução de contrato / consentimento opcional (art. 7º, I ou V) | Railway (PostgreSQL 16 `core`) | Enquanto a conta estiver ativa; removidos/sobrescritos na anonimização da conta (ADR-0014) | Sem compartilhamento com terceiros |
| Perfil público do Instrutor (`instructor_profiles`) | `bio`, `headline`, `social_links` | Apresentar credenciais profissionais do Instrutor nas páginas de curso | Execução de contrato (art. 7º, V) | Railway (PostgreSQL 16 `core`) | Enquanto o Instrutor mantiver conta ativa; descaracterizado na anonimização | Exibido publicamente no catálogo de cursos |
| Recuperação de senha (`password_reset_tokens`) | `user_id`, `token_hash`, `expires_at`, `used_at` (+ envio de `email`) | Permitir redefinição segura de senha com token de uso único (RNF017) | Execução de contrato e segurança da conta (art. 7º, V e IX) | Railway (PostgreSQL 16 `core`), provedor de e-mail transacional | Token válido por 30 min; expurgo periódico de tokens expirados/usados | E-mail de destino trafega apenas ao provedor de e-mail transacional |
| Sessão persistente (`refresh_sessions` e cookies JWT) | `user_id`, `token_hash`, `family_id`, `jti` (Redis), cookies `__Host-access` e `__Secure-refresh` | Manter autenticação segura (RS256, ADR-0008), renovação «manter conectado» e revogação imediata | Execução de contrato e legítimo interesse para cookies estritamente necessários (art. 7º, V e IX; Guia de Cookies ANPD) | Railway (PostgreSQL 16 `core`, Redis), Vercel (proxy `/api/*`) | Access token: 1 h; refresh session: 30 dias ou até logout/revogação | Sem compartilhamento com terceiros |

### 2.2 Área B — Autoria do instrutor (módulo Authoring)

| Operação / Tabela | Dados pessoais tratados | Finalidade | Base legal (LGPD) | Operadores envolvidos | Retenção e término | Compartilhamento |
|---|---|---|---|---|---|---|
| Autoria de cursos, aulas e materiais (`courses`, `modules`, `lessons`, `lesson_materials`) | `instructor_id`, imagem e voz do Instrutor em vídeos (`video_key`), nome/conteúdo em materiais (`file_key`), `thumbnail_key` | Publicação e entrega pedagógica de cursos em vídeo e materiais complementares | Execução de contrato (art. 7º, V) | Railway (API, `media-service`, PostgreSQL 16 `core`), Cloudflare R2 (bucket privado) | Enquanto o curso estiver publicado ou arquivado com alunos ativos; exclusão física de mídia e embeddings quando o curso for excluído em cascata | Acesso restrito a Alunos matriculados (ou prévias `is_preview`) via URL assinada de 15 min (ADR-0019) |

### 2.3 Área C — Aprendizagem do aluno (módulo Learning)

| Operação / Tabela | Dados pessoais tratados | Finalidade | Base legal (LGPD) | Operadores envolvidos | Retenção e término | Compartilhamento |
|---|---|---|---|---|---|---|
| Matrículas e progresso (`enrollments`, `lesson_progress`) | `user_id`, `course_id`, `status`, `price_paid_cents`, `completed`, `watched_seconds`, `completed_at` | Liberar acesso às aulas, retomar reprodução e compor métricas de conclusão | Execução de contrato (art. 7º, V) | Railway (PostgreSQL 16 `core`) | Mantido enquanto a conta estiver ativa; preservado de forma anonimizada após anonimização do titular (ADR-0014, LGPD art. 16, IV) | Métricas agregadas exibidas ao Instrutor dono do curso e ao Administrador no dashboard |
| Pagamento simulado (`payments`) | `user_id`, `course_id`, `enrollment_id`, `purpose`, `amount_cents`, `currency`, `status`, `paid_at` (sem dados de cartão) | Registrar transações simuladas de matrícula ou pacotes de crédito do Tutor de IA (RF014, RF020) | Execução de contrato (art. 7º, V) | Railway (PostgreSQL 16 `core`) | Preservado de forma anonimizada após anonimização do titular (ADR-0014) | Nenhum gateway financeiro externo (pagamento 100% simulado) |
| Tentativas e respostas de quiz (`quiz_attempts`, `quiz_answers`) | `enrollment_id`, `quiz_id`, `score`, `submitted_at`, alternativas marcadas | Correção automática e acompanhamento de aprendizagem | Execução de contrato (art. 7º, V) | Railway (PostgreSQL 16 `core`) | Preservado de forma anonimizada após anonimização do titular | Desempenho agregado visível ao Instrutor do curso |
| Avaliações de curso (`reviews`) | `user_id`, `course_id`, `rating`, `comment` | Permitir que o Aluno avalie cursos concluídos/matriculados | Execução de contrato / consentimento na publicação do comentário (art. 7º, I e V) | Railway (PostgreSQL 16 `core`) | Enquanto a conta estiver ativa; na anonimização, desvincular autoria e expurgar eventual PII em `comment` | Exibido na página do curso (nota e comentário) |

### 2.4 Área D — Tutor de IA, analytics e administração (`ai-service` e módulos Admin/Analytics)

| Operação / Tabela | Dados pessoais tratados | Finalidade | Base legal (LGPD) | Operadores envolvidos | Retenção e término | Compartilhamento |
|---|---|---|---|---|---|---|
| Conversas com Tutor de IA (`conversations`, `messages`, `tutor_credit_packs`) | `user_id`, `course_id`, `lesson_id`, texto livre da pergunta (`content`) que pode conter PII incidental, respostas com timestamp | Esclarecer dúvidas do Aluno no contexto da aula via RAG (UC001, RF009) | Execução de contrato (art. 7º, V); para menores, salvaguardas do art. 14 | Railway (API, `ai-service`, PostgreSQL 16 `core` e `ai`, RabbitMQ, Redis), provedor externo de LLM | Mantido para histórico do Aluno enquanto a conta estiver ativa; na anonimização, expurgar ou descaracterizar PII em `messages.content` | Apenas texto da dúvida (sem metadados cadastrais de PII) e trechos da aula trafegam ao provedor de LLM, sob cláusula *zero-training* |
| Transcrição e indexação vetorial (database `ai` — `pgvector`) | Transcrição da voz do Instrutor (chunks e embeddings por `course_id` e `lesson_id`) | Permitir busca semântica restrita ao curso e citação de timestamp (RNF004) | Execução de contrato (art. 7º, V) | Railway (`ai-service`, PostgreSQL 16 `ai`, RabbitMQ), provedor de transcrição (STT), Cloudflare R2 | Gerado uma única vez por aula (RNF004); removido quando o vídeo for substituído ou o curso excluído | Áudio da aula trafega ao serviço de transcrição (STT) sob DPA sem retenção para treino |
| Trilha de auditoria e logs (`audit_logs` e logs de aplicação) | `user_id`, `action`, `target_type`, `target_id`, `ip_address`, `user_agent`, `details`, `created_at` | Garantir responsabilização administrativa, segurança e atendimento a obrigações legais (RNF016, ADR-0016, MCI art. 15) | Cumprimento de obrigação legal (art. 7º, II — MCI art. 15) e exercício regular de direitos / segurança (art. 7º, VI e IX) | Railway (PostgreSQL 16 `core`), Cloudflare R2 (arquivo frio compactado) | `audit_logs`: 12 meses no PostgreSQL + 5 anos no R2 via `audit:archive` (ADR-0016) com descarte automático ao término; logs de aplicação: mínimo de 6 meses para registros de acesso (MCI art. 15; revisar meta de 90 dias da ADR-0016) | Sem compartilhamento com terceiros, salvo requisição legal ou autoridade competente |

---

## 3. Transferência internacional e contratos com operadores (L12)

Em conformidade com os arts. 33 a 36 e 39 da LGPD, a **Resolução CD/ANPD nº 19/2024** (`[F89]`) e o **RNF023**, todo fornecedor externo que armazena ou processa dados pessoais atua como **operador** e pode envolver transferência internacional de dados (servidores fora do Brasil, em especial EUA/UE).

### 3.1 Inventário de operadores e requisitos contratuais

| Operador / Categoria | Serviço na plataforma | Dados que trafegam | Risco de transferência internacional | Requisitos obrigatórios no contrato (DPA) |
|---|---|---|---|---|
| **Vercel** | Hospedagem do front-end SPA e proxy `/api/*` (ADR-0010) | Requisições HTTPS, IP de origem, cabeçalhos e cookies de sessão | Sim (rede edge global / EUA) | DPA assinado + Cláusulas-Padrão Contratuais (Res. CD/ANPD nº 19/2024) + logs sem payload sensível |
| **Railway** | Hospedagem da API, `ai-service`, `media-service`, PostgreSQL 16 (`core` e `ai`), Redis e RabbitMQ (ADR-0010, ADR-0017) | Toda a base relacional, vetorial, filas e cache | Sim (regiões EUA/UE) | DPA assinado + Cláusulas-Padrão Contratuais (Res. CD/ANPD nº 19/2024) + bancos sem exposição pública + criptografia em repouso e trânsito |
| **Cloudflare (R2)** | Armazenamento privado de vídeos, materiais, capas, fotos e arquivo frio de auditoria (ADR-0010, ADR-0016, ADR-0019) | Vídeos (voz/imagem do Instrutor), materiais, fotos de perfil, JSONL de auditoria | Sim (infraestrutura global/EUA) | DPA assinado + Cláusulas-Padrão Contratuais (Res. CD/ANPD nº 19/2024) + bucket estritamente privado com acesso por URL assinada |
| **Provedor de LLM** *(a selecionar)* | Inferência do Tutor de IA em streaming (SDD seção 4) | Pergunta do Aluno (texto livre) e chunks da transcrição da aula | Sim (API de nuvem estrangeira) | DPA + CPCs (Res. 19/2024) + **cláusula expressa *zero-training*** (vedação de uso de prompts/respostas para treino) + retenção zero ou mínima de logs no provedor |
| **Provedor de STT (transcrição)** *(a selecionar)* | Transcrição de áudio das videoaulas (RNF004) | Faixa de áudio do Instrutor e transcrição textual | Sim (API de nuvem estrangeira) | DPA + CPCs (Res. 19/2024) + vedação de treino de modelos e descarte imediato do áudio após transcrição |
| **Provedor de e-mail transacional** *(a selecionar)* | Envio de link de redefinição de senha (UC011) | Endereço de e-mail do Usuário e link temporário (30 min) | Possível (conforme provedor) | DPA + CPCs (se fora do Brasil) + retenção mínima de logs de entrega e TLS obrigatório |

### 3.2 Salvaguardas de transferência internacional

1. **Mecanismo jurídico:** adoção das Cláusulas-Padrão Contratuais (CPCs) da Resolução CD/ANPD nº 19/2024 ou país/organismo reconhecido com nível adequado pela ANPD antes da entrada em produção com dados reais.
2. **Transparência ao titular:** a Política de Privacidade pública (RNF020, RNF025) deve informar expressamente a lista de categorias de operadores, os países de destino e as salvaguardas adotadas (LGPD, art. 9º e art. 33).
3. **Minimização antes do envio:** a API não envia nome, e-mail, CPF, telefone ou endereço do Aluno ao provedor de LLM; o `ai-service` deve aplicar filtro/alerta para PII informada incidentalmente em texto livre.

---

## Ligações

- **Pesquisa legal:** [pesquisa/lgpd.md](../../pesquisa/lgpd.md) · [pesquisa/fontes.md](../../pesquisa/fontes.md)
- **Demais artefatos LGPD:** [RIPD](ripd.md) · [Encarregado e canais públicos](encarregado-e-canais.md)
- **Arquitetura e dados:** [TDD](../tdd.md) · [SDD](../sdd.md) · [Item 12 — Modelo de dados](../../especificacao/12-modelo-de-dados/00-item.md)
- **Requisitos e decisões:** [Item 8 — RNFs](../../especificacao/08-requisitos-nao-funcionais/00-item.md) · [ADR-0010](../adr/0010-hospedagem-e-armazenamento.md) · [ADR-0014](../adr/0014-exclusao-logica-e-anonimizacao.md) · [ADR-0016](../adr/0016-retencao-de-logs-e-auditoria.md) · [ADR-0019](../adr/0019-upload-pela-api.md)

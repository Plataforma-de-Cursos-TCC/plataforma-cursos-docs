---
id: lgpd-ripd
titulo: "RIPD — Relatório de Impacto à Proteção de Dados Pessoais (Tutor de IA e Menores)"
tipo: documento-projeto
status: rascunho
atualizado: 2026-11-25
relacionados: [pesquisa-lgpd, lgpd-ropa, lgpd-encarregado, sdd, tdd, adr-0005, adr-0014]
---
# RIPD — Relatório de Impacto à Proteção de Dados Pessoais (Rascunho para Revisão)

> **Status:** rascunho técnico para revisão pelo grupo e pelo Encarregado (DPO) antes de entrada em produção. Elaborado em conformidade com os arts. 5º, XVII, e 38 da LGPD (Lei nº 13.709/2018) e o RNF024.

## 1. Escopo e justificativa do relatório

Este Relatório de Impacto à Proteção de Dados Pessoais (RIPD) avalia dois tratamentos de **alto risco** identificados na Plataforma de Cursos ([pesquisa/lgpd.md](../../pesquisa/lgpd.md)):

1. **Tutor de IA (IA generativa com RAG — UC001, `ai-service`):** processamento de perguntas em texto livre de Alunos e transcrições de voz de Instrutores, com envio a provedor externo de modelo de linguagem (LLM) e serviço de transcrição (STT), gerando risco de exposição incidental de dados pessoais ou sensíveis, alucinação pedagógica e transferência internacional.
2. **Tratamento de dados de crianças e adolescentes (LGPD, art. 14; ECA, art. 2º; Enunciado CD/ANPD nº 1/2023):** a plataforma de cursos online pode ser acessada por adolescentes (12 a 18 anos) e, se não houver trava etária no cadastro (UC012), por crianças (menores de 12 anos), o que exige salvaguardas reforçadas no cadastro, no perfil e na interação com o Tutor de IA.

---

## 2. Descrição dos tratamentos avaliados

### 2.1 Tutor de IA (`ai-service`)
- **Fluxo de ingestão (RNF004):** após upload de videoaula pelo Instrutor via API/`media-service`, um job no RabbitMQ aciona o `ai-service` para transcrever o áudio (STT), segmentar trechos com timestamp e gerar embeddings armazenados no PostgreSQL 16 + `pgvector` (database `ai`, ADR-0017).
- **Fluxo de consulta (UC001, RNF003):** o Aluno matriculado envia dúvida na página da aula; o `ai-service` faz busca vetorial restrita ao `course_id`, monta o prompt com os trechos relevantes e envia a pergunta + contexto ao provedor externo de LLM em streaming SSE. O histórico é persistido em `conversations` e `messages` no database `core`.
- **Dados envolvidos:** texto livre do Aluno (que pode conter PII ou dados sensíveis digitados espontaneamente), transcrição da fala do Instrutor, identificador interno de curso/aula. Dados cadastrais diretos (`name`, `email`, `document_number`, `phone`) **não** são anexados ao prompt pela API.

### 2.2 Crianças e adolescentes
- **Pontos de entrada:** cadastro (`UC012`, `users.birth_date` atualmente opcional), edição de perfil (`UC013`), consumo de aulas e avaliações (`UC009`, `UC010`) e interação conversacional com o Tutor de IA (`UC001`).
- **Exigência legal:** melhor interesse do menor prevalecente (Enunciado CD/ANPD nº 1/2023); consentimento específico e verificável de pelo menos um dos pais ou responsável legal para crianças (< 12 anos, LGPD art. 14, §§ 1º e 5º); linguagem simples, clara e acessível (§ 6º).

---

## 3. Avaliação de riscos e medidas de mitigação

### 3.1 Riscos do Tutor de IA

| ID | Risco identificado | Probabilidade | Impacto | Medidas técnicas e administrativas de mitigação | Risco residual |
|---|---|---|---|---|---|
| **R-IA-01** | **Exposição incidental de PII ou dados sensíveis no prompt:** Aluno digita nome, CPF, condição de saúde ou dados de terceiros na pergunta ao Tutor, que trafega ao provedor externo de LLM | Média | Alto | 1) API não envia campos cadastrais ao LLM; 2) aviso visível na caixa de chat orientando a não inserir dados pessoais; 3) filtro/mascaramento automático de padrões de PII (CPF, e-mail, telefone) antes do envio ao LLM; 4) DPA com cláusula *zero-training* e retenção zero no provedor (RNF023) | Baixo |
| **R-IA-02** | **Transferência internacional sem garantia adequada:** provedor de LLM ou STT processa dados fora do Brasil sem mecanismo válido do art. 33 | Alta (sem DPA) | Alto | Adotar Cláusulas-Padrão Contratuais da Resolução CD/ANPD nº 19/2024 no contrato com provedores de LLM e STT e divulgar na Política de Privacidade ([ROPA seção 3](ropa.md)) | Baixo |
| **R-IA-03** | **Vazamento de conteúdo entre cursos ou acesso indevido:** resposta do Tutor mistura material de outro curso ou responde a Aluno não matriculado | Baixa | Médio | Isolamento obrigatório por `course_id` na consulta vetorial (`where('course_id', $courseId)`), validação de JWT e matrícula ativa antes de consultar o `ai-service`, database `ai` separado do `core` (ADR-0017) | Baixo |
| **R-IA-04** | **Retenção indevida de histórico e voz/transcrições após exclusão:** PII em `messages.content` ou transcrições do Instrutor permanecem após pedido de eliminação | Média | Médio | Estender rotina de anonimização (`UC018`) para descaracterizar/expurgar PII em `messages.content` e remover transcrições/embeddings quando cursos do Instrutor forem excluídos em cascata | Baixo |
| **R-IA-05** | **Alucinação ou resposta inadequada:** Tutor gera conteúdo fora do escopo da aula ou inadequado ao estudante | Média | Médio | RAG restrito ao material do curso, citação obrigatória de aula e timestamp, fallback explícito quando não houver correspondência no material (UC001 A-1) e moderação de conteúdo no provedor de LLM | Baixo |

### 3.2 Riscos relacionados a crianças e adolescentes

| ID | Risco identificado | Probabilidade | Impacto | Medidas técnicas e administrativas de mitigação | Risco residual |
|---|---|---|---|---|---|
| **R-MEN-01** | **Cadastro de criança (< 12 anos) sem consentimento verificável de responsável:** `birth_date` hoje não bloqueia menores no UC012 | Alta (no desenho atual) | Alto | **Decisão pendente para o grupo:** (a) restringir a plataforma a maiores de 18 anos ou adolescentes (≥ 12 anos) com verificação etária no UC012, bloqueando < 12 anos; ou (b) implementar fluxo verificável de consentimento parental (art. 14, §§ 1º e 5º) antes de ativar a conta | Baixo (após decisão e implementação) |
| **R-MEN-02** | **Interação de menores com IA generativa sem salvaguardas:** menor compartilha dados pessoais no chat ou recebe resposta imprópria | Média | Alto | Restrição estrita do Tutor ao escopo didático da aula (RAG fechado), filtros de segurança/moderação de conteúdo, aviso em linguagem simples e acessível (art. 14, § 6º) e vedação de perfilamento comportamental ou publicidade | Baixo |
| **R-MEN-03** | **Coleta excessiva de dados de menores:** solicitação de CPF e endereço sem necessidade operacional | Média | Médio | Aplicar princípio da necessidade (art. 6º, III): tornar CPF e endereço dispensáveis para contas de Aluno (especialmente menores) e documentar justificativa estrita no [ROPA](ropa.md) | Baixo |
| **R-MEN-04** | **Incidente de segurança envolvendo dados de menores:** critério expresso de risco relevante na Resolução CD/ANPD nº 15/2024 | Baixa | Alto | Criptografia em trânsito (TLS) e em repouso, cookies `HttpOnly`/`Secure`/`SameSite`, plano de resposta a incidentes com comunicação à ANPD e titulares em até **3 dias úteis** (Res. 15/2024) | Baixo |

---

## 4. Pontos em aberto para aprovação do grupo

1. **Política etária oficial (R-MEN-01):** definir se a Plataforma de Cursos na v1 será destinada apenas a maiores de 18 anos, a partir de 12 anos (adolescentes com salvaguardas), ou aberta a crianças com verificação de consentimento parental.
2. **Seleção de fornecedores de LLM e STT:** confirmar provedores que ofereçam DPA compatível com a Resolução CD/ANPD nº 19/2024 e garantia contratual *zero-training*.
3. **Aprovação formal:** revisão e assinatura pelo Encarregado pelo Tratamento de Dados Pessoais ([encarregado-e-canais.md](encarregado-e-canais.md)) antes do lançamento em produção.

---

## Ligações

- **Pesquisa legal:** [pesquisa/lgpd.md](../../pesquisa/lgpd.md) · [pesquisa/fontes.md](../../pesquisa/fontes.md)
- **Demais artefatos LGPD:** [ROPA](ropa.md) · [Encarregado e canais públicos](encarregado-e-canais.md)
- **Arquitetura e requisitos:** [SDD](../sdd.md) · [TDD](../tdd.md) · [Item 8 — RNFs](../../especificacao/08-requisitos-nao-funcionais/00-item.md) · [ADR-0005](../adr/0005-tutor-de-ia-como-ator-sistemico.md) · [ADR-0014](../adr/0014-exclusao-logica-e-anonimizacao.md)

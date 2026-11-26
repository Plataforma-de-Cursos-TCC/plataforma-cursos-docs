---
id: backlog-tcc
titulo: "Backlog de Evolução para o TCC — Plataforma de Cursos"
tipo: documento-projeto
status: rascunho
atualizado: 2026-11-25
relacionados: [prd, sdd, tdd, pesquisa-lgpd]
---
# Backlog de Evolução para o TCC — Plataforma de Cursos

> **Escopo:** registro de propostas de evolução, validação empírica e aprofundamento pedagógico/técnico para as etapas de **TCC 1 e TCC 2**. Este documento **não altera** o escopo nem os artefatos congelados da entrega de 28/11 (RA2).

---

## 1. Público piloto

- **Objetivo:** definir e recrutar um grupo controlado de usuários reais (Instrutores e Alunos) para validar o fluxo completo de autoria, consumo de aulas, quizzes e interação com o Tutor de IA em ambiente de teste/piloto.
- **Critérios sugeridos:**
  - 2 a 3 Instrutores produzindo cursos curtos (1 a 2 módulos com aulas em vídeo e quiz com gabarito);
  - 15 a 30 Alunos voluntários (preferencialmente maiores de 18 anos no piloto inicial, simplificando a conformidade com o art. 14 da LGPD);
  - Termo de consentimento informado para coleta de métricas de uso e feedback qualitativo.
- **Entregável no TCC:** relatório de perfil do piloto, taxa de conclusão observada e principais pontos de atrito na usabilidade.

## 2. Protocolo de avaliação do Tutor de IA

- **Objetivo:** estabelecer um conjunto reprodutível de testes e métricas para medir a qualidade, fidelidade ao material da aula e segurança das respostas do Tutor de IA (`ai-service`).
- **Eixos de avaliação:**
  - **Fidelidade ao contexto (grounding):** percentual de respostas suportadas exclusivamente pelos trechos recuperados do curso e com citação correta de aula e timestamp;
  - **Taxa de recusa adequada:** comportamento diante de perguntas fora do escopo do curso (fluxo alternativo A-1 do UC001), sem inventar conteúdo;
  - **Taxa de alucinação:** medição em um banco curado de perguntas-teste (gold set) avaliado por revisores humanos e/ou juiz automatizado;
  - **Desempenho:** validação do p95 de tempo até o primeiro token (meta de até 3 s do RNF003).
- **Entregável no TCC:** dataset de avaliação, script automatizado de benchmark e tabela comparativa de resultados antes e depois de ajustes de prompt/chunking.

## 3. Postura socrática do Tutor de IA

- **Objetivo:** refinar o *system prompt* e os fluxos de diálogo do `CourseTutorAgent` para priorizar mediação pedagógica (postura socrática) em vez de entregar respostas prontas ou resolver diretamente questões de quiz.
- **Diretrizes propostas:**
  - Fazer perguntas orientadoras curtas e apontar o trecho exato da aula (`[Aula X, mm:ss]`) para o Aluno reconstruir o raciocínio;
  - Evitar entrega direta do gabarito de quizzes quando a pergunta reproduzir enunciados de avaliação do módulo;
  - Permitir ajuste gradual de profundidade (dica inicial -> explicação guiada -> resumo com referência) preservando linguagem clara e acessível.
- **Entregável no TCC:** versão versionada do *system prompt*, casos de teste de postura socrática e análise qualitativa com Alunos do piloto.

## 4. Ciclo de melhoria contínua de aula (feedback loop para o Instrutor)

- **Objetivo:** transformar as interações agregadas e anonimizadas dos Alunos com o Tutor de IA e o desempenho em quizzes em insumos acionáveis no dashboard do Instrutor (Área D).
- **Diretrizes propostas:**
  - Agrupar dúvidas recorrentes por aula e por intervalo de tempo do vídeo (*hotspots* de confusão), sempre sem expor identidade individual do Aluno;
  - Cruzar aulas com maior volume de dúvidas com questões de quiz de menor taxa de acerto;
  - Oferecer recomendações práticas ao Instrutor (ex.: gravar esclarecimento complementar, anexar material de apoio ou revisar enunciado de questão).
- **Entregável no TCC:** especificação do agregador de tópicos de dúvida (preservando privacidade) e validação de utilidade com os Instrutores do piloto.

## 5. Demonstração antecipada (marco intermediário)

- **Objetivo:** planejar uma demonstração funcional antecipada (fatia vertical ponta a ponta) antes da entrega final do TCC, reduzindo risco de integração entre Front-end (Next.js), API Core (Laravel 13), `media-service` (Cloudflare R2) e `ai-service` (`pgvector` + LLM).
- **Escopo mínimo da demonstração antecipada:**
  - Upload de 1 aula em vídeo pelo Instrutor -> transcrição e indexação assíncrona via RabbitMQ -> reprodução por URL assinada pelo Aluno -> 1 interação completa com o Tutor de IA em streaming SSE citando aula e timestamp;
  - Evidência gravada (vídeo curto ou roteiro reproduzível) e checklist de latência e estabilidade.
- **Entregável no TCC:** data-marco definida no cronograma do TCC 1/TCC 2, checklist de prontidão e ata de feedback do orientador.

---

## Ligações

- **Documentos de projeto:** [PRD](prd.md) · [SDD](sdd.md) · [TDD](tdd.md)
- **Conformidade LGPD:** [ROPA](lgpd/ropa.md) · [RIPD](lgpd/ripd.md) · [Encarregado e canais](lgpd/encarregado-e-canais.md)
- **Rubricas do TCC:** [TCC 1](../entregas/rubricas-tcc-1.md) · [TCC 2](../entregas/rubricas-tcc-2.md)

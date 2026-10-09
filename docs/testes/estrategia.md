---
id: testes-estrategia
titulo: "Estratégia de testes"
tipo: documento-projeto
status: rascunho
atualizado: 2026-10-08
---
# Estratégia de testes

A estratégia de testes da Plataforma de Cursos estabelece diretrizes formais de qualidade e verificação contínua, alinhadas aos requisitos não-funcionais do sistema (em especial RNF006 e RNF021 para cobertura mínima de 75% no backend e no frontend), às decisões arquiteturais ([ADR-0007](../adr/0007-stack-e-bancos.md), [ADR-0005](../adr/0005-tutor-de-ia-como-ator-sistemico.md)) e ao ciclo de integração contínua ([CI do repositório de código](../ci-repo-codigo.md)).

## 1. Pirâmide de testes

A suíte de testes é distribuída em três níveis complementares, equilibrando velocidade de execução, isolamento e confiabilidade:

```
        / \
       /   \
      / E2E \        Playwright (Fluxos críticos do usuário)
     /-------\
    /         \
   / Integração\     Pest (Feature Tests / API) & Vitest (Componentes)
  /-------------\
 /               \
/     Unidade     \  Pest (Domain / Value Objects / Rules) & Vitest (Hooks / Utils)
-------------------
```

- **Testes de Unidade (Base):**
  - **Foco:** Validam regras de negócio puras, algoritmos de cálculo (cálculo de notas de quiz, progresso percentual de aulas), validações de campos e políticas de senha, DTOs, objetos de valor e métodos utilitários sem tocar em banco de dados, rede ou serviços externos.
  - **Execução:** Extremamente rápida em memória, servindo como primeira linha de feedback durante o desenvolvimento.
- **Testes de Integração (Camada Média):**
  - **Backend (Feature Tests com Pest):** Testam requisições HTTP completas contra os endpoints REST da API, fluxos de autenticação JWT, controle de acesso por perfil (`assertOwnership`, middleware de RBAC), transações com o banco de dados (MySQL em container efêmero no CI), despacho de eventos e jobs assíncronos no RabbitMQ (utilizando fakes de fila).
  - **Frontend (Vitest + Testing Library):** Validam a interação dos componentes React/Next.js, renderização condicional por estado, validações de formulário cliente e consumo mockado de endpoints da API via handlers simulados (MSW).
- **Testes Ponta a Ponta / E2E (Topo):**
  - **Foco:** Simulam jornadas completas do usuário em navegadores reais (Chromium, Firefox, WebKit) via Playwright, validando a integração entre interface SPA e API.
  - **Fluxos E2E Principais (mapeados nos Casos de Uso):**
    1. **Jornada de Acesso e Conta:** Cadastro de usuário com aceite de termos (`UC012`) seguido por autenticação (`UC005`) e redirecionamento conforme perfil (`UC016`).
    2. **Jornada de Matrícula:** Aluno autenticado consulta catálogo (`UC020`), acessa página do curso e realiza matrícula com pagamento simulado (`UC003`, `UC019`).
    3. **Jornada de Aprendizagem:** Aluno matriculado assiste à videoaula com player de vídeo (`UC009`), interage com o chat lateral do Tutor de IA (`UC001`), conclui a aula e tem o progresso persistido.
    4. **Jornada de Avaliação:** Aluno responde a quiz com gabarito automático (`UC002`) e submete avaliação do curso (`UC010`).
    5. **Jornada de Autoria do Instrutor:** Instrutor cria curso (`UC006`), módulos (`UC014`), aulas com simulação de upload de vídeo (`UC015`) e quiz com gabarito (`UC004`).
    6. **Jornada de Administração:** Administrador filtra e gerencia status de usuários (`UC008`, `UC018`) e consulta métricas no dashboard (`UC007`).

## 2. Desenvolvimento Guiado por Testes (TDD)

A equipe adota o ciclo clássico de **TDD (Red → Green → Refactor)** como metodologia padrão de implementação de regras de negócio:

1. **Red (Vermelho):** A partir dos critérios de aceite de cada User Story (especificados no padrão BDD *Dado que / Quando / Então* em `especificacao/07-estorias-de-usuario/`), escreve-se inicialmente o teste automatizado (Feature Test no Pest ou teste de componente no Vitest) descrevendo o comportamento esperado. O teste deve falhar antes de qualquer código de produção ser escrito.
2. **Green (Verde):** Implementa-se a quantidade mínima estritamente necessária de código para fazer o teste passar com sucesso.
3. **Refactor (Refatoração):** Limpa-se o código, eliminando duplicações, aplicando padrões de projeto adequados (Repositories, Services, Form Requests) e mantendo a cobertura verde.

### Quando aplicar TDD rigorosamente:
- Em **100% das regras de negócio**, transações financeiras simuladas (pagamento, regras de unicidade de matrícula), cálculo de notas de quiz, geração e validação de tokens JWT, e validações de ownership de recursos (`assertOwnership`).
- Em cenários negativos e de exceção mapeados nas especificações de caso de uso (ex.: tentativa de matrícula em curso em rascunho, e-mail duplicado, alteração de senha incorreta).

### Abordagem para CRUD boilerplate:
- Para endpoints puramente CRUD de recursos simples, aplicam-se testes de integração de caminho feliz e validação de schema em lote, garantindo que controllers e rotas mantenham a cobertura sem onerar a velocidade de entrega inicial.

## 3. Cobertura de testes

- **Meta e Limite Mínimo:** Conforme definido no **RNF006**, a cobertura de código mínima obrigatória é de **75%** nas linhas do backend. O **RNF021** fixa a mesma meta de **75%** para o frontend (Vitest).
- **Portão de Qualidade no CI:** O pipeline de Integração Contínua ([CI do repositório de código](../ci-repo-codigo.md)) executa a verificação em cada Pull Request via:
  ```bash
  php artisan test --coverage --min=75
  ```
  No frontend, o equivalente é `vitest run --coverage` com `thresholds` de 75% em linhas (provider `v8`).
  Caso a cobertura caia abaixo do limiar de 75%, o pipeline falha e o Pull Request é automaticamente **bloqueado para merge**.
- **Motor de Cobertura:** No ambiente de CI utiliza-se o driver de alta performance **PCOV** integrado ao PHP 8.3, reduzindo o tempo de execução dos builds.
- **Acompanhamento:** A evolução histórica da cobertura por módulo e release é registrada na planilha de acompanhamento em [cobertura.md](cobertura.md).

## 4. Ferramentas

| Finalidade | Ferramenta | Ambiente | Justificativa técnica |
|---|---|---|---|
| **Testes de Backend (Unit e Feature)** | **Pest PHP** (v2.x / v3.x) | PHP 8.3 / Laravel 13 | Sintaxe declarativa e fluente, facilidade de organização de datasets e suporte nativo ao ecossistema Laravel. |
| **Driver de Cobertura de Código** | **PCOV** | PHP / CI | Muito mais rápido que Xdebug para geração de métricas de code coverage no pipeline do GitHub Actions. |
| **Testes de Frontend (Unit e Componentes)** | **Vitest** + **React Testing Library** | Node.js LTS / Next.js | Execução ultrarrápida com suporte nativo a ESM e TypeScript, compatível com o ecossistema de componentes shadcn/ui e Tailwind. |
| **Mock de APIs no Frontend** | **Mock Service Worker (MSW)** | Frontend / Testes | Intercepta requisições HTTP na camada de rede nos testes Vitest, permitindo simular contratos REST reais sem subir a API completa. |
| **Testes Ponta a Ponta (E2E)** | **Playwright** | Chromium, Firefox, WebKit | Testes multiplataforma com gravação de traces, screenshots de falhas, suporte a fluxos assíncronos e simulação de responsividade móvel (RNF019). |
| **Banco Efêmero de Testes** | **MySQL 8** (Service Container) | GitHub Actions CI | Garante fidelidade de tipos e restrições de integridade idênticas ao ambiente de produção. |
| **Banco Vetorial Efêmero** | **PostgreSQL 16 + pgvector** (Service Container) | GitHub Actions CI | Valida as consultas com `whereVectorSimilarTo()` do `ai-service` sem depender de banco SQLite incompatível com vetores. |

## 5. Testes do Tutor de IA (`ai-service`)

O Tutor de IA introduz desafios específicos de teste devido à natureza probabilística dos modelos de linguagem grandes (LLMs) e ao pipeline RAG. Para garantir testes determinísticos, repetíveis e de baixo custo, aplicam-se as seguintes regras:

### 5.1. Provedor Mockado / Fake (Sem chamadas reais no CI)
- **Zero chamadas externas no pipeline:** Em nenhuma hipótese o pipeline de CI executa chamadas pagas ou externas à API de LLM (OpenAI, Anthropic ou provedores compatíveis).
- **Driver Fake / Stubs:** Utiliza-se o mecanismo de fake do Laravel AI SDK (ou stubs do cliente HTTP) para simular a resposta do modelo:
  - Para geração de embeddings: retorna vetores estáticos pré-calculados na dimensão do modelo de embeddings configurado, baseados em hash determinístico do texto de entrada.
  - Para chat em streaming: simula chunks de Server-Sent Events (SSE) emitindo tokens incrementais e payload estruturado contendo a citação formal de aula e timestamp.

### 5.2. Isolamento Obrigatório por Curso (`course_id`)
- **Teste Crítico de Segurança e Escopo:** Conforme a [ADR-0005](../adr/0005-tutor-de-ia-como-ator-sistemico.md) e as regras do `UC001`, o Tutor de IA **nunca** pode vazar trechos de outros cursos.
- **Cenário de Teste Obrigatório:**
  - Cria-se um banco de testes com chunks de transcrição indexados para o Curso A e chunks indexados para o Curso B.
  - Submete-se uma pergunta no contexto do Curso A cujo termo semântico coincida fortemente com um conteúdo do Curso B.
  - O teste assere que a query de similaridade vetorial contém estritamente o filtro `WHERE course_id = ?` e que nenhum trecho do Curso B é retornado ou utilizado no prompt final.

### 5.3. Fluxo de Indisponibilidade e Tratamento de Falhas (Fallback)
- **Simulação de Falha de Rede ou Timeout do Provedor:** <!-- proposta: fluxo não especificado no UC001 -->
  - O provedor mockado é configurado para lançar exceção de timeout ou erro HTTP 503.
  - O teste valida que o `ai-service` captura o erro graciosa e rapidamente, não trava o streaming do aluno e retorna resposta de erro amigável sem expor detalhes internos da infraestrutura.
- **Aulas sem Embeddings Prontos (Fluxo E-1 do UC001):**
  - Teste automatizado para o fluxo de exceção `E-1`: quando o aluno pergunta sobre uma aula cuja transcrição e indexação ainda não foram concluídas, o sistema avisa que o conteúdo ainda está sendo preparado e sugere tentar novamente mais tarde, sem disparar chamadas ao LLM.
- **Limite de Mensagens Atingido (Fluxo E-2 do UC001):**
  - Teste automatizado para o fluxo de exceção `E-2`: ao identificar que o aluno excedeu o limite de mensagens do período, o sistema bloqueia o novo envio e a resposta informa o tempo de espera restante.

### 5.4. Conjunto de Perguntas de Referência (Golden Dataset)
- Para testes de avaliação de qualidade semântica (executados manualmente em ambiente de homologação, fora do gatilho de PR):
  - Mantém-se uma suíte de 20 perguntas de referência com gabarito de citação esperada (aula e intervalo de minutos).
  - Avalia-se a métrica de acurácia de recuperação (Recall@K) para assegurar que os trechos relevantes continuem no topo do ranking ao ajustar parâmetros de chunking ou embeddings.

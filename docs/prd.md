---
id: prd
titulo: "PRD — Plataforma de Cursos"
tipo: documento-projeto
status: rascunho
atualizado: 2026-10-07
---

# PRD — Plataforma de Cursos

## 1. Problema
A plataforma de cursos enfrenta três lacunas principais no mercado:

1. **Fragmentação do Tutor de IA** – concorrentes oferecem chats genéricos ou tutores não contextualizados ao conteúdo da aula. ([lacunas-e-diferencial](../pesquisa/similares/lacunas-e-diferencial.md))
2. **Dependência de curadoria fechada** – soluções como Khan Academy ou Coursera limitam a autoria aberta e a tutoria contextualizada. ([lacunas-e-diferencial](../pesquisa/similares/lacunas-e-diferencial.md))
3. **Complexidade de monetização e dashboards** – plataformas comerciais restringem análises para instrutores independentes. ([lacunas-e-diferencial](../pesquisa/similares/lacunas-e-diferencial.md))
<!-- proposta: estes apontamentos foram extrapolados do resumo de lacunas‑e‑diferencial; não há fonte direta na especificação -->

Essas lacunas justificam a necessidade de um produto que ofereça tutor de IA intrinsecamente contextualizado, autoria livre e dashboards acessíveis.
<!-- proposta: conclusão baseada na análise de mercado, sem referência literal na especificação -->

## 2. Personas
| Persona | Objetivo | Contexto | Frustração |
|---|---|---|---|
| **Visitante** | Explorar o catálogo e decidir criar conta. | Usuário sem conta, navega conteúdo público. | Falta de informação clara sobre cursos antes de cadastro. |
| **Aluno** | Consumir aulas, resolver dúvidas rapidamente, acompanhar progresso. | Usuário matriculado, assiste aulas, interage com tutor de IA. | Dúvidas não respondidas no momento da aula, ausência de métricas de desempenho. |
| **Instrutor** | Criar e gerir cursos, acompanhar engajamento dos alunos. | Produz conteúdo, configura módulos, quizzes e visualiza dashboard. | Dashboard fechado ou limitado, necessidade de validação manual de avaliações. |
| **Administrador** | Gerenciar usuários e perfis, garantir operação da plataforma. | Supervisiona contas, acessa métricas globais. | Falta de visibilidade consolidada das atividades e auditoria. |
| **Tutor de IA** (ator sistêmico) | Responder dúvidas contextualizadas ao conteúdo da aula. | Sistema que recebe pergunta do aluno e consulta embeddings da aula. | Respostas genéricas ou alucinações fora do escopo do curso. |
*(Os detalhes das descrições foram extraídos do item 5, [Relação de Atores / Usuários](../especificacao/05-atores-usuarios.md).)*
<!-- proposta: as frustrações foram extraídas da tabela de atores do item 5, porém não têm fonte literal; marcamos como proposta -->

## 3. Objetivos e métricas
| Objetivo | Métrica | Meta | Prazo |
|---|---|---|---|
| **Aumentar taxa de conclusão** | % de cursos concluídos por aluno | ≥ 60% | 6 meses |
| **Reduzir abandono por falta de suporte** | Redução de dúvidas manuais ao Tutor de IA | ≥ 30% | 6 meses |
| **Capacitar instrutores com dashboards** | % de instrutores com curso publicado que consultam o dashboard ao menos uma vez por mês | ≥ 70% | 6 meses |
| **Escalar número de cursos publicados** | Cursos publicados com status “publicado” | ≥ 10 | 6 meses |
Objetivos baseados no item 1, [3 Objetivos](../especificacao/01-3-objetivos.md). As metas de 60% em 6 meses e de 70% dos instrutores consultando o dashboard mensalmente constam no item 1; a redução de 30% das dúvidas consta no item 3, [Visão do produto](../especificacao/03-visao-do-produto.md). A meta de 10 cursos publicados também consta no item 1, como 10 instrutores com curso publicado. <!-- proposta: metas sem fonte literal foram adicionadas como suposições -->

## 4. Escopo
### 4.1 Dentro (MVP)
- Sistema web SaaS para criação, consumo e gestão de cursos online.
- Autoria completa por Instrutores (cursos, módulos, aulas, quizzes com gabarito).
- Tutor de IA que responde exclusivamente a dúvidas sobre a aula atual.
- Dashboard de métricas para Instrutores e Administradores (progresso, engajamento, notas).
- Matrícula simulada (sem gateway de pagamento real).

### 4.2 Fora
- Marketplace de pagamento real, emissão de certificados com validade legal.
- Aplicativo móvel nativo.
- Integração com redes sociais ou gamificação avançada.
- Curadoria externa de conteúdo.
Escopo alinhado ao item 2, [É – Não é – Faz – Não faz](../especificacao/02-e-nao-e-faz-nao-faz.md).

## 5. Requisitos em alto nível
*Organizado por áreas A‑D conforme ADR‑0006.*

- **Área A – Acesso e conta**: Registro, login, recuperação de senha, perfis. ([item 6](../especificacao/06-requisitos-funcionais/00-item.md); detalhamento nos arquivos `area-a.md` do item 7, [estórias](../especificacao/07-estorias-de-usuario/area-a.md), e do item 10, [casos de uso](../especificacao/10-especificacoes-de-caso-de-uso/area-a.md))
  - IDs: RF001, RF013, RF017
- **Área B – Autoria do instrutor**: Criação de cursos, módulos, aulas, quizzes e gabaritos. ([item 6](../especificacao/06-requisitos-funcionais/00-item.md); detalhamento nos arquivos `area-b.md` do item 7, [estórias](../especificacao/07-estorias-de-usuario/area-b.md), e do item 10, [casos de uso](../especificacao/10-especificacoes-de-caso-de-uso/area-b.md))
  - IDs: RF002, RF003, RF004, RF007, RF016
- **Área C – Aprendizagem do aluno**: Matrícula, visualização de aulas, quizzes, avaliação, interação com Tutor de IA. ([item 6](../especificacao/06-requisitos-funcionais/00-item.md); detalhamento nos arquivos `area-c.md` do item 7, [estórias](../especificacao/07-estorias-de-usuario/area-c.md), e do item 10, [casos de uso](../especificacao/10-especificacoes-de-caso-de-uso/area-c.md))
  - IDs: RF005, RF006, RF008, RF011, RF014, RF015
- **Área D – Tutor de IA & Analytics**: Consulta de embeddings, respostas contextualizadas, dashboard de analytics. ([item 6](../especificacao/06-requisitos-funcionais/00-item.md); detalhamento nos arquivos `area-d.md` do item 7, [estórias](../especificacao/07-estorias-de-usuario/area-d.md), e do item 10, [casos de uso](../especificacao/10-especificacoes-de-caso-de-uso/area-d.md))
  - IDs: RF009, RF010, RF012, RF018

## 6. Concorrentes e diferencial
A matriz comparativa mostra que nenhum concorrente oferece simultaneamente:
- Tutor de IA contextualizado ao conteúdo da aula.
- Autoria totalmente aberta para instrutores independentes.
- Dashboard de métricas acessível a instrutores individuais.

Esse conjunto de diferenciais está descrito em lacunas‑e‑diferencial:
- **DF1. Tutor de IA intrinsecamente contextualizado à aula** – O Tutor de IA atua como ator sistêmico ([ADR‑0005]) e responde somente ao conteúdo da aula. *(lacunas‑e‑diferencial, linha 35)*
- **DF2. Democratização da autoria com quizzes e gabaritos objetivos** – Instrutores podem criar cursos, módulos, aulas e quizzes com gabarito automático. *(lacunas‑e‑diferencial, linha 36)*
- **DF3. Analytics acessível e direto ao Instrutor** – Dashboard com indicadores e filtros para o Instrutor acompanhar progresso e engajamento. *(lacunas‑e‑diferencial, line 37)*
- **DF4. Separação clara de papéis e governança do produto** – Quatro perfis humanos + ator sistêmico, com regras de acesso rigorosas. *(lacunas‑e‑diferencial, line 38)*

## 7. Riscos e premissas
- **Custo do modelo de linguagem** para o Tutor de IA pode exceder orçamento. <!-- proposta: risco de custo identificado, mas sem fonte literal na especificação -->
- **Direitos autorais** sobre vídeos devem ser garantidos pelos instrutores. <!-- proposta: risco de direitos autorais, baseada na prática de produção de conteúdo -->
- **Conformidade LGPD** para armazenamento de dados pessoais.
- **Disponibilidade** da infraestrutura (SLA ≥ 99%).
---

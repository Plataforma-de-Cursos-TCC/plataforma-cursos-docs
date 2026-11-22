# Relatório do RA2: Áreas A a D integradas (itens 12 a 15)

Atualizado em 2026-11-22. As quatro áreas entraram na `main` pelo PR #141 (merge `d6f4e56`, com bypass de admin), em 123 commits. Cada commit mantém o autor da sua área. Este arquivo não está commitado.

## Como foi feito

- [x] Um worker do Orca por área, cada um num worktree próprio, na ordem 12, 13, 14 e 15.
- [x] Duas revisões cruzadas (#135), só leitura: 9 bloqueios na 1ª e 8 na 2ª, todos resolvidos.
- [x] Decisões entre áreas registradas nos ADRs 0014 a 0018: exclusão lógica, snake_case no banco e camelCase na API, retenção da auditoria, PostgreSQL 16 e monólito modular, com leitura entre módulos só por Services ou Repositories.
- [x] Conferência visual dos 41 PNGs por quatro modelos do agy (Flash, Hydrogen, Argon e Neon) e revisão final do coordenador. Os defeitos reais foram corrigidos nas áreas B, C e D.
- [x] A branch `docs/tasks-lucas-bruno` foi comparada com a Área C. O que valia entrou na nossa versão, com os IDs e as decisões do grupo; a branch foi apagada.
- [x] Integração por cherry-pick na ordem A, B, C e D. Os conflitos nos arquivos compartilhados (`docs/tdd.md`, `docs/testes/cobertura.md`, itens 6 e 8, `CHANGELOG.md` e `scripts/drawio-seqgen`) foram resolvidos à mão.
- [x] `CHANGELOG.md` consolidado em uma linha por área, com o #141.

## Decisões entre áreas

| Ponto | Decisão |
|---|---|
| Exclusão bloqueada por matrícula ou histórico (UC006, UC014 e UC015) | 409 `CONFLICT` |
| JWT inválido ou adulterado | 401 `UNAUTHENTICATED` |
| Validação do token e do perfil | `JwtGuard.parseToken` e `JwtGuard.authorize`, declarados na Área A |
| Dono de `Quiz.status`, `Quiz.allowRetake` e `Lesson.indexStatus` | Área B (`allowRetake` resolve a permissão de refazer o quiz) |
| `Payment` | `Enrollment` 1 para 0..* `Payment`; `userId` mantido, porque a compra de créditos do Tutor de IA não tem matrícula |
| Nota do quiz (UC002 R-2) | Acertos sobre o total vezes 100, de 0,00 a 100,00, com 2 casas e arredondamento meio para cima |
| Dashboard do Instrutor (UC007) | A Área D chama `LearningMetricsService.aggregateProgressAndEnrollments` da Área C, sem ler as tabelas dela (ADR-0018) |
| Enums gravados no banco | Em inglês, com o rótulo em pt-BR no item 12 |
| Exceções | Não viram classe no item 13; aparecem na sequência como resposta com o código do TDD |
| Ícones do item 14 | Controller, Request, Resource e View como `boundary`; Service como `control`; Repository como `entity`; interface de infraestrutura como `boundary` com `<<interface>>` |

## Entregas por área

### Área A (Lucas Stopinski)
- [x] Ajustes de integração: `JwtGuard` com `parseToken` e `authorize`; `UserRepository` com paginação; tabelas em snake_case com `deleted_at`.
- [x] UC005 via `RefreshSessionRepository` e UC012 com `createEmpty`; PNGs de sequência reexportados em escala 1.5.
- [x] `scripts/drawio-seqgen` com uma versão só nas quatro áreas: ícone pelo papel e sufixo "(Área X)" ignorado.

### Área B (Adrian)
- [x] Item 12: PostgreSQL, snake_case, exclusão lógica, `position` e materiais da aula (#92).
- [x] Item 13: classes negocial e de implementação, com cor por papel e legenda (#97).
- [x] Item 14: UC004, UC006 (partes 1 e 2), UC014 e UC015, com cancelamento, arquivamento e repositórios como `entity` (#102).
- [x] Item 15: TC091 a TC118, com exclusão lógica e 503 (#107).
- [x] Itens 6, 7 e 10: RF004 e US006 com material complementar; cancelamento em UC004, UC006, UC014 e UC015.

### Área C (Lucas Bruno)
- [x] Item 12: matrícula, pagamento 0..*, progresso, tentativa de quiz com `draft` e `submitted`, e avaliação (#93).
- [x] Item 13: negocial com legenda; implementação com `LearningMetricsService`, `LearningActivityDTO`, `GroupBy` e os métodos de agregação nos repositórios (#98).
- [x] Item 14: UC002, UC003, UC009, UC010, UC019 e UC020; o UC002 desfaz o envio quando o gabarito está incompleto (#103).
- [x] Item 15: TC151 a TC197, com cálculo da nota, concorrência, nova tentativa de pagamento e paginação (#108).
- [x] TDD com `Enrollment` 1 para 0..* `Payment`.

### Área D (Vinicius Teider)
- [x] Item 12: conversas, mensagens, créditos extras do Tutor de IA e auditoria particionada, com as multiplicidades junto às setas (#94).
- [x] Item 13: administração, Tutor de IA e analytics, com a dependência da Área C (#99).
- [x] Item 14: UC001, UC007 (via Área C), UC008, UC016 e UC018 (#104).
- [x] Item 15: TC211 a TC272 (#109).
- [x] Pendências cruzadas #122 e #123; RF020, US022 e RNF022 (créditos extras); RNF016 com o arquivamento da auditoria.

## Verificação final

- [x] Todo `.drawio` em `especificacao/diagramas/` tem `.png`.
- [x] Nenhum PNG de sequência cortado.
- [x] Nenhum ID de caso de teste repetido entre as áreas.
- [x] Todos os links Markdown relativos resolvem.
- [x] CI do #141 verde (`changelog`, `checks`, `conventions` e `issue-link`).

## Fechamento e limpeza

- [x] PR #141 mergeado; `main` local atualizada.
- [x] Issues #93, #94, #104, #122 e #123 fechadas pelo #141.
- [ ] Issues #92, #97, #98, #99, #102, #103, #107, #108 e #109: a issue-flow reabriu as nove depois do merge. Estão sendo fechadas pelos PRs #142 a #150, um por issue.
- [x] Worktrees `area-{a,b,c,d}-ra2`, branches das áreas e backups apagados.
- [x] Branch remota `docs/tasks-lucas-bruno` apagada.
- [x] Não há mais `pendencias-area-*.md` na raiz.

## O que fica para o grupo

- [ ] Revisão cruzada final de todo o projeto (#135).
- [ ] A faixa reservada da Área D ia até TC270, e ela usa TC271 e TC272. Não colide com ninguém, mas vale registrar.
- [ ] Gerar o DOCX e o PDF com o template oficial antes do Canvas (prazo do RA2: 28/11/2026).
- [ ] Tag e release da versão: decisão do grupo no envio ao professor.

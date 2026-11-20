# Relatório do RA2: Áreas B, C e D integradas à Área A (itens 12 a 15)

Data: 2026-11-19. Branch local `ra2-areas-abcd` (a partir da `main`, que já tem a Área A). 47 commits locais. Nada foi pushado, nenhum PR foi aberto e nenhuma issue foi alterada no GitHub. Este arquivo não está commitado.

## Como foi feito

- Um worker do Orca por área, cada um num worktree próprio (`~/orca/workspaces/plataforma-cursos-docs/area-{b,c,d}-ra2`), na ordem 12, 13, 14 e 15, um commit por issue.
- Modelos: primeira entrega em `gemini-3.8-flash` (agy, effort high). A rodada 1 de correção da D também saiu no Gemini. As rodadas 1 da B e da C caíram por autenticação do Gemini e depois por cota do agy (`claude-sonnet-5-5`), então B e C terminaram no Haiku 5.5 do Claude (effort high), assim como a rodada 2 da C e da D.
- Padrão seguido: o da Área A. Item 12 com o dicionário de dados e o `.drawio` relacional; item 13 negocial e de implementação, com o tipo num círculo (`scripts/drawio-seqgen/typeicon.py`); item 14 com um diagrama por UC, gerado por `scripts/drawio-seqgen/seqgen.py`, e `alt` para cancelar; item 15 com um cenário negativo por regra e o estado anterior verificado.
- IDs de casos de teste: o catálogo [docs/testes/casos-de-teste.md](../docs/testes/casos-de-teste.md) já reserva TC001 a TC090 por UC (a Área A faz igual); os novos casos começam em TC091. Faixas reservadas: B TC091-TC150, C TC151-TC210, D TC211-TC270.
- Duas revisões cruzadas (#135), só leitura. A 1ª achou 9 bloqueios e 16 itens a corrigir; a 2ª, já incluindo a Área A, achou 8 bloqueios e 8 itens a corrigir. Depois da 2ª rodada, conferi os 8 bloqueios um por um: todos resolvidos.
- A integração refaz a branch por cherry-pick das três branches das áreas. O `CHANGELOG.md` deu conflito e foi consolidado à mão (cf0600e).

### Decisões entre áreas tomadas na revisão

| Ponto | Decisão |
|---|---|
| Exclusão bloqueada por matrícula ou histórico (UC006, UC014, UC015) | 409 `CONFLICT` (TDD 3.1); o TDD não mudou |
| UC009 E1 | 404 `NOT_FOUND` |
| JWT inválido ou adulterado | 401 `UNAUTHENTICATED` |
| Nomes de classe | B: `InstructorCourseController`, `InstructorLessonController`, `InstructorQuizController`, `QuizAuthoringService`. C: `LessonPlayerController`, `QuizAttemptController`, `QuizAttemptService` |
| Dono de `Quiz.status`, `Quiz.allowRetake`, `Lesson.indexStatus` | Área B |
| `Payment` | 1 `Enrollment` para 0..* `Payment` (o pagamento recusado permite tentar de novo) |
| Enums gravados no banco | Em inglês, com o rótulo em pt-BR mapeado no item 12 (inclusive na Área A) |
| Exceções | Não viram classe no item 13; aparecem na sequência como resposta com o código do TDD |
| Validação do token e do perfil | `JwtGuard.parseToken` e `JwtGuard.authorize`, declarados na Área A |

## Área A (Lucas Stopinski): ajuste de integração

| O quê | Onde | Commit |
|---|---|---|
| `JwtGuard` ganha `parseToken(token)` e `authorize(user, role)`, usados pela D no UC016 | [13-classes-area-a-implementacao-login.drawio](../especificacao/diagramas/13-classes-area-a-implementacao-login.drawio) e `.png`, [13/area-a.md](../especificacao/13-diagrama-de-classes/area-a.md) | 5daeead |
| `User.status` e `User.theme` com os valores em inglês e o rótulo em pt-BR | [12/area-a.md](../especificacao/12-modelo-de-dados/area-a.md) | 5daeead |

## Área B (Adrian): autoria do instrutor

| Issue | O que foi implementado | Arquivos | Commits |
|---|---|---|---|
| #92 item 12 | Category, Course, Module, Lesson, Quiz, Question, QuestionOption; `Quiz.status`, `Quiz.allowRetake`, `Lesson.indexStatus`; bloqueio de exclusão com histórico de alunos (UC014 R-4, UC015 R-5) | [12/area-b.md](../especificacao/12-modelo-de-dados/area-b.md), `12-modelo-de-dados-area-b.drawio/.png` | 72d5a7f, 5e52761 |
| #97 item 13 | Negocial e implementação em três diagramas (cursos e módulos, aulas, quizzes); `Instructor` 1 para 1 `InstructorProfile` (Área A); classes renomeadas | [13/area-b.md](../especificacao/13-diagrama-de-classes/area-b.md), `13-classes-area-b-*.drawio/.png` | d68523d, bbca189 |
| #102 item 14 | UC004, UC006 (partes 1 e 2), UC014, UC015; cancelar em `alt`; exclusão bloqueada em 409 | [14/area-b.md](../especificacao/14-diagramas-de-sequencia/area-b.md), `14-sequencia-uc004`, `uc006-1`, `uc006-2`, `uc014`, `uc015` | c6aa6c2, 5b47c6f |
| #107 item 15 | IDs do catálogo para os UCs da B (TC010-TC018, TC028-TC030) e casos novos TC091-TC118; negativos por regra (incluindo UC015 R-4 e UC006 R-2) | [15/area-b.md](../especificacao/15-casos-de-teste/area-b.md) | 62bcbae, 19817df |

Pendências para o grupo, em [pendencias-area-b.md](../pendencias-area-b.md): o cancelamento pelo Instrutor não tem fluxo no item 10; o upload direto ao storage fica fora do item 13; não está definido se a aula é criada antes ou depois do upload (UC015 passo 7).

## Área C (Lucas Bruno): aprendizagem do aluno

| Issue | O que foi implementado | Arquivos | Commits |
|---|---|---|---|
| #93 item 12 | Enrollment (pending/active), Payment 0..* por matrícula, LessonProgress, QuizAttempt com `status` draft/submitted, QuizAnswer, Review; desvio da 3FN em Payment justificado | [12/area-c.md](../especificacao/12-modelo-de-dados/area-c.md), `12-modelo-de-dados-area-c.drawio/.png` | f7e6c91, 69342c8 |
| #98 item 13 | Negocial (QuizAnswer com associações, factories `Enrollment.create`/`Payment.create`, `QuizAttempt.submit`) e implementação (matrícula, aprendizagem); layout refeito sem cruzamento | [13/area-c.md](../especificacao/13-diagrama-de-classes/area-c.md), `13-classes-area-c-*.drawio/.png` | c02c062, 3a45147, f7fa7c0, f8a851b |
| #103 item 14 | UC002 (rascunho via `saveDraft`), UC003, UC009 (404), UC010, UC019, UC020; mensagens iguais aos métodos do 13 | [14/area-c.md](../especificacao/14-diagramas-de-sequencia/area-c.md), `14-sequencia-uc002`, `uc003`, `uc009`, `uc010`, `uc019`, `uc020` | 13edba6, 6bf6d3e, 28de1cb |
| #108 item 15 | IDs do catálogo para os UCs da C e casos novos TC151-TC179; TC157 sem regra inventada; TC019/TC151 em 201 | [15/area-c.md](../especificacao/15-casos-de-teste/area-c.md) | 1b28040, 681b53a, ec15b27 |

Pendências para o grupo, em [pendencias-area-c.md](../pendencias-area-c.md):
- falta a R-4 no UC002 (gabarito oculto antes do envio) e no UC009;
- o endpoint `stream` do TDD diz 403 e a decisão foi 404;
- é preciso atualizar o catálogo `docs/testes/casos-de-teste.md` (TC054 removido, TC057 renomeado, TC178 e TC179 novos);
- aceitar ou não o desvio da 3FN em Payment;
- "Matricular-se" ou "Concluir pagamento" para matrícula pendente (TC152/TC154);
- tipos de framework no item 13.

## Área D (Vinicius Teider): Tutor de IA, analytics e administração

| Issue | O que foi implementado | Arquivos | Commits |
|---|---|---|---|
| #94 item 12 | Conversation (UNIQUE userId+lessonId), Message, AuditLog (ipAddress, userAgent, details, targetId UUID); 3FN declarada com precisão | [12/area-d.md](../especificacao/12-modelo-de-dados/area-d.md), `12-modelo-de-dados-area-d.drawio/.png` | 07a5b29, d4e8ca4, 4f2a591 |
| #122 pendências do item 12 | Seed do primeiro Administrador (`DatabaseSeeder`); `blocked` compatível com 403 `ACCOUNT_BLOCKED`; AuditLog com retenção de 12 meses (RNF016); `User.locale` no Tutor de IA e no dashboard | [12/area-d.md](../especificacao/12-modelo-de-dados/area-d.md) | fb1020f |
| #99 item 13 | Negocial (AuditLog ligado a User, `Instructor.viewDashboard`) e implementação (administração, Tutor de IA e analytics), com os DTOs e Resources citados desenhados | [13/area-d.md](../especificacao/13-diagrama-de-classes/area-d.md), `13-classes-area-d-*.drawio/.png` | 7789747, 1565098, 4c9065d, 2d5a1cc, 4baf1e3 |
| #104 item 14 | UC001, UC007, UC008, UC016, UC018; erros com os códigos do TDD; UC016 com `JwtGuard` (Área A); duas chamadas `MessageRepository.create` no UC001 | [14/area-d.md](../especificacao/14-diagramas-de-sequencia/area-d.md), `14-sequencia-uc001`, `uc007`, `uc008`, `uc016`, `uc018` | bf47542, 22792b6, 451fa15, 2be679d, a39c427, 86ef864, 655f822, b9ede98 |
| #123 pendências do item 14 | 409 `CONFLICT` só para exclusão bloqueada, `LESSON_NOT_INDEXED` para aula não indexada, 503 `SERVICE_UNAVAILABLE` com `Retry-After`; auditoria no UC008 | [14/area-d.md](../especificacao/14-diagramas-de-sequencia/area-d.md), fim do arquivo | 48912d0, 22792b6 |
| #109 item 15 | TC211-TC264; TC255 em 401; filtros com os nomes do 13 (`startDate`, `endDate`, `courseId`, `groupBy`); casos sem regra removidos | [15/area-d.md](../especificacao/15-casos-de-teste/area-d.md) | ad7db41, 0851568, bb6da0a |

Pendências para o grupo, em [pendencias-area-d.md](../pendencias-area-d.md):
- TC243 a TC246 e TC265 a TC268 saíram por falta de regra no item 10;
- retenção do AuditLog por job agendado, a confirmar;
- detalhes de blocklist no Redis e de `Retry-After` sem regra.

## Verificação final

- Todo `.drawio` em `especificacao/diagramas/` tem `.png`; não há `.puml` em `especificacao/`.
- Nenhum ID de caso de teste se repete entre os arquivos das áreas.
- Todos os links Markdown relativos dos itens 12 a 15 resolvem.
- Os 8 bloqueios da 2ª revisão foram conferidos no arquivo: `parseToken` na A e na D; sem `quiz_drafts`; `saveDraft` e as factories declaradas no 13; sem `save(msgUser`; as 6 classes citadas desenhadas; `pendencias-area-d.md` existe; o TC usa `groupBy`; o CHANGELOG está consolidado.
- Não verifiquei depois da integração: os 8 itens "corrigir" e as sugestões da 2ª revisão que não eram bloqueio (layout fino de PNG, TC154 e outros) foram tratados pelos workers, mas não conferi um por um.

## O que falta para entregar

1. O grupo decidir as pendências de `pendencias-area-{b,c,d}.md` e apagar esses três arquivos da raiz (ou movê-los para as issues `pendencia-cruzada`).
2. Commits da B e da C saíram sem acento e em português ("logico", "area"); a regra global pede commit em inglês. Dá para reescrever num squash do PR.
3. Push, PR (um por área ou um só) com `Closes #92 ... #123` e troca de `#TBD` pelo número do PR no `CHANGELOG.md`: só quando você mandar.

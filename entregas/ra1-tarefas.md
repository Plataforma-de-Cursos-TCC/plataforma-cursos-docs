---
id: ra1-tarefas
titulo: "Quebra de tarefas: RA1 (Especificação do Projeto, itens 1 a 11)"
tipo: processo
status: rascunho, aguardando aprovação do grupo
atualizado: 2026-10-08
relacionados: [ra1-criterios-de-aceite, contexto, adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006]
---

# Quebra de Tarefas: RA1 (Especificação do Projeto, itens 1 a 11)

> **Atualização de 08/10/2026:** este plano é o registro histórico de como as tarefas foram abertas. Quatro pontos dele foram revistos e valem as decisões novas: (1) "mínimo 4 por integrante" e os totais "≥16" são meta interna, e o mínimo oficial é de 8 especificações de caso de uso ([ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md)); (2) não há IDs provisórios nem renumeração em T12, fica a numeração da v11 com IDs novos no fim; (3) o «extend» sai do caso de uso opcional e aponta para o base ([ADR-0003](../docs/adr/0003-extend-no-sentido-do-te3-3.md)); (4) o item 4 é BPMN 2.0 e os itens 9 e 11 são PlantUML ([ADR-0004](../docs/adr/0004-diagramas-como-codigo.md)), e as tabelas dos itens 6 e 8 seguem só as colunas do template. Os critérios vigentes estão em [ra1-criterios-de-aceite](ra1-criterios-de-aceite.md).

> Plano de tarefas para o GitHub Project do repositório `Plataforma-de-Cursos-TCC/plataforma-cursos-docs`, derivado de [`ra1-criterios-de-aceite.md`](ra1-criterios-de-aceite.md).
> Os critérios (IDs `Cxx.y`, `X.y`, `K.y`) estão definidos naquele arquivo. Aqui só se referenciam os IDs.
> **Status:** rascunho, aguardando aprovação do grupo. Prazo da entrega: 10/10/2026, 23:59 (Canvas, "Avaliação do RA 1 - Projeto").

---

## 1. Decisões de divisão

### 1.1 Responsáveis
- **Sub-issues por área** (itens 6, 7, 8 e 10): responsável é o dono da área (tabela 1.2): A Lucas Stopinski, B Adrian, C Lucas Bruno, D Vinicius.
- **Demais tarefas** ficam sem responsável; quem puxar se coloca como responsável (assignee) ao começar.
- **Itens 1 a 5, 9 e 11 e tarefas gerais** (preparação, revisão final, consolidação e envio): do grupo; quem puxar escreve, e outro integrante revisa ([CONTEXT.md](../CONTEXT.md), seção 5).
- **Integrantes:** Adrian Antônio de Souza Gomes (`adrian69-droid`), Lucas Bruno e Silva (`Luc-Bruno`), Lucas Stopinski da Silva (`LucasStop`) e Vinicius Lima Teider (`Teider011`).

### 1.2 Divisão por área (itens 6, 7, 8 e 10)

Cada integrante fica com **uma área** ([ADR-0006](../docs/adr/0006-divisao-por-areas.md)). Dentro dela faz **no mínimo 4 RFs**, uma estória por RF, **no mínimo 4 especificações de caso de uso** e **no mínimo 4 RNFs**, sem máximo ([ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md)). RF além do mínimo pode ser coberto por caso de uso existente, por `include` ou `extend`. A cadeia RF, estória, caso de uso fica com a mesma pessoa.

| Área | Escopo | Casos de uso de partida | IDs provisórios | RNF (ISO/IEC 25010) | Responsável |
|---|---|---|---|---|---|
| **A** | Acesso e conta | Cadastrar-se, Realizar login, Recuperar senha, Editar dados do perfil | RF-A1… · US-A1… · RNF-A1… · UC-A1… | Segurança (incl. LGPD) · Compatibilidade | Lucas Stopinski da Silva (`LucasStop`) |
| **B** | Autoria do instrutor | Cadastrar curso, Gerenciar módulos, Gerenciar aulas, Cadastrar quiz com gabarito | RF-B1… · US-B1… · RNF-B1… · UC-B1… | Manutenibilidade · Portabilidade | Adrian Antônio de Souza Gomes (`adrian69-droid`) |
| **C** | Aprendizagem do aluno | Matricular-se em curso, Assistir aula, Responder quiz, Avaliar curso | RF-C1… · US-C1… · RNF-C1… · UC-C1… | Capacidade de interação · Acessibilidade | Lucas Bruno e Silva (`Luc-Bruno`) |
| **D** | Tutor de IA, analytics e administração | Conversar com Tutor de IA, Ver dashboard com filtro, Gerenciar usuários, Acessar área protegida por perfil | RF-D1… · US-D1… · RNF-D1… · UC-D1… | Eficiência de desempenho · Confiabilidade | Vinicius Lima Teider (`Teider011`) |

Os escopos são orientação para evitar sobreposição. Os requisitos em si são definidos por cada integrante nas sub-issues. A renumeração única (RF001, US001, RNF001, UC001) acontece no início de T12 e fica registrada em `entregas/ra1-renumeracao.md`.

### 1.3 Fluxo de trabalho

- **Formato:** todo o conteúdo é produzido em arquivos **Markdown** no repositório, e não direto no .docx do template.
- **Diagramas como código** ([ADR-0004](../docs/adr/0004-diagramas-como-codigo.md)): Mermaid (`.mmd` ou bloco no Markdown); BPMN 2.0 em `.bpmn` no item 4 (critério C04.1). Fonte versionada junto da imagem exportada.
- **Branches:** uma por tarefa (`feat/nome-descritivo` ou `fix/nome-descritivo`), entrando na `main` por **pull request** (`gh pr create`). PR aberto = **In review**; **Done** só após o merge.
- **Consolidação:** com todos os itens na `main`, os MDs viram um único documento na ordem e com os títulos do template, exportado em **PDF e DOCX**.
- **Nomes exatos:** produto "Plataforma de Cursos"; atores Visitante, Aluno, Instrutor, Administrador e Tutor de IA.

### 1.4 Pendências cruzadas entre áreas

As áreas não avançam no mesmo ritmo. Um RF, estória ou caso de uso pode depender de algo que outra área ainda não escreveu. **O trabalho não para, mas a suposição fica registrada** (AGENTS.md, regra 8); ninguém inventa o requisito da outra área.

- **Onde registrar:** issue com o rótulo `pendencia-cruzada`, o rótulo do item e o da área que precisa resolver. Uma issue por área e item, com uma linha marcável por pendência e a indicação de onde a suposição aparece.
- **Quem registra:** quem escreve ou revisa; se a issue não existir, cria.
- **Bloqueio:** cada issue de pendência bloqueia a tarefa-mãe do item (T06, T07, T08 ou T10). A consolidação não fecha com pendência aberta (K.12).
- **Como fechar uma linha:** escrever o ID do requisito que atende (por exemplo `→ RF-A3`) ou a decisão do grupo de não fazer. Se o requisito sair diferente do suposto, o dono da área afetada ajusta o texto.
- **Conferência por item:** com as quatro áreas entregues, a tarefa-mãe começa pela conferência cruzada: percorrer as issues do item, fechar cada linha e reler os quatro textos juntos.

---

## 2. Rótulos (labels) a criar no repositório

| Rótulo | Cor | Uso |
|---|---|---|
| `ra1` | `#1D76DB` | Todas as tarefas desta entrega |
| `item-01` … `item-11` | `#C5DEF5` | Item do template |
| `geral` | `#BFDADC` | Tarefas que não são de um item específico |
| `por-integrante` | `#FBCA04` | Sub-issues da cota mínima de 4 por integrante |
| `area-a` … `area-d` | `#D4C5F9` | Área (seção 1.2) |
| `tarefa-mae` | `#C5DEF5` | Tarefa de consolidação com sub-issues (T06, T07, T08, T10) |
| `pendencia-cruzada` | `#B60205` | Amarração entre áreas (seção 1.4) |

---

## 3. Lista de tarefas

Título: `[RA1][Item NN] <descrição>`; gerais: `[RA1][Geral] <descrição>`. **T06, T07, T08 e T10 são tarefas-mãe** com 4 sub-issues (a, b, c, d = áreas A a D). Total: **30 issues** (14 principais + 16 sub-issues).

### Resumo

| ID | Título da issue | Rótulos | Critérios | Bloqueada por | Responsável |
|---|---|---|---|---|---|
| T00 | [RA1][Geral] Preparar a estrutura do repositório para a especificação | `ra1`, `geral` | X.1, X.9 | — | |
| T01 | [RA1][Item 01] Quadro "3 Objetivos" | `ra1`, `item-01` | C01.1 a C01.4 | T00 | |
| T02 | [RA1][Item 02] Quadro "É – Não é – Faz – Não faz" | `ra1`, `item-02` | C02.1 a C02.4 | T00 | |
| T03 | [RA1][Item 03] Visão do Produto | `ra1`, `item-03` | C03.1 a C03.5 | T01, T02 | |
| T05 | [RA1][Item 05] Relação de Atores / Usuários | `ra1`, `item-05` | C05.1 a C05.5 | T03 | |
| T04 | [RA1][Item 04] Mapeamento de Negócios (BPMN TO BE) | `ra1`, `item-04` | C04.1 a C04.9 | T05 | |
| T06 | [RA1][Item 06] Relação de Requisitos Funcionais (≥16 RFs) | `ra1`, `item-06`, `tarefa-mae` | C06.1 a C06.9 | T03, T05 | |
| T07 | [RA1][Item 07] Relação de Estórias de Usuário (≥16 estórias) | `ra1`, `item-07`, `tarefa-mae` | C07.1 a C07.7 | T06 | |
| T08 | [RA1][Item 08] Relação de Requisitos Não Funcionais (≥16 RNFs) | `ra1`, `item-08`, `tarefa-mae` | C08.1 a C08.6 | T03 | |
| T09 | [RA1][Item 09] Diagrama Geral de Casos de Uso | `ra1`, `item-09` | C09.1 a C09.8 | T04, T06 | |
| T10 | [RA1][Item 10] Especificações de Caso de Uso (≥16 especificações) | `ra1`, `item-10`, `tarefa-mae` | C10.1 a C10.9 | T07, T09 | |
| T11 | [RA1][Item 11] Diagrama de Atividades | `ra1`, `item-11` | C11.1 a C11.7 | T10 | |
| T12 | [RA1][Geral] Revisão cruzada e verificação independente | `ra1`, `geral` | K.1 a K.13, X.8 e a verificação de todos os `Cxx.y` | T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11 | |
| T13 | [RA1][Geral] Consolidar em PDF e DOCX e enviar no Canvas | `ra1`, `geral` | X.1, X.2, X.3, X.4, X.5, X.6, X.7, X.9, X.10 | T12 | |
| T06a |   ↳ [RA1][Item 06] RFs da área A (Acesso e conta) | `ra1`, `item-06`, `por-integrante`, `area-a` | C06.2, C06.3, C06.4, C06.5, C06.9 | T03, T05 | |
| T06b |   ↳ [RA1][Item 06] RFs da área B (Autoria do instrutor) | `ra1`, `item-06`, `por-integrante`, `area-b` | C06.2, C06.3, C06.4, C06.5, C06.9 | T03, T05 | |
| T06c |   ↳ [RA1][Item 06] RFs da área C (Aprendizagem do aluno) | `ra1`, `item-06`, `por-integrante`, `area-c` | C06.2, C06.3, C06.4, C06.5, C06.9 | T03, T05 | |
| T06d |   ↳ [RA1][Item 06] RFs da área D (Tutor de IA, analytics e administração) | `ra1`, `item-06`, `por-integrante`, `area-d` | C06.2, C06.3, C06.4, C06.5, C06.9 | T03, T05 | |
| T07a |   ↳ [RA1][Item 07] Estórias da área A (Acesso e conta) | `ra1`, `item-07`, `por-integrante`, `area-a` | C07.2 a C07.7 | T06a | |
| T07b |   ↳ [RA1][Item 07] Estórias da área B (Autoria do instrutor) | `ra1`, `item-07`, `por-integrante`, `area-b` | C07.2 a C07.7 | T06b | |
| T07c |   ↳ [RA1][Item 07] Estórias da área C (Aprendizagem do aluno) | `ra1`, `item-07`, `por-integrante`, `area-c` | C07.2 a C07.7 | T06c | |
| T07d |   ↳ [RA1][Item 07] Estórias da área D (Tutor de IA, analytics e administração) | `ra1`, `item-07`, `por-integrante`, `area-d` | C07.2 a C07.7 | T06d | |
| T08a |   ↳ [RA1][Item 08] RNFs da área A (Acesso e conta) | `ra1`, `item-08`, `por-integrante`, `area-a` | C08.2, C08.3, C08.4, C08.6 | T03 | |
| T08b |   ↳ [RA1][Item 08] RNFs da área B (Autoria do instrutor) | `ra1`, `item-08`, `por-integrante`, `area-b` | C08.2, C08.3, C08.4, C08.6 | T03 | |
| T08c |   ↳ [RA1][Item 08] RNFs da área C (Aprendizagem do aluno) | `ra1`, `item-08`, `por-integrante`, `area-c` | C08.2, C08.3, C08.4, C08.6 | T03 | |
| T08d |   ↳ [RA1][Item 08] RNFs da área D (Tutor de IA, analytics e administração) | `ra1`, `item-08`, `por-integrante`, `area-d` | C08.2, C08.3, C08.4, C08.6 | T03 | |
| T10a |   ↳ [RA1][Item 10] Especificações de caso de uso da área A (Acesso e conta) | `ra1`, `item-10`, `por-integrante`, `area-a` | C10.2 a C10.9 | T07a, T09 | |
| T10b |   ↳ [RA1][Item 10] Especificações de caso de uso da área B (Autoria do instrutor) | `ra1`, `item-10`, `por-integrante`, `area-b` | C10.2 a C10.9 | T07b, T09 | |
| T10c |   ↳ [RA1][Item 10] Especificações de caso de uso da área C (Aprendizagem do aluno) | `ra1`, `item-10`, `por-integrante`, `area-c` | C10.2 a C10.9 | T07c, T09 | |
| T10d |   ↳ [RA1][Item 10] Especificações de caso de uso da área D (Tutor de IA, analytics e administração) | `ra1`, `item-10`, `por-integrante`, `area-d` | C10.2 a C10.9 | T07d, T09 | |

### Fase 0 — Preparação

**T00 · [RA1][Geral] Preparar a estrutura do repositório para a especificação**
- Responsável: em branco · Rótulos: `ra1`, `geral`
- Descrição: Criar em `especificacao/` um arquivo MD por item do template (1 a 11), com os títulos originais; nos itens 6, 7, 8 e 10, um arquivo por área (`area-a.md` a `area-d.md`, ADR-0006). Definir a pasta dos diagramas (fonte `.mmd` ou `.bpmn` + imagem exportada), o nome do produto (Plataforma de Cursos) e o padrão de branch (`feat/` ou `fix/`). Registrar no `README.md`.
- Critérios que fecha: X.1, X.9
- Bloqueada por: nenhuma

### Fase 1 — Visão do produto

**T01 · [RA1][Item 01] Quadro "3 Objetivos"**
- Responsável: em branco · Rótulos: `ra1`, `item-01`
- Descrição: Escrever os 3 objetivos de negócio, cada um com problema, valor e métrica de sucesso.
- Critérios que fecha: C01.1, C01.2, C01.3, C01.4
- Bloqueada por: T00

**T02 · [RA1][Item 02] Quadro "É – Não é – Faz – Não faz"**
- Responsável: em branco · Rótulos: `ra1`, `item-02`
- Descrição: Preencher os 4 quadrantes (≥3 itens específicos cada), coerentes com o fora de escopo do `CONTEXT.md` (seção 1).
- Critérios que fecha: C02.1, C02.2, C02.3, C02.4
- Bloqueada por: T00

**T03 · [RA1][Item 03] Visão do Produto**
- Responsável: em branco · Rótulos: `ra1`, `item-03`
- Descrição: Quadro A (problemas e expectativas) e quadro B (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor), com os rótulos exatos do template.
- Critérios que fecha: C03.1, C03.2, C03.3, C03.4, C03.5
- Bloqueada por: T01, T02

**T05 · [RA1][Item 05] Relação de Atores / Usuários**
- Responsável: em branco · Rótulos: `ra1`, `item-05`
- Descrição: Tabela com Visitante, Aluno, Instrutor, Administrador e Tutor de IA (ator sistêmico), com papel, responsabilidades e relação com o sistema; nomes idênticos em todos os itens.
- Critérios que fecha: C05.1, C05.2, C05.3, C05.4, C05.5
- Bloqueada por: T03

**T04 · [RA1][Item 04] Mapeamento de Negócios (BPMN TO BE)**
- Responsável: em branco · Rótulos: `ra1`, `item-04`
- Descrição: Diagrama BPMN 2.0 (`.bpmn`) do processo TO BE, com lanes dos atores do item 5, gateways com condições e mensagens com o Tutor de IA. Exportar a imagem para o documento.
- Critérios que fecha: C04.1, C04.2, C04.3, C04.4, C04.5, C04.6, C04.7, C04.8, C04.9
- Bloqueada por: T05

### Fase 2 — Requisitos (todos)

**T06 · [RA1][Item 06] Relação de Requisitos Funcionais (≥16 RFs)**
- Responsável: em branco · Rótulos: `ra1`, `item-06`, `tarefa-mae`
- Descrição: Tarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Consolida os RFs das 4 áreas (≥16) na tabela do template, com coluna OBJETIVO; divide em sprints e escreve a justificativa da priorização (C06.6 e C06.7) depois que RFs e RNFs estiverem definidos.
- Critérios que fecha: C06.1, C06.2, C06.3, C06.4, C06.5, C06.6, C06.7, C06.8, C06.9
- Bloqueada por: T03, T05

  **T06a · [RA1][Item 06] RFs da área A (Acesso e conta)**
  - Responsável: `LucasStop` · Rótulos: `ra1`, `item-06`, `por-integrante`, `area-a`
  - Descrição: Escrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-A1….
  - Critérios que fecha: C06.2, C06.3, C06.4, C06.5, C06.9
  - Bloqueada por: T03, T05

  **T06b · [RA1][Item 06] RFs da área B (Autoria do instrutor)**
  - Responsável: `adrian69-droid` · Rótulos: `ra1`, `item-06`, `por-integrante`, `area-b`
  - Descrição: Escrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-B1….
  - Critérios que fecha: C06.2, C06.3, C06.4, C06.5, C06.9
  - Bloqueada por: T03, T05

  **T06c · [RA1][Item 06] RFs da área C (Aprendizagem do aluno)**
  - Responsável: `Luc-Bruno` · Rótulos: `ra1`, `item-06`, `por-integrante`, `area-c`
  - Descrição: Escrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-C1….
  - Critérios que fecha: C06.2, C06.3, C06.4, C06.5, C06.9
  - Bloqueada por: T03, T05

  **T06d · [RA1][Item 06] RFs da área D (Tutor de IA, analytics e administração)**
  - Responsável: `Teider011` · Rótulos: `ra1`, `item-06`, `por-integrante`, `area-d`
  - Descrição: Escrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-D1….
  - Critérios que fecha: C06.2, C06.3, C06.4, C06.5, C06.9
  - Bloqueada por: T03, T05

**T07 · [RA1][Item 07] Relação de Estórias de Usuário (≥16 estórias)**
- Responsável: em branco · Rótulos: `ra1`, `item-07`, `tarefa-mae`
- Descrição: Tarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Confere uma estória por RF e ≥2 critérios DADO QUE / QUANDO / ENTÃO por estória.
- Critérios que fecha: C07.1, C07.2, C07.3, C07.4, C07.5, C07.6, C07.7
- Bloqueada por: T06

  **T07a · [RA1][Item 07] Estórias da área A (Acesso e conta)**
  - Responsável: `LucasStop` · Rótulos: `ra1`, `item-07`, `por-integrante`, `area-a`
  - Descrição: Escrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-A1….
  - Critérios que fecha: C07.2, C07.3, C07.4, C07.5, C07.6, C07.7
  - Bloqueada por: T06a

  **T07b · [RA1][Item 07] Estórias da área B (Autoria do instrutor)**
  - Responsável: `adrian69-droid` · Rótulos: `ra1`, `item-07`, `por-integrante`, `area-b`
  - Descrição: Escrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-B1….
  - Critérios que fecha: C07.2, C07.3, C07.4, C07.5, C07.6, C07.7
  - Bloqueada por: T06b

  **T07c · [RA1][Item 07] Estórias da área C (Aprendizagem do aluno)**
  - Responsável: `Luc-Bruno` · Rótulos: `ra1`, `item-07`, `por-integrante`, `area-c`
  - Descrição: Escrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-C1….
  - Critérios que fecha: C07.2, C07.3, C07.4, C07.5, C07.6, C07.7
  - Bloqueada por: T06c

  **T07d · [RA1][Item 07] Estórias da área D (Tutor de IA, analytics e administração)**
  - Responsável: `Teider011` · Rótulos: `ra1`, `item-07`, `por-integrante`, `area-d`
  - Descrição: Escrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-D1….
  - Critérios que fecha: C07.2, C07.3, C07.4, C07.5, C07.6, C07.7
  - Bloqueada por: T06d

**T08 · [RA1][Item 08] Relação de Requisitos Não Funcionais (≥16 RNFs)**
- Responsável: em branco · Rótulos: `ra1`, `item-08`, `tarefa-mae`
- Descrição: Tarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Consolida os RNFs (≥16), classificados na ISO/IEC 25010 e com métrica; confere a cobertura das características (C08.5). Pode correr em paralelo com T06 e T07.
- Critérios que fecha: C08.1, C08.2, C08.3, C08.4, C08.5, C08.6
- Bloqueada por: T03

  **T08a · [RA1][Item 08] RNFs da área A (Acesso e conta)**
  - Responsável: `LucasStop` · Rótulos: `ra1`, `item-08`, `por-integrante`, `area-a`
  - Descrição: Escrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (segurança (LGPD) e compatibilidade) e com métrica mensurável. IDs provisórios: RNF-A1….
  - Critérios que fecha: C08.2, C08.3, C08.4, C08.6
  - Bloqueada por: T03

  **T08b · [RA1][Item 08] RNFs da área B (Autoria do instrutor)**
  - Responsável: `adrian69-droid` · Rótulos: `ra1`, `item-08`, `por-integrante`, `area-b`
  - Descrição: Escrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (manutenibilidade e portabilidade) e com métrica mensurável. IDs provisórios: RNF-B1….
  - Critérios que fecha: C08.2, C08.3, C08.4, C08.6
  - Bloqueada por: T03

  **T08c · [RA1][Item 08] RNFs da área C (Aprendizagem do aluno)**
  - Responsável: `Luc-Bruno` · Rótulos: `ra1`, `item-08`, `por-integrante`, `area-c`
  - Descrição: Escrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (capacidade de interação e acessibilidade) e com métrica mensurável. IDs provisórios: RNF-C1….
  - Critérios que fecha: C08.2, C08.3, C08.4, C08.6
  - Bloqueada por: T03

  **T08d · [RA1][Item 08] RNFs da área D (Tutor de IA, analytics e administração)**
  - Responsável: `Teider011` · Rótulos: `ra1`, `item-08`, `por-integrante`, `area-d`
  - Descrição: Escrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (eficiência de desempenho e confiabilidade) e com métrica mensurável. IDs provisórios: RNF-D1….
  - Critérios que fecha: C08.2, C08.3, C08.4, C08.6
  - Bloqueada por: T03

### Fase 3 — Casos de uso (todos + integração)

**T09 · [RA1][Item 09] Diagrama Geral de Casos de Uso**
- Responsável: em branco · Rótulos: `ra1`, `item-09`
- Descrição: Um único diagrama Mermaid com todos os casos de uso (≥16), montado a partir dos RFs das 4 áreas, com generalização de atores e `include`/`extend` (seta do caso base para o estendido, ADR-0003). Todo RF coberto por ao menos um caso de uso (K.3).
- Critérios que fecha: C09.1, C09.2, C09.3, C09.4, C09.5, C09.6, C09.7, C09.8
- Bloqueada por: T04, T06

**T10 · [RA1][Item 10] Especificações de Caso de Uso (≥16 especificações)**
- Responsável: em branco · Rótulos: `ra1`, `item-10`, `tarefa-mae`
- Descrição: Tarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Confere os campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção em todas as especificações.
- Critérios que fecha: C10.1, C10.2, C10.3, C10.4, C10.5, C10.6, C10.7, C10.8, C10.9
- Bloqueada por: T07, T09

  **T10a · [RA1][Item 10] Especificações de caso de uso da área A (Acesso e conta)**
  - Responsável: `LucasStop` · Rótulos: `ra1`, `item-10`, `por-integrante`, `area-a`
  - Descrição: Escrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-A1….
  - Critérios que fecha: C10.2, C10.3, C10.4, C10.5, C10.6, C10.7, C10.8, C10.9
  - Bloqueada por: T07a, T09

  **T10b · [RA1][Item 10] Especificações de caso de uso da área B (Autoria do instrutor)**
  - Responsável: `adrian69-droid` · Rótulos: `ra1`, `item-10`, `por-integrante`, `area-b`
  - Descrição: Escrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-B1….
  - Critérios que fecha: C10.2, C10.3, C10.4, C10.5, C10.6, C10.7, C10.8, C10.9
  - Bloqueada por: T07b, T09

  **T10c · [RA1][Item 10] Especificações de caso de uso da área C (Aprendizagem do aluno)**
  - Responsável: `Luc-Bruno` · Rótulos: `ra1`, `item-10`, `por-integrante`, `area-c`
  - Descrição: Escrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-C1….
  - Critérios que fecha: C10.2, C10.3, C10.4, C10.5, C10.6, C10.7, C10.8, C10.9
  - Bloqueada por: T07c, T09

  **T10d · [RA1][Item 10] Especificações de caso de uso da área D (Tutor de IA, analytics e administração)**
  - Responsável: `Teider011` · Rótulos: `ra1`, `item-10`, `por-integrante`, `area-d`
  - Descrição: Escrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-D1….
  - Critérios que fecha: C10.2, C10.3, C10.4, C10.5, C10.6, C10.7, C10.8, C10.9
  - Bloqueada por: T07d, T09

**T11 · [RA1][Item 11] Diagrama de Atividades**
- Responsável: em branco · Rótulos: `ra1`, `item-11`
- Descrição: Diagrama de atividades UML em Mermaid, com raias dos atores, decisões com guarda e fork/join (ex.: Aluno assiste à aula enquanto o Tutor de IA fica disponível).
- Critérios que fecha: C11.1, C11.2, C11.3, C11.4, C11.5, C11.6, C11.7
- Bloqueada por: T10

### Fase 4 — Fechamento

**T12 · [RA1][Geral] Revisão cruzada e verificação independente**
- Responsável: em branco · Rótulos: `ra1`, `geral`
- Descrição: Primeiro, aplicar a renumeração única (RF-A1… para RF001…, US-A1… para US001…, RNF-A1… para RNF001…, UC-A1… para UC001…; ADR-0001), atualizar as referências cruzadas e registrar a correspondência em `entregas/ra1-renumeracao.md`. Depois, com todos os MDs na `main`, executar o checklist K.1 a K.13 e a verificação independente de todos os IDs (seção 0.3, passo 6), produzindo a tabela `ID | status | evidência`. Corrigir ou devolver aos responsáveis o que não passar.
- Critérios que fecha: K.1, K.2, K.3, K.4, K.5, K.6, K.7, K.8, K.9, K.10, K.11, K.12, K.13, X.8
- Bloqueada por: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11

**T13 · [RA1][Geral] Consolidar em PDF e DOCX e enviar no Canvas**
- Responsável: em branco · Rótulos: `ra1`, `geral`
- Descrição: Consolidar os MDs em um único documento no formato do template (capa com Plataforma de Cursos, os 4 autores e 2026; sumário; seções 1 a 11 na ordem; diagramas legíveis), incluir a declaração de uso de IA preenchida, exportar em PDF e DOCX e enviar na tarefa "Avaliação do RA 1 - Projeto" até 10/10/2026, 23:59.
- Critérios que fecha: X.1, X.2, X.3, X.4, X.5, X.6, X.7, X.9, X.10
- Bloqueada por: T12

---

## 4. Corpo padrão de cada issue

```markdown
## Objetivo
<o que entregar, em uma ou duas frases>

## Insumos obrigatórios
- Ler `CONTEXT.md` antes de começar.
- <arquivos e ADRs que a tarefa exige>

## Critérios de aceite
Referência: `entregas/ra1-criterios-de-aceite.md`
- [ ] <Cxx.y> <texto do critério>

## Dependências
- Bloqueada por: <#n>
- Bloqueia: <#n>

## Definição de pronto
- Branch própria, arquivo(s) MD no repositório, diagramas como código.
- Todos os critérios marcados, cada um com evidência.
- Dúvida sobre outra área registrada na issue `pendencia-cruzada`.
- PR para a `main`, outro integrante revisa; Done só após o merge.
```

---

## 5. Instruções de criação (gh)

**Pré-requisitos:** `gh` autenticado com escopo `project` (`gh auth status`; se faltar, `gh auth refresh -s project`). Repositório `Plataforma-de-Cursos-TCC/plataforma-cursos-docs`. Project nº 1 da organização (`gh project item-add 1 --owner Plataforma-de-Cursos-TCC`).

1. Ler este arquivo e `ra1-criterios-de-aceite.md` por inteiro.
2. Criar os rótulos da seção 2 (ignorar os existentes).
3. Criar as 14 issues principais na ordem da seção 3 a partir do bloco JSON abaixo, sem responsável. Guardar o número de cada uma.
4. Criar as 16 sub-issues e vinculá-las como sub-issues das mães (campo `parent`).
5. Trocar cada placeholder `{{Txx}}` dos corpos pelo `#n` real; registrar também o bloqueio nativo, se disponível (campo `blocked_by`).
6. Adicionar as 30 issues ao Project com Status **Todo**, sem datas.
7. Verificar por comando: 30 issues com `ra1`; 30 itens no Project; 4 mães com 4 sub-issues; nenhum `{{` pendente nos corpos; responsável só nas 16 sub-issues por área.
8. Relatório final: `Tarefa | nº da issue | status no Project | verificado`.

---

## 6. Pontos em aberto

- **A1.** Resolvido: A `LucasStop`, B `adrian69-droid`, C `Luc-Bruno`, D `Teider011`.
- **A2.** Resolvido: Project nº 1 (https://github.com/orgs/Plataforma-de-Cursos-TCC/projects/1).
- **A3.** Resolvido: entrega em PDF e DOCX.
- **A4.** A rubrica do Canvas não estava disponível; os critérios foram revisados contra o plano de ensino e os ADRs (ver `ra1-criterios-de-aceite.md`).
- **A5.** Resolvido: `Teider011`.

---

## Ligações

- [Critérios de aceite da entrega](ra1-criterios-de-aceite.md)
- [CONTEXT.md](../CONTEXT.md) · [AGENTS.md](../AGENTS.md)
- [ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md) · [ADR-0002](../docs/adr/0002-formato-de-estoria-e-criterios.md) · [ADR-0003](../docs/adr/0003-extend-no-sentido-do-te3-3.md) · [ADR-0004](../docs/adr/0004-diagramas-como-codigo.md) · [ADR-0005](../docs/adr/0005-tutor-de-ia-como-ator-sistemico.md) · [ADR-0006](../docs/adr/0006-divisao-por-areas.md)

---

## 7. Issues a criar (JSON)

```json
[
 {
  "id": "T00",
  "title": "[RA1][Geral] Preparar a estrutura do repositório para a especificação",
  "labels": [
   "ra1",
   "geral"
  ],
  "parent": null,
  "blocked_by": [],
  "body": "## Objetivo\nCriar em `especificacao/` um arquivo MD por item do template (1 a 11), com os títulos originais; nos itens 6, 7, 8 e 10, um arquivo por área (`area-a.md` a `area-d.md`, ADR-0006). Definir a pasta dos diagramas (fonte `.mmd` ou `.bpmn` + imagem exportada), o nome do produto (Plataforma de Cursos) e o padrão de branch (`feat/` ou `fix/`). Registrar no `README.md`.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `especificacao/` e `README.md` (mapa do repositório)\n- ADR-0001, ADR-0004, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] X.1 Template. O documento final (consolidado a partir dos MDs do repositório e entregue em PDF e DOCX) segue a estrutura do template oficial: seções na ordem de 1 a 11, títulos originais e…\n- [ ] X.9 Nome do produto. O nome Plataforma de Cursos (exatamente assim) aparece em todos os campos \"NOME DO PRODUTO\" / \"PRODUTO\" dos quadros.\n\n## Dependências\n- Bloqueada por: nenhuma\n- Bloqueia: {{T01}}, {{T02}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T01",
  "title": "[RA1][Item 01] Quadro \"3 Objetivos\"",
  "labels": [
   "ra1",
   "item-01"
  ],
  "parent": null,
  "blocked_by": [
   "T00"
  ],
  "body": "## Objetivo\nEscrever os 3 objetivos de negócio, cada um com problema, valor e métrica de sucesso.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `pesquisa/similares/lacunas-e-diferencial.md`\n- `CONTEXT.md` seções 1 e 8\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C01.1 Exatamente 3 objetivos.\n- [ ] C01.2 Cada objetivo é claro, específico e verificável.\n- [ ] C01.3 Cada objetivo articula problema, valor e métrica de sucesso: a métrica é explícita e mensurável.\n- [ ] C01.4 Os objetivos são coerentes com a Visão do Produto (item 3) e com os demais artefatos.\n\n## Dependências\n- Bloqueada por: {{T00}}\n- Bloqueia: {{T03}}, {{T06}}, {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T02",
  "title": "[RA1][Item 02] Quadro \"É – Não é – Faz – Não faz\"",
  "labels": [
   "ra1",
   "item-02"
  ],
  "parent": null,
  "blocked_by": [
   "T00"
  ],
  "body": "## Objetivo\nPreencher os 4 quadrantes (≥3 itens específicos cada), coerentes com o fora de escopo do `CONTEXT.md` (seção 1).\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `pesquisa/similares/lacunas-e-diferencial.md`, `pesquisa/similares/matriz-comparativa.md`\n- ADR-0005\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C02.1 Os 4 quadrantes estão preenchidos.\n- [ ] C02.2 Cada quadrante tem ≥3 itens específicos, não genéricos.\n- [ ] C02.3 Não há contradição entre quadrantes nem com os outros itens.\n- [ ] C02.4 O quadro delimita claramente escopo, anti-escopo, capacidades e restrições. O \"Não faz\" é coerente com o fora de escopo vigente do projeto (CONTEXT, seção 1): sem…\n\n## Dependências\n- Bloqueada por: {{T00}}\n- Bloqueia: {{T03}}, {{T06}}, {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T03",
  "title": "[RA1][Item 03] Visão do Produto",
  "labels": [
   "ra1",
   "item-03"
  ],
  "parent": null,
  "blocked_by": [
   "T01",
   "T02"
  ],
  "body": "## Objetivo\nQuadro A (problemas e expectativas) e quadro B (cliente-alvo, categoria-segmento, benefício-chave, diferencial-chave, meta-valor), com os rótulos exatos do template.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `pesquisa/similares/README.md`, `matriz-comparativa.md`, `lacunas-e-diferencial.md`\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C03.1 O quadro A está completo: problemas e expectativas bem definidos.\n- [ ] C03.2 Cada expectativa corresponde a pelo menos um problema levantado.\n- [ ] C03.3 Os 5 campos do quadro B estão preenchidos com precisão.\n- [ ] C03.4 Valor (meta-valor) e diferencial são verificáveis, não apenas slogans. O diferencial (Tutor de IA no contexto da aula) é confirmado ou ajustado pela pesquisa…\n- [ ] C03.5 Os dois quadros são coerentes entre si e com os itens 1 e 2.\n\n## Dependências\n- Bloqueada por: {{T01}}, {{T02}}\n- Bloqueia: {{T05}}, {{T06}}, {{T08}}, {{T12}}, {{T06a}}, {{T06b}}, {{T06c}}, {{T06d}}, {{T08a}}, {{T08b}}, {{T08c}}, {{T08d}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T05",
  "title": "[RA1][Item 05] Relação de Atores / Usuários",
  "labels": [
   "ra1",
   "item-05"
  ],
  "parent": null,
  "blocked_by": [
   "T03"
  ],
  "body": "## Objetivo\nTabela com Visitante, Aluno, Instrutor, Administrador e Tutor de IA (ator sistêmico), com papel, responsabilidades e relação com o sistema; nomes idênticos em todos os itens.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 2\n- ADR-0005\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C05.1 ≥3 atores.\n- [ ] C05.2 Cada ator tem papel e responsabilidades descritos. Como a tabela do template só tem nome, acrescentar descrição, em coluna extra ou texto abaixo.\n- [ ] C05.3 Cada ator tem sua relação com o processo e com o sistema explicitada.\n- [ ] C05.4 As descrições são sucintas, sem ambiguidade e sem sobreposição de papéis.\n- [ ] C05.5 Os atores são os mesmos usados nas lanes do BPMN (item 4), nos RFs (item 6), nas estórias (item 7) e nos casos de uso (itens 9 e 10).\n\n## Dependências\n- Bloqueada por: {{T03}}\n- Bloqueia: {{T04}}, {{T06}}, {{T12}}, {{T06a}}, {{T06b}}, {{T06c}}, {{T06d}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T04",
  "title": "[RA1][Item 04] Mapeamento de Negócios (BPMN TO BE)",
  "labels": [
   "ra1",
   "item-04"
  ],
  "parent": null,
  "blocked_by": [
   "T05"
  ],
  "body": "## Objetivo\nDiagrama BPMN 2.0 (`.bpmn`) do processo TO BE, com lanes dos atores do item 5, gateways com condições e mensagens com o Tutor de IA. Exportar a imagem para o documento.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 2 e glossário\n- ADR-0004\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C04.1 A notação é BPMN de verdade, não um fluxograma improvisado.\n- [ ] C04.2 O diagrama representa apenas o TO BE, sem misturar com o AS IS.\n- [ ] C04.3 Tem evento de início e de fim.\n- [ ] C04.4 Tem atividades rotuladas de forma padronizada (verbo no infinitivo + objeto).\n- [ ] C04.5 Tem gateways com condições escritas nas saídas.\n- [ ] C04.6 Tem pools/lanes coerentes com os atores do item 5.\n- [ ] C04.7 Tem eventos e mensagens quando aplicável, por exemplo a pergunta do Aluno ao Tutor de IA e a resposta com o contexto da aula.\n- [ ] C04.8 O caminho principal está representado (do curso publicado ao Aluno que estuda, é avaliado e tira dúvidas com o Tutor de IA); o nível de detalhe é adequado e o…\n- [ ] C04.9 É consistente com a Visão do Produto.\n\n## Dependências\n- Bloqueada por: {{T05}}\n- Bloqueia: {{T09}}, {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T06",
  "title": "[RA1][Item 06] Relação de Requisitos Funcionais (≥16 RFs)",
  "labels": [
   "ra1",
   "item-06",
   "tarefa-mae"
  ],
  "parent": null,
  "blocked_by": [
   "T03",
   "T05"
  ],
  "body": "## Objetivo\nTarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Consolida os RFs das 4 áreas (≥16) na tabela do template, com coluna OBJETIVO; divide em sprints e escreve a justificativa da priorização (C06.6 e C06.7) depois que RFs e RNFs estiverem definidos.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5\n- `pesquisa/similares/matriz-comparativa.md`\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C06.1 ≥16 RFs (no mínimo 4 por integrante, sem máximo; ADR-0001).\n- [ ] C06.2 Enumeração sequencial e sem lacunas no documento final: RF001, RF002…. Durante a escrita vale o ID provisório por área (RF-A1, RF-A2…), em sequência dentro da área; a…\n- [ ] C06.3 Cada RF está redigido de forma clara e testável: uma ação verificável, sem \"etc.\" e sem termos vagos.\n- [ ] C06.4 Cada RF é rastreado a um ator (coluna preenchida, com ator do item 5).\n- [ ] C06.5 Cada RF é rastreado a um objetivo do item 1, na coluna OBJETIVO acrescentada à tabela do template.\n- [ ] C06.6 A priorização está presente: coluna SPRINT preenchida e/ou prioridade. A coluna fica vazia enquanto as áreas escrevem; o grupo divide em sprints na consolidação…\n- [ ] C06.7 Há uma breve justificativa da priorização.\n- [ ] C06.8 Os RFs cobrem o núcleo do produto: cadastro de curso, módulos, aulas e quiz com gabarito; matrícula, progresso e avaliação do curso; correção automática do quiz;…\n- [ ] C06.9 Nenhum RF descreve atributo de qualidade (desempenho, segurança, usabilidade etc.): isso é RNF e vai para o item 8. O RF descreve o que o sistema faz (plano de…\n\n## Dependências\n- Bloqueada por: {{T03}}, {{T05}}\n- Bloqueia: {{T07}}, {{T09}}, {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T07",
  "title": "[RA1][Item 07] Relação de Estórias de Usuário (≥16 estórias)",
  "labels": [
   "ra1",
   "item-07",
   "tarefa-mae"
  ],
  "parent": null,
  "blocked_by": [
   "T06"
  ],
  "body": "## Objetivo\nTarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Confere uma estória por RF e ≥2 critérios DADO QUE / QUANDO / ENTÃO por estória.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- RFs da área (item 6)\n- ADR-0001, ADR-0002\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C07.1 ≥16 estórias (no mínimo 4 por integrante e sempre uma por RF; ADR-0001).\n- [ ] C07.2 Todas no formato COMO / POSSO / PARA.\n- [ ] C07.3 Cada estória está vinculada a um RF correspondente, com o número do RF no título. Durante a escrita, a estória usa o ID provisório com o mesmo número do RF (US-A1 ↔…\n- [ ] C07.4 Cada estória tem ≥2 critérios de aceite.\n- [ ] C07.5 Todos os critérios estão no formato DADO QUE / QUANDO / ENTÃO, claros e verificáveis, com resultado observável.\n- [ ] C07.6 Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário.\n- [ ] C07.7 As estórias são consistentes com as outras especificações: atores, RFs e casos de uso.\n\n## Dependências\n- Bloqueada por: {{T06}}\n- Bloqueia: {{T10}}, {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T08",
  "title": "[RA1][Item 08] Relação de Requisitos Não Funcionais (≥16 RNFs)",
  "labels": [
   "ra1",
   "item-08",
   "tarefa-mae"
  ],
  "parent": null,
  "blocked_by": [
   "T03"
  ],
  "body": "## Objetivo\nTarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Consolida os RNFs (≥16), classificados na ISO/IEC 25010 e com métrica; confere a cobertura das características (C08.5). Pode correr em paralelo com T06 e T07.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- RFs da área (item 6, se já existirem)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C08.1 ≥16 RNFs (no mínimo 4 por integrante, sem máximo; ADR-0001).\n- [ ] C08.2 Enumeração RNF001, RNF002… no documento final. Durante a escrita vale o ID provisório por área (RNF-A1, RNF-A2…); a renumeração única é aplicada no início do T12…\n- [ ] C08.3 Cada RNF está classificado em uma característica da ISO/IEC 25010.\n- [ ] C08.4 Cada RNF é mensurável, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de \"ser rápido\" ou \"ser seguro\".\n- [ ] C08.5 Os RNFs das quatro áreas somados cobrem, no mínimo, eficiência de desempenho, segurança/LGPD, confiabilidade, capacidade de interação (usabilidade) e…\n- [ ] C08.6 Nenhum RNF descreve funcionalidade (ação do sistema ou do ator): isso é RF e vai para o item 6 (plano de ensino, ID1.3).\n\n## Dependências\n- Bloqueada por: {{T03}}\n- Bloqueia: {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T09",
  "title": "[RA1][Item 09] Diagrama Geral de Casos de Uso",
  "labels": [
   "ra1",
   "item-09"
  ],
  "parent": null,
  "blocked_by": [
   "T04",
   "T06"
  ],
  "body": "## Objetivo\nUm único diagrama Mermaid com todos os casos de uso (≥16), montado a partir dos RFs das 4 áreas, com generalização de atores e `include`/`extend` (seta do caso base para o estendido, ADR-0003). Todo RF coberto por ao menos um caso de uso (K.3).\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seções 2 e 5\n- ADR-0003, ADR-0004, ADR-0005\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C09.1 Tem fronteira do sistema com o nome do produto.\n- [ ] C09.2 Os atores estão corretos e são os mesmos do item 5.\n- [ ] C09.3 Os casos de uso principais correspondem aos RFs (≈ RF).\n- [ ] C09.4 Tem generalização de atores onde fizer sentido, como o template pede.\n- [ ] C09.5 Tem relacionamentos include/extend onde forem pertinentes, com a direção correta das setas: o «extend» segue o sentido do material da disciplina (TE3_3), com a seta…\n- [ ] C09.6 Os nomes dos casos de uso são consistentes com os RFs e as estórias.\n- [ ] C09.7 O diagrama é legível.\n- [ ] C09.8 Há ≥16 casos de uso no diagrama, número que permite uma especificação (item 10) por caso de uso (C10.1).\n\n## Dependências\n- Bloqueada por: {{T04}}, {{T06}}\n- Bloqueia: {{T10}}, {{T12}}, {{T10a}}, {{T10b}}, {{T10c}}, {{T10d}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T10",
  "title": "[RA1][Item 10] Especificações de Caso de Uso (≥16 especificações)",
  "labels": [
   "ra1",
   "item-10",
   "tarefa-mae"
  ],
  "parent": null,
  "blocked_by": [
   "T07",
   "T09"
  ],
  "body": "## Objetivo\nTarefa-mãe de consolidação. Começa pela conferência cruzada das issues `pendencia-cruzada` do item. Confere os campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção em todas as especificações.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- Item 9 (diagrama) e item 7 (estórias)\n- ADR-0001, ADR-0003, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C10.1 ≥16 especificações (no mínimo 4 por integrante × 4 integrantes, sem máximo; ADR-0001). Decisão fechada pelo grupo; o \"mínimo 8\" do plano de ensino não se aplica.\n- [ ] C10.2 Cada especificação tem os 10 campos preenchidos.\n- [ ] C10.3 Cada especificação tem protótipo(s) de tela de alta fidelidade.\n- [ ] C10.4 Cada especificação tem fluxo básico completo, em passos numerados.\n- [ ] C10.5 Cada especificação tem ao menos um fluxo alternativo (variação intencional do ator).\n- [ ] C10.6 Cada especificação tem ao menos um fluxo de exceção (variação não intencional ou erro).\n- [ ] C10.7 A linguagem é testável: cada passo é observável.\n- [ ] C10.8 Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores.\n- [ ] C10.9 As regras de negócio são coerentes com as estórias e os RFs.\n\n## Dependências\n- Bloqueada por: {{T07}}, {{T09}}\n- Bloqueia: {{T11}}, {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T11",
  "title": "[RA1][Item 11] Diagrama de Atividades",
  "labels": [
   "ra1",
   "item-11"
  ],
  "parent": null,
  "blocked_by": [
   "T10"
  ],
  "body": "## Objetivo\nDiagrama de atividades UML em Mermaid, com raias dos atores, decisões com guarda e fork/join (ex.: Aluno assiste à aula enquanto o Tutor de IA fica disponível).\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- Item 10 (especificações)\n- ADR-0004\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C11.1 Representa o fluxo principal.\n- [ ] C11.2 Representa os fluxos alternativos.\n- [ ] C11.3 Tem decisões com condições de guarda escritas.\n- [ ] C11.4 Tem atividades paralelas (fork/join) onde houver ramos concorrentes, por exemplo o Aluno assistir à aula enquanto o Tutor de IA está disponível para dúvidas.\n- [ ] C11.5 Tem responsabilidades (partições/raias) coerentes com os atores.\n- [ ] C11.6 A notação UML é usada corretamente: nó inicial e final, ações, decisão/merge, fork/join.\n- [ ] C11.7 É legível e aderente à documentação (atores, casos de uso, BPMN).\n\n## Dependências\n- Bloqueada por: {{T10}}\n- Bloqueia: {{T12}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T12",
  "title": "[RA1][Geral] Revisão cruzada e verificação independente",
  "labels": [
   "ra1",
   "geral"
  ],
  "parent": null,
  "blocked_by": [
   "T01",
   "T02",
   "T03",
   "T04",
   "T05",
   "T06",
   "T07",
   "T08",
   "T09",
   "T10",
   "T11"
  ],
  "body": "## Objetivo\nPrimeiro, aplicar a renumeração única (RF-A1… para RF001…, US-A1… para US001…, RNF-A1… para RNF001…, UC-A1… para UC001…; ADR-0001), atualizar as referências cruzadas e registrar a correspondência em `entregas/ra1-renumeracao.md`. Depois, com todos os MDs na `main`, executar o checklist K.1 a K.13 e a verificação independente de todos os IDs (seção 0.3, passo 6), produzindo a tabela `ID | status | evidência`. Corrigir ou devolver aos responsáveis o que não passar.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `entregas/ra1-criterios-de-aceite.md` seções 0.3 e 5\n- ADR-0001\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] K.1 Os mesmos atores (nomes idênticos) aparecem nos itens 4, 5, 6, 7, 9, 10 e 11.\n- [ ] K.2 Todo RF (item 6) tem exatamente uma estória (item 7) e toda estória aponta para um RF existente.\n- [ ] K.3 Todo RF está coberto por pelo menos um caso de uso no diagrama (item 9).\n- [ ] K.4 Toda especificação (item 10) corresponde a um caso de uso do diagrama (item 9), com o mesmo nome.\n- [ ] K.5 Os critérios de aceite das estórias não contradizem as regras de negócio nem os fluxos das especificações do mesmo requisito.\n- [ ] K.6 Os objetivos (item 1) são atendidos por algum RF e aparecem refletidos na Visão (item 3).\n- [ ] K.7 Nada listado em \"Não faz\" (item 2) aparece como RF, estória ou caso de uso.\n- [ ] K.8 As lanes do BPMN (item 4) e as raias do diagrama de atividades (item 11) usam os atores do item 5.\n- [ ] K.9 As contagens mínimas conferem por contagem real: RF ≥16, estórias ≥16, cada estória com ≥2 critérios, RNF ≥16, casos de uso no diagrama ≥16, especificações ≥16.\n- [ ] K.10 Todos os critérios gerais X.1 a X.10 estão atendidos.\n- [ ] K.11 Nenhum item contradiz o `CONTEXT.md` nem as decisões D1–D6 (`docs/adr/`), e todo número, preço ou recurso de concorrente usado na especificação cita a fonte da…\n- [ ] K.12 Não há issue aberta com o rótulo `pendencia-cruzada`: toda amarração entre áreas foi resolvida, com o ID do requisito que a atende ou com a decisão do grupo…\n- [ ] K.13 A renumeração única foi aplicada (RF001…, US001…, RNF001…, UC001…), não restou ID provisório (`-A1`, `-B2`…) em nenhum arquivo e `entregas/ra1-renumeracao.md` lista a…\n- [ ] X.8 Regra dos 4 por integrante. Nos itens que dependem da quantidade de integrantes, o mínimo é 4 itens por integrante, sem máximo. Com 4 integrantes, o mínimo é 16…\n\n## Dependências\n- Bloqueada por: {{T01}}, {{T02}}, {{T03}}, {{T04}}, {{T05}}, {{T06}}, {{T07}}, {{T08}}, {{T09}}, {{T10}}, {{T11}}\n- Bloqueia: {{T13}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T13",
  "title": "[RA1][Geral] Consolidar em PDF e DOCX e enviar no Canvas",
  "labels": [
   "ra1",
   "geral"
  ],
  "parent": null,
  "blocked_by": [
   "T12"
  ],
  "body": "## Objetivo\nConsolidar os MDs em um único documento no formato do template (capa com Plataforma de Cursos, os 4 autores e 2026; sumário; seções 1 a 11 na ordem; diagramas legíveis), incluir a declaração de uso de IA preenchida, exportar em PDF e DOCX e enviar na tarefa \"Avaliação do RA 1 - Projeto\" até 10/10/2026, 23:59.\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `entregas/ra1-criterios-de-aceite.md` seções 2 e 6\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] X.1 Template. O documento final (PDF consolidado a partir dos MDs do repositório) segue a estrutura do template oficial: seções na ordem de 1 a 11, títulos originais e…\n- [ ] X.2 Capa. Nome do produto (Plataforma de Cursos) no lugar de \"NOME DO PRODUTO DE SOFTWARE\", os 4 autores no lugar de \"NOME AUTOR 1..4\" e ano 2026 (o template traz 2025).\n- [ ] X.3 Textos em azul. Todos os textos personalizáveis (em azul) foram substituídos e estão na cor preta.\n- [ ] X.4 Textos em laranja. Todos os quadros de aviso e textos de orientação em laranja foram removidos.\n- [ ] X.5 Exemplos do template. Os exemplos do template foram removidos ou substituídos, por exemplo RF1 \"Realizar login de usuário\" com o ator genérico e as estórias…\n- [ ] X.6 Sumário. O sumário está atualizado, com números de página corretos.\n- [ ] X.7 Declaração de uso de IA. O documento contém a declaração obrigatória (plano de ensino, seção 7.1): *\"Durante a preparação deste [TIPO DE CONTEÚDO], o(s) autor(es)…\n- [ ] X.9 Nome do produto. O nome Plataforma de Cursos (exatamente assim) aparece em todos os campos \"NOME DO PRODUTO\" / \"PRODUTO\" dos quadros.\n- [ ] X.10 Legibilidade dos diagramas. Os diagramas (itens 4, 9 e 11) estão legíveis no documento final, sem texto cortado ou ilegível. As imagens são geradas a partir do…\n\n## Dependências\n- Bloqueada por: {{T12}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T06a",
  "title": "[RA1][Item 06] RFs da área A (Acesso e conta)",
  "labels": [
   "ra1",
   "item-06",
   "por-integrante",
   "area-a"
  ],
  "parent": "T06",
  "blocked_by": [
   "T03",
   "T05"
  ],
  "body": "## Objetivo\nEscrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-A1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área A)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C06.2 Enumeração sequencial e sem lacunas no documento final: RF001, RF002…. Durante a escrita vale o ID provisório por área (RF-A1, RF-A2…), em sequência dentro da área; a…\n- [ ] C06.3 Cada RF está redigido de forma clara e testável: uma ação verificável, sem \"etc.\" e sem termos vagos.\n- [ ] C06.4 Cada RF é rastreado a um ator (coluna preenchida, com ator do item 5).\n- [ ] C06.5 Cada RF é rastreado a um objetivo do item 1, na coluna OBJETIVO acrescentada à tabela do template.\n- [ ] C06.9 Nenhum RF descreve atributo de qualidade (desempenho, segurança, usabilidade etc.): isso é RNF e vai para o item 8. O RF descreve o que o sistema faz (plano de…\n\n## Dependências\n- Bloqueada por: {{T03}}, {{T05}}\n- Bloqueia: {{T07a}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T06b",
  "title": "[RA1][Item 06] RFs da área B (Autoria do instrutor)",
  "labels": [
   "ra1",
   "item-06",
   "por-integrante",
   "area-b"
  ],
  "parent": "T06",
  "blocked_by": [
   "T03",
   "T05"
  ],
  "body": "## Objetivo\nEscrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-B1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área B)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C06.2 Enumeração sequencial e sem lacunas no documento final: RF001, RF002…. Durante a escrita vale o ID provisório por área (RF-A1, RF-A2…), em sequência dentro da área; a…\n- [ ] C06.3 Cada RF está redigido de forma clara e testável: uma ação verificável, sem \"etc.\" e sem termos vagos.\n- [ ] C06.4 Cada RF é rastreado a um ator (coluna preenchida, com ator do item 5).\n- [ ] C06.5 Cada RF é rastreado a um objetivo do item 1, na coluna OBJETIVO acrescentada à tabela do template.\n- [ ] C06.9 Nenhum RF descreve atributo de qualidade (desempenho, segurança, usabilidade etc.): isso é RNF e vai para o item 8. O RF descreve o que o sistema faz (plano de…\n\n## Dependências\n- Bloqueada por: {{T03}}, {{T05}}\n- Bloqueia: {{T07b}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T06c",
  "title": "[RA1][Item 06] RFs da área C (Aprendizagem do aluno)",
  "labels": [
   "ra1",
   "item-06",
   "por-integrante",
   "area-c"
  ],
  "parent": "T06",
  "blocked_by": [
   "T03",
   "T05"
  ],
  "body": "## Objetivo\nEscrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-C1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área C)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C06.2 Enumeração sequencial e sem lacunas no documento final: RF001, RF002…. Durante a escrita vale o ID provisório por área (RF-A1, RF-A2…), em sequência dentro da área; a…\n- [ ] C06.3 Cada RF está redigido de forma clara e testável: uma ação verificável, sem \"etc.\" e sem termos vagos.\n- [ ] C06.4 Cada RF é rastreado a um ator (coluna preenchida, com ator do item 5).\n- [ ] C06.5 Cada RF é rastreado a um objetivo do item 1, na coluna OBJETIVO acrescentada à tabela do template.\n- [ ] C06.9 Nenhum RF descreve atributo de qualidade (desempenho, segurança, usabilidade etc.): isso é RNF e vai para o item 8. O RF descreve o que o sistema faz (plano de…\n\n## Dependências\n- Bloqueada por: {{T03}}, {{T05}}\n- Bloqueia: {{T07c}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T06d",
  "title": "[RA1][Item 06] RFs da área D (Tutor de IA, analytics e administração)",
  "labels": [
   "ra1",
   "item-06",
   "por-integrante",
   "area-d"
  ],
  "parent": "T06",
  "blocked_by": [
   "T03",
   "T05"
  ],
  "body": "## Objetivo\nEscrever os RFs da área (mínimo 4, sem máximo), tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | OBJETIVO | SPRINT`, com SPRINT vazia (decidida em T06). IDs provisórios: RF-D1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área D)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C06.2 Enumeração sequencial e sem lacunas no documento final: RF001, RF002…. Durante a escrita vale o ID provisório por área (RF-A1, RF-A2…), em sequência dentro da área; a…\n- [ ] C06.3 Cada RF está redigido de forma clara e testável: uma ação verificável, sem \"etc.\" e sem termos vagos.\n- [ ] C06.4 Cada RF é rastreado a um ator (coluna preenchida, com ator do item 5).\n- [ ] C06.5 Cada RF é rastreado a um objetivo do item 1, na coluna OBJETIVO acrescentada à tabela do template.\n- [ ] C06.9 Nenhum RF descreve atributo de qualidade (desempenho, segurança, usabilidade etc.): isso é RNF e vai para o item 8. O RF descreve o que o sistema faz (plano de…\n\n## Dependências\n- Bloqueada por: {{T03}}, {{T05}}\n- Bloqueia: {{T07d}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T07a",
  "title": "[RA1][Item 07] Estórias da área A (Acesso e conta)",
  "labels": [
   "ra1",
   "item-07",
   "por-integrante",
   "area-a"
  ],
  "parent": "T07",
  "blocked_by": [
   "T06a"
  ],
  "body": "## Objetivo\nEscrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-A1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área A)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C07.2 Todas no formato COMO / POSSO / PARA.\n- [ ] C07.3 Cada estória está vinculada a um RF correspondente, com o número do RF no título. Durante a escrita, a estória usa o ID provisório com o mesmo número do RF (US-A1 ↔…\n- [ ] C07.4 Cada estória tem ≥2 critérios de aceite.\n- [ ] C07.5 Todos os critérios estão no formato DADO QUE / QUANDO / ENTÃO, claros e verificáveis, com resultado observável.\n- [ ] C07.6 Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário.\n- [ ] C07.7 As estórias são consistentes com as outras especificações: atores, RFs e casos de uso.\n\n## Dependências\n- Bloqueada por: {{T06a}}\n- Bloqueia: {{T10a}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T07b",
  "title": "[RA1][Item 07] Estórias da área B (Autoria do instrutor)",
  "labels": [
   "ra1",
   "item-07",
   "por-integrante",
   "area-b"
  ],
  "parent": "T07",
  "blocked_by": [
   "T06b"
  ],
  "body": "## Objetivo\nEscrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-B1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área B)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C07.2 Todas no formato COMO / POSSO / PARA.\n- [ ] C07.3 Cada estória está vinculada a um RF correspondente, com o número do RF no título. Durante a escrita, a estória usa o ID provisório com o mesmo número do RF (US-A1 ↔…\n- [ ] C07.4 Cada estória tem ≥2 critérios de aceite.\n- [ ] C07.5 Todos os critérios estão no formato DADO QUE / QUANDO / ENTÃO, claros e verificáveis, com resultado observável.\n- [ ] C07.6 Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário.\n- [ ] C07.7 As estórias são consistentes com as outras especificações: atores, RFs e casos de uso.\n\n## Dependências\n- Bloqueada por: {{T06b}}\n- Bloqueia: {{T10b}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T07c",
  "title": "[RA1][Item 07] Estórias da área C (Aprendizagem do aluno)",
  "labels": [
   "ra1",
   "item-07",
   "por-integrante",
   "area-c"
  ],
  "parent": "T07",
  "blocked_by": [
   "T06c"
  ],
  "body": "## Objetivo\nEscrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-C1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área C)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C07.2 Todas no formato COMO / POSSO / PARA.\n- [ ] C07.3 Cada estória está vinculada a um RF correspondente, com o número do RF no título. Durante a escrita, a estória usa o ID provisório com o mesmo número do RF (US-A1 ↔…\n- [ ] C07.4 Cada estória tem ≥2 critérios de aceite.\n- [ ] C07.5 Todos os critérios estão no formato DADO QUE / QUANDO / ENTÃO, claros e verificáveis, com resultado observável.\n- [ ] C07.6 Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário.\n- [ ] C07.7 As estórias são consistentes com as outras especificações: atores, RFs e casos de uso.\n\n## Dependências\n- Bloqueada por: {{T06c}}\n- Bloqueia: {{T10c}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T07d",
  "title": "[RA1][Item 07] Estórias da área D (Tutor de IA, analytics e administração)",
  "labels": [
   "ra1",
   "item-07",
   "por-integrante",
   "area-d"
  ],
  "parent": "T07",
  "blocked_by": [
   "T06d"
  ],
  "body": "## Objetivo\nEscrever uma estória por RF da área, no formato COMO / POSSO / PARA, com ≥2 critérios DADO QUE / QUANDO / ENTÃO cada (ADR-0002). IDs provisórios: US-D1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área D)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C07.2 Todas no formato COMO / POSSO / PARA.\n- [ ] C07.3 Cada estória está vinculada a um RF correspondente, com o número do RF no título. Durante a escrita, a estória usa o ID provisório com o mesmo número do RF (US-A1 ↔…\n- [ ] C07.4 Cada estória tem ≥2 critérios de aceite.\n- [ ] C07.5 Todos os critérios estão no formato DADO QUE / QUANDO / ENTÃO, claros e verificáveis, com resultado observável.\n- [ ] C07.6 Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário.\n- [ ] C07.7 As estórias são consistentes com as outras especificações: atores, RFs e casos de uso.\n\n## Dependências\n- Bloqueada por: {{T06d}}\n- Bloqueia: {{T10d}}\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T08a",
  "title": "[RA1][Item 08] RNFs da área A (Acesso e conta)",
  "labels": [
   "ra1",
   "item-08",
   "por-integrante",
   "area-a"
  ],
  "parent": "T08",
  "blocked_by": [
   "T03"
  ],
  "body": "## Objetivo\nEscrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (segurança (LGPD) e compatibilidade) e com métrica mensurável. IDs provisórios: RNF-A1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área A)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C08.2 Enumeração RNF001, RNF002… no documento final. Durante a escrita vale o ID provisório por área (RNF-A1, RNF-A2…); a renumeração única é aplicada no início do T12…\n- [ ] C08.3 Cada RNF está classificado em uma característica da ISO/IEC 25010.\n- [ ] C08.4 Cada RNF é mensurável, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de \"ser rápido\" ou \"ser seguro\".\n- [ ] C08.6 Nenhum RNF descreve funcionalidade (ação do sistema ou do ator): isso é RF e vai para o item 6 (plano de ensino, ID1.3).\n\n## Dependências\n- Bloqueada por: {{T03}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T08b",
  "title": "[RA1][Item 08] RNFs da área B (Autoria do instrutor)",
  "labels": [
   "ra1",
   "item-08",
   "por-integrante",
   "area-b"
  ],
  "parent": "T08",
  "blocked_by": [
   "T03"
  ],
  "body": "## Objetivo\nEscrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (manutenibilidade e portabilidade) e com métrica mensurável. IDs provisórios: RNF-B1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área B)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C08.2 Enumeração RNF001, RNF002… no documento final. Durante a escrita vale o ID provisório por área (RNF-A1, RNF-A2…); a renumeração única é aplicada no início do T12…\n- [ ] C08.3 Cada RNF está classificado em uma característica da ISO/IEC 25010.\n- [ ] C08.4 Cada RNF é mensurável, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de \"ser rápido\" ou \"ser seguro\".\n- [ ] C08.6 Nenhum RNF descreve funcionalidade (ação do sistema ou do ator): isso é RF e vai para o item 6 (plano de ensino, ID1.3).\n\n## Dependências\n- Bloqueada por: {{T03}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T08c",
  "title": "[RA1][Item 08] RNFs da área C (Aprendizagem do aluno)",
  "labels": [
   "ra1",
   "item-08",
   "por-integrante",
   "area-c"
  ],
  "parent": "T08",
  "blocked_by": [
   "T03"
  ],
  "body": "## Objetivo\nEscrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (capacidade de interação e acessibilidade) e com métrica mensurável. IDs provisórios: RNF-C1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área C)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C08.2 Enumeração RNF001, RNF002… no documento final. Durante a escrita vale o ID provisório por área (RNF-A1, RNF-A2…); a renumeração única é aplicada no início do T12…\n- [ ] C08.3 Cada RNF está classificado em uma característica da ISO/IEC 25010.\n- [ ] C08.4 Cada RNF é mensurável, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de \"ser rápido\" ou \"ser seguro\".\n- [ ] C08.6 Nenhum RNF descreve funcionalidade (ação do sistema ou do ator): isso é RF e vai para o item 6 (plano de ensino, ID1.3).\n\n## Dependências\n- Bloqueada por: {{T03}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T08d",
  "title": "[RA1][Item 08] RNFs da área D (Tutor de IA, analytics e administração)",
  "labels": [
   "ra1",
   "item-08",
   "por-integrante",
   "area-d"
  ],
  "parent": "T08",
  "blocked_by": [
   "T03"
  ],
  "body": "## Objetivo\nEscrever os RNFs da área (mínimo 4, sem máximo), classificados na ISO/IEC 25010 (eficiência de desempenho e confiabilidade) e com métrica mensurável. IDs provisórios: RNF-D1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área D)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C08.2 Enumeração RNF001, RNF002… no documento final. Durante a escrita vale o ID provisório por área (RNF-A1, RNF-A2…); a renumeração única é aplicada no início do T12…\n- [ ] C08.3 Cada RNF está classificado em uma característica da ISO/IEC 25010.\n- [ ] C08.4 Cada RNF é mensurável, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de \"ser rápido\" ou \"ser seguro\".\n- [ ] C08.6 Nenhum RNF descreve funcionalidade (ação do sistema ou do ator): isso é RF e vai para o item 6 (plano de ensino, ID1.3).\n\n## Dependências\n- Bloqueada por: {{T03}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T10a",
  "title": "[RA1][Item 10] Especificações de caso de uso da área A (Acesso e conta)",
  "labels": [
   "ra1",
   "item-10",
   "por-integrante",
   "area-a"
  ],
  "parent": "T10",
  "blocked_by": [
   "T07a",
   "T09"
  ],
  "body": "## Objetivo\nEscrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-A1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área A)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C10.2 Cada especificação tem os 10 campos preenchidos.\n- [ ] C10.3 Cada especificação tem protótipo(s) de tela de alta fidelidade.\n- [ ] C10.4 Cada especificação tem fluxo básico completo, em passos numerados.\n- [ ] C10.5 Cada especificação tem ao menos um fluxo alternativo (variação intencional do ator).\n- [ ] C10.6 Cada especificação tem ao menos um fluxo de exceção (variação não intencional ou erro).\n- [ ] C10.7 A linguagem é testável: cada passo é observável.\n- [ ] C10.8 Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores.\n- [ ] C10.9 As regras de negócio são coerentes com as estórias e os RFs.\n\n## Dependências\n- Bloqueada por: {{T07a}}, {{T09}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T10b",
  "title": "[RA1][Item 10] Especificações de caso de uso da área B (Autoria do instrutor)",
  "labels": [
   "ra1",
   "item-10",
   "por-integrante",
   "area-b"
  ],
  "parent": "T10",
  "blocked_by": [
   "T07b",
   "T09"
  ],
  "body": "## Objetivo\nEscrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-B1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área B)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C10.2 Cada especificação tem os 10 campos preenchidos.\n- [ ] C10.3 Cada especificação tem protótipo(s) de tela de alta fidelidade.\n- [ ] C10.4 Cada especificação tem fluxo básico completo, em passos numerados.\n- [ ] C10.5 Cada especificação tem ao menos um fluxo alternativo (variação intencional do ator).\n- [ ] C10.6 Cada especificação tem ao menos um fluxo de exceção (variação não intencional ou erro).\n- [ ] C10.7 A linguagem é testável: cada passo é observável.\n- [ ] C10.8 Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores.\n- [ ] C10.9 As regras de negócio são coerentes com as estórias e os RFs.\n\n## Dependências\n- Bloqueada por: {{T07b}}, {{T09}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T10c",
  "title": "[RA1][Item 10] Especificações de caso de uso da área C (Aprendizagem do aluno)",
  "labels": [
   "ra1",
   "item-10",
   "por-integrante",
   "area-c"
  ],
  "parent": "T10",
  "blocked_by": [
   "T07c",
   "T09"
  ],
  "body": "## Objetivo\nEscrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-C1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área C)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C10.2 Cada especificação tem os 10 campos preenchidos.\n- [ ] C10.3 Cada especificação tem protótipo(s) de tela de alta fidelidade.\n- [ ] C10.4 Cada especificação tem fluxo básico completo, em passos numerados.\n- [ ] C10.5 Cada especificação tem ao menos um fluxo alternativo (variação intencional do ator).\n- [ ] C10.6 Cada especificação tem ao menos um fluxo de exceção (variação não intencional ou erro).\n- [ ] C10.7 A linguagem é testável: cada passo é observável.\n- [ ] C10.8 Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores.\n- [ ] C10.9 As regras de negócio são coerentes com as estórias e os RFs.\n\n## Dependências\n- Bloqueada por: {{T07c}}, {{T09}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 },
 {
  "id": "T10d",
  "title": "[RA1][Item 10] Especificações de caso de uso da área D (Tutor de IA, analytics e administração)",
  "labels": [
   "ra1",
   "item-10",
   "por-integrante",
   "area-d"
  ],
  "parent": "T10",
  "blocked_by": [
   "T07d",
   "T09"
  ],
  "body": "## Objetivo\nEscrever as especificações da área (mínimo 4, sem máximo; uma por caso de uso do item 9), com os 10 campos, protótipos de alta fidelidade e fluxos básico, alternativo e de exceção. IDs provisórios: UC-D1….\n\n## Insumos obrigatórios\n- Ler `CONTEXT.md` antes de começar.\n- `CONTEXT.md` seção 5 (linha da área D)\n- ADR-0001, ADR-0006\n\n## Critérios de aceite\nReferência: `entregas/ra1-criterios-de-aceite.md`\n- [ ] C10.2 Cada especificação tem os 10 campos preenchidos.\n- [ ] C10.3 Cada especificação tem protótipo(s) de tela de alta fidelidade.\n- [ ] C10.4 Cada especificação tem fluxo básico completo, em passos numerados.\n- [ ] C10.5 Cada especificação tem ao menos um fluxo alternativo (variação intencional do ator).\n- [ ] C10.6 Cada especificação tem ao menos um fluxo de exceção (variação não intencional ou erro).\n- [ ] C10.7 A linguagem é testável: cada passo é observável.\n- [ ] C10.8 Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores.\n- [ ] C10.9 As regras de negócio são coerentes com as estórias e os RFs.\n\n## Dependências\n- Bloqueada por: {{T07d}}, {{T09}}\n- Bloqueia: nenhuma\n\n## Definição de pronto\n- Trabalho em branch própria (`feat/` ou `fix/`), em arquivo(s) MD do repositório; diagramas como código com fonte versionada.\n- Todos os critérios acima marcados, cada um com evidência (arquivo e seção, quantidade contada).\n- Dúvida sobre outra área: registrar na issue `pendencia-cruzada` da área, sem inventar o requisito dela.\n- Pull request para a `main`, card em **In review**; outro integrante revisa. **Done** só após o merge."
 }
]
```

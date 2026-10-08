---
id: pendencias-revisao
titulo: "Inventário de Pendências para Revisão do Grupo"
tipo: processo
status: rascunho
atualizado: 2026-10-07
origem: v11.md + repo grep + _lacunas.md
relacionados: [ra1-criterios-de-aceite, ra1-tarefas, contexto, adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006]
---

# Inventário de Pendências para Revisão do Grupo

> Este documento consolida todo comentário `<!-- revisar ... -->` identificado no repositório (`especificacao/`, `docs/`, `entregas/`), as lacunas de ingestão registradas em `_lacunas.md` e as pendências de casos de teste da v11.
> Cada item foi analisado frente à versão base **v11** (texto e diagramas visuais), às **ADRs** vigentes e ao **CONTEXT.md**.
>
> **Classificação:**
> - **(M) Mecânico:** resolvível diretamente com base na v11 ou em regra mecânica já estabelecida nas decisões, sem necessidade de deliberação ou julgamento do grupo.
> - **(G) Grupo:** requer decisão do grupo (definição de escopo, resolução de conflito com ADR/template, criação de conteúdo ausente na v11, preenchimento de dados pessoais/individuais).

---

## 1. Resumo Quantitativo

| Categoria | Tipo M (Mecânico) | Tipo G (Decisão do Grupo) | Total |
|---|:---:|:---:|:---:|
| Comentários `<!-- revisar ... -->` mapeados | 14 | 28 | 42 |
| Lacunas de Ingestão (`_lacunas.md`), Testes e Modelo | 0 | 6 | 6 |
| **Total Consolidado de Itens** | **14** | **34** | **48** |

---

## 2. Inventário Completo de Ocorrências `<!-- revisar -->`

A tabela abaixo lista todas as 42 ocorrências encontradas no repositório, com a classificação **M/G** e a sugestão de responsável conforme a área (A–D) definida no `CONTEXT.md` (seção 5) e `README.md`:
- **Área A (Acesso e conta):** Lucas Stopinski da Silva (`LucasStop`)
- **Área B (Autoria do instrutor):** Adrian Antônio de Souza Gomes (`adrian69-droid`)
- **Área C (Aprendizagem do aluno):** Lucas Bruno e Silva (`Luc-Bruno`)
- **Área D (Tutor de IA, analytics e administração):** Vinicius Lima Teider (`Teider011`)
- **Grupo:** Transversal / Todos os integrantes

| # | Arquivo | Linha | Pendência / Texto da Marcação | Tipo | Responsável Sugerido | Justificativa / Encaminhamento |
|---|---|:---:|---|:---:|:---:|---|
| 1 | `especificacao/01-3-objetivos.md` | 13 | v11 não separa "Problema" e "Valor" por objetivo (o esqueleto pede); texto mantido como na v11, sem inventar (template do RA1) | **G** | Grupo | Decidir se mantém o texto consolidado em parágrafo único (v11) ou se divide em campos explícitos de Problema e Valor. |
| 2 | `especificacao/04-mapeamento-de-negocios.md` | 17 | v11 traz o diagrama em Mermaid (flowchart com raias), não em .bpmn; o esqueleto cita .bpmn (ADR 0004 aceita as duas formas) | **M** | Grupo | ADR 0004 aceita Mermaid e BPMN 2.0; o Mermaid já está transcrito e funcional da v11. |
| 3 | `especificacao/06-requisitos-funcionais/area-a.md` | 12 | O esqueleto pede a coluna OBJETIVO; a v11 traz UC, PRIORIDADE e JUSTIFICATIVA e não traz OBJETIVO. Colunas da v11 mantidas, sem inventar objetivo (ADR 0001) | **G** | Área A (`LucasStop`) | Decidir se adiciona mapeamento formal ao objetivo de negócio (1, 2 ou 3) na tabela de RFs. |
| 4 | `especificacao/06-requisitos-funcionais/area-a.md` | 14 | Área A com 2 RFs, abaixo do mínimo de 4 (ADR 0001); ver `_lacunas.md` | **G** | Área A (`LucasStop`) | Decidir quais 2 novos RFs serão incorporados à Área A (ver propostas em `entregas/propostas-lacunas.md`). |
| 5 | `especificacao/06-requisitos-funcionais/area-b.md` | 15 | O esqueleto pede a coluna OBJETIVO; a v11 traz UC, PRIORIDADE e JUSTIFICATIVA e não traz OBJETIVO. Colunas da v11 mantidas, sem inventar objetivo (ADR 0001) | **G** | Área B (`adrian69-droid`) | Decidir se inclui coluna de objetivo vinculado (Objetivo 1). |
| 6 | `especificacao/06-requisitos-funcionais/area-b.md` | 17 | RF-B5 (RF016) não tem UC na v11 ("Sem UC (lacuna)"); alocado à área B por escopo (ADR 0006). | **G** | Área B (`adrian69-droid`) | Decidir se especifica um UC dedicado para "Gerenciar perfil do instrutor" ou se o associa a UC existente. |
| 7 | `especificacao/06-requisitos-funcionais/area-c.md` | 16 | O esqueleto pede a coluna OBJETIVO; a v11 traz UC, PRIORIDADE e JUSTIFICATIVA e não traz OBJETIVO. Colunas da v11 mantidas, sem inventar objetivo (ADR 0001) | **G** | Área C (`Luc-Bruno`) | Decidir se inclui coluna de objetivo vinculado (Objetivo 2). |
| 8 | `especificacao/06-requisitos-funcionais/area-c.md` | 18 | RF-C6 (RF015) não tem UC na v11 ("Sem UC (lacuna)"); alocado à área C por escopo (ADR 0006). | **G** | Área C (`Luc-Bruno`) | Decidir se cria especificação de UC para consulta e busca de cursos no catálogo. |
| 9 | `especificacao/06-requisitos-funcionais/area-d.md` | 13 | O esqueleto pede a coluna OBJETIVO; a v11 traz UC, PRIORIDADE e JUSTIFICATIVA e não traz OBJETIVO. Colunas da v11 mantidas, sem inventar objetivo (ADR 0001) | **G** | Área D (`Teider011`) | Decidir se inclui coluna de objetivo vinculado (Objetivos 2 e 3). |
| 10 | `especificacao/06-requisitos-funcionais/area-d.md` | 15 | Área D com 3 RFs, abaixo do mínimo de 4 (ADR 0001); ver `_lacunas.md` | **G** | Área D (`Teider011`) | Decidir qual 4º RF incorporar para a Área D (ver propostas em `entregas/propostas-lacunas.md`). |
| 11 | `especificacao/07-estorias-de-usuario/area-a.md` | 5 | A v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) | **G** | Área A (`LucasStop`) | Padronização sintática formal de "Quero" para "posso" conforme ADR 0002. |
| 12 | `especificacao/07-estorias-de-usuario/area-a.md` | 73 | 4 estórias para 2 RF(s) na área; a regra "mesmo número do RF" (US-An ↔ RF-An) não se aplica a US-A2, US-A3, US-A4, que têm vários por RF na v11 (ADR 0001) | **G** | Área A (`LucasStop`) | Reconciliar mapeamento 1:1 entre US e RF após decisão sobre inclusão de novos RFs. |
| 13 | `especificacao/07-estorias-de-usuario/area-b.md` | 5 | A v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) | **G** | Área B (`adrian69-droid`) | Padronização sintática formal de "Quero" para "posso" conforme ADR 0002. |
| 14 | `especificacao/07-estorias-de-usuario/area-c.md` | 5 | A v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) | **G** | Área C (`Luc-Bruno`) | Padronização sintática formal de "Quero" para "posso" conforme ADR 0002. |
| 15 | `especificacao/07-estorias-de-usuario/area-c.md` | 121 | 7 estórias para 6 RF(s) na área; a regra "mesmo número do RF" (US-Cn ↔ RF-Cn) não se aplica a US-C3, US-C4, US-C5, US-C6, US-C7 | **G** | Área C (`Luc-Bruno`) | Reconciliar correspondência de numeração entre estórias e RFs. |
| 16 | `especificacao/07-estorias-de-usuario/area-d.md` | 5 | A v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) | **G** | Área D (`Teider011`) | Padronização sintática formal de "Quero" para "posso" conforme ADR 0002. |
| 17 | `especificacao/07-estorias-de-usuario/area-d.md` | 73 | 4 estórias para 3 RF(s) na área; a regra "mesmo número do RF" (US-Dn ↔ RF-Dn) não se aplica a US-D4 | **G** | Área D (`Teider011`) | Reconciliar mapeamento entre US-D4 e RF correspondente. |
| 18 | `especificacao/08-requisitos-nao-funcionais/area-a.md` | 13 | A v11 classifica diretamente por característica da ISO/IEC 25010 sem coluna de subcaracterística; preenchido com '-' | **G** | Área A (`LucasStop`) | Decidir se preenche subcaracterísticas da ISO/IEC 25010 (ex.: Confidencialidade, Integridade). |
| 19 | `especificacao/08-requisitos-nao-funcionais/area-a.md` | 15 | Área A com 3 RNFs, abaixo do mínimo de 4 (ADR 0001); ver `_lacunas.md` | **G** | Área A (`LucasStop`) | Definir 4º RNF da Área A (ver proposta em `entregas/propostas-lacunas.md`). |
| 20 | `especificacao/08-requisitos-nao-funcionais/area-b.md` | 13 | RNF-B1 (RNF002) é requisito de segurança associado ao upload de vídeo de aula (UC015 / autoria do instrutor); alocado na área do UC | **M** | Área B (`adrian69-droid`) | Alocação correta conforme regra da ADR 0006; registro meramente informativo. |
| 21 | `especificacao/08-requisitos-nao-funcionais/area-b.md` | 15 | A v11 classifica diretamente por característica da ISO/IEC 25010 sem coluna de subcaracterística; preenchido com '-' | **G** | Área B (`adrian69-droid`) | Decidir se preenche subcaracterísticas da ISO/IEC 25010 (ex.: Modificabilidade, Testabilidade). |
| 22 | `especificacao/08-requisitos-nao-funcionais/area-b.md` | 17 | Área B com 3 RNFs, abaixo do mínimo de 4 (ADR 0001); ver `_lacunas.md` | **G** | Área B (`adrian69-droid`) | Definir 4º RNF da Área B (ver proposta em `entregas/propostas-lacunas.md`). |
| 23 | `especificacao/08-requisitos-nao-funcionais/area-c.md` | 14 | A v11 classifica diretamente por característica da ISO/IEC 25010 sem coluna de subcaracterística; preenchido com '-' | **G** | Área C (`Luc-Bruno`) | Decidir se preenche subcaracterísticas da ISO/IEC 25010 (ex.: Reconhecimento de Adequabilidade). |
| 24 | `especificacao/08-requisitos-nao-funcionais/area-d.md` | 16 | RNF-D6 (RNF016) é requisito de segurança ligado a ações administrativas (UC016 / gerenciar usuários); alocado na área do UC | **M** | Área D (`Teider011`) | Alocação correta conforme regra da ADR 0006; registro meramente informativo. |
| 25 | `especificacao/08-requisitos-nao-funcionais/area-d.md` | 18 | A v11 classifica diretamente por característica da ISO/IEC 25010 sem coluna de subcaracterística; preenchido com '-' | **G** | Área D (`Teider011`) | Decidir se preenche subcaracterísticas da ISO/IEC 25010 (ex.: Comportamento Temporal, Tolerância a Falhas). |
| 26 | `docs/ssd/UC001-conversar-com-tutor-de-ia.md` | 5 | Diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original | **M** | Área D (`Teider011`) | Tarefa de checagem visual contra Figura 15 (atribuída à tarefa `v2-a`). |
| 27 | `docs/ssd/UC002-responder-quiz.md` | 5 | Diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original | **M** | Área C (`Luc-Bruno`) | Tarefa de checagem visual contra Figura 16 (atribuída à tarefa `v2-a`). |
| 28 | `docs/ssd/UC003-matricular-se-em-curso.md` | 5 | Diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original | **M** | Área C (`Luc-Bruno`) | Tarefa de checagem visual contra Figura 17 (atribuída à tarefa `v2-a`). |
| 29 | `docs/ssd/UC004-cadastrar-quiz-com-gabarito.md` | 5 | Diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original | **M** | Área B (`adrian69-droid`) | Tarefa de checagem visual contra Figura 18 (atribuída à tarefa `v2-b`). |
| 30 | `docs/ssd/UC009-assistir-aula.md` | 5 | Diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original | **M** | Área C (`Luc-Bruno`) | Tarefa de checagem visual contra Figura 23 (atribuída à tarefa `v2-b`). |
| 31 | `docs/ssd/UC010-avaliar-curso.md` | 5 | Diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original | **M** | Área C (`Luc-Bruno`) | Tarefa de checagem visual contra Figura 24 (atribuída à tarefa `v2-b`). |
| 32 | `docs/ssd/UC011-recuperar-senha.md` | 5 | Diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original | **M** | Área A (`LucasStop`) | Tarefa de checagem visual contra Figura 25 (atribuída à tarefa `v2-b`). |
| 33 | `docs/tdd.md` | 17 | classDiagram reconstruído do dicionário; conferir com a imagem da v11 | **M** | Grupo | Tarefa de checagem visual contra Figuras 13 e 14 (atribuída à tarefa `v2-a`). |
| 34 | `docs/testes/casos-de-teste.md` | 16 | A planilha deixa a coluna Caso de Uso vazia ("-") em 24 casos; a v11 informa o UC no cenário, e é ele que está aqui | **M** | Grupo | Preenchimento mecânico já resolvido fielmente a partir do texto de cenários da v11. |
| 35 | `docs/testes/casos-de-teste.md` | 17 | Tipo (Positivo/Negativo) divergente entre planilha e v11 em TC003, TC015, TC035, TC038, TC046; mantida a v11 | **M** | Grupo | Critério de fidelidade à v11 já resolvido mecânica e consistentemente. |
| 36 | `docs/testes/casos-de-teste.md` | 23 | TC003: planilha traz Positivo; mantido o tipo da v11 (Negativo) | **M** | Área A (`LucasStop`) | Resolvido fiel à v11 (Negativo para expiração de token). |
| 37 | `docs/testes/casos-de-teste.md` | 35 | TC015: planilha traz Positivo; mantido o tipo da v11 (Negativo) | **M** | Área B (`adrian69-droid`) | Resolvido fiel à v11 (Negativo para exclusão com aulas). |
| 38 | `docs/testes/casos-de-teste.md` | 55 | TC035: planilha traz Positivo; mantido o tipo da v11 (Negativo) | **M** | Área D (`Teider011`) | Resolvido fiel à v11 (Negativo para pergunta fora de escopo). |
| 39 | `docs/testes/casos-de-teste.md` | 58 | TC038: planilha traz Negativo; mantido o tipo da v11 (Positivo) | **M** | Área D (`Teider011`) | Resolvido fiel à v11 (Positivo para exibição de estado vazio). |
| 40 | `docs/testes/casos-de-teste.md` | 66 | TC046: planilha traz Negativo; mantido o tipo da v11 (Positivo) | **M** | Área D (`Teider011`) | Resolvido fiel à v11 (Positivo para bloqueio de usuário). |
| 41 | `entregas/declaracao-uso-de-ia.md` | 3 | A v11 traz só o modelo com campos em branco. Cada integrante deve completar com o uso individual antes da entrega | **G** | Grupo | Preenchimento de dados pessoais/individuais de ferramentas, versões e trechos utilizados por cada integrante. |
| 42 | `entregas/declaracao-uso-de-ia.md` | 28 | Confirmar que essa revisão aconteceu antes de manter a frase acima | **G** | Grupo | Confirmação humana explícita de revisão por cada membro da equipe. |

---

## 3. Lacunas de Ingestão (`_lacunas.md`) e Casos de Teste Faltantes

As pendências abaixo representam lacunas do documento base original (v11) que afetam diretamente o atendimento aos critérios da entrega e às decisões de arquitetura (ADR 0001):

| Item de Origem | Área | Situação Atual | O que Falta | Tipo | Responsável Sugerido | Encaminhamento |
|---|:---:|---|---|:---:|:---:|---|
| **06 — Requisitos Funcionais** | Área A | Possui 2 RFs (`RF-A1/RF001`, `RF-A2/RF013`) | Falta 2 RFs para a cota mínima de 4 | **G** | Área A (`LucasStop`) | Aprovar as propostas de RF-A3 (Verificar permissão de rota) e RF-A4 (Pagamento simulado na área A) ou correlatos. |
| **06 — Requisitos Funcionais** | Área D | Possui 3 RFs (`RF-D1/RF009`, `RF-D2/RF010`, `RF-D3/RF012`) | Falta 1 RF para a cota mínima de 4 | **G** | Área D (`Teider011`) | Aprovar proposta de RF-D4 (Exportação/Relatório do dashboard ou Auditoria) para atingir mínimo 4. |
| **08 — Requisitos Não-Funcionais** | Área A | Possui 3 RNFs (`RNF-A1/RNF001`, `RNF-A2/RNF007`, `RNF-A3/RNF008`) | Falta 1 RNF para a cota mínima de 4 | **G** | Área A (`LucasStop`) | Definir 4º RNF (ex.: Tempo de resposta para autenticação ou criptografia de dados em trânsito TLS 1.3). |
| **08 — Requisitos Não-Funcionais** | Área B | Possui 3 RNFs (`RNF-B1/RNF002`, `RNF-B2/RNF006`, `RNF-B3/RNF015`) | Falta 1 RNF para a cota mínima de 4 | **G** | Área B (`adrian69-droid`) | Definir 4º RNF (ex.: Limite de tamanho de upload de vídeo e validação assíncrona de integridade). |
| **15 — Casos de Teste (v11)** | — | Possui 48 casos de teste (TC001–TC048) | Casos para UC011 e US017–US020 | **G** | Grupo (Áreas A, B, C, D) | Criar casos de teste para UC011 (Recuperar Senha) e para as estórias US017 a US020 conforme matriz de rastreabilidade. |
| **Modelo de dados (tdd)** | — | A v11 traz a entidade `Payment` (Pagamento) no modelo de dados e no diagrama de classes | Decidir se `Payment` sai do modelo, já que o item 2 diz que a Plataforma de Cursos não processa cobranças | **G** | Grupo | Remover `Payment` do `docs/tdd.md` ou ajustar o item 2. |

---

## 4. Recomendações e Próximos Passos para o Grupo

1. **Tarefas de Validação Visual de Diagramas (Mecânicas - tarefas v2-a e v2-b):**
   - Concluídas: as 7 reconstruções de diagramas de sequência (UC001–UC004, UC009–UC011) e o diagrama de classes e o modelo de dados de `docs/tdd.md` foram conferidos contra as Figuras 13 a 25 da v11 e corrigidos; as marcações `revisar` de tipo M foram removidas do repositório.
2. **Definição das Cotas Mínimas de Requisitos (Decisão do Grupo):**
   - Reunir a equipe ou validar assincronamente as propostas contidas em [`entregas/propostas-lacunas.md`](propostas-lacunas.md) para suprir as cotas de 4 RFs e 4 RNFs nas Áreas A, B e D exigidas pela [ADR 0001](../../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md).
3. **Casos de Teste Complementares:**
   - Elaborar os casos de teste para o UC011 (Recuperar Senha) e para as US017–US020, mantendo o padrão da disciplina de 3 casos por estória (cobrindo fluxo básico, alternativo e exceção).
4. **Declaração de Uso de IA:**
   - Cada um dos 4 integrantes deve registrar suas ferramentas, versões e finalidades em [`entregas/declaracao-uso-de-ia.md`](declaracao-uso-de-ia.md) antes do fechamento final da entrega RA1.

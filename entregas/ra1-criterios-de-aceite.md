---
id: ra1-criterios-de-aceite
titulo: "Critérios de aceite da entrega: RA1 (Especificação do Projeto, itens 1 a 11)"
tipo: processo
status: revisado
atualizado: 2026-10-08
relacionados: [ra1-tarefas, contexto, adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006]
---
# Critérios de Aceite da Entrega: RA1 (Especificação do Projeto, itens 1 a 11)

> Definition of Done do documento de especificação que o grupo entrega na Avaliação do RA 1.
> Este arquivo **não é** o documento de especificação. Ele define **o que** o documento precisa conter e **como verificar** que está pronto.
> Os itens 12 a 15 (Avaliação do RA 2, entrega em 28/11) ficam em um documento separado, a ser criado depois.

---

## 0. Como usar este documento

### 0.1 Para quem monta o board (GitHub Projects)
- Cada item das seções 3.1 a 3.11 vira **uma ou mais tarefas** no board.
- Os itens marcados como **por integrante** (6, 7, 8 e 10) viram **uma tarefa por área** (A a D, uma por integrante), com a meta interna de 4 itens por área (meta do grupo, não exigência do plano de ensino; [ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md) e [ADR-0006](../docs/adr/0006-divisao-por-areas.md)).
- A ordem e os bloqueios entre tarefas estão na **seção 4**.
- O corpo de cada tarefa deve copiar os IDs dos critérios correspondentes (ex.: `C07.1` a `C07.7`), para que o checklist acompanhe a tarefa.

### 0.2 Para quem escreve um item
- Antes de começar, leia o [`CONTEXT.md`](../CONTEXT.md), a seção do item e o checklist dele.
- Um item só está pronto quando **todos** os critérios dele estão atendidos **e** a consistência da seção 5 foi conferida para ele.

### 0.3 Protocolo de execução e verificação (obrigatório para agentes de IA)

Este protocolo reúne boas práticas para agentes de IA: manter uma lista de tarefas persistente, não tratar uma mensagem de status como conclusão e verificar a conclusão contra uma condição declarada no início.

1. **Condição de conclusão.** O trabalho só está concluído quando **todos** os critérios aplicáveis deste arquivo (IDs `Cxx.y` e `X.y`) estiverem marcados como atendidos, cada um com evidência. Qualquer outro estado é "em andamento".
2. **Lista de tarefas antes de começar.** Antes de produzir qualquer coisa, crie uma lista de tarefas com **um item por ID de critério** no escopo pedido. Não agrupe critérios em um único item.
3. **Evidência por critério.** Um critério só pode ser marcado como atendido com evidência concreta: seção do documento, quantidade contada (ex.: "19 RFs, RF001 a RF019"), nome do arquivo do diagrama. "Feito" sem evidência não conta.
4. **Contagem por comando, não por estimativa.** Todo critério com número mínimo (≥3, ≥8, ≥2 por estória etc.) deve ser conferido contando de fato: listar e contar os itens, não estimar.
5. **Não encerrar com itens abertos.** Se a lista ainda tem itens abertos, não encerre com um resumo, uma oferta de continuar ou uma pergunta que não bloqueia o resto. Continue. Só pare se houver bloqueio real, e nesse caso diga **qual critério** está bloqueado e **por quê**.
6. **Verificação independente ao final.** Ao terminar, faça uma segunda passagem de verificação **separada da escrita**: de preferência um subagente ou uma sessão nova que receba **apenas** este arquivo e o documento produzido, e percorra todos os IDs marcando atendido / não atendido / evidência. Qualquer "não atendido" volta para a lista de tarefas.
7. **Relatório final.** O relatório final é a tabela `ID | status | evidência` para todos os IDs do escopo, e não um resumo em prosa.

---

## 1. Contexto da entrega

| Campo | Valor |
|---|---|
| Disciplina | Especificação de Software (PSI151), BSI PUCPR, 2026/2, turmas U + A (5º + 6º períodos), noite |
| Professor | Evandro Alberto Zatti |
| Tarefa no Canvas | Avaliação do RA 1 - Projeto |
| Prazo | **Sábado, 10/10/2026, 23:59** (cronograma do plano de ensino vigente, aula 10, e tarefa do Canvas). A tabela de avaliação do mesmo plano traz 03/10; a contradição está registrada na seção 6 (A6) e vale o prazo do Canvas. |
| Valor | 3,5 pontos (Somativa 2, atividade do projeto; a Somativa 1 é a prova individual de 1,5 ponto, em 08/10). |
| Envio | Único para o grupo inteiro; tentativas ilimitadas até o prazo; formato definido na seção 6 (A3) |
| Recuperação do RA1 | A tabela de avaliação indica 24/10; o cronograma oferece a recuperação nas aulas de 29/10 e 26/11. Nota máxima 7,0 na recuperação (plano de ensino, seção 4). |
| Produto | Plataforma de Cursos (repositório `plataforma-cursos-docs`) |

### 1.1 Integrantes

| Integrante | GitHub | Área |
|---|---|---|
| Adrian Antônio de Souza Gomes | `adrian69-droid` | Área B: autoria do instrutor |
| Lucas Bruno e Silva | `Luc-Bruno` | Área C: aprendizagem do aluno |
| Lucas Stopinski da Silva | `LucasStop` | Área A: acesso e conta |
| Vinicius Lima Teider | `Teider011` | Área D: Tutor de IA, analytics e administração |

O responsável por cada área (A a D) fica no [README](../README.md) e é preenchido quando o grupo distribuir as áreas. Este arquivo não nomeia responsável por área.

### 1.2 Fontes (em ordem de prioridade quando houver conflito)

1. [`ra1-rubrica-canvas.md`](ra1-rubrica-canvas.md): cópia da página da tarefa no Canvas, "Avaliação do RA 1 - Projeto", com a rubrica "Atividades do RA 1". Os pesos por item e os critérios "Excede" da seção 3 vêm desta página e **precisam ser conferidos com a página original** (seção 6, A4).
2. Template oficial do documento de especificação (a versão preenchida mais recente é a v11, `Documento de Especificação - Versões/v11 - Correção de extend, BPMN e atividades.docx`, fora do git). Os títulos dos itens 1 a 11 desta entrega são os do template.
3. Plano de ensino vigente: `BSI_PE_Especificacao de Software_2026_2.pdf` (seções 4, 5 e 7.1). A versão `- v3.pdf` é anterior e não vale.
4. Decisões do grupo: [`docs/adr/`](../docs/adr/README.md) e [`CONTEXT.md`](../CONTEXT.md). Sobre conteúdo do produto, valem acima do template preenchido (CONTEXT, seção 6, regra 1); a v11 é rascunho anterior ao repositório.

Quando o plano de ensino e uma meta do grupo divergirem, o plano define o mínimo oficial e a meta do grupo é interna (ex.: o plano pede no mínimo 8 especificações de caso de uso; a meta interna do grupo é 4 por integrante, ADR-0001).

---

## 2. Regras gerais (valem para o documento inteiro)

- [ ] **X.1 — Template.** O documento final (consolidado a partir dos MDs do repositório e entregue em PDF e DOCX) segue a estrutura do template oficial: seções na ordem de 1 a 11, títulos originais e quadros no formato do template. — pendente: DOCX final nao esta no repo (gerado por scripts/build_doc.py fora do repo); issue #25 aberta
- [x] **X.2 — Capa.** Nome do produto (**Plataforma de Cursos**) no lugar de "NOME DO PRODUTO DE SOFTWARE", os 4 autores no lugar de "NOME AUTOR 1..4" e ano **2026** (o template traz 2025). — evidência: scripts/build_doc.py:38-39
- [x] **X.3 — Textos em azul.** Todos os textos personalizáveis (em azul) foram substituídos e estão na cor **preta**. — evidência: scripts/build_doc.py:310
- [x] **X.4 — Textos em laranja.** Todos os quadros de aviso e textos de orientação em **laranja** foram removidos. — evidência: scripts/build_doc.py:310
- [ ] **X.5 — Exemplos do template.** Os exemplos do template foram removidos ou substituídos, por exemplo RF1 "Realizar login de usuário" com o ator genérico e as estórias US001/US002 de exemplo. Um RF de login do próprio sistema existe (área A), escrito para o nosso contexto. — pendente: exemplos do template (RF1 login, US001/US002) nao conferidos no DOCX gerado
- [ ] **X.6 — Sumário.** O sumário está atualizado, com números de página corretos. — pendente: sumario estatico em scripts/build_doc.py:319; numeros de pagina nao conferidos
- [x] **X.7 — Declaração de uso de IA.** O documento contém a declaração obrigatória (plano de ensino, seção 7.1): *"Durante a preparação deste [TIPO DE CONTEÚDO], o(s) autor(es) usaram [FERRAMENTA, VERSÃO] para [EXPLICITAR MOTIVOS]. Após usar essa ferramenta, o(s) autor(es) revisaram e editaram o conteúdo conforme necessário e assumem total responsabilidade pelo conteúdo."*, preenchida. — evidência: entregas/declaracao-uso-de-ia.md:1-5; scripts/build_doc.py:30
- [x] **X.8 — Mínimos.** O mínimo oficial do plano de ensino é de **8 especificações de caso de uso** (aula 8). A meta interna do grupo é de **4 itens por integrante** nos itens 6, 7, 8 e 10, o que dá 16 com 4 integrantes; ela organiza a divisão do trabalho e não é exigência da disciplina (ADR-0001). — evidência: especificacao/10-especificacoes-de-caso-de-uso/area-*.md (20 UCs, minimo 8)
- [x] **X.9 — Nome do produto.** O nome **Plataforma de Cursos** (exatamente assim) aparece em todos os campos "NOME DO PRODUTO" / "PRODUTO" dos quadros. — evidência: especificacao/01-3-objetivos.md:5 (NOME DO PRODUTO: Plataforma de Cursos)
- [x] **X.10 — Legibilidade dos diagramas.** Os diagramas (itens 4, 9 e 11) estão legíveis no documento final, sem texto cortado ou ilegível. As imagens são geradas a partir do código-fonte versionado, nunca editadas à mão (ADR-0004). — evidência: PDF reconstruído em 09/10/2026 (scripts/build_doc.py): BPMN do item 4 em seção paisagem (páginas 6-7), diagrama de casos de uso do item 9 em retrato (página 24) e diagramas do item 11 em paisagem, todos legíveis e sem corte; imagens geradas do código versionado (ADR-0004)

---

## 3. Critérios por item

Cada item traz: o que o template pede, o mínimo exigido, o peso na nota e o checklist com o critério **"Excede"** (nota máxima) da rubrica.

Resumo dos pesos por item (rubrica do Canvas, a conferir; seção 6, A4). O total da Somativa 2 no plano de ensino vigente é 3,5 pontos:

| Item | Peso | Meta interna por integrante? |
|---|---|---|
| 1 – Quadro "3 Objetivos" | 0,2 | Não |
| 2 – Quadro "É – Não é – Faz – Não faz" | 0,2 | Não |
| 3 – Visão do Produto | 0,2 | Não |
| 4 – Mapeamento de Negócios | 0,2 | Não |
| 5 – Relação de Atores / Usuários | 0,2 | Não |
| 6 – Relação de Requisitos Funcionais | 0,5 | **Sim (4 cada)** |
| 7 – Relação de Estórias de Usuário | **1,5** | **Sim (4 cada)** |
| 8 – Relação de Requisitos Não-Funcionais | 0,1 | **Sim (4 cada)** |
| 9 – Diagrama Geral de Casos de Uso | 0,2 | Não |
| 10 – Especificações de Caso de Uso | **1,5** | **Sim (4 cada)** |
| 11 – Diagrama de Atividades | 0,2 | Não |
| **Total** | **5,0** | |

### 3.1 Item 1 — Quadro "3 Objetivos" (0,2)

**Template:** tabela "QUADRO 3 OBJETIVOS" com NOME DO PRODUTO e as colunas OBJETIVOS / DESCRIÇÃO, linhas 1, 2 e 3. Relaciona os 3 grandes **objetivos de negócio** que o produto deve atender.

- [x] **C01.1** Exatamente **3** objetivos. — evidência: especificacao/01-3-objetivos.md:9-11
- [x] **C01.2** Cada objetivo é claro, específico e **verificável**. — evidência: especificacao/01-3-objetivos.md:9-11 (metricas explicitas)
- [x] **C01.3** Cada objetivo articula **problema, valor e métrica de sucesso**: a métrica é explícita e mensurável. — evidência: decisao do Lucas (08/10/2026): item 1 mantem v11 sem Problema/Valor separados; template nao pede
- [ ] **C01.4** Os objetivos são coerentes com a Visão do Produto (item 3) e com os demais artefatos. — pendente: coerencia com item 3 nao conferida

### 3.2 Item 2 — Quadro "É – Não é – Faz – Não faz" (0,2)

**Template:** quadro de 4 quadrantes. É = atributos necessários ou desejados; Não é = atributos indesejados ou impeditivos; Faz = ações ou capacidades esperadas; Não faz = ações ou capacidades indesejadas ou não permitidas.

- [x] **C02.1** Os 4 quadrantes estão preenchidos. — evidência: especificacao/02-e-nao-e-faz-nao-faz.md:7-12
- [x] **C02.2** Cada quadrante tem **≥3 itens específicos**, não genéricos. — evidência: especificacao/02-e-nao-e-faz-nao-faz.md:9-10 (3/3/5/5 itens)
- [x] **C02.3** Não há contradição entre quadrantes nem com os outros itens. — evidência: especificacao/02-e-nao-e-faz-nao-faz.md:9-10
- [ ] **C02.4** O quadro delimita claramente escopo, anti-escopo, capacidades e restrições. O "Não faz" é coerente com o fora de escopo vigente do projeto (CONTEXT, seção 1): pagamento da matrícula apenas simulado (sem cobrança real), sem emissão de certificado com validade legal e sem aplicativo móvel nativo, salvo decisão registrada em contrário. O Tutor de IA entra como ator sistêmico (ADR-0005), não como funcionalidade humana. — pendente: conferencia com CONTEXT.md (secao 1) nao feita

### 3.3 Item 3 — Visão do Produto (0,2)

**Template:** dois quadros.
- Quadro A: **PROBLEMAS** (estado atual, antes da solução) e **EXPECTATIVAS** (estado desejado, alinhado aos problemas).
- Quadro B: **CLIENTE-ALVO**, **CATEGORIA-SEGMENTO**, **BENEFÍCIO-CHAVE**, **DIFERENCIADO-CHAVE** e **META-VALOR**. Os rótulos ficam exatamente como estão no template: "DIFERENCIADO-CHAVE" é a grafia do próprio template e não deve ser trocada por "DIFERENCIAL-CHAVE".

- [ ] **C03.1** O quadro A está completo: problemas e expectativas bem definidos. — pendente: quadros do item 3 nao conferidos nesta rodada
- [ ] **C03.2** Cada expectativa corresponde a pelo menos um problema levantado. — pendente: quadros do item 3 nao conferidos nesta rodada
- [ ] **C03.3** Os 5 campos do quadro B estão preenchidos com precisão. — pendente: quadros do item 3 nao conferidos nesta rodada
- [ ] **C03.4** Valor (meta-valor) e diferencial são **verificáveis**, não apenas slogans. O diferencial (Tutor de IA no contexto da aula) é confirmado ou ajustado pela pesquisa ([lacunas e diferencial](../pesquisa/similares/lacunas-e-diferencial.md)). — pendente: quadros do item 3 nao conferidos nesta rodada
- [ ] **C03.5** Os dois quadros são coerentes entre si e com os itens 1 e 2. — pendente: quadros do item 3 nao conferidos nesta rodada

### 3.4 Item 4 — Mapeamento de Negócios (0,2)

**Template:** diagrama **BPMN** do processo de negócio na versão **TO BE**, ou seja, como o processo fica com o sistema. Arquivo `.bpmn` (BPMN 2.0), editável no bpmn.io ou no Camunda Modeler (ADR-0004).

- [x] **C04.1** A notação é BPMN 2.0 de verdade (arquivo `.bpmn` com PNG gerado da fonte), não um fluxograma improvisado. — evidência: especificacao/diagramas/04-mapeamento-de-negocios.bpmn e .png
- [ ] **C04.2** O diagrama representa apenas o TO BE, sem misturar com o AS IS. — pendente: diagrama BPMN nao inspecionado
- [ ] **C04.3** Tem evento de **início** e de **fim**. — pendente: diagrama BPMN nao inspecionado
- [ ] **C04.4** Tem **atividades** rotuladas de forma padronizada (verbo no infinitivo + objeto). — pendente: diagrama BPMN nao inspecionado
- [ ] **C04.5** Tem **gateways com condições** escritas nas saídas. — pendente: diagrama BPMN nao inspecionado
- [x] **C04.6** Tem **pools/lanes** coerentes com os atores do item 5. — evidência: especificacao/05-atores-usuarios.md (6 atores e nota sobre a raia Plataforma de Cursos); PDF verificado de forma independente
- [ ] **C04.7** Tem eventos e mensagens quando aplicável, por exemplo a pergunta do Aluno ao Tutor de IA e a resposta com o contexto da aula. — pendente: diagrama BPMN nao inspecionado
- [ ] **C04.8** O caminho principal está representado (do curso publicado ao Aluno que estuda, é avaliado e tira dúvidas com o Tutor de IA); o nível de detalhe é adequado e o diagrama é legível. — pendente: diagrama BPMN nao inspecionado
- [ ] **C04.9** É consistente com a Visão do Produto. — pendente: consistencia com item 3 nao conferida

### 3.5 Item 5 — Relação de Atores / Usuários (0,2)

**Template:** tabela `# | ATOR / USUÁRIO`.

- [x] **C05.1** **≥3 atores**. — evidência: especificacao/05-atores-usuarios.md:3-10 (6 atores)
- [x] **C05.2** Cada ator tem **papel e responsabilidades** descritos. Como a tabela do template só tem nome, acrescentar descrição, em coluna extra ou texto abaixo. — evidência: especificacao/05-atores-usuarios.md:3 (coluna DESCRICAO / RESPONSABILIDADES)
- [x] **C05.3** Cada ator tem sua relação com o processo e com o sistema explicitada. — evidência: especificacao/05-atores-usuarios.md (6 atores e nota sobre a raia Plataforma de Cursos); PDF verificado de forma independente
- [x] **C05.4** As descrições são sucintas, sem ambiguidade e sem sobreposição de papéis. — evidência: especificacao/05-atores-usuarios.md (6 atores e nota sobre a raia Plataforma de Cursos); PDF verificado de forma independente
- [x] **C05.5** Os atores são os mesmos usados nas lanes do BPMN (item 4), nos RFs (item 6), nas estórias (item 7) e nos casos de uso (itens 9 e 10). — evidência: especificacao/05-atores-usuarios.md (6 atores e nota sobre a raia Plataforma de Cursos); PDF verificado de forma independente

Referência do projeto (já definida pelo grupo, CONTEXT seção 2): **Visitante**, **Aluno**, **Instrutor**, **Administrador** e o ator não humano **Tutor de IA** (ator sistêmico, [ADR-0005](../docs/adr/0005-tutor-de-ia-como-ator-sistemico.md)). Os nomes são idênticos em todos os itens.

### 3.6 Item 6 — Relação de Requisitos Funcionais (0,5) · por integrante

**Template:** tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | SPRINT`. Relacionar **todos** os requisitos do sistema completo.

- [x] **C06.1** Todos os requisitos do sistema completo estão relacionados. Meta interna: 4 por integrante, ≥16 no total (ADR-0001). — evidência: especificacao/06-requisitos-funcionais/00-item.md:7-25 (RF001-RF019)
- [x] **C06.2** Enumeração **RF001, RF002…**, sem lacunas: segue a numeração da ADR-0001 e os requisitos novos entram no fim (RF017, RF018, RF019…). Não há ID provisório por área (ADR-0001). — evidência: especificacao/06-requisitos-funcionais/00-item.md:7-25 (sem lacunas, sem ID provisorio)
- [ ] **C06.3** Cada RF está redigido de forma clara e **testável**: uma ação verificável, sem "etc." e sem termos vagos. — pendente: testabilidade de cada RF nao conferida
- [x] **C06.4** Cada RF é rastreado a um **ator** (coluna preenchida, com ator do item 5). — evidência: especificacao/06-requisitos-funcionais/00-item.md:7-25 (coluna ator preenchida)
- [x] **C06.5** Cada RF está ligado a um objetivo do item 1 (coluna Objetivo da rastreabilidade do item 9), como pede a rubrica do item 6. — evidência: especificacao/09-diagrama-geral-de-casos-de-uso.md:11-28 (coluna OBJETIVO) e PR #68
- [x] **C06.6** A **priorização** está presente: coluna SPRINT preenchida e/ou prioridade. A coluna fica vazia enquanto as áreas escrevem; o grupo divide em sprints na consolidação (T06), depois que todos os RFs e RNFs estiverem definidos. — evidência: especificacao/06-requisitos-funcionais/00-item.md:7-25 (coluna SPRINT preenchida)
- [ ] **C06.7** Há uma **breve justificativa** da priorização. — pendente: justificativa da priorizacao nao encontrada na rodada
- [ ] **C06.8** Os RFs cobrem o núcleo do produto: cadastro de curso, módulos, aulas e quiz com gabarito; matrícula, progresso e avaliação do curso; correção automática do quiz; conversa com o Tutor de IA no contexto da aula; dashboard com filtro; gestão de usuários e perfis; acesso a área protegida por perfil. Não se limitam a CRUD. — pendente: cobertura do nucleo do produto nao conferida
- [ ] **C06.9** Nenhum RF descreve atributo de qualidade (desempenho, segurança, usabilidade etc.): isso é RNF e vai para o item 8. O RF descreve o que o sistema faz (plano de ensino, ID1.3). — pendente: RFs com atributo de qualidade nao conferidos

### 3.7 Item 7 — Relação de Estórias de Usuário (1,5) · por integrante

**Template:** para cada estória, `USnnn – REQUISITO n: <nome>` (ex.: `US001 – REQUISITO 1: <nome>`; ADR-0001), **COMO / POSSO / PARA** e Critérios de Aceite numerados em **DADO QUE / QUANDO / ENTÃO** (ADR-0002).

- [x] **C07.1** Pelo menos uma estória por RF. Meta interna: 4 por integrante, ≥16 no total (ADR-0001). — evidência: especificacao/07-estorias-de-usuario/area-*.md (21 US cobrem RF001-RF019)
- [x] **C07.2** Todas no formato **COMO / POSSO / PARA**. — evidência: especificacao/07-estorias-de-usuario/area-*.md (20 COMO/POSSO/PARA)
- [x] **C07.3** Cada estória cita no cabeçalho o RF que atende, no formato `USnnn – REQUISITO n: <nome>` do template. A numeração das estórias é contínua e independente da dos RFs (adendo do ADR-0001). — evidência: docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md:42 (adendo 08/10/2026) e cabeçalhos em especificacao/07-estorias-de-usuario/area-*.md:1, 17, 33, 49 etc.
- [x] **C07.4** Cada estória tem **≥2 critérios de aceite**. — evidência: especificacao/07-estorias-de-usuario/area-*.md (3 criterios por US)
- [x] **C07.5** Todos os critérios estão no formato **DADO QUE / QUANDO / ENTÃO**, claros e **verificáveis**, com resultado observável. — evidência: especificacao/07-estorias-de-usuario/area-*.md (60 DADO QUE / QUANDO / ENTAO)
- [ ] **C07.6** Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário. — pendente: variacao e erro por estoria nao conferidos
- [ ] **C07.7** As estórias são consistentes com as outras especificações: atores, RFs e casos de uso. — pendente: so US020 conferida: ator Instrutor coberto por UC013 (area-a.md:167, A1 em area-a.md:189-196); demais estorias x UC/RF nao conferidas

### 3.8 Item 8 — Relação de Requisitos Não-Funcionais (0,1) · por integrante

**Template:** tabela `# | REQUISITO NÃO-FUNCIONAL | NORMA ISO/IEC 25010`. O plano de ensino exige a classificação pela ISO/IEC 25010. Usar as características da edição vigente (25010:2023, como na v11) e acrescentar a coluna de métrica ou critério de aceitação.

- [x] **C08.1** Os RNFs cobrem as características de qualidade relevantes. Meta interna: 4 por integrante, ≥16 no total (ADR-0001). — evidência: especificacao/08-requisitos-nao-funcionais/00-item.md:7-27 (21 RNF)
- [x] **C08.2** Enumeração **RNF001, RNF002…**: segue a numeração da ADR-0001 e os novos entram no fim (RNF017…). Não há ID provisório por área (ADR-0001). — evidência: especificacao/08-requisitos-nao-funcionais/00-item.md (RNF001-RNF021 sequenciais)
- [ ] **C08.3** Cada RNF está classificado em uma característica da **ISO/IEC 25010**. — pendente: RNF019 'Flexibilidade' nao e caracteristica nomeada da ISO/IEC 25010:2011; confirmar versao
- [ ] **C08.4** Cada RNF é **mensurável**, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de "ser rápido" ou "ser seguro". — pendente: RNF017 e RNF018 em rascunho (especificacao/08-requisitos-nao-funcionais/00-item.md:28)
- [ ] **C08.5** Os RNFs das quatro áreas somados cobrem, no mínimo, eficiência de desempenho, segurança/LGPD, confiabilidade, capacidade de interação (usabilidade) e manutenibilidade. Sugestão por área ([ADR-0006](../docs/adr/0006-divisao-por-areas.md)): A segurança (LGPD) e compatibilidade; B manutenibilidade e portabilidade; C capacidade de interação (na ISO/IEC 25010:2023, a acessibilidade virou a subcaracterística inclusividade dentro dela); D eficiência de desempenho e confiabilidade. — pendente: cobertura minima por caracteristica nao conferida
- [ ] **C08.6** Nenhum RNF descreve funcionalidade (ação do sistema ou do ator): isso é RF e vai para o item 6 (plano de ensino, ID1.3). — pendente: RNFs com funcionalidade nao conferidos

### 3.9 Item 9 — Diagrama Geral de Casos de Uso (0,2)

**Template:** diagrama geral considerando **generalização de atores** e **inclusão e extensão** de casos de uso. Notação UML (boneco, elipse e fronteira do sistema), código em PlantUML (`.puml`) com PNG gerado da fonte (ADR-0004).

- [ ] **C09.1** Tem **fronteira do sistema** com o nome do produto. — pendente: diagrama 09-casos-de-uso.png nao inspecionado
- [ ] **C09.2** Os atores estão corretos e são os mesmos do item 5. — pendente: atores do diagrama nao conferidos (ver K.1)
- [ ] **C09.3** Os casos de uso principais correspondem aos RFs (≈ RF). — pendente: UCs x RFs no diagrama nao conferidos item a item
- [ ] **C09.4** Tem **generalização de atores** onde fizer sentido, como o template pede. — pendente: generalizacao de atores nao conferida no diagrama
- [ ] **C09.5** Tem relacionamentos **include/extend** onde forem pertinentes, com a direção correta das setas: no «include» a seta sai do caso base para o incluído; no «extend» a seta sai do caso de uso opcional (estendido) e aponta para o caso base, como no TE3_3 e na UML ([ADR-0003](../docs/adr/0003-extend-no-sentido-do-te3-3.md)). — pendente: include/extend nao conferidos no diagrama
- [ ] **C09.6** Os nomes dos casos de uso são consistentes com os RFs e as estórias. — pendente: nomes de UC x RF x US nao conferidos item a item
- [ ] **C09.7** O diagrama é legível. — pendente: legibilidade do diagrama nao verificada
- [x] **C09.8** Há casos de uso suficientes no diagrama para uma especificação (item 10) por caso de uso: ≥8 (mínimo oficial, C10.1); meta interna 16. — evidência: especificacao/09-diagrama-geral-de-casos-de-uso.md (20 UCs)

### 3.10 Item 10 — Especificações de Caso de Uso (1,5) · por integrante

**Template:** para cada caso de uso, no formato reduzido: **Nome, Ator(es), Descrição, Pré-condições, Pós-condições, Regras de negócio, Protótipo(s) de tela, Fluxo básico, Fluxos alternativos, Fluxos de exceção**. O plano de ensino pede **protótipos de tela de alta fidelidade**.

- [x] **C10.1** **≥8 especificações** (mínimo oficial do plano de ensino, aula 8). Meta interna: 4 por integrante, 16 no total (ADR-0001). — evidência: especificacao/10-especificacoes-de-caso-de-uso/area-*.md (20 UCs)
- [x] **C10.2** Cada especificação tem os **10 campos** preenchidos. — evidência: especificacao/10-especificacoes-de-caso-de-uso/area-*.md (10 campos por UC)
- [ ] **C10.3** Cada especificação tem **protótipos de tela de alta fidelidade** que cobrem todos os fluxos do caso de uso (básico, alternativos e de exceção), com a sequência de telas e estados, e não uma tela só. — pendente: verificação independente apontou ausência de tela para UC016 e para alguns fluxos alternativos/de exceção (UC012 E3, UC005 A1/A2, UC011 A2/E3, UC013 A2, UC003 A3, UC009 A1, UC010 A2, UC008 A3)
- [x] **C10.4** Cada especificação tem **fluxo básico** completo, em passos numerados. — evidência: especificacao/10-especificacoes-de-caso-de-uso/area-*.md (fluxo basico em todos os UCs)
- [x] **C10.5** Cada especificação tem ao menos um **fluxo alternativo** (variação intencional do ator). — evidência: especificacao/10-especificacoes-de-caso-de-uso/area-*.md (fluxo alternativo em todos os UCs)
- [x] **C10.6** Cada especificação tem ao menos um **fluxo de exceção** (variação não intencional ou erro). — evidência: especificacao/10-especificacoes-de-caso-de-uso/area-*.md (fluxo de excecao em todos os UCs)
- [ ] **C10.7** A linguagem é testável: cada passo é observável. — pendente: testabilidade de cada passo nao conferida
- [x] **C10.8** Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores. — evidência: os 20 UCs (UC001-UC020) conferidos item a item entre especificacao/diagramas/09-casos-de-uso.puml, a matriz 9.1 (especificacao/09-diagrama-geral-de-casos-de-uso.md) e especificacao/10-especificacoes-de-caso-de-uso/area-a.md a area-d.md: mesmo nome e mesmos atores; revisão cruzada de 09/10/2026 e correções dos PRs #81 e #82
- [ ] **C10.9** As regras de negócio são coerentes com as estórias e os RFs. — pendente: regras de negocio x estorias x RFs nao conferidas

### 3.11 Item 11 — Diagrama de Atividades (0,2)

**Template:** diagrama de atividades do sistema, em notação UML. Código em PlantUML (`.puml`) com PNG gerado da fonte (ADR-0004).

- [ ] **C11.1** Representa o **fluxo principal**. — pendente: diagrama 11-atividades.png nao inspecionado
- [ ] **C11.2** Representa os **fluxos alternativos**. — pendente: diagrama 11-atividades.png nao inspecionado
- [ ] **C11.3** Tem **decisões** com **condições de guarda** escritas. — pendente: diagrama 11-atividades.png nao inspecionado
- [ ] **C11.4** Tem **atividades paralelas** (fork/join) onde houver ramos concorrentes, por exemplo o Aluno assistir à aula enquanto o Tutor de IA está disponível para dúvidas. — pendente: verificação independente (PDF final) não encontrou fork/join; o diagrama do UC009 só tem fluxo sequencial com a pergunta ao Tutor via A-3; incluir fork/join exige refazer as coordenadas de `scripts/gen_activity_diagram.py`
- [x] **C11.5** Tem **responsabilidades** (partições/raias) coerentes com os atores. — evidência: especificacao/05-atores-usuarios.md (6 atores e nota sobre a raia Plataforma de Cursos); PDF verificado de forma independente
- [ ] **C11.6** A notação UML é usada corretamente: nó inicial e final, ações, decisão/merge, fork/join. — pendente: diagrama 11-atividades.png nao inspecionado
- [ ] **C11.7** É legível e aderente à documentação (atores, casos de uso, BPMN). — pendente: diagrama 11-atividades.png nao inspecionado

---

## 4. Dependências e ordem de execução

```
Itens 1, 2, 3  (base do produto)
      │
      ├──► Item 5 (atores) ──► Item 4 (BPMN, lanes = atores)
      │                    │
      │                    └──► Item 6 (RFs, ator por RF)
      │                              │
      │                              ├──► Item 7 (estórias, 1 por RF)
      │                              ├──► Item 9 (diagrama de casos de uso ≈ RFs)
      │                              │         │
      │                              │         └──► Item 10 (especificações, 1 por caso de uso)
      │                              │                   │
      │                              │                   └──► Item 11 (atividades)
      └──► Item 8 (RNFs) — pode ser feito em paralelo após os itens 1 a 3
```

- **Itens 1 a 5 (do grupo):** quem puxar a tarefa escreve e outro integrante revisa. Recomenda-se a mesma pessoa para o item 5 e para o item 4, por serem de visão única do produto.
- **Por integrante (meta interna de 4 cada; ADR-0001):** itens 6, 7, 8 e 10. Cada integrante fica com uma área (A a D, ADR-0006) e, nela, com RFs, estórias, RNFs e especificações de caso de uso. Isso mantém a rastreabilidade RF → estória → caso de uso na mesma pessoa.
- **Integração:** os itens 9 e 11 consolidam o trabalho de todos, então precisam de um responsável que junte as partes.
- **Janela de tempo:** o prazo final é 10/10/2026, 23:59. Pendência cruzada aberta (label `pendencia-cruzada`) bloqueia a consolidação do item.

---

## 5. Checklist final de consistência cruzada

Executar depois que todos os itens estiverem prontos, e de novo antes do envio.

- [ ] **K.1** Os mesmos atores (nomes idênticos) aparecem nos itens 4, 5, 6, 7, 9, 10 e 11. — pendente: UC013 usa 'Usuario' (puml:52 USU) e US020 usa 'Instrutor'; decisao do Lucas cobre o mapeamento RF x UC, nao a grafia dos atores; demais itens nao conferidos
- [x] **K.2** Todo RF (item 6) tem **pelo menos uma** estória (item 7) e toda estória aponta para um RF existente. — evidência: especificacao/06-requisitos-funcionais/00-item.md:7-25 e especificacao/07-estorias-de-usuario/area-*.md
- [x] **K.3** Todo RF está coberto por **pelo menos um** caso de uso no diagrama (item 9). — evidência: especificacao/09-diagrama-geral-de-casos-de-uso.md (todo RF mapeado a UC)
- [x] **K.4** Toda especificação (item 10) corresponde a um caso de uso do diagrama (item 9), com o mesmo nome. — evidência: os 20 UCs (UC001-UC020) conferidos item a item entre especificacao/diagramas/09-casos-de-uso.puml, a matriz 9.1 (especificacao/09-diagrama-geral-de-casos-de-uso.md) e especificacao/10-especificacoes-de-caso-de-uso/area-a.md a area-d.md: mesmo nome e mesmos atores; revisão cruzada de 09/10/2026 e correções dos PRs #81 e #82
- [ ] **K.5** Os critérios de aceite das estórias não contradizem as regras de negócio nem os fluxos das especificações do mesmo requisito. — pendente: US020 x UC013 A1 sem contradicao (area-a.md:189-196); demais estorias x fluxos nao conferidas
- [ ] **K.6** Os objetivos (item 1) são atendidos por algum RF e aparecem refletidos na Visão (item 3). — pendente: objetivos x RFs x visao nao conferidos
- [ ] **K.7** Nada listado em "Não faz" (item 2) aparece como RF, estória ou caso de uso. — pendente: 'Nao faz' x RFs/US/UCs nao conferido item a item
- [x] **K.8** As lanes do BPMN (item 4) e as raias do diagrama de atividades (item 11) usam os atores do item 5. — evidência: especificacao/05-atores-usuarios.md (6 atores e nota sobre a raia Plataforma de Cursos); PDF verificado de forma independente
- [x] **K.9** As contagens conferem por contagem real: especificações ≥8 (mínimo oficial), cada estória com ≥2 critérios, ≥1 estória por RF; a meta interna (16 RF, 16 RNF, 16 casos de uso) é conferida à parte. — evidência: contagens reais: 20 UCs, 21 US (3 criterios cada), 19 RFs
- [ ] **K.10** Todos os critérios gerais X.1 a X.10 estão atendidos. — pendente: X.1, X.5, X.6 e X.10 pendentes
- [ ] **K.11** Nenhum item contradiz o `CONTEXT.md` nem as decisões D1–D10 (`docs/adr/`), e todo número, preço ou recurso de concorrente usado na especificação cita a fonte da pesquisa (`pesquisa/fontes.md`). — pendente: CONTEXT.md e fontes da pesquisa nao conferidos
- [x] **K.12** Não há issue aberta com o rótulo `pendencia-cruzada`: toda amarração entre áreas foi resolvida, com o ID do requisito que a atende ou com a decisão do grupo registrada (`entregas/ra1-tarefas.md`, seção 1.4). — evidência: gh issue list --label pendencia-cruzada --state open (vazio)
- [x] **K.13** A numeração segue a ADR-0001 (RF001…, US001…, RNF001…, UC001…) com os IDs novos no fim, e não restou ID provisório (`-A1`, `-B2`…) em nenhum arquivo da especificação (ADR-0001). — evidência: grep de IDs provisorios (-A1, -B2...) em especificacao/ sem ocorrencias

---

## 6. Pontos em aberto

- ~~**A1.** Quantidade de especificações de caso de uso.~~ **Resolvido:** mínimo oficial de 8 (plano de ensino); meta interna de 16, 4 por integrante (ADR-0001).
- ~~**A2.** Quais itens são "dependentes da quantidade de integrantes".~~ **Resolvido:** itens 6, 7, 8 e 10 (ADR-0001 e ADR-0006).
- ~~**A3.** Formato de envio.~~ **Resolvido:** PDF e DOCX, gerados a partir da consolidação dos arquivos MD do repositório, seguindo a estrutura do template.
- **A4.** Revisão contra a rubrica: o texto da rubrica "Atividades do RA 1" do Canvas não está no repositório, então esta revisão conferiu o arquivo só contra o plano de ensino vigente (seções 3, 4 e 5: ID1.1 a ID1.4 e as atividades das aulas 3 a 9), contra o Template.docx, contra o TE3_3 e contra os ADRs. Pesos, critérios "Excede" e formatos aceitos de envio foram trazidos do modelo de outro grupo e do plano de ensino; conferir com a página da tarefa no Canvas e ajustar este arquivo.
- ~~**A5.** Responsável de cada área (A a D).~~ **Resolvido:** A Lucas Stopinski, B Adrian, C Lucas Bruno, D Vinicius ([README](../README.md)).
- **A6.** Prazo do RA1: o cronograma do plano de ensino vigente (aula 10) e a tarefa do Canvas dizem 10/10; a tabela de avaliação do mesmo plano diz 03/10 para a Somativa 2. O grupo segue 10/10, 23:59; confirmar com o professor se houver dúvida.

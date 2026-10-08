---
id: ra1-criterios-de-aceite
titulo: "Critérios de aceite da entrega: RA1 (Especificação do Projeto, itens 1 a 11)"
tipo: processo
status: revisado
atualizado: 2026-10-07
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
- Os itens marcados como **por integrante** (6, 7, 8 e 10) viram **uma tarefa por área** (A a D, uma por integrante), com a cota mínima indicada (mínimo, não máximo; [ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md) e [ADR-0006](../docs/adr/0006-divisao-por-areas.md)).
- A ordem e os bloqueios entre tarefas estão na **seção 4**.
- O corpo de cada tarefa deve copiar os IDs dos critérios correspondentes (ex.: `C07.1` a `C07.7`), para que o checklist acompanhe a tarefa.

### 0.2 Para quem escreve um item
- Antes de começar, leia o [`CONTEXT.md`](../CONTEXT.md), a seção do item e o checklist dele.
- Um item só está pronto quando **todos** os critérios dele estão atendidos **e** a consistência da seção 5 foi conferida para ele.

### 0.3 Protocolo de execução e verificação (obrigatório para agentes de IA)

Este protocolo reúne boas práticas para agentes de IA: manter uma lista de tarefas persistente, não tratar uma mensagem de status como conclusão e verificar a conclusão contra uma condição declarada no início.

1. **Condição de conclusão.** O trabalho só está concluído quando **todos** os critérios aplicáveis deste arquivo (IDs `Cxx.y` e `X.y`) estiverem marcados como atendidos, cada um com evidência. Qualquer outro estado é "em andamento".
2. **Lista de tarefas antes de começar.** Antes de produzir qualquer coisa, crie uma lista de tarefas com **um item por ID de critério** no escopo pedido. Não agrupe critérios em um único item.
3. **Evidência por critério.** Um critério só pode ser marcado como atendido com evidência concreta: seção do documento, quantidade contada (ex.: "16 RFs, RF-A1 a RF-D4"), nome do arquivo do diagrama. "Feito" sem evidência não conta.
4. **Contagem por comando, não por estimativa.** Todo critério com número mínimo (≥3, ≥16, ≥2 por estória etc.) deve ser conferido contando de fato: listar e contar os itens, não estimar.
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
| Prazo | **Sábado, 10/10/2026, 23:59** |
| Valor | 5,0 pontos (Somativa 1) |
| Envio | Único para o grupo inteiro; tentativas ilimitadas até o prazo; formato definido na seção 6 (A3) |
| Recuperação do RA1 | Reentrega até 28/11 (nota máxima 7,0 na recuperação; plano de ensino, seção 4) |
| Produto | Plataforma de Cursos (repositório `plataforma-cursos-docs`) |

### 1.1 Integrantes

| Integrante | GitHub | Área |
|---|---|---|
| Adrian Antônio de Souza Gomes | `adrian69-droid` | A definir |
| Lucas Bruno e Silva | `Luc-Bruno` | A definir |
| Lucas Stopinski da Silva | `LucasStop` | A definir |
| Vinicius Lima Teider | a informar | A definir |

O responsável por cada área (A a D) fica no [README](../README.md) e é preenchido quando o grupo distribuir as áreas. Este arquivo não nomeia responsável por área.

### 1.2 Fontes (em ordem de prioridade quando houver conflito)

1. Página da tarefa no Canvas, "Avaliação do RA 1 - Projeto", com a rubrica "Atividades do RA 1". Os pesos e os critérios "Excede" da seção 3 vêm desta página e **precisam ser conferidos com ela** (seção 6, A4); a cópia local não está no repositório.
2. Template oficial do documento de especificação (a versão preenchida mais recente é a v11, `Documento de Especificação - Versões/v11 - Correção de extend, BPMN e atividades.docx`, fora do git). Os títulos dos itens 1 a 11 desta entrega são os do template.
3. Plano de ensino: `BSI_PE_Especificacao de Software_2026_2 - v3.pdf` (seções 4, 5 e 7.1).
4. Decisões do grupo: [`docs/adr/`](../docs/adr/README.md) e [`CONTEXT.md`](../CONTEXT.md). Sobre conteúdo do produto, valem acima do template preenchido (CONTEXT, seção 6, regra 1); a v11 é rascunho anterior ao repositório.

Quando o plano de ensino e uma decisão do grupo divergirem, vale o que for mais exigente para a nota (ex.: o plano pede no mínimo 8 casos de uso; o grupo adotou no mínimo 16).

---

## 2. Regras gerais (valem para o documento inteiro)

- [ ] **X.1 — Template.** O documento final (PDF consolidado a partir dos MDs do repositório) segue a estrutura do template oficial: seções na ordem de 1 a 11, títulos originais e quadros no formato do template.
- [ ] **X.2 — Capa.** Nome do produto (**Plataforma de Cursos**) no lugar de "NOME DO PRODUTO DE SOFTWARE", os 4 autores no lugar de "NOME AUTOR 1..4" e ano **2026** (o template traz 2025).
- [ ] **X.3 — Textos em azul.** Todos os textos personalizáveis (em azul) foram substituídos e estão na cor **preta**.
- [ ] **X.4 — Textos em laranja.** Todos os quadros de aviso e textos de orientação em **laranja** foram removidos.
- [ ] **X.5 — Exemplos do template.** Os exemplos do template foram removidos ou substituídos, por exemplo RF1 "Realizar login de usuário" com o ator genérico e as estórias US001/US002 de exemplo. Um RF de login do próprio sistema existe (área A), escrito para o nosso contexto.
- [ ] **X.6 — Sumário.** O sumário está atualizado, com números de página corretos.
- [ ] **X.7 — Declaração de uso de IA.** O documento contém a declaração obrigatória (plano de ensino, seção 7.1): *"Durante a preparação deste [TIPO DE CONTEÚDO], o(s) autor(es) usaram [FERRAMENTA, VERSÃO] para [EXPLICITAR MOTIVOS]. Após usar essa ferramenta, o(s) autor(es) revisaram e editaram o conteúdo conforme necessário e assumem total responsabilidade pelo conteúdo."*, preenchida.
- [ ] **X.8 — Regra dos 4 por integrante.** Nos itens que dependem da quantidade de integrantes, o mínimo é **4 itens por integrante**, sem máximo. Com 4 integrantes, o mínimo é **16** (itens 6, 7, 8 e 10; ADR-0001).
- [ ] **X.9 — Nome do produto.** O nome **Plataforma de Cursos** (exatamente assim) aparece em todos os campos "NOME DO PRODUTO" / "PRODUTO" dos quadros.
- [ ] **X.10 — Legibilidade dos diagramas.** Os diagramas (itens 4, 9 e 11) estão legíveis no documento final, sem texto cortado ou ilegível. As imagens são geradas a partir do código-fonte versionado, nunca editadas à mão (ADR-0004).

---

## 3. Critérios por item

Cada item traz: o que o template pede, o mínimo exigido, o peso na nota e o checklist com o critério **"Excede"** (nota máxima) da rubrica.

Resumo dos pesos:

| Item | Peso | Por integrante? |
|---|---|---|
| 1 – Quadro "3 Objetivos" | 0,2 | Não |
| 2 – Quadro "É – Não é – Faz – Não faz" | 0,2 | Não |
| 3 – Visão do Produto | 0,2 | Não |
| 4 – Mapeamento de Negócios | 0,2 | Não |
| 5 – Relação de Atores / Usuários | 0,2 | Não |
| 6 – Relação de Requisitos Funcionais | 0,5 | **Sim (≥16)** |
| 7 – Relação de Estórias de Usuário | **1,5** | **Sim (≥16)** |
| 8 – Relação de Requisitos Não-Funcionais | 0,1 | **Sim (≥16)** |
| 9 – Diagrama Geral de Casos de Uso | 0,2 | Não |
| 10 – Especificações de Caso de Uso | **1,5** | **Sim (≥16)** |
| 11 – Diagrama de Atividades | 0,2 | Não |
| **Total** | **5,0** | |

### 3.1 Item 1 — Quadro "3 Objetivos" (0,2)

**Template:** tabela "QUADRO 3 OBJETIVOS" com NOME DO PRODUTO e as colunas OBJETIVOS / DESCRIÇÃO, linhas 1, 2 e 3. Relaciona os 3 grandes **objetivos de negócio** que o produto deve atender.

- [ ] **C01.1** Exatamente **3** objetivos.
- [ ] **C01.2** Cada objetivo é claro, específico e **verificável**.
- [ ] **C01.3** Cada objetivo articula **problema, valor e métrica de sucesso**: a métrica é explícita e mensurável.
- [ ] **C01.4** Os objetivos são coerentes com a Visão do Produto (item 3) e com os demais artefatos.

### 3.2 Item 2 — Quadro "É – Não é – Faz – Não faz" (0,2)

**Template:** quadro de 4 quadrantes. É = atributos necessários ou desejados; Não é = atributos indesejados ou impeditivos; Faz = ações ou capacidades esperadas; Não faz = ações ou capacidades indesejadas ou não permitidas.

- [ ] **C02.1** Os 4 quadrantes estão preenchidos.
- [ ] **C02.2** Cada quadrante tem **≥3 itens específicos**, não genéricos.
- [ ] **C02.3** Não há contradição entre quadrantes nem com os outros itens.
- [ ] **C02.4** O quadro delimita claramente escopo, anti-escopo, capacidades e restrições. O "Não faz" é coerente com o fora de escopo vigente do projeto (CONTEXT, seção 1): sem pagamento, sem emissão de certificado com validade legal e sem aplicativo móvel nativo, salvo decisão registrada em contrário. O Tutor de IA entra como ator sistêmico (ADR-0005), não como funcionalidade humana.

### 3.3 Item 3 — Visão do Produto (0,2)

**Template:** dois quadros.
- Quadro A: **PROBLEMAS** (estado atual, antes da solução) e **EXPECTATIVAS** (estado desejado, alinhado aos problemas).
- Quadro B: **CLIENTE-ALVO**, **CATEGORIA-SEGMENTO**, **BENEFÍCIO-CHAVE**, **DIFERENCIAL-CHAVE** e **META-VALOR**. Usar os rótulos exatamente como estão no template (a v11 grafa "DIFERENCIADO-CHAVE" e "META-VALOR."; conferir e corrigir).

- [ ] **C03.1** O quadro A está completo: problemas e expectativas bem definidos.
- [ ] **C03.2** Cada expectativa corresponde a pelo menos um problema levantado.
- [ ] **C03.3** Os 5 campos do quadro B estão preenchidos com precisão.
- [ ] **C03.4** Valor (meta-valor) e diferencial são **verificáveis**, não apenas slogans. O diferencial (Tutor de IA no contexto da aula) é confirmado ou ajustado pela pesquisa ([lacunas e diferencial](../pesquisa/similares/lacunas-e-diferencial.md)).
- [ ] **C03.5** Os dois quadros são coerentes entre si e com os itens 1 e 2.

### 3.4 Item 4 — Mapeamento de Negócios (0,2)

**Template:** diagrama **BPMN** do processo de negócio na versão **TO BE**, ou seja, como o processo fica com o sistema. Arquivo `.bpmn` (BPMN 2.0), editável no bpmn.io ou no Camunda Modeler (ADR-0004).

- [ ] **C04.1** A notação é BPMN de verdade, não um fluxograma improvisado.
- [ ] **C04.2** O diagrama representa apenas o TO BE, sem misturar com o AS IS.
- [ ] **C04.3** Tem evento de **início** e de **fim**.
- [ ] **C04.4** Tem **atividades** rotuladas de forma padronizada (verbo no infinitivo + objeto).
- [ ] **C04.5** Tem **gateways com condições** escritas nas saídas.
- [ ] **C04.6** Tem **pools/lanes** coerentes com os atores do item 5.
- [ ] **C04.7** Tem eventos e mensagens quando aplicável, por exemplo a pergunta do Aluno ao Tutor de IA e a resposta com o contexto da aula.
- [ ] **C04.8** O caminho principal está representado (do curso publicado ao Aluno que estuda, é avaliado e tira dúvidas com o Tutor de IA); o nível de detalhe é adequado e o diagrama é legível.
- [ ] **C04.9** É consistente com a Visão do Produto.

### 3.5 Item 5 — Relação de Atores / Usuários (0,2)

**Template:** tabela `# | ATOR / USUÁRIO`.

- [ ] **C05.1** **≥3 atores**.
- [ ] **C05.2** Cada ator tem **papel e responsabilidades** descritos. Como a tabela do template só tem nome, acrescentar descrição, em coluna extra ou texto abaixo.
- [ ] **C05.3** Cada ator tem sua relação com o processo e com o sistema explicitada.
- [ ] **C05.4** As descrições são sucintas, sem ambiguidade e sem sobreposição de papéis.
- [ ] **C05.5** Os atores são os mesmos usados nas lanes do BPMN (item 4), nos RFs (item 6), nas estórias (item 7) e nos casos de uso (itens 9 e 10).

Referência do projeto (já definida pelo grupo, CONTEXT seção 2): **Visitante**, **Aluno**, **Instrutor**, **Administrador** e o ator não humano **Tutor de IA** (ator sistêmico, [ADR-0005](../docs/adr/0005-tutor-de-ia-como-ator-sistemico.md)). Os nomes são idênticos em todos os itens.

### 3.6 Item 6 — Relação de Requisitos Funcionais (0,5) · por integrante

**Template:** tabela `# | REQUISITO FUNCIONAL | ATOR / USUÁRIO | SPRINT`. Relacionar **todos** os requisitos do sistema completo.

- [ ] **C06.1** **≥16 RFs** (no mínimo 4 por integrante, sem máximo; ADR-0001).
- [ ] **C06.2** Enumeração sequencial e sem lacunas no documento final: **RF001, RF002…**. Durante a escrita vale o ID provisório por área (RF-A1, RF-A2…), em sequência dentro da área; a renumeração única (RF001…) é aplicada no início do T12 e registrada em `entregas/ra1-renumeracao.md` (ADR-0001).
- [ ] **C06.3** Cada RF está redigido de forma clara e **testável**: uma ação verificável, sem "etc." e sem termos vagos.
- [ ] **C06.4** Cada RF é rastreado a um **ator** (coluna preenchida, com ator do item 5).
- [ ] **C06.5** Cada RF é rastreado a um **objetivo** do item 1, na coluna **OBJETIVO** acrescentada à tabela do template.
- [ ] **C06.6** A **priorização** está presente: coluna SPRINT preenchida e/ou prioridade. A coluna fica vazia enquanto as áreas escrevem; o grupo divide em sprints na consolidação (T06), depois que todos os RFs e RNFs estiverem definidos.
- [ ] **C06.7** Há uma **breve justificativa** da priorização.
- [ ] **C06.8** Os RFs cobrem o núcleo do produto: cadastro de curso, módulos, aulas e quiz com gabarito; matrícula, progresso e avaliação do curso; correção automática do quiz; conversa com o Tutor de IA no contexto da aula; dashboard com filtro; gestão de usuários e perfis; acesso a área protegida por perfil. Não se limitam a CRUD.
- [ ] **C06.9** Nenhum RF descreve atributo de qualidade (desempenho, segurança, usabilidade etc.): isso é RNF e vai para o item 8. O RF descreve o que o sistema faz (plano de ensino, ID1.3).

### 3.7 Item 7 — Relação de Estórias de Usuário (1,5) · por integrante

**Template:** para cada estória, `USnnn – REQUISITO n: <nome>` (durante a escrita, `US-<área><n> – REQUISITO RF-<área><n>: <nome>`; ADR-0001), **COMO / POSSO / PARA** e Critérios de Aceite numerados em **DADO QUE / QUANDO / ENTÃO** (ADR-0002).

- [ ] **C07.1** **≥16 estórias** (no mínimo 4 por integrante e sempre uma por RF; ADR-0001).
- [ ] **C07.2** Todas no formato **COMO / POSSO / PARA**.
- [ ] **C07.3** Cada estória está vinculada a um RF correspondente, com o número do RF no título. Durante a escrita, a estória usa o ID provisório com o mesmo número do RF (US-A1 ↔ RF-A1); no documento final, US001 ↔ RF001 (ADR-0001).
- [ ] **C07.4** Cada estória tem **≥2 critérios de aceite**.
- [ ] **C07.5** Todos os critérios estão no formato **DADO QUE / QUANDO / ENTÃO**, claros e **verificáveis**, com resultado observável.
- [ ] **C07.6** Os critérios cobrem cenários diferentes (caminho principal e ao menos uma variação ou erro), e não repetições do mesmo cenário.
- [ ] **C07.7** As estórias são consistentes com as outras especificações: atores, RFs e casos de uso.

### 3.8 Item 8 — Relação de Requisitos Não-Funcionais (0,1) · por integrante

**Template:** tabela `# | REQUISITO NÃO-FUNCIONAL | NORMA ISO/IEC 25010`. O plano de ensino exige a classificação pela ISO/IEC 25010. Usar as características da edição vigente (25010:2023, como na v11) e acrescentar a coluna de métrica ou critério de aceitação.

- [ ] **C08.1** **≥16 RNFs** (no mínimo 4 por integrante, sem máximo; ADR-0001).
- [ ] **C08.2** Enumeração **RNF001, RNF002…** no documento final. Durante a escrita vale o ID provisório por área (RNF-A1, RNF-A2…); a renumeração única é aplicada no início do T12 (ADR-0001).
- [ ] **C08.3** Cada RNF está classificado em uma característica da **ISO/IEC 25010**.
- [ ] **C08.4** Cada RNF é **mensurável**, com medida ou critério de aceitação objetivo (ex.: tempo de resposta ≤ X s no percentil 95). Nada de "ser rápido" ou "ser seguro".
- [ ] **C08.5** Os RNFs das quatro áreas somados cobrem, no mínimo, eficiência de desempenho, segurança/LGPD, confiabilidade, capacidade de interação (usabilidade) e manutenibilidade. Sugestão por área ([ADR-0006](../docs/adr/0006-divisao-por-areas.md)): A segurança (LGPD) e compatibilidade; B manutenibilidade e portabilidade; C capacidade de interação e acessibilidade; D eficiência de desempenho e confiabilidade.
- [ ] **C08.6** Nenhum RNF descreve funcionalidade (ação do sistema ou do ator): isso é RF e vai para o item 6 (plano de ensino, ID1.3).

### 3.9 Item 9 — Diagrama Geral de Casos de Uso (0,2)

**Template:** diagrama geral considerando **generalização de atores** e **inclusão e extensão** de casos de uso. Código em Mermaid (ADR-0004).

- [ ] **C09.1** Tem **fronteira do sistema** com o nome do produto.
- [ ] **C09.2** Os atores estão corretos e são os mesmos do item 5.
- [ ] **C09.3** Os casos de uso principais correspondem aos RFs (≈ RF).
- [ ] **C09.4** Tem **generalização de atores** onde fizer sentido, como o template pede.
- [ ] **C09.5** Tem relacionamentos **include/extend** onde forem pertinentes, com a direção correta das setas: o «extend» segue o sentido do material da disciplina (TE3_3), com a seta saindo do caso de uso base para o estendido ([ADR-0003](../docs/adr/0003-extend-no-sentido-do-te3-3.md)).
- [ ] **C09.6** Os nomes dos casos de uso são consistentes com os RFs e as estórias.
- [ ] **C09.7** O diagrama é legível.
- [ ] **C09.8** Há **≥16 casos de uso** no diagrama, número que permite uma especificação (item 10) por caso de uso (C10.1).

### 3.10 Item 10 — Especificações de Caso de Uso (1,5) · por integrante

**Template:** para cada caso de uso, no formato reduzido: **Nome, Ator(es), Descrição, Pré-condições, Pós-condições, Regras de negócio, Protótipo(s) de tela, Fluxo básico, Fluxos alternativos, Fluxos de exceção**. O plano de ensino pede **protótipos de tela de alta fidelidade**.

- [ ] **C10.1** **≥16 especificações** (no mínimo 4 por integrante × 4 integrantes, sem máximo; ADR-0001). Decisão fechada pelo grupo; o "mínimo 8" do plano de ensino não se aplica.
- [ ] **C10.2** Cada especificação tem os **10 campos** preenchidos.
- [ ] **C10.3** Cada especificação tem **protótipo(s) de tela de alta fidelidade**.
- [ ] **C10.4** Cada especificação tem **fluxo básico** completo, em passos numerados.
- [ ] **C10.5** Cada especificação tem ao menos um **fluxo alternativo** (variação intencional do ator).
- [ ] **C10.6** Cada especificação tem ao menos um **fluxo de exceção** (variação não intencional ou erro).
- [ ] **C10.7** A linguagem é testável: cada passo é observável.
- [ ] **C10.8** Cada especificação corresponde a um caso de uso do diagrama (item 9), com o mesmo nome e os mesmos atores.
- [ ] **C10.9** As regras de negócio são coerentes com as estórias e os RFs.

### 3.11 Item 11 — Diagrama de Atividades (0,2)

**Template:** diagrama de atividades do sistema, em notação UML. Código em Mermaid (ADR-0004).

- [ ] **C11.1** Representa o **fluxo principal**.
- [ ] **C11.2** Representa os **fluxos alternativos**.
- [ ] **C11.3** Tem **decisões** com **condições de guarda** escritas.
- [ ] **C11.4** Tem **atividades paralelas** (fork/join) onde houver ramos concorrentes, por exemplo o Aluno assistir à aula enquanto o Tutor de IA está disponível para dúvidas.
- [ ] **C11.5** Tem **responsabilidades** (partições/raias) coerentes com os atores.
- [ ] **C11.6** A notação UML é usada corretamente: nó inicial e final, ações, decisão/merge, fork/join.
- [ ] **C11.7** É legível e aderente à documentação (atores, casos de uso, BPMN).

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
- **Por integrante (no mínimo 4 cada, sem máximo; ADR-0001):** itens 6, 7, 8 e 10. Cada integrante fica com uma área (A a D, ADR-0006) e, nela, com RFs, estórias, RNFs e especificações de caso de uso. Isso mantém a rastreabilidade RF → estória → caso de uso na mesma pessoa.
- **Integração:** os itens 9 e 11 consolidam o trabalho de todos, então precisam de um responsável que junte as partes.
- **Janela de tempo:** o prazo final é 10/10/2026, 23:59. Pendência cruzada aberta (label `pendencia-cruzada`) bloqueia a consolidação do item.

---

## 5. Checklist final de consistência cruzada

Executar depois que todos os itens estiverem prontos, e de novo antes do envio.

- [ ] **K.1** Os mesmos atores (nomes idênticos) aparecem nos itens 4, 5, 6, 7, 9, 10 e 11.
- [ ] **K.2** Todo RF (item 6) tem **exatamente uma** estória (item 7) e toda estória aponta para um RF existente.
- [ ] **K.3** Todo RF está coberto por **pelo menos um** caso de uso no diagrama (item 9).
- [ ] **K.4** Toda especificação (item 10) corresponde a um caso de uso do diagrama (item 9), com o mesmo nome.
- [ ] **K.5** Os critérios de aceite das estórias não contradizem as regras de negócio nem os fluxos das especificações do mesmo requisito.
- [ ] **K.6** Os objetivos (item 1) são atendidos por algum RF e aparecem refletidos na Visão (item 3).
- [ ] **K.7** Nada listado em "Não faz" (item 2) aparece como RF, estória ou caso de uso.
- [ ] **K.8** As lanes do BPMN (item 4) e as raias do diagrama de atividades (item 11) usam os atores do item 5.
- [ ] **K.9** As contagens mínimas conferem por contagem real: RF ≥16, estórias ≥16, cada estória com ≥2 critérios, RNF ≥16, casos de uso no diagrama ≥16, especificações ≥16.
- [ ] **K.10** Todos os critérios gerais X.1 a X.10 estão atendidos.
- [ ] **K.11** Nenhum item contradiz o `CONTEXT.md` nem as decisões D1–D6 (`docs/adr/`), e todo número, preço ou recurso de concorrente usado na especificação cita a fonte da pesquisa (`pesquisa/fontes.md`).
- [ ] **K.12** Não há issue aberta com o rótulo `pendencia-cruzada`: toda amarração entre áreas foi resolvida, com o ID do requisito que a atende ou com a decisão do grupo registrada (`entregas/ra1-tarefas.md`, seção 1.4).
- [ ] **K.13** A renumeração única foi aplicada (RF001…, US001…, RNF001…, UC001…), não restou ID provisório (`-A1`, `-B2`…) em nenhum arquivo e `entregas/ra1-renumeracao.md` lista a correspondência provisório → final.

---

## 6. Pontos em aberto

- ~~**A1.** Quantidade de especificações de caso de uso.~~ **Resolvido:** no mínimo 16 (4 por integrante × 4 integrantes); sem máximo (ADR-0001).
- ~~**A2.** Quais itens são "dependentes da quantidade de integrantes".~~ **Resolvido:** itens 6, 7, 8 e 10 (ADR-0001 e ADR-0006).
- **A3.** Formato de envio. Proposta: **PDF**, gerado a partir da consolidação dos arquivos MD do repositório, seguindo a estrutura do template. Confirmar com o grupo.
- **A4.** Revisão contra a rubrica: o texto da rubrica "Atividades do RA 1" do Canvas não está no repositório, então esta revisão conferiu o arquivo só contra o plano de ensino (seções 3, 4 e 5: ID1.1 a ID1.4 e as atividades das aulas 3 a 9) e contra os ADRs. Pesos, critérios "Excede" e formatos aceitos de envio foram trazidos do modelo de outro grupo e do plano de ensino; conferir com a página da tarefa no Canvas e ajustar este arquivo.
- **A5.** Responsável de cada área (A a D): "A definir" no [README](../README.md).

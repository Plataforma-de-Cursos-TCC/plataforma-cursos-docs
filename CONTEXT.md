---
id: contexto
titulo: "Contexto do projeto: leia antes de qualquer tarefa"
tipo: contexto
status: vigente
atualizado: 2026-10-08
relacionados: [mapa-pesquisa, adr-indice, adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006]
---
# Contexto do projeto

> Leia este arquivo **antes de qualquer tarefa de documentação**. Ele resume o que está decidido e aponta onde está o detalhe. É curto de propósito: abra só o que o seu item pede (tabela da seção 8).

## 1. Produto

- **Nome (sempre exatamente assim):** Plataforma de Cursos.
- **O que é:** sistema web de cursos online. O Instrutor publica cursos organizados em módulos e aulas, com quiz e gabarito; o Aluno se matricula, assiste às aulas, responde aos quizzes, avalia o curso e tira dúvidas com o Tutor de IA no contexto da aula.
- **Diferencial pretendido:** o Tutor de IA responde com base no conteúdo da aula que o Aluno está assistindo, e não como um chat genérico. A pesquisa de mercado ([lacunas e diferencial](pesquisa/similares/lacunas-e-diferencial.md)) confirma ou ajusta este ponto.
- **Fora de escopo:** a lista vigente fica no item 2 da especificação (É / Não é / Faz / Não faz). O pagamento da matrícula é apenas simulado (sem cobrança real), e não há emissão de certificado com validade legal nem aplicativo móvel nativo.

## 2. Atores (nomes idênticos em todos os itens)

| Ator | Papel |
|---|---|
| **Usuário** | Ator geral (generalização) de Aluno, Instrutor e Administrador: quem tem conta e faz login e edita o próprio perfil. |
| **Visitante** | Pessoa sem conta ou sem sessão; navega pelo que é público e cadastra-se. Depois do login, atua como Usuário. |
| **Aluno** | Matricula-se em cursos, assiste às aulas, responde aos quizzes, avalia cursos e conversa com o Tutor de IA. |
| **Instrutor** | Cadastra cursos, módulos, aulas e quizzes com gabarito; acompanha o desempenho dos alunos no dashboard. |
| **Administrador** | Gerencia usuários e perfis de acesso; vê o dashboard da plataforma; não produz conteúdo de curso. |
| **Tutor de IA** | Ator sistêmico (não humano): recebe a pergunta do Aluno com o contexto da aula e devolve a resposta. |

Decisão: [ADR-0005](docs/adr/0005-tutor-de-ia-como-ator-sistemico.md).

## 3. Glossário mínimo

| Termo | Significado no projeto |
|---|---|
| Curso | Conjunto publicado por um Instrutor, organizado em módulos. |
| Módulo | Agrupamento ordenado de aulas dentro de um curso. |
| Aula | Unidade de conteúdo (vídeo e material) dentro de um módulo; é o contexto do Tutor de IA. |
| Quiz | Conjunto de questões ligado a uma aula ou módulo, com gabarito cadastrado pelo Instrutor. |
| Gabarito | Resposta correta de cada questão do quiz, usada na correção automática. |
| Matrícula | Vínculo entre um Aluno e um curso; libera o acesso às aulas. |
| Progresso | Aulas concluídas e notas de quiz de um Aluno em um curso. |
| Avaliação do curso | Nota e comentário que o Aluno dá ao curso. |
| Dashboard | Painel com indicadores e filtro, para o Instrutor (seus cursos) e para o Administrador (plataforma). |
| Área protegida | Parte do sistema acessível só a quem tem sessão e o perfil certo. |

## 4. Decisões vigentes

| | Decisão | ADR |
|---|---|---|
| D1 | **Meta interna de 4 por integrante** (mínimo oficial: 8 especificações de caso de uso); numeração final da v11 (RF001, US001, RNF001, UC001), com IDs novos no fim (RF017…) | [0001](docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md) |
| D2 | Estória no formato **Como / Posso / Para**, com **pelo menos 2 critérios** DADO QUE / QUANDO / ENTÃO | [0002](docs/adr/0002-formato-de-estoria-e-criterios.md) |
| D3 | **«extend»** no sentido do TE3_3 e da UML: a seta sai do caso de uso opcional e aponta para o base | [0003](docs/adr/0003-extend-no-sentido-do-te3-3.md) |
| D4 | **Diagramas como código**: BPMN 2.0 (`.bpmn`) no item 4, PlantUML (`.puml`) nos itens 9 e 11, PNG gerado da fonte | [0004](docs/adr/0004-diagramas-como-codigo.md) |
| D5 | **Tutor de IA como ator sistêmico** | [0005](docs/adr/0005-tutor-de-ia-como-ator-sistemico.md) |
| D6 | **Divisão por áreas A a D**, uma por integrante | [0006](docs/adr/0006-divisao-por-areas.md) |

## 5. Áreas

| Área | Escopo | Casos de uso de partida |
|---|---|---|
| A | Acesso e conta | Cadastrar-se, Realizar login, Recuperar senha, Editar dados do perfil |
| B | Autoria do instrutor | Cadastrar curso, Gerenciar módulos, Gerenciar aulas, Cadastrar quiz com gabarito |
| C | Aprendizagem do aluno | Matricular-se em curso, Assistir aula, Responder quiz, Avaliar curso |
| D | Tutor de IA, analytics e administração | Conversar com Tutor de IA, Ver dashboard com filtro, Gerenciar usuários, Acessar área protegida por perfil |

O responsável por cada área está no [README](README.md). Os itens 1 a 5, 9 e 11 são do grupo: quem puxar a tarefa escreve, e outro integrante revisa.

## 6. Regras para quem escreve (pessoas e IAs)

1. **Precedência:** decisões ([docs/adr/](docs/adr/README.md)) > pesquisa vigente ([pesquisa/](pesquisa/README.md)) > rascunhos e textos antigos (inclusive as versões `.docx` anteriores ao repositório).
2. **Não contradiga uma decisão.** Se algo pedir mudança, registre a dúvida para o grupo em vez de mudar o texto.
3. **Cite a fonte** ao usar número, preço ou recurso de concorrente, pelo número de [pesquisa/fontes.md](pesquisa/fontes.md).
4. **Separe fato de inferência** quando o texto não for óbvio: [Fato] e [Inferência].
5. **Use os nomes exatos** do produto, dos atores e do glossário.

## 7. Onde fica cada coisa

- **Especificação (a entrega):** [especificacao/](especificacao/)
- **Decisões:** [docs/adr/README.md](docs/adr/README.md)
- **Pesquisa de mercado:** [pesquisa/README.md](pesquisa/README.md); fontes em [pesquisa/fontes.md](pesquisa/fontes.md)
- **Plano e critérios do RA1:** [entregas/ra1-tarefas.md](entregas/ra1-tarefas.md), [entregas/ra1-criterios-de-aceite.md](entregas/ra1-criterios-de-aceite.md)
- **Documentos de projeto:** [docs/prd.md](docs/prd.md), [docs/sdd.md](docs/sdd.md), [docs/tdd.md](docs/tdd.md), [docs/ssd/](docs/ssd/README.md), [docs/testes/](docs/testes/estrategia.md), [docs/design-system.md](docs/design-system.md)
- **Grafo** (quando existir): `graphify-out/GRAPH_REPORT.md` e `graphify-out/graph.html`. Use para achar o que ler; decida pelos arquivos.

## 8. O que ler para cada item

D1 e D6 valem para todos os itens com parte por integrante (6, 7, 8 e 10).

| Item | Leia | Decisões |
|---|---|---|
| 1 - 3 Objetivos | [lacunas e diferencial](pesquisa/similares/lacunas-e-diferencial.md) | |
| 2 - É / Não é / Faz / Não faz | [lacunas e diferencial](pesquisa/similares/lacunas-e-diferencial.md), [matriz](pesquisa/similares/matriz-comparativa.md) | D5 |
| 3 - Visão do Produto | [similares](pesquisa/similares/README.md), [matriz](pesquisa/similares/matriz-comparativa.md), [lacunas e diferencial](pesquisa/similares/lacunas-e-diferencial.md) | |
| 4 - BPMN TO BE | seção 2 e glossário deste arquivo | D4 |
| 5 - Atores | seção 2 deste arquivo | D5 |
| 6 - RFs | seção 5 (linha da sua área), [matriz](pesquisa/similares/matriz-comparativa.md) | D1, D6 |
| 7 - Estórias | RFs da sua área | D1, D2, D6 |
| 8 - RNFs | RFs da sua área | D1, D6 |
| 9 - Casos de uso | seções 2 e 5 deste arquivo | D3, D4, D5 |
| 10 - Especificações de caso de uso | caso de uso da sua área no item 9 | D1, D3, D6 |
| 11 - Diagrama de atividades | item 10 | D4 |

# 7 RELAÇÃO DE ESTÓRIAS DE USUÁRIO – ÁREA D (Tutor de IA, analytics e administração)

O template exige uma estória de usuário por requisito funcional, com critérios de aceite. Formato Como / Posso / Para, com pelo menos 2 critérios (ADR-0002).

<!-- revisar: a v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) -->

Área D: Tutor de IA, analytics e administração. Responsável: Vinicius Lima Teider (`Teider011`). IDs: US-Dn, uma por RF da área, com o mesmo número (US-D1 ↔ RF-D1).

## US-D1 (US012) – REQUISITO RF-D1 (RF009): Conversar com Tutor de IA

**COMO:** Aluno matriculado num curso
**QUERO:** conversar com o Tutor de IA daquele curso
**PARA:** que eu possa tirar dúvida sobre o conteúdo sem esperar resposta do instrutor.
**PRIORIDADE:** Could Have
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou numa aula do curso em que sou matriculado <br> **QUANDO:** pergunto algo relacionado ao conteúdo <br> **ENTÃO:** recebo resposta com citação da aula e do timestamp de origem. |
| 2 | **DADO QUE:** pergunto algo fora do conteúdo do curso <br> **QUANDO:** envio a mensagem <br> **ENTÃO:** o tutor responde que não tem essa informação no material do curso. |
| 3 | **DADO QUE:** excedo o limite de mensagens por período (rate limit) <br> **QUANDO:** tento enviar nova pergunta <br> **ENTÃO:** recebo aviso de limite atingido. |

## US-D2 (US013) – REQUISITO RF-D2 (RF010): Ver dashboard com filtro

**COMO:** Instrutor
**QUERO:** ver o dashboard da minha turma com filtro de período
**PARA:** que eu possa decidir o que ajustar no curso com base em dado real.
**PRIORIDADE:** Should Have
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho alunos matriculados <br> **QUANDO:** seleciono um intervalo de datas <br> **ENTÃO:** vejo progresso e engajamento agregados só daquele período. |
| 2 | **DADO QUE:** nenhum aluno teve atividade no período selecionado <br> **QUANDO:** aplico o filtro <br> **ENTÃO:** vejo estado vazio claro, não erro. |
| 3 | **DADO QUE:** tenho mais de um curso <br> **QUANDO:** acesso o dashboard <br> **ENTÃO:** consigo filtrar também por curso, além do período. |

## US-D3 (US015) – REQUISITO RF-D3 (RF012): Acessar área protegida por perfil

**COMO:** Usuário autenticado
**QUERO:** acessar apenas as áreas e rotas permitidas pro meu perfil (aluno/instrutor/admin)
**PARA:** que eu possa ter uma experiência segura e sem acesso indevido a dados de outros perfis.
**PRIORIDADE:** Must Have
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou logado como aluno <br> **QUANDO:** tento acessar uma rota exclusiva de instrutor <br> **ENTÃO:** recebo erro de acesso negado e sou redirecionado pra minha área. |
| 2 | **DADO QUE:** estou logado como instrutor <br> **QUANDO:** acesso minha área <br> **ENTÃO:** vejo meu nome e perfil (role) visíveis na interface. |
| 3 | **DADO QUE:** meu token expira enquanto navego numa rota protegida <br> **QUANDO:** tento uma ação <br> **ENTÃO:** sou redirecionado pra login sem exposição de dados da rota. |

## US-D4 (US016) – REQUISITO RF-D3 (RF012): Gerenciar usuários

**COMO:** Administrador
**QUERO:** gerenciar os usuários da plataforma
**PARA:** que eu possa manter o ambiente seguro e organizado.
**PRIORIDADE:** Should Have
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou logado como admin <br> **QUANDO:** busco um usuário e altero seu status pra bloqueado <br> **ENTÃO:** o acesso dele é revogado imediatamente. |
| 2 | **DADO QUE:** tento bloquear minha própria conta admin <br> **QUANDO:** confirmo a ação <br> **ENTÃO:** o sistema impede e mostra aviso. |
| 3 | **DADO QUE:** um usuário é excluído <br> **QUANDO:** a exclusão é confirmada <br> **ENTÃO:** seus dados pessoais são removidos mas o histórico de matrícula/pagamento permanece anonimizado. |

<!-- revisar: 4 estórias para 3 RF(s) na área; a regra "mesmo número do RF" (US-Dn ↔ RF-Dn) não se aplica a US-D4, que têm vários por RF na v11 (ADR 0001). A referência ao RF segue o ID correto -->

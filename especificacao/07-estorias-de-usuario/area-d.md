## US012 – REQUISITO RF009: Conversar com Tutor de IA

**COMO:** Aluno matriculado em um curso\
**POSSO:** conversar com o Tutor de IA daquele curso\
**PARA:** tirar dúvidas sobre o conteúdo sem esperar a resposta do Instrutor.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou em uma aula do curso em que sou matriculado <br> **QUANDO:** pergunto algo relacionado ao conteúdo <br> **ENTÃO:** recebo resposta que cita a aula e o minuto do vídeo de origem. |
| 2 | **DADO QUE:** pergunto algo fora do conteúdo do curso <br> **QUANDO:** envio a mensagem <br> **ENTÃO:** o Tutor de IA responde que não tem essa informação no material do curso. |
| 3 | **DADO QUE:** excedo o limite de mensagens por período <br> **QUANDO:** tento enviar nova pergunta <br> **ENTÃO:** recebo aviso de limite atingido. |

## US013 – REQUISITO RF010: Ver dashboard com filtro

**COMO:** Instrutor\
**POSSO:** ver o dashboard da minha turma com filtro de período\
**PARA:** decidir o que ajustar no curso com base em dados reais.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho alunos matriculados <br> **QUANDO:** seleciono um intervalo de datas <br> **ENTÃO:** vejo progresso e engajamento agregados só daquele período. |
| 2 | **DADO QUE:** nenhum aluno teve atividade no período selecionado <br> **QUANDO:** aplico o filtro <br> **ENTÃO:** vejo um aviso claro de que não há dados, e não um erro. |
| 3 | **DADO QUE:** tenho mais de um curso <br> **QUANDO:** acesso o dashboard <br> **ENTÃO:** consigo filtrar também por curso, além do período. |

## US015 – REQUISITO RF018: Acessar área protegida por perfil

**COMO:** Usuário autenticado\
**POSSO:** acessar apenas as áreas permitidas para o meu perfil (Aluno, Instrutor ou Administrador)\
**PARA:** ter uma experiência segura, sem acesso indevido a dados de outros perfis.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou logado como Aluno <br> **QUANDO:** tento acessar uma área exclusiva do Instrutor <br> **ENTÃO:** recebo erro de acesso negado e sou direcionado para a minha área. |
| 2 | **DADO QUE:** estou logado como Instrutor <br> **QUANDO:** acesso a minha área <br> **ENTÃO:** vejo o meu nome e o meu perfil na interface. |
| 3 | **DADO QUE:** a minha sessão expira enquanto navego em uma área protegida <br> **QUANDO:** tento uma ação <br> **ENTÃO:** sou direcionado para o login, sem exposição dos dados da área. |

## US016 – REQUISITO RF012: Gerenciar usuários

**COMO:** Administrador\
**POSSO:** gerenciar os usuários da plataforma\
**PARA:** manter o ambiente seguro e organizado.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou logado como Administrador <br> **QUANDO:** busco um usuário e altero o status dele para bloqueado <br> **ENTÃO:** o acesso dele é revogado imediatamente. |
| 2 | **DADO QUE:** tento bloquear a minha própria conta de Administrador <br> **QUANDO:** confirmo a ação <br> **ENTÃO:** o sistema impede e mostra um aviso. |
| 3 | **DADO QUE:** um usuário é excluído <br> **QUANDO:** a exclusão é confirmada <br> **ENTÃO:** os dados pessoais dele são removidos, mas o histórico de matrícula e pagamento permanece anonimizado. |

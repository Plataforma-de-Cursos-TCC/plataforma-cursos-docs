## 18. US012 – REQUISITO RF009: Conversar com Tutor de IA

**COMO:** Aluno matriculado em um curso\
**POSSO:** conversar com o Tutor de IA daquele curso\
**PARA:** tirar dúvidas sobre o conteúdo sem esperar a resposta do Instrutor.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| | |
|---|---|
| 1 | **DADO QUE:** estou em uma aula do curso em que sou matriculado <br> **QUANDO:** pergunto algo relacionado ao conteúdo <br> **ENTÃO:** recebo resposta que cita a aula e o minuto do vídeo de origem. |
| 2 | **DADO QUE:** pergunto algo fora do conteúdo do curso <br> **QUANDO:** envio a mensagem <br> **ENTÃO:** o Tutor de IA responde que não tem essa informação no material do curso. |
| 3 | **DADO QUE:** excedo a cota horária regular de 20 mensagens <br> **QUANDO:** tento enviar nova pergunta sem créditos extras <br> **ENTÃO:** recebo aviso de limite atingido com o tempo restante de espera (Retry-After) e indicação para adquirir créditos extras. |

## 19. US013 – REQUISITO RF010: Ver dashboard com filtro

**COMO:** Instrutor\
**POSSO:** ver o dashboard da minha turma com filtro de período\
**PARA:** decidir o que ajustar no curso com base em dados reais.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| | |
|---|---|
| 1 | **DADO QUE:** tenho alunos matriculados <br> **QUANDO:** seleciono um intervalo de datas <br> **ENTÃO:** vejo progresso e engajamento agregados só daquele período. |
| 2 | **DADO QUE:** nenhum aluno teve atividade no período selecionado <br> **QUANDO:** aplico o filtro <br> **ENTÃO:** vejo um aviso claro de que não há dados, e não um erro. |
| 3 | **DADO QUE:** tenho mais de um curso <br> **QUANDO:** acesso o dashboard <br> **ENTÃO:** consigo filtrar também por curso, além do período. |
| 4 | **DADO QUE:** informo uma data final anterior à data inicial <br> **QUANDO:** aplico o filtro <br> **ENTÃO:** vejo mensagem de erro e o último intervalo válido é mantido. |

## 20. US015 – REQUISITO RF018: Acessar área protegida por perfil

**COMO:** Usuário autenticado\
**POSSO:** acessar apenas as áreas permitidas para o meu perfil (Aluno, Instrutor ou Administrador)\
**PARA:** ter uma experiência segura, sem acesso indevido a dados de outros perfis.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| | |
|---|---|
| 1 | **DADO QUE:** estou logado como Aluno <br> **QUANDO:** tento acessar uma área exclusiva do Instrutor <br> **ENTÃO:** recebo erro de acesso negado e sou direcionado para a minha área. |
| 2 | **DADO QUE:** estou logado como Instrutor <br> **QUANDO:** acesso a minha área <br> **ENTÃO:** vejo o meu nome e o meu perfil na interface. |
| 3 | **DADO QUE:** a minha sessão expira ou meu token está na blocklist enquanto navego em uma área protegida <br> **QUANDO:** tento uma ação <br> **ENTÃO:** sou direcionado para o login, sem exposição dos dados da área. |

## 21. US016 – REQUISITO RF012: Gerenciar usuários

**COMO:** Administrador\
**POSSO:** gerenciar os usuários da plataforma\
**PARA:** manter o ambiente seguro e organizado.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| | |
|---|---|
| 1 | **DADO QUE:** estou logado como Administrador <br> **QUANDO:** busco um usuário e altero o status dele para bloqueado <br> **ENTÃO:** o acesso dele é revogado imediatamente via blocklist de token no Redis e revogação das sessões de refresh. |
| 2 | **DADO QUE:** tento bloquear a minha própria conta de Administrador <br> **QUANDO:** confirmo a ação <br> **ENTÃO:** o sistema impede e mostra um aviso. |
| 3 | **DADO QUE:** seleciono um usuário para exclusão <br> **QUANDO:** confirmo a exclusão <br> **ENTÃO:** a exclusão lógica é aplicada com status deleted e deleted_at preenchido, mantendo os dados para possível reativação e o histórico acadêmico vinculado ao mesmo usuário; a anonimização irreversível dos dados pessoais é um passo posterior, em conformidade com a Lei Geral de Proteção de Dados Pessoais (LGPD) (BRASIL, 2018). |
| 4 | **DADO QUE:** estou logado como Administrador <br> **QUANDO:** altero o perfil de um usuário e confirmo a ação <br> **ENTÃO:** o novo perfil é salvo com registro na trilha de auditoria, as sessões de refresh são revogadas, o token atual vai para a blocklist do Redis e o novo perfil passa a valer a partir do próximo login. |
| 5 | **DADO QUE:** tento alterar o meu próprio perfil de Administrador <br> **QUANDO:** aciono a alteração de perfil <br> **ENTÃO:** o sistema impede a ação e exibe um aviso. |
| 6 | **DADO QUE:** estou logado como Administrador <br> **QUANDO:** busco um usuário bloqueado e confirmo o desbloqueio <br> **ENTÃO:** o status é alterado para ativo, a ação é registrada na trilha de auditoria e o acesso é restabelecido. |
| 7 | **DADO QUE:** tento desbloquear a minha própria conta de Administrador <br> **QUANDO:** confirmo a ação <br> **ENTÃO:** o sistema impede a ação e mostra um aviso. |
| 8 | **DADO QUE:** seleciono a exclusão de um Instrutor com cursos publicados <br> **QUANDO:** confirmo a exclusão <br> **ENTÃO:** escolho entre despublicar os cursos (status archived) preservando o acesso dos alunos matriculados ou aplicar exclusão lógica em cascata. |

## 22. US022 – REQUISITO RF020: Comprar créditos extras do Tutor de IA

**COMO:** Aluno matriculado em um curso\
**POSSO:** comprar pacote de mensagens extras do Tutor de IA com pagamento simulado\
**PARA:** continuar tirando dúvidas pedagógicas quando a cota horária regular de 20 mensagens estiver esgotada.\
**PRIORIDADE:** Could Have\
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| | |
|---|---|
| 1 | **DADO QUE:** estou logado como Aluno e desejo créditos adicionais <br> **QUANDO:** confirmo a compra do pacote de mensagens extras com pagamento simulado <br> **ENTÃO:** o pacote de créditos é registrado na minha conta e vinculado ao pagamento simulado (`tutor_credit_packs`). |
| 2 | **DADO QUE:** possuo um pacote de créditos extras ativo e esgotei a cota de 20 mensagens por hora <br> **QUANDO:** envio uma nova pergunta ao Tutor de IA <br> **ENTÃO:** a pergunta é aceita e respondida normalmente, debitando um crédito do pacote. |
| 3 | **DADO QUE:** estou na interface de aquisição de créditos extras <br> **QUANDO:** o pagamento simulado não é confirmado ou é cancelado <br> **ENTÃO:** a operação é cancelada sem cobrança, nenhum crédito é adicionado e a cota regular é mantida (ADR-0002). |

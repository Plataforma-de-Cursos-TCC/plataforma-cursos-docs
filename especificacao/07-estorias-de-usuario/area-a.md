## US001 – REQUISITO RF017: Realizar login de usuário

**COMO:** Usuário já cadastrado na plataforma\
**POSSO:** fazer login com e-mail e senha\
**PARA:** acessar a minha área (Aluno, Instrutor ou Administrador) conforme o meu perfil.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** informo e-mail e senha corretos <br> **QUANDO:** envio o formulário <br> **ENTÃO:** sou autenticado e direcionado para a minha área conforme o meu perfil. |
| 2 | **DADO QUE:** informo senha incorreta <br> **QUANDO:** envio o formulário <br> **ENTÃO:** recebo mensagem de erro sem indicar se o e-mail existe ou não. |
| 3 | **DADO QUE:** a minha sessão expirou <br> **QUANDO:** tento acessar uma área protegida <br> **ENTÃO:** sou direcionado para a tela de login. |

## US002 – REQUISITO RF001: Cadastrar-se na plataforma

**COMO:** Visitante ainda não cadastrado\
**POSSO:** criar uma conta com e-mail e senha\
**PARA:** acessar a plataforma como Aluno ou Instrutor.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** informo e-mail ainda não usado e senha válida <br> **QUANDO:** envio o cadastro <br> **ENTÃO:** a minha conta é criada com perfil Aluno por padrão e recebo confirmação. |
| 2 | **DADO QUE:** informo um e-mail já cadastrado <br> **QUANDO:** envio o cadastro <br> **ENTÃO:** recebo erro informando que o e-mail já está em uso. |
| 3 | **DADO QUE:** informo senha fora dos critérios mínimos (tamanho e complexidade) <br> **QUANDO:** envio o cadastro <br> **ENTÃO:** recebo erro apontando o requisito não atendido. |

## US003 – REQUISITO RF001: Editar dados do perfil

**COMO:** Usuário logado\
**POSSO:** editar os meus dados cadastrais (nome, telefone, endereço)\
**PARA:** manter as minhas informações atualizadas.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** altero nome e telefone válidos <br> **QUANDO:** salvo <br> **ENTÃO:** os dados são atualizados e aparecem no meu perfil. |
| 2 | **DADO QUE:** tento alterar o meu e-mail para um já usado por outro usuário <br> **QUANDO:** salvo <br> **ENTÃO:** recebo erro de e-mail em uso. |
| 3 | **DADO QUE:** deixo um campo obrigatório em branco <br> **QUANDO:** tento salvar <br> **ENTÃO:** o sistema bloqueia o envio e indica o campo pendente. |

## US017 – REQUISITO RF013: Recuperar senha por e-mail

**COMO:** Usuário que esqueceu a senha\
**POSSO:** solicitar a redefinição por e-mail\
**PARA:** recuperar o acesso à minha conta.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** informo um e-mail cadastrado <br> **QUANDO:** solicito a recuperação <br> **ENTÃO:** recebo um link de redefinição com validade limitada. |
| 2 | **DADO QUE:** informo um e-mail não cadastrado <br> **QUANDO:** solicito a recuperação <br> **ENTÃO:** vejo a mesma mensagem de sucesso, sem revelar se o e-mail existe. |
| 3 | **DADO QUE:** abro um link de redefinição expirado <br> **QUANDO:** tento definir a nova senha <br> **ENTÃO:** o sistema recusa e permite solicitar um novo link. |

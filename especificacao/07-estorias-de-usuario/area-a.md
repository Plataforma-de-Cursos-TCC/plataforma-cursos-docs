# 7 RELAÇÃO DE ESTÓRIAS DE USUÁRIO – ÁREA A (Acesso e conta)

O template exige uma estória de usuário por requisito funcional, com critérios de aceite. Formato Como / Posso / Para, com pelo menos 2 critérios (ADR-0002).

<!-- revisar: a v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) -->

Área A: Acesso e conta. Responsável: Lucas Stopinski da Silva (`LucasStop`). IDs: US-An, uma por RF da área, com o mesmo número (US-A1 ↔ RF-A1).

## US-A1 (US001) – REQUISITO RF-A1 (RF001): Realizar login de usuário

**COMO:** Usuário já cadastrado na plataforma
**QUERO:** fazer login com e-mail e senha
**PARA:** que eu possa acessar minha área (aluno/instrutor/admin) conforme meu perfil.
**PRIORIDADE:** Must Have
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** informo e-mail e senha corretos <br> **QUANDO:** envio o formulário <br> **ENTÃO:** sou autenticado e redirecionado pra minha área conforme meu perfil (role). |
| 2 | **DADO QUE:** informo senha incorreta <br> **QUANDO:** envio o formulário <br> **ENTÃO:** recebo mensagem de erro sem indicar se o e-mail existe ou não. |
| 3 | **DADO QUE:** meu token JWT expirou <br> **QUANDO:** tento acessar uma rota protegida <br> **ENTÃO:** sou redirecionado pra tela de login. |

## US-A2 (US002) – REQUISITO RF-A1 (RF001): Cadastrar-se na plataforma

**COMO:** Visitante ainda não cadastrado
**QUERO:** criar uma conta com e-mail e senha
**PARA:** que eu possa acessar a plataforma como aluno ou instrutor.
**PRIORIDADE:** Must Have
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** informo e-mail ainda não usado e senha válida <br> **QUANDO:** envio o cadastro <br> **ENTÃO:** minha conta é criada com perfil aluno por padrão e recebo confirmação. |
| 2 | **DADO QUE:** informo um e-mail já cadastrado <br> **QUANDO:** envio o cadastro <br> **ENTÃO:** recebo erro informando que o e-mail já está em uso. |
| 3 | **DADO QUE:** informo senha fora dos critérios mínimos (tamanho/complexidade) <br> **QUANDO:** envio o cadastro <br> **ENTÃO:** recebo erro apontando o requisito não atendido. |

## US-A3 (US003) – REQUISITO RF-A1 (RF001): Editar dados do perfil

**COMO:** Usuário logado
**QUERO:** editar meus dados cadastrais (nome, telefone, endereço)
**PARA:** que eu possa manter minhas informações atualizadas.
**PRIORIDADE:** Should Have
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** altero nome e telefone válidos <br> **QUANDO:** salvo <br> **ENTÃO:** os dados são atualizados e refletidos no meu perfil. |
| 2 | **DADO QUE:** tento alterar meu e-mail para um já usado por outro usuário <br> **QUANDO:** salvo <br> **ENTÃO:** recebo erro de e-mail em uso. |
| 3 | **DADO QUE:** deixo um campo obrigatório em branco <br> **QUANDO:** tento salvar <br> **ENTÃO:** o sistema bloqueia o envio e indica o campo pendente. |

## US-A4 (US017) – REQUISITO RF-A2 (RF013): Recuperar senha por e-mail

**COMO:** Usuário que esqueceu a senha
**QUERO:** solicitar a redefinição por e-mail
**PARA:** que eu possa recuperar o acesso à minha conta.
**PRIORIDADE:** Should Have
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** informo um e-mail cadastrado <br> **QUANDO:** solicito a recuperação <br> **ENTÃO:** recebo um link de redefinição com validade limitada. |
| 2 | **DADO QUE:** informo um e-mail não cadastrado <br> **QUANDO:** solicito a recuperação <br> **ENTÃO:** vejo a mesma mensagem de sucesso, sem revelar se o e-mail existe. |
| 3 | **DADO QUE:** abro um link de redefinição expirado <br> **QUANDO:** tento definir a nova senha <br> **ENTÃO:** o sistema recusa e permite solicitar um novo link. |

<!-- revisar: 4 estórias para 2 RF(s) na área; a regra "mesmo número do RF" (US-An ↔ RF-An) não se aplica a US-A2, US-A3, US-A4, que têm vários por RF na v11 (ADR 0001). A referência ao RF segue o ID correto -->

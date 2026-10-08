## US004 – REQUISITO RF002: Gerenciar cadastro do curso

**COMO:** Instrutor logado\
**POSSO:** criar, editar, excluir e listar os meus cursos\
**PARA:** gerenciar o meu catálogo de conteúdo.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** preencho título, descrição e preço do curso <br> **QUANDO:** salvo <br> **ENTÃO:** o curso é criado com status rascunho. |
| 2 | **DADO QUE:** edito um curso já publicado <br> **QUANDO:** salvo a alteração <br> **ENTÃO:** as mudanças aparecem no catálogo sem remover as matrículas existentes. |
| 3 | **DADO QUE:** tento excluir um curso com alunos matriculados <br> **QUANDO:** confirmo a exclusão <br> **ENTÃO:** o sistema impede e sugere despublicar em vez de excluir. |

## US005 – REQUISITO RF003: Gerenciar módulos do curso

**COMO:** Instrutor logado\
**POSSO:** criar, editar, excluir e reordenar módulos dentro de um curso\
**PARA:** organizar o conteúdo em blocos de aprendizado.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho um curso em rascunho <br> **QUANDO:** adiciono um módulo com título <br> **ENTÃO:** ele é salvo na ordem informada. |
| 2 | **DADO QUE:** reordeno os módulos existentes <br> **QUANDO:** salvo a nova ordem <br> **ENTÃO:** a nova sequência aparece para os alunos matriculados. |
| 3 | **DADO QUE:** tento excluir um módulo com aulas cadastradas <br> **QUANDO:** confirmo <br> **ENTÃO:** recebo aviso de que as aulas do módulo também serão removidas. |

## US006 – REQUISITO RF004: Gerenciar aulas do curso

**COMO:** Instrutor logado\
**POSSO:** cadastrar uma aula com vídeo dentro de um módulo\
**PARA:** disponibilizar o conteúdo em vídeo aos alunos.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** envio um arquivo de vídeo válido com o título da aula <br> **QUANDO:** o envio termina <br> **ENTÃO:** a aula fica disponível para reprodução pelos alunos matriculados. |
| 2 | **DADO QUE:** envio um arquivo em formato não suportado <br> **QUANDO:** tento salvar <br> **ENTÃO:** recebo erro informando os formatos aceitos. |
| 3 | **DADO QUE:** marco a aula como prévia <br> **QUANDO:** um Visitante sem matrícula acessa o curso <br> **ENTÃO:** ele consegue assistir a essa aula sem se matricular. |

## US010 – REQUISITO RF007: Gerenciar quizzes do curso

**COMO:** Instrutor\
**POSSO:** cadastrar quiz com perguntas e gabarito\
**PARA:** avaliar automaticamente o aprendizado dos alunos do módulo.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho um módulo criado <br> **QUANDO:** cadastro uma pergunta com uma alternativa marcada como correta <br> **ENTÃO:** o sistema usa esse gabarito para corrigir as respostas dos alunos. |
| 2 | **DADO QUE:** tento salvar uma pergunta sem nenhuma alternativa marcada como correta <br> **QUANDO:** envio <br> **ENTÃO:** recebo erro pedindo para marcar o gabarito. |
| 3 | **DADO QUE:** edito o gabarito de uma pergunta já respondida por alunos <br> **QUANDO:** salvo a alteração <br> **ENTÃO:** as notas já lançadas não mudam retroativamente. |

## US020 – REQUISITO RF016: Gerenciar perfil do instrutor

**COMO:** Instrutor\
**POSSO:** gerenciar o meu perfil de instrutor\
**PARA:** apresentar a minha formação e as minhas redes aos alunos.\
**PRIORIDADE:** Could Have\
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou logado como Instrutor <br> **QUANDO:** preencho minibiografia e links e salvo <br> **ENTÃO:** o perfil é atualizado e exibido na página do curso. |
| 2 | **DADO QUE:** informo um link em formato inválido <br> **QUANDO:** salvo <br> **ENTÃO:** o sistema recusa e indica o campo. |
| 3 | **DADO QUE:** sou Aluno ou Administrador <br> **QUANDO:** tento editar um perfil de Instrutor <br> **ENTÃO:** o acesso é negado. |

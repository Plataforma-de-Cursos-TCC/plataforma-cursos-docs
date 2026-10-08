# 7 RELAÇÃO DE ESTÓRIAS DE USUÁRIO – ÁREA B (Autoria do instrutor)

O template exige uma estória de usuário por requisito funcional, com critérios de aceite. Formato Como / Posso / Para, com pelo menos 2 critérios (ADR-0002).

<!-- revisar: a v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) -->

Área B: Autoria do instrutor. Responsável: Adrian Antônio de Souza Gomes (`adrian69-droid`). IDs: US-Bn, uma por RF da área, com o mesmo número (US-B1 ↔ RF-B1).

## US-B1 (US004) – REQUISITO RF-B1 (RF002): Gerenciar cadastro do curso

**COMO:** Instrutor logado
**QUERO:** criar, editar, excluir e listar meus cursos
**PARA:** que eu possa gerenciar meu catálogo de conteúdo.
**PRIORIDADE:** Must Have
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** preencho título, descrição e preço do curso <br> **QUANDO:** salvo <br> **ENTÃO:** o curso é criado com status rascunho. |
| 2 | **DADO QUE:** edito um curso já publicado <br> **QUANDO:** salvo a alteração <br> **ENTÃO:** as mudanças refletem no catálogo sem remover matrículas existentes. |
| 3 | **DADO QUE:** tento excluir um curso com alunos matriculados <br> **QUANDO:** confirmo a exclusão <br> **ENTÃO:** o sistema impede e sugere despublicar em vez de excluir. |

## US-B2 (US005) – REQUISITO RF-B2 (RF003): Gerenciar módulos do curso

**COMO:** Instrutor logado
**QUERO:** criar, editar, excluir e reordenar módulos dentro de um curso
**PARA:** que eu possa organizar o conteúdo em blocos de aprendizado.
**PRIORIDADE:** Must Have
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho um curso em rascunho <br> **QUANDO:** adiciono um módulo com título <br> **ENTÃO:** ele é salvo na ordem informada. |
| 2 | **DADO QUE:** reordeno os módulos existentes <br> **QUANDO:** salvo a nova ordem <br> **ENTÃO:** a sequência é refletida pros alunos matriculados. |
| 3 | **DADO QUE:** tento excluir um módulo com aulas cadastradas <br> **QUANDO:** confirmo <br> **ENTÃO:** recebo aviso que as aulas do módulo também serão removidas. |

## US-B3 (US006) – REQUISITO RF-B3 (RF004): Gerenciar aulas do curso

**COMO:** Instrutor logado
**QUERO:** cadastrar uma aula com vídeo dentro de um módulo
**PARA:** que eu possa disponibilizar o conteúdo em vídeo aos alunos.
**PRIORIDADE:** Must Have
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** envio um arquivo de vídeo válido com título da aula <br> **QUANDO:** o upload termina <br> **ENTÃO:** a aula fica disponível com URL assinada de reprodução. |
| 2 | **DADO QUE:** envio um arquivo em formato não suportado <br> **QUANDO:** tento salvar <br> **ENTÃO:** recebo erro informando os formatos aceitos. |
| 3 | **DADO QUE:** marco a aula como “prévia” (isPreview) <br> **QUANDO:** um visitante não matriculado acessa o curso <br> **ENTÃO:** ele consegue assistir essa aula sem matrícula. |

## US-B4 (US010) – REQUISITO RF-B4 (RF007): Gerenciar quizzes do curso

**COMO:** Instrutor
**QUERO:** cadastrar quiz com perguntas e gabarito
**PARA:** que eu possa avaliar automaticamente o aprendizado dos alunos do módulo.
**PRIORIDADE:** Should Have
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** tenho um módulo criado <br> **QUANDO:** cadastro uma pergunta com uma alternativa marcada como correta <br> **ENTÃO:** o sistema usa esse gabarito pra corrigir as respostas dos alunos. |
| 2 | **DADO QUE:** tento salvar uma pergunta sem nenhuma alternativa marcada como correta <br> **QUANDO:** envio <br> **ENTÃO:** recebo erro pedindo pra marcar o gabarito. |
| 3 | **DADO QUE:** edito o gabarito de uma pergunta já respondida por alunos <br> **QUANDO:** salvo a alteração <br> **ENTÃO:** as notas já lançadas não mudam retroativamente. |

## US-B5 (US020) – REQUISITO RF-B5 (RF016): Gerenciar perfil do instrutor

**COMO:** Instrutor
**QUERO:** gerenciar meu perfil de instrutor
**PARA:** que eu possa apresentar minha formação e minhas redes aos alunos.
**PRIORIDADE:** Could Have
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** estou logado como instrutor <br> **QUANDO:** preencho minibiografia e links e salvo <br> **ENTÃO:** o perfil é atualizado e exibido na página do curso. |
| 2 | **DADO QUE:** informo um link em formato inválido <br> **QUANDO:** salvo <br> **ENTÃO:** o sistema recusa e indica o campo. |
| 3 | **DADO QUE:** sou aluno ou administrador <br> **QUANDO:** tento editar um perfil de instrutor <br> **ENTÃO:** o acesso é negado. |

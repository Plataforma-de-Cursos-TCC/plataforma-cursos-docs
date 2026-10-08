## US007 – REQUISITO RF005: Matricular-se em curso

**COMO:** Aluno logado\
**POSSO:** matricular-me em um curso publicado\
**PARA:** começar a assistir às aulas.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o curso está publicado e eu não estou matriculado <br> **QUANDO:** clico em "matricular-se" <br> **ENTÃO:** o curso aparece em "meus cursos" e a matrícula é registrada. |
| 2 | **DADO QUE:** eu já estou matriculado no curso <br> **QUANDO:** acesso a página do curso <br> **ENTÃO:** o botão de matrícula não aparece, só o de continuar assistindo. |
| 3 | **DADO QUE:** o curso está em rascunho (não publicado) <br> **QUANDO:** tento acessá-lo <br> **ENTÃO:** recebo erro de curso não encontrado. |

## US008 – REQUISITO RF006: Registrar progresso de aula assistida

**COMO:** Aluno matriculado\
**POSSO:** ter o meu progresso de visualização registrado automaticamente\
**PARA:** acompanhar quanto já avancei no curso.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** assisto a uma aula até o fim <br> **QUANDO:** o vídeo termina <br> **ENTÃO:** a aula é marcada como concluída no meu progresso. |
| 2 | **DADO QUE:** pauso a aula na metade <br> **QUANDO:** saio e volto depois <br> **ENTÃO:** o progresso mostra os segundos assistidos até aquele ponto. |
| 3 | **DADO QUE:** já completei todas as aulas de um módulo <br> **QUANDO:** acesso o curso <br> **ENTÃO:** vejo o percentual de conclusão do curso atualizado. |

## US009 – REQUISITO RF006: Retomar aula de onde parou

**COMO:** Aluno matriculado\
**POSSO:** retomar a reprodução de uma aula no ponto exato em que parei\
**PARA:** não perder tempo revendo conteúdo já assistido.\
**PRIORIDADE:** Could Have\
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** assisti a 5 minutos de uma aula de 10 e saí <br> **QUANDO:** volto a acessá-la <br> **ENTÃO:** o vídeo inicia a partir do minuto 5. |
| 2 | **DADO QUE:** já concluí uma aula <br> **QUANDO:** acesso a aula de novo <br> **ENTÃO:** o vídeo inicia do começo, mas o status de concluída é mantido. |
| 3 | **DADO QUE:** assisto à aula em outro dispositivo <br> **QUANDO:** retomo a reprodução <br> **ENTÃO:** o ponto salvo é o mesmo, independentemente do dispositivo usado. |

## US011 – REQUISITO RF008: Responder quiz

**COMO:** Aluno matriculado\
**POSSO:** responder ao quiz de um módulo\
**PARA:** validar o meu aprendizado e ver a minha nota.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** completei as aulas do módulo <br> **QUANDO:** envio as respostas do quiz <br> **ENTÃO:** recebo a nota calculada e o resultado fica salvo no meu progresso. |
| 2 | **DADO QUE:** não respondo a todas as questões <br> **QUANDO:** tento enviar <br> **ENTÃO:** recebo aviso de questão pendente e o envio é bloqueado. |
| 3 | **DADO QUE:** já respondi ao quiz antes <br> **QUANDO:** acesso de novo <br> **ENTÃO:** vejo o meu resultado anterior, sem poder refazer, salvo se o Instrutor permitir. |

## US014 – REQUISITO RF011: Avaliar curso

**COMO:** Aluno matriculado\
**POSSO:** avaliar um curso com nota e comentário\
**PARA:** dar feedback e ajudar outros alunos a escolher.\
**PRIORIDADE:** Could Have\
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** completei ao menos uma aula do curso <br> **QUANDO:** envio uma avaliação com nota de 1 a 5 e comentário <br> **ENTÃO:** ela é salva e exibida na página do curso. |
| 2 | **DADO QUE:** já avaliei o curso antes <br> **QUANDO:** tento avaliar de novo <br> **ENTÃO:** o sistema atualiza a minha avaliação existente em vez de criar uma duplicada. |
| 3 | **DADO QUE:** não estou matriculado no curso <br> **QUANDO:** tento avaliar <br> **ENTÃO:** o sistema bloqueia a ação e informa que só alunos matriculados podem avaliar. |

## US018 – REQUISITO RF014: Registrar pagamento simulado da matrícula

**COMO:** Aluno\
**POSSO:** confirmar um pagamento simulado ao me matricular em um curso pago\
**PARA:** liberar o meu acesso ao conteúdo.\
**PRIORIDADE:** Must Have\
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** escolhi um curso pago <br> **QUANDO:** confirmo o pagamento simulado <br> **ENTÃO:** o pagamento é registrado como aprovado e a matrícula é criada. |
| 2 | **DADO QUE:** o pagamento simulado é recusado <br> **QUANDO:** o resultado é exibido <br> **ENTÃO:** nenhuma matrícula é criada e posso tentar novamente. |
| 3 | **DADO QUE:** o curso é gratuito <br> **QUANDO:** solicito a matrícula <br> **ENTÃO:** nenhum pagamento é exigido. |

## US019 – REQUISITO RF015: Consultar catálogo e buscar cursos por categoria

**COMO:** Visitante ou Aluno\
**POSSO:** consultar o catálogo e buscar cursos por categoria\
**PARA:** encontrar o curso que atende ao meu interesse.\
**PRIORIDADE:** Should Have\
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** acesso o catálogo <br> **QUANDO:** a página carrega <br> **ENTÃO:** vejo apenas cursos publicados, com título, instrutor e preço. |
| 2 | **DADO QUE:** seleciono uma categoria <br> **QUANDO:** aplico o filtro <br> **ENTÃO:** a lista mostra somente cursos dessa categoria. |
| 3 | **DADO QUE:** busco um termo sem resultado <br> **QUANDO:** a busca termina <br> **ENTÃO:** vejo a mensagem de nenhum curso encontrado. |

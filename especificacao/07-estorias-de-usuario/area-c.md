# 7 RELAÇÃO DE ESTÓRIAS DE USUÁRIO – ÁREA C (Aprendizagem do aluno)

O template exige uma estória de usuário por requisito funcional, com critérios de aceite. Formato Como / Posso / Para, com pelo menos 2 critérios (ADR-0002).

<!-- revisar: a v11 usa Como/Quero/Para que; o formato da ADR é Como/Posso/Para (ADR 0002) -->

Área C: Aprendizagem do aluno. Responsável: Lucas Bruno e Silva (`Luc-Bruno`). IDs: US-Cn, uma por RF da área, com o mesmo número (US-C1 ↔ RF-C1).

## US-C1 (US007) – REQUISITO RF-C1 (RF005): Matricular-se em curso

**COMO:** Aluno logado
**QUERO:** me matricular em um curso publicado
**PARA:** que eu possa começar a assistir as aulas.
**PRIORIDADE:** Must Have
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** o curso está publicado e eu não estou matriculado <br> **QUANDO:** clico em "matricular-se" <br> **ENTÃO:** o curso aparece em "meus cursos" e a matrícula é registrada. |
| 2 | **DADO QUE:** eu já estou matriculado no curso <br> **QUANDO:** acesso a página do curso <br> **ENTÃO:** o botão de matrícula não aparece, só o de continuar assistindo. |
| 3 | **DADO QUE:** o curso está em rascunho (não publicado) <br> **QUANDO:** tento acessá-lo <br> **ENTÃO:** recebo erro de curso não encontrado. |

## US-C2 (US008) – REQUISITO RF-C2 (RF006): Registrar progresso de aula assistida

**COMO:** Aluno matriculado
**QUERO:** ter meu progresso de visualização registrado automaticamente
**PARA:** que eu possa acompanhar quanto já avancei no curso.
**PRIORIDADE:** Should Have
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** assisto uma aula até o fim <br> **QUANDO:** o vídeo termina <br> **ENTÃO:** a aula é marcada como concluída no meu progresso. |
| 2 | **DADO QUE:** pauso a aula na metade <br> **QUANDO:** saio e volto depois <br> **ENTÃO:** o progresso reflete os segundos assistidos até aquele ponto. |
| 3 | **DADO QUE:** já completei todas as aulas de um módulo <br> **QUANDO:** acesso o curso <br> **ENTÃO:** vejo o percentual de conclusão do curso atualizado. |

## US-C3 (US009) – REQUISITO RF-C2 (RF006): Retomar aula de onde parou

**COMO:** Aluno matriculado
**QUERO:** retomar a reprodução de uma aula no ponto exato em que parei
**PARA:** que eu possa não perder tempo revendo conteúdo já assistido.
**PRIORIDADE:** Could Have
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** assisti 5 minutos de uma aula de 10 e saí <br> **QUANDO:** volto a acessá-la <br> **ENTÃO:** o vídeo inicia a partir do minuto 5. |
| 2 | **DADO QUE:** já concluí uma aula <br> **QUANDO:** acesso ela de novo <br> **ENTÃO:** o vídeo inicia do começo, mas o status de concluída é mantido. |
| 3 | **DADO QUE:** assisto a aula em outro dispositivo <br> **QUANDO:** retomo a reprodução <br> **ENTÃO:** o ponto salvo é o mesmo, independente do dispositivo usado. |

## US-C4 (US011) – REQUISITO RF-C3 (RF008): Responder quiz

**COMO:** Aluno matriculado
**QUERO:** responder o quiz de um módulo
**PARA:** que eu possa validar meu aprendizado e ver minha nota.
**PRIORIDADE:** Should Have
**AUTOR(A):** Lucas Stopinski da Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** completei as aulas do módulo <br> **QUANDO:** envio as respostas do quiz <br> **ENTÃO:** recebo a nota calculada e o resultado fica salvo no meu progresso. |
| 2 | **DADO QUE:** não respondo todas as questões <br> **QUANDO:** tento enviar <br> **ENTÃO:** recebo aviso de questão pendente e o envio é bloqueado. |
| 3 | **DADO QUE:** já respondi o quiz antes <br> **QUANDO:** acesso de novo <br> **ENTÃO:** vejo meu resultado anterior, sem poder refazer salvo se o instrutor permitir. |

## US-C5 (US014) – REQUISITO RF-C4 (RF011): Avaliar curso

**COMO:** Aluno matriculado
**QUERO:** avaliar um curso com nota e comentário
**PARA:** que eu possa dar feedback e ajudar outros alunos a escolher.
**PRIORIDADE:** Could Have
**AUTOR(A):** Vinicius Lima Teider

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** completei ao menos uma aula do curso <br> **QUANDO:** envio uma avaliação com nota de 1 a 5 e comentário <br> **ENTÃO:** ela é salva e exibida na página do curso. |
| 2 | **DADO QUE:** já avaliei o curso antes <br> **QUANDO:** tento avaliar de novo <br> **ENTÃO:** o sistema atualiza minha avaliação existente em vez de criar uma duplicada. |
| 3 | **DADO QUE:** não estou matriculado no curso <br> **QUANDO:** tento avaliar <br> **ENTÃO:** o sistema bloqueia a ação e informa que só alunos matriculados podem avaliar. |

## US-C6 (US018) – REQUISITO RF-C5 (RF014): Registrar pagamento simulado da matrícula

**COMO:** Aluno
**QUERO:** confirmar um pagamento simulado ao me matricular em um curso pago
**PARA:** que eu possa liberar meu acesso ao conteúdo.
**PRIORIDADE:** Must Have
**AUTOR(A):** Lucas Bruno e Silva

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** escolhi um curso pago <br> **QUANDO:** confirmo o pagamento simulado <br> **ENTÃO:** o pagamento é registrado como aprovado e a matrícula é criada. |
| 2 | **DADO QUE:** o pagamento simulado é recusado <br> **QUANDO:** o resultado é exibido <br> **ENTÃO:** nenhuma matrícula é criada e posso tentar novamente. |
| 3 | **DADO QUE:** o curso é gratuito <br> **QUANDO:** solicito a matrícula <br> **ENTÃO:** nenhum pagamento é exigido. |

## US-C7 (US019) – REQUISITO RF-C6 (RF015): Consultar catálogo e buscar cursos por categoria

**COMO:** Visitante ou Aluno
**QUERO:** consultar o catálogo e buscar cursos por categoria
**PARA:** que eu possa encontrar o curso que atende ao meu interesse.
**PRIORIDADE:** Should Have
**AUTOR(A):** Adrian Antônio de Souza Gomes

**Critérios de Aceite:**

| # | |
|---|---|
| 1 | **DADO QUE:** acesso o catálogo <br> **QUANDO:** a página carrega <br> **ENTÃO:** vejo apenas cursos publicados com título, instrutor e preço. |
| 2 | **DADO QUE:** seleciono uma categoria <br> **QUANDO:** aplico o filtro <br> **ENTÃO:** a lista mostra somente cursos dessa categoria. |
| 3 | **DADO QUE:** busco um termo sem resultado <br> **QUANDO:** a busca termina <br> **ENTÃO:** vejo a mensagem de nenhum curso encontrado. |

<!-- revisar: 7 estórias para 6 RF(s) na área; a regra "mesmo número do RF" (US-Cn ↔ RF-Cn) não se aplica a US-C3, US-C4, US-C5, US-C6, US-C7, que têm vários por RF na v11 (ADR 0001). A referência ao RF segue o ID correto -->

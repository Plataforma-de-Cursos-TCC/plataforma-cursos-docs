---
id: testes-casos
titulo: "Casos de teste"
tipo: documento-projeto
status: rascunho
atualizado: 2026-10-08
---
# Casos de teste

64 casos de teste (TC001–TC064), derivados dos critérios de aceite do item 7 (Dado/Quando/Então) e dos fluxos principal, alternativo e de exceção dos casos de uso do item 10, no padrão Cenário, CT, Entradas e Resultado Esperado. Todos os casos de uso (UC001–UC020) e estórias de usuário (US001–US021) possuem cobertura de testes associada.

Padrão TE6. Os casos nascem dos critérios de aceite das estórias (ADR-0002) e das especificações de casos de uso.

Colunas conforme o esqueleto do arquivo; a coluna **Cenário** mantém a origem do caso (fluxo do UC ou critério da estória). Onde a planilha de casos de teste e a v11 divergem, vale a v11.


| ID | UC | Tipo | Pré-condição | Passos | Resultado esperado | Cenário |
|---|---|---|---|---|---|---|
| TC001 | UC005 | Positivo | Dado que informo e-mail e senha corretos | 1. Quando envio o formulário. | Então sou autenticado e redirecionado pra minha área conforme meu perfil (role). | Fluxo básico (passos 1-7) |
| TC002 | UC005 | Negativo | Dado que informo senha incorreta | 1. Quando envio o formulário. | Então recebo mensagem de erro sem indicar se o e-mail existe ou não. | Fluxo de exceção E1 |
| TC003 | UC005 | Negativo | Dado que meu token JWT expirou | 1. Quando tento acessar uma rota protegida. | Então sou redirecionado pra tela de login. | Fluxo de exceção E2 |
| TC004 | UC012 | Positivo | Dado que informo e-mail ainda não usado e senha válida | 1. Quando envio o cadastro. | Então minha conta é criada com perfil aluno por padrão e recebo confirmação. | Critério 1 (US002) |
| TC005 | UC012 | Negativo | Dado que informo um e-mail já cadastrado | 1. Quando envio o cadastro. | Então recebo erro informando que o e-mail já está em uso. | Critério 2 (US002) |
| TC006 | UC012 | Negativo | Dado que informo senha fora dos critérios mínimos (tamanho/complexidade) | 1. Quando envio o cadastro. | Então recebo erro apontando o requisito não atendido. | Critério 3 (US002) |
| TC007 | UC013 | Positivo | Dado que altero nome e telefone válidos | 1. Quando salvo. | Então os dados são atualizados e refletidos no meu perfil. | Critério 1 (US003) |
| TC008 | UC013 | Negativo | Dado que tento alterar meu e-mail para um já usado por outro usuário | 1. Quando salvo. | Então recebo erro de e-mail em uso. | Critério 2 (US003) |
| TC009 | UC013 | Negativo | Dado que deixo um campo obrigatório em branco | 1. Quando tento salvar. | Então o sistema bloqueia o envio e indica o campo pendente. | Critério 3 (US003) |
| TC010 | UC006 | Positivo | Dado que preencho título, descrição e preço do curso | 1. Quando salvo. | Então o curso é criado com status rascunho. | Fluxo básico (passos 1-4) |
| TC011 | UC006 | Positivo | Dado que edito um curso já publicado | 1. Quando salvo a alteração. | Então as mudanças refletem no catálogo sem remover matrículas existentes. | Fluxo alternativo A1 |
| TC012 | UC006 | Negativo | Dado que tento excluir um curso com alunos matriculados | 1. Quando confirmo a exclusão. | Então o sistema impede e sugere despublicar em vez de excluir. | Fluxo de exceção E2 |
| TC013 | UC014 | Positivo | Dado que tenho um curso em rascunho | 1. Quando adiciono um módulo com título. | Então ele é salvo na ordem informada. | Critério 1 (US005) |
| TC014 | UC014 | Positivo | Dado que reordeno os módulos existentes | 1. Quando salvo a nova ordem. | Então a sequência é refletida pros alunos matriculados. | Critério 2 (US005) |
| TC015 | UC014 | Negativo | Dado que tento excluir um módulo com aulas cadastradas | 1. Quando confirmo. | Então recebo aviso que as aulas do módulo também serão removidas. | Critério 3 (US005) |
| TC016 | UC015 | Positivo | Dado que envio um arquivo de vídeo válido com título da aula | 1. Quando o upload termina. | Então a aula fica disponível com URL assinada de reprodução. | Critério 1 (US006) |
| TC017 | UC015 | Negativo | Dado que envio um arquivo em formato não suportado | 1. Quando tento salvar. | Então recebo erro informando os formatos aceitos. | Critério 2 (US006) |
| TC018 | UC015 | Positivo | Dado que marco a aula como “prévia” (isPreview) | 1. Quando um visitante não matriculado acessa o curso. | Então ele consegue assistir essa aula sem matrícula. | Critério 3 (US006) |
| TC019 | UC003 | Positivo | Dado que o curso está publicado e eu não estou matriculado | 1. Quando clico em "matricular-se". | Então o curso aparece em "meus cursos" e a matrícula é registrada. | Fluxo básico (passos 1-6) |
| TC020 | UC003 | Negativo | Dado que eu já estou matriculado no curso | 1. Quando acesso a página do curso. | Então o botão de matrícula não aparece, só o de continuar assistindo. | Fluxo alternativo A1 |
| TC021 | UC003 | Negativo | Dado que o curso está em rascunho (não publicado) | 1. Quando tento acessá-lo. | Então recebo erro de curso não encontrado. | Fluxo de exceção E1 |
| TC022 | UC009 | Positivo | Dado que assisto uma aula até o fim | 1. Quando o vídeo termina. | Então a aula é marcada como concluída no meu progresso. | Critério 1 (US008) |
| TC023 | UC009 | Positivo | Dado que pauso a aula na metade | 1. Quando saio e volto depois. | Então o progresso reflete os segundos assistidos até aquele ponto. | Critério 2 (US008) |
| TC024 | UC009 | Positivo | Dado que já completei todas as aulas de um módulo | 1. Quando acesso o curso. | Então vejo o percentual de conclusão do curso atualizado. | Critério 3 (US008) |
| TC025 | UC009 | Positivo | Dado que assisti 5 minutos de uma aula de 10 e saí | 1. Quando volto a acessá-la. | Então o vídeo inicia a partir do minuto 5. | Critério 1 (US009) |
| TC026 | UC009 | Positivo | Dado que já concluí uma aula | 1. Quando acesso ela de novo. | Então o vídeo inicia do começo, mas o status de concluída é mantido. | Critério 2 (US009) |
| TC027 | UC009 | Positivo | Dado que assisto a aula em outro dispositivo | 1. Quando retomo a reprodução. | Então o ponto salvo é o mesmo, independente do dispositivo usado. | Critério 3 (US009) |
| TC028 | UC004 | Positivo | Dado que tenho um módulo criado | 1. Quando cadastro uma pergunta com uma alternativa marcada como correta. | Então o sistema usa esse gabarito pra corrigir as respostas dos alunos. | Fluxo básico (passos 1-6) |
| TC029 | UC004 | Negativo | Dado que tento salvar uma pergunta sem nenhuma alternativa marcada como correta | 1. Quando envio. | Então recebo erro pedindo pra marcar o gabarito. | Fluxo de exceção E2 |
| TC030 | UC004 | Positivo | Dado que edito o gabarito de uma pergunta já respondida por alunos | 1. Quando salvo a alteração. | Então as notas já lançadas não mudam retroativamente. | Fluxo alternativo A1 |
| TC031 | UC002 | Positivo | Dado que completei as aulas do módulo | 1. Quando envio as respostas do quiz. | Então recebo a nota calculada e o resultado fica salvo no meu progresso. | Fluxo básico (passos 1-6) |
| TC032 | UC002 | Negativo | Dado que não respondo todas as questões | 1. Quando tento enviar. | Então recebo aviso de questão pendente e o envio é bloqueado. | Fluxo de exceção E1 |
| TC033 | UC002 | Positivo | Dado que já respondi o quiz antes | 1. Quando acesso de novo. | Então vejo meu resultado anterior, sem poder refazer salvo se o instrutor permitir. | Fluxo alternativo A1 |
| TC034 | UC001 | Positivo | Dado que estou numa aula do curso em que sou matriculado | 1. Quando pergunto algo relacionado ao conteúdo. | Então recebo resposta com citação da aula e do timestamp de origem. | Fluxo básico (passos 1-6) |
| TC035 | UC001 | Negativo | Dado que pergunto algo fora do conteúdo do curso | 1. Quando envio a mensagem. | Então o tutor responde que não tem essa informação no material do curso. | Fluxo alternativo A1 |
| TC036 | UC001 | Negativo | Dado que excedo o limite de mensagens por período (rate limit) | 1. Quando tento enviar nova pergunta. | Então recebo aviso de limite atingido. | Fluxo de exceção E2 |
| TC037 | UC007 | Positivo | Dado que tenho alunos matriculados | 1. Quando seleciono um intervalo de datas. | Então vejo progresso e engajamento agregados só daquele período. | Fluxo básico (passos 1-6) |
| TC038 | UC007 | Positivo | Dado que nenhum aluno teve atividade no período selecionado | 1. Quando aplico o filtro. | Então vejo estado vazio claro, não erro. | Fluxo de exceção E2 |
| TC039 | UC007 | Positivo | Dado que tenho mais de um curso | 1. Quando acesso o dashboard. | Então consigo filtrar também por curso, além do período. | Fluxo alternativo A1 |
| TC040 | UC010 | Positivo | Dado que completei ao menos uma aula do curso | 1. Quando envio uma avaliação com nota de 1 a 5 e comentário. | Então ela é salva e exibida na página do curso. | Critério 1 (US014) |
| TC041 | UC010 | Positivo | Dado que já avaliei o curso antes | 1. Quando tento avaliar de novo. | Então o sistema atualiza minha avaliação existente em vez de criar uma duplicada. | Critério 2 (US014) |
| TC042 | UC010 | Negativo | Dado que não estou matriculado no curso | 1. Quando tento avaliar. | Então o sistema bloqueia a ação e informa que só alunos matriculados podem avaliar. | Critério 3 (US014) |
| TC043 | UC016 | Negativo | Dado que estou logado como aluno | 1. Quando tento acessar uma rota exclusiva de instrutor. | Então recebo erro de acesso negado e sou redirecionado pra minha área. | Critério 1 (US015) |
| TC044 | UC016 | Positivo | Dado que estou logado como instrutor | 1. Quando acesso minha área. | Então vejo meu nome e perfil (role) visíveis na interface. | Critério 2 (US015) |
| TC045 | UC016 | Positivo | Dado que meu token expira enquanto navego numa rota protegida | 1. Quando tento uma ação. | Então sou redirecionado pra login sem exposição de dados da rota. | Critério 3 (US015) |
| TC046 | UC008 | Positivo | Dado que estou logado como admin | 1. Quando busco um usuário e altero seu status pra bloqueado. | Então o acesso dele é revogado imediatamente. | Fluxo básico (passos 1-6) |
| TC047 | UC008 | Negativo | Dado que tento bloquear minha própria conta admin | 1. Quando confirmo a ação. | Então o sistema impede e mostra aviso. | Fluxo de exceção E1 |
| TC048 | UC008 | Positivo | Dado que um usuário é excluído | 1. Quando a exclusão é confirmada. | Então seus dados pessoais são removidos mas o histórico de matrícula/pagamento permanece anonimizado. | Fluxo básico (passos 1-6) |
| TC049 | UC011 | Positivo | Dado que informo um e-mail cadastrado | 1. Quando solicito a recuperação. | Então recebo um link de redefinição com validade limitada de 30 minutos. | Critério 1 (US017) / Fluxo básico (passos 1-6) |
| TC050 | UC011 | Positivo | Dado que informo um e-mail não cadastrado | 1. Quando solicito a recuperação. | Então vejo a mesma mensagem de confirmação genérica sem revelar se o e-mail existe. | Critério 2 (US017) / Fluxo de exceção E1 |
| TC051 | UC011 | Negativo | Dado que abro um link de redefinição expirado | 1. Quando tento definir a nova senha. | Então o sistema recusa e permite solicitar um novo link. | Critério 3 (US017) / Fluxo de exceção E2 |
| TC052 | UC019 | Positivo | Dado que escolhi um curso pago | 1. Quando confirmo o pagamento simulado. | Então o pagamento é registrado como aprovado e a matrícula é criada. | Critério 1 (US018) / Fluxo básico (passos 1-5) |
| TC053 | UC019 | Negativo | Dado que informo dados de pagamento simulado inválidos | 1. Quando confirmo o pagamento simulado. | Então o pagamento é recusado, nenhuma matrícula é criada e posso tentar novamente. | Critério 2 (US018) / Fluxo de exceção E1 |
| TC054 | UC019 | Positivo | Dado que o curso é gratuito | 1. Quando solicito a matrícula. | Então nenhum pagamento é exigido e o acesso é liberado diretamente. | Critério 3 (US018) / Regra R-1 |
| TC055 | UC020 | Positivo | Dado que existem cursos publicados e em rascunho | 1. Quando acesso o catálogo. | Então vejo apenas cursos publicados, com título, instrutor e preço. | Critério 1 (US019) / Fluxo básico (passos 1-2) |
| TC056 | UC020 | Positivo | Dado que seleciono uma categoria | 1. Quando aplico o filtro. | Então a lista mostra somente cursos dessa categoria. | Critério 2 (US019) / Fluxo básico (passos 3-4) |
| TC057 | UC020 | Positivo | Dado que uma categoria não tem cursos publicados | 1. Quando filtro por essa categoria. | Então vejo a mensagem "Nenhum curso encontrado nesta categoria." com botão para ver todos. | Critério 3 (US019) / Fluxo de exceção E2 |
| TC058 | UC013 | Positivo | Dado que estou logado como Instrutor | 1. Quando preencho minibiografia e links e salvo. | Então o perfil é atualizado e exibido na página do curso. | Critério 1 (US020) / Fluxo alternativo A1 |
| TC059 | UC013 | Negativo | Dado que informo um link em formato inválido | 1. Quando salvo. | Então o sistema recusa e indica o campo com mensagem de erro. | Critério 2 (US020) / Fluxo de exceção E1 |
| TC060 | UC013 | Negativo | Dado que sou Aluno ou Administrador | 1. Quando tento editar campos exclusivos de perfil de Instrutor. | Então o acesso aos campos é bloqueado e a alteração é negada. | Critério 3 (US020) / Regra R-1 |
| TC061 | UC017 | Positivo | Dado que estou logado e informo a senha atual correta e nova senha válida | 1. Quando aciono "Salvar senha". | Então a senha é substituída pela nova e recebo confirmação de alteração. | Fluxo básico (passos 1-6) |
| TC062 | UC017 | Negativo | Dado que informo uma senha atual incorreta | 1. Quando aciono "Salvar senha". | Então o sistema recusa a troca e exibe aviso de senha atual incorreta. | Fluxo de exceção E1 |
| TC063 | UC018 | Negativo | Dado que estou logado como Administrador e tento excluir minha própria conta | 1. Quando tento confirmar a exclusão. | Então o sistema impede a exclusão e exibe o aviso "Não é possível excluir a própria conta". | Fluxo de exceção E1 |
| TC064 | UC017 | Negativo | Dado que informo uma nova senha e uma confirmação diferente dela | 1. Quando aciono "Salvar senha". | Então o sistema bloqueia a troca, indica o campo de confirmação e a senha não é alterada. | Critério 3 (US021) / Fluxo de exceção E3 |


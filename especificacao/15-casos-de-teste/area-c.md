## 1. UC003 – Matricular-se em Curso

**Rastreio:** US007, RF005 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC019 | 1 – Fluxo básico (curso gratuito) | CT1 Matrícula em curso gratuito | Aluno logado (`student`) aciona «Matricular-se» em curso com preço 0 | Resposta 201 `Created` (`EnrollmentResource`), matrícula criada diretamente com status `active` sem cobrança (R-4) e curso exibido em «Meus cursos». |
| TC151 | 1 – Fluxo básico (curso pago) | CT2 Matrícula em curso pago | Aluno logado aciona «Matricular-se» em curso com preço > 0 | Resposta 201 `Created` (`EnrollmentResource`), matrícula criada com status `pending` (R-3) e redirecionamento ao modal de pagamento simulado (UC019). |
| TC020 | 2 – A1 Aluno já matriculado | CT1 Curso já matriculado | Aluno com matrícula ativa acessa a página do curso | Botão «Matricular-se» não aparece; exibe botão «Continuar assistindo», sem gerar matrícula duplicada (R-2). |
| TC152 | 2 – A1 Matrícula pendente existente | CT2 Retomar pagamento pendente | Aluno com matrícula pendente acessa a página do curso | Exibe botão «Concluir pagamento», permitindo retomar a liquidação na mesma matrícula sem criar nova linha em `Enrollment` (R-2). |
| TC021 | 3 – E1 Curso não publicado | CT1 Curso em rascunho | Aluno tenta acessar rota de matrícula de curso com `status = draft` | Resposta 404 `NOT_FOUND` informando que o curso não foi encontrado (R-1); nenhuma matrícula criada. |
| TC153 | 3 – E1 Curso despublicado | CT2 Despublicação durante a matrícula | Instrutor despublica o curso no instante do acionamento de «Matricular-se» | Resposta 409 `CONFLICT` com aviso de que o curso não está mais disponível (R-1); nenhuma matrícula gravada. |
| TC154 | 4 – E2 Pagamento não concluído | CT1 Recusa ou desistência no UC019 | Aluno cancela ou tem pagamento simulado recusado no UC019 | Matrícula em `Enrollment` permanece com status `pending` e acesso às aulas segue bloqueado (R-3); botão «Matricular-se» continua disponível para nova tentativa. |

## 2. UC019 – Processar Pagamento Simulado

**Rastreio:** US018, RF014 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC052 | 1 – Fluxo básico | CT1 Pagamento simulado aprovado | Aluno aciona «Confirmar pagamento» em curso de R$ 150,00 | Transação processada sem acionar gateway externo nem dados reais de cartão (R-1), registro em `Payment` com status `approved` e valor 15000 centavos (R-2), matrícula promovida a status `active` (R-3), resposta 200 `OK` e aulas liberadas. |
| TC155 | 2 – A1 Cancelar no resumo | CT1 Cancelamento pelo aluno | Clique em «Cancelar» no modal de resumo do pagamento | Modal é fechado sem registro em `Payment`, matrícula permanece `pending` sem acesso às aulas (R-3) e nenhum valor é cobrado. |
| TC053 | 3 – E1 Pagamento simulado recusado | CT1 Recusa de pagamento simulado | Confirmação de pagamento simulado em cenário de recusa | Resposta 422 `PAYMENT_DECLINED`, registro gerado em `Payment` com status `declined`, matrícula mantida como `pending` sem liberação das aulas (R-3) e permissão de nova tentativa na mesma matrícula. |
| TC156 | 4 – E2 Preço alterado durante o resumo | CT1 Valor modificado pelo instrutor | Preço do curso é alterado no catálogo após a abertura do modal | Resposta 409 `CONFLICT` com aviso de preço alterado (R-2); pagamento não é registrado e novo resumo com o valor atualizado é apresentado ao aluno. |
| TC157 | 4 – E2 Curso despublicado no pagamento | CT2 Curso retirado do catálogo | Curso é despublicado antes da confirmação do pagamento | Resposta 409 `CONFLICT` informando indisponibilidade do curso; nenhum pagamento registrado. |
| TC158 | 5 – E3 Matrícula duplicada | CT1 Duplo acionamento de confirmação | Dois cliques rápidos consecutivos em «Confirmar pagamento» | Primeira requisição processa com sucesso; segunda recebe 409 `CONFLICT` informando que o aluno já possui matrícula ativa, impedindo pagamento duplicado. |

## 3. UC009 – Assistir Aula

**Rastreio:** US008, US009, RF006 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC022 | 1 – Fluxo básico | CT1 Assistir aula até o fim | Aluno matriculado assiste a todos os 600 segundos da videoaula | Chamada `POST /lessons/{id}/progress` com `concluida: true`, registro em `LessonProgress` com `completed = true` e `completedAt` preenchido, e progresso do curso recalculado de modo desacoplado do quiz (R-2). A regra de desacoplamento não tem R-4 no item 10; ver `pendencias-area-c.md`. |
| TC023 | 2 – A1 Sair da aula antes do fim | CT1 Pausa e saída aos 180 segundos | Aluno pausa vídeo aos 180 segundos de aula de 600 segundos e fecha a tela | Chamada `POST /lessons/{id}/progress` com `segundos_assistidos: 180, concluida: false`, gravando `LessonProgress.watchedSeconds = 180` e `completed = false` (R-2). |
| TC025 | 3 – A2 Retomar aula iniciada | CT1 Retomada no mesmo dispositivo | Aluno abre aula com 180 segundos salvos | Resposta 200 `OK` em `GET /lessons/{id}/stream` contendo URL assinada e `watchedSeconds: 180`; reprodutor inicia a reprodução exatamente a partir do segundo 180 (R-2). |
| TC027 | 3 – A2 Retomada em dispositivo diferente | CT2 Retomada em outro aparelho | Aluno loga em outro navegador/dispositivo e acessa a mesma aula | Backend retorna `watchedSeconds: 180` e vídeo retoma do mesmo ponto salvo independentemente do dispositivo (R-3). |
| TC026 | 3 – A2 Aula já concluída | CT3 Reassistir aula concluída | Aluno acessa aula com status `completed = true` | Vídeo inicia do começo (segundo 0), mas status `completed = true` e `completedAt` permanecem preservados no progresso (R-2). |
| TC024 | 4 – Conclusão de módulo | CT1 Concluir todas as aulas do módulo | Aluno assiste à última aula pendente de um módulo | Percentual de conclusão do módulo atinge 100% e acesso ao quiz do módulo é liberado. A regra não tem R-4 no item 10 de UC009; ver `pendencias-area-c.md`. |
| TC159 | 5 – A4 Visitante em aula prévia | CT1 Reprodução de preview sem login | Visitante sem autenticação acessa aula com `isPreview = true` | Resposta 200 `OK` com URL assinada temporária; vídeo reproduz sem restrição e nenhum progresso é registrado em `LessonProgress` (R-1). |
| TC160 | 6 – E1 Aula bloqueada sem matrícula | CT1 Aluno não matriculado em aula comum | Aluno sem matrícula ativa acessa aula com `isPreview = false` | Resposta 404 `NOT_FOUND` com bloqueio do player e orientação para matricular-se no curso (R-1); nenhuma URL de vídeo emitida. A aula não é revelada a quem não tem acesso. |
| TC161 | 6 – E1 Visitante em aula privada | CT2 Visitante acessa aula privada | Visitante sem login acessa aula com `isPreview = false` | Resposta 401 `UNAUTHENTICATED` e redirecionamento à tela de login; nenhum dado da mídia é vazado (R-1). |
| TC162 | 7 – E2 Falha no carregamento do vídeo | CT1 Erro de conexão com Cloudflare R2 | Falha na resposta do serviço de mídia ao assinar URL | Resposta 503 `SERVICE_UNAVAILABLE` com cabeçalho `Retry-After` e interface exibindo botão de tentar novamente. |
| TC163 | 8 – Negativo Regra R-2 | CT1 Segundos assistidos negativos | Envio de progresso com `segundos_assistidos: -10` | Resposta 422 `VALIDATION_FAILED` no campo `segundos_assistidos`; progresso anterior mantido intacto. |

## 4. UC002 – Responder Quiz

**Rastreio:** US011, RF008 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC031 | 1 – Fluxo básico | CT1 Submissão válida de quiz com correção | Aluno com aulas concluídas responde às 5 questões (3 corretas) e envia | Resposta 200 `OK` (`QuizResultResource`) com nota 60,00 calculada automaticamente contra o gabarito (R-2), respostas e gabarito exibidos lado a lado após envio (regra sem R-4 no item 10 de UC002; ver `pendencias-area-c.md`) e tentativa gravada em `QuizAttempt`. |
| TC033 | 2 – A1 Quiz já respondido sem refazer | CT1 Consulta de tentativa anterior | Aluno acessa quiz já respondido com opção de refazer desabilitada | Resposta 200 `OK` exibindo o resultado e nota salvos; botão de novo envio desabilitado impedindo repetição (R-3). |
| TC164 | 2 – A1 Quiz com permissão de refazer | CT2 Envio de nova tentativa autorizada | Aluno acessa quiz respondido com permissão de refazer e submete novas alternativas | Novo registro gerado em `QuizAttempt` com nova pontuação calculada, mantendo o histórico da tentativa anterior inalterado (R-3, UC004 R-2). |
| TC165 | 3 – A2 Salvar rascunho de respostas | CT1 Rascunho parcial | Aluno assinala 3 de 5 questões e aciona «Salvar rascunho» | Resposta 200 `OK`, respostas parciais salvas; ao reabrir o quiz, as 3 opções marcadas permanecem pré-selecionadas. |
| TC032 | 4 – E1 Questões pendentes no envio | CT1 Envio incompleto de questões | Aluno tenta submeter quiz deixando 2 questões sem marcação | Resposta 422 `VALIDATION_FAILED` indicando as questões pendentes (R-1); nenhuma tentativa é registrada em `QuizAttempt` e nenhuma nota é calculada. |
| TC166 | 5 – E2 Gabarito incompleto no quiz | CT1 Erro ao calcular nota por gabarito ausente | Aluno submete respostas para quiz com questão sem alternativa correta cadastrada | Resposta 500 `INTERNAL_SERVER_ERROR`, registro do erro em log para o instrutor e tentativa cancelada sem corromper o progresso do aluno. |
| TC167 | 6 – E3 Aulas do módulo pendentes | CT1 Acesso com aulas incompletas | Aluno com aulas pendentes no módulo tenta acessar `GET /quizzes/{id}` | Resposta 403 `FORBIDDEN` indicando as aulas pendentes; questões e alternativas do quiz permanecem ocultas. |
| TC168 | 7 – E4 Aluno não matriculado | CT1 Quiz de curso não matriculado | Aluno autenticado tenta carregar quiz de curso em que não está matriculado | Resposta 404 `NOT_FOUND` sem confirmar existência do quiz, protegendo o recurso contra enumeração. |
| TC179 | 8 – Negativo Gabarito oculto antes do envio | CT1 Resposta de quiz sem gabarito | Aluno com aulas concluídas acessa `GET /quizzes/{id}` antes de enviar e inspeciona o corpo da resposta | Resposta 200 `OK` (`QuizResource`) sem qualquer campo de gabarito (`correctOptionId`, `isCorrect`); o gabarito só aparece em `GET /quizzes/{id}/attempt/result` após o envio (TDD, seção 3.3; UC002 fluxo básico, passos 2 e 5). |

## 5. UC010 – Avaliar Curso

**Rastreio:** US014, RF011 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC040 | 1 – Fluxo básico | CT1 Avaliação válida com nota e comentário | Aluno matriculado com 2 aulas concluídas envia nota 5 e comentário «Excelente curso!» | Resposta 201 `Created` (`ReviewResource`), avaliação gravada em `Review`, nota média do curso recalculada e exibida na página (R-1, R-3). |
| TC169 | 1 – Fluxo básico | CT2 Avaliação válida sem comentário | Aluno envia nota 4 com campo de comentário vazio | Resposta 201 `Created`, avaliação registrada com comentário nulo e nota computada na média (R-3). |
| TC041 | 2 – A1 Editar avaliação anterior | CT1 Substituição de avaliação existente | Aluno que já havia avaliado com nota 3 reenvia nota 5 e novo comentário | Resposta 200 `OK`, registro anterior em `Review` atualizado na mesma chave primária sem duplicidade (R-2) e média do curso atualizada. |
| TC170 | 3 – A2 Cancelar alteração | CT1 Descarte de edição de avaliação | Aluno abre modal, altera nota de 5 para 2 e clica em «Cancelar» | Modal é fechado sem salvar; avaliação anterior de nota 5 em `Review` é mantida estritamente inalterada. |
| TC171 | 4 – E1 Nenhuma aula concluída | CT1 Avaliação sem aula assistida | Aluno matriculado com 0 aulas concluídas tenta abrir formulário de avaliação | Resposta 403 `FORBIDDEN` informando que é obrigatório concluir ao menos uma aula para avaliar (R-1); nenhuma avaliação registrada. |
| TC042 | 4 – E1 Aluno não matriculado | CT2 Usuário sem matrícula tenta avaliar | Usuário logado sem matrícula tenta enviar `POST /courses/{id}/reviews` | Resposta 403 `FORBIDDEN` com aviso de que apenas alunos matriculados podem avaliar o curso. |
| TC172 | 5 – E2 Envio sem nota selecionada | CT1 Nota ausente | Aluno envia formulário preenchendo apenas texto no comentário, sem selecionar nota | Resposta 422 `VALIDATION_FAILED` no campo `rating` apontando obrigatoriedade da nota (R-3); banco de dados inalterado. |
| TC173 | 5 – E2 Nota fora da escala | CT2 Nota menor que 1 ou maior que 5 | Envio de requisição com `rating: 6` ou `rating: 0` | Resposta 422 `VALIDATION_FAILED` no campo `rating` indicando escala de 1 a 5 (R-3); nenhuma avaliação gravada. |

## 6. UC020 – Consultar Catálogo de Cursos

**Rastreio:** US019, RF015 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC055 | 1 – Fluxo básico | CT1 Listagem inicial pública | Acesso público a `/courses` sem parâmetros de busca | Resposta 200 `OK` com lista de cursos publicados contendo título, instrutor e preço em R$ ou «Gratuito» (R-1, R-2), paginada em 20 itens (`meta.currentPage: 1`, `meta.perPage: 20`) (R-4). |
| TC056 | 1 – Fluxo básico | CT2 Filtro por categoria existente | Seleção do chip «Programação» (`?category=Programacao&page=1`) | Resposta 200 `OK` contendo exclusivamente cursos publicados pertencentes à categoria «Programação» (R-1, R-3) com estado refletido na URL (R-4). |
| TC174 | 2 – A1 Limpar filtro de categoria | CT1 Seleção do chip «Todas» | Ator com filtro ativo seleciona chip «Todas» (`?category=&page=1`) | Resposta 200 `OK` com catálogo completo de todas as categorias e URL atualizada sem parâmetro de categoria (R-3, R-4). |
| TC178 | 3 – E1 Catálogo vazio | CT1 Nenhum curso publicado no sistema | Base de dados sem nenhum curso em status `published` | Resposta 200 `OK` com array de dados vazio (`data: []`) e exibição da mensagem «Nenhum curso disponível no momento.». |
| TC175 | 4 – E2 Categoria sem cursos | CT1 Categoria cadastrada sem cursos | Seleção de categoria que não possui cursos com status `published` | Resposta 200 `OK` com `data: []`, exibição da mensagem «Nenhum curso encontrado nesta categoria.» e botão para ver todos os cursos (R-1, R-3). |
| TC176 | 5 – Negativo Regra R-1 | CT1 Ocultação de cursos em rascunho | Consulta no catálogo com curso existente em status `draft` | O curso em rascunho não é retornado na listagem da API nem exibido em nenhum card do catálogo (R-1). |
| TC177 | 6 – Negativo Regra R-4 | CT1 Parâmetro de paginação inválido | Requisição com `?page=-1` ou `?per_page=500` | Resposta 422 `VALIDATION_FAILED` nos campos `page` e `per_page` (fields.page, fields.per_page), sem consultar a base, prevenindo sobrecarga ou quebra de consulta (R-4). |

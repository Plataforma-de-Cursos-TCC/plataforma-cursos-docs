## 1. UC006 – Cadastrar Curso

**Rastreio:** US004, RF002 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC010 | 1 – Fluxo básico | CT1 Cadastro de curso em rascunho | Título `Curso de Docker e Kubernetes`, descrição `Do zero à produção`, preço R$ 199,90 (`priceCents: 19990`), categoria `DevOps` | Curso criado com status `rascunho` por padrão (R-1), persistido no banco e retornado com status 201 (`CourseResource`). |
| TC091 | 1 – Fluxo básico | CT2 Publicação de curso válido | Curso em rascunho com módulos e aulas cadastrados; clique em «Publicar» | Status alterado para `publicado`, curso disponibilizado no catálogo público e resposta 200 OK. |
| TC011 | 2 – A1 Editar curso publicado | CT1 Atualizar dados do curso | Curso publicado; alteração de título para `Docker e Kubernetes Avançado` e preço R$ 249,90 | Dados atualizados e refletidos no catálogo; matrículas ativas existentes permanecem inalteradas (200 OK). |
| TC092 | 3 – A2 Cancelar cadastro | CT1 Cancelar no formulário | Preenchimento parcial dos dados do curso; clique em «Cancelar» | O fluxo é encerrado sem gravar nenhuma informação no banco; lista «Meus cursos» permanece inalterada. |
| TC093 | 4 – E1 Campos obrigatórios ausentes | CT1 Título e preço em branco | Título vazio, descrição `Introdução`, preço em branco | Resposta 422 `VALIDATION_FAILED` com `fields.title` e `fields.priceCents` indicando obrigatoriedade; nenhum registro é criado. |
| TC012 | 5 – E2 Excluir curso com matrículas | CT1 Exclusão bloqueada com alunos | Curso com 5 alunos matriculados em `Enrollment`; acionamento de «Excluir curso» | Resposta 422 `VALIDATION_FAILED` com mensagem de bloqueio (R-2), impedindo a exclusão e sugerindo despublicar o curso; dados mantidos intactos. |
| TC094 | 6 – E3 Não proprietário do curso | CT1 Instrutor edita curso de terceiro | Instrutor logado envia `PUT /api/v1/instructor/courses/{id}` para curso de outro instrutor | Resposta 403 `FORBIDDEN`; nenhuma alteração é persistida. |
| TC095 | 7 – E4 Publicar curso sem conteúdo | CT1 Publicar curso vazio | Curso recém-criado em rascunho sem nenhum módulo ou aula cadastrado; clique em «Publicar» | Resposta 422 `VALIDATION_FAILED` informando necessidade de ao menos um módulo e uma aula para publicação; curso permanece em rascunho. |

## 2. UC014 – Gerenciar Módulos do Curso

**Rastreio:** US005, RF003 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC013 | 1 – Fluxo básico | CT1 Adicionar novo módulo | Curso existente; título `Fundamentos de Contêineres`, posição `1` | Módulo criado e associado ao curso na ordem definida, lista de módulos atualizada e resposta 201 Created. |
| TC014 | 2 – A1 Editar e reordenar módulos | CT1 Alterar posição de módulo | Módulo 2 reposicionado para a ordem `3` | Sequência reordenada persistida no banco e exibida na visualização do curso (200 OK). |
| TC015 | 3 – A2 Excluir módulo sem histórico | CT1 Exclusão com confirmação | Módulo sem histórico de alunos, contendo 2 aulas e 1 quiz; confirmação de exclusão | Módulo, suas aulas e seu quiz são removidos em cascata (R-3); resposta 204 No Content e lista atualizada. |
| TC096 | 3 – A2 Excluir módulo sem histórico | CT2 Excluir módulo vazio | Módulo recém-criado sem aulas e sem quiz; acionamento de exclusão e confirmação | Módulo removido com sucesso; resposta 204 No Content. |
| TC097 | 4 – A3 Cancelar exclusão | CT1 Cancelar no diálogo de confirmação | Clique em «Excluir» em módulo existente; clique em «Cancelar» no diálogo de confirmação | Exclusão abortada; módulo, aulas e quiz permanecem intactos na lista do curso. |
| TC098 | 5 – E1 Título ausente | CT1 Criar módulo sem título | Formulário de novo módulo com título em branco e posição `2` | Resposta 422 `VALIDATION_FAILED` em `fields.title`; módulo não é salvo. |
| TC099 | 6 – E2 Posição já utilizada | CT1 Posição duplicada no mesmo curso | Módulo com posição `1` já cadastrado no curso; envio de novo módulo com posição `1` | Resposta 422 `VALIDATION_FAILED` em `fields.order` apontando conflito de posição (R-2); nenhum dado é gravado. |
| TC100 | 7 – E3 Não proprietário do curso | CT1 Módulo em curso de outro instrutor | Envio de `POST /api/v1/instructor/courses/{id}/modules` em curso de terceiro | Resposta 403 `FORBIDDEN` (R-1); criação rejeitada. |
| TC101 | 8 – E4 Exclusão com histórico de progresso | CT1 Módulo com aula assistida | Módulo onde ao menos um aluno possui registro em `LessonProgress`; confirmação de exclusão | Resposta 422 `VALIDATION_FAILED` com bloqueio da exclusão (R-4); módulo, aulas e histórico de progresso permanecem preservados; orientação para apenas editar. |
| TC102 | 8 – E4 Exclusão com histórico de quiz | CT2 Módulo com tentativa de quiz | Módulo onde ao menos um aluno respondeu ao quiz (`QuizAttempt`); confirmação de exclusão | Resposta 422 `VALIDATION_FAILED` com bloqueio da exclusão (R-4); módulo, quiz e histórico de notas permanecem preservados. |

## 3. UC015 – Gerenciar Aulas do Curso

**Rastreio:** US006, RF004, RNF002, RNF004, RNF018 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC016 | 1 – Fluxo básico | CT1 Criar aula com vídeo válido | Módulo existente; título `Instalação do Docker`, descrição `Passo a passo`, ordem `1`, vídeo MP4 de 150 MB | Validação aprovada, URL assinada do Cloudflare R2 gerada com validade de 15 min (RNF002), upload concluído e resposta 201 Created. |
| TC018 | 1 – Fluxo básico | CT2 Marcar aula como prévia | Dados válidos com opção `isPreview: true` marcada | Aula cadastrada com liberação de acesso para visitantes não matriculados (201 Created). |
| TC103 | 1 – Fluxo básico | CT3 Disparo de transcrição após upload | Conclusão do envio do vídeo via URL assinada; acionamento de confirmação de upload | Aula salva com `videoKey`, job assíncrono enfileirado no RabbitMQ para transcrição e indexação pelo serviço de IA (RNF004). |
| TC104 | 2 – A1 Editar aula e trocar vídeo | CT1 Substituição de arquivo de vídeo | Aula existente; seleção de novo vídeo WebM de 200 MB | Nova URL de upload gerada, novo vídeo gravado e reprocessamento único de transcrição disparado, substituindo o anterior (200 OK). |
| TC105 | 3 – A2 Excluir aula sem histórico | CT1 Excluir aula sem alunos | Aula sem registros em `LessonProgress`; confirmação de exclusão | Aula removida do banco de dados (204 No Content) e arquivo de vídeo excluído do storage R2. |
| TC106 | 4 – A3 Cancelar exclusão | CT1 Cancelar no diálogo de confirmação | Clique em «Excluir» em aula existente; clique em «Cancelar» no diálogo de confirmação | Operação cancelada; aula e vídeo permanecem inalterados. |
| TC017 | 5 – E1 Formato de vídeo inválido | CT1 Envio de arquivo AVI | Arquivo de vídeo com extensão `.avi` (30 MB) | Resposta 422 `VALIDATION_FAILED` em `fields.video`, informando que são aceitos apenas MP4 e WebM (R-2, RNF018). |
| TC107 | 5 – E1 Tamanho de vídeo excedido | CT2 Envio de arquivo acima de 500 MB | Arquivo MP4 com tamanho de 550 MB | Resposta 422 `VALIDATION_FAILED` em `fields.video`, informando o limite máximo de 500 MB por arquivo (R-2, RNF018). |
| TC108 | 6 – E2 Falha no envio ou URL expirada | CT1 Upload após 16 minutos | URL pré-assinada emitida há mais de 15 minutos | Upload rejeitado pelo storage com 403 Forbidden; aplicação informa expiração e gera nova URL de 15 minutos para reenvio (RNF002). |
| TC109 | 7 – E3 Não proprietário do curso | CT1 Aula em módulo de outro instrutor | Envio de `POST /api/v1/instructor/modules/{id}/lessons` para módulo de terceiro | Resposta 403 `FORBIDDEN` (R-1); nenhuma URL de upload é gerada e nenhuma aula é criada. |
| TC110 | 8 – E4 Exclusão com histórico de alunos | CT1 Aula assistida por aluno | Aula com registro de progresso em `LessonProgress` (`watchedSeconds > 0` ou `completed = true`); confirmação de exclusão | Resposta 422 `VALIDATION_FAILED` bloqueando a exclusão (R-5); aula e vídeo preservados; orientação para apenas editar. |

## 4. UC004 – Cadastrar Quiz com Gabarito

**Rastreio:** US010, RF007 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC028 | 1 – Fluxo básico | CT1 Cadastro e publicação de quiz | Módulo existente; título `Quiz de Revisão`, 3 perguntas, cada uma com 4 alternativas e exatamente 1 marcada como correta | Quiz validado, salvo e publicado para os alunos matriculados no módulo, com gabarito registrado para correção automática (201 Created). |
| TC111 | 2 – A1 Editar pergunta existente | CT1 Edição mantendo notas anteriores | Quiz existente com tentativas de alunos registradas (`QuizAttempt`); alteração no enunciado da pergunta 1 e do gabarito | Quiz atualizado com sucesso (200 OK); respostas e notas já lançadas nas tentativas anteriores são preservadas sem recálculo (R-2). |
| TC112 | 3 – A2 Salvar como rascunho | CT1 Salvar quiz sem publicar | Quiz com perguntas e gabarito preenchidos; clique em «Salvar como rascunho» | Quiz persistido no banco com visibilidade oculta para os alunos (`status = rascunho`) e resposta 201 Created. |
| TC113 | 4 – A3 Cancelar cadastro | CT1 Cancelar no formulário de quiz | Preenchimento de perguntas e alternativas; clique em «Cancelar» | Operação abortada sem gravar nenhum registro no banco; tela do módulo é recarregada. |
| TC114 | 5 – E1 Menos de duas alternativas | CT1 Pergunta com apenas uma alternativa | Pergunta com texto válido, porém com apenas 1 alternativa cadastrada | Resposta 422 `VALIDATION_FAILED` com indicação de que toda pergunta exige no mínimo duas alternativas (R-1); quiz não é salvo. |
| TC115 | 6 – E2 Pergunta sem gabarito | CT1 Pergunta sem alternativa correta | Pergunta com 4 alternativas cadastradas, nenhuma marcada com `isCorrect = true` | Resposta 422 `VALIDATION_FAILED` informando a obrigatoriedade de marcar a alternativa correta (R-1); quiz não é salvo. |
| TC116 | 7 – E3 Não proprietário do curso | CT1 Quiz em módulo de terceiro | Envio de `POST /api/v1/instructor/modules/{id}/quiz` em módulo de outro instrutor | Resposta 403 `FORBIDDEN`; nenhum quiz é cadastrado. |
| TC117 | 8 – E4 Módulo inexistente | CT1 Quiz para módulo removido | ID de módulo inexistente ou já excluído no endpoint de criação | Resposta 404 `NOT_FOUND` informando módulo não encontrado. |

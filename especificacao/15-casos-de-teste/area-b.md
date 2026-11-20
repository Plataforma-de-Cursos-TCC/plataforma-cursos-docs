## 1. UC006 – Cadastrar Curso

**Rastreio:** US004, RF002 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC010 | 1 – Fluxo básico | CT1 Cadastro de curso em rascunho | Título `Curso de Docker e Kubernetes`, descrição `Do zero à produção`, preço R$ 199,90 (`priceCents: 19990`), categoria `DevOps` | Curso criado com status `draft` por padrão (R-1), persistido no banco e retornado com status 201 (`CourseResource`). |
| TC091 | 1 – Fluxo básico | CT2 Publicação de curso válido | Curso em rascunho com módulos e aulas cadastrados; clique em «Publicar» | Status alterado para `published`, curso disponibilizado no catálogo público e resposta 200 OK. |
| TC011 | 2 – A1 Editar curso publicado | CT1 Atualizar dados do curso | Curso publicado; alteração de título para `Docker e Kubernetes Avançado` e preço R$ 249,90 | Dados atualizados e refletidos no catálogo; matrículas ativas existentes permanecem inalteradas (200 OK). |
| TC124 | 3 – A2 Excluir curso sem matrículas | CT1 Exclusão com confirmação | Curso sem matrículas em `Enrollment`; confirmação de exclusão pelo instrutor proprietário | Curso marcado com exclusão lógica (`deleted_at = NOW()`, ADR-0014) e resposta 204 No Content. |
| TC092 | 4 – A3 Cancelar cadastro de curso | CT1 Cancelamento de novo curso | Formulário de criação de curso com dados preenchidos; clique em «Cancelar» | Operação cancelada, alterações descartadas e retorno à listagem «Meus cursos» sem persistir nenhum registro. |
| TC123 | 5 – A4 Arquivar curso | CT1 Arquivamento de curso | Curso publicado (`status: published`); acionamento de arquivamento pelo instrutor proprietário | Status alterado para `archived` (D-TC266), curso removido das listagens do catálogo público, mantendo acesso apenas aos alunos já matriculados (200 OK). |
| TC093 | 6 – E1 Campos obrigatórios ausentes | CT1 Título e preço em branco | Título vazio, descrição `Introdução`, preço em branco | Resposta 422 `VALIDATION_FAILED` com `fields.title` e `fields.priceCents` indicando obrigatoriedade; nenhum registro é criado. |
| TC012 | 7 – E2 Excluir curso com matrículas | CT1 Exclusão bloqueada com alunos | Curso com 5 alunos matriculados em `Enrollment`; acionamento de «Excluir curso» | Resposta 409 `CONFLICT` com mensagem de bloqueio (R-2), impedindo a exclusão e sugerindo despublicar ou arquivar o curso; dados mantidos intactos. |
| TC094 | 8 – E3 Não proprietário do curso | CT1 Instrutor edita curso de terceiro | Instrutor logado envia `PUT /api/v1/instructor/courses/{id}` para curso de outro instrutor | Resposta 403 `FORBIDDEN` (R-1); nenhuma alteração é persistida. |
| TC095 | 9 – E4 Publicar curso sem conteúdo | CT1 Publicar curso vazio | Curso recém-criado em rascunho sem nenhum módulo ou aula cadastrado; clique em «Publicar» | Resposta 422 `VALIDATION_FAILED` informando necessidade de ao menos um módulo e uma aula para publicação; curso permanece com status `draft`. |

## 2. UC014 – Gerenciar Módulos do Curso

**Rastreio:** US005, RF003 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC013 | 1 – Fluxo básico | CT1 Adicionar novo módulo | Curso existente; título `Fundamentos de Contêineres`, posição `1` | Módulo criado e associado ao curso na ordem definida, lista de módulos atualizada e resposta 201 Created. |
| TC014 | 2 – A1 Editar e reordenar módulos | CT1 Alterar posição de módulo | Módulo 2 reposicionado para a ordem `3` | Sequência reordenada persistida no banco e exibida na visualização do curso (200 OK). |
| TC015 | 3 – A2 Excluir módulo sem histórico | CT1 Exclusão com confirmação | Módulo sem histórico de alunos, contendo 2 aulas e 1 quiz; confirmação de exclusão | Módulo, suas aulas e seu quiz são removidos logicamente em cascata (`deleted_at = NOW()`, R-3, ADR-0014); resposta 204 No Content e lista atualizada. |
| TC096 | 3 – A2 Excluir módulo sem histórico | CT2 Excluir módulo vazio | Módulo recém-criado sem aulas e sem quiz; acionamento de exclusão e confirmação | Módulo removido logicamente com sucesso (`deleted_at = NOW()`); resposta 204 No Content. |
| TC097 | 4 – A3 Cancelar exclusão de módulo | CT1 Cancelamento de exclusão | Diálogo de confirmação de exclusão de módulo exibido; clique em «Cancelar» | Diálogo fechado sem remover o módulo nem alterar suas aulas ou quiz associados. |
| TC098 | 5 – E1 Título ausente | CT1 Criar módulo sem título | Formulário de novo módulo com título em branco e posição `2` | Resposta 422 `VALIDATION_FAILED` em `fields.title`; módulo não é salvo. |
| TC099 | 6 – E2 Posição já utilizada | CT1 Posição duplicada no mesmo curso | Módulo com posição `1` já cadastrado no curso; envio de novo módulo com posição `1` | Resposta 422 `VALIDATION_FAILED` em `fields.order` apontando conflito de posição (R-2); nenhum dado é gravado. |
| TC100 | 7 – E3 Não proprietário do curso | CT1 Módulo em curso de outro instrutor | Envio de `POST /api/v1/instructor/courses/{id}/modules` em curso de terceiro | Resposta 403 `FORBIDDEN` (R-1); criação rejeitada. |
| TC101 | 8 – E4 Exclusão com histórico de progresso | CT1 Módulo com aula assistida | Módulo onde ao menos um aluno possui registro em `LessonProgress`; confirmação de exclusão | Resposta 409 `CONFLICT` com bloqueio da exclusão (R-4); módulo, aulas e histórico de progresso permanecem preservados; orientação para apenas editar. |
| TC102 | 8 – E4 Exclusão com histórico de quiz | CT2 Módulo com tentativa de quiz | Módulo onde ao menos um aluno respondeu ao quiz (`QuizAttempt`); confirmação de exclusão | Resposta 409 `CONFLICT` com bloqueio da exclusão (R-4); módulo, quiz e histórico de notas permanecem preservados. |

## 3. UC015 – Gerenciar Aulas do Curso

**Rastreio:** US006, RF004, RNF002, RNF004, RNF018 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC016 | 1 – Fluxo básico | CT1 Criar aula com vídeo válido | Módulo existente; título `Instalação do Docker`, descrição `Passo a passo`, ordem `1`, vídeo MP4 de 150 MB enviado via API multipart | Arquivo validado, vídeo transmitido via API ao `media-service`, armazenado no Cloudflare R2 com chave retornada, aula salva com `video_key` obrigatório (R-3) e resposta 201 Created (`LessonResource`). |
| TC018 | 1 – Fluxo básico | CT2 Marcar aula como prévia | Dados válidos com opção `isPreview: true` marcada e anexo de vídeo | Aula cadastrada com liberação de acesso para visitantes não matriculados (201 Created). |
| TC103 | 1 – Fluxo básico | CT3 Disparo de transcrição após upload | Envio do vídeo via API concluído com `video_key`; salvamento da aula com `video_key` obrigatório | Aula salva com `video_key`, job assíncrono enfileirado para transcrição e indexação pelo serviço de IA (RNF004) e resposta 201 Created. |
| TC104 | 2 – A1 Editar aula e trocar vídeo | CT1 Substituição de arquivo de vídeo | Aula existente; seleção de novo vídeo WebM de 200 MB via API multipart | Novo vídeo enviado ao `media-service` via API, gravado no R2 e novo job de transcrição enfileirado em substituição ao anterior (200 OK). |
| TC118 | 2 – A1 Editar aula sem trocar vídeo | CT2 Edição de dados sem novo vídeo não reprocessa | Aula já indexada (`indexStatus = indexed`); alteração apenas do título | Dados atualizados (200 OK); nenhum job de transcrição enfileirado e `indexStatus` permanece `indexed` (R-4, A-1.4). |
| TC105 | 3 – A2 Excluir aula sem histórico | CT1 Excluir aula sem alunos | Aula sem registros em `LessonProgress`; confirmação de exclusão | Aula marcada com exclusão lógica (`deleted_at = NOW()`, ADR-0014), materiais vinculados excluídos logicamente, resposta 204 No Content e arquivo de vídeo excluído do storage R2. |
| TC106 | 4 – A3 Cancelar exclusão de aula | CT1 Cancelamento de exclusão | Diálogo de confirmação de exclusão de aula exibido; clique em «Cancelar» | Diálogo fechado sem remover a aula nem o vídeo, mantendo o estado inalterado. |
| TC119 | 5 – A4 Adicionar material complementar em PDF | CT1 Upload de material PDF válido | Aula existente; título `Guia de Comandos Docker`, ordem `1`, arquivo PDF de 15 MB enviado via API multipart | Arquivo validado, transmitido via API ao `media-service`, armazenado no Cloudflare R2, registrado em `LessonMaterial` (B4) e retornado com 201 Created (`LessonMaterialResource`). |
| TC122 | 5 – A4 Excluir material complementar | CT2 Remoção de material complementar | Material complementar existente vinculado à aula; confirmação de exclusão pelo instrutor proprietário | Registro marcado com exclusão lógica (`deleted_at = NOW()`, ADR-0014), arquivo PDF removido do storage e resposta 204 No Content. |
| TC017 | 6 – E1 Formato de vídeo inválido | CT1 Envio de arquivo AVI | Arquivo de vídeo com extensão `.avi` (30 MB) | Resposta 422 `VALIDATION_FAILED` em `fields.video`, informando que são aceitos apenas MP4 e WebM (R-2, RNF018). |
| TC107 | 6 – E1 Tamanho de vídeo excedido | CT2 Envio de arquivo acima de 500 MB | Arquivo MP4 com tamanho de 550 MB | Resposta 422 `VALIDATION_FAILED` em `fields.video`, informando o limite máximo de 500 MB por arquivo (R-2, RNF018). |
| TC108 | 7 – E2 Falha no envio do vídeo ou no armazenamento | CT1 Falha de transmissão ou erro no storage | Queda de conexão durante upload de vídeo ou erro de comunicação da API com o storage Cloudflare R2 | Aplicação informa falha no envio, não cria aula inconsistente e permite nova tentativa de envio pelo instrutor (E2). |
| TC109 | 8 – E3 Não proprietário do curso | CT1 Aula em módulo de outro instrutor | Envio de `POST /api/v1/instructor/modules/{id}/lessons` para módulo de terceiro | Resposta 403 `FORBIDDEN` (R-1); nenhuma aula é criada e nenhum upload é realizado. |
| TC110 | 9 – E4 Exclusão com histórico de alunos | CT1 Aula assistida por aluno | Aula com registro de progresso em `LessonProgress` (`watchedSeconds > 0` ou `completed = true`); confirmação de exclusão | Resposta 409 `CONFLICT` bloqueando a exclusão (R-5); aula e vídeo preservados; orientação para apenas editar. |
| TC120 | 10 – E5 Formato de material complementar inválido | CT1 Envio de arquivo não PDF | Arquivo de material complementar com extensão `.docx` ou `.zip` (5 MB) | Resposta 422 `VALIDATION_FAILED` em `fields.file`, informando que são aceitos apenas arquivos PDF (R-6); nenhum registro persistido. |
| TC121 | 10 – E5 Tamanho de material complementar excedido | CT2 Envio de arquivo PDF acima de 50 MB | Arquivo PDF com tamanho de 55 MB para material complementar | Resposta 422 `VALIDATION_FAILED` em `fields.file`, informando o limite máximo de 50 MB por arquivo (R-6); nenhum registro persistido. |

## 4. UC004 – Cadastrar Quiz com Gabarito

**Rastreio:** US010, RF007 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC028 | 1 – Fluxo básico | CT1 Cadastro e publicação de quiz | Módulo existente; título `Quiz de Revisão`, 3 perguntas, cada uma com 4 alternativas e exatamente 1 marcada como correta | Quiz validado, salvo e publicado para os alunos matriculados no módulo, com gabarito registrado para correção automática (201 Created). |
| TC030 | 2 – A1 Editar pergunta existente | CT1 Edição mantendo notas anteriores | Quiz existente com tentativas de alunos registradas (`QuizAttempt`); alteração no enunciado da pergunta 1 e do gabarito | Quiz atualizado com sucesso (200 OK); respostas e notas já lançadas nas tentativas anteriores são preservadas sem recálculo (R-2). |
| TC112 | 3 – A2 Salvar como rascunho | CT1 Salvar quiz sem publicar | Quiz com perguntas e gabarito preenchidos; clique em «Salvar como rascunho» | Quiz persistido no banco com visibilidade oculta para os alunos (`status = draft`) e resposta 201 Created. |
| TC113 | 4 – A3 Cancelar cadastro de quiz | CT1 Cancelamento de criação de quiz | Formulário de criação de quiz com dados preenchidos; clique em «Cancelar» | Operação cancelada, alterações descartadas e retorno à visualização do módulo sem persistir dados. |
| TC114 | 5 – E1 Menos de duas alternativas | CT1 Pergunta com apenas uma alternativa | Pergunta com texto válido, porém com apenas 1 alternativa cadastrada | Resposta 422 `VALIDATION_FAILED` com indicação de que toda pergunta exige no mínimo duas alternativas (R-1); quiz não é salvo. |
| TC029 | 6 – E2 Pergunta sem gabarito | CT1 Pergunta sem alternativa correta | Pergunta com 4 alternativas cadastradas, nenhuma marcada com `isCorrect = true` | Resposta 422 `VALIDATION_FAILED` informando a obrigatoriedade de marcar a alternativa correta (R-1); quiz não é salvo. |
| TC116 | 7 – E3 Não proprietário do curso | CT1 Quiz em módulo de terceiro | Envio de `POST /api/v1/instructor/modules/{id}/quiz` em módulo de outro instrutor | Resposta 403 `FORBIDDEN` (R-1); nenhum quiz é cadastrado. |
| TC117 | 8 – E4 Módulo inexistente | CT1 Quiz para módulo removido | ID de módulo inexistente ou já excluído no endpoint de criação | Resposta 404 `NOT_FOUND` informando módulo não encontrado. |

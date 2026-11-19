# Pendências da Área C (Aprendizagem do aluno)

Dúvidas que a Área C não resolve sozinha. Cada uma depende de outra área, de um documento que não é da Área C (TDD e casos de teste compartilhados) ou de uma decisão do grupo. Enquanto não houver resposta, o texto da Área C segue a decisão vigente e não inventa requisito.

## 1. Regra R-4 ausente em UC002 (item 10)

- O que está escrito: TC031 e o diagrama de sequência do UC002 mostram nota, alternativas e gabarito lado a lado após o envio, e o TC179 testa que o gabarito não aparece antes do envio (TDD, seção 3.3; UC002 fluxo básico, passos 2 e 5).
- O que falta: a especificação de caso de uso do UC002 (item 10) tem só R-1 a R-3. A exibição do gabarito após o envio e a regra de ocultá-lo antes não aparecem como regra numerada.
- Pedido: incluir R-4 no UC002 do item 10 (área responsável: Área C), ou confirmar que a regra vale só pelo TDD.

## 2. Regra R-4 ausente em UC009 (item 10)

- O que está escrito: o TC022 cita o desacoplamento do progresso do quiz, e o TC024 cita a liberação do quiz quando todas as aulas do módulo estão concluídas.
- O que falta: UC009 tem só R-1 a R-3 no item 10.
- Pedido: incluir R-4 no UC009 do item 10 com essas duas regras, ou confirmar que elas vêm de outro item.

## 3. Conflito entre TDD e decisão: `GET /lessons/{id}/stream` (UC009 E1)

- O TDD (docs/tdd.md, tabela de endpoints) responde `403 FORBIDDEN` para aluno sem matrícula em aula que não é prévia.
- A decisão vigente da análise do grupo é `404 NOT_FOUND` (tabela de erros do TDD, linha 590), para não revelar a existência da aula.
- A Área C segue 404 no diagrama de sequência do UC009, nos casos TC160 e no texto do item 14. O TDD não foi alterado, porque não é arquivo da Área C.
- Pedido: a área do TDD (Área A ou responsável pelo TDD) alinhar o endpoint à decisão de 404.

## 4. Catálogo compartilhado de casos de teste (docs/testes/casos-de-teste.md)

- O catálogo tem TC054 com "curso gratuito sem pagamento" e TC057 com "categoria sem cursos publicados", e a Área C usava o mesmo TC057 para "catálogo vazio". A Área C removeu o TC054 (a regra já está coberta pelo TC019) e renumerou o caso de catálogo vazio para TC178. A categoria sem cursos continua em TC175.
- Pedido: atualizar o catálogo para registrar TC178 e TC179 e remover o TC054 e a descrição antiga do TC057. Arquivo fora da Área C.

## 5. Exceções citadas no item 14 e ausentes no item 13 (resolvido)

- Decisão do coordenador: exceções não viram classe no item 13. Elas aparecem nas sequências como resposta de erro com código HTTP e nome do erro, conforme a tabela de erros do TDD (seção 3.1).
- Ajuste feito: `IncompleteAnswerKeyException` virou `500 INTERNAL_SERVER_ERROR`, `PaymentDeclinedException` virou `422 PAYMENT_DECLINED` e `IneligibleReviewException` virou `403 FORBIDDEN`.

## 6. Status de curso `draft` e `published` (Área B)

- O modelo de dados (item 12), o diagrama de sequência do UC003 e o do UC020 usam `draft` e `published` para o status de `Course`. Esses valores são da Área B.
- Pedido: a Área B confirmar os valores persistidos e o mapeamento para o pt-BR (rascunho e publicado).

## 7. Desnormalização de `Payment` (item 12)

- `Payment` guarda `userId` e `courseId`, que derivam de `Enrollment` pelo `enrollmentId`. Isso fica fora da 3FN, e o documento justifica o desvio pelo registro de auditoria da transação.
- Dúvida para o grupo: aceitar o desvio justificado (como está) ou remover as duas colunas e obter o usuário e o curso pela matrícula.

## 8. Divergência do botão de matrícula pendente: «Concluir pagamento» x «Matricular-se»

- O que foi pedido: a matrícula pendente mostraria o botão «Concluir pagamento» (UC019 e US018).
- O que está escrito: o texto «Concluir pagamento» não existe na especificação. UC003 (E-2.2) e UC019 (E-1.3) dizem que o botão «Matricular-se» continua disponível.
- Decisão aplicada na Área C: TC152 e TC154 usam «Matricular-se», com retomada na mesma matrícula (R-2), sem nova linha em `Enrollment`.
- Pedido: o grupo decidir qual rótulo vale. Se for «Concluir pagamento», a mudança cabe em UC003 e UC019, que estão fora da Área C.

## 9. Campos de `Curso` usados nos casos de teste (Área B)

- TC055 citava o instrutor do curso na listagem pública, e o modelo de dados não tem essa coluna em `Course`. O campo foi removido do TC055.
- TC056 filtra por `category` (`?category=Programacao`), e `Course` não tem categoria no modelo (item 12).
- Pedido: a Área B decidir se `Course` tem `instructorId` e `category`. Se tiver, a Área C recoloca os campos nos casos de teste.

## 10. Nome de paginação: `per_page` (TDD) x `perPage` (DTO)

- O TDD usa `per_page` (padrão 20, máximo 100) como parâmetro de consulta. O DTO de listagem da Área C usa `perPage` no corpo da resposta.
- TC177 mantém `per_page`, porque é o nome do parâmetro do TDD.
- Pedido: confirmar a convenção de nomes para o parâmetro de consulta e para o campo de resposta em todas as áreas.

## 11. Tipos de framework nas assinaturas de método

- As assinaturas de `ProgressRepository`, `ReviewRepository` e `QuizAttemptRepository` usam `LengthAwarePaginator` e `AnonymousResourceCollection`, que são tipos do framework e não tipos de domínio.
- Dúvida para o grupo: manter os tipos de framework no diagrama de classes ou trocar por `List` e `Page`, que são neutros.

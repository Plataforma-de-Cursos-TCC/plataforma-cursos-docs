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

## 5. Exceções citadas no item 14 e ausentes no item 13

- O item 14 mostra exceções como `IncompleteAnswerKeyException`, `PaymentDeclinedException` e `IneligibleReviewException`. O item 13 não as desenha como classes.
- Dúvida: incluí-las no item 13 (como classes de exceção) ou tratá-las como nomes de erro, fora do diagrama de classes?

## 6. Status de curso `draft` e `published` (Área B)

- O modelo de dados (item 12), o diagrama de sequência do UC003 e o do UC020 usam `draft` e `published` para o status de `Course`. Esses valores são da Área B.
- Pedido: a Área B confirmar os valores persistidos e o mapeamento para o pt-BR (rascunho e publicado).

## 7. Desnormalização de `Payment` (item 12)

- `Payment` guarda `userId` e `courseId`, que derivam de `Enrollment` pelo `enrollmentId`. Isso fica fora da 3FN, e o documento justifica o desvio pelo registro de auditoria da transação.
- Dúvida para o grupo: aceitar o desvio justificado (como está) ou remover as duas colunas e obter o usuário e o curso pela matrícula.

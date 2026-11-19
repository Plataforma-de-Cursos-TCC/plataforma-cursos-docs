# Pendências da Área B (Autoria do instrutor)

Dúvidas que dependem de decisão do grupo. Nenhuma foi resolvida inventando regra.

## 1. Cancelamento pelo Instrutor sem regra no item 10

Os diagramas de sequência (item 14) de UC004, UC006, UC014 e UC015 modelam o cancelamento em bloco `alt`. O item 10 desses casos de uso não tem fluxo de cancelamento. Os casos de teste que dependiam dele saíram da planilha do item 15 (TC092, TC097, TC106 e TC113) até o grupo decidir.

**Decisão necessária:** incluir o cancelamento como fluxo alternativo no item 10 (com as regras e o texto de cada caso de uso), ou tirar o `alt` de cancelamento dos diagramas do item 14. Se entrar no item 10, os casos de teste podem voltar com esses IDs.

## 2. Upload direto ao storage fora do item 13

O item 14 (UC015) mostra o envio do vídeo direto ao storage por URL pré-assinada. Essa troca não aparece como mensagem nem como participante no item 13: o diagrama de classes tem `MediaStorageInterface.generateSignedUploadUrl` e `deleteObject`, mas não o cliente que faz o PUT.

**Decisão necessária:** o grupo confirma que o envio é direto do navegador ao storage e entra no item 13 como mensagem externa, ou o envio passa pela API.

## 3. Aula criada antes do upload (videoKey pendente)

O item 14 (UC015) cria a aula com `videoKey` pendente e só depois confirma o upload. O item 10 do UC015 diz que o sistema salva a aula após a confirmação do envio (passo 7). Os dois não batem.

**Decisão necessária:** o grupo escolhe entre criar a aula antes do upload, com `videoKey` nulo até a confirmação (como está nos diagramas), ou salvar a aula só após a confirmação (como está no item 10). A escolha muda o modelo de dados do item 12 e o texto do passo 7.

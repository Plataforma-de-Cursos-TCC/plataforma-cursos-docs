## 1. UC005 – Realizar Login

**Rastreio:** US001, RF017 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC001 | 1 – Fluxo básico | CT1 Login válido | E-mail `ana.souza@example.com`, senha `Senha123`, sem «manter conectado» | Autenticação aceita, cookie de acesso `HttpOnly` emitido e redirecionamento à área do perfil (UC016). |
| TC065 | 1 – Fluxo básico | CT2 Login válido com «manter conectado» | Mesmos dados, com «manter conectado» marcado | Além do cookie de acesso, é emitido o cookie de refresh com validade de 30 dias. |
| TC066 | 2 – A1 Esqueci minha senha | CT1 Acionar a recuperação | Clique em «Esqueci minha senha» na tela de login | O UC011 é iniciado, com a tela de solicitação do link. |
| TC067 | 3 – Sessão já ativa | CT1 Abrir o login com sessão válida | Usuário autenticado acessa `/login` | Vai direto à área do perfil, sem pedir credenciais. |
| TC002 | 4 – E1 Credenciais incorretas | CT1 Senha incorreta | E-mail `ana.souza@example.com`, senha `Senha999` | Acesso recusado com mensagem genérica, sem indicar se o e-mail existe (R-1). |
| TC068 | 4 – E1 Credenciais incorretas | CT2 E-mail inexistente | E-mail `naoexiste@example.com`, senha `Senha123` | Mesma mensagem genérica do CT1; a resposta não diferencia os dois casos (R-1). |
| TC003 | 5 – E2 Sessão expirada | CT1 Acessar rota protegida com sessão expirada | Cookie de acesso vencido (mais de 1 hora) em uma rota protegida | Redirecionamento à tela de login. |
| TC069 | 6 – E3 Conta bloqueada | CT1 Login de conta bloqueada | Conta com status bloqueado e credenciais corretas | Acesso negado, com aviso de conta bloqueada; nenhum cookie é emitido. |
| TC070 | 7 – E4 Tentativas excedidas | CT1 Sexta tentativa após 5 falhas | 5 senhas incorretas seguidas e, depois, a senha correta | A tentativa é recusada com resposta 429 e aviso de bloqueio de 15 minutos (RNF008). |
| TC071 | 7 – E4 Tentativas excedidas | CT2 Login após o bloqueio | Senha correta 15 minutos depois do bloqueio | Autenticação aceita e contador de falhas zerado. |

## 2. UC011 – Recuperar Senha

**Rastreio:** US017, RF013 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC049 | 1 – Fluxo básico | CT1 Solicitar o link | E-mail cadastrado `ana.souza@example.com` | Link de redefinição enviado por e-mail, com validade de 30 minutos (RNF017), e mensagem de confirmação. |
| TC072 | 1 – Fluxo básico | CT2 Redefinir com link válido | Link válido, nova senha `NovaSenha1` e confirmação `NovaSenha1` | Senha substituída, link marcado como usado e retorno ao login (UC005). |
| TC073 | 2 – A1 Novo link | CT1 Usar o link anterior | Dois pedidos seguidos para o mesmo e-mail e uso do primeiro link | O primeiro link é recusado, pois o novo link o invalidou. |
| TC074 | 3 – A2 Cancelar | CT1 Cancelar a redefinição | Clique em «Cancelar» na tela de nova senha | A senha atual é mantida e o link continua válido até expirar. |
| TC050 | 4 – E1 E-mail não cadastrado | CT1 Solicitar com e-mail inexistente | E-mail `naoexiste@example.com` | Mesma mensagem de confirmação do fluxo básico, sem revelar que o e-mail não existe (R-2); nada é enviado. |
| TC051 | 5 – E2 Link expirado | CT1 Usar o link após 30 minutos | Link emitido há mais de 30 minutos e nova senha `NovaSenha1` | Redefinição recusada com resposta 422 e opção de solicitar novo link. |
| TC075 | 6 – E3 Link já usado | CT1 Reutilizar o link | Link já usado em uma redefinição anterior | Redefinição recusada com resposta 422, informando que o link não é válido. |
| TC076 | 6 – E3 Link inválido | CT2 Token adulterado | Link com o token alterado em um caractere | Redefinição recusada com resposta 422, informando que o link não é válido. |

## 3. UC012 – Cadastrar-se na Plataforma

**Rastreio:** US002, RF001 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC004 | 1 – Fluxo básico | CT1 Cadastro válido | E-mail `novo.aluno@example.com`, senha `Senha123`, confirmação `Senha123`, termos aceitos | Conta criada com perfil Aluno, senha guardada em hash, aceite dos termos registrado e redirecionamento ao login. |
| TC077 | 2 – A1 Perfil Instrutor | CT1 Cadastro como Instrutor | Mesmos dados com «Quero ser instrutor» marcado | Conta criada com perfil Instrutor e orientação para preencher o perfil de Instrutor depois do login. |
| TC005 | 3 – E1 E-mail em uso | CT1 E-mail já cadastrado | E-mail `ana.souza@example.com`, já cadastrado | Cadastro recusado com aviso de que o e-mail já está em uso. |
| TC006 | 4 – E2 Senha fora da política | CT1 Senha curta | Senha `abc12` (5 caracteres) | Cadastro recusado com resposta 422, apontando o mínimo de 8 caracteres. |
| TC078 | 4 – E2 Senha fora da política | CT2 Senha sem número | Senha `somenteletras` | Cadastro recusado com resposta 422, apontando a exigência de pelo menos um número. |
| TC079 | 5 – E3 Termos não aceitos | CT1 Cadastro sem o aceite | Dados válidos, caixa de termos e política de privacidade desmarcada (RNF020) | Cadastro recusado com resposta 422, pedindo o aceite; nenhuma conta é criada. |

## 4. UC013 – Editar Dados do Perfil

**Rastreio:** US003, US020, RF001, RF016 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC007 | 1 – Fluxo básico | CT1 Alterar nome e telefone | Nome `Ana Souza Lima`, telefone `(41) 99999-0000` | Dados atualizados e exibidos no perfil. |
| TC080 | 1 – Fluxo básico | CT2 Trocar o tema | Tema `escuro` | Tema salvo e aplicado à interface (R-7). |
| TC081 | 1 – Fluxo básico | CT3 Enviar foto válida | Foto JPG de 1 MB | Foto guardada no storage e exibida no perfil (R-6). |
| TC058 | 2 – A1 Perfil do Instrutor | CT1 Preencher minibiografia e links | Instrutor logado, bio `Engenheira de software há 10 anos`, link `https://github.com/anasouza` | Perfil do Instrutor atualizado e exibido na página do curso. |
| TC060 | 2 – A1 Perfil do Instrutor | CT2 Campos de Instrutor por outro perfil | Aluno tenta enviar bio e links de Instrutor | Alteração negada; os campos de Instrutor não são gravados. |
| TC082 | 3 – A2 Alterar senha | CT1 Acionar «Alterar senha» | Clique em «Alterar senha» no perfil | O UC017 é iniciado. |
| TC009 | 4 – E1 Campo inválido | CT1 Nome em branco | Nome vazio | Envio bloqueado, com indicação do campo obrigatório (R-2). |
| TC083 | 4 – E1 Campo inválido | CT2 CPF inválido | CPF `111.111.111-11` (dígitos verificadores incorretos) | Envio bloqueado, com aviso de CPF inválido (R-3). |
| TC084 | 4 – E1 Campo inválido | CT3 Foto acima de 2 MB | Foto PNG de 3 MB | Envio bloqueado, com aviso do limite de 2 MB (R-6). |
| TC085 | 4 – E1 Campo inválido | CT4 Nascimento futuro | Data de nascimento `01/01/2030` | Envio bloqueado, com aviso de data inválida (R-4). |
| TC059 | 5 – E2 Link ou bio inválidos | CT1 Link em formato inválido | Instrutor logado, link `github ponto com barra ana` | Alteração recusada, com a indicação do campo de link. |
| TC086 | 6 – E3 Acesso negado | CT1 Editar perfil de outro Instrutor | Instrutor A envia a atualização do perfil do Instrutor B | Resposta 403 e acesso negado; nada é alterado. |

## 5. UC017 – Alterar Senha

**Rastreio:** US021, RF019 (itens 6, 7 e 10).

| ID | CENÁRIO | CASO DE TESTE | ENTRADAS | RESULTADO ESPERADO |
|---|---|---|---|---|
| TC061 | 1 – Fluxo básico | CT1 Alterar a senha | Senha atual `Senha123`, nova `NovaSenha1`, confirmação `NovaSenha1` | Senha substituída e confirmação exibida. |
| TC088 | 2 – A1 Cancelar | CT1 Cancelar a alteração | Clique em «Cancelar» com os campos preenchidos | A senha atual é mantida e nenhum dado é gravado. |
| TC062 | 3 – E1 Senha atual incorreta | CT1 Senha atual errada | Senha atual `Senha999`, nova `NovaSenha1`, confirmação `NovaSenha1` | Troca recusada, com aviso de senha atual incorreta (R-1). |
| TC089 | 4 – E2 Nova senha fora da política | CT1 Nova senha curta | Senha atual `Senha123`, nova `abc12`, confirmação `abc12` | Troca recusada, apontando a política de senha (R-2). |
| TC064 | 5 – E3 Confirmação diferente | CT1 Confirmação divergente | Senha atual `Senha123`, nova `NovaSenha1`, confirmação `NovaSenha2` | Troca bloqueada, com indicação do campo de confirmação (R-3); a senha não muda. |

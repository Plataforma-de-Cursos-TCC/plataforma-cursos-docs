## 1. UC005 – Realizar Login

Fluxo básico, alternativo A1 (esqueci minha senha) e exceções do login: bloqueio por tentativas (E4), credencial inválida (E1), conta bloqueada (E3) e emissão do refresh com «manter conectado».

![Diagrama de sequência do UC005](../diagramas/14-sequencia-uc005.png)

*Figura 0 – UC005, diagrama de sequência: realizar login*

## 2. UC011 – Recuperar Senha

Duas fases: solicitação do link (E1 anti-enumeração, A1 novo link invalida o anterior) e redefinição (E2 link expirado, E3 link usado ou inválido, A2 cancelar).

![Diagrama de sequência do UC011, solicitação do link](../diagramas/14-sequencia-uc011-1.png)

*Figura 0 – UC011, diagrama de sequência: solicitação do link*

![Diagrama de sequência do UC011, redefinição da senha](../diagramas/14-sequencia-uc011-2.png)

*Figura 0 – UC011, diagrama de sequência: redefinição da senha*

## 3. UC012 – Cadastrar-se na Plataforma

Validação pelo Form Request (E2 senha fora da política, E3 termos não aceitos), e-mail em uso (E1) e o alternativo A1, que cria a conta com perfil Instrutor.

![Diagrama de sequência do UC012](../diagramas/14-sequencia-uc012.png)

*Figura 0 – UC012, diagrama de sequência: cadastrar-se na plataforma*

## 4. UC013 – Editar Dados do Perfil

Validação (E1, E2), acesso negado a quem não é o dono (E3), upload da foto no R2, o alternativo A1 do Instrutor (minibiografia e links) e A2 (alterar senha).

![Diagrama de sequência do UC013](../diagramas/14-sequencia-uc013.png)

*Figura 0 – UC013, diagrama de sequência: editar dados do perfil*

## 5. UC017 – Alterar Senha

Validação da política e da confirmação (E2, E3), senha atual incorreta (E1) e cancelamento (A1).

![Diagrama de sequência do UC017](../diagramas/14-sequencia-uc017.png)

*Figura 0 – UC017, diagrama de sequência: alterar senha*

# 13 DIAGRAMA DE CLASSES

**PRODUTO:** Plataforma de Cursos

Diagrama de classes em nível técnico, com elementos negociais (classes do domínio) e de implementação (Controller, Form Request, Service e Repository da API Laravel, em MVC). Atributos aparecem como `nome: tipo`, métodos como `nome(parâmetros): retorno`, com visibilidade (`-` privado, `#` protegido, `+` público) e multiplicidade nas associações. Uma classe referencia o tipo do objeto relacionado, nunca o id da chave estrangeira (`userId` existe só no modelo do item 12). Cada área apresenta as classes dos seus casos de uso; os métodos daqui são as mensagens dos diagramas de sequência do item 14.

| Nº | ÁREA | CLASSES | ARQUIVO |
|---|---|---|---|
| 1 | A (Acesso e conta) | User e subclasses, Address, InstructorProfile, PasswordResetToken, RefreshSession, controllers, serviços e repositórios de acesso | [area-a.md](area-a.md) |
| 2 | B (Autoria do instrutor) | a preencher | [area-b.md](area-b.md) |
| 3 | C (Aprendizagem do aluno) | a preencher | [area-c.md](area-c.md) |
| 4 | D (Tutor de IA, analytics e administração) | a preencher | [area-d.md](area-d.md) |

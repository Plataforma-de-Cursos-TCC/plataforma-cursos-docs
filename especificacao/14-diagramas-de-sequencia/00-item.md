# 14 DIAGRAMAS DE SEQUÊNCIA

**PRODUTO:** Plataforma de Cursos

Um diagrama de sequência por caso de uso, mostrando a interação entre as camadas: o ator, a tela e o Controller (boundary), o Service (control), o Repository e a entidade (entity) e o banco de dados (database). As mensagens são os métodos do diagrama de classes (item 13) e o fluxo básico vem da especificação do caso de uso (item 10); cada fluxo de exceção vira uma região de um fragmento `alt`; cada fluxo alternativo também é um `alt`, e o cancelamento é a última região do `alt` que encerra o diagrama (sem `opt` seguido de continuação). O mínimo exigido é de 4 casos de uso para a equipe; cada área entrega os diagramas dos seus casos de uso prioritários.

| Nº | UC | CASO DE USO | ÁREA | ARQUIVO |
|---|---|---|---|---|
| 1 | UC005 | Realizar login | A (Acesso e conta) | [area-a.md](area-a.md) |
| 2 | UC011 | Recuperar senha | A (Acesso e conta) | [area-a.md](area-a.md) |
| 3 | UC012 | Cadastrar-se na plataforma | A (Acesso e conta) | [area-a.md](area-a.md) |
| 4 | UC013 | Editar dados do perfil | A (Acesso e conta) | [area-a.md](area-a.md) |
| 5 | UC017 | Alterar senha | A (Acesso e conta) | [area-a.md](area-a.md) |
| 6 | UC004 | Cadastrar quiz com gabarito | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| 7 | UC006 | Cadastrar curso | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| 8 | UC014 | Gerenciar módulos do curso | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| 9 | UC015 | Gerenciar aulas do curso | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| 10 | UC002 | Responder quiz | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| 11 | UC003 | Matricular-se em curso | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| 12 | UC009 | Assistir aula | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| 13 | UC010 | Avaliar curso | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| 14 | UC019 | Processar pagamento simulado | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| 15 | UC020 | Consultar catálogo de cursos | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| 16 | UC001 | Conversar com Tutor de IA | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| 17 | UC007 | Ver dashboard com filtro | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| 18 | UC008 | Gerenciar usuários | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| 19 | UC016 | Acessar área protegida por perfil | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| 20 | UC018 | Excluir e anonimizar usuário | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |

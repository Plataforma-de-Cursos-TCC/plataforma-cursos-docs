# 10 ESPECIFICAÇÕES DE CASO DE USO

O template exige a especificação de, no mínimo, 8 casos de uso, com protótipos de tela de alta fidelidade e fluxos principal, alternativo e de exceção.

O conteúdo fica nos arquivos area-a.md a area-d.md, nessa ordem. Os IDs provisórios por área são renumerados em sequência única antes da revisão final (ADR-0001).

**PRODUTO:** Plataforma de Cursos

Índice das 16 especificações de caso de uso, distribuídas nas quatro áreas (4 casos de uso por integrante/área).

| ID provisório | ID v11 | CASO DE USO | ATOR(ES) | ÁREA | ARQUIVO |
|---|---|---|---|---|---|
| UC-A1 | UC012 | Cadastrar-se na plataforma | Visitante | A (Acesso e conta) | [area-a.md](area-a.md) |
| UC-A2 | UC005 | Realizar login | Aluno, Instrutor, Administrador | A (Acesso e conta) | [area-a.md](area-a.md) |
| UC-A3 | UC011 | Recuperar senha | Aluno, Instrutor, Administrador (ainda não autenticado) | A (Acesso e conta) | [area-a.md](area-a.md) |
| UC-A4 | UC013 | Editar dados do perfil | Aluno, Instrutor, Administrador | A (Acesso e conta) | [area-a.md](area-a.md) |
| UC-B1 | UC006 | Cadastrar curso | Instrutor | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| UC-B2 | UC014 | Gerenciar módulos do curso | Instrutor | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| UC-B3 | UC015 | Gerenciar aulas do curso | Instrutor | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| UC-B4 | UC004 | Cadastrar quiz com gabarito | Instrutor | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| UC-C1 | UC003 | Matricular-se em curso | Aluno | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| UC-C2 | UC009 | Assistir aula | Aluno | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| UC-C3 | UC002 | Responder quiz | Aluno | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| UC-C4 | UC010 | Avaliar curso | Aluno | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| UC-D1 | UC001 | Conversar com Tutor de IA | Aluno (primário); Tutor de IA (ator sistêmico, secundário) | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| UC-D2 | UC007 | Ver dashboard com filtro | Instrutor, Administrador | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| UC-D3 | UC008 | Gerenciar usuários | Administrador | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| UC-D4 | UC016 | Acessar área protegida por perfil | Aluno, Instrutor, Administrador | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |

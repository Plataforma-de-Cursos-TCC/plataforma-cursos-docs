# 12 MODELO DE DADOS

**PRODUTO:** Plataforma de Cursos

Modelo lógico do banco de dados, na perspectiva relacional e com notação UML, derivado dos requisitos funcionais (item 6) e das especificações de caso de uso (item 10). Cada tabela é uma caixa com nome, região da chave primária e demais campos; PK e FK ficam à esquerda, campos obrigatórios em negrito e a seta da chave estrangeira aponta para a tabela que guarda a chave primária. A cardinalidade usa `1` e `n`. Cada área apresenta o diagrama das suas tabelas e o dicionário de dados.

| Nº | ÁREA | TABELAS | ARQUIVO |
|---|---|---|---|
| 1 | A (Acesso e conta) | User, Address, InstructorProfile, PasswordResetToken, RefreshSession | [area-a.md](area-a.md) |
| 2 | B (Autoria do instrutor) | categories, courses, modules, lessons, lesson_materials, quizzes, questions, question_options | [area-b.md](area-b.md) |
| 3 | C (Aprendizagem do aluno) | enrollments, payments, lesson_progress, quiz_attempts, quiz_answers, reviews | [area-c.md](area-c.md) |
| 4 | D (Tutor de IA, analytics e administração) | conversations, messages, tutor_credit_packs, audit_logs | [area-d.md](area-d.md) |

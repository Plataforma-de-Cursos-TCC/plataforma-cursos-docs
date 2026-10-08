# 5 RELAÇÃO DE ATORES / USUÁRIOS

O template exige a relação dos atores e usuários do sistema, com papel e relação com o processo. Nomes dos atores idênticos aos do CONTEXT.md.

| # | ATOR / USUÁRIO | DESCRIÇÃO / RESPONSABILIDADES / RELAÇÃO COM O SISTEMA |
|---|---|---|
| 1 | Usuário | Ator geral (generalização) de Aluno, Instrutor e Administrador: quem tem conta, faz login e edita o próprio perfil. No diagrama de casos de uso, Aluno, Instrutor e Administrador herdam as associações do Usuário. |
| 2 | Visitante | Pessoa sem conta ou sem sessão. Consulta o catálogo e cadastra-se. Depois do login, passa a atuar como Usuário (Aluno, Instrutor ou Administrador). Ator primário. |
| 3 | Aluno | Usuário autenticado que se matricula, assiste às aulas, responde a quizzes, avalia cursos e conversa com o tutor de IA. Ator primário. |
| 4 | Instrutor | Usuário que cria e gerencia cursos, módulos, aulas e quizzes, mantém seu perfil e acompanha o dashboard da turma. Ator primário. |
| 5 | Administrador | Usuário que gerencia contas e perfis de acesso e consulta o dashboard geral da plataforma. Ator primário. |
| 6 | Tutor de IA | Ator sistêmico secundário. Responde às perguntas do aluno com base no conteúdo transcrito do curso, citando aula e timestamp. |

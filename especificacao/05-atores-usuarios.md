# 5 RELAÇÃO DE ATORES / USUÁRIOS

| # | ATOR / USUÁRIO | DESCRIÇÃO / RESPONSABILIDADES / RELAÇÃO COM O SISTEMA |
|---|---|---|
| 1 | Usuário | Ator geral (generalização) de Aluno, Instrutor e Administrador: quem tem conta, faz login e edita o próprio perfil. No diagrama de casos de uso, Aluno, Instrutor e Administrador herdam as associações do Usuário. |
| 2 | Visitante | Pessoa sem conta ou sem sessão. Consulta o catálogo e cadastra-se. Depois do login, passa a atuar como Usuário (Aluno, Instrutor ou Administrador). Ator primário. |
| 3 | Aluno | Usuário autenticado que se matricula, assiste às aulas, responde a quizzes, avalia cursos e conversa com o Tutor de IA. Ator primário. |
| 4 | Instrutor | Usuário que cria e gerencia cursos, módulos, aulas e quizzes, mantém seu perfil e acompanha o dashboard da turma. Ator primário. |
| 5 | Administrador | Usuário que gerencia contas e perfis de acesso e consulta o dashboard geral da plataforma. Ator primário. |
| 6 | Tutor de IA | Ator sistêmico secundário. Responde às perguntas do aluno com base no conteúdo transcrito do curso, citando a aula e o minuto do vídeo de origem. |

**Plataforma de Cursos:** é o próprio sistema, não um ator. Aparece como pool e como raia "Plataforma" no mapeamento de negócios (item 4) e como raia "Plataforma de Cursos" no diagrama de atividades (item 11) para agrupar o que o sistema executa (armazenar e transcrever aulas, processar o pagamento simulado, registrar matrícula e progresso, calcular a nota do quiz). Nos casos de uso (itens 9 e 10), o sistema é a fronteira do diagrama, e só os atores da tabela acima interagem com ele. O Tutor de IA é o único componente do sistema modelado como ator, por ser sistêmico secundário ([ADR-0005](../docs/adr/0005-tutor-de-ia-como-ator-sistemico.md)).

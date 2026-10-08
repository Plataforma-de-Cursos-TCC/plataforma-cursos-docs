# 8 RELAÇÃO DE REQUISITOS NÃO-FUNCIONAIS

**PRODUTO:** Plataforma de Cursos

| # | REQUISITO NÃO-FUNCIONAL | NORMA ISO/IEC 25010 |
|---|---|---|
| RNF001 | Autenticação por token JWT com expiração de 1 h; 100% das áreas protegidas verificam o perfil do usuário. | Segurança (autenticidade) |
| RNF002 | Upload de vídeo somente por URL assinada com expiração de 15 min; 0 acessos diretos ao armazenamento. | Segurança (confidencialidade) |
| RNF003 | Resposta do Tutor de IA em streaming, com o primeiro trecho em até 3 s no percentil 95. | Eficiência de desempenho (comportamento temporal) |
| RNF004 | Transcrição e embeddings gerados uma única vez por aula; 0 reprocessamentos em acessos repetidos à mesma aula. | Eficiência de desempenho (utilização de recursos) |
| RNF005 | 100% dos campos obrigatórios validados com mensagem de erro clara. | Capacidade de interação (proteção contra erro do usuário) |
| RNF006 | Cobertura mínima de 75% dos testes automatizados do backend; merge bloqueado abaixo disso. | Manutenibilidade (testabilidade) |
| RNF007 | 0 senhas em texto puro (armazenadas com hash). | Segurança (confidencialidade) |
| RNF008 | Bloqueio do login por 15 min após 5 tentativas inválidas consecutivas. | Segurança (resistência) |
| RNF009 | Listagens da API com p95 de até 2 s com 1000 usuários simultâneos. | Eficiência de desempenho (comportamento temporal) |
| RNF010 | Disponibilidade mensal mínima de 99%. | Confiabilidade (disponibilidade) |
| RNF011 | Backup diário do banco de dados, com restauração testada mensalmente. | Confiabilidade (recuperabilidade) |
| RNF012 | Interface conforme WCAG 2.1 AA: contraste mínimo de 4,5:1 e navegação completa por teclado. | Capacidade de interação (inclusividade) |
| RNF013 | 100% dos textos em pt-BR e en; datas, números e valores formatados conforme o idioma. | Capacidade de interação (inclusividade) |
| RNF014 | Alternância entre modo claro e escuro em 100% das telas, com a preferência salva por usuário. | Capacidade de interação (engajamento do usuário) |
| RNF015 | 100% dos endpoints da API documentados em OpenAPI e acessíveis online. | Manutenibilidade (analisabilidade) |
| RNF016 | Registro de 100% das ações administrativas, retido por 12 meses. | Segurança (responsabilização) |
| RNF017 | Link de redefinição de senha de uso único, com expiração de 30 min. | Segurança (autenticidade) |
| RNF018 | Vídeo de aula aceito somente em mp4 ou webm, com até 500 MB por arquivo. | Eficiência de desempenho (capacidade) |
| RNF019 | Layout funcional de 360 a 1920 px de largura. | Flexibilidade (adaptabilidade) |
| RNF020 | Aceite de termos e da política de dados pessoais (LGPD) registrado em 100% dos cadastros. | Segurança (responsabilização) |

<!-- revisar: RNF017 e RNF018 são rascunhos tirados das regras do UC011 e do UC015; o grupo valida os valores -->

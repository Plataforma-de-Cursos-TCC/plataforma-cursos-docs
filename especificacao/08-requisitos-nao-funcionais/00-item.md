# 8 RELAÇÃO DE REQUISITOS NÃO-FUNCIONAIS

**PRODUTO:** Plataforma de Cursos

Requisitos classificados segundo a norma da Organização Internacional de Normalização (ISO, *International Organization for Standardization*) e da Comissão Eletrotécnica Internacional (IEC, *International Electrotechnical Commission*), a ISO/IEC 25010 (ISO/IEC, 2011).

| # | REQUISITO NÃO-FUNCIONAL | NORMA ISO/IEC 25010 |
|---|---|---|
| RNF001 | Autenticação por token JWT (*JSON Web Token*) (JONES; BRADLEY; SAKIMURA, 2015) com expiração de 1 h; 100% das áreas protegidas verificam o perfil do usuário. | Segurança (autenticidade) |
| RNF002 | Upload de vídeo e de material somente pela Interface de Programação de Aplicações (API, do inglês *Application Programming Interface*), que grava no armazenamento; reprodução somente por URL assinada (*Uniform Resource Locator*) com expiração de 15 min; 0 acessos diretos ao armazenamento. | Segurança (confidencialidade) |
| RNF003 | Resposta do Tutor de IA em streaming, com o primeiro trecho em até 3 s no percentil 95. | Eficiência de desempenho (comportamento temporal) |
| RNF004 | Transcrição e embeddings gerados uma única vez por aula, salvo quando o vídeo é substituído (UC015 A1); 0 reprocessamentos em acessos repetidos à mesma aula. | Eficiência de desempenho (utilização de recursos) |
| RNF005 | 100% dos campos obrigatórios validados, com mensagem que indica o campo e a regra violada em 100% dos casos. | Capacidade de interação (proteção contra erro do usuário) |
| RNF006 | Cobertura mínima de 75% dos testes automatizados do backend; merge bloqueado abaixo disso. | Manutenibilidade (testabilidade) |
| RNF007 | 0 senhas em texto puro (armazenadas com hash). | Segurança (confidencialidade) |
| RNF008 | 0 logins aceitos durante os 15 min seguintes a 5 tentativas inválidas consecutivas na mesma conta. | Segurança (resistência) |
| RNF009 | Listagens da API com p95 de até 2 s com 1000 usuários simultâneos; listagens paginadas (`perPage` padrão 20, máximo 100; fora disso 422 VALIDATION_FAILED). | Eficiência de desempenho (comportamento temporal) |
| RNF010 | Disponibilidade mensal mínima de 99%. | Confiabilidade (disponibilidade) |
| RNF011 | Backup diário do banco de dados e dos arquivos de vídeo e material das aulas, com restauração dos dois testada mensalmente. | Confiabilidade (recuperabilidade) |
| RNF012 | Interface conforme as Diretrizes de Acessibilidade para Conteúdo Web (WCAG, *Web Content Accessibility Guidelines*), versão 2.1 nível AA (*Double-A*) (W3C, 2018): contraste mínimo de 4,5:1 e navegação completa por teclado. | Capacidade de interação (inclusividade) |
| RNF013 | 100% dos textos em pt-BR, em arquivos de tradução prontos para receber en e es sem mudança de código; datas, números e valores formatados conforme o idioma. | Capacidade de interação (inclusividade) |
| RNF014 | Alternância entre modo claro e escuro em 100% das telas, aplicada em até 1 s sem recarregar a página. | Capacidade de interação (engajamento do usuário) |
| RNF015 | 100% dos endpoints da API documentados no padrão OpenAPI (OPENAPI INITIATIVE, 2021) e acessíveis online. | Manutenibilidade (analisabilidade) |
| RNF016 | 100% das ações administrativas com registro auditável em PostgreSQL (POSTGRESQL GLOBAL DEVELOPMENT GROUP, 2023) (autor, ação, data, endereço IP (*Internet Protocol*) e detalhes), particionado mensalmente e retido por 12 meses no banco operacional, com arquivamento frio compactado no Cloudflare R2 (CLOUDFLARE, 2022) por 5 anos via job diário audit:archive. | Segurança (responsabilização) |
| RNF017 | Link de redefinição de senha de uso único, com expiração de 30 min. | Segurança (autenticidade) |
| RNF018 | Vídeo de aula aceito somente em formato MP4 (*MPEG-4 Part 14*) ou WebM, com até 500 MB por arquivo. | Eficiência de desempenho (capacidade) |
| RNF019 | Layout funcional de 360 a 1920 px de largura. | Portabilidade (adaptabilidade) |
| RNF020 | Aceite de termos e da política de dados pessoais em conformidade com a LGPD (BRASIL, 2018) registrado em 100% dos cadastros. | Segurança (responsabilização) |
| RNF021 | Cobertura mínima de 75% dos testes automatizados do frontend; merge bloqueado abaixo disso. | Manutenibilidade (testabilidade) |
| RNF022 | Preço fixo por pacote de créditos extras do Tutor de IA (R$ 19,90 por 50 mensagens adicionais), adquirido exclusivamente via pagamento simulado (sem cobrança financeira real). | Adequação funcional (completude funcional) |
| RNF023 | Todo operador externo de dados (hospedagem, armazenamento de mídia, envio de e-mail, transcrição e modelo de linguagem) deve estar vinculado por contrato de tratamento de dados (DPA) com cláusulas-padrão contratuais da ANPD (Resolução CD/ANPD nº 19/2024) em caso de transferência internacional e cláusula expressa vedando o uso de dados de alunos e instrutores para treinamento de modelos de IA. | Segurança (responsabilização) |
| RNF024 | Manter atualizados o Registro de Operações de Tratamento de Dados Pessoais (ROPA, LGPD art. 37) e o Relatório de Impacto à Proteção de Dados Pessoais (RIPD, LGPD art. 38) para o Tutor de IA e o tratamento de dados de menores, revisados a cada mudança de fluxo ou de operador de dados. | Segurança (responsabilização) |
| RNF025 | Divulgar publicamente no rodapé e na Política de Privacidade a identidade e o canal de contato do Encarregado pelo Tratamento de Dados Pessoais (LGPD, art. 41; Resolução CD/ANPD nº 18/2024), garantindo resposta a requisições de confirmação e acesso em formato simplificado imediato ou declaração completa em até 15 dias (LGPD, art. 19). | Segurança (responsabilização) |

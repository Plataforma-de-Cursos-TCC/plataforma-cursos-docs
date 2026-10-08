# 8 RELAÇÃO DE REQUISITOS NÃO-FUNCIONAIS

O template exige a lista de requisitos não-funcionais, classificados segundo a norma ISO/IEC 25010.

O conteúdo fica nos arquivos area-a.md a area-d.md, nessa ordem. Os IDs provisórios por área são renumerados em sequência única antes da revisão final (ADR-0001).

**PRODUTO:** Plataforma de Cursos

Índice dos 16 requisitos não-funcionais, com a área e a característica ISO/IEC 25010 de cada um.

| ID provisório | ID v11 | REQUISITO NÃO-FUNCIONAL | CARACTERÍSTICA ISO/IEC 25010 | ÁREA | ARQUIVO |
|---|---|---|---|---|---|
| RNF-A1 | RNF001 | Autenticação por token JWT e rotas protegidas por perfil (aluno/instrutor/admin) | Segurança | A (Acesso e conta) | [area-a.md](area-a.md) |
| RNF-A2 | RNF007 | Senhas armazenadas com hash e consentimento para uso de dados pessoais (LGPD) | Segurança | A (Acesso e conta) | [area-a.md](area-a.md) |
| RNF-A3 | RNF008 | Bloqueio temporário de login após tentativas inválidas | Segurança | A (Acesso e conta) | [area-a.md](area-a.md) |
| RNF-B1 | RNF002 | Upload de vídeo somente por URL assinada, nunca por acesso direto ao armazenamento | Segurança | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| RNF-B2 | RNF006 | Cobertura de testes automatizados no backend, com merge travado abaixo do mínimo | Manutenibilidade | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| RNF-B3 | RNF015 | Documentação da API em OpenAPI disponível online | Manutenibilidade | B (Autoria do instrutor) | [area-b.md](area-b.md) |
| RNF-C1 | RNF005 | Interface com validação de campo obrigatório, mensagem de erro clara e layout responsivo | Capacidade de Interação | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| RNF-C2 | RNF012 | Acessibilidade da interface (WCAG 2.1 AA) | Acessibilidade | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| RNF-C3 | RNF013 | Internacionalização de textos, datas, números e valores | Capacidade de Interação | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| RNF-C4 | RNF014 | Modo escuro na interface | Capacidade de Interação | C (Aprendizagem do aluno) | [area-c.md](area-c.md) |
| RNF-D1 | RNF003 | Resposta do chat com tutor de IA em streaming, para reduzir a percepção de latência | Eficiência de Desempenho | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| RNF-D2 | RNF004 | Transcrição e embeddings gerados uma única vez por aula (cache), sem reprocessar a cada acesso | Eficiência de Desempenho | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| RNF-D3 | RNF009 | Desempenho das listagens da API sob carga | Eficiência de Desempenho | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| RNF-D4 | RNF010 | Disponibilidade do serviço | Confiabilidade | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| RNF-D5 | RNF011 | Backup do banco de dados com restauração testada | Confiabilidade | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |
| RNF-D6 | RNF016 | Trilha de auditoria das ações administrativas | Segurança | D (Tutor de IA, analytics e administração) | [area-d.md](area-d.md) |

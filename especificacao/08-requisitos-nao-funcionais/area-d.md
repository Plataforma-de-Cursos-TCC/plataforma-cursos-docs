# 8 RELAÇÃO DE REQUISITOS NÃO-FUNCIONAIS – ÁREA D (Tutor de IA, analytics e administração)

O template exige a lista de requisitos não-funcionais, classificados segundo a norma ISO/IEC 25010.

Área D: Tutor de IA, analytics e administração. Responsável: Vinicius Lima Teider (`Teider011`). IDs: RNF-D1, RNF-D2… (mínimo 4 por integrante, sem máximo; ADR-0001).

| # | REQUISITO NÃO-FUNCIONAL | CARACTERÍSTICA ISO/IEC 25010 | SUBCARACTERÍSTICA | CRITÉRIO MENSURÁVEL |
|---|---|---|---|---|
| RNF-D1 (RNF003) | Resposta do chat com tutor de IA em streaming, para reduzir a percepção de latência | Eficiência de Desempenho | - | Primeiro trecho da resposta em até 3 s no percentil 95. |
| RNF-D2 (RNF004) | Transcrição e embeddings gerados uma única vez por aula (cache), sem reprocessar a cada acesso | Eficiência de Desempenho | - | 0 reprocessamentos em acessos repetidos à mesma aula. |
| RNF-D3 (RNF009) | Desempenho das listagens da API sob carga | Eficiência de Desempenho | - | p95 das listagens de até 2 s com 1000 usuários simultâneos. |
| RNF-D4 (RNF010) | Disponibilidade do serviço | Confiabilidade | - | Disponibilidade mensal mínima de 99%. |
| RNF-D5 (RNF011) | Backup do banco de dados com restauração testada | Confiabilidade | - | Backup diário; restauração testada mensalmente. |
| RNF-D6 (RNF016) | Trilha de auditoria das ações administrativas | Segurança | - | Registro de 100% das ações administrativas, retido por 12 meses. |

<!-- revisar: RNF-D6 (RNF016) é requisito de segurança ligado a ações administrativas (UC016 / gerenciar usuários); alocado na área do UC relacionado conforme regra de ingestão (ADR 0006) -->

<!-- revisar: a v11 classifica diretamente por característica da ISO/IEC 25010 sem coluna de subcaracterística; preenchido com '-' sem inventar dado -->

# 8 RELAÇÃO DE REQUISITOS NÃO-FUNCIONAIS – ÁREA A (Acesso e conta)

O template exige a lista de requisitos não-funcionais, classificados segundo a norma ISO/IEC 25010.

Área A: Acesso e conta. Responsável: Lucas Stopinski da Silva (`LucasStop`). IDs: RNF-A1, RNF-A2… (mínimo 4 por integrante, sem máximo; ADR-0001).

| # | REQUISITO NÃO-FUNCIONAL | CARACTERÍSTICA ISO/IEC 25010 | SUBCARACTERÍSTICA | CRITÉRIO MENSURÁVEL |
|---|---|---|---|---|
| RNF-A1 (RNF001) | Autenticação por token JWT e rotas protegidas por perfil (aluno/instrutor/admin) | Segurança | - | Token com expiração de 1 h; 100% das rotas protegidas verificam o perfil. |
| RNF-A2 (RNF007) | Senhas armazenadas com hash e consentimento para uso de dados pessoais (LGPD) | Segurança | - | 0 senhas em texto puro; aceite de termos e política registrado em 100% dos cadastros. |
| RNF-A3 (RNF008) | Bloqueio temporário de login após tentativas inválidas | Segurança | - | Bloqueio de 15 min após 5 tentativas inválidas consecutivas. |

<!-- revisar: a v11 classifica diretamente por característica da ISO/IEC 25010 sem coluna de subcaracterística; preenchido com '-' sem inventar dado -->

<!-- revisar: Área A com 3 RNFs, abaixo do mínimo de 4 (ADR 0001); ver _lacunas.md -->

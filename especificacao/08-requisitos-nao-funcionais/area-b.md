# 8 RELAÇÃO DE REQUISITOS NÃO-FUNCIONAIS – ÁREA B (Autoria do instrutor)

O template exige a lista de requisitos não-funcionais, classificados segundo a norma ISO/IEC 25010.

Área B: Autoria do instrutor. Responsável: Adrian Antônio de Souza Gomes (`adrian69-droid`). IDs: RNF-B1, RNF-B2… (mínimo 4 por integrante, sem máximo; ADR-0001).

| # | REQUISITO NÃO-FUNCIONAL | CARACTERÍSTICA ISO/IEC 25010 | SUBCARACTERÍSTICA | CRITÉRIO MENSURÁVEL |
|---|---|---|---|---|
| RNF-B1 (RNF002) | Upload de vídeo somente por URL assinada, nunca por acesso direto ao armazenamento | Segurança | - | URL assinada com expiração de 15 min; 0 acessos diretos ao armazenamento. |
| RNF-B2 (RNF006) | Cobertura de testes automatizados no backend, com merge travado abaixo do mínimo | Manutenibilidade | - | Cobertura mínima de 75%; merge bloqueado abaixo disso. |
| RNF-B3 (RNF015) | Documentação da API em OpenAPI disponível online | Manutenibilidade | - | 100% dos endpoints documentados e acessíveis online. |

<!-- revisar: RNF-B1 (RNF002) é requisito de segurança associado ao upload de vídeo de aula (UC015 / autoria do instrutor); alocado na área do UC relacionado conforme regra de ingestão (ADR 0006) -->

<!-- revisar: a v11 classifica diretamente por característica da ISO/IEC 25010 sem coluna de subcaracterística; preenchido com '-' sem inventar dado -->

<!-- revisar: Área B com 3 RNFs, abaixo do mínimo de 4 (ADR 0001); ver _lacunas.md -->

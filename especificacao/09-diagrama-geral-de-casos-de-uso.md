# 9 DIAGRAMA GERAL DE CASOS DE USO

Fonte: `especificacao/diagramas/09-casos-de-uso.puml` (PlantUML, [ADR-0004](../docs/adr/0004-diagramas-como-codigo.md)). O «extend» segue a [ADR-0003](../docs/adr/0003-extend-no-sentido-do-te3-3.md): a seta sai do caso de uso opcional e aponta para o caso de uso base.

![Diagrama Geral de Casos de Uso](diagramas/09-casos-de-uso.png)

*Figura 2 – Diagrama Geral de Casos de Uso*

### 9.1 RASTREABILIDADE ENTRE REQUISITOS FUNCIONAIS E CASOS DE USO

A coluna Objetivo indica qual dos 3 objetivos do item 1 o RF atende.

| RF | UC | OBJETIVO | ÁREA | PRIORIDADE | JUSTIFICATIVA |
|---|---|---|---|---|---|
| RF001 | UC012, UC013, UC017 | 1 | A | Must Have | Base de acesso à plataforma. |
| RF002 | UC006 | 1 | B | Must Have | Sem curso cadastrado não há conteúdo. |
| RF003 | UC014 | 1 | B | Must Have | Organiza o curso em módulos. |
| RF004 | UC015 | 1 | B | Must Have | Conteúdo central do curso e insumo do Tutor de IA. |
| RF005 | UC003 | 1 | C | Must Have | Libera o acesso do Aluno ao curso. |
| RF006 | UC009 | 2 | C | Must Have | Permite retomar a aula e medir a conclusão. |
| RF007 | UC004 | 2 | B | Should Have | Avalia o aprendizado do módulo. |
| RF008 | UC002 | 2 | C | Should Have | Dá retorno imediato ao Aluno. |
| RF009 | UC001 | 2 | D | Should Have | Diferencial do produto. |
| RF010 | UC007 | 3 | D | Should Have | Decisão do Instrutor orientada a dados. |
| RF011 | UC010 | 3 | C | Could Have | Coleta a opinião do Aluno sobre o curso. |
| RF012 | UC008, UC018 | 1 | D | Must Have | Segurança e organização dos usuários. |
| RF013 | UC011 | 1 | A | Should Have | Evita a perda de acesso à conta. |
| RF014 | UC019 | 1 | C | Must Have | Viabiliza o curso pago sem gateway externo. |
| RF015 | UC020 | 1 | C | Should Have | Descoberta de cursos pelo catálogo; coberto pela estória US019. |
| RF016 | UC013 (fluxo A1) | 1 | B | Could Have | Apresenta o Instrutor aos alunos. |
| RF017 | UC005 | 1 | A | Must Have | Acesso às áreas da plataforma. |
| RF018 | UC016 | 1 | D | Must Have | Cada perfil vê só a sua área. |

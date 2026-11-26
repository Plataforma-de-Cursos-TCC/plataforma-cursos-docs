---
id: pesquisa-lgpd
titulo: "Base legal e regulatória — LGPD aplicada à Plataforma de Cursos"
tipo: pesquisa-regulatoria
itens_template: [8, 10, 12]
areas: [A, B, C, D]
decisoes: [D8, D10, D14, D16, D19]
fontes: [F81, F82, F83, F84, F85, F86, F87, F88, F89]
relacionados: [mapa-pesquisa, adr-0008, adr-0010, adr-0014, adr-0016, adr-0019, sdd, tdd]
status: vigente
atualizado: 2026-11-25
---
# Base legal e regulatória — LGPD aplicada à Plataforma de Cursos

> Base de conhecimento do projeto · consolida os dispositivos legais da LGPD (Lei nº 13.709/2018), do Marco Civil da Internet (Lei nº 12.965/2014), do ECA (Lei nº 8.069/1990) e das normas e guias da ANPD aplicáveis à **Plataforma de Cursos** (sistema web de cursos online no Brasil com Visitante, Aluno, Instrutor, Administrador e Tutor de IA via RAG com provedor externo de LLM e transcrição STT; pagamento simulado; menores de idade possíveis).
>
> **Convenção:** afirmações verificadas diretamente no texto legal ou em atos normativos oficiais da ANPD vão marcadas como `[Fato]` com o ID de [fontes.md](fontes.md); interpretações jurídicas ou técnicas aplicadas à arquitetura do projeto vão marcadas como `[Inferência]`.

---

## 1. Definições fundamentais (LGPD, art. 5º)

- `[Fato][F81]` A LGPD define *dado pessoal* (informação relacionada a pessoa natural identificada ou identificável), *dado pessoal sensível* (origem racial/étnica, convicção religiosa, opinião política, filiação sindical/religiosa/filosófica/política, saúde, vida sexual, dado genético ou biométrico), *dado anonimizado*, *titular*, *controlador*, *operador*, *encarregado*, *tratamento*, *consentimento*, *eliminação* e *transferência internacional de dados* (LGPD, art. 5º).
- `[Inferência][F81]` Na Plataforma de Cursos, endereço IP combinado a `user_agent`, `user_id`/`target_id` e timestamps em `audit_logs`, bem como texto livre enviado ao Tutor de IA, comentários em avaliações, fotos de perfil e voz/imagem do Instrutor em videoaulas qualificam-se como dados pessoais (art. 5º, I) e podem conter incidentalmente dados pessoais sensíveis (art. 5º, II).

## 2. Princípios do tratamento (LGPD, art. 6º)

- `[Fato][F81]` Todo tratamento deve observar a boa-fé e dez princípios: finalidade, adequação, necessidade (limitação ao mínimo necessário), livre acesso, qualidade dos dados, transparência, segurança, prevenção, não discriminação e responsabilização e prestação de contas (LGPD, art. 6º).
- `[Inferência][F81]` Coletar CPF (`document_number`), endereço de cobrança/entrega (`addresses`) e data de nascimento (`birth_date`) em plataforma com pagamento apenas simulado, sem entrega física e sem emissão de certificado com validade legal tensiona os princípios da finalidade e da necessidade (art. 6º, I e III) se não houver justificativa documental formal no ROPA.

## 3. Bases legais e requisitos do consentimento (LGPD, arts. 7º, 8º e 9º)

- `[Fato][F81]` O tratamento de dados pessoais comuns exige enquadramento em uma das hipóteses legais do art. 7º (consentimento, cumprimento de obrigação legal ou regulatória, execução de contrato ou procedimentos preliminares, exercício regular de direitos, legítimo interesse, entre outras).
- `[Fato][F81]` Quando baseado em consentimento (art. 7º, I), ele deve ser fornecido por escrito em cláusula destacada das demais cláusulas contratuais (§ 1º) ou por outro meio que demonstre manifestação de vontade; o ônus da prova cabe ao controlador (§ 2º); autorizações genéricas são nulas (§ 4º); e a revogação deve ser possível a qualquer momento mediante procedimento gratuito e facilitado (§ 5º) (LGPD, art. 8º, §§ 1º a 5º).
- `[Fato][F81]` O titular tem direito ao acesso facilitado a informações claras, adequadas e ostensivas sobre finalidade específica, forma e duração do tratamento, identificação e contato do controlador, uso compartilhado, responsabilidades dos agentes e direitos do art. 18 (LGPD, art. 9º).
- `[Fato][F85]` Segundo o Guia Orientativo sobre Cookies e Proteção de Dados Pessoais da ANPD, cookies estritamente necessários podem amparar-se em legítimo interesse com transparência ao titular, enquanto cookies não necessários exigem consentimento prévio (*opt-in*) e mecanismo facilitado de recusa.

## 4. Dados pessoais sensíveis e anonimização (LGPD, arts. 11 e 12)

- `[Fato][F81]` Dados pessoais sensíveis só podem ser tratados mediante consentimento específico e destacado para finalidades específicas ou nas hipóteses estritas sem consentimento previstas no art. 11, II.
- `[Fato][F81]` O dado anonimizado deixa de ser considerado dado pessoal apenas quando o processo de anonimização não puder ser revertido, considerando meios técnicos razoáveis e disponíveis na ocasião do tratamento (LGPD, art. 12).
- `[Fato][F85]` Estudos técnicos da ANPD sobre anonimização ressaltam que a anonimização é avaliada pelo risco de reidentificação e que a anonimização posterior não convalida coleta originariamente ilícita.

## 5. Crianças e adolescentes (LGPD, art. 14; ECA, art. 2º; Enunciado CD/ANPD nº 1/2023)

- `[Fato][F83]` Pelo Estatuto da Criança e do Adolescente, considera-se criança a pessoa até doze anos de idade incompletos, e adolescente aquela entre doze e dezoito anos de idade (ECA, art. 2º).
- `[Fato][F81]` O tratamento de dados pessoais de crianças e adolescentes deve ser realizado em seu melhor interesse; para crianças, o art. 14, § 1º prevê consentimento específico e em destaque dado por pelo menos um dos pais ou responsável legal, devendo o controlador realizar todos os esforços razoáveis para verificar esse consentimento com as tecnologias disponíveis (§ 5º) e fornecer informações de maneira simples, clara e acessível (§ 6º).
- `[Fato][F86]` O Enunciado CD/ANPD nº 1/2023 firmou o entendimento de que o tratamento de dados pessoais de crianças e adolescentes pode apoiar-se nas hipóteses legais dos arts. 7º ou 11 da LGPD, desde que observado e prevalecente o melhor interesse do menor avaliado no caso concreto.

## 6. Término do tratamento, eliminação, retenção legal e backups (LGPD, arts. 15 e 16; MCI, art. 15)

- `[Fato][F81]` O término do tratamento ocorre quando verificada a finalidade alcançada, o fim do período de tratamento, a comunicação do titular (inclusive revogação do consentimento) ou determinação da autoridade nacional (LGPD, art. 15).
- `[Fato][F81]` Encerrado o tratamento, os dados pessoais devem ser eliminados, autorizada a conservação apenas para: (I) cumprimento de obrigação legal ou regulatória pelo controlador; (II) estudo por órgão de pesquisa; (III) transferência a terceiro, respeitados os requisitos da Lei; ou (IV) uso exclusivo do controlador, vedado acesso por terceiro e desde que anonimizados os dados (LGPD, art. 16).
- `[Fato][F82]` O provedor de aplicações de internet constituído como pessoa jurídica com atividade organizada, profissional e fins econômicos deve manter registros de acesso a aplicações de internet, sob sigilo, em ambiente controlado e de segurança, pelo prazo de 6 meses (Marco Civil da Internet, art. 15).
- `[Fato][F85]` Documentos de planejamento e monitoramento da ANPD reconhecem o óbice técnico para exclusão seletiva dentro de cópias de segurança (*backups*) sem comprometer integridade, tratando o tema sob governança e ciclo de vida até eliminação ou anonimização definitiva.
- `[Inferência][F81][F85]` Para conformidade com os arts. 15, 16, 46 e 49 da LGPD, os backups da Plataforma de Cursos devem possuir prazo máximo de rotação definido, criptografia e procedimento de supressão ou re-anonimização pós-restauração para impedir a reintrodução de contas já eliminadas ou anonimizadas.

## 7. Direitos do titular e prazos de atendimento (LGPD, arts. 18, 19 e 20)

- `[Fato][F81]` O titular tem direito a obter do controlador, a qualquer momento e mediante requisição: (I) confirmação da existência de tratamento; (II) acesso aos dados; (III) correção de dados incompletos, inexatos ou desatualizados; (IV) anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou desconformes; (V) portabilidade; (VI) eliminação dos dados tratados com consentimento, salvo art. 16; (VII) informação das entidades públicas e privadas com as quais houve uso compartilhado; (VIII) informação sobre a possibilidade de não fornecer consentimento e consequências da negativa; e (IX) revogação do consentimento (LGPD, art. 18).
- `[Fato][F81]` A confirmação de existência ou o acesso a dados pessoais deve ser providenciada imediatamente em formato simplificado (art. 19, I) ou por declaração clara e completa no prazo de até 15 dias (art. 19, II) (LGPD, art. 19).
- `[Fato][F81]` O titular tem direito de solicitar revisão de decisões tomadas unicamente com base em tratamento automatizado de dados pessoais que afetem seus interesses e de obter informações claras sobre critérios e procedimentos utilizados (LGPD, art. 20 e § 1º).

## 8. Transferência internacional de dados (LGPD, arts. 33 a 36; Resolução CD/ANPD nº 19/2024)

- `[Fato][F81]` A transferência internacional de dados pessoais somente é permitida nas hipóteses do art. 33, como país ou organismo internacional com grau adequado (I), garantias contratuais — incluindo cláusulas-padrão contratuais, cláusulas específicas ou normas corporativas globais — (II), consentimento específico e em destaque com informação prévia sobre o caráter internacional (VIII), ou hipóteses do art. 7º, II, V e VI (IX) (LGPD, arts. 33 a 36).
- `[Fato][F89]` A Resolução CD/ANPD nº 19, de 23 de agosto de 2024, aprovou o Regulamento de Transferência Internacional de Dados e instituiu o conteúdo obrigatório das Cláusulas-Padrão Contratuais (CPCs) para operações transfronteiriças.

## 9. Registro de operações, RIPD e deveres do operador (LGPD, arts. 37, 38 e 39)

- `[Fato][F81]` Controlador e operador devem manter registro das operações de tratamento de dados pessoais que realizarem, especialmente quando baseado no legítimo interesse (LGPD, art. 37).
- `[Fato][F81]` A ANPD pode determinar ao controlador a elaboração de Relatório de Impacto à Proteção de Dados Pessoais (RIPD), inclusive referente a dados sensíveis (LGPD, art. 38).
- `[Inferência][F81]` Da cadeia controlador–operador (arts. 5º, VI–VII, e 39), provedores de LLM, transcrição (STT), nuvem (Vercel, Railway, Cloudflare R2) e envio de e-mail atuam como operadores e exigem contrato de tratamento de dados (DPA) vinculando o tratamento às instruções do controlador e vedando uso secundário, em especial o treinamento de modelos de IA.

## 10. Encarregado pelo tratamento de dados — DPO (LGPD, art. 41; Resoluções CD/ANPD nº 18/2024 e nº 2/2022)

- `[Fato][F81]` O controlador deve indicar encarregado pelo tratamento de dados pessoais, cuja identidade e informações de contato devem ser divulgadas publicamente, preferencialmente no sítio eletrônico do controlador, para atender titulares, receber comunicações da ANPD e orientar a equipe (LGPD, art. 41, caput e §§ 1º e 2º).
- `[Fato][F84][F88]` A Resolução CD/ANPD nº 18, de 16 de julho de 2024, exige indicação formal do encarregado, autonomia técnica, prevenção de conflitos de interesse e divulgação pública dos canais de contato, ressalvadas as hipóteses de dispensa para agentes de tratamento de pequeno porte previstas na Resolução CD/ANPD nº 2/2022.
- `[Inferência][F84][F88]` Mesmo que a Plataforma de Cursos se enquadre como agente de pequeno porte, a presença potencial de crianças e adolescentes e o uso de IA generativa podem configurar tratamento de alto risco (afastando dispensas), e ainda que houvesse dispensa do Encarregado permaneceria obrigatório manter canal público de comunicação com titulares.

## 11. Segurança, *privacy by design* e comunicação de incidentes (LGPD, arts. 46 a 49; Resolução CD/ANPD nº 15/2024)

- `[Fato][F81]` Agentes de tratamento devem adotar medidas de segurança técnicas e administrativas contra acessos não autorizados e eventos acidentais ou ilícitos, observadas desde a fase de concepção do produto ou serviço até sua execução (*privacy/security by design*, art. 46, § 2º), estruturando os sistemas conforme padrões de segurança, boas práticas e governança (art. 49) (LGPD, arts. 46 a 49).
- `[Fato][F81]` O controlador deve comunicar à ANPD e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante (LGPD, art. 48).
- `[Fato][F87]` A Resolução CD/ANPD nº 15, de 24 de abril de 2024 (RCIS), fixa o prazo de **3 dias úteis** a partir da ciência para comunicação à ANPD e aos titulares (em dobro para agentes de pequeno porte), estabelece critérios de risco relevante (como dados sensíveis, de crianças/adolescentes, de autenticação ou em larga escala) e exige manutenção de registro interno de todos os incidentes por no mínimo **5 anos**.

---

## Ligações

- **Fontes oficiais:** [fontes.md](fontes.md) (F81 a F89) · **Mapa de pesquisa:** [README.md](README.md)
- **Artefatos LGPD do projeto:** [ROPA](../docs/lgpd/ropa.md) · [RIPD](../docs/lgpd/ripd.md) · [Encarregado e canais públicos](../docs/lgpd/encarregado-e-canais.md)
- **Decisões relacionadas:** [ADR-0008](../docs/adr/0008-sessao-jwt-em-cookie.md) · [ADR-0010](../docs/adr/0010-hospedagem-e-armazenamento.md) · [ADR-0014](../docs/adr/0014-exclusao-logica-e-anonimizacao.md) · [ADR-0016](../docs/adr/0016-retencao-de-logs-e-auditoria.md) · [ADR-0019](../docs/adr/0019-upload-pela-api.md)
- **Especificação e arquitetura:** [RNF020, RNF023–RNF025](../especificacao/08-requisitos-nao-funcionais/00-item.md) · [SDD](../docs/sdd.md) · [TDD](../docs/tdd.md) · [CONTEXT.md](../CONTEXT.md)

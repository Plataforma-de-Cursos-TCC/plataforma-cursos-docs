---
id: adr-0010
titulo: "ADR-0010 — Hospedagem na Vercel e no Railway, mídia no Cloudflare R2"
tipo: decisao
decisao: D10
status: aceita
data: 2026-10-09
decisor: Grupo
itens_template: [5, 11]
areas: [A, B, C, D]
relacionados: [adr-0007, adr-0008]
---
# ADR-0010 — Hospedagem na Vercel e no Railway, mídia no Cloudflare R2

- **Status:** aceita · **Data:** 09/10/2026 · **Decisor:** Grupo

## Contexto

- A [ADR-0007](0007-stack-e-bancos.md) previa uma VPS única com Docker Compose. O grupo decidiu hospedar o front-end na Vercel, o back-end no Railway e os arquivos de mídia no Cloudflare R2.
- O RNF002 e o RNF018 exigem URLs assinadas e vídeos de até 500 MB por aula; o cookie da [ADR-0008](0008-sessao-jwt-em-cookie.md) exige que o navegador veja um único host.
- Base: [hospedagem-e-jwt.md](../pesquisas/hospedagem-e-jwt.md).

## Alternativas

- **VPS única (ADR-0007 original):** mais barata e previsível, mas exige administrar servidor, TLS e backups. Substituída.
- **Tudo na Vercel:** o back-end Laravel, os microsserviços e os bancos não cabem no modelo de funções da Vercel.
- **Mídia no Railway ou no próprio disco:** sem CDN e sem URL assinada nativa. Descartada.
- **Vercel + Railway + Cloudflare R2:** escolhida.

## Decisão

1. O front-end Next.js (SPA) fica na Vercel. Um `rewrite` de `/api/:path*` para o Railway faz o navegador ver um único host, o que mantém o cookie `__Host-` da ADR-0008. A origem recusa chamadas que não tragam o cabeçalho secreto da Vercel.
2. O core Laravel, o `ai-service` e o `media-service` rodam como serviços Docker no Railway, com MySQL 8, PostgreSQL 16 com `pgvector`, Redis e RabbitMQ no mesmo projeto, em rede privada. Apenas a API do core é pública.
3. Vídeos, imagens e arquivos ficam em bucket privado do Cloudflare R2. O navegador envia e baixa por URL assinada gerada pela API, direto no domínio S3 do R2, sem passar pelo `rewrite`. O CORS do bucket libera somente a origem do front-end.
4. Domínio: **pendente**. Enquanto não houver domínio próprio, usa-se o domínio padrão da Vercel. Se for comprado, o DNS fica na Cloudflare.

## Consequências

- **Custo variável:** Railway cobra por uso (Hobby US$ 5/mês com crédito equivalente) e o R2 tem 10 GB gratuitos; estimativa real **a confirmar** após o primeiro deploy.
- **Pontos a confirmar antes de implementar:** `pgvector` e RabbitMQ no Railway, upload de 500 MB (PUT ou multipart) e `Range` no R2, `Set-Cookie` com `__Host-` pelo `rewrite`, plano da Vercel para uso comercial.
- **Menos operação:** sem servidor próprio, TLS e deploy ficam com as plataformas; em troca, há dependência de três fornecedores.
- **Efeito na ADR-0007:** os trechos sobre VPS única e Docker Compose em produção ficam superados por esta decisão; o Docker Compose continua válido para desenvolvimento local.

---

## Ligações

- **Pesquisa:** [hospedagem-e-jwt.md](../pesquisas/hospedagem-e-jwt.md)
- **Stack:** [ADR-0007](0007-stack-e-bancos.md) · **Sessão:** [ADR-0008](0008-sessao-jwt-em-cookie.md)
- **SDD:** [sdd.md](../sdd.md) · **Índice:** [README.md](README.md)

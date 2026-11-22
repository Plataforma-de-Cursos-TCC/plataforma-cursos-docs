---
id: adr-0019
titulo: "ADR-0019 — Upload de arquivos pela API, chave no banco e leitura por URL assinada"
tipo: decisao
decisao: D19
status: aceita
data: 2026-11-22
decisor: Grupo
itens_template: [8, 10, 12, 13, 14]
areas: [A, B, C, D]
relacionados: [adr-0010, adr-0018]
---
# ADR-0019 — Upload de arquivos pela API, chave no banco e leitura por URL assinada

- **Status:** aceita · **Data:** 22/11/2026 · **Decisor:** Grupo

## Contexto

- O item 3 da [ADR-0010](0010-hospedagem-e-armazenamento.md) dizia que o navegador envia os arquivos direto ao Cloudflare R2, por URL assinada.
- A especificação do RA2 seguiu outro caminho: o RNF002, o UC015, o modelo de dados da Área B e o TDD mandam o arquivo para a API, e o `media-service` grava no R2. A revisão cruzada final (#135) apontou a contradição.
- A foto de perfil (Área A) era descrita como arquivo de URL pública, o que também contradizia o bucket privado.

## Opções consideradas

- **Upload direto do navegador ao R2 por URL assinada (ADR-0010):** tira o tráfego da API, mas a validação de tipo, tamanho e dono do arquivo fica depois do envio.
- **Upload pela API:** a API valida antes de gravar e o `media-service` cuida dos arquivos grandes. Escolhida.
- **Banco guardar a URL do arquivo:** exige bucket público e contradiz o RNF002. Descartada.

## Decisão

1. Todo arquivo (vídeo, material da aula, thumbnail do curso e foto de perfil) é enviado à API em `multipart/form-data`. A API valida e o `media-service` grava no bucket privado do Cloudflare R2.
2. O banco guarda a **chave** do objeto no R2 (por exemplo `video_key`, `file_key`, `photo`), nunca uma URL.
3. A leitura é sempre por URL assinada gerada pela API, com expiração (15 minutos no vídeo, RNF002). Não há arquivo público.
4. Substitui o item 3 da ADR-0010; os demais itens dela continuam valendo.

## Consequências

- O tráfego de upload passa pela API e pelo `media-service`, que precisam aceitar até 500 MB por vídeo (RNF018).
- A foto de perfil e a thumbnail também saem por URL assinada; o front-end pede a URL à API ao exibir.
- O item 13 da Área A deixa de descrever `PhotoStorage` com URL pública.

---

## Ligações

- **Substitui parte de:** [ADR-0010](0010-hospedagem-e-armazenamento.md) · **Módulos:** [ADR-0018](0018-core-como-monolito-modular.md)
- **Revisão:** [ra2-revisao-cruzada.md](../../entregas/ra2-revisao-cruzada.md) · **Índice:** [README.md](README.md)

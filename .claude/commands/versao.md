---
description: Fecha uma versão do documento de especificação (bump, changelog, PR, merge, tag, Release e DOCX). Duas etapas.
argument-hint: "preparar X.Y.Z \"resumo\" | concluir X.Y.Z"
---

Feche a versão do documento de especificação do repositório `Plataforma-de-Cursos-TCC/plataforma-cursos-docs`. Argumentos: `$ARGUMENTS`.

## Interpretação dos argumentos

- 1º argumento: `preparar` ou `concluir`.
- 2º argumento: a versão sem o `v` (ex.: `2.0.8`). A tag é `vX.Y.Z`.
- 3º argumento (só em `preparar`): resumo do que mudou, em português, com o porquê. Sem resumo, leia `git log` e `git diff main` e proponha um antes de seguir.
- Argumento faltando ou versão que não sobe a atual (`VERSAO` em `scripts/build_doc.py`): pare e pergunte.

## Regras que valem nas duas etapas

- Autor: conta `LucasStop` no `gh` (confira `gh auth status`) e `git -c user.name="Lucas Stopinski da Silva" -c user.email=lucas.stopinski@pucpr.edu.br`. Sem `Co-Authored-By`, sem `Claude-Session`.
- Commits em inglês, Conventional Commits completo (`tipo(escopo): resumo` + linha em branco + corpo com o porquê).
- Template do build: `/Users/lucasstopinski/Desktop/Especificação de Software/2026-08-06 - Semana 2/ESSW - Especificacao de Projeto - Template.docx`. Python do projeto: `.venv/bin/python`.
- O `--check` do build **não** regenera `docs/f`; só o build normal regenera. Sem esse passo os links curtos das figuras ficam na versão antiga.
- O merge com `--admin` só sai com ordem explícita do Lucas na conversa. Sem ela, pare no PR verde e peça a ordem.

## Etapa `preparar`

1. Confira `git status` limpo e `main` atualizada; crie a branch `feat/<assunto>` ou `docs/<assunto>` a partir da `main`.
2. Mudanças do documento (se houver) em commit próprio, com o corpo explicando o porquê.
3. Suba `VERSAO` em `scripts/build_doc.py` para `vX.Y.Z` e faça um commit só disso (`feat(build)` ou `docs(build)`, conforme o caso).
4. Rode o build normal (sem `--check`, sem `--saida`): isso regenera os 185 `docs/f/N.html` para `vX.Y.Z`. Confirme com `grep -c vX.Y.Z docs/f/1.html`. Commit: `docs(build): point short Fonte links at vX.Y.Z`.
5. Rode `build_doc.py 1 15 --check` com o template; precisa terminar em `check ok`.
6. Push e `gh pr create` com os labels `sem-issue` e `sem-changelog` e título em Conventional Commits. Corpo em português: o que mudou e a contagem de páginas se o layout mudou.
7. Com o número do PR, em `CHANGELOG.md`: transforme o conteúdo de `[Não lançado]` (ou escreva) em `## [X.Y.Z] - AAAA-MM-DD`, deixando `## [Não lançado]` vazio acima; cada linha termina com `(#N)`; ajuste os links de comparação no rodapé (`[Não lançado]` compara `vX.Y.Z...HEAD` e `[X.Y.Z]` compara a anterior com `vX.Y.Z`). Commit: `docs(changelog): close version X.Y.Z`. Push.
8. Vigie o CI até o fim (`gh pr checks N`, sem `sleep` em foreground longo; use Monitor). Verde: avise. Vermelho: leia o log, corrija e empurre de novo.
9. Pare e peça ao Lucas a ordem de merge com `--admin`.

## Etapa `concluir`

Só depois do merge do PR da versão (o `--admin` já foi ordenado e executado, ou o Lucas mergeou na UI).

1. `git checkout main`, `git pull --ff-only`, `git fetch -p`; apague a branch local com `git branch -d` (`-D` só se `gh pr list --head <branch> --state merged` mostrar o PR mergeado). `git branch --merged main` não pode sobrar nada.
2. Extraia as notas da seção `[X.Y.Z]` do `CHANGELOG.md` para um arquivo temporário (use o scratchpad).
3. Tag anotada `vX.Y.Z` no commit de merge (mensagem curta com o que mudou), `git push origin vX.Y.Z`, e `gh release create vX.Y.Z --title "vX.Y.Z" --notes-file <notas> --verify-tag`.
4. Rode o build normal para gerar o DOCX final: `build/Especificação - itens 1-15.docx`. `git status` precisa continuar limpo (se `docs/f` mudou, algo ficou fora do PR: avise).
5. Espere cerca de 1 minuto e teste três links curtos (por exemplo as figuras 1, 100 e 185 em `https://plataforma-de-cursos-tcc.github.io/plataforma-cursos-docs/f/N`): o destino precisa ser `blob/vX.Y.Z/...` e responder 200.
6. Reporte: commit de merge, link da Release, caminho e tamanho do DOCX e resultado dos links. Lembre que o PDF em `build/` não é regenerado (o build gera só DOCX) e que o envio no Canvas é com o Lucas.

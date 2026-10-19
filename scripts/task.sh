#!/usr/bin/env bash
# Uso: scripts/task.sh start <issue> <tipo/assunto>   cria a branch ligada à issue, a partir da main
#      scripts/task.sh pr <issue>                      envia a branch e abre o PR com "Closes #<issue>"
set -euo pipefail
case "${1:-}" in
  start)
    git fetch -q origin main
    gh issue develop "${2:?issue}" --name "${3:?tipo/assunto}" --base main --checkout ;;
  pr)
    git push -q -u origin HEAD
    gh pr create --base main --title "$(git log -1 --format=%s)" \
      --body "$(sed "s/^Closes #$/Closes #${2:?issue}/" .github/pull_request_template.md)" ;;
  *) sed -n '2,3p' "$0"; exit 1 ;;
esac

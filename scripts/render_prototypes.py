#!/usr/bin/env python3
"""Renderiza os protótipos HTML em PNG (Chrome headless, 1440x900).

Lê prototipos/html/estados-*.txt (um por autor). Cada captura sai em dois temas:
claro em prototipos/png/<png>.png (é a que entra no DOCX) e escuro em
prototipos/png/escuro/<png>.png, com &tema=claro e &tema=escuro na URL (o tema do sistema
do Chrome não pode decidir a captura clara).
Linhas: "<tela>.html <estado> <png> | <legenda>" ou, para reusar uma captura em
outro fluxo, "@ <png-existente> <UC>-<fluxo> | <legenda>". --check só valida a lista; filtro opcional por
prefixos de PNG (ex.: UC005 UC006) renderizam só as linhas que casam.
"""
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "especificacao/10-especificacoes-de-caso-de-uso/prototipos"
HTML, PNG = BASE / "html", BASE / "png"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def linhas(reusos=False):
    """(origem, tela, estado, png, legenda); com reusos=True, também ("@", png, fluxo, legenda)."""
    for arq in sorted(HTML.glob("estados-*.txt")):
        for n, raw in enumerate(arq.read_text().splitlines(), 1):
            raw = raw.strip()
            if raw and not raw.startswith("#"):
                campos, _, legenda = raw.partition(" | ")
                partes = campos.split()
                assert len(partes) == 3, f"{arq.name}:{n}: esperado 3 campos, veio {partes}"
                if partes[0] != "@" or reusos:
                    yield f"{arq.name}:{n}", *partes, legenda.strip()


def check():
    erros, vistos, reusos = [], set(), []
    for n, tela, estado, png, legenda in linhas(reusos=True):
        if not legenda:
            erros.append(f"{n}: sem legenda")
        if tela == "@":
            reusos.append((n, estado))
            continue
        if not (HTML / tela).is_file():
            erros.append(f"{n}: {tela} não existe")
        if png in vistos:
            erros.append(f"{n}: PNG duplicada {png}")
        vistos.add(png)
    erros += [f"{n}: reuso de {png} inexistente" for n, png in reusos if png not in vistos]
    for e in erros:
        print(e)
    print(f"{len(vistos)} capturas, {len(reusos)} reusos, {len(erros)} erros")
    return not erros


TEMAS = (("&tema=claro", PNG), ("&tema=escuro", PNG / "escuro"))


def render(filtros=("",)):
    for _, tela, estado, png, _ in linhas():
        if not png.startswith(filtros):
            continue
        for extra, pasta in TEMAS:
            pasta.mkdir(parents=True, exist_ok=True)
            url = f"{(HTML / tela).as_uri()}?estado={estado}{extra}"
            subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                            "--window-size=1440,900", "--virtual-time-budget=3000",
                            f"--screenshot={pasta / (png + '.png')}", url],
                           check=True, capture_output=True)
        print(png)


if __name__ == "__main__":
    ok = check()
    if "--check" not in sys.argv:
        filtros = tuple(a for a in sys.argv[1:] if not a.startswith("-"))
        if not ok and not filtros:
            sys.exit(1)  # com filtro, renderiza mesmo com erro em outra lista
        render(filtros or ("",))
    sys.exit(0 if ok else 1)

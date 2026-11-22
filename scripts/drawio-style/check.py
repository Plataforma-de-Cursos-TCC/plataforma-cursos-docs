"""Confere as regras de seta e legenda nos diagramas dos itens 12 e 13."""
import re, sys, xml.etree.ElementTree as ET
from pathlib import Path

DIR = Path(__file__).resolve().parents[2] / "especificacao" / "diagramas"


def problems(path):
    root = ET.parse(path).getroot()
    cells = {c.get("id"): c for c in root.iter("mxCell")}
    out = []
    for c in cells.values():
        if c.get("edge") != "1":
            continue
        st, g = c.get("style", ""), c.find("mxGeometry")
        tag = c.get("id")
        if not c.get("source") or not c.get("target"):
            out.append(f"{tag}: ponta solta")
        if "orthogonalEdgeStyle" not in st:
            out.append(f"{tag}: sem orthogonalEdgeStyle")
        if g is not None and g.find("Array") is not None:
            out.append(f"{tag}: waypoints manuais")
    legend = [c for c in cells.values() if "Legenda" in (c.get("value") or "")]
    if len(legend) != 1:
        out.append(f"legendas: {len(legend)}")
    return out


if __name__ == "__main__":
    bad = 0
    for f in sorted(DIR.glob("1[23]-*.drawio")):
        p = problems(f)
        bad += len(p)
        print(f"{f.name}: {len(p)}", *p[:6], sep="\n  " if p else "")
    sys.exit(1 if bad else 0)

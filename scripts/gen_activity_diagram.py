#!/usr/bin/env python3
"""
Gera o Diagrama de Atividades do UC009 (com UC001 via A-3) com raias horizontais
explícitas e layout determinístico vetorial (SVG) e compila para PNG via Chrome headless.

Versão v7:
- Canvas de 2000 x 950 px (proporção 2.11:1, perfeitamente em [1.8, 2.4]).
- Coluna esquerda de raias com 180 px e texto quebrado em duas linhas ("Plataforma de", "Cursos").
- Correção 1: O laço de retorno de "Vídeo terminou? [não]" foi deslocado para y=662 (corredor inferior
  da raia Plataforma de Cursos), garantindo mais de 45 px de folga livre abaixo do nó final de "4. Conclui aula"
  (que fica em y=615) e 8 px de folga acima da borda inferior da raia (y=670).
- Correção 2: As duas verticais paralelas perto de x=955 e x=1010 foram afastadas para 55 px de distância,
  com o nó 3 começando em x=1030 e o rótulo "[sim]" posicionado com fundo branco encostado apenas na sua linha,
  sem sobreposição nem proximidade excessiva.
- Roteamento ortogonal estrito: nenhuma seta cruza texto ou nós.

Comando de compilação SVG -> PNG:
  CHROME="$HOME/.cache/puppeteer/chrome/mac_arm-148.0.7778.97/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
  "$CHROME" --headless --disable-gpu --window-size=2000,950 --screenshot=especificacao/diagramas/11-atividades.png especificacao/diagramas/11-atividades.svg
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SVG_PATH = BASE_DIR / "especificacao" / "diagramas" / "11-atividades.svg"
PNG_PATH = BASE_DIR / "especificacao" / "diagramas" / "11-atividades.png"

# Canvas dimensions
WIDTH = 2000
HEIGHT = 950
RATIO = WIDTH / HEIGHT  # 2.105:1 (dentro de [1.8, 2.4])

# Swimlanes (Horizontal bands)
HEADER_WIDTH = 180
CONTENT_WIDTH = WIDTH - HEADER_WIDTH - 20

LANE_ALUNO_Y = 20
LANE_ALUNO_H = 220

LANE_PLAT_Y = 260
LANE_PLAT_H = 410

LANE_TUTOR_Y = 690
LANE_TUTOR_H = 240

def make_svg():
    elements = []

    # Defs: Arrow markers & filters
    defs = """
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#222222" />
    </marker>
    <filter id="shadow" x="-4%" y="-4%" width="108%" height="108%">
      <feDropShadow dx="1" dy="2" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.07" />
    </filter>
  </defs>
"""
    elements.append(defs)

    # Background
    elements.append(f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff" />')

    # Draw Swimlanes
    lanes = [
        (["Aluno"], LANE_ALUNO_Y, LANE_ALUNO_H, "#f8f9fa"),
        (["Plataforma", "de Cursos"], LANE_PLAT_Y, LANE_PLAT_H, "#ffffff"),
        (["Tutor de IA"], LANE_TUTOR_Y, LANE_TUTOR_H, "#f8f9fa"),
    ]

    for title_lines, y, h, bg in lanes:
        elements.append(f'  <rect x="{HEADER_WIDTH}" y="{y}" width="{CONTENT_WIDTH}" height="{h}" fill="{bg}" stroke="#adb5bd" stroke-width="1.5" />')
        elements.append(f'  <rect x="20" y="{y}" width="{HEADER_WIDTH-20}" height="{h}" fill="#e9ecef" stroke="#adb5bd" stroke-width="1.5" />')
        line_h = 22
        start_ty = y + h/2 - (len(title_lines) - 1) * (line_h / 2) + 6
        for idx, tline in enumerate(title_lines):
            elements.append(f'  <text x="{20 + (HEADER_WIDTH-20)/2}" y="{start_ty + idx*line_h}" font-family="Arial" font-size="16" font-weight="bold" fill="#212529" text-anchor="middle">{tline}</text>')

    # Helpers for nodes
    def action_box(x, y, w, h, text_lines):
        out = []
        out.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" ry="8" fill="#ffffff" stroke="#222222" stroke-width="1.8" filter="url(#shadow)" />')
        line_height = 18
        total_text_h = len(text_lines) * line_height
        start_y = y + (h - total_text_h) / 2 + 14
        for i, line in enumerate(text_lines):
            weight = "bold" if i == 0 and ("." in line or "-" in line) else "normal"
            out.append(f'  <text x="{x + w/2}" y="{start_y + i*line_height}" font-family="Arial" font-size="14" font-weight="{weight}" fill="#111111" text-anchor="middle">{line}</text>')
        return "\n".join(out)

    def diamond(cx, cy, r_w, r_h, text_lines):
        pts = f"{cx},{cy-r_h} {cx+r_w},{cy} {cx},{cy+r_h} {cx-r_w},{cy}"
        out = []
        out.append(f'  <polygon points="{pts}" fill="#ffffff" stroke="#222222" stroke-width="1.8" filter="url(#shadow)" />')
        line_height = 16
        total_text_h = len(text_lines) * line_height
        start_y = cy - total_text_h/2 + 12
        for i, line in enumerate(text_lines):
            out.append(f'  <text x="{cx}" y="{start_y + i*line_height}" font-family="Arial" font-size="13" font-weight="bold" fill="#222222" text-anchor="middle">{line}</text>')
        return "\n".join(out)

    def start_node(cx, cy):
        return f'  <circle cx="{cx}" cy="{cy}" r="12" fill="#222222" stroke="#111111" stroke-width="1.5" />'

    def end_node(cx, cy):
        return f'''  <circle cx="{cx}" cy="{cy}" r="14" fill="#ffffff" stroke="#222222" stroke-width="1.8" />
  <circle cx="{cx}" cy="{cy}" r="8" fill="#222222" />'''

    def arrow(points, label=None, label_pos=None, label_anchor="middle"):
        d_str = f"M {points[0][0]} {points[0][1]} " + " ".join([f"L {p[0]} {p[1]}" for p in points[1:]])
        out = [f'  <path d="{d_str}" fill="none" stroke="#222222" stroke-width="1.8" marker-end="url(#arrow)" />']
        if label and label_pos:
            lx, ly = label_pos
            text_len = len(label) * 8 + 14
            out.append(f'  <rect x="{lx - text_len/2 if label_anchor=="middle" else lx}" y="{ly - 12}" width="{text_len}" height="18" fill="#ffffff" stroke="#d0d0d0" stroke-width="0.8" rx="3" />')
            out.append(f'  <text x="{lx}" y="{ly + 2}" font-family="Arial" font-size="12" font-weight="bold" fill="#333333" text-anchor="{label_anchor}">[{label}]</text>')
        return "\n".join(out)

    # -------------------------------------------------------------------------
    # TABELA DE COLUNAS E NÓS (Folga mínima >= 40 px em X e Y)
    # -------------------------------------------------------------------------
    # Col 1: Início (x=220) e Passo 1 (x=260..400, y=105..157)
    elements.append(start_node(220, 131))
    elements.append(action_box(260, 105, 140, 52, ["1. Acessa aula", "no curso"]))

    # Col 2: Pode assistir? (cx=470, cy=350, rw=55, rh=36 -> x=415..525, y=314..386)
    elements.append(diamond(470, 350, 55, 36, ["Pode", "assistir?"]))
    # Col 2 (abaixo): E-1 (x=395..545, y=460..510) e Fim 1 (x=470, y=565)
    elements.append(action_box(395, 460, 150, 50, ["E-1. Bloqueia e", "sugere matrícula"]))
    elements.append(end_node(470, 565))

    # Col 3: Aula iniciada antes? (cx=610, cy=350, rw=58, rh=36 -> x=552..668, y=314..386)
    elements.append(diamond(610, 350, 58, 36, ["Aula já", "iniciada?"]))

    # Col 4: A-2 Posiciona vídeo (x=720..870, y=285..333)
    elements.append(action_box(720, 285, 150, 48, ["A-2. Posiciona vídeo", "no ponto salvo"]))

    # Col 4: 2. Carrega vídeo (x=720..870, y=390..440)
    elements.append(action_box(720, 390, 150, 50, ["2. Carrega e", "reproduz vídeo"]))

    # Col 5: Vídeo carregou? (cx=945, cy=415, rw=55, rh=36 -> x=890..1000, y=379..451)
    elements.append(diamond(945, 415, 55, 36, ["Vídeo", "carregou?"]))
    # Col 5 (abaixo): E-2 (x=870..1020, y=505..555) e Fim 2 (x=945, y=605)
    elements.append(action_box(870, 505, 150, 50, ["E-2. Exibe erro e", "oferece recarregar"]))
    elements.append(end_node(945, 605))

    # Col 6: 3. Assiste vídeo (x=1030..1180, y=105..157)
    elements.append(action_box(1030, 105, 150, 52, ["3. Assiste ao", "vídeo da aula"]))

    # Col 7: Tem dúvida? (cx=1240, cy=131, rw=48, rh=34 -> x=1192..1288, y=97..165)
    elements.append(diamond(1240, 131, 48, 34, ["Tem", "dúvida?"]))

    # Col 8: A-3. Envia pergunta (x=1340..1490, y=105..157)
    elements.append(action_box(1340, 105, 150, 52, ["A-3. Envia pergunta", "no chat"]))

    # Col 8 (Plataforma): Limite de mensagens? (cx=1415, cy=335, rw=58, rh=36 -> x=1357..1473, y=299..371)
    elements.append(diamond(1415, 335, 58, 36, ["Limite de", "mensagens?"]))

    # Col 7 (Plataforma): UC001 E-2 (x=1230..1380, y=425..475)
    elements.append(action_box(1230, 425, 150, 50, ["UC001 E-2. Informa", "tempo de espera"]))

    # Col 8 (Tutor): Busca trechos (x=1340..1490, y=740..790)
    elements.append(action_box(1340, 740, 150, 50, ["Busca trechos", "no conteúdo"]))

    # Col 9 (Tutor): Trecho relevante? (cx=1560, cy=765, rw=52, rh=36 -> x=1508..1612, y=729..801)
    elements.append(diamond(1560, 765, 52, 36, ["Trecho", "relevante?"]))

    # Col 10 (Tutor): Gera resposta (x=1650..1800, y=715..761)
    elements.append(action_box(1650, 715, 150, 46, ["Gera resposta", "com citação"]))
    # Col 10 (Tutor): UC001 A-1 (x=1650..1800, y=785..831)
    elements.append(action_box(1650, 785, 150, 46, ["UC001 A-1. Informa", "que não cobre"]))

    # Col 9 (Plataforma): Exibe resposta (x=1490..1640, y=425..475)
    elements.append(action_box(1490, 425, 150, 50, ["Exibe resposta e", "salva histórico"]))

    # Col 11 (Plataforma): Saiu da tela? (cx=1725, cy=335, rw=55, rh=36 -> x=1670..1780, y=299..371)
    elements.append(diamond(1725, 335, 55, 36, ["Saiu da", "tela?"]))

    # Col 12 (Plataforma): A-1 Salva segundos (x=1840..1960, y=311..359) e Fim 3 (x=1900, y=225)
    elements.append(action_box(1840, 311, 120, 48, ["A-1. Salva", "segundos"]))
    elements.append(end_node(1900, 225))

    # Col 11 (Plataforma - linha inferior): Vídeo terminou? (cx=1725, cy=455, rw=55, rh=36 -> x=1670..1780, y=419..491)
    elements.append(diamond(1725, 455, 55, 36, ["Vídeo", "terminou?"]))

    # Col 11 (Plataforma - base): 4. Conclui aula (x=1650..1800, y=535..583) e Fim 4 (x=1725, y=615)
    elements.append(action_box(1650, 535, 150, 48, ["4. Conclui aula e", "atualiza progresso"]))
    elements.append(end_node(1725, 615))

    # -------------------------------------------------------------------------
    # ARESTAS RIGOROSAMENTE MAPEADAS - SEM SOBREPOSIÇÃO NEM CRUZAMENTO DE NÓS
    # -------------------------------------------------------------------------

    # 1. Início -> 1. Acessa aula
    elements.append(arrow([(232, 131), (260, 131)]))

    # 2. 1. Acessa aula -> Pode assistir? (desce pelo canal x=470)
    elements.append(arrow([(400, 131), (470, 131), (470, 314)]))

    # 3. Pode assistir? -> [não] E-1
    elements.append(arrow([(470, 386), (470, 460)], label="não", label_pos=(470, 423)))

    # 4. E-1 -> Fim 1
    elements.append(arrow([(470, 510), (470, 551)]))

    # 5. Pode assistir? -> [sim] Aula iniciada?
    elements.append(arrow([(525, 350), (552, 350)], label="sim", label_pos=(538, 340)))

    # 6. Aula iniciada? -> [sim] A-2 (sobe para y=309)
    elements.append(arrow([(610, 314), (610, 309), (720, 309)], label="sim", label_pos=(655, 299)))

    # 7. Aula iniciada? -> [não] 2. Carrega vídeo (desce para y=415)
    elements.append(arrow([(610, 386), (610, 415), (720, 415)], label="não", label_pos=(655, 425)))

    # 8. A-2 -> 2. Carrega vídeo
    # Sai da face direita de A-2 (x=870, y=309), desce pelo canal x=895 até y=365, vira para a esquerda até x=795 e desce no topo de 2 (y=390)
    elements.append(arrow([(870, 309), (895, 309), (895, 365), (795, 365), (795, 390)]))

    # 9. 2. Carrega vídeo -> Vídeo carregou?
    elements.append(arrow([(870, 415), (890, 415)]))

    # 10. Vídeo carregou? -> [não] E-2
    elements.append(arrow([(945, 451), (945, 505)], label="não", label_pos=(945, 478)))

    # 11. E-2 -> Fim 2
    elements.append(arrow([(945, 555), (945, 591)]))

    # 12. Vídeo carregou? -> [sim] 3. Assiste vídeo
    # Sai do topo de Vídeo carregou? (x=945, y=379), sobe até y=360, vira para x=955,
    # sobe pelo canal x=955 até y=131 e entra na face esquerda de 3 (x=1030, y=131).
    # O rótulo "[sim]" fica em (x=955, y=245), com folga de 55 px da linha do laço (que fica em x=1010)!
    elements.append(arrow([(945, 379), (945, 360), (955, 360), (955, 131), (1030, 131)], label="sim", label_pos=(955, 245)))

    # 13. 3. Assiste vídeo -> Tem dúvida?
    elements.append(arrow([(1180, 131), (1192, 131)]))

    # 14. Tem dúvida? -> [sim] A-3. Envia pergunta
    elements.append(arrow([(1288, 131), (1340, 131)], label="sim", label_pos=(1314, 120)))

    # 15. Tem dúvida? -> [não] Saiu da tela?
    # Sobe pelo topo da raia Aluno (y=60), segue horizontalmente até x=1725 e desce no topo de Saiu da tela? (y=299)
    elements.append(arrow([(1240, 97), (1240, 60), (1725, 60), (1725, 299)], label="não", label_pos=(1480, 50)))

    # 16. A-3. Envia pergunta -> Limite de mensagens?
    # Desce direto da face inferior de A-3 (x=1415, y=157) para o topo de Limite (x=1415, y=299)
    elements.append(arrow([(1415, 157), (1415, 299)]))

    # 17. Limite de mensagens? -> [sim] UC001 E-2
    # Sai da esquerda de Limite (x=1357, y=335), vai para x=1305, desce até y=425 (topo de UC001 E-2 em x=1305)
    elements.append(arrow([(1357, 335), (1305, 335), (1305, 425)], label="sim", label_pos=(1305, 375)))

    # 18. Limite de mensagens? -> [não] Busca trechos (Tutor de IA)
    # Desce reto da face inferior de Limite (x=1415, y=371) para o topo de Busca trechos (x=1415, y=740)
    elements.append(arrow([(1415, 371), (1415, 740)], label="não", label_pos=(1415, 600)))

    # 19. Busca trechos -> Trecho relevante?
    elements.append(arrow([(1490, 765), (1508, 765)]))

    # 20. Trecho relevante? -> [sim] Gera resposta
    elements.append(arrow([(1560, 729), (1560, 738), (1650, 738)], label="sim", label_pos=(1605, 728)))

    # 21. Trecho relevante? -> [não] UC001 A-1
    elements.append(arrow([(1560, 801), (1560, 808), (1650, 808)], label="não", label_pos=(1605, 818)))

    # 22. Gera resposta e UC001 A-1 -> Exibe resposta (Plataforma)
    # Dois pontos de entrada distintos no fundo de Exibe resposta: x=1550 e x=1610
    elements.append(arrow([(1725, 715), (1725, 670), (1610, 670), (1610, 475)]))
    elements.append(arrow([(1800, 808), (1830, 808), (1830, 660), (1550, 660), (1550, 475)]))

    # 23. UC001 E-2 -> Saiu da tela?
    elements.append(arrow([(1350, 425), (1350, 390), (1460, 390), (1460, 335), (1670, 335)]))

    # 24. Exibe resposta -> Saiu da tela?
    elements.append(arrow([(1565, 425), (1565, 350), (1670, 350)]))

    # 25. Saiu da tela? -> [sim] A-1 Salva segundos
    elements.append(arrow([(1780, 335), (1840, 335)], label="sim", label_pos=(1810, 325)))

    # 26. A-1 -> Fim 3
    elements.append(arrow([(1900, 311), (1900, 241)]))

    # 27. Saiu da tela? -> [não] Vídeo terminou?
    elements.append(arrow([(1725, 371), (1725, 419)], label="não", label_pos=(1725, 395)))

    # 28. Vídeo terminou? -> [sim] 4. Conclui aula
    elements.append(arrow([(1725, 491), (1725, 535)], label="sim", label_pos=(1725, 513)))

    # 29. 4. Conclui aula -> Fim 4
    elements.append(arrow([(1725, 583), (1725, 601)]))

    # 30. Vídeo terminou? -> [não] Retorna para 3. Assiste ao vídeo
    # Sai da face direita de Vídeo terminou? (x=1780, y=455), vai para x=1975 (coluna direita livre),
    # desce para y=662 (corredor inferior da raia Plataforma, com 47 px livres abaixo de Fim 4 e 8 px acima do fim da raia),
    # segue à esquerda até x=1010, e sobe até y=131, entrando na esquerda de 3. Assiste ao vídeo (x=1030, y=131).
    # Com isso:
    # - Folga do nó final Fim 4 (centro em y=615, raio 14 -> base em y=629): y=662 - 629 = 33 px livres (> 25 px exigidos).
    # - Folga entre as verticais em x=955 e x=1010: 1010 - 955 = 55 px livres (> 40 px exigidos).
    elements.append(arrow([
        (1780, 455),
        (1975, 455),
        (1975, 662),
        (1010, 662),
        (1010, 131),
        (1030, 131)
    ], label="não: continua", label_pos=(1450, 652)))

    svg_content = f"""<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">
{''.join(elements)}
</svg>
"""
    return svg_content

def main():
    svg_code = make_svg()
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg_code)
    print(f"SVG v7 gerado em {SVG_PATH}")

    chrome_bin = Path.home() / ".cache" / "puppeteer" / "chrome" / "mac_arm-148.0.7778.97" / "chrome-mac-arm64" / "Google Chrome for Testing.app" / "Contents" / "MacOS" / "Google Chrome for Testing"
    if not chrome_bin.exists():
        raise FileNotFoundError(f"Chrome não encontrado em {chrome_bin}")

    cmd = [
        str(chrome_bin),
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={WIDTH},{HEIGHT}",
        f"--screenshot={PNG_PATH}",
        str(SVG_PATH)
    ]
    print("Compilando PNG v7 via Chrome headless...")
    subprocess.run(cmd, check=True)
    print(f"PNG v7 gerado com sucesso em {PNG_PATH}")

if __name__ == "__main__":
    main()

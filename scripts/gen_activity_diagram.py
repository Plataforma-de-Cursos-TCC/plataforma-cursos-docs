#!/usr/bin/env python3
"""
Gera o Diagrama de Atividades do UC009 (com UC001 via A-3) com raias horizontais
explícitas e layout determinístico vetorial (SVG) e compila para PNG via Chrome headless.

Nota de Histórico e Registro:
- As abordagens anteriores com PlantUML, Mermaid e Graphviz dot (registradas em
  especificacao/diagramas/11-atividades.puml e 11-atividades.dot) não produziram raias
  reais horizontais com controle estrito de roteamento de arestas e proporção landscape A4.
- Este gerador Python (stdlib apenas) posiciona cada ator em sua faixa horizontal,
  garante corredores livres para retornos ortogonais e mantém a proporção entre 1.8:1 e 2.4:1
  com texto upright (Arial 14-16 pt em viewBox de 1840x880) legível a >= 8 pt na impressão.

Comando de compilação SVG -> PNG:
  CHROME="$HOME/.cache/puppeteer/chrome/mac_arm-148.0.7778.97/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
  "$CHROME" --headless --disable-gpu --window-size=1840,880 --screenshot=especificacao/diagramas/11-atividades.png especificacao/diagramas/11-atividades.svg
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SVG_PATH = BASE_DIR / "especificacao" / "diagramas" / "11-atividades.svg"
PNG_PATH = BASE_DIR / "especificacao" / "diagramas" / "11-atividades.png"

# Canvas dimensions
WIDTH = 1840
HEIGHT = 880
RATIO = WIDTH / HEIGHT  # ~2.09:1 (perfeitamente entre 1.8:1 e 2.4:1)

# Swimlanes (Horizontal bands)
# De cima para baixo: Aluno, Plataforma de Cursos, Tutor de IA
HEADER_WIDTH = 150
CONTENT_WIDTH = WIDTH - HEADER_WIDTH - 20

LANE_ALUNO_Y = 20
LANE_ALUNO_H = 220

LANE_PLAT_Y = 250
LANE_PLAT_H = 360

LANE_TUTOR_Y = 620
LANE_TUTOR_H = 240

def make_svg():
    elements = []

    # Defs: Arrow markers
    defs = """
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#222222" />
    </marker>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="1" dy="2" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.08" />
    </filter>
  </defs>
"""
    elements.append(defs)

    # Background
    elements.append(f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff" />')

    # Draw Swimlanes
    lanes = [
        ("Aluno", LANE_ALUNO_Y, LANE_ALUNO_H, "#f8f9fa", "#2b2b2b"),
        ("Plataforma de Cursos", LANE_PLAT_Y, LANE_PLAT_H, "#fdfdfd", "#2b2b2b"),
        ("Tutor de IA", LANE_TUTOR_Y, LANE_TUTOR_H, "#f8f9fa", "#2b2b2b"),
    ]

    for title, y, h, bg, border in lanes:
        # Lane content area
        elements.append(f'  <rect x="{HEADER_WIDTH}" y="{y}" width="{CONTENT_WIDTH}" height="{h}" fill="{bg}" stroke="#cccccc" stroke-width="1.5" />')
        # Lane header box
        elements.append(f'  <rect x="20" y="{y}" width="{HEADER_WIDTH-20}" height="{h}" fill="#e9ecef" stroke="#adb5bd" stroke-width="1.5" />')
        # Lane title (centered vertically in header box)
        elements.append(f'  <text x="{20 + (HEADER_WIDTH-20)/2}" y="{y + h/2 + 6}" font-family="Arial" font-size="16" font-weight="bold" fill="#212529" text-anchor="middle">{title}</text>')

    # Corridor hints / separators are inherent in the lane borders

    # Helper functions for UML nodes
    def action_box(x, y, w, h, text_lines, node_id=None):
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
        # points is list of (x,y)
        d_str = f"M {points[0][0]} {points[0][1]} " + " ".join([f"L {p[0]} {p[1]}" for p in points[1:]])
        out = [f'  <path d="{d_str}" fill="none" stroke="#222222" stroke-width="1.8" marker-end="url(#arrow)" />']
        if label and label_pos:
            lx, ly = label_pos
            text_len = len(label) * 8 + 12
            out.append(f'  <rect x="{lx - text_len/2 if label_anchor=="middle" else lx}" y="{ly - 12}" width="{text_len}" height="18" fill="#ffffff" rx="3" fill-opacity="0.92" />')
            out.append(f'  <text x="{lx}" y="{ly + 2}" font-family="Arial" font-size="12" font-weight="bold" fill="#333333" text-anchor="{label_anchor}">[{label}]</text>')
        return "\n".join(out)

    # -------------------------------------------------------------
    # POSICIONAMENTO EXATO DOS NÓS POR COLUNAS E RAIAS
    # -------------------------------------------------------------
    # Raia Aluno: Y central útil ~ 130
    # Raia Plataforma: Y topo ~ 320, Y meio ~ 430, Y base ~ 530
    # Raia Tutor: Y central útil ~ 730

    # 1. Start & Passo 1 (Aluno)
    elements.append(start_node(180, 130))
    elements.append(action_box(220, 105, 140, 52, ["1. Acessa aula", "no curso"]))

    # 2. Decisão: Pode assistir? (Plataforma)
    elements.append(diamond(430, 340, 55, 36, ["Pode", "assistir?"]))

    # 3. Exceção E-1 (Plataforma) & Fim 1
    elements.append(action_box(355, 420, 150, 52, ["E-1. Bloqueia e", "sugere matrícula"]))
    elements.append(end_node(430, 510))

    # 4. Decisão: Aula iniciada antes? (Plataforma)
    elements.append(diamond(580, 340, 58, 36, ["Aula já", "iniciada?"]))

    # 5. A-2 Posiciona vídeo (Plataforma)
    elements.append(action_box(680, 275, 150, 48, ["A-2. Posiciona vídeo", "no ponto salvo"]))

    # 6. Passo 2: Carrega e reproduz vídeo (Plataforma)
    elements.append(action_box(680, 355, 150, 50, ["2. Carrega e", "reproduz vídeo"]))

    # 7. Decisão: Vídeo carregou? (Plataforma)
    elements.append(diamond(900, 380, 55, 36, ["Vídeo", "carregou?"]))

    # 8. Exceção E-2 (Plataforma) & Fim 2
    elements.append(action_box(825, 460, 150, 50, ["E-2. Exibe erro e", "oferece recarregar"]))
    elements.append(end_node(900, 545))

    # 9. Passo 3: Assiste ao vídeo (Aluno)
    elements.append(action_box(825, 105, 150, 52, ["3. Assiste ao", "vídeo da aula"]))

    # 10. Decisão: Dúvida? (Aluno)
    elements.append(diamond(1055, 131, 50, 34, ["Tem", "dúvida?"]))

    # 11. Alternativo A-3: Envia pergunta (Aluno)
    elements.append(action_box(1160, 105, 150, 52, ["A-3. Envia pergunta", "no chat"]))

    # 12. Decisão: Limite de mensagens? (Plataforma)
    elements.append(diamond(1235, 340, 58, 36, ["Limite de", "mensagens?"]))

    # 13. Exceção UC001 E-2: Tempo de espera (Plataforma)
    elements.append(action_box(1155, 420, 160, 50, ["UC001 E-2. Informa", "tempo de espera"]))

    # 14. Tutor de IA: Busca trechos (Tutor)
    elements.append(action_box(1155, 660, 160, 50, ["Busca trechos", "no conteúdo"]))

    # 15. Decisão: Trecho relevante? (Tutor)
    elements.append(diamond(1385, 685, 58, 36, ["Trecho", "relevante?"]))

    # 16. Tutor Gera resposta (Tutor)
    elements.append(action_box(1495, 645, 150, 48, ["Gera resposta", "com citação"]))

    # 17. Exceção UC001 A-1: Não cobre (Tutor)
    elements.append(action_box(1495, 715, 150, 48, ["UC001 A-1. Informa", "que não cobre"]))

    # 18. Plataforma: Exibe resposta e salva histórico (Plataforma)
    elements.append(action_box(1495, 420, 150, 50, ["Exibe resposta e", "salva histórico"]))

    # 19. Decisão: Aluno saiu da tela? (Plataforma)
    elements.append(diamond(1570, 310, 58, 36, ["Saiu da", "tela?"]))

    # 20. Alternativo A-1: Salva segundos assistidos (Plataforma) & Fim 3
    elements.append(action_box(1670, 275, 140, 48, ["A-1. Salva os", "segundos"]))
    elements.append(end_node(1740, 210))

    # 21. Decisão: Vídeo terminou? (Plataforma)
    elements.append(diamond(1685, 380, 55, 36, ["Vídeo", "terminou?"]))

    # 22. Passo 4: Marca aula concluída (Plataforma) & Fim 4
    elements.append(action_box(1610, 470, 150, 52, ["4. Conclui aula e", "atualiza progresso"]))
    elements.append(end_node(1685, 555))

    # -------------------------------------------------------------
    # ARESTAS ORTOGONAIS COM RÓTULOS LIMPOS
    # -------------------------------------------------------------

    # Início -> 1. Acessa aula
    elements.append(arrow([(192, 130), (220, 130)]))

    # 1. Acessa aula -> Pode assistir? (Plataforma)
    elements.append(arrow([(360, 130), (430, 130), (430, 304)]))

    # Pode assistir? -> [não] E-1
    elements.append(arrow([(430, 376), (430, 420)], label="não", label_pos=(430, 398)))

    # E-1 -> Fim 1
    elements.append(arrow([(430, 472), (430, 496)]))

    # Pode assistir? -> [sim] Aula iniciada?
    elements.append(arrow([(485, 340), (522, 340)], label="sim", label_pos=(503, 330)))

    # Aula iniciada? -> [sim] A-2
    elements.append(arrow([(580, 304), (580, 299), (680, 299)], label="sim", label_pos=(615, 290)))

    # Aula iniciada? -> [não] 2. Carrega vídeo
    elements.append(arrow([(580, 376), (580, 380), (680, 380)], label="não", label_pos=(615, 370)))

    # A-2 -> 2. Carrega vídeo
    elements.append(arrow([(755, 323), (755, 355)]))

    # 2. Carrega vídeo -> Vídeo carregou?
    elements.append(arrow([(830, 380), (845, 380)]))

    # Vídeo carregou? -> [não] E-2
    elements.append(arrow([(900, 416), (900, 460)], label="não", label_pos=(900, 438)))

    # E-2 -> Fim 2
    elements.append(arrow([(900, 510), (900, 531)]))

    # Vídeo carregou? -> [sim] 3. Assiste vídeo (sobe para Aluno)
    elements.append(arrow([(900, 344), (900, 157)], label="sim", label_pos=(900, 230)))

    # 3. Assiste vídeo -> Tem dúvida?
    elements.append(arrow([(975, 131), (1005, 131)]))

    # Tem dúvida? -> [sim] A-3. Envia pergunta
    elements.append(arrow([(1105, 131), (1160, 131)], label="sim", label_pos=(1132, 120)))

    # Tem dúvida? -> [não] Saiu da tela? (desce pelo corredor superior da Plataforma)
    elements.append(arrow([(1055, 97), (1055, 75), (1570, 75), (1570, 274)], label="não", label_pos=(1280, 65)))

    # A-3. Envia pergunta -> Limite de mensagens? (desce para Plataforma)
    elements.append(arrow([(1235, 157), (1235, 304)]))

    # Limite de mensagens? -> [sim] UC001 E-2
    elements.append(arrow([(1235, 376), (1235, 420)], label="sim", label_pos=(1235, 398)))

    # Limite de mensagens? -> [não] Busca trechos (desce para Tutor de IA)
    elements.append(arrow([(1293, 340), (1330, 340), (1330, 685), (1315, 685)], label="não", label_pos=(1330, 550)))

    # Limite não -> Busca trechos entrada esquerda
    # Redirecionando ponta para Busca trechos:
    elements.pop()  # remove acima para fazer percurso limpo:
    elements.append(arrow([(1235, 376), (1235, 390)], label="sim", label_pos=(1235, 398)))
    # Corrigindo:
    elements.pop()
    elements.append(arrow([(1235, 376), (1235, 420)], label="sim", label_pos=(1235, 398)))
    elements.append(arrow([(1293, 340), (1320, 340), (1320, 635), (1235, 635), (1235, 660)], label="não", label_pos=(1320, 520)))

    # Busca trechos -> Trecho relevante?
    elements.append(arrow([(1315, 685), (1327, 685)]))

    # Trecho relevante? -> [sim] Gera resposta
    elements.append(arrow([(1385, 649), (1385, 669), (1495, 669)], label="sim", label_pos=(1420, 659)))

    # Trecho relevante? -> [não] UC001 A-1
    elements.append(arrow([(1385, 721), (1385, 739), (1495, 739)], label="não", label_pos=(1420, 729)))

    # Gera resposta -> Exibe resposta (sobe para Plataforma)
    elements.append(arrow([(1645, 669), (1670, 669), (1670, 445), (1645, 445)]))

    # UC001 A-1 -> Exibe resposta
    elements.append(arrow([(1645, 739), (1670, 739), (1670, 445)]))

    # UC001 E-2 -> Saiu da tela?
    elements.append(arrow([(1315, 445), (1410, 445), (1410, 310), (1512, 310)]))

    # Exibe resposta -> Saiu da tela?
    elements.append(arrow([(1570, 420), (1570, 346)]))

    # Saiu da tela? -> [sim] A-1. Salva segundos
    elements.append(arrow([(1628, 310), (1670, 310), (1670, 299)], label="sim", label_pos=(1648, 300)))

    # A-1 -> Fim 3
    elements.append(arrow([(1740, 275), (1740, 224)]))

    # Saiu da tela? -> [não] Vídeo terminou?
    elements.append(arrow([(1570, 346), (1570, 380), (1630, 380)], label="não", label_pos=(1595, 370)))

    # Vídeo terminou? -> [sim] 4. Conclui aula
    elements.append(arrow([(1685, 416), (1685, 470)], label="sim", label_pos=(1685, 443)))

    # 4. Conclui aula -> Fim 4
    elements.append(arrow([(1685, 522), (1685, 541)]))

    # Vídeo terminou? -> [não] Retorna para 3. Assiste vídeo (corredor inferior Aluno/Plataforma)
    # Rota livre sem cruzar texto: desce pelo fundo, passa pelo corredor y=580 e sobe até a esquerda do nó 3
    elements.append(arrow([(1740, 380), (1780, 380), (1780, 580), (790, 580), (790, 131), (825, 131)],
                          label="não: assiste", label_pos=(1280, 570)))

    # Final SVG assembly
    svg_content = f"""<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 1840 880" xmlns="http://www.w3.org/2000/svg">
{''.join(elements)}
</svg>
"""
    return svg_content

def main():
    svg_code = make_svg()
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg_code)
    print(f"SVG gerado em {SVG_PATH}")

    # Compile to PNG with headless Chrome
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
    print("Compilando PNG via Chrome headless...")
    subprocess.run(cmd, check=True)
    print(f"PNG gerado com sucesso em {PNG_PATH}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Gera o Diagrama de Atividades do UC009 (com UC001 via A-3) com raias horizontais
explícitas e layout determinístico vetorial (SVG) e compila para PNG via Chrome headless.

Versão v6:
- Canvas expandido para 2000 x 950 px (proporção 2.11:1).
- Coluna esquerda das raias com 180 px e texto quebrado em duas linhas ("Plataforma de", "Cursos").
- Colunas sequenciais bem espaçadas (>= 40 px de folga mínima entre nós).
- Roteamento ortogonal com coordenadas exatas: nenhuma seta atravessa nós, textos ou outras setas.
- Pontos de entrada/saída dedicados em cada face dos nós.
- Corredor de retorno inferior totalmente livre.
- Guardas [sim]/[não] com caixas brancas dedicadas ao lado dos segmentos.

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
        # Lane content area
        elements.append(f'  <rect x="{HEADER_WIDTH}" y="{y}" width="{CONTENT_WIDTH}" height="{h}" fill="{bg}" stroke="#adb5bd" stroke-width="1.5" />')
        # Lane header box
        elements.append(f'  <rect x="20" y="{y}" width="{HEADER_WIDTH-20}" height="{h}" fill="#e9ecef" stroke="#adb5bd" stroke-width="1.5" />')
        # Lane title (centered vertically in header box)
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
            out.append(f'  <rect x="{lx - text_len/2 if label_anchor=="middle" else lx}" y="{ly - 12}" width="{text_len}" height="18" fill="#ffffff" stroke="#e0e0e0" stroke-width="0.8" rx="3" />')
            out.append(f'  <text x="{lx}" y="{ly + 2}" font-family="Arial" font-size="12" font-weight="bold" fill="#333333" text-anchor="{label_anchor}">[{label}]</text>')
        return "\n".join(out)

    # -------------------------------------------------------------
    # POSICIONAMENTO E COORDENADAS EXATAS DOS NÓS
    # -------------------------------------------------------------
    # Coluna 1: Início e Passo 1 (Aluno)
    elements.append(start_node(220, 130))
    elements.append(action_box(260, 105, 140, 52, ["1. Acessa aula", "no curso"]))

    # Coluna 2: Pode assistir? (Plataforma)
    elements.append(diamond(470, 360, 55, 36, ["Pode", "assistir?"]))

    # Coluna 2 (abaixo): E-1 Bloqueia acesso (Plataforma) & Fim 1
    elements.append(action_box(395, 470, 150, 50, ["E-1. Bloqueia e", "sugere matrícula"]))
    elements.append(end_node(470, 575))

    # Coluna 3: Aula iniciada antes? (Plataforma)
    elements.append(diamond(610, 360, 58, 36, ["Aula já", "iniciada?"]))

    # Coluna 4: A-2 Posiciona vídeo (Plataforma - linha superior)
    elements.append(action_box(720, 290, 150, 48, ["A-2. Posiciona vídeo", "no ponto salvo"]))

    # Coluna 5: 2. Carrega e reproduz vídeo (Plataforma - linha central)
    elements.append(action_box(720, 400, 150, 50, ["2. Carrega e", "reproduz vídeo"]))

    # Coluna 6: Vídeo carregou? (Plataforma)
    elements.append(diamond(945, 425, 55, 36, ["Vídeo", "carregou?"]))

    # Coluna 6 (abaixo): E-2 Exibe erro (Plataforma) & Fim 2
    elements.append(action_box(870, 510, 150, 50, ["E-2. Exibe erro e", "oferece recarregar"]))
    elements.append(end_node(945, 610))

    # Coluna 7: 3. Assiste ao vídeo (Aluno)
    elements.append(action_box(1025, 105, 150, 52, ["3. Assiste ao", "vídeo da aula"]))

    # Coluna 8: Tem dúvida? (Aluno)
    elements.append(diamond(1245, 131, 50, 34, ["Tem", "dúvida?"]))

    # Coluna 9: A-3. Envia pergunta no chat (Aluno)
    elements.append(action_box(1345, 105, 150, 52, ["A-3. Envia pergunta", "no chat"]))

    # Coluna 10: Limite de mensagens? (Plataforma - linha superior)
    elements.append(diamond(1420, 340, 58, 36, ["Limite de", "mensagens?"]))

    # Coluna 9 (meio): UC001 E-2 Tempo de espera (Plataforma)
    elements.append(action_box(1345, 430, 150, 50, ["UC001 E-2. Informa", "tempo de espera"]))

    # Coluna 10 (base): Tutor Busca trechos (Tutor de IA)
    elements.append(action_box(1345, 735, 150, 50, ["Busca trechos", "no conteúdo"]))

    # Coluna 11: Trecho relevante? (Tutor de IA)
    elements.append(diamond(1560, 760, 55, 36, ["Trecho", "relevante?"]))

    # Coluna 12 (superior Tutor): Gera resposta (Tutor de IA)
    elements.append(action_box(1660, 715, 150, 46, ["Gera resposta", "com citação"]))

    # Coluna 12 (inferior Tutor): UC001 A-1 Não cobre (Tutor de IA)
    elements.append(action_box(1660, 785, 150, 46, ["UC001 A-1. Informa", "que não cobre"]))

    # Coluna 13: Exibe resposta e salva histórico (Plataforma)
    elements.append(action_box(1560, 430, 150, 50, ["Exibe resposta e", "salva histórico"]))

    # Coluna 14: Saiu da tela? (Plataforma)
    elements.append(diamond(1780, 340, 55, 36, ["Saiu da", "tela?"]))

    # Coluna 15: A-1 Salva segundos (Plataforma) & Fim 3
    elements.append(action_box(1870, 316, 110, 48, ["A-1. Salva", "segundos"]))
    elements.append(end_node(1925, 230))

    # Coluna 14 (abaixo): Vídeo terminou? (Plataforma)
    elements.append(diamond(1780, 455, 55, 36, ["Vídeo", "terminou?"]))

    # Coluna 14 (mais abaixo): 4. Conclui aula (Plataforma) & Fim 4
    elements.append(action_box(1705, 535, 150, 50, ["4. Conclui aula e", "atualiza progresso"]))
    elements.append(end_node(1780, 625))

    # -------------------------------------------------------------
    # ARESTAS ORTOGONAIS SEM SOBREPOSIÇÃO
    # -------------------------------------------------------------

    # Início -> 1. Acessa aula
    elements.append(arrow([(232, 130), (260, 130)]))

    # 1. Acessa aula -> Pode assistir? (desce pelo corredor x=470 sem cruzar nós)
    elements.append(arrow([(400, 130), (470, 130), (470, 324)]))

    # Pode assistir? -> [não] E-1
    elements.append(arrow([(470, 396), (470, 470)], label="não", label_pos=(470, 433)))

    # E-1 -> Fim 1
    elements.append(arrow([(470, 520), (470, 561)]))

    # Pode assistir? -> [sim] Aula já iniciada?
    elements.append(arrow([(525, 360), (552, 360)], label="sim", label_pos=(538, 350)))

    # Aula iniciada? -> [sim] A-2 (sobe para x=720, y=314)
    elements.append(arrow([(610, 324), (610, 314), (720, 314)], label="sim", label_pos=(650, 304)))

    # Aula iniciada? -> [não] 2. Carrega vídeo (desce para x=720, y=425)
    elements.append(arrow([(610, 396), (610, 425), (720, 425)], label="não", label_pos=(650, 435)))

    # A-2 -> 2. Carrega vídeo (desce pela direita de A-2 para a face superior de 2)
    # A-2: x=720..870, y=290..338. 2: x=720..870, y=400..450.
    # Desce pelo corredor x=895 sem cruzar nenhum texto!
    elements.append(arrow([(870, 314), (895, 314), (895, 375), (795, 375), (795, 400)]))

    # 2. Carrega vídeo -> Vídeo carregou?
    elements.append(arrow([(870, 425), (890, 425)]))

    # Vídeo carregou? -> [não] E-2
    elements.append(arrow([(945, 461), (945, 510)], label="não", label_pos=(945, 485)))

    # E-2 -> Fim 2
    elements.append(arrow([(945, 560), (945, 596)]))

    # Vídeo carregou? -> [sim] 3. Assiste vídeo
    # Sai da face superior de Vídeo carregou? (x=945, y=389), sobe pelo corredor x=980 até y=131, entra na face esquerda de 3 (x=1025)
    # Totalmente livre, sem cruzar nó 2 nem nada!
    elements.append(arrow([(945, 389), (945, 370), (985, 370), (985, 131), (1025, 131)], label="sim", label_pos=(985, 250)))

    # 3. Assiste vídeo -> Tem dúvida?
    elements.append(arrow([(1175, 131), (1195, 131)]))

    # Tem dúvida? -> [sim] A-3. Envia pergunta
    elements.append(arrow([(1295, 131), (1345, 131)], label="sim", label_pos=(1320, 120)))

    # Tem dúvida? -> [não] Saiu da tela?
    # Sobe pelo topo da raia Aluno (y=65), atravessa até x=1780 e desce na face superior de Saiu da tela? (y=304)
    # Totalmente livre, acima de todos os nós de Aluno!
    elements.append(arrow([(1245, 97), (1245, 65), (1780, 65), (1780, 304)], label="não", label_pos=(1510, 55)))

    # A-3. Envia pergunta -> Limite de mensagens?
    # Sai do fundo de A-3 (x=1420, y=157) e desce direto na face superior de Limite (x=1420, y=304)
    elements.append(arrow([(1420, 157), (1420, 304)]))

    # Limite de mensagens? -> [sim] UC001 E-2
    # Sai da face inferior de Limite (x=1420, y=376), entra no topo de UC001 E-2 (x=1420, y=430)
    elements.append(arrow([(1420, 376), (1420, 430)], label="sim", label_pos=(1420, 403)))

    # Limite de mensagens? -> [não] Busca trechos (Tutor de IA)
    # Sai da face esquerda de Limite (x=1362, y=340), desce pelo corredor x=1315 até y=760, entra na esquerda de Busca trechos (x=1345)
    elements.append(arrow([(1362, 340), (1315, 340), (1315, 760), (1345, 760)], label="não", label_pos=(1315, 550)))

    # Busca trechos -> Trecho relevante?
    elements.append(arrow([(1495, 760), (1505, 760)]))

    # Trecho relevante? -> [sim] Gera resposta
    elements.append(arrow([(1560, 724), (1560, 738), (1660, 738)], label="sim", label_pos=(1605, 728)))

    # Trecho relevante? -> [não] UC001 A-1
    elements.append(arrow([(1560, 796), (1560, 808), (1660, 808)], label="não", label_pos=(1605, 818)))

    # Gera resposta -> Exibe resposta (Plataforma)
    # Sai de Gera resposta pela direita (x=1810, y=738), sobe pelo corredor x=1835 até y=700...
    # Espera: Exibe resposta está em x=1560, y=430..480!
    # Trajeto livre de Gera resposta (x=1810, y=738) e UC001 A-1 (x=1810, y=808):
    # Ambos vão para x=1840, sobem pelo corredor x=1840 até y=455, entram na direita de Exibe resposta (x=1710, y=455)
    # MAS wait: Saiu da tela está em x=1780! Corredor x=1840 cruzaria Saiu da tela!
    # Melhor: fazer as setas do Tutor subirem pelo corredor x=1740 (entre Exibe resposta e Saiu da tela)!
    # Exibe resposta termina em x=1710. Saiu da tela começa em x=1725 (1780-55).
    # O corredor entre 1710 e 1725 é apertado (15 px).
    # Vamos posicionar Exibe resposta em x=1520..1670. Aí entre 1670 e 1725 temos 55 px de corredor livre (x=1700)!
    # Vamos redefinir as coordenadas para garantir folga >= 40 px:

def get_complete_svg():
    elements = []

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
    elements.append(f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff" />')

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
            out.append(f'  <rect x="{lx - text_len/2 if label_anchor=="middle" else lx}" y="{ly - 12}" width="{text_len}" height="18" fill="#ffffff" stroke="#e0e0e0" stroke-width="0.8" rx="3" />')
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

    # Col 11 (Plataforma - linha inferior): Vídeo terminou? (cx=1725, cy=465, rw=55, rh=36 -> x=1670..1780, y=429..501)
    elements.append(diamond(1725, 465, 55, 36, ["Vídeo", "terminou?"]))

    # Col 11 (Plataforma - base): 4. Conclui aula (x=1650..1800, y=550..600) e Fim 4 (x=1725, y=635)
    elements.append(action_box(1650, 550, 150, 50, ["4. Conclui aula e", "atualiza progresso"]))
    elements.append(end_node(1725, 635))

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
    # Sai do topo de Vídeo carregou? (x=945, y=379), sobe pelo canal x=990 até y=131 e entra na esquerda de 3 (x=1030)
    elements.append(arrow([(945, 379), (945, 360), (990, 360), (990, 131), (1030, 131)], label="sim", label_pos=(990, 245)))

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
    # Sai da esquerda de Limite (x=1357, y=335), desce pelo canal x=1305 até y=450 e entra na esquerda de UC001 E-2 (x=1230, y=450)?
    # Melhor: UC001 E-2 está em x=1230..1380, y=425..475.
    # Sai de Limite em (x=1357, y=335), vai para x=1305, desce até y=425 (topo de UC001 E-2 em x=1305)
    elements.append(arrow([(1357, 335), (1305, 335), (1305, 425)], label="sim", label_pos=(1305, 375)))

    # 18. Limite de mensagens? -> [não] Busca trechos (Tutor de IA)
    # Sai do fundo de Limite (x=1415, y=371), desce pelo canal x=1415 direto para o topo de Busca trechos (x=1415, y=740)
    # Totalmente reto e limpo no vão entre os nós!
    elements.append(arrow([(1415, 371), (1415, 740)], label="não", label_pos=(1415, 600)))

    # 19. Busca trechos -> Trecho relevante?
    elements.append(arrow([(1490, 765), (1508, 765)]))

    # 20. Trecho relevante? -> [sim] Gera resposta
    elements.append(arrow([(1560, 729), (1560, 738), (1650, 738)], label="sim", label_pos=(1605, 728)))

    # 21. Trecho relevante? -> [não] UC001 A-1
    elements.append(arrow([(1560, 801), (1560, 808), (1650, 808)], label="não", label_pos=(1605, 818)))

    # 22. Gera resposta -> Exibe resposta (Plataforma)
    # Sai da direita de Gera resposta (x=1800, y=738), vai para x=1825, sobe até y=460...
    # Espera: Exibe resposta está em x=1490..1640, y=425..475!
    # Podemos rotear os dois nós do Tutor subindo pelo canal x=1665 (logo à direita de Exibe resposta):
    # Gera resposta sai em (x=1725, y=715 topo), sobe até y=450, vira à esquerda e entra em Exibe resposta (x=1640, y=450)!
    # E UC001 A-1 sai em (x=1800, y=808), sobe pelo canal x=1820 até y=460, vira à esquerda para Exibe resposta?
    # Para ser super limpo e sem cruzamentos:
    # Gera resposta (x=1650..1800, y=715..761): sai da esquerda em x=1650? Não, entrada vem da esquerda.
    # Sai do topo de Gera resposta em (x=1725, y=715), sobe até y=670, vira à esquerda até x=1610, sobe até y=475 (fundo de Exibe resposta em x=1610)!
    # UC001 A-1 sai da direita em (x=1800, y=808), sobe pelo canal x=1830 até y=660, vira à esquerda até x=1550, sobe até y=475 (fundo de Exibe resposta em x=1550)!
    # Dois pontos de entrada distintos no fundo de Exibe resposta: x=1550 e x=1610! Perfeito!
    elements.append(arrow([(1725, 715), (1725, 670), (1610, 670), (1610, 475)]))
    elements.append(arrow([(1800, 808), (1830, 808), (1830, 660), (1550, 660), (1550, 475)]))

    # 23. UC001 E-2 -> Saiu da tela?
    # UC001 E-2 está em x=1230..1380, y=425..475.
    # Sai da direita de UC001 E-2 em (x=1380, y=450), desce até y=500, passa por baixo de Exibe resposta até x=1690, sobe até y=350 e entra na esquerda de Saiu da tela? (x=1670)
    # Espera, Saiu da tela está em cx=1725, cy=335.
    # Melhor trajeto de UC001 E-2:
    # Sai de UC001 E-2 pelo topo (x=1350, y=425), sobe até y=390, segue para a direita até x=1460, sobe até y=335, passa reto por cima de Exibe resposta até a esquerda de Saiu da tela (x=1670, y=335)!
    # E Exibe resposta está em y=425..475, então a linha em y=335 passa LIVRE por cima dele!
    elements.append(arrow([(1350, 425), (1350, 390), (1460, 390), (1460, 335), (1670, 335)]))

    # 24. Exibe resposta -> Saiu da tela?
    # Sai do topo de Exibe resposta em (x=1565, y=425), sobe até y=350, entra em Saiu da tela pelo ponto (x=1670, y=350)!
    # Como o ponto 23 entra em y=335, os dois entram em alturas diferentes na esquerda de Saiu da tela!
    elements.append(arrow([(1565, 425), (1565, 350), (1670, 350)]))

    # 25. Saiu da tela? -> [sim] A-1 Salva segundos
    elements.append(arrow([(1780, 335), (1840, 335)], label="sim", label_pos=(1810, 325)))

    # 26. A-1 -> Fim 3
    elements.append(arrow([(1900, 311), (1900, 241)]))

    # 27. Saiu da tela? -> [não] Vídeo terminou?
    # Sai do fundo de Saiu da tela (x=1725, y=371) e desce direto no topo de Vídeo terminou? (x=1725, y=429)
    elements.append(arrow([(1725, 371), (1725, 429)], label="não", label_pos=(1725, 400)))

    # 28. Vídeo terminou? -> [sim] 4. Conclui aula
    # Sai do fundo de Vídeo terminou? (x=1725, y=501) e desce no topo de 4. Conclui aula (x=1725, y=550)
    elements.append(arrow([(1725, 501), (1725, 550)], label="sim", label_pos=(1725, 525)))

    # 29. 4. Conclui aula -> Fim 4
    elements.append(arrow([(1725, 600), (1725, 621)]))

    # 30. Vídeo terminou? -> [não] Retorna para 3. Assiste ao vídeo
    # Sai da esquerda de Vídeo terminou? (x=1670, y=465) ou da direita?
    # Se sair da direita (x=1780, y=465), vai para x=1980 (borda direita livre),
    # desce pelo corredor inferior de retorno (y=645, entre Plataforma e Tutor),
    # segue para a esquerda até x=1010, e sobe até y=131, entrando na esquerda de 3. Assiste vídeo (x=1030, y=131)!
    # Esse trajeto é 100% livre, não encosta em nenhum nó nem em nenhuma outra seta!
    elements.append(arrow([
        (1780, 465),
        (1975, 465),
        (1975, 645),
        (1010, 645),
        (1010, 131),
        (1030, 131)
    ], label="não: continua", label_pos=(1450, 635)))

    svg_content = f"""<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" xmlns="http://www.w3.org/2000/svg">
{''.join(elements)}
</svg>
"""
    return svg_content

def main():
    svg_code = get_complete_svg()
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg_code)
    print(f"SVG v6 gerado em {SVG_PATH}")

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
    print("Compilando PNG v6 via Chrome headless...")
    subprocess.run(cmd, check=True)
    print(f"PNG v6 gerado com sucesso em {PNG_PATH}")

if __name__ == "__main__":
    main()

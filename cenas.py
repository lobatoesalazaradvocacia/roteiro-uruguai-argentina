# -*- coding: utf-8 -*-
"""Ilustrações em SVG de cada lugar do roteiro, geradas em Python.

Cada cena é desenhada numa tela de 300 x 240 com o assunto principal no miolo,
para aguentar o recorte do cartão-postal no celular e no computador.
As cores são fixas (são "fotos"), por isso valem nos temas claro e escuro.
"""
import math


def _svg(conteudo, rotulo):
    return (f'<svg class="cena" viewBox="0 0 300 240" preserveAspectRatio="xMidYMid slice" '
            f'role="img" aria-label="{rotulo}">{conteudo}</svg>')


def _ceu(id_, cores):
    paradas = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in cores)
    return (f'<defs><linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1">{paradas}</linearGradient></defs>'
            f'<rect width="300" height="240" fill="url(#{id_})"/>')


def _ondas(y, cor, amp=3, passo=20, largura=1.4, opacidade=0.6):
    d = f"M0 {y}"
    x = 0
    while x < 300:
        d += f" q{passo / 4} {-amp} {passo / 2} 0 t{passo / 2} 0"
        x += passo
    return f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{largura}" opacity="{opacidade}"/>'


def sol_de_mayo(cx, cy, r, cor="#F2B51B", rosto="#E09A0C", raios=16, classe=""):
    """Sol de Mayo: raios retos e ondulados alternados, presente nas duas bandeiras."""
    partes = []
    for i in range(raios):
        a = 2 * math.pi * i / raios
        r1, r2 = r * 1.15, r * (2.05 if i % 2 == 0 else 1.85)
        x1, y1 = cx + r1 * math.cos(a), cy + r1 * math.sin(a)
        x2, y2 = cx + r2 * math.cos(a), cy + r2 * math.sin(a)
        if i % 2 == 0:
            # raio reto: triângulo fino
            w = r * 0.16
            px, py = -math.sin(a) * w, math.cos(a) * w
            partes.append(f'<path d="M{x1 + px:.1f} {y1 + py:.1f} L{x2:.1f} {y2:.1f} L{x1 - px:.1f} {y1 - py:.1f}Z"/>')
        else:
            # raio ondulado
            n = 4
            pts = []
            for k in range(n * 6 + 1):
                t = k / (n * 6)
                rr = r1 + (r2 - r1) * t
                off = math.sin(t * n * 2 * math.pi) * r * 0.1
                pts.append((cx + rr * math.cos(a) - math.sin(a) * off, cy + rr * math.sin(a) + math.cos(a) * off))
            d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
            partes.append(f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{r * 0.1:.1f}" stroke-linecap="round"/>')
    cls = f' class="{classe}"' if classe else ""
    return (f'<g{cls} fill="{cor}">{"".join(partes)}'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{cor}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * 0.78:.1f}" fill="none" stroke="{rosto}" stroke-width="{r * 0.08:.1f}"/>'
            f'</g>')


def _fogos(cx, cy, r, cor, raios=14):
    linhas = []
    for i in range(raios):
        a = 2 * math.pi * i / raios
        x1, y1 = cx + r * 0.35 * math.cos(a), cy + r * 0.35 * math.sin(a)
        x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
        linhas.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
        linhas.append(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="1.6" fill="{cor}"/>')
    return f'<g stroke="{cor}" stroke-width="1.6" stroke-linecap="round">{"".join(linhas)}</g>'


# ---------------------------------------------------------------------------
# Cenas
# ---------------------------------------------------------------------------
def rambla():
    letras = "MONTEVIDEO"
    cores = ["#E63946", "#F4A261", "#2A9D8F", "#E9C46A", "#457B9D", "#F28482", "#8AB17D", "#E76F51", "#3D5A80", "#F6BD60"]
    bloco = "".join(
        f'<text x="{60 + i * 18}" y="178" fill="{cores[i]}" font-family="Arial Black, Arial, sans-serif" '
        f'font-weight="900" font-size="22" text-anchor="middle">{c}</text>'
        for i, c in enumerate(letras))
    return _svg(
        _ceu("g-rambla", [(0, "#35507F"), (.45, "#C9678A"), (.75, "#F59E5B"), (1, "#FFD08A")])
        + '<circle cx="205" cy="128" r="34" fill="#FFE3A1"/>'
        + '<rect y="128" width="300" height="42" fill="#2D5C8C"/>'
        + _ondas(138, "#A9CBEA") + _ondas(150, "#A9CBEA", opacidade=.45) + _ondas(161, "#A9CBEA", opacidade=.3)
        + '<rect x="150" y="128" width="110" height="3" fill="#FFE3A1" opacity=".55"/>'
        + '<rect y="166" width="300" height="74" fill="#E8D3A6"/>'
        + '<rect y="166" width="300" height="5" fill="#CDB585"/>'
        + bloco,
        "Pôr do sol na Rambla de Pocitos com o letreiro Montevideo")


def salvo():
    listras = "".join(f'<rect y="{i * 240 / 9:.1f}" width="300" height="{240 / 9:.1f}" fill="#2E63B0" opacity=".9"/>'
                      for i in range(1, 9, 2))
    janelas = ('<pattern id="p-janela" width="8" height="10" patternUnits="userSpaceOnUse">'
               '<rect x="2" y="2" width="4" height="5" fill="#F8D675" opacity=".85"/></pattern>')
    return _svg(
        f'<defs>{janelas}</defs>'
        + '<rect width="300" height="240" fill="#F4F7FC"/>' + listras
        + '<rect width="120" height="107" fill="#F4F7FC"/>'
        + sol_de_mayo(58, 52, 17)
        # Palacio Salvo (1928): base larga, corpo, torre e lanterna
        + '<g fill="#0E2445">'
          '<rect x="140" y="140" width="130" height="100"/>'
          '<rect x="160" y="104" width="90" height="40"/>'
          '<rect x="180" y="72" width="50" height="34"/>'
          '<rect x="192" y="48" width="26" height="26"/>'
          '<path d="M192 48 Q205 30 218 48Z"/>'
          '<rect x="203.5" y="14" width="3" height="24"/>'
          '</g>'
        + '<rect x="146" y="148" width="118" height="92" fill="url(#p-janela)"/>'
        + '<rect x="166" y="110" width="78" height="30" fill="url(#p-janela)"/>'
        + '<rect x="184" y="78" width="42" height="24" fill="url(#p-janela)"/>'
        + '<rect x="0" y="206" width="300" height="34" fill="#1B3B6A"/>',
        "Palacio Salvo diante das listras da bandeira uruguaia e do Sol de Mayo")


def faro():
    return _svg(
        _ceu("g-faro", [(0, "#2B2D5C"), (.5, "#B5547A"), (.8, "#F2915A"), (1, "#FBC77B")])
        + '<circle cx="80" cy="140" r="26" fill="#FFD9A0" opacity=".9"/>'
        + '<rect y="140" width="300" height="100" fill="#28466F"/>'
        + _ondas(152, "#F6B77E", opacidade=.5) + _ondas(166, "#F6B77E", opacidade=.35) + _ondas(182, "#9EB9DA", opacidade=.3)
        # facho de luz
        + '<path d="M204 62 L300 30 L300 80Z" fill="#FFF3C4" opacity=".35"/>'
        # rochas
        + '<path d="M120 240 L140 186 L170 176 L205 170 L240 178 L270 190 L300 206 L300 240Z" fill="#2A2438"/>'
        # farol
        + '<path d="M190 176 L195 76 L213 76 L218 176Z" fill="#F7F4EE"/>'
        + '<rect x="193" y="118" width="22" height="7" fill="#D9D3C7"/>'
        + '<rect x="191" y="66" width="26" height="12" fill="#3A3A48"/>'
        + '<rect x="196" y="68" width="16" height="8" fill="#FFE8A3"/>'
        + '<path d="M189 66 L204 52 L219 66Z" fill="#3A3A48"/>',
        "Farol de Punta Carretas ao pôr do sol")


def travessia():
    return _svg(
        _ceu("g-trav", [(0, "#9CC7EA"), (.55, "#D6E7F3"), (1, "#EAF2F8")])
        # margens distantes: Buenos Aires à esquerda, Montevidéu à direita
        + '<g fill="#6F8FB0" opacity=".75">'
          '<rect x="8" y="92" width="8" height="22"/><rect x="18" y="84" width="7" height="30"/>'
          '<rect x="27" y="96" width="10" height="18"/><rect x="39" y="78" width="6" height="36"/>'
          '<rect x="47" y="90" width="9" height="24"/></g>'
        + '<g fill="#6F8FB0" opacity=".55">'
          '<rect x="252" y="96" width="9" height="18"/><rect x="263" y="84" width="8" height="30"/>'
          '<rect x="273" y="92" width="10" height="22"/><rect x="285" y="100" width="8" height="14"/></g>'
        # o rio "cor de leão"
        + '<rect y="112" width="300" height="128" fill="#B9996B"/>'
        + _ondas(124, "#E5D2B0", opacidade=.6) + _ondas(146, "#E5D2B0", opacidade=.45)
        + _ondas(200, "#E5D2B0", opacidade=.35) + _ondas(222, "#E5D2B0", opacidade=.3)
        # rastro
        + '<path d="M214 170 Q250 176 300 168 M214 176 Q252 186 300 186" stroke="#F3E6CD" stroke-width="2" fill="none" opacity=".8"/>'
        # ferry indo para o oeste (Buenos Aires)
        + '<path d="M70 158 L222 158 L210 180 L86 180Z" fill="#FFFFFF"/>'
        + '<rect x="86" y="170" width="126" height="4" fill="#1D4E96"/>'
        + '<path d="M96 158 L100 138 L200 138 L208 158Z" fill="#F4F6F8"/>'
        + '<g fill="#23405F">' + "".join(f'<rect x="{106 + i * 12}" y="144" width="8" height="6" rx="1"/>' for i in range(8)) + '</g>'
        + '<path d="M118 138 L124 122 L176 122 L182 138Z" fill="#E6EAEE"/>'
        + '<rect x="146" y="108" width="10" height="16" fill="#1D4E96"/>'
        + '<rect x="146" y="108" width="10" height="4" fill="#C8102E"/>',
        "Ferry cruzando o Rio da Prata de Montevidéu a Buenos Aires")


def recoleta():
    petalas = []
    for i in range(6):
        ang = -90 + i * 60
        petalas.append(
            f'<path transform="rotate({ang} 150 104)" d="M150 104 Q170 88 150 40 Q130 88 150 104Z" '
            f'fill="url(#g-metal)" stroke="#7D8C9B" stroke-width="1"/>')
    return _svg(
        '<defs><linearGradient id="g-metal" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#F4F7FA"/><stop offset=".5" stop-color="#B7C3CF"/><stop offset="1" stop-color="#8797A8"/>'
        '</linearGradient></defs>'
        + _ceu("g-rec", [(0, "#8FC1E8"), (1, "#D9ECF8")])
        + '<rect y="166" width="300" height="74" fill="#6FA66A"/>'
        + '<ellipse cx="150" cy="190" rx="118" ry="22" fill="#5E8FB8"/>'
        + '<ellipse cx="150" cy="190" rx="118" ry="22" fill="none" stroke="#D5E6F2" stroke-width="2"/>'
        + '<rect x="146" y="104" width="8" height="84" fill="#8797A8"/>'
        + "".join(petalas)
        + '<circle cx="150" cy="104" r="11" fill="#E8EDF2" stroke="#7D8C9B"/>',
        "Floralis Genérica, a flor de metal da Recoleta")


def caminito():
    casas = [("#D7263D", "#F4C430"), ("#F4C430", "#1B98E0"), ("#1B98E0", "#2E933C"),
             ("#2E933C", "#D7263D"), ("#F28C28", "#1B98E0"), ("#7B2CBF", "#F4C430")]
    partes = []
    x = 0
    larguras = [52, 46, 54, 48, 50, 50]
    alturas = [96, 118, 86, 108, 92, 112]
    for (cor, porta), w, h in zip(casas, larguras, alturas):
        y = 240 - h
        partes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{cor}"/>')
        partes.append(f'<rect x="{x}" y="{y}" width="{w}" height="6" fill="#9BA3AE"/>')
        for jx in (x + 8, x + w - 20):
            partes.append(f'<rect x="{jx}" y="{y + 18}" width="12" height="18" fill="#FDF3C4"/>')
            partes.append(f'<rect x="{jx - 3}" y="{y + 36}" width="18" height="3" fill="#1E1E28"/>')
        partes.append(f'<rect x="{x + w / 2 - 7}" y="{240 - 30}" width="14" height="30" fill="{porta}"/>')
        x += w
    return _svg(
        _ceu("g-cam", [(0, "#0E1033"), (.6, "#252A6B"), (1, "#3D3F8F")])
        + _fogos(70, 52, 34, "#FFD166") + _fogos(200, 40, 28, "#EF476F") + _fogos(252, 92, 20, "#7BDFF2")
        + _fogos(140, 88, 16, "#F7F7FF")
        + "".join(partes),
        "Casas coloridas de Caminito sob os fogos do Réveillon")


def palermo():
    rosas = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>' for x, y, c in [
        (24, 206, "#E75A7C"), (40, 214, "#F28BA8"), (58, 204, "#E75A7C"), (238, 210, "#F28BA8"),
        (256, 202, "#E75A7C"), (274, 214, "#F7B2C4"), (90, 222, "#F7B2C4"), (210, 224, "#E75A7C")])
    return _svg(
        _ceu("g-pal", [(0, "#F7C9A8"), (.55, "#F4DCC6"), (1, "#CFE3F1")])
        # Palacio Barolo ao fundo, com seu farol
        + '<g fill="#8E7F9C" opacity=".85"><rect x="226" y="70" width="34" height="80"/>'
          '<rect x="232" y="46" width="22" height="26"/><rect x="237" y="30" width="12" height="18"/>'
          '<circle cx="243" cy="26" r="5" fill="#FFE8A3"/></g>'
        + '<g fill="#3F7D4E"><circle cx="30" cy="118" r="30"/><circle cx="70" cy="110" r="26"/>'
          '<circle cx="110" cy="124" r="22"/><circle cx="290" cy="124" r="26"/></g>'
        + '<rect y="140" width="300" height="100" fill="#79B36C"/>'
        + '<path d="M0 170 Q150 150 300 170 L300 196 Q150 178 0 196Z" fill="#6FA4CF"/>'
        # Puente Griego do Rosedal
        + '<path d="M104 172 Q150 132 196 172" fill="none" stroke="#FAFAF7" stroke-width="7"/>'
        + '<g fill="#FAFAF7"><rect x="112" y="150" width="3" height="20"/><rect x="134" y="140" width="3" height="26"/>'
          '<rect x="163" y="140" width="3" height="26"/><rect x="185" y="150" width="3" height="20"/></g>'
        + rosas,
        "Rosedal de Palermo com o Palacio Barolo ao fundo")


def colon():
    dobras = "".join(
        f'<rect x="{x}" y="0" width="6" height="240" fill="#6E1119" opacity=".55"/>' for x in (10, 30, 50, 244, 264, 284))
    return _svg(
        _ceu("g-col", [(0, "#F6B86B"), (.6, "#F9D8A9"), (1, "#F3E4C8")])
        # avião partindo
        + '<g transform="translate(150 86) rotate(-14)" fill="#2B3A55">'
          '<path d="M-40 0 Q-38 -5 -30 -5 L34 -5 Q42 -4 44 0 Q42 4 34 5 L-30 5 Q-38 5 -40 0Z"/>'
          '<path d="M-6 -4 L10 -30 L18 -30 L10 -4Z"/><path d="M-6 4 L10 30 L18 30 L10 4Z"/>'
          '<path d="M-36 -4 L-30 -18 L-24 -18 L-26 -4Z"/></g>'
        + '<path d="M60 116 Q100 104 120 110" stroke="#FFFFFF" stroke-width="2" fill="none" opacity=".8"/>'
        # palco
        + '<rect y="196" width="300" height="44" fill="#5B3A1E"/>'
        + '<rect y="196" width="300" height="5" fill="#C99A3B"/>'
        # cortinas de veludo
        + '<path d="M0 0 L96 0 Q70 90 86 196 L0 196Z" fill="#9E1B28"/>'
        + '<path d="M300 0 L204 0 Q230 90 214 196 L300 196Z" fill="#9E1B28"/>'
        + dobras
        # moldura dourada do arco
        + '<path d="M0 0 L300 0 L300 22 Q150 48 0 22Z" fill="#8A1520"/>'
        + '<path d="M0 22 Q150 48 300 22" fill="none" stroke="#D8A93F" stroke-width="5"/>'
        + '<circle cx="150" cy="30" r="8" fill="#D8A93F"/>',
        "Cortinas do Teatro Colón abrindo para o voo de volta")


CENAS = {
    "rambla": rambla,
    "salvo": salvo,
    "faro": faro,
    "travessia": travessia,
    "recoleta": recoleta,
    "caminito": caminito,
    "palermo": palermo,
    "colon": colon,
}


def cena(nome):
    return CENAS[nome]()


# ---------------------------------------------------------------------------
# Ornamentos das seções de cidade e do mapa do Rio da Prata
# ---------------------------------------------------------------------------
def voluta(cx, cy, r, voltas=2.2, sentido=1, passos=90):
    """Espiral do filete porteño."""
    pts = []
    for i in range(passos + 1):
        t = i / passos
        a = sentido * t * voltas * 2 * math.pi
        rr = r * (1 - t * 0.85)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)


def filete(lado="esq"):
    """Ornamento de filete porteño: volutas em vermelho, verde e ouro."""
    s = 1 if lado == "esq" else -1
    g = []
    g.append(f'<path d="{voluta(60, 60, 44, sentido=s)}" fill="none" stroke="#D8A93F" stroke-width="9" stroke-linecap="round"/>')
    g.append(f'<path d="{voluta(60, 60, 44, sentido=s)}" fill="none" stroke="#C8283A" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="{voluta(128, 92, 26, voltas=1.8, sentido=-s)}" fill="none" stroke="#D8A93F" stroke-width="7" stroke-linecap="round"/>')
    g.append(f'<path d="{voluta(128, 92, 26, voltas=1.8, sentido=-s)}" fill="none" stroke="#2E9A5E" stroke-width="3.5" stroke-linecap="round"/>')
    # folhas de acanto
    for (x, y, rot, cor) in [(96, 30, -30, "#2E9A5E"), (112, 40, 10, "#3FA9E0"), (30, 112, 60, "#2E9A5E")]:
        g.append(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="5" transform="rotate({rot} {x} {y})" fill="{cor}" stroke="#D8A93F" stroke-width="1.5"/>')
    g.append('<circle cx="60" cy="60" r="5" fill="#F3E3B5"/><circle cx="128" cy="92" r="3.5" fill="#F3E3B5"/>')
    transf = "" if lado == "esq" else ' transform="scale(-1 1) translate(-160 0)"'
    return (f'<svg class="filete filete--{lado}" viewBox="0 0 160 140" aria-hidden="true">'
            f'<g{transf}>{"".join(g)}</g></svg>')


def sol_svg(classe="sol"):
    return f'<svg class="{classe}" viewBox="0 0 100 100" aria-hidden="true">{sol_de_mayo(50, 50, 20)}</svg>'


def mapa_rio():
    """Mapa esquemático do Rio da Prata com as duas rotas de travessia."""
    return (
        '<svg class="mapa-rio" viewBox="0 0 520 300" role="img" '
        'aria-label="Mapa esquemático do Rio da Prata: Buenos Aires a oeste, Colonia e Montevidéu na margem norte">'
        '<rect class="m-agua" width="520" height="300"/>'
        # Uruguai (margem norte)
        '<path class="m-terra" d="M96 0 L520 0 L520 138 C490 130 460 118 432 114 C392 110 350 112 312 106 '
        'C262 98 212 106 172 98 C150 94 128 70 110 40 Z"/>'
        # Argentina (margem sul e delta)
        '<path class="m-terra" d="M0 0 L84 0 C74 32 58 64 54 96 C50 136 58 176 72 204 C96 232 150 256 214 276 '
        'C252 288 286 296 306 300 L0 300 Z"/>'
        '<path class="m-costa" d="M110 40 C128 70 150 94 172 98 C212 106 262 98 312 106 C350 112 392 110 432 114 '
        'C460 118 490 130 520 138"/>'
        '<path class="m-costa" d="M84 0 C74 32 58 64 54 96 C50 136 58 176 72 204 C96 232 150 256 214 276 C252 288 286 296 306 300"/>'
        # rotas
        '<path class="m-rota-colonia" d="M80 196 Q120 150 162 104 L170 100 Q300 80 432 112"/>'
        '<path class="m-rota" d="M80 196 Q250 176 430 116"/>'
        # cidades
        '<circle class="m-ba" cx="76" cy="198" r="8"/>'
        '<circle class="m-mvd" cx="434" cy="114" r="8"/>'
        '<circle class="m-col" cx="164" cy="100" r="4.5"/>'
        '<text class="m-cidade" x="92" y="222">Buenos Aires</text>'
        '<text class="m-sub" x="92" y="240">29/12 a 02/01</text>'
        '<text class="m-cidade" x="428" y="92" text-anchor="end">Montevidéu</text>'
        '<text class="m-sub" x="428" y="74" text-anchor="end">26 a 29/12</text>'
        '<text class="m-sub" x="170" y="86">Colonia</text>'
        '<text class="m-pais" x="330" y="40">URUGUAI</text>'
        '<text class="m-pais" x="20" y="286">ARGENTINA</text>'
        '<text class="m-rio" x="300" y="248" transform="rotate(-10 300 248)">Río de la Plata</text>'
        '<text class="m-legenda" x="183" y="204" transform="rotate(-13 183 204)">Buquebus direta · 2h15 a 2h30</text>'
        '</svg>'
    )


# ---------------------------------------------------------------------------
# Elementos de festa: bandeirinhas, ondas e ícones
# ---------------------------------------------------------------------------
CORES_FESTA = ["#E8363D", "#FFC53D", "#1E5BC6", "#14A86B", "#FF4F8B", "#43A9EC", "#FF8A1F", "#7B4BD1"]


def bandeirinhas_uri(largura=320, altura=54, n=8):
    """Varal de bandeirinhas (como nas festas de bairro) em data URI para usar em CSS."""
    partes = [f"<path d='M0 6 Q{largura / 2} 26 {largura} 6' fill='none' stroke='%231D1B3F' stroke-width='1.6' opacity='.55'/>"]
    passo = largura / n
    for i in range(n):
        x0, x1 = i * passo + 3, (i + 1) * passo - 3

        def y(x):
            t = x / largura
            return (1 - t) ** 2 * 6 + 2 * t * (1 - t) * 26 + t ** 2 * 6

        xm = (x0 + x1) / 2
        cor = CORES_FESTA[i % len(CORES_FESTA)].replace("#", "%23")
        partes.append(f"<path d='M{x0:.1f} {y(x0):.1f} L{x1:.1f} {y(x1):.1f} L{xm:.1f} {y(xm) + 30:.1f}Z' fill='{cor}'/>")
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' width='{largura}' height='{altura}'>{''.join(partes)}</svg>"
    return f'url("data:image/svg+xml;utf8,{svg}")'


def onda(cor, classe="onda"):
    """Divisória ondulada entre faixas; `cor` é a cor da faixa de baixo."""
    return (f'<svg class="{classe}" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="M0 50 C 180 90 360 90 540 55 S 900 5 1080 35 S 1320 80 1440 45 V90 H0Z" fill="{cor}"/></svg>')


ICONES = {
    "rua": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "cultura": '<path d="M3 9l9-5 9 5"/><path d="M5.5 9v9M10 9v9M14 9v9M18.5 9v9"/><path d="M3 20h18"/>',
    "comida": '<path d="M7 3v7M4.5 3v4.5a2.5 2.5 0 0 0 5 0V3M7 10v11"/><path d="M17.5 21V3c-2.2 1.6-3.5 4.3-3.5 8h3.5"/>',
    "cafe": '<path d="M4 9h12v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M16 10.5h1.5a2.5 2.5 0 0 1 0 5H16"/><path d="M8 3.5c-1 1 1 2 0 3M12 3.5c-1 1 1 2 0 3"/>',
    "doce": '<path d="M7.5 10.5a4.5 4.5 0 1 1 9 0"/><path d="M6.5 10.5h11L12 22z"/><path d="M9 14l5 3"/>',
    "mov": '<path d="M4 15.5l1.6-5.2A2 2 0 0 1 7.5 9h9a2 2 0 0 1 1.9 1.3l1.6 5.2V18H4z"/><circle cx="7.5" cy="18" r="1.6"/><circle cx="16.5" cy="18" r="1.6"/>',
    "feira": '<path d="M5 8h14l-1.2 13H6.2z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/>',
    "festa": '<path d="M12 2.5v4M12 17.5v4M2.5 12h4M17.5 12h4M5.3 5.3l2.8 2.8M15.9 15.9l2.8 2.8M5.3 18.7l2.8-2.8M15.9 8.1l2.8-2.8"/>',
    "pausa": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
    "mapa": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "seta": '<path d="M7 17L17 7M9 7h8v8"/>',
    "casa": '<path d="M3 11l9-7 9 7"/><path d="M5.5 9.5V20h13V9.5"/><path d="M10 20v-5h4v5"/>',
    "calendario": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M8 14h2M14 14h2M8 17h2"/>',
    "navio": '<path d="M3 17.5c1.5 1.2 3 1.2 4.5 0s3-1.2 4.5 0 3 1.2 4.5 0 3-1.2 4.5 0"/><path d="M5 14.5L4 11h16l-1.5 3.5"/><path d="M7 11V7h8l2 4"/><path d="M11 7V4"/>',
    "documento": '<rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M8.5 17h7"/>',
    "escudo": '<path d="M12 3l7.5 3v5.5c0 4.6-3.2 8-7.5 9.5-4.3-1.5-7.5-4.9-7.5-9.5V6z"/><path d="M9 12l2 2 4-4"/>',
    "check": '<rect x="4" y="4" width="16" height="16" rx="4"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>',
    "livro": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/>',
    "lupa": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/>',
    "pontos": '<circle cx="12" cy="5" r="1.6" fill="currentColor"/><circle cx="12" cy="12" r="1.6" fill="currentColor"/><circle cx="12" cy="19" r="1.6" fill="currentColor"/>',
    "fechar": '<path d="M6 6l12 12M18 6L6 18"/>',
    "esq": '<path d="M15 5l-7 7 7 7"/>',
    "dir": '<path d="M9 5l7 7-7 7"/>',
    "cidade": '<path d="M3 21h18"/><path d="M5 21V9l5-3v15"/><path d="M10 21V4h9v17"/><path d="M13 8h3M13 12h3M13 16h3"/>',
    "ticket": '<path d="M3.5 8.5V6.5a1.5 1.5 0 0 1 1.5-1.5h14a1.5 1.5 0 0 1 1.5 1.5v2a2.5 2.5 0 0 0 0 5v2a1.5 1.5 0 0 1-1.5 1.5H5a1.5 1.5 0 0 1-1.5-1.5v-2a2.5 2.5 0 0 0 0-5z"/><path d="M14.5 5v2.5M14.5 11v2M14.5 16.5V19"/>',
    "estrela": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
}


def icone(nome, classe="ico"):
    return (f'<svg class="{classe}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONES[nome]}</svg>')

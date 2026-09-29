#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o site do roteiro a partir de dados.py.

Uso:
    python3 gerar_site.py              gera docs/index.html
    python3 gerar_site.py --abrir      gera e abre no navegador
    python3 gerar_site.py --servir     gera e publica na rede Wi-Fi local (celulares na mesma rede)

As fotos ficam em docs/fotos (baixadas com baixar_fotos.py). Se alguma faltar,
o dia usa a ilustração de cenas.py no lugar. Só usa a biblioteca padrão do Python 3.
"""
import argparse
import datetime as dt
import functools
import html
import http.server
import json
import re
import socket
import webbrowser
from pathlib import Path
from urllib.parse import quote_plus

import cenas
import dados

RAIZ = Path(__file__).resolve().parent
MODELO = RAIZ / "modelo"
SAIDA = RAIZ / "docs"
FOTOS = SAIDA / "fotos"
CREDITOS = json.loads((RAIZ / "creditos_fotos.json").read_text(encoding="utf-8")) \
    if (RAIZ / "creditos_fotos.json").exists() else {}

FONTES_GOOGLE = ("https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400"
                 "&family=Shrikhand&family=Yellowtail&display=swap")

SEMANA = {"Sáb": "Sábado", "Dom": "Domingo", "Seg": "Segunda", "Ter": "Terça", "Qua": "Quarta", "Qui": "Quinta", "Sex": "Sexta"}
MESES = {"12": "dez", "01": "jan"}
TIPOS = {
    "rua": "Passeio", "cultura": "Museu e cultura", "comida": "Refeição", "cafe": "Café", "doce": "Sorvete",
    "mov": "Deslocamento", "feira": "Feira e compras", "festa": "Noite", "pausa": "Descanso",
}
MENU = [
    ("roteiro", "Roteiro"), ("montevideu", "Montevidéu"), ("buenos-aires", "Buenos Aires"), ("comer", "Onde comer"),
    ("compras", "Compras"), ("travessia", "Travessia e Réveillon"), ("antes", "Antes de ir"),
    ("seguranca", "Segurança"), ("pendencias", "Checklist"), ("fontes", "Fontes"),
]
COR_CATEGORIA = {"carnes": "vermelho", "restaurantes": "roxo", "cafes": "cafe", "pizzas": "laranja", "sorvetes": "rosa"}
ICONE_CATEGORIA = {"carnes": "comida", "restaurantes": "comida", "cafes": "cafe", "pizzas": "comida", "sorvetes": "doce"}
CORES_NOTAS = ["sol", "rosa", "celeste", "verde", "laranja", "roxo"]

NC = re.compile(r"\bn/c\b")
DATA_CURTA = re.compile(r"\b(\d{2})/(\d{2})\b")


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def e(texto):
    return html.escape(str(texto), quote=True)


def rico(texto):
    """Escapa o texto e transforma "n/c" num selo de "não confirmado"."""
    return NC.sub('<abbr class="nc" title="não confirmado">n/c</abbr>', e(texto))


def foto(chave):
    """Caminho relativo da foto, ou None se ela ainda não foi baixada."""
    return f"fotos/{chave}.jpg" if chave and (FOTOS / f"{chave}.jpg").exists() else None


def img(chave, alt, classe="", lazy=True):
    src = foto(chave)
    if not src:
        return ""
    cls = f' class="{classe}"' if classe else ""
    carga = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img{cls} src="{src}" alt="{e(alt)}"{carga}>'


def credito(chave):
    c = CREDITOS.get(chave)
    if not c or not foto(chave):
        return ""
    autor = c["autor"] if len(c["autor"]) <= 42 else c["autor"][:40].rstrip() + "…"
    return f'<span class="credito">Foto: {e(autor)} · {e(c["licenca"])}</span>'


def url_mapa(busca):
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(busca)


def link_mapa(busca, rotulo="Ver no mapa"):
    return (f'<a class="lk" href="{e(url_mapa(busca))}" target="_blank" rel="noopener">'
            f'{cenas.icone("mapa")}{e(rotulo)}</a>')


def link_site(url, rotulo="Site oficial"):
    return (f'<a class="lk lk-site" href="{e(url)}" target="_blank" rel="noopener">'
            f'{e(rotulo)}{cenas.icone("seta")}</a>')


def whatsapp(numero, rotulo="WhatsApp"):
    digitos = re.sub(r"\D", "", numero)
    return (f'<span class="zap">{e(rotulo)}: <code>{e(numero)}</code>'
            f'<button class="copiar" type="button" data-copiar="+{digitos}">Copiar</button>'
            f'{link_site("https://wa.me/" + digitos, "Abrir conversa")}</span>')


def ddmm(iso):
    return f"{iso[8:10]}/{iso[5:7]}"


DIA_POR_ID = {d["id"]: d for d in dados.DIAS}
ID_POR_DATA = {ddmm(d["data"]): d["id"] for d in dados.DIAS}


def link_dia(texto):
    """Liga um texto como "Qua 30/12 (opção)" ao cartão daquele dia."""
    m = DATA_CURTA.search(texto)
    alvo = ID_POR_DATA.get(m.group(0)) if m else None
    conteudo = f"No roteiro: {e(texto)}"
    if alvo:
        return f'<a class="no-roteiro" href="#{alvo}">{conteudo}</a>'
    return f'<span class="no-roteiro">{conteudo}</span>'


def titulo_secao(script, titulo_html, texto=""):
    p = f"<p>{rico(texto)}</p>" if texto else ""
    return f'<div class="titulo-secao"><span class="script">{e(script)}</span><h2>{titulo_html}</h2>{p}</div>'


def faixa(id_, fundo, conteudo, proxima, extra=""):
    return (f'<section class="faixa faixa--{fundo}" id="{id_}"{extra}>{conteudo}'
            f'{cenas.onda(proxima)}</section>')


# ---------------------------------------------------------------------------
# Topo e abertura
# ---------------------------------------------------------------------------
def topo():
    itens = "".join(f'<a href="#{i}">{e(r)}</a>' for i, r in MENU)
    return (f'<header class="topo"><div class="topo-in">'
            f'<a class="marca" href="#inicio">{cenas.sol_svg()}<span>Uruguai &amp; Argentina</span></a>'
            f'<nav class="menu" aria-label="Seções">{itens}</nav></div></header>')


def palavra_foto(texto, chave, cor, pais):
    src = foto(chave)
    if src:
        return f'<span class="foto-letra foto-letra--{pais}" style="--img:url(\'{src}\')">{e(texto)}</span>'
    return f'<span style="color:var(--{cor})">{e(texto)}</span>'


def abertura(hoje):
    v = dados.VIAGEM
    faltam = (dt.date.fromisoformat(v["inicio"]) - hoje).days
    num = str(faltam) if faltam > 0 else "Hoje"
    rot = ("dia para embarcar" if faltam == 1 else "dias para embarcar") if faltam > 0 else "Boa viagem!"
    polaroides = "".join(
        f'<figure class="polaroide">{img(ch, legenda, lazy=False)}<figcaption>{e(legenda)}</figcaption></figure>'
        for ch, legenda in dados.POLAROIDES if foto(ch))
    return f"""
<section class="ceu" id="inicio">
  <div class="bandeirinhas" aria-hidden="true"></div>
  {cenas.sol_svg("sol-ceu")}
  <div class="wrap ceu-in">
    <div class="ceu-titulo">
      <p class="saludos">¡Saludos desde</p>
      <h1 class="letreiro"><span class="linha">{palavra_foto("Uruguai", "rambla", "azul", "uy")}<span class="e">&amp;</span></span><span class="linha">{palavra_foto("Argentina!", "caminito", "vermelho", "ar")}</span></h1>
    </div>
    <div class="ceu-texto">
      <p class="lead">{rico(v["resumo"])}</p>
      <ul class="pilulas">
        <li class="pilula cor-azul">3 noites em Montevidéu</li>
        <li class="pilula cor-celeste">4 noites em Buenos Aires</li>
        <li class="pilula cor-rosa">{v["viajantes"]} viajantes</li>
        <li class="pilula cor-sol">1 Réveillon inesquecível</li>
      </ul>
      <a class="contagem" id="contagem" href="#roteiro"><span class="num" id="contagem-num">{num}</span><span class="rot" id="contagem-rot">{rot}<small>26 de dezembro, Montevidéu</small></span></a>
    </div>
    <div class="polaroides">{polaroides}</div>
  </div>
  {cenas.onda("var(--papel)")}
</section>"""


# ---------------------------------------------------------------------------
# Roteiro
# ---------------------------------------------------------------------------
def parada(p):
    tipo = p["tipo"]
    reserva = '<span class="selo-reserva">Reservar</span>' if p.get("reserva") else ""
    links = "".join(link_mapa(q, r) for r, q in p.get("mapas", []))
    links += "".join(link_site(u, r) for r, u in p.get("links", []))
    if p.get("whatsapp"):
        links += whatsapp(p["whatsapp"][1])
    links_html = f'<div class="links">{links}</div>' if links else ""
    mini = img(p.get("foto"), p["titulo"], "mini")
    return (f'<li class="parada" data-tipo="{tipo}">'
            f'<span class="bolinha" title="{e(TIPOS[tipo])}">{cenas.icone(tipo)}'
            f'<span class="visually-hidden">{e(TIPOS[tipo])}: </span></span>'
            f'<div><span class="hora">{e(p["hora"])}</span><h4>{rico(p["titulo"])}{reserva}</h4>'
            f'<p>{rico(p["texto"])}</p>{links_html}</div>{mini}</li>')


def cartao_dia(d, n):
    rotulo = f'{d["semana"]} {ddmm(d["data"])} · {d["titulo"]}'
    pais = {"mvd": "Uruguai", "ba": "Argentina", "rio": "Uruguai → Argentina"}[d["cidade"]]
    imagem = img(d["foto"], d["legenda"]) or cenas.cena(d["cena"])
    nota = f'<p class="dia-nota">{rico(d["nota"])}</p>' if d.get("nota") else ""
    aviso = ""
    if d.get("aviso"):
        t, texto = d["aviso"]
        aviso = f'<div class="aviso"><b>{e(t)}</b>{rico(texto)}</div>'
    paradas = "".join(parada(p) for p in d["paradas"])
    return f"""
<article class="dia cor-{d["cor"]}" id="{d["id"]}" data-data="{d["data"]}" data-titulo="{e(rotulo)}">
  <figure class="dia-foto">
    {imagem}
    <span class="selo-data"><b>{d["data"][8:10]}</b><small>{MESES[d["data"][5:7]]}</small></span>
    <span class="pais-foto">{e(pais)}</span>
    <figcaption>{e(d["legenda"])}{credito(d["foto"])}</figcaption>
  </figure>
  <div class="dia-corpo">
    <span class="dia-etiqueta">Dia {n} · {e(SEMANA[d["semana"]])}</span><span class="hoje-selo">HOJE</span>
    <h3>{e(d["titulo"])}</h3>
    <p class="dia-lugar">{e(d["lugar"])}</p>
    {nota}
    <ol class="paradas">{paradas}</ol>
    {aviso}
  </div>
</article>"""


def roteiro():
    notas = "".join(
        f'<li class="nota-ordem cor-{CORES_NOTAS[i % len(CORES_NOTAS)]}"><b>{e(q)}</b>{rico(t)}</li>'
        for i, (q, t) in enumerate(dados.ORDEM))
    premissas = "".join(f"<li>{rico(p)}</li>" for p in dados.PREMISSAS)
    chips = "".join(
        f'<a class="dia-chip cor-{d["cor"]}" href="#{d["id"]}" data-data="{d["data"]}">'
        f'<small>{e(d["semana"])}</small><b>{d["data"][8:10]}</b>'
        f'<span>{"Montevidéu" if d["cidade"] == "mvd" else "Buenos Aires" if d["cidade"] == "ba" else "Ferry"}</span></a>'
        for d in dados.DIAS)
    dias = "".join(cartao_dia(d, i + 1) for i, d in enumerate(dados.DIAS))
    conteudo = f"""
<div class="wrap">
  {titulo_secao("Dia a dia", "Oito dias de alegria",
                "Cada período tem de três a cinco pontos, todos a pé dentro do mesmo bloco. Sorvete, café e lanche entram como paradas no caminho.")}
  <ul class="notas-ordem" aria-label="Por que os passeios estão nesta ordem">{notas}</ul>
  <div class="premissas">
    <h3>Premissas do roteiro</h3>
    <ul>{premissas}</ul>
    <p><abbr class="nc" title="não confirmado">n/c</abbr> = não confirmado. {rico(dados.NOTA_ESTIMATIVAS)}</p>
  </div>
  <nav class="dias-nav" aria-label="Dias da viagem">{chips}</nav>
  <div class="dias">{dias}</div>
</div>"""
    return faixa("roteiro", "papel", conteudo, "var(--azul)")


# ---------------------------------------------------------------------------
# Cidades
# ---------------------------------------------------------------------------
def ficha(p, cidade_mapa):
    end = f'<p class="end">{rico(p["endereco"])}</p>' if p["endereco"] else ""
    busca = p["mapa"] or ", ".join(x for x in (p["nome"], p["endereco"], cidade_mapa) if x)
    links = link_mapa(busca)
    if p["link"]:
        links += link_site(p["link"])
    return (f'<div class="ficha"><h4>{rico(p["nome"])}</h4>{end}<dl>'
            f'<dt>Horário</dt><dd>{rico(p["horario"])}</dd>'
            f'<dt>Entrada</dt><dd>{rico(p["entrada"])}</dd>'
            f'<dt>Dica</dt><dd>{rico(p["obs"])}</dd></dl>'
            f'<div class="links">{links}</div></div>')


def bloco(chave, b, cidade_mapa):
    dias = "".join(
        f'<a class="cor-{DIA_POR_ID[i]["cor"]}" href="#{i}">{e(DIA_POR_ID[i]["semana"])} {ddmm(DIA_POR_ID[i]["data"])}</a>'
        for i in b["dias"])
    fichas = "".join(ficha(p, cidade_mapa) for p in b["pontos"])
    return (f'<article class="bloco" id="{chave}-{b["letra"].lower()}"><div class="bloco-cab">'
            f'<span class="letra" aria-hidden="true">{b["letra"]}</span><div>'
            f'<h3><span class="visually-hidden">Bloco {b["letra"]}: </span>{e(b["nome"])}</h3>'
            f'<p class="bloco-sub">{rico(b["sub"])}</p><div class="bloco-dias">{dias}</div></div></div>'
            f'<div class="fichas">{fichas}</div></article>')


def cartao_cultura(c):
    return (f'<figure class="cult cor-{c["cor"]}">{img(c["foto"], c["titulo"])}<figcaption>'
            f'<span class="tag">{e(c["tag"])}</span><h4>{e(c["titulo"])}</h4><p>{rico(c["texto"])}</p>'
            f'{credito(c["foto"])}</figcaption></figure>')


def gemeos():
    g = dados.GEMEOS
    fotos = "".join(f'<figure>{img(ch, leg)}<figcaption>{e(leg)}</figcaption></figure>' for ch, leg in g["fotos"] if foto(ch))
    return (f'<div class="gemeos"><div class="gemeos-fotos">{fotos}</div><div>'
            f'<span class="script">Você sabia?</span><h3>{e(g["titulo"])}</h3><p>{rico(g["texto"])}</p></div></div>')


def cidade(chave, ancora):
    c = dados.CIDADES[chave]
    pilulas = f'<ul class="pilulas"><li class="pilula">{e(c["noites"])}</li><li class="pilula">{e(c["moeda"])}</li></ul>'
    if chave == "mvd":
        enfeite = f'<span class="bandeira-uy" aria-hidden="true">{cenas.sol_svg("sol-bandeira")}</span>'
        faixa_ar = ""
        titulo_cultura = ("Cultura uruguaia", "para viver de perto")
    else:
        enfeite = cenas.filete("esq") + cenas.filete("dir")
        faixa_ar = '<div class="faixa-ar" aria-hidden="true"></div>'
        titulo_cultura = ("Cultura portenha", "tango, filete e doce de leite")
    cultura = "".join(cartao_cultura(x) for x in dados.CULTURA[chave])
    extra_ba = gemeos() if chave == "ba" else ""
    blocos = "".join(bloco(chave, b, c["cidade_mapa"]) for b in c["blocos"])
    if c.get("extras"):
        itens = []
        for x in c["extras"]:
            zap = whatsapp(x["whatsapp"]) if x.get("whatsapp") else ""
            itens.append(
                f'<div class="extra"><span class="quando">{e(x["quando"])}</span><h4>{e(x["nome"])}</h4>'
                f'<p class="end">{e(x["onde"])}</p><p>{rico(x["info"])}</p>'
                f'<div class="links">{link_mapa(x["onde"] + ", " + c["cidade_mapa"])}{link_site(x["link"], "Página")}{zap}</div></div>')
        blocos += (f'<article class="bloco" id="{chave}-extras"><div class="bloco-cab">'
                   f'<span class="letra" aria-hidden="true">+</span><div><h3>Extras dos vídeos</h3>'
                   f'<p class="bloco-sub">Cinco lugares dos vídeos entraram no roteiro, alguns como opção.</p></div></div>'
                   f'<div class="extras-lista">{"".join(itens)}</div></article>')
    conteudo = f"""
<div class="wrap">
  <div class="banner">
    {img(c["foto"], c["legenda"])}
    {enfeite}
    <span class="script">{e(c["saudacao"])}</span>
    <h2>{e(c["nome"])}</h2>
    <p>{rico(c["intro"])}</p>
    {faixa_ar}
    {pilulas}
    {credito(c["foto"])}
  </div>
  <div class="sub-titulo"><h3>{titulo_cultura[0]}</h3><span class="script">{titulo_cultura[1]}</span></div>
  <div class="cultura">{cultura}</div>
  {extra_ba}
  <div class="sub-titulo"><h3>Os blocos de passeio</h3><span class="script">tudo a pé, de A a {c["blocos"][-1]["letra"]}</span></div>
  <div class="blocos">{blocos}</div>
  <p class="fora">{rico(c["fora"])}</p>
</div>"""
    fundo, proxima = ("azul", "var(--filete-bg)") if chave == "mvd" else ("filete", "var(--amarelo-claro)")
    return faixa(ancora, fundo, conteudo, proxima, ' data-cidade="%s"' % chave)


# ---------------------------------------------------------------------------
# Onde comer, compras, travessia, réveillon
# ---------------------------------------------------------------------------
def restaurante(r):
    cid = dados.CIDADES[r["cidade"]]
    cat = dict(dados.CATEGORIAS)[r["cat"]]
    linhas = [("Destaque", r["destaque"]), ("Preço", r["preco"]), ("Nota", r["nota"]), ("Reserva", r["reserva"])]
    dl = "".join(f"<dt>{k}</dt><dd>{rico(v)}</dd>" for k, v in linhas if v)
    busca = r["mapa"] or f'{r["nome"]}, {r["onde"]}, {cid["cidade_mapa"]}'
    links = link_mapa(busca)
    if r["link"]:
        links += link_site(r["link"])
    if r["whatsapp"]:
        links += whatsapp(r["whatsapp"])
    dia = link_dia(r["dia"]) if r["dia"] else ""
    return (f'<article class="rest cor-{COR_CATEGORIA[r["cat"]]}" data-cidade="{r["cidade"]}" data-cat="{r["cat"]}">'
            f'<div class="rest-faixa"><span>{cenas.icone(ICONE_CATEGORIA[r["cat"]])}{e(cat)}</span>'
            f'<span class="pais">{e(cid["nome"])}</span></div>'
            f'<h3>{e(r["nome"])}</h3><p class="onde">{rico(r["onde"])}</p>'
            f'{f"<dl>{dl}</dl>" if dl else ""}{dia}<div class="links">{links}</div></article>')


def comer():
    cidades = [("todas", "Todas", ""), ("mvd", "Montevidéu", "cor-azul"), ("ba", "Buenos Aires", "cor-celeste")]
    cats = [("todas", "Todos", "")] + [(k, r, f"cor-{COR_CATEGORIA[k]}") for k, r in dados.CATEGORIAS]

    def chips(nome, itens):
        return "".join(
            f'<button class="chip {cls}" type="button" data-filtro="{nome}" data-valor="{v}" '
            f'aria-pressed="{"true" if v == "todas" else "false"}">{e(r)}</button>' for v, r, cls in itens)

    cards = "".join(restaurante(r) for r in dados.RESTAURANTES)
    dicas = "".join(f"<li>{rico(t)}</li>" for _, t in dados.DICAS_COMIDA)
    conteudo = f"""
<div class="wrap">
  {titulo_secao("Parrillas, cafés e sorvetes", "Onde <em>comer</em> (e muito!)",
                "Em Buenos Aires as melhores carnes exigem reserva com semanas de antecedência; em Montevidéu o melhor custo-benefício está no Mercado del Puerto e nas parrillas de Punta Carretas. Notas do TripAdvisor (TA) na data da pesquisa.")}
  <div class="filtros">
    <div class="filtro-linha" role="group" aria-label="Filtrar por cidade"><span>Cidade</span>{chips("cidade", cidades)}</div>
    <div class="filtro-linha" role="group" aria-label="Filtrar por tipo"><span>Tipo</span>{chips("cat", cats)}</div>
    <p class="contador" id="contador-rest" aria-live="polite">{len(dados.RESTAURANTES)} lugares</p>
  </div>
  <div class="rest-grid">{cards}</div>
  <p class="vazio" id="rest-vazio" hidden>Nenhum lugar com esse filtro. Escolham outra cidade ou tipo.</p>
  <ul class="dicas">{dicas}</ul>
  <p class="reservem" data-so-antes><b>Reservem já!</b> Faltam <strong data-faltam>…</strong> dias: Don Julio, Fogón Asado e La Carnicería lotam com semanas de antecedência.</p>
</div>"""
    return faixa("comer", "amarelo", conteudo.replace("<em>", "").replace("</em>", ""), "var(--rosa-claro)")


def lista_compras(itens, cor):
    lis = "".join(
        f'<li class="cor-{cor}"><span class="cat">{e(cat)}</span><span class="melhor">{rico(melhor)}</span>'
        f'<span class="det">{rico(onde)}</span><span class="det">{rico(obs)}</span></li>'
        for cat, melhor, onde, obs in itens)
    return f'<ul class="lista-compras">{lis}</ul>'


def compras():
    notas = "".join(f'<div class="nota cor-{CORES_NOTAS[i]}"><h4>{e(t)}</h4><p>{rico(x)}</p></div>'
                    for i, (t, x) in enumerate(dados.IMPOSTOS))
    conteudo = f"""
<div class="wrap">
  {titulo_secao("Roupas, couro e lembrancinhas", "O que trazer na mala", dados.COMPRAS_INTRO)}
  <div class="duas">
    <div class="cartao"><div class="cartao-tit"><span class="bandeirinha band-ar"></span><h3>Argentina</h3></div>{lista_compras(dados.COMPRAS["ba"], "celeste")}</div>
    <div class="cartao"><div class="cartao-tit"><span class="bandeirinha band-uy"></span><h3>Uruguai</h3></div>{lista_compras(dados.COMPRAS["mvd"], "azul")}</div>
  </div>
  <div class="notas">{notas}</div>
</div>"""
    return faixa("compras", "rosa", conteudo, "var(--celeste-claro)")


def travessia():
    opcoes = []
    for o in dados.TRAVESSIA:
        rot = '<span class="rotulo">No roteiro</span>' if o.get("no_roteiro") else ""
        opcoes.append(
            f'<div class="opcao{" escolhida" if o.get("no_roteiro") else ""}">{rot}<h4>{e(o["nome"])}</h4>'
            f'<p class="det">{e(o["detalhe"])}</p><div class="numeros">'
            f'<div><small>Duração</small><b>{e(o["duracao"])}</b></div><div><small>Por pessoa</small><b>{e(o["preco"])}</b></div></div>'
            f'<p>{rico(o["texto"])}</p><div class="links">{link_site(o["link"])}</div></div>')
    notas = "".join(f"<li>{rico(n)}</li>" for n in dados.TRAVESSIA_NOTAS)
    conteudo = f"""
<div class="wrap">
  <div class="travessia-topo">
    {titulo_secao("Terça, 29 de dezembro", "Cruzando o Rio da Prata", dados.TRAVESSIA_INTRO)}
    <figure class="mapa">{cenas.mapa_rio()}<figcaption>Em vermelho, a Buquebus direta; pontilhado, a rota via Colonia.</figcaption></figure>
  </div>
  <div class="opcoes">{"".join(opcoes)}</div>
  <ul class="lista-simples">{notas}</ul>
</div>"""
    return faixa("travessia", "celeste", conteudo, "var(--noite)")


def reveillon():
    opcoes = "".join(
        f'<div class="opcao"><h4><span class="letra-op">{r["letra"]}.</span> {e(r["nome"])}</h4><p>{rico(r["lugar"])}</p>'
        f'<div class="numeros"><div><small>Por pessoa (2025)</small><b>{e(r["preco"])}</b></div></div>'
        f'<p class="det">{rico(r["obs"])}</p></div>'
        for r in dados.REVEILLON)
    notas = "".join(f'<div class="nota"><h4>{e(t)}</h4><p>{rico(x)}</p></div>' for t, x in dados.REVEILLON_NOTAS)
    conteudo = f"""
<canvas id="fogos" aria-hidden="true"></canvas>
<div class="wrap">
  {titulo_secao("¡Feliz Año Nuevo!", "Réveillon em Buenos Aires", dados.REVEILLON_INTRO)}
  <div class="opcoes">{opcoes}</div>
  <div class="notas">{notas}</div>
</div>"""
    return faixa("reveillon", "noite", conteudo, "var(--papel)", ' data-menu="travessia"')


# ---------------------------------------------------------------------------
# Antes de ir, segurança, checklist, fontes
# ---------------------------------------------------------------------------
def antes():
    itens = "".join(f'<div class="cor-{CORES_NOTAS[i % len(CORES_NOTAS)]}"><h4>{e(t)}</h4><p>{rico(x)}</p></div>'
                    for i, (t, x) in enumerate(dados.ANTES))
    c = dados.CAMBIO
    brl = 100
    fmt0 = lambda v: f"{v:,.0f}".replace(",", ".")
    conteudo = f"""
<div class="wrap">
  {titulo_secao("Documentos, dinheiro e transporte", "Antes de embarcar", dados.ANTES_INTRO)}
  <div class="antes">{itens}</div>
  <div class="conversor" id="conversor">
    <h3>Conversor de bolso</h3>
    <p>Digitem em qualquer campo. Cotações de referência de 29/09/2026; ajustem antes de usar.</p>
    <div class="moedas">
      <div class="moeda"><label for="conv-brl">Real (R$)</label><input id="conv-brl" type="text" inputmode="decimal" autocomplete="off" value="{brl}"></div>
      <div class="moeda"><label for="conv-uyu">Peso uruguaio (UYU)</label><input id="conv-uyu" type="text" inputmode="decimal" autocomplete="off" value="{fmt0(brl / c["brl_por_uyu"])}"></div>
      <div class="moeda"><label for="conv-ars">Peso argentino (ARS)</label><input id="conv-ars" type="text" inputmode="decimal" autocomplete="off" value="{fmt0(brl * c["ars_por_brl"])}"></div>
    </div>
    <div class="taxas">
      <label for="taxa-uyu">1 UYU = R$ <input id="taxa-uyu" type="text" inputmode="decimal" autocomplete="off" value="{str(c["brl_por_uyu"]).replace(".", ",")}"></label>
      <label for="taxa-ars">R$ 1 = ARS <input id="taxa-ars" type="text" inputmode="decimal" autocomplete="off" value="{c["ars_por_brl"]}"></label>
    </div>
  </div>
</div>"""
    return faixa("antes", "papel", conteudo, "var(--verde-claro)")


def seguranca():
    pares = lambda itens: "".join(f"<div><dt>{e(t)}</dt><dd>{rico(x)}</dd></div>" for t, x in itens)
    conteudo = f"""
<div class="wrap">
  {titulo_secao("A pé, com calma", "Acessibilidade e segurança", dados.DESLOCAMENTOS)}
  <div class="duas">
    <div class="cartao"><div class="cartao-tit"><h3>Acessibilidade</h3></div><dl class="pares">{pares(dados.ACESSIBILIDADE)}</dl></div>
    <div class="cartao"><div class="cartao-tit"><h3>Segurança prática</h3></div><dl class="pares">{pares(dados.SEGURANCA)}</dl></div>
  </div>
</div>"""
    return faixa("seguranca", "verde", conteudo, "var(--papel)")


def pendencias():
    atencao = "".join(f'<div class="nota cor-{CORES_NOTAS[i]}"><h4>{e(t)}</h4><p>{rico(x)}</p></div>'
                      for i, (t, x) in enumerate(dados.ATENCAO))
    quando = lambda q: f'<span class="quando">{rico(q)}</span>' if q else ""
    itens = "".join(
        f'<li><label for="chk-{k}"><input type="checkbox" id="chk-{k}"><span><span class="txt">{rico(t)}</span>'
        f'{quando(q)}</span></label></li>'
        for k, t, q in dados.CHECKLIST)
    perguntas = "".join(f"<li>{rico(p)}</li>" for p in dados.PERGUNTAS)
    conteudo = f"""
<div class="wrap">
  {titulo_secao("Antes de pagar qualquer reserva", "Checklist da turma",
                "Reservas e confirmações na ordem em que travam. As marcações ficam salvas neste aparelho.")}
  <div class="duas">
    <div>
      <div class="progresso"><span id="progresso-texto">0 de {len(dados.CHECKLIST)} feitos</span><span class="barra"><i id="progresso-barra"></i></span></div>
      <ul class="checklist">{itens}</ul>
    </div>
    <div class="cartao"><div class="cartao-tit"><h3>Perguntas que mudam o roteiro</h3></div><ol class="perguntas">{perguntas}</ol></div>
  </div>
  <div class="notas">{atencao}</div>
</div>"""
    return faixa("pendencias", "papel", conteudo, "var(--lavanda)")


def fontes():
    link = lambda u, t: f'<a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a>'
    grupos = "".join(
        f'<div><h3>{e(g)}</h3><ul>{"".join(f"<li>{link(u, t)}</li>" for t, u in links)}</ul></div>'
        for g, links in dados.FONTES)
    creditos = "".join(
        f'<li>{link(c["pagina"], c["titulo"])} · {e(c["autor"])} · {e(c["licenca"])}</li>'
        for ch, c in sorted(CREDITOS.items()) if foto(ch))
    bloco_creditos = (f'<div class="creditos"><h3>Créditos das fotos (Wikimedia Commons)</h3><ul>{creditos}</ul></div>'
                      if creditos else "")
    conteudo = f"""
<div class="wrap">
  {titulo_secao("Pesquisa de 29/09/2026", "Fontes",
                "Onde o site oficial bloqueava leitura, foram usadas fontes secundárias e a informação ficou marcada como n/c.")}
  <div class="fontes">{grupos}</div>
  {bloco_creditos}
</div>"""
    return faixa("fontes", "lavanda", conteudo, "var(--sol)")


def rodape(hoje):
    return (f'<footer class="rodape"><div class="bandeirinhas" aria-hidden="true"></div>{cenas.sol_svg()}'
            f'<p class="tchau">¡Buen viaje!</p>'
            f'<p>Gerado em {hoje.strftime("%d/%m/%Y")} por gerar_site.py a partir de dados.py.</p></footer>')


# ---------------------------------------------------------------------------
# Montagem
# ---------------------------------------------------------------------------
def montar(hoje):
    v = dados.VIAGEM
    css = (MODELO / "estilo.css").read_text(encoding="utf-8")
    css += f"\n:root {{ --bandeirinhas: {cenas.bandeirinhas_uri()}; }}\n"
    js = (MODELO / "app.js").read_text(encoding="utf-8")
    cabeca = (f'<title>{e(v["titulo"])}</title>\n'
              f'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
              f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
              f'<link rel="stylesheet" href="{e(FONTES_GOOGLE)}">\n'
              f'<style>\n{css}\n</style>\n')
    corpo = (f'<div id="app" data-inicio="{v["inicio"]}" data-fim="{v["fim"]}">\n'
             f'{topo()}\n<main>'
             f'{abertura(hoje)}{roteiro()}{cidade("mvd", "montevideu")}{cidade("ba", "buenos-aires")}'
             f'{comer()}{compras()}{travessia()}{reveillon()}{antes()}{seguranca()}{pendencias()}{fontes()}'
             f'</main>\n{rodape(hoje)}\n</div>\n<script>\n{js}\n</script>\n')
    return cabeca, corpo


def gerar():
    hoje = dt.date.today()
    cabeca, corpo = montar(hoje)
    SAIDA.mkdir(exist_ok=True)
    completo = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                '<meta name="description" content="Roteiro dia a dia de Montevidéu e Buenos Aires, 26/12 a 02/01.">\n'
                '<meta name="theme-color" content="#BFE3FF">\n'
                f'{cabeca}</head>\n<body>\n{corpo}</body>\n</html>\n')
    (SAIDA / "index.html").write_text(completo, encoding="utf-8")
    # Versão sem <html>/<head>/<body>, para publicar como Artifact no Claude.
    (SAIDA / "artifact.html").write_text(cabeca + corpo, encoding="utf-8")
    kb = (SAIDA / "index.html").stat().st_size / 1024
    n_fotos = len(list(FOTOS.glob("*.jpg"))) if FOTOS.exists() else 0
    print(f"Site gerado: {SAIDA / 'index.html'} ({kb:.0f} KB, {n_fotos} fotos em docs/fotos)")


def ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def servir(porta):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SAIDA))
    servidor = http.server.ThreadingHTTPServer(("0.0.0.0", porta), handler)
    print(f"Neste Mac:            http://localhost:{porta}")
    print(f"Celulares no Wi-Fi:   http://{ip_local()}:{porta}")
    print("Ctrl+C para parar.")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor parado.")


def main():
    ap = argparse.ArgumentParser(description="Gera o site do roteiro Uruguai e Argentina.")
    ap.add_argument("--abrir", action="store_true", help="abre o site no navegador depois de gerar")
    ap.add_argument("--servir", action="store_true", help="publica o site na rede local")
    ap.add_argument("--porta", type=int, default=8000)
    args = ap.parse_args()
    gerar()
    if args.abrir:
        webbrowser.open((SAIDA / "index.html").as_uri())
    if args.servir:
        servir(args.porta)


if __name__ == "__main__":
    main()

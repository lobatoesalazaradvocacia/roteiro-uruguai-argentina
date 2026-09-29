#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baixa as fotos do site a partir do Wikimedia Commons (licenças livres).

Uso:
    python3 baixar_fotos.py            baixa só as que faltam
    python3 baixar_fotos.py --todas    baixa tudo de novo

As fotos vão para docs/fotos/ (reduzidas para 1200 px de largura) e os
créditos (autor e licença) para creditos_fotos.json, que o gerar_site.py lê.
Usa o curl do macOS porque o Python do python.org vem sem certificados.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlencode

RAIZ = Path(__file__).resolve().parent
PASTA = RAIZ / "docs" / "fotos"
CREDITOS = RAIZ / "creditos_fotos.json"
UA = "RoteiroUruguaiArgentina/1.0 (site pessoal de viagem)"

# chave -> título do arquivo no Wikimedia Commons
FOTOS = {
    # Montevidéu
    "salvo": "Palacio Salvo, Montevideo, Uruguay (2019).jpg",
    "letras": "Letras Montevideo en Pocitos.jpg",
    "rambla": "2016 Rambla de Pocitos Montevideo.jpg",
    "solis": "Montevideo Teatro Solis 1030762PSD.jpg",
    "mercado-puerto": "2016 Mercado del Puerto de Montevideo.jpg",
    "faro": "2016 Faro de Punta Carretas - Montevideo.jpg",
    "legislativo": "Palacio Legislativo Montevideo 2.jpg",
    "tristan-narvaja": "Libros en Feria Tristán Narvaja.jpg",
    "plaza-independencia": "Plaza Independencia, Montevideo.jpg",
    "candombe": "Candombe dancers in Uruguay.jpg",
    "chivito": "Chivito Uruguayo casero.jpg",
    "buquebus": "Buquebus (5459500819).jpg",
    # Buenos Aires
    "caminito": "El caminito2 - Buenos Aires - Argentina.jpg",
    "casa-rosada": "Casa Rosada, Plaza de Mayo (9515728023).jpg",
    "tortoni": "Café Tortoni 01.jpg",
    "floralis": "Floralis Genérica (27547134408).jpg",
    "recoleta": "Cementerio de la Recoleta.jpg",
    "puente-mujer": "Buenos Aires Puente de la Mujer 1030985.jpg",
    "colon": "Teatro Colón - Columbus Theatre - Buenos Aires - Argentina.jpg",
    "ateneo": "Librería El Ateneo Grand Splendid - 1.jpg",
    "barolo": "Palacio Barolo 10.jpg",
    "rosedal": "Rosedal de Palermo en Buenos Aires 2020 by Cesar Perez.jpg",
    "obelisco": "Obelisco de Buenos Aires at sunset.jpg",
    "san-telmo": "Calle Defensa - Plaza Dorrego.jpg",
    # Cultura
    "tango": "Bailarines de Tango en San Telmo.JPG",
    "filete": "Fileteado Porteño Gustavo Ferrari.jpg",
    "asado": "Asado de cerdo con costillas y chorizos al estilo argentino (presentación).jpg",
    "mate": "Traditional mate set calabash gourd with La Merced yerba mate.jpg",
    "alfajor": "Alfajor H.jpg",
}


def curl(url, destino=None):
    cmd = ["curl", "-sSL", "--fail", "--retry", "3", "--retry-delay", "4", "-A", UA, url]
    if destino:
        cmd += ["-o", str(destino)]
    r = subprocess.run(cmd, capture_output=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode(errors="ignore").strip() or f"curl saiu com {r.returncode}")
    return r.stdout


def limpar(texto):
    texto = re.sub(r"<[^>]+>", "", texto or "")
    return re.sub(r"\s+", " ", texto).strip()


def info(titulo):
    params = {"action": "query", "format": "json", "titles": "File:" + titulo, "prop": "imageinfo",
              "iiprop": "url|extmetadata", "iiurlwidth": "1400"}
    dados = json.loads(curl("https://commons.wikimedia.org/w/api.php?" + urlencode(params)))
    pagina = next(iter(dados["query"]["pages"].values()))
    ii = pagina["imageinfo"][0]
    md = ii.get("extmetadata", {})
    return {
        "titulo": titulo,
        "thumb": ii["thumburl"],
        "pagina": ii["descriptionurl"],
        "autor": limpar(md.get("Artist", {}).get("value")) or "Autor desconhecido",
        "licenca": limpar(md.get("LicenseShortName", {}).get("value")) or "ver página",
        "licenca_url": md.get("LicenseUrl", {}).get("value", ""),
    }


def main():
    todas = "--todas" in sys.argv
    PASTA.mkdir(parents=True, exist_ok=True)
    creditos = json.loads(CREDITOS.read_text(encoding="utf-8")) if CREDITOS.exists() else {}
    for chave, titulo in FOTOS.items():
        destino = PASTA / f"{chave}.jpg"
        if destino.exists() and chave in creditos and creditos[chave]["titulo"] == titulo and not todas:
            continue
        try:
            dados = info(titulo)
            curl(dados["thumb"], destino)
            # reduz e recomprime com o sips do macOS
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "60", "-Z", "1200",
                            str(destino), "--out", str(destino)], capture_output=True, check=True)
            creditos[chave] = {k: dados[k] for k in ("titulo", "pagina", "autor", "licenca", "licenca_url")}
            print(f"ok   {chave:20} {destino.stat().st_size / 1024:5.0f} KB  {dados['autor'][:40]}")
        except Exception as ex:  # segue para a próxima foto
            print(f"ERRO {chave:20} {ex}")
        time.sleep(9)
    CREDITOS.write_text(json.dumps(creditos, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(p.stat().st_size for p in PASTA.glob("*.jpg")) / 1024 / 1024
    print(f"{len(list(PASTA.glob('*.jpg')))} fotos, {total:.1f} MB em {PASTA}")


if __name__ == "__main__":
    main()

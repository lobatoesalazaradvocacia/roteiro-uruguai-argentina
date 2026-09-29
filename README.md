# Roteiro Uruguai e Argentina (26/12/2026 a 02/01/2027)

Site do roteiro de viagem, gerado em Python a partir do documento "Roteiro Uruguai e Argentina - 26-12 a 02-01.docx".

**Site no ar:** https://lobatoesalazaradvocacia.github.io/roteiro-uruguai-argentina/

## Como gerar

Não precisa instalar nada: só o `python3` que já vem no Mac.

```bash
python3 gerar_site.py --abrir
```

O resultado fica em `docs/`: a página `docs/index.html` e as fotos em `docs/fotos/`. O GitHub Pages publica essa pasta.

## Atualizar o site no ar

Depois de editar e gerar de novo:

```bash
git add -A && git commit -m "Atualiza roteiro" && git push
```

Em cerca de um minuto o GitHub Pages mostra a versão nova.

## Ver no celular (mesma rede Wi-Fi)

```bash
python3 gerar_site.py --servir
```

O terminal mostra um endereço como `http://192.168.0.10:8000`. Abra esse endereço no navegador do celular.

## Como editar o roteiro

| Quero mudar... | Arquivo |
| --- | --- |
| Horários, paradas, restaurantes, compras, checklist, cultura | `dados.py` |
| Reservas (link, contato, antecedência, valor) e verificação do Réveillon | `reservas.py` |
| Fotos (Wikimedia Commons, licenças livres) | `baixar_fotos.py` → `docs/fotos/` e `creditos_fotos.json` |
| Sol de Mayo, filete, bandeirinhas, ícones e mapa do Rio da Prata | `cenas.py` |
| Cores, fontes e layout | `modelo/estilo.css` |
| Contagem regressiva, filtros, conversor de moedas, checklist, fogos | `modelo/app.js` |

Qualquer texto com `n/c` vira automaticamente um selo de "não confirmado". Quando confirmar um horário, é só tirar o `n/c` do texto em `dados.py`.

## O que o site tem

- Roteiro dia a dia em polaroides com foto e cor própria para cada dia
- Montevidéu (azul uruguaio) e Buenos Aires (filete porteño), com cultura local e blocos de passeio A a G
- Todos os pontos com botão "Ver no mapa" (abre o Google Maps)
- Onde comer, com filtro por cidade e tipo (carnes, cafés, pizzas, sorvetes)
- Compras, tax free, travessia do Rio da Prata e Réveillon com fogos animados
- Conversor de moedas R$ / UYU / ARS
- Checklist de reservas (as marcações ficam salvas no aparelho de cada pessoa)
- Durante a viagem, o site destaca o dia de hoje automaticamente

`docs/artifact.html` é a mesma página sem as tags `<html>/<head>/<body>`, usada para publicar o link no Claude.

## Créditos

Fotos do [Wikimedia Commons](https://commons.wikimedia.org), com autor e licença listados no fim do site e em `creditos_fotos.json`.

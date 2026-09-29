(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var semMovimento = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var CORES = ["#E8363D", "#FFC53D", "#1E5BC6", "#14A86B", "#FF4F8B", "#43A9EC", "#FF8A1F", "#7B4BD1"];

  // Preferências salvas só neste aparelho; a página funciona sem elas.
  var guardar = {
    ler: function (chave, padrao) {
      try { var v = localStorage.getItem(chave); return v === null ? padrao : JSON.parse(v); }
      catch (e) { return padrao; }
    },
    gravar: function (chave, valor) {
      try { localStorage.setItem(chave, JSON.stringify(valor)); } catch (e) { /* sem armazenamento */ }
    }
  };

  var app = $("#app");
  if (!app) return;

  // ---------- Datas: contagem regressiva e "hoje" ----------
  function isoLocal(d) {
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  function diasEntre(a, b) {
    return Math.round((Date.parse(b + "T12:00:00") - Date.parse(a + "T12:00:00")) / 86400000);
  }
  var hoje = isoLocal(new Date());
  var faltam = diasEntre(hoje, app.dataset.inicio);
  var cartaoHoje = $('.dia[data-data="' + hoje + '"]');
  var contagem = $("#contagem"), num = $("#contagem-num"), rot = $("#contagem-rot");
  if (faltam > 0) {
    num.textContent = String(faltam);
    rot.innerHTML = (faltam === 1 ? "dia para" : "dias para") + " embarcar<small>26 de dezembro, Montevidéu</small>";
    $$("[data-faltam]").forEach(function (el) { el.textContent = String(faltam); });
  } else if (cartaoHoje) {
    cartaoHoje.classList.add("hoje");
    $$('[data-data="' + hoje + '"]').forEach(function (el) { el.classList.add("hoje"); });
    contagem.classList.add("ao-vivo");
    contagem.setAttribute("href", "#" + cartaoHoje.id);
    num.textContent = "Hoje";
    rot.innerHTML = cartaoHoje.dataset.titulo + "<small>toque para ver o roteiro do dia</small>";
  } else if (hoje > app.dataset.fim) {
    num.textContent = "♥";
    rot.innerHTML = "Viagem concluída<small>que venha a próxima!</small>";
  }
  $$("[data-so-antes]").forEach(function (el) { el.hidden = faltam <= 0; });

  // ---------- Menu lateral (três pontinhos) ----------
  var gaveta = $("#gaveta"), fundo = $("#gaveta-fundo"), btnMenu = $("#btn-menu"), btnFechar = $("#btn-fechar");
  function abrirMenu() {
    gaveta.hidden = false; fundo.hidden = false;
    requestAnimationFrame(function () { gaveta.classList.add("aberta"); fundo.classList.add("aberta"); });
    btnMenu.setAttribute("aria-expanded", "true");
    var atual = $('.gaveta-lista a[aria-current="true"]') || $(".gaveta-busca");
    setTimeout(function () { atual.focus(); }, 60);
  }
  function fecharMenu(devolverFoco) {
    if (gaveta.hidden) return;
    gaveta.classList.remove("aberta"); fundo.classList.remove("aberta");
    btnMenu.setAttribute("aria-expanded", "false");
    setTimeout(function () { gaveta.hidden = true; fundo.hidden = true; }, semMovimento ? 0 : 300);
    if (devolverFoco) btnMenu.focus();
  }
  btnMenu.addEventListener("click", function () { gaveta.hidden ? abrirMenu() : fecharMenu(true); });
  btnFechar.addEventListener("click", function () { fecharMenu(true); });
  fundo.addEventListener("click", function () { fecharMenu(true); });
  gaveta.addEventListener("click", function (ev) { if (ev.target.closest("a")) fecharMenu(false); });
  document.addEventListener("keydown", function (ev) { if (ev.key === "Escape") fecharMenu(true); });

  // ---------- Páginas (troca pelo endereço #) ----------
  var paginas = $$(".pagina");
  var dias = $$("#roteiro .dia");
  var tituloAtual = $("#pagina-atual");
  function diaPadrao() { return cartaoHoje || dias[0]; }
  function mostrarDia(dia) {
    dias.forEach(function (d) { d.classList.toggle("ativo", d === dia); });
    $$(".dia-chip, .gaveta-dia").forEach(function (c) {
      c.setAttribute("aria-current", String(c.getAttribute("href") === "#" + dia.id));
    });
    var chip = $('.dia-chip[href="#' + dia.id + '"]');
    if (chip) chip.parentElement.scrollLeft = chip.offsetLeft - chip.parentElement.offsetLeft - 16;
  }
  function rota() {
    var h = decodeURIComponent(location.hash.slice(1)) || "inicio";
    var alvo = null;
    try { alvo = document.getElementById(h); } catch (e) { alvo = null; }
    var pag = alvo && (alvo.classList.contains("pagina") ? alvo : alvo.closest(".pagina"));
    if (!pag) { pag = $("#inicio"); alvo = null; }
    paginas.forEach(function (p) { p.classList.toggle("ativa", p === pag); });
    tituloAtual.textContent = pag.id === "inicio" ? "" : pag.dataset.titulo;
    document.title = (pag.id === "inicio" ? "" : pag.dataset.titulo + " · ") + "Roteiro Uruguai e Argentina";
    $$(".gaveta-lista a").forEach(function (a) { a.setAttribute("aria-current", String(a.dataset.pagina === pag.id)); });
    if (pag.id === "roteiro") {
      mostrarDia(alvo && alvo.classList.contains("dia") ? alvo : diaPadrao());
    } else {
      $$(".gaveta-dia").forEach(function (c) { c.setAttribute("aria-current", "false"); });
    }
    if (alvo && alvo.tagName === "DETAILS") alvo.open = true;
    if (alvo && alvo.classList.contains("rest") && alvo.hidden) {
      filtro = { cidade: "todas", cat: "todas" };
      aplicarFiltro();
    }
    if (pag.id === "buscar") buscar();
    var rolarAte = alvo && alvo !== pag && !alvo.classList.contains("dia") ? alvo : null;
    if (rolarAte) {
      requestAnimationFrame(function () {
        rolarAte.scrollIntoView({ block: "start" });
        rolarAte.classList.remove("destaque");
        void rolarAte.offsetWidth;
        rolarAte.classList.add("destaque");
      });
    } else {
      window.scrollTo(0, 0);
    }
  }
  window.addEventListener("hashchange", rota);

  // ---------- Onde comer: filtros ----------
  var filtro = guardar.ler("roteiro-filtro", { cidade: "todas", cat: "todas" });
  var cards = $$(".rest");
  var contador = $("#contador-rest"), vazio = $("#rest-vazio");
  function aplicarFiltro() {
    var n = 0;
    cards.forEach(function (c) {
      var ok = (filtro.cidade === "todas" || c.dataset.cidade === filtro.cidade) &&
               (filtro.cat === "todas" || c.dataset.cat === filtro.cat);
      c.hidden = !ok;
      if (ok) n++;
    });
    $$(".chip[data-filtro]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(filtro[b.dataset.filtro] === b.dataset.valor));
    });
    if (contador) contador.textContent = n === 1 ? "1 lugar" : n + " lugares";
    if (vazio) vazio.hidden = n > 0;
  }
  $$(".chip[data-filtro]").forEach(function (b) {
    b.addEventListener("click", function () {
      filtro[b.dataset.filtro] = b.dataset.valor;
      guardar.gravar("roteiro-filtro", filtro);
      aplicarFiltro();
    });
  });
  aplicarFiltro();

  // ---------- Buscar ----------
  var fonteIndice = $("#indice");
  var BUSCA = fonteIndice ? JSON.parse(fonteIndice.textContent) : null;
  var ROTULO_K = { parada: "No roteiro", ponto: "Ponto turístico", rest: "Onde comer", cultura: "Cultura", extra: "Extra dos vídeos", compra: "Compras" };
  var ORDEM_K = { parada: 0, extra: 1, ponto: 2, rest: 3, cultura: 4, compra: 5 };
  var estado = { q: "", dia: cartaoHoje ? cartaoHoje.id : dias[0].id, diaAuto: true, cidade: "todas", tipo: "tudo" };
  var campo = $("#busca-q"), resultados = $("#resultados"), contBusca = $("#busca-contador"), limpar = $("#busca-limpar");
  var LIMITE = 40, mostrarTodos = false;

  function normalizar(s) {
    return String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  }
  function esc(s) {
    return String(s || "").replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; });
  }
  function icone(nome) {
    return '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + (BUSCA.icones[nome] || "") + "</svg>";
  }
  function destacar(texto, termos) {
    var html = esc(texto);
    termos.forEach(function (t) {
      if (t.length < 2) return;
      var re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
      html = html.replace(re, "<mark>$1</mark>");
    });
    return html.replace(/\bn\/c\b/g, '<abbr class="nc" title="não confirmado">n/c</abbr>');
  }
  function resumir(texto, max) {
    return texto.length > max ? texto.slice(0, max).replace(/\s+\S*$/, "") + "…" : texto;
  }
  if (BUSCA) {
    BUSCA.itens.forEach(function (it) {
      it._txt = normalizar([it.titulo, it.texto, it.meta, BUSCA.tipos[it.t], ROTULO_K[it.k], BUSCA.cidades[it.c]].join(" "));
    });
  }
  function marcarChips() {
    $$(".chip[data-busca]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(estado[b.dataset.busca] === b.dataset.valor));
    });
    if (limpar) limpar.hidden = !estado.q;
  }
  function buscar() {
    if (!BUSCA || !resultados) return;
    marcarChips();
    var termos = normalizar(estado.q).split(/\s+/).filter(Boolean);
    var achados = BUSCA.itens.filter(function (it) {
      if (estado.dia !== "todos" && (it.d || []).indexOf(estado.dia) < 0) return false;
      if (estado.cidade !== "todas" && it.c !== estado.cidade) return false;
      if (estado.tipo !== "tudo" && it.t !== estado.tipo) return false;
      return termos.every(function (t) { return it._txt.indexOf(t) >= 0; });
    });
    achados.sort(function (a, b) { return (ORDEM_K[a.k] - ORDEM_K[b.k]) || (a.o - b.o); });
    var partes = [];
    if (estado.dia !== "todos") partes.push(BUSCA.dias[estado.dia]);
    if (estado.cidade !== "todas") partes.push(BUSCA.cidades[estado.cidade]);
    if (estado.tipo !== "tudo") partes.push(BUSCA.tipos[estado.tipo]);
    if (estado.q) partes.push("“" + estado.q + "”");
    contBusca.textContent = (achados.length === 1 ? "1 resultado" : achados.length + " resultados") + (partes.length ? " · " + partes.join(" · ") : "");
    if (!achados.length) {
      resultados.innerHTML = '<p class="vazio">Nada encontrado. Tentem outra palavra ou escolham “Todos os dias”.</p>';
      return;
    }
    var lista = mostrarTodos ? achados : achados.slice(0, LIMITE);
    var termosBrutos = estado.q.split(/\s+/).filter(Boolean);
    resultados.innerHTML = lista.map(function (it) {
      var links = '<a class="lk" href="' + esc(it.link) + '">' + esc(it.rotulo) + icone("dir") + "</a>";
      if (it.mapa) links += '<a class="lk" href="' + esc(it.mapa) + '" target="_blank" rel="noopener">' + icone("mapa") + "Ver no mapa</a>";
      var dias = (it.d || []).map(function (d) { return BUSCA.dias[d]; }).join(", ");
      var meta = it.k === "parada" ? esc(it.meta) : esc(it.meta) + (dias ? " · " + esc(dias) : "");
      return '<article class="res" data-tipo="' + esc(it.t) + '">' +
        '<span class="bolinha" title="' + esc(BUSCA.tipos[it.t]) + '">' + icone(it.t) + "</span>" +
        '<div><p class="res-meta"><span class="res-k">' + esc(ROTULO_K[it.k]) + "</span>" + meta +
        " · " + esc(BUSCA.cidades[it.c] || "") + "</p>" +
        "<h3>" + destacar(it.titulo, termosBrutos) + "</h3>" +
        "<p>" + destacar(resumir(it.texto, 220), termosBrutos) + "</p>" +
        '<div class="links">' + links + "</div></div>" +
        (it.foto ? '<img class="mini" src="' + esc(it.foto) + '" alt="" loading="lazy">' : "") +
        "</article>";
    }).join("") + (achados.length > lista.length
      ? '<button class="chip mais" type="button" id="ver-mais">Ver mais ' + (achados.length - lista.length) + " resultados</button>" : "");
    var mais = $("#ver-mais");
    if (mais) mais.addEventListener("click", function () { mostrarTodos = true; buscar(); });
  }
  if (campo) {
    campo.addEventListener("input", function () {
      estado.q = campo.value.trim();
      if (estado.q && estado.diaAuto) { estado.dia = "todos"; estado.diaAuto = false; }
      mostrarTodos = false;
      buscar();
    });
    $$(".chip[data-busca]").forEach(function (b) {
      b.addEventListener("click", function () {
        estado[b.dataset.busca] = b.dataset.valor;
        if (b.dataset.busca === "dia") estado.diaAuto = false;
        mostrarTodos = false;
        buscar();
      });
    });
    $$("[data-sugestao]").forEach(function (b) {
      b.addEventListener("click", function () {
        campo.value = b.dataset.sugestao;
        campo.dispatchEvent(new Event("input"));
      });
    });
    limpar.addEventListener("click", function () {
      campo.value = "";
      campo.dispatchEvent(new Event("input"));
      campo.focus();
    });
    buscar();
  }

  // ---------- Conversor de moedas ----------
  var brl = $("#conv-brl"), uyu = $("#conv-uyu"), ars = $("#conv-ars");
  var tUyu = $("#taxa-uyu"), tArs = $("#taxa-ars");
  function lerNumero(s) {
    s = String(s || "").trim().replace(/\s/g, "").replace(/^R\$/, "");
    if (!s) return NaN;
    if (s.indexOf(",") >= 0) s = s.replace(/\./g, "").replace(",", ".");
    else if (/^\d{1,3}(\.\d{3})+$/.test(s)) s = s.replace(/\./g, "");
    return parseFloat(s);
  }
  function fmt(v, casas) {
    if (!isFinite(v)) return "";
    return v.toLocaleString("pt-BR", { minimumFractionDigits: casas, maximumFractionDigits: casas });
  }
  if (brl && uyu && ars && tUyu && tArs) {
    var taxas = guardar.ler("roteiro-cambio", null);
    if (taxas) { tUyu.value = fmt(taxas.uyu, 3); tArs.value = fmt(taxas.ars, 0); }
    var ultimo = "brl";
    var converter = function (origem) {
      ultimo = origem || ultimo;
      var ru = lerNumero(tUyu.value), ra = lerNumero(tArs.value);
      if (!(ru > 0) || !(ra > 0)) return;
      var reais;
      if (ultimo === "brl") reais = lerNumero(brl.value);
      else if (ultimo === "uyu") reais = lerNumero(uyu.value) * ru;
      else reais = lerNumero(ars.value) / ra;
      if (!isFinite(reais)) {
        [brl, uyu, ars].forEach(function (i) { if (i.id !== "conv-" + ultimo) i.value = ""; });
        return;
      }
      if (ultimo !== "brl") brl.value = fmt(reais, 2);
      if (ultimo !== "uyu") uyu.value = fmt(reais / ru, 0);
      if (ultimo !== "ars") ars.value = fmt(reais * ra, 0);
    };
    brl.addEventListener("input", function () { converter("brl"); });
    uyu.addEventListener("input", function () { converter("uyu"); });
    ars.addEventListener("input", function () { converter("ars"); });
    [tUyu, tArs].forEach(function (inp) {
      inp.addEventListener("input", function () {
        var ru = lerNumero(tUyu.value), ra = lerNumero(tArs.value);
        if (ru > 0 && ra > 0) guardar.gravar("roteiro-cambio", { uyu: ru, ars: ra });
        converter();
      });
    });
    converter("brl");
  }

  // ---------- Checklist com confete ----------
  function confete(el) {
    if (semMovimento) return;
    var r = el.getBoundingClientRect();
    for (var i = 0; i < 26; i++) {
      var c = document.createElement("i");
      c.className = "confete";
      c.style.left = (r.left + r.width / 2) + "px";
      c.style.top = (r.top + r.height / 2) + "px";
      c.style.background = CORES[i % CORES.length];
      var ang = Math.random() * Math.PI * 2, dist = 50 + Math.random() * 90;
      c.style.setProperty("--dx", Math.cos(ang) * dist + "px");
      c.style.setProperty("--dy", (Math.sin(ang) * dist - 40) + "px");
      c.style.setProperty("--rot", (Math.random() * 720 - 360) + "deg");
      document.body.appendChild(c);
      setTimeout(function (n) { n.remove(); }, 950, c);
    }
  }
  var marcados = guardar.ler("roteiro-checklist", {});
  var caixas = $$(".checklist input[type=checkbox]");
  var prog = $("#progresso-texto"), barra = $("#progresso-barra");
  function atualizarProgresso() {
    var feitos = caixas.filter(function (c) { return c.checked; }).length;
    if (prog) prog.textContent = feitos === caixas.length ? "Tudo pronto!" : feitos + " de " + caixas.length + " feitos";
    if (barra) barra.style.width = (caixas.length ? (100 * feitos / caixas.length) : 0) + "%";
  }
  caixas.forEach(function (c) {
    c.checked = !!marcados[c.id];
    c.addEventListener("change", function () {
      marcados[c.id] = c.checked;
      guardar.gravar("roteiro-checklist", marcados);
      atualizarProgresso();
      if (c.checked) confete(c);
    });
  });
  atualizarProgresso();

  // ---------- Copiar número de WhatsApp ----------
  $$("[data-copiar]").forEach(function (b) {
    b.addEventListener("click", function () {
      var original = b.textContent;
      var aviso = function (t) { b.textContent = t; setTimeout(function () { b.textContent = original; }, 1600); };
      var selecionar = function () {
        var alvo = b.previousElementSibling;
        if (!alvo) return;
        var r = document.createRange(); r.selectNodeContents(alvo);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
        aviso("Selecionado");
      };
      try { navigator.clipboard.writeText(b.getAttribute("data-copiar")).then(function () { aviso("Copiado"); }, selecionar); }
      catch (e) { selecionar(); }
    });
  });

  // ---------- Fogos do Réveillon ----------
  var tela = $("#fogos");
  if (tela && tela.getContext) {
    var ctx = tela.getContext("2d");
    var particulas = [], rodando = false, ultimoDisparo = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);
    var medir = function () {
      var r = tela.getBoundingClientRect();
      tela.width = Math.max(1, r.width * dpr); tela.height = Math.max(1, r.height * dpr);
    };
    var explodir = function (x, y) {
      var cor = CORES[Math.floor(Math.random() * CORES.length)];
      var n = 46 + Math.floor(Math.random() * 30);
      for (var i = 0; i < n; i++) {
        var a = (i / n) * Math.PI * 2, v = (1.6 + Math.random() * 2.6) * dpr;
        particulas.push({ x: x, y: y, vx: Math.cos(a) * v, vy: Math.sin(a) * v, vida: 1, cor: Math.random() < .2 ? "#FFFFFF" : cor });
      }
    };
    var quadro = function (t) {
      if (!rodando) return;
      if (t - ultimoDisparo > 700 + Math.random() * 600) {
        explodir(tela.width * (.12 + Math.random() * .76), tela.height * (.1 + Math.random() * .35));
        ultimoDisparo = t;
      }
      ctx.globalCompositeOperation = "destination-out";
      ctx.fillStyle = "rgba(0,0,0,.22)";
      ctx.fillRect(0, 0, tela.width, tela.height);
      ctx.globalCompositeOperation = "lighter";
      particulas = particulas.filter(function (p) {
        p.x += p.vx; p.y += p.vy; p.vy += .035 * dpr; p.vx *= .985; p.vy *= .985; p.vida -= .012;
        if (p.vida <= 0) return false;
        ctx.globalAlpha = Math.max(p.vida, 0);
        ctx.fillStyle = p.cor;
        ctx.beginPath(); ctx.arc(p.x, p.y, 1.8 * dpr, 0, Math.PI * 2); ctx.fill();
        return true;
      });
      ctx.globalAlpha = 1;
      requestAnimationFrame(quadro);
    };
    var estatico = function () {
      medir();
      [[.2, .25], [.5, .15], [.8, .3]].forEach(function (p) { explodir(tela.width * p[0], tela.height * p[1]); });
      particulas.forEach(function (p) {
        for (var k = 0; k < 28; k++) { p.x += p.vx; p.y += p.vy; p.vy += .035 * dpr; }
        ctx.globalAlpha = .8; ctx.fillStyle = p.cor;
        ctx.beginPath(); ctx.arc(p.x, p.y, 1.8 * dpr, 0, Math.PI * 2); ctx.fill();
      });
      particulas = [];
    };
    window.addEventListener("resize", medir);
    if (!("IntersectionObserver" in window)) {
      estatico();
    } else {
      new IntersectionObserver(function (en) {
        var visivel = en[0].isIntersecting;
        if (visivel) medir();
        if (visivel && semMovimento) { estatico(); return; }
        if (visivel && !rodando) { rodando = true; requestAnimationFrame(quadro); }
        if (!visivel) rodando = false;
      }).observe(tela);
    }
  }

  // Mostra a página do endereço atual depois que tudo está pronto.
  rota();
  // Ao abrir um link direto para um trecho (ex.: #mvd-b), rola de novo quando as fotos terminam de carregar.
  window.addEventListener("load", function () {
    var el = location.hash.length > 1 ? document.getElementById(decodeURIComponent(location.hash.slice(1))) : null;
    if (el && !el.classList.contains("pagina") && !el.classList.contains("dia")) el.scrollIntoView({ block: "start" });
  });
})();

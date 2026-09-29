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

  // ---------- Contagem regressiva e "hoje" ----------
  function isoLocal(d) {
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  function diasEntre(a, b) {
    return Math.round((Date.parse(b + "T12:00:00") - Date.parse(a + "T12:00:00")) / 86400000);
  }
  var hoje = isoLocal(new Date());
  var faltam = diasEntre(hoje, app.dataset.inicio);
  var contagem = $("#contagem"), num = $("#contagem-num"), rot = $("#contagem-rot");
  if (faltam > 0) {
    num.textContent = String(faltam);
    rot.innerHTML = (faltam === 1 ? "dia para" : "dias para") + " embarcar<small>26 de dezembro, Montevidéu</small>";
    $$("[data-faltam]").forEach(function (el) { el.textContent = String(faltam); });
  } else if (hoje <= app.dataset.fim) {
    var cartao = $('.dia[data-data="' + hoje + '"]');
    var chip = $('.dia-chip[data-data="' + hoje + '"]');
    if (cartao) {
      cartao.classList.add("hoje");
      if (chip) chip.classList.add("hoje");
      contagem.classList.add("ao-vivo");
      contagem.setAttribute("href", "#" + cartao.id);
      num.textContent = "Hoje";
      rot.innerHTML = cartao.dataset.titulo + "<small>toque para ver o roteiro do dia</small>";
    }
  } else {
    num.textContent = "♥";
    rot.innerHTML = "Viagem concluída<small>que venha a próxima!</small>";
  }
  $$("[data-so-antes]").forEach(function (el) { el.hidden = faltam <= 0; });

  // ---------- Menu: seção atual ----------
  var links = $$(".menu a");
  if ("IntersectionObserver" in window && links.length) {
    var porId = {};
    links.forEach(function (a) { porId[a.getAttribute("href").slice(1)] = a; });
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (en) {
        if (!en.isIntersecting) return;
        var a = porId[en.target.dataset.menu || en.target.id];
        links.forEach(function (l) { l.removeAttribute("aria-current"); });
        if (!a) return;
        a.setAttribute("aria-current", "true");
        var menu = a.parentElement;
        menu.scrollTo({ left: a.offsetLeft - menu.clientWidth / 2 + a.clientWidth / 2, behavior: semMovimento ? "auto" : "smooth" });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    $$("main > section[id]").forEach(function (s) { obs.observe(s); });
  }

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
    if (semMovimento || !("IntersectionObserver" in window)) {
      estatico();
    } else {
      medir();
      new IntersectionObserver(function (en) {
        var visivel = en[0].isIntersecting;
        if (visivel && !rodando) { rodando = true; requestAnimationFrame(quadro); }
        if (!visivel) rodando = false;
      }).observe(tela);
    }
  }
})();

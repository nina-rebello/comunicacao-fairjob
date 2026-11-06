// Lê o carrossel renderizado e descreve cada slide em JSON (fundo, formas, imagens e blocos de texto),
// para o montar-pptx.py recriar tudo como elementos editáveis no Canva.
// Uso: node posts/05-fairhealth/canva/extrair.js
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const pasta = __dirname;
  const html = path.resolve(pasta, '..', 'carrossel-5.html');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 3 });
  await page.goto('file://' + html);
  // versão para o Canva: as tags de vidro viram pílulas lisas (desfoque e sombra não viram forma editável)
  await page.addStyleTag({ content: `
    .vidro { box-shadow: none !important; background: #F1FAF8 !important; border: 2px solid #9ED9CF !important; }
    .vidro::before, .vidro::after, .vidro i { display: none !important; }
    .botao2 { box-shadow: none !important; }` });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => [...document.images].every((i) => i.complete && i.naturalWidth > 0));

  // cada ícone SVG vira um PNG transparente
  const svgs = await page.$$('.slide svg');
  for (let i = 0; i < svgs.length; i++) {
    await svgs[i].evaluate((el, n) => el.setAttribute('data-icone', String(n)), i);
    await svgs[i].screenshot({ path: path.join(pasta, `icone-${i}.png`), omitBackground: true });
  }

  const dados = await page.evaluate(() => {
    const px = (v) => parseFloat(v) || 0;
    const vazio = (c) => !c || c === 'transparent' || /rgba\(.*,\s*0\)$/.test(c);
    const slides = [];
    for (const s of document.querySelectorAll('.slide')) {
      const base = s.getBoundingClientRect();
      const caixa = (r) => ({ x: r.left - base.left, y: r.top - base.top, w: r.width, h: r.height });
      const out = { fundo: getComputedStyle(s).backgroundColor, formas: [], imagens: [], textos: [] };

      for (const el of s.querySelectorAll('*')) {
        const cs = getComputedStyle(el);
        if (cs.display === 'none' || cs.visibility === 'hidden') continue;
        if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') continue;
        const r = el.getBoundingClientRect();
        if (r.width === 0 || r.height === 0) continue;
        const b = caixa(r);
        if (el.tagName === 'IMG') { out.imagens.push({ ...b, src: el.getAttribute('src') }); continue; }
        if (el.tagName.toLowerCase() === 'svg') { out.imagens.push({ ...b, icone: el.getAttribute('data-icone') }); continue; }
        const raio = Math.min(px(cs.borderTopLeftRadius), b.h / 2, b.w / 2);
        const lados = ['Top', 'Right', 'Bottom', 'Left']
          .map((l) => ({ l, w: px(cs[`border${l}Width`]), c: cs[`border${l}Color`], st: cs[`border${l}Style`] }))
          .filter((x) => x.w > 0 && x.st !== 'none' && !vazio(x.c));
        const todos = lados.length === 4 && lados.every((x) => x.c === lados[0].c && x.w === lados[0].w);
        if (!vazio(cs.backgroundColor) || todos) {
          out.formas.push({ ...b, raio, fundo: vazio(cs.backgroundColor) ? null : cs.backgroundColor,
            borda: todos ? { w: lados[0].w, c: lados[0].c } : null });
        }
        if (!todos) for (const x of lados) {
          const t = { Top: { x: b.x, y: b.y, w: b.w, h: x.w }, Bottom: { x: b.x, y: b.y + b.h - x.w, w: b.w, h: x.w },
            Left: { x: b.x, y: b.y, w: x.w, h: b.h }, Right: { x: b.x + b.w - x.w, y: b.y, w: x.w, h: b.h } }[x.l];
          out.formas.push({ ...t, raio: 0, fundo: x.c, borda: null });
        }
      }

      // blocos de texto: nós de texto agrupados pelo ancestral não-inline mais próximo
      const blocos = new Map();
      const tw = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = tw.nextNode())) {
        if (!n.textContent.length) continue;
        if (n.parentElement.closest('script, style, svg')) continue;
        if (getComputedStyle(n.parentElement).display === 'none') continue;
        let blocoEl = n.parentElement;
        while (getComputedStyle(blocoEl).display === 'inline') blocoEl = blocoEl.parentElement;
        if (!blocos.has(blocoEl)) blocos.set(blocoEl, []);
        blocos.get(blocoEl).push(n);
      }
      for (const [el, nos] of blocos) {
        const runs = [];
        for (const t of nos) {
          const cs = getComputedStyle(t.parentElement);
          let txt = t.textContent.replace(/\s+/g, ' ');
          if (cs.textTransform === 'uppercase') txt = txt.toUpperCase();
          runs.push({ txt, cor: cs.color, peso: cs.fontWeight, italico: cs.fontStyle === 'italic', fonte: cs.fontFamily,
            tam: px(cs.fontSize), esp: cs.letterSpacing === 'normal' ? 0 : px(cs.letterSpacing) });
        }
        while (runs.length && !runs[0].txt.trim()) runs.shift();
        while (runs.length && !runs[runs.length - 1].txt.trim()) runs.pop();
        if (!runs.length) continue;
        runs[0].txt = runs[0].txt.replace(/^\s+/, '');
        runs[runs.length - 1].txt = runs[runs.length - 1].txt.replace(/\s+$/, '');
        const comTexto = nos.filter((t) => t.textContent.trim());
        const rg = document.createRange();
        rg.setStart(comTexto[0], 0);
        rg.setEnd(comTexto[comTexto.length - 1], comTexto[comTexto.length - 1].length);
        const rects = [...rg.getClientRects()].filter((r) => r.width > 0);
        const L = Math.min(...rects.map((r) => r.left)), T = Math.min(...rects.map((r) => r.top));
        const R = Math.max(...rects.map((r) => r.right)), B = Math.max(...rects.map((r) => r.bottom));
        const cs = getComputedStyle(el);
        const linhas = new Set(rects.map((r) => Math.round(r.top))).size;
        const conteudo = el.getBoundingClientRect();
        const lh = cs.lineHeight === 'normal' ? px(cs.fontSize) * 1.2 : px(cs.lineHeight);
        out.textos.push({ x: L - base.left, y: T - base.top, w: R - L, h: B - T, linhas,
          larguraBloco: conteudo.width - px(cs.paddingLeft) - px(cs.paddingRight),
          esquerdaBloco: conteudo.left + px(cs.paddingLeft) - base.left,
          alinhamento: cs.textAlign, entrelinha: lh, runs });
      }
      slides.push(out);
    }
    return slides;
  });
  fs.writeFileSync(path.join(pasta, 'slides.json'), JSON.stringify(dados, null, 1));
  await browser.close();
  console.log(dados.map((d, i) => `slide ${i + 1}: ${d.formas.length} formas, ${d.imagens.length} imagens, ${d.textos.length} textos`).join('\n'));
})();

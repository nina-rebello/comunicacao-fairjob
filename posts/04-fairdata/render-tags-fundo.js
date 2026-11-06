// Exporta só o fundo das tags (vidro + ícone, sem texto) para o texto ficar editável no Canva.
// A largura reservada para o texto é a do texto em Arial/Helvetica negrito 22 px (fonte padrão do Canva), com folga.
// Uso: node posts/04-fairdata/render-tags-fundo.js
const path = require('path');
const { chromium } = require('playwright');

// Textos atuais no Canva: "Mapa de calor", "Segurança psicológica", "COPSOQ" (medidos a 22 px sem escala, com folga). No Canva todas usam a mesma escala: 0,727 (texto 16 px).
// Para outro texto, troque a largura aqui ou passe JSON: node render-tags-fundo.js '{"t-mapa":200}'
const LARGURA_TEXTO = Object.assign({ 't-mapa': 152, 't-seg': 245, 't-copsoq': 102 }, JSON.parse(process.argv[2] || '{}'));

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 800 }, deviceScaleFactor: 3 });
  await page.goto('file://' + path.join(__dirname, 'tags-vidro.html'));
  await page.evaluate((larguras) => {
    for (const [id, w] of Object.entries(larguras)) {
      const span = document.querySelector(`#${id} span`);
      span.textContent = '';
      Object.assign(span.style, { display: 'inline-block', width: w + 'px', height: '1px' });
    }
  }, LARGURA_TEXTO);
  for (const id of Object.keys(LARGURA_TEXTO)) {
    const el = await page.$('#' + id);
    const box = await el.boundingBox();
    await el.screenshot({ path: path.join(__dirname, 'img', `tag-fundo-${id.slice(2)}.png`), omitBackground: true });
    console.log(id, Math.round(box.width), Math.round(box.height));
  }
  await browser.close();
})();

// Renderiza ecossistema-diagrama.html em PNG 2x (1720 x 820) para subir no Canva.
// Uso: node posts/01-ecossistema/render-diagrama.js [neutro|cor] [saida.png]
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const anel = process.argv[2] || 'neutro';
  const saida = process.argv[3] || path.join(__dirname, 'ecossistema-diagrama.png');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 860, height: 410 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'ecossistema-diagrama.html') + '?anel=' + anel);
  await page.waitForFunction(() => [...document.images].every((i) => i.complete && i.naturalWidth > 0));
  await page.screenshot({ path: saida });
  await browser.close();
  console.log(saida);
})();

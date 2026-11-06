// Exporta um carrossel (seções .slide de 1080x1350) em slide-N.png e num PDF para o LinkedIn.
// Uso: node posts/05-fairhealth/render.js carrossel-5.html
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const html = path.resolve(__dirname, process.argv[2]);
  const nome = path.basename(html, '.html');
  const pasta = path.join(__dirname, nome);
  fs.mkdirSync(pasta, { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + html);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => [...document.images].every((i) => i.complete && i.naturalWidth > 0));

  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(pasta, `slide-${i + 1}.png`) });
  }
  await page.pdf({ path: path.join(__dirname, `${nome}.pdf`), width: '1080px', height: '1350px', printBackground: true });
  await browser.close();
  console.log(`${slides.length} slides em ${pasta} + ${nome}.pdf`);
})();

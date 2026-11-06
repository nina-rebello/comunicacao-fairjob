// Exporta cada tag de tags-vidro.html como PNG transparente (3x) e a capa do carrossel sem as tags.
// Uso: node posts/04-fairdata/render-tags.js
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const pasta = path.join(__dirname, 'img');
  const browser = await chromium.launch();

  const page = await browser.newPage({ viewport: { width: 1200, height: 800 }, deviceScaleFactor: 3 });
  await page.goto('file://' + path.join(__dirname, 'tags-vidro.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const id of ['t-mapa', 't-seg', 't-copsoq']) {
    const el = await page.$('#' + id);
    const box = await el.boundingBox();
    await el.screenshot({ path: path.join(pasta, `tag-${id.slice(2)}.png`), omitBackground: true });
    console.log(id, Math.round(box.width), Math.round(box.height));
  }

  // capa sem as tags, para o slide duplicado no Canva
  const capa = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await capa.goto('file://' + path.join(__dirname, 'carrossel-5.html'));
  await capa.evaluate(() => document.fonts.ready);
  await capa.waitForFunction(() => [...document.images].every((i) => i.complete && i.naturalWidth > 0));
  await capa.evaluate(() => document.querySelectorAll('.tag').forEach((t) => t.remove()));
  await (await capa.$('.slide')).screenshot({ path: path.join(pasta, 'capa-sem-tags.png') });

  await browser.close();
})();

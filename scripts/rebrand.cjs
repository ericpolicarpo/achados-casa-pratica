const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../public');
let changed = 0;
function visit(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) { visit(file); continue; }
    if (!/\.(html|xml|js)$/.test(entry.name)) continue;
    const old = fs.readFileSync(file, 'utf8');
    let text = old.replaceAll('Achados Casa Prática', 'Achouê')
      .replaceAll('<strong>Achados</strong><em>Casa Prática</em>', '<strong>Achouê</strong><em>Moda, casa e achados</em>')
      .replace(/<span class="brand-mark"[^>]*>⌂<\/span>/g, '<img class="achoue-brand-icon" src="/achoue-perfil.png" alt="" width="40" height="40">');
    if (entry.name === 'index.html' && dir === root) {
      text = text.replace(/\s*<section class="intro"[\s\S]*?<\/section>\s*/, '\n');
      text = text.replace(/\s*<p class="store-disclosure">[\s\S]*?<\/p>\s*/, '\n');
      text = text.replace('<h2 id="achados-title">Encontre o seu favorito</h2>', '<h1 id="achados-title">Encontre o seu favorito</h1>');
    }
    if (entry.name === 'index.html' && dir === root && !text.includes('class="brand-socials"')) {
      text = text.replace('</footer>', '<nav class="brand-socials" aria-label="Redes sociais"><a href="https://www.tiktok.com/@achoue_" target="_blank" rel="noopener">TikTok @achoue_ ↗</a><a href="https://www.youtube.com/channel/UCce2ZJnnAQTamLO4wP4jTfQ" target="_blank" rel="noopener">YouTube Achouê ↗</a></nav></footer>');
    }
    if (text !== old) { fs.writeFileSync(file, text); changed++; }
  }
}
visit(root);
const cssPath = path.join(root, 'styles.css');
const css = fs.readFileSync(cssPath, 'utf8');
if (!css.includes('/* Achoue identity */')) {
  fs.appendFileSync(cssPath, '\n/* Achoue identity */\n.achoue-brand-icon{width:40px;height:40px;border-radius:50%;object-fit:cover}.brand-name strong{font-size:24px}.brand-name em{font-size:11px;font-style:normal}.brand-socials{display:flex;gap:18px;flex-wrap:wrap}.brand-socials a{font-size:13px}\n');
}
console.log(`Achouê: identidade aplicada em ${changed} arquivos.`);
if (!fs.readFileSync(cssPath, 'utf8').includes('/* Achoue catalog first */')) {
  fs.appendFileSync(cssPath, '\n/* Achoue catalog first */\n.storefront .catalog{padding-top:28px}.catalog-heading h1{margin:0;font-family:"Playfair Display",serif;font-size:clamp(26px,3vw,40px);line-height:1.15}\n');
}
const pricesPath = path.join(__dirname, 'prices.json');
if (fs.existsSync(pricesPath)) {
  const prices = JSON.parse(fs.readFileSync(pricesPath, 'utf8'));
  const homePath = path.join(root, 'index.html');
  let home = fs.readFileSync(homePath, 'utf8');
  for (const item of prices) {
    const block = `<div class="product-price-block"><p class="product-price">R$ ${item.value}${item.coupon ? ' <span>com cupom</span>' : ''}</p><p class="product-price-note">Preço anunciado em ${item.checked}. Variações e condições no anúncio.</p></div>`;
    home = home.replace(new RegExp(`(<article class="product-card" id="${item.id}"[\\s\\S]*?)(</article>)`), (_, card, end) => {
      card = card.replace(/<div class="product-price-block">[\s\S]*?<\/div>/g, '');
      return card.replace('<p class="product-platform">', `${block}<p class="product-platform">`) + end;
    });
    const detailPath = path.join(root, item.path.endsWith('/') ? item.path + 'index.html' : item.path);
    if (fs.existsSync(detailPath)) {
      let detail = fs.readFileSync(detailPath, 'utf8').replace(/<div class="product-price-block">[\s\S]*?<\/div>/g, '');
      detail = detail.replace(/(<p class="detail-intro">[\s\S]*?<\/p>)/, `$1${block}`);
      fs.writeFileSync(detailPath, detail);
    }
  }
  fs.writeFileSync(homePath, home);
  if (!fs.readFileSync(cssPath, 'utf8').includes('/* Achoue prices */')) {
    fs.appendFileSync(cssPath, '\n/* Achoue prices */\n.product-price-block{margin:12px 0}.product-content .product-price,.product-price{font-size:23px;font-weight:700;color:#a64427;margin:0}.product-price span{font-size:12px;font-weight:500}.product-content .product-price-note,.product-price-note{font-size:11px;line-height:1.4;color:#746e65;margin:4px 0 0}\n');
  }
  console.log(`Achouê: ${prices.length} preços consultados aplicados.`);
}

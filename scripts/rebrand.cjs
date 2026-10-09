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

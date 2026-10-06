const filterButtons = document.querySelectorAll('.filter-chip');
const productCards = [...document.querySelectorAll('.product-card')];
const searchInput = document.querySelector('#product-search');
const resultCount = document.querySelector('#catalog-results');
const emptyMessage = document.querySelector('#catalog-empty');
let activeFilter = 'todos';
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

function updateCatalog() {
  const query = normalize(searchInput?.value.trim() || '');
  const terms = query.split(/\s+/).filter(Boolean);
  let visible = 0;
  productCards.forEach(card => {
    const categoryMatches = activeFilter === 'todos' || card.dataset.category.split(' ').includes(activeFilter);
    const text = normalize(card.querySelector('.product-content').textContent);
    const matches = categoryMatches && terms.every(term => text.includes(term));
    card.classList.toggle('is-hidden', !matches);
    if (matches) visible++;
  });
  if (resultCount) resultCount.textContent = query || activeFilter !== 'todos' ? `${visible} ${visible === 1 ? 'produto encontrado' : 'produtos encontrados'}` : 'Explore nossa seleção';
  if (emptyMessage) emptyMessage.hidden = visible !== 0;
}
filterButtons.forEach(button => button.addEventListener('click', () => {
  activeFilter = button.dataset.filter;
  filterButtons.forEach(item => {
    const selected = item === button;
    item.classList.toggle('is-active', selected);
    item.setAttribute('aria-pressed', String(selected));
  });
  updateCatalog();
}));
searchInput?.addEventListener('input', updateCatalog);
updateCatalog();

document.querySelectorAll('.product-card img').forEach(img => {
  const showFallback = () => {
    img.hidden = true;
    const link = img.closest('.product-image-wrap');
    if (!link || link.querySelector('.image-fallback')) return;
    const message = document.createElement('span');
    message.className = 'image-fallback';
    message.textContent = 'Veja a imagem no Mercado Livre ↗';
    link.append(message);
  };
  img.addEventListener('error', showFallback, {once:true});
  if (img.complete && img.naturalWidth === 0) showFallback();
});

const toast = document.querySelector('.toast');
document.querySelector('#share-storefront')?.addEventListener('click', async () => {
  const shareData = {title:'Achados Casa Prática',text:'Achados úteis para casa e rotina, disponíveis no Mercado Livre:',url:'https://achadoscasapratica.netlify.app/'};
  try {
    if (navigator.share) await navigator.share(shareData);
    else {
      await navigator.clipboard.writeText(`${shareData.text} ${shareData.url}`);
      toast.textContent = 'Mensagem e link copiados.';
    }
  } catch (error) {
    if (error.name === 'AbortError') return;
    toast.textContent = `Copie este endereço: ${shareData.url}`;
  }
  if (!toast.textContent) return;
  toast.classList.add('show');
  window.setTimeout(() => toast.classList.remove('show'), 2800);
});

const grid = document.querySelector('.product-grid');
const orderSelect = document.querySelector('#product-order');
orderSelect?.addEventListener('change', () => {
  const ordered = orderSelect.value === 'az' ? [...productCards].sort((a,b) => a.querySelector('h3').textContent.localeCompare(b.querySelector('h3').textContent, 'pt-BR')) : productCards;
  ordered.forEach(card => grid.append(card));
});
document.querySelector('#catalog-reset')?.addEventListener('click', () => {
  searchInput.value = '';
  activeFilter = 'todos';
  filterButtons.forEach(button => {
    const selected = button.dataset.filter === 'todos';
    button.classList.toggle('is-active', selected);
    button.setAttribute('aria-pressed', String(selected));
  });
  updateCatalog();
  searchInput.focus();
});

#!/usr/bin/env python3
"""Generate static, product-first category guides from confirmed storefront items."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
BASE = "https://achadoscasapratica.netlify.app"
CATEGORY_IMAGES = {
    "cozinha": "potes-despensa-pequena",
    "banheiro": "organizar-banheiro-pequeno",
    "ferramentas": "soquetes-catraca-ou-impacto",
}

GUIDES = [
    {
        "slug": "cozinha",
        "title": "Utensílios e potes para cozinha prática",
        "description": "Compare utensílios, potes de vidro e plástico e canecas para organizar a cozinha. Confira cada anúncio e compre no Mercado Livre.",
        "lead": "Quatro ideias para preparar, guardar e aproveitar melhor os espaços da cozinha. Veja o que muda entre as opções antes de escolher.",
        "checklist": [
            "Para utensílios, confira quantidade de peças, material e instruções de uso informadas pelo vendedor.",
            "Para potes, compare material, capacidade, formato e tipo de tampa. Confirme no anúncio se atendem ao uso que você pretende.",
            "Para canecas, veja a quantidade de peças, dimensões e cuidados de limpeza descritos no anúncio.",
        ],
        "products": [
            ("Kit de utensílios de silicone", "12 peças com cabo de madeira.", "06-utensilios-silicone.webp", "https://meli.la/12Ji2Wy"),
            ("Potes plásticos com tampa trava", "Kit com 10 potes de 750 ml.", "04-potes-plasticos.webp", "https://meli.la/2CTNSsV"),
            ("Potes de vidro com tampa de bambu", "Kit com 10 peças.", "05-potes-hermeticos.webp", "https://meli.la/2PAWrD6"),
            ("Canecas de cappuccino em vidro", "Jogo com 6 peças.", "03-canecas-cappuccino.webp", "https://meli.la/2aALM9Z"),
        ],
    },
    {
        "slug": "banheiro",
        "title": "Organizadores e tapetes para banheiro",
        "description": "Veja organizadores transparentes e tapetes para banheiro. Compare medidas, materiais e condições diretamente nos anúncios do Mercado Livre.",
        "lead": "Organizadores e tapetes são duas formas de começar pelo que você vê e usa todos os dias. Compare tamanho e material antes de decidir.",
        "checklist": [
            "Meça a bancada e confira as dimensões dos organizadores no anúncio.",
            "Compare o tamanho, material e as instruções de cuidado do tapete com o espaço do seu banheiro.",
            "Veja avaliações do vendedor, frete e regras de devolução aplicáveis antes da compra.",
        ],
        "products": [
            ("Organizadores transparentes", "Trio para algodão, cotonetes e acessórios.", "02-organizadores-banheiro.webp", "https://meli.la/2AuP2Pv"),
            ("Tapete de banheiro cinza", "Modelo de 60 × 40 cm.", "07-tapete-60x40.webp", "https://meli.la/1hfrGJ3"),
            ("Jogo de tapetes marrons", "Kit com 3 peças.", "08-kit-tapetes.webp", "https://meli.la/2ju9fHa"),
        ],
    },
    {
        "slug": "ferramentas",
        "title": "Jogos de soquetes para reparos domésticos",
        "description": "Compare um kit de soquetes com catraca e soquetes longos de impacto. Confira medidas e compatibilidade nos anúncios do Mercado Livre.",
        "lead": "Dois conjuntos de soquetes para finalidades diferentes. Verifique o encaixe e as medidas exigidas pela tarefa antes de abrir o carrinho.",
        "checklist": [
            "Compare quantidade de peças, medidas e tipo de encaixe descritos em cada anúncio.",
            "Confirme compatibilidade com suas ferramentas e se o modelo é indicado para o uso pretendido.",
            "Consulte vendedor, avaliações, prazo, preço e regras de devolução na plataforma.",
        ],
        "products": [
            ("Kit de soquetes com catraca", "40 peças em maleta.", "01-kit-soquetes.webp", "https://meli.la/19jjDP5"),
            ("Soquetes longos de impacto", "20 peças, encaixe de 1/2, conforme o anúncio.", "15-soquetes-impacto.webp", "https://meli.la/1UnbxeB"),
        ],
    },
]

RELATED_ARTICLE = {
    "cozinha": ("/blog/potes-despensa-pequena.html", "Como escolher potes para despensa"),
    "banheiro": ("/blog/organizar-banheiro-pequeno.html", "Como organizar banheiro pequeno"),
    "ferramentas": ("/blog/soquetes-catraca-ou-impacto.html", "Soquetes manuais ou de impacto?"),
}

SEO_TITLES = {
    "cozinha": "Cozinha: utensílios e potes | Achados Casa Prática",
    "banheiro": "Banheiro: organizadores e tapetes | Achados Casa Prática",
    "ferramentas": "Soquetes e ferramentas | Achados Casa Prática",
}


def render_card(product):
    name, detail, image, link = map(escape, product)
    return f'''<article class="guide-card">
      <a href="{link}" target="_blank" rel="sponsored nofollow noopener" aria-label="Ver {name} no Mercado Livre">
        <img src="/product-images/{image}" alt="{name}" loading="lazy" />
      </a>
      <div class="guide-card-copy"><h3>{name}</h3><p>{detail}</p>
        <p class="product-platform">Disponível no Mercado Livre</p><a class="product-link" href="{link}" target="_blank" rel="sponsored nofollow noopener">Ver no Mercado Livre <span>↗</span></a>
      </div>
    </article>'''


def render(guide):
    slug = guide["slug"]
    title = escape(guide["title"])
    description = escape(guide["description"])
    lead = escape(guide["lead"])
    social_image = f"{BASE}/blog-images/{CATEGORY_IMAGES[slug]}.webp"
    items = "\n".join(render_card(p) for p in guide["products"])
    tips = "\n".join(f"<li>{escape(tip)}</li>" for tip in guide["checklist"])
    other = " ".join(
        f'<a href="/{g["slug"]}.html">{escape(g["slug"].title())}</a>'
        for g in GUIDES if g["slug"] != slug
    )
    related_url, related_label = RELATED_ARTICLE[slug]
    return f'''<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#f8f5ef" />
    <meta name="robots" content="max-image-preview:large" />
    <meta name="description" content="{description}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Achados Casa Prática" />
    <meta property="og:title" content="{title} | Achados Casa Prática" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="{BASE}/{slug}.html" />
    <meta property="og:image" content="{social_image}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title} | Achados Casa Prática" />
    <meta name="twitter:description" content="{description}" />
    <meta name="twitter:image" content="{social_image}" />
    <link rel="canonical" href="{BASE}/{slug}.html" />
    <link rel="alternate" type="application/rss+xml" title="Guias Achados Casa Prática" href="{BASE}/feed.xml" />
    <title>{SEO_TITLES[slug]}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="/styles.css" />
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="/" aria-label="Achados Casa Prática, início"><span class="brand-mark" aria-hidden="true">⌂</span><span class="brand-name"><strong>Achados</strong><em>Casa Prática</em></span></a>
      <nav class="top-nav" aria-label="Navegação principal"><a href="/">Todos os produtos</a><a href="/#como-funciona">Como funciona</a></nav>
      <a class="header-back" href="/">← Voltar à vitrine</a>
    </header>
    <main class="guide-main">
      <nav class="breadcrumbs" aria-label="Você está aqui"><a href="/">Vitrine</a><span>›</span><span>{escape(slug.title())}</span></nav>
      <div class="guide-heading"><p class="eyebrow">Achados por ambiente</p><h1>{title}</h1><p>{lead}</p>
        <p class="guide-disclosure">Curadoria independente com links de afiliado. Podemos receber comissão sem custo extra para você. A compra acontece no Mercado Livre.</p></div>
      <section class="guide-products" aria-labelledby="guide-products-title"><h2 id="guide-products-title">Produtos da seleção</h2><div class="guide-grid">{items}</div></section>
      <section class="guide-advice" aria-labelledby="guide-advice-title"><h2 id="guide-advice-title">Antes de escolher</h2><ul>{tips}</ul><p>Esta página não substitui o anúncio. Confira preço, disponibilidade, frete, vendedor e condições aplicáveis de devolução no Mercado Livre.</p></section>
      <nav class="guide-related" aria-label="Outras seleções"><strong>Veja também</strong> <a href="{related_url}">{related_label}</a> {other} <a href="/">Todos os 15 achados</a></nav>
    </main>
    <footer class="site-footer"><span>⌂ <strong>Achados Casa Prática</strong></span><p>Curadoria independente · Links de afiliado · Compra no Mercado Livre</p><a href="/">Voltar à vitrine ↑</a></footer>
  </body>
</html>
'''


def main():
    home = (PUBLIC / "index.html").read_text(encoding="utf-8")
    for guide in GUIDES:
        for _, _, image, link in guide["products"]:
            assert link in home, f"Link ausente na vitrine: {link}"
            assert (PUBLIC / "product-images" / image).is_file(), image
        path = PUBLIC / f'{guide["slug"]}.html'
        path.write_text(render(guide), encoding="utf-8")
        print(path)


if __name__ == "__main__":
    main()

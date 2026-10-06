#!/usr/bin/env python3
"""Build a small, honest editorial blog and public RSS feed for the storefront."""
from email.utils import format_datetime
from html import escape
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
BLOG = PUBLIC / "blog"
BASE = "https://achadoscasapratica.netlify.app"
PUBLISHED = datetime(2026, 10, 3, 10, 13, tzinfo=timezone(timedelta(hours=-3)))

ARTICLES = [
    {
        "slug": "potes-despensa-pequena",
        "title": "Potes para despensa pequena: como escolher sem comprar a mais",
        "seo_title": "Como escolher potes para despensa | Achados Casa Prática",
        "description": "Meça a prateleira, compare vidro e plástico e escolha potes pela rotina. Guia prático com critérios de compra e links para conferir os anúncios.",
        "lead": "Antes de comprar um conjunto inteiro, descubra o que precisa caber nos potes — e onde os potes vão caber.",
        "image": "05-potes-hermeticos.webp",
        "image_alt": "Conjuntos de potes de vidro e de plástico sobre bancadas de cozinha",
        "topic": "Cozinha",
        "category": "/cozinha.html",
        "products": [
            ("Potes de vidro com tampa de bambu", "05-potes-hermeticos.webp", "https://meli.la/2PAWrD6", "Confira dimensões e tipo de tampa no anúncio."),
            ("Potes plásticos com tampa trava", "04-potes-plasticos.webp", "https://meli.la/2CTNSsV", "Kit anunciado com 10 potes de 750 ml; confirme medidas."),
        ],
        "source": ("Serious Eats — critérios para potes de mantimentos", "https://www.seriouseats.com/best-dry-food-storage-containers-8421211"),
        "body": """
          <h2>1. Comece pela prateleira, não pela foto do conjunto</h2>
          <p>Meça a largura, a profundidade e a altura livres da prateleira. Reserve espaço para pegar o pote sem retirar todos os outros. Depois anote o que você realmente guarda: pequenas porções, ingredientes de uso diário ou pacotes maiores. Comprar dez recipientes iguais antes de mapear essas necessidades pode deixar unidades sem função e armários mais cheios.</p>
          <p>Uma lista simples já ajuda: escreva o nome do mantimento, a quantidade que costuma comprar e onde ele fica hoje. Se alguns itens ainda cabem bem na embalagem original, talvez não seja necessário transferi-los. A organização útil é aquela que facilita encontrar e repor, não a que apenas uniformiza a fotografia.</p>
          <h2>2. Compare formato, capacidade e abertura</h2>
          <p>O volume anunciado não informa sozinho se o pote cabe no armário: dois recipientes de capacidade parecida podem ter alturas e larguras diferentes. Confira as medidas de cada peça e da prateleira. Potes baixos podem servir melhor a armários com pouca altura; recipientes com abertura ampla podem facilitar o uso de uma colher medidora. Se pretende empilhar, confirme se o fabricante informa essa possibilidade.</p>
          <p>O kit plástico que aparece nesta vitrine informa 10 potes de 750 ml; essa informação ajuda a começar a comparação, mas não substitui as dimensões de cada peça. Já um conjunto de vidro com tampa de bambu pode ter proporções diferentes. Consulte as especificações atuais de ambos os anúncios antes de comprar.</p>
          <h2>3. Vidro ou plástico? Decida pela sua rotina</h2>
          <p>O vidro permite ver o conteúdo e pode ser interessante para uma bancada onde os potes ficam à mostra, mas peso e risco de quebra importam em prateleiras altas ou no uso por crianças. O plástico costuma ser mais leve; avalie no anúncio o material, as instruções de lavagem e a indicação de contato com alimentos para o uso pretendido. Não presuma que qualquer pote pode ir ao forno, freezer, micro-ondas ou lava-louças.</p>
          <p>O tipo de tampa também merece atenção. Veja como ela fecha, se há vedação descrita e quais cuidados são indicados. A palavra “hermético” no título de um anúncio não substitui a leitura das especificações do modelo nem é garantia universal para todo alimento ou condição de armazenamento.</p>
          <h2>4. Faça uma escolha pequena e verificável</h2>
          <ol><li>Liste os itens que precisam mesmo de recipiente.</li><li>Meça armário e espaço de abertura da porta.</li><li>Compare as dimensões dos potes, não só o número de unidades.</li><li>Leia instruções de uso e limpeza e confira vendedor, entrega e preço atual no anúncio.</li></ol>
          <p>Se ainda estiver em dúvida, teste a lógica da organização no papel antes de comprar. Uma compra menor e mais adequada ao espaço pode ser mais útil do que preencher todas as prateleiras com peças novas. Veja também a <a href="/cozinha.html">seleção de cozinha</a> para comparar as opções exibidas na vitrine.</p>
        """,
    },
    {
        "slug": "organizar-banheiro-pequeno",
        "title": "Como organizar banheiro pequeno sem encher a bancada",
        "seo_title": "Banheiro pequeno: como organizar | Achados Casa Prática",
        "description": "Um passo a passo para separar itens diários, medir a bancada e escolher organizadores e tapetes sem atrapalhar a circulação do banheiro.",
        "lead": "Uma bancada livre pode funcionar melhor do que muitas caixas bonitas. Comece pelos objetos que você usa todos os dias.",
        "image": "02-organizadores-banheiro.webp",
        "image_alt": "Organizadores transparentes e tapete cinza para banheiro",
        "topic": "Banheiro",
        "category": "/banheiro.html",
        "products": [
            ("Trio de organizadores transparentes", "02-organizadores-banheiro.webp", "https://meli.la/2AuP2Pv", "Para pequenos acessórios; verifique as dimensões."),
            ("Tapete de banheiro 60 × 40 cm", "07-tapete-60x40.webp", "https://meli.la/1hfrGJ3", "Meça o espaço livre antes de escolher."),
        ],
        "source": ("CASACOR — dicas para organizar a bancada do banheiro", "https://casacor.com.br/pt-BR/noticias/decoracao/5-dicas-praticas-para-organizar-a-bancada-do-banheiro"),
        "body": """
          <h2>1. Deixe à vista apenas o que entra na rotina</h2>
          <p>Separe os itens em três grupos: uso diário, uso ocasional e estoque. Os de uso diário precisam estar acessíveis; os demais podem ir para uma gaveta ou prateleira, se houver. Isso não exige comprar nada. Antes de escolher organizadores, teste a bancada sem embalagens vazias e produtos que você não usa naquela área.</p>
          <p>Uma boa pergunta é: “consigo limpar a pia sem mover cinco objetos?” Se a resposta for não, tente reduzir o número de itens expostos. O objetivo é facilitar o uso e a limpeza, não criar um novo lugar para acumular pequenos frascos.</p>
          <h2>2. Meça a superfície e pense em zonas</h2>
          <p>Anote a área livre ao lado da cuba, a distância da torneira e a abertura de portas ou gavetas. Reserve uma zona para sabonete e cuidados básicos, outra para pequenos acessórios e um caminho livre para usar a pia. Um trio de potes transparentes pode agrupar algodão e cotonetes, mas só vale a pena se couber sem bloquear a torneira ou a área de apoio.</p>
          <p>Antes de escolher o trio desta vitrine, confira medidas e material nas especificações do vendedor. Também avalie como o organizador será limpo e se as tampas são práticas para a frequência de uso. Pequenos objetos muito perto de respingos exigem mais atenção à limpeza.</p>
          <h2>3. O chão também precisa de medida</h2>
          <p>Um tapete deve caber na área escolhida sem travar a porta nem atrapalhar a circulação. O modelo individual exibido aqui é anunciado com 60 × 40 cm, mas a posição ideal depende do desenho do banheiro. Meça a área livre e observe, no anúncio, material, base e orientações de lavagem. Evite deixar tapetes úmidos acumulados no chão e siga os cuidados informados pelo fabricante.</p>
          <p>Um kit de três peças pode parecer interessante para diferentes áreas, mas um banheiro compacto talvez não tenha espaço para todas. Compare o que será realmente usado com a <a href="/banheiro.html">seleção completa para banheiro</a>, que traz as opções disponíveis na vitrine.</p>
          <h2>4. Mantenha uma revisão simples</h2>
          <ol><li>Retire embalagens vazias e itens fora de uso.</li><li>Deixe apenas o essencial na bancada.</li><li>Meça antes de comprar organizadores ou tapetes.</li><li>Limpe a área e reveja periodicamente o que volta a se acumular.</li></ol>
          <p>É um método adaptável ao espaço, não uma promessa de transformação automática. O anúncio do Mercado Livre é a fonte atualizada para medidas, condições, preço, vendedor e devolução.</p>
        """,
    },
    {
        "slug": "soquetes-catraca-ou-impacto",
        "title": "Soquetes com catraca ou de impacto: o que conferir",
        "seo_title": "Soquetes: catraca ou impacto? | Achados Casa Prática",
        "description": "Entenda a diferença entre soquetes para uso manual e de impacto. Confira encaixe, medidas e compatibilidade antes de escolher um jogo.",
        "lead": "A primeira pergunta não é quantas peças vêm na maleta: é qual ferramenta você vai usar e de que medidas precisa.",
        "image": "01-kit-soquetes.webp",
        "image_alt": "Maleta com catraca e conjunto de soquetes longos de impacto",
        "topic": "Ferramentas",
        "category": "/ferramentas.html",
        "products": [
            ("Jogo de soquetes com catraca", "01-kit-soquetes.webp", "https://meli.la/19jjDP5", "Conjunto anunciado com 40 peças em maleta."),
            ("Soquetes longos de impacto", "15-soquetes-impacto.webp", "https://meli.la/1UnbxeB", "Conjunto anunciado com 20 peças e encaixe 1/2; confira no anúncio."),
        ],
        "source": ("GEARWRENCH — guia de soquetes de impacto", "https://www.gearwrench.com/resources/impact-products/impact-socket-guide"),
        "body": """
          <h2>1. Identifique a ferramenta antes do conjunto</h2>
          <p>Uma catraca manual e uma chave de impacto não têm a mesma forma de trabalho. Um kit com catraca pode ser interessante para quem busca acessórios para apertar ou soltar fixadores manualmente. Se você usa uma ferramenta de impacto, procure peças explicitamente classificadas pelo fabricante para esse uso e compatíveis com a ferramenta. Não assuma que os soquetes de um jogo comum foram feitos para impacto só porque encaixam.</p>
          <p>Os anúncios desta vitrine mostram um jogo de 40 peças com catraca e um conjunto de 20 soquetes longos de impacto. Isso não diz, por si só, quais medidas há dentro da maleta, nem substitui as recomendações do fabricante da sua ferramenta.</p>
          <h2>2. Confira encaixe e medida separadamente</h2>
          <p>O encaixe quadrado liga o soquete à ferramenta; a medida da boca corresponde ao fixador. São informações diferentes. O conjunto longo de impacto é anunciado com encaixe de 1/2, mas você ainda precisa verificar as medidas individuais e a compatibilidade com seu equipamento. No jogo de catraca, procure a lista completa de peças e adaptadores no anúncio.</p>
          <p>Antes de comprar, anote o fixador que pretende usar e compare essa informação com a tabela do anúncio. Se não souber a medida, não confie apenas na foto da maleta. Adaptadores podem existir, mas devem ser compatíveis com o tipo de uso e especificações das ferramentas envolvidas.</p>
          <h2>3. Comprimento e acesso fazem diferença</h2>
          <p>Soquetes longos podem ser úteis em algumas situações de acesso, mas nem sempre um comprimento maior é necessário ou conveniente. Verifique o espaço disponível ao redor do fixador e as dimensões informadas pelo fabricante. Para uso com impacto, siga também as instruções de segurança e de retenção de acessórios da ferramenta.</p>
          <p>Se a descrição do anúncio não deixar clara a compatibilidade, pergunte ao vendedor antes de comprar. Essa checagem é mais importante do que escolher pelo número de peças ou pela aparência do estojo.</p>
          <h2>Checklist antes de abrir o anúncio</h2>
          <ol><li>Qual ferramenta será usada: manual ou de impacto?</li><li>Qual o tamanho do encaixe quadrado?</li><li>Quais medidas dos fixadores precisam estar no kit?</li><li>O modelo e os acessórios têm indicação do fabricante para o uso pretendido?</li><li>O que dizem preço, frete, vendedor e condições de devolução atuais?</li></ol>
          <p>Compare as duas opções na <a href="/ferramentas.html">seleção de ferramentas</a>. Este texto oferece critérios gerais de escolha; não é teste dos produtos nem instrução profissional de reparo.</p>
        """,
    },
]


def product_card(product):
    name, image, link, note = map(escape, product)
    return f'''<div class="blog-product"><img src="/product-images/{image}" alt="{name}" loading="lazy" width="160" height="160" /><div><strong>{name}</strong><p>{note}</p><a href="{link}" target="_blank" rel="sponsored nofollow noopener">Ver no Mercado Livre ↗</a></div></div>'''


def render_article(article):
    slug = article["slug"]
    url = f"{BASE}/blog/{slug}.html"
    title = escape(article["title"])
    seo_title = escape(article["seo_title"])
    desc = escape(article["description"])
    image = f'{BASE}/blog-images/{slug}.webp'
    schema = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "mainEntityOfPage": url, "headline": article["title"],
        "description": article["description"], "image": image,
        "datePublished": PUBLISHED.isoformat(), "dateModified": PUBLISHED.isoformat(),
        "author": {"@type": "Organization", "name": "Achados Casa Prática", "url": BASE + "/"},
        "publisher": {"@type": "Organization", "name": "Achados Casa Prática", "url": BASE + "/"},
    }
    related = "".join(
        f'<a href="/blog/{escape(a["slug"])}.html">{escape(a["title"])} ↗</a>'
        for a in ARTICLES if a["slug"] != slug
    )
    source_label, source_url = article["source"]
    cards = "".join(product_card(p) for p in article["products"])
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#f8f5ef" />
  <meta name="robots" content="max-image-preview:large" />
  <title>{seo_title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" type="application/rss+xml" title="Guias Achados Casa Prática" href="{BASE}/feed.xml" />
  <meta property="og:type" content="article" /><meta property="og:site_name" content="Achados Casa Prática" />
  <meta property="og:title" content="{title}" /><meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" /><meta property="og:image" content="{image}" />
  <meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" /><meta name="twitter:image" content="{image}" />
  <script type="application/ld+json">{json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
  <header class="site-header"><a class="brand" href="/" aria-label="Achados Casa Prática, início"><span class="brand-mark" aria-hidden="true">⌂</span><span class="brand-name"><strong>Achados</strong><em>Casa Prática</em></span></a><a class="header-back" href="/blog/">← Todos os guias</a></header>
  <main class="article-main">
    <nav class="breadcrumbs" aria-label="Você está aqui"><a href="/">Vitrine</a><span>›</span><a href="/blog/">Guias</a><span>›</span><span>{escape(article["topic"])}</span></nav>
    <article class="article-page">
      <header class="article-header"><p class="eyebrow">Guia de {escape(article["topic"]).lower()}</p><h1>{title}</h1><p class="article-lead">{escape(article["lead"])}</p>
      <p class="article-byline">Por Achados Casa Prática · Publicado em 3 de outubro de 2026 · Seleção feita a partir dos anúncios, sem testes independentes dos produtos.</p></header>
      <div class="article-body"><div class="article-prose">
        <figure class="article-image"><img src="/blog-images/{slug}.webp" alt="{escape(article["image_alt"])}" width="1280" height="720" /><figcaption>Composição das imagens dos anúncios; características, oferta e disponibilidade podem mudar.</figcaption></figure>
        {article["body"]}
        <div class="article-sources"><h2>Sobre este guia</h2><p>Critérios gerais de seleção, não avaliação ou recomendação técnica testada por nós. Consultamos <a href="{escape(source_url)}">{escape(source_label)}</a> para orientar o tema; as especificações e condições dos produtos devem ser confirmadas nos anúncios atuais.</p></div>
      </div><aside class="article-aside" aria-label="Produtos relacionados"><p class="eyebrow">Na vitrine</p><h2>Veja as opções</h2><p class="affiliate-note">Links de afiliado: podemos receber comissão sem custo extra. Compra, suporte e devolução no Mercado Livre, conforme as condições aplicáveis.</p>{cards}<a class="article-category" href="{escape(article["category"])}">Ver seleção de {escape(article["topic"]).lower()} ↗</a></aside></div>
    </article>
    <nav class="article-related" aria-label="Mais guias"><strong>Continue lendo</strong>{related}<a href="/">Ir para os 15 produtos ↗</a></nav>
  </main>
  <footer class="site-footer"><span>⌂ <strong>Achados Casa Prática</strong></span><p>Curadoria independente · Links de afiliado · Compra no Mercado Livre</p><a href="/">Vitrine ↑</a></footer>
</body></html>
'''


def render_index():
    cards = "".join(
        f'''<article class="blog-index-card"><a href="/blog/{escape(a["slug"])}.html"><img src="/blog-images/{escape(a["slug"])}.webp" alt="{escape(a["image_alt"])}" loading="lazy" width="1280" height="720" /><span>{escape(a["topic"])}</span><h2>{escape(a["title"])}</h2><p>{escape(a["lead"])}</p><strong>Ler guia ↗</strong></a></article>'''
        for a in ARTICLES
    )
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="theme-color" content="#f8f5ef" /><meta name="robots" content="max-image-preview:large" /><title>Guias para escolher melhor | Achados Casa Prática</title>
<meta name="description" content="Guias práticos sobre potes para despensa, organização de banheiro e escolha de soquetes. Critérios claros antes de visitar os anúncios." />
<link rel="canonical" href="{BASE}/blog/" /><link rel="alternate" type="application/rss+xml" title="Guias Achados Casa Prática" href="{BASE}/feed.xml" />
<meta property="og:type" content="website" /><meta property="og:site_name" content="Achados Casa Prática" />
<meta property="og:title" content="Guias para escolher melhor | Achados Casa Prática" /><meta property="og:description" content="Ideias práticas de casa e ferramentas para decidir melhor antes de comprar." />
<meta property="og:url" content="{BASE}/blog/" /><meta property="og:image" content="{BASE}/blog-images/potes-despensa-pequena.webp" />
<meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="Guias para escolher melhor" /><meta name="twitter:description" content="Ideias práticas para decidir melhor antes de comprar." /><meta name="twitter:image" content="{BASE}/blog-images/potes-despensa-pequena.webp" />
<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet" /><link rel="stylesheet" href="/styles.css" /></head>
<body><header class="site-header"><a class="brand" href="/" aria-label="Achados Casa Prática, início"><span class="brand-mark" aria-hidden="true">⌂</span><span class="brand-name"><strong>Achados</strong><em>Casa Prática</em></span></a><a class="header-back" href="/">← Voltar à vitrine</a></header>
<main class="blog-home"><nav class="breadcrumbs" aria-label="Você está aqui"><a href="/">Vitrine</a><span>›</span><span>Guias</span></nav><div class="blog-home-heading"><p class="eyebrow">Ideias para a vida real</p><h1>Escolha melhor, <i>com calma.</i></h1><p>Antes de abrir um anúncio, use estes guias para entender medidas, materiais e compatibilidade. A vitrine continua a um clique.</p></div><div class="blog-index-grid">{cards}</div><p class="blog-disclosure">Textos editoriais feitos a partir de pesquisa e informações de anúncios; não realizamos testes independentes dos produtos. Alguns links são de afiliado e podem gerar comissão sem custo extra.</p><p class="blog-feed"><a href="/feed.xml">Assinar atualizações por RSS ↗</a></p></main>
<footer class="site-footer"><span>⌂ <strong>Achados Casa Prática</strong></span><p>Curadoria independente · Links de afiliado · Compra no Mercado Livre</p><a href="/">Vitrine ↑</a></footer></body></html>
'''


def render_feed():
    atom_ns = "http://www.w3.org/2005/Atom"
    ET.register_namespace("atom", atom_ns)
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    for tag, value in [("title", "Guias | Achados Casa Prática"), ("link", BASE + "/blog/"),
                       ("description", "Guias úteis sobre organização da casa e escolha de ferramentas, com transparência de afiliados."),
                       ("language", "pt-br"), ("lastBuildDate", format_datetime(PUBLISHED))]:
        ET.SubElement(channel, tag).text = value
    ET.SubElement(channel, f"{{{atom_ns}}}link", href="https://pubsubhubbub.appspot.com/", rel="hub")
    ET.SubElement(channel, f"{{{atom_ns}}}link", href=BASE + "/feed.xml", rel="self", type="application/rss+xml")
    for a in ARTICLES:
        item = ET.SubElement(channel, "item")
        url = f'{BASE}/blog/{a["slug"]}.html'
        for tag, value in [("title", a["title"]), ("link", url), ("guid", url),
                           ("description", a["description"]), ("pubDate", format_datetime(PUBLISHED))]:
            el = ET.SubElement(item, tag)
            el.text = value
            if tag == "guid": el.set("isPermaLink", "true")
    ET.indent(rss, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(rss, encoding="unicode") + '\n'


def main():
    home = (PUBLIC / "index.html").read_text(encoding="utf-8")
    BLOG.mkdir(exist_ok=True)
    for article in ARTICLES:
        for _, image, link, _ in article["products"]:
            assert (PUBLIC / "product-images" / image).is_file(), image
            assert link in home, f"Link ausente da vitrine: {link}"
        path = BLOG / (article["slug"] + ".html")
        path.write_text(render_article(article), encoding="utf-8")
        print(path)
    (BLOG / "index.html").write_text(render_index(), encoding="utf-8")
    (PUBLIC / "feed.xml").write_text(render_feed(), encoding="utf-8")
    print(BLOG / "index.html", PUBLIC / "feed.xml")


if __name__ == "__main__":
    main()

# Achados Casa Prática

Site estático independente, preparado para GitHub → Netlify.

## Conteúdo

- 15 produtos originais preservados, mais 28 produtos únicos dos 29 links recebidos em 6 de outubro de 2026.
- `1uZEyzq` e `2udUegA` apontam para o mesmo lava-roupas OMO 7 L (MLB5317443929); mantido o primeiro no catálogo.
- Os anúncios comuns do copo térmico e do tênis masculino também foram representados pelos respectivos links de afiliado `2PemxhA` e `31EAatq`.
- Busca por nome e descrição, combinada com filtros de categoria.
- Identificação da plataforma em cada produto, botões para Mercado Livre e aviso de comissão.
- Três páginas de seleção, três artigos, índice do blog, RSS, robots e sitemap preservados a partir do material enviado.
- As novas imagens usam o CDN oficial do Mercado Livre. As imagens originais e capas dos guias estão no repositório. Nenhum recurso do site depende do Manus.
- Não foram publicados preços fixos, promessas de desempenho ou frete: o anúncio é a fonte dessas condições.

## Conectar ao site existente na Netlify

1. Abra o projeto **achadoscasapratica** na sua conta Netlify.
2. Na configuração de publicação contínua, vincule o repositório `ericpolicarpo/achados-casa-pratica`.
3. Selecione a branch `main`, deixe a pasta base vazia e o comando de build vazio. A pasta de publicação é `public`, definida em `netlify.toml`.
4. Antes de publicar, use a prévia da Netlify para conferir a vitrine e o blog.
5. Mantenha o projeto e domínio atuais. Não crie outro site para substituir o endereço existente.

Documentação oficial: https://docs.netlify.com/build/configure-builds/file-based-configuration/

Esta preparação não vincula automaticamente sua conta Netlify. O site publicado anteriormente continua ativo até a nova publicação.

## Manutenção

A vitrine está em `public/index.html`; estilos em `public/styles.css`; busca, filtros e compartilhamento em `public/app.js`. Registre novos produtos em `catalogo/novos-produtos.json` e acrescente os cartões HTML à vitrine, atualizando a contagem.

Os scripts em `scripts/` geram as seleções, artigos, capas e sitemap. `build_blog_covers.py` usa Pillow; os demais usam somente a biblioteca padrão do Python. As páginas já geradas estão em `public`, portanto a Netlify não precisa executar os scripts nem instalar dependências.

Prévia local: `python -m http.server 8765 --directory public`.

Não inclua senhas, tokens, arquivos `.env` ou a pasta `.netlify` no repositório.

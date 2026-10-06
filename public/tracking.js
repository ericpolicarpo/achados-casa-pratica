const notifyCopy = message => {const toast=document.querySelector('.toast');if(!toast)return;toast.textContent=message;toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),3000);};
document.querySelectorAll('[data-share-path]').forEach(button=>button.addEventListener('click',async()=>{const url=new URL(button.dataset.sharePath,location.origin).href;try{await navigator.clipboard.writeText(url);notifyCopy('Link do produto copiado.');}catch{notifyCopy('Copie este link: '+url);}}));
const allowedChannels=['youtube','facebook','instagram','whatsapp','teste'];
const source=new URLSearchParams(location.search).get('utm_source');
const channel=allowedChannels.includes(source)?source:'direto';
if(channel!=='direto')document.querySelectorAll('a[href], [data-share-path]').forEach(element=>{const attr=element.hasAttribute('data-share-path')?'data-share-path':'href';const raw=element.getAttribute(attr);if(!raw||raw.startsWith('#'))return;const url=new URL(raw,location.origin);if(url.origin!==location.origin)return;url.searchParams.set('utm_source',channel);element.setAttribute(attr,url.pathname+url.search+url.hash);});
fetch('/product-map.json').then(r=>r.json()).then(products=>{
 const byLink=new Map(products.map(p=>[p.affiliate,p.id]));
 let lastId='',lastTime=0;
 document.addEventListener('click',event=>{
  const link=event.target.closest('a');if(!link)return;
  const id=byLink.get(link.href);if(!id)return;
  const now=Date.now();if(lastId===id&&now-lastTime<1000)return;lastId=id;lastTime=now;
  const payload=JSON.stringify({product:id,channel,page:location.pathname});
  const body=new Blob([payload],{type:'application/json'});
  if(!navigator.sendBeacon('/.netlify/functions/product-click',body))fetch('/.netlify/functions/product-click',{method:'POST',headers:{'Content-Type':'application/json'},body:payload,keepalive:true}).catch(()=>{});
 });
}).catch(()=>{});

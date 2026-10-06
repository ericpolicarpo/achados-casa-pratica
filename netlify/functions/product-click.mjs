const products=new Set(["kit-de-utensilios-de-silicone", "potes-com-tampa-trava", "organizadores-de-banheiro", "kit-de-30-cabides-de-veludo-vittak", "kit-de-10-sacos-a-vacuo-com-bomba", "porta-temperos-giratorio-solar", "copo-termico-preto-de-1-2-l", "kit-de-10-potes-de-vidro-rishon", "kit-de-soquetes-com-catraca", "potes-de-vidro", "canecas-de-cappuccino", "tapete-de-banheiro", "jogo-de-tapetes", "caderneta-executiva-a5", "cozedor-de-ovos-eletrico", "sacos-para-lavar-tenis", "cobre-leito-queen", "fone-bluetooth-tws", "raquete-eletrica", "soquetes-de-impacto", "lava-roupas-liquido-omo-7-l", "chinelo-havaianas-top-branco", "protetor-de-colchao-casal-cinza", "chaleira-eletrica-atacama-unitermi", "kit-de-4-camisetas-dry-fit-sandrini", "mangueira-de-jardim-marqs-home-50-m", "jogo-de-lencol-casal-com-3-pecas", "cortina-blackout-texfine-preta", "protetor-de-colchao-queen", "macarico-gourmet-com-3-refis", "kit-de-2-toucas-de-cetim", "parafusadeira-e-furadeira-tb12a", "kit-de-3-camisetas-sandrini", "adaptador-de-tomada-para-viagem", "carregador-usb-c-com-fonte-e-cabo", "marmita-eletrica-woosh-1-5-l", "filtro-de-linha-com-6-tomadas-e-2-usb", "camera-inteligente-intelbras-im7", "cooktop-itatiaia-essencial-5-bocas", "chuveiro-eletronico-fame-intense", "tenis-feminino-sneeks-cinza-e-rosa", "power-bank-com-display-digital", "tenis-masculino-para-treino"]);
const channels=new Set(['youtube','facebook','instagram','whatsapp','direto','teste']);
export default async request=>{
 const headers={'Cache-Control':'no-store'};
 if(request.method!=='POST')return new Response(null,{status:405,headers});
 if(request.headers.get('origin')!=='https://achadoscasapratica.netlify.app')return new Response(null,{status:403,headers});
 const text=await request.text();if(text.length>1024)return new Response(null,{status:413,headers});
 let data;try{data=JSON.parse(text);}catch{return new Response(null,{status:400,headers});}
 if(!products.has(data.product)||!channels.has(data.channel)||typeof data.page!=='string'||!/^\/(?:produtos\/[a-z0-9-]+\/|selecoes\/[a-z0-9-]+\/)?$/.test(data.page))return new Response(null,{status:400,headers});
 console.log(JSON.stringify({event:'product_click',product:data.product,channel:data.channel,page:data.page,time:new Date().toISOString()}));
 return new Response(null,{status:204,headers});
};

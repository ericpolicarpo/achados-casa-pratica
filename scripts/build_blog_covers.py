#!/usr/bin/env python3
"""Pad two existing product images into each wide cover without cropping or text."""
from pathlib import Path
from PIL import Image, ImageOps

PUBLIC = Path(__file__).resolve().parents[1] / "public"
OUT = PUBLIC / "blog-images"
OUT.mkdir(exist_ok=True)
PAIRS = {
    "potes-despensa-pequena": ("05-potes-hermeticos.webp", "04-potes-plasticos.webp"),
    "organizar-banheiro-pequeno": ("02-organizadores-banheiro.webp", "07-tapete-60x40.webp"),
    "soquetes-catraca-ou-impacto": ("01-kit-soquetes.webp", "15-soquetes-impacto.webp"),
}

for slug, names in PAIRS.items():
    cover = Image.new("RGB", (1280, 720), (247, 245, 239))
    for x, name in zip((32, 652), names):
        source = ImageOps.exif_transpose(Image.open(PUBLIC / "product-images" / name)).convert("RGB")
        resized = ImageOps.contain(source, (596, 680), Image.Resampling.LANCZOS)
        cover.paste(resized, (x + (596 - resized.width) // 2, 20 + (680 - resized.height) // 2))
    output = OUT / f"{slug}.webp"
    cover.save(output, "WEBP", quality=84, method=6)
    print(output, cover.size)

#!/usr/bin/env python3
"""Generate a URL and image sitemap from the public route manifest and static HTML."""
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
ORIGIN = "https://achadoscasapratica.netlify.app"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
IMAGE_NS = "http://www.google.com/schemas/sitemap-image/1.1"
ET.register_namespace("", SITEMAP_NS)
ET.register_namespace("image", IMAGE_NS)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        src = attributes.get("src") or ""
        rel = attributes.get("rel") or ""
        if tag == "img" and src.startswith(("/product-images/", "/blog-images/")):
            self.images.append(src)
        if tag == "link" and "canonical" in rel.split():
            self.canonical = attributes.get("href")


def main():
    routes = json.loads((PUBLIC / "routes.json").read_text(encoding="utf-8"))["routes"]
    root = ET.Element(f"{{{SITEMAP_NS}}}urlset")
    for route in routes:
        path = route["path"]
        source = PUBLIC / "index.html" if path == "/" else PUBLIC / path.lstrip("/") / "index.html" if path.endswith("/") else PUBLIC / path.lstrip("/")
        assert source.is_file(), source
        parser = PageParser()
        parser.feed(source.read_text(encoding="utf-8"))
        url = ORIGIN + path
        assert parser.canonical == url, (source, parser.canonical, url)
        entry = ET.SubElement(root, f"{{{SITEMAP_NS}}}url")
        ET.SubElement(entry, f"{{{SITEMAP_NS}}}loc").text = url
        ET.SubElement(entry, f"{{{SITEMAP_NS}}}lastmod").text = date.today().isoformat()
        for image in dict.fromkeys(parser.images):
            assert (PUBLIC / image.lstrip("/")).is_file(), image
            image_tag = ET.SubElement(entry, f"{{{IMAGE_NS}}}image")
            ET.SubElement(image_tag, f"{{{IMAGE_NS}}}loc").text = ORIGIN + image
        print(path, len(set(parser.images)), "imagens")
    ET.indent(root, space="  ")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n"
    (PUBLIC / "sitemap.xml").write_text(xml, encoding="utf-8")


if __name__ == "__main__":
    main()

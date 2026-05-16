#!/usr/bin/env python3
"""Assert the v4 OG/Twitter production card pipeline is wired correctly."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SITE_HOST = "https://panta-rhei.site"


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.metas: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "meta":
            self.metas.append({key: value or "" for key, value in attrs})
        if tag == "link":
            self.links.append({key: value or "" for key, value in attrs})


def fail(message: str) -> None:
    print(f"OG pipeline assertion failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def slug_for(route: str) -> str:
    route = route or "/"
    slug = route.strip("/")
    if not slug:
        return "index"
    return re.sub(r"[^a-zA-Z0-9_.-]", "-", slug.replace("/", "__"))


def route_html(site: Path, route: str) -> Path:
    if route == "/":
        return site / "index.html"
    return site / route.strip("/") / "index.html"


def meta(parser: MetaParser, attr: str, key: str) -> str:
    for item in parser.metas:
        if item.get(attr) == key:
            return item.get("content", "")
    return ""


def metas(parser: MetaParser, attr: str, key: str) -> list[str]:
    return [item.get("content", "") for item in parser.metas if item.get(attr) == key]


def canonical(parser: MetaParser) -> str:
    for item in parser.links:
        if item.get("rel") == "canonical":
            return item.get("href", "")
    return ""


def assert_file(path: Path, min_size: int = 500) -> None:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    if path.is_file() and path.stat().st_size < min_size:
        fail(f"file is too small to be valid: {path.relative_to(ROOT)}")


def collect_sitemap_routes() -> list[str]:
    data = yaml.safe_load((ROOT / "_data/sitemap_v4.yml").read_text(encoding="utf-8")) or {}
    routes: list[str] = []
    seen: set[str] = set()

    def add(url: object) -> None:
        if not isinstance(url, str):
            return
        if not url.startswith("/") or url.startswith("//") or url == "/sitemap.xml":
            return
        if url in seen:
            return
        seen.add(url)
        routes.append(url)

    def walk_cards(cards: object) -> None:
        if isinstance(cards, dict):
            cards = [cards]
        for card in cards or []:
            if not isinstance(card, dict):
                continue
            add(card.get("root_url"))
            for link in card.get("links", []) or []:
                if isinstance(link, dict):
                    add(link.get("url"))

    for group_name in ("primary_lanes", "support_cards", "support_card", "secondary_cards", "support_sections"):
        walk_cards(data.get(group_name))
    return routes


def main() -> int:
    if len(sys.argv) != 2:
        fail("usage: assert_og_pipeline.py <built-site-root>")
    built = Path(sys.argv[1])
    if not built.exists():
        fail(f"built site root does not exist: {built}")

    required = [
        ROOT / "_data/og/icon-token-map.yml",
        ROOT / "_data/og/template-geometry.yml",
        ROOT / "_data/og/pages.yml",
        ROOT / "_data/og/sitemap_pages.yml",
        ROOT / "_data/og/generated_cards.yml",
        ROOT / "scripts/generate_og_images.py",
        ROOT / "assets/og/backgrounds/og-background-dark-standard.svg",
        ROOT / "assets/og/backgrounds/og-background-light-standard.svg",
        ROOT / "assets/og/logo/logo-og-lockup.svg",
        ROOT / "assets/og/logo/logo-og-lockup-light.svg",
        ROOT / "assets/og/fonts-local/EBGaramond-Regular.ttf",
        ROOT / "assets/og/fonts-local/SourceSans3-Regular.ttf",
        ROOT / "assets/og/fonts-local/SourceCodePro-Regular.ttf",
        ROOT / "assets/og/icons/material-symbols/account_balance.svg",
    ]
    for path in required:
        assert_file(path, min_size=80 if path.suffix == ".svg" else 500)

    manifest = yaml.safe_load((ROOT / "_data/og/generated_cards.yml").read_text(encoding="utf-8"))
    cards = manifest.get("cards", {})
    if len(cards) < 190:
        fail(f"expected at least 190 generated cards after sitemap coverage, found {len(cards)}")

    cards_by_route = {card.get("route"): slug for slug, card in cards.items()}
    sitemap_routes = collect_sitemap_routes()
    missing_sitemap_cards = [route for route in sitemap_routes if route not in cards_by_route]
    if missing_sitemap_cards:
        fail("sitemap-linked routes missing generated cards: " + ", ".join(missing_sitemap_cards[:30]))

    generator_source = (ROOT / "scripts/generate_og_images.py").read_text(encoding="utf-8", errors="ignore")
    if ">π</text>" in generator_source or "Independent open research program</text>" in generator_source:
        fail("OG generator still contains the old ad hoc text lockup fallback")

    site_atlas = json.loads((ROOT / "_data/site_atlas/pages.json").read_text(encoding="utf-8"))
    launch_routes = [
        page["route"]
        for page in site_atlas["pages"]
        if page.get("release", {}).get("launch_critical") is True
        and page.get("status") in {"canonical", "auxiliary"}
    ]
    missing_launch_cards = [route for route in launch_routes if slug_for(route) not in cards]
    if missing_launch_cards:
        fail("launch-critical routes missing generated cards: " + ", ".join(missing_launch_cards[:20]))

    required_preview_routes = [
        "/",
        "/program/",
        "/publications/",
        "/publications/anchor-documents/c001-standing-in-the-inquiry-of-being/",
        "/publications/anchor-documents/wp001-panta-rhei-research-program-executive-overview/",
        "/publications/anchor-documents/wp004-public-research-observatory-blueprint/",
        "/publications/anchor-documents/wp005-global-public-good-impact-overview/",
        "/verify/predictions-and-falsification/",
    ]
    missing_preview_cards = [route for route in required_preview_routes if slug_for(route) not in cards]
    if missing_preview_cards:
        fail("representative preview routes missing generated cards: " + ", ".join(missing_preview_cards))

    for slug, card in cards.items():
        for field in ("image", "svg", "webp"):
            rel = card.get(field)
            if not rel:
                fail(f"{slug} missing manifest field {field}")
            assert_file(ROOT / rel.lstrip("/"))
        if not card.get("alt"):
            fail(f"{slug} missing alt text")
        icon = card.get("icon")
        if not icon:
            fail(f"{slug} missing icon token in generated manifest")
        assert_file(ROOT / "assets" / "og" / "icons" / "material-symbols" / f"{icon}.svg", min_size=80)

        svg_text = (ROOT / card["svg"].lstrip("/")).read_text(encoding="utf-8", errors="ignore")
        if "canonical-lockup" not in svg_text:
            fail(f"{slug} generated SVG missing canonical-lockup marker")
        if "π ρ wordmark" in svg_text or "Independent open research program</text>" in svg_text:
            fail(f"{slug} generated SVG contains the old ad hoc wordmark construction")

    index_png = ROOT / "assets/og/png/index.png"
    for legacy_fallback in [ROOT / "assets/og-image.png", ROOT / "assets/brand/og-image.png"]:
        assert_file(legacy_fallback)
        if legacy_fallback.read_bytes() != index_png.read_bytes():
            fail(f"{legacy_fallback.relative_to(ROOT)} should match the v4 generated fallback card")

    offenders: list[str] = []
    legacy_metadata_offenders: list[str] = []
    for html_path in built.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="ignore")
        if "/assets/og-cards/" in text:
            offenders.append(str(html_path.relative_to(built)))
            if len(offenders) >= 20:
                break
        if (
            'property="og:image" content="https://panta-rhei.site/assets/og-image.png"' in text
            or 'name="twitter:image" content="https://panta-rhei.site/assets/og-image.png"' in text
            or '"https://panta-rhei.site/assets/og-image.png"' in text
        ):
            legacy_metadata_offenders.append(str(html_path.relative_to(built)))
    if offenders:
        fail("legacy /assets/og-cards references remain: " + ", ".join(offenders))
    if legacy_metadata_offenders:
        fail("legacy /assets/og-image.png metadata references remain: " + ", ".join(legacy_metadata_offenders[:20]))

    sample_routes = sorted(set(sitemap_routes + launch_routes + ["/", "/program/", "/agenda/", "/impact/", "/engage/"]))
    for route in sample_routes:
        slug = cards_by_route.get(route) or slug_for(route)
        card = cards.get(slug)
        if not card or card.get("route") != route:
            fail(f"{route} missing generated card")
        html_path = route_html(built, route)
        if not html_path.exists():
            fail(f"{route} did not build at {html_path}")
        parser = MetaParser()
        html = html_path.read_text(encoding="utf-8", errors="ignore")
        parser.feed(html)
        expected = f"{SITE_HOST}{card['image']}"
        expected_url = f"{SITE_HOST}{route}" if route != "/" else f"{SITE_HOST}/"
        if not canonical(parser):
            fail(f"{route} missing canonical link")
        for attr, key in [
            ("property", "og:title"),
            ("property", "og:description"),
            ("property", "og:type"),
            ("property", "og:url"),
            ("property", "og:image"),
            ("property", "og:image:secure_url"),
            ("property", "og:image:type"),
            ("property", "og:image:width"),
            ("property", "og:image:height"),
            ("property", "og:image:alt"),
            ("name", "twitter:card"),
            ("name", "twitter:title"),
            ("name", "twitter:description"),
            ("name", "twitter:image"),
            ("name", "twitter:image:alt"),
            ("name", "author"),
            ("name", "date"),
            ("name", "dcterms.created"),
            ("name", "dcterms.modified"),
        ]:
            if not meta(parser, attr, key):
                fail(f"{route} missing {key} metadata")
        if meta(parser, "property", "og:image") != expected:
            fail(f"{route} og:image should be generated card {expected}")
        if meta(parser, "property", "og:image:secure_url") != expected:
            fail(f"{route} og:image:secure_url should be generated card {expected}")
        if meta(parser, "property", "og:image:type") != "image/png":
            fail(f"{route} og:image:type should be image/png")
        if meta(parser, "name", "twitter:image") != expected:
            fail(f"{route} twitter:image should be generated card {expected}")
        if meta(parser, "property", "og:image:alt") != card["alt"]:
            fail(f"{route} og:image:alt should use generated card alt")
        if meta(parser, "name", "twitter:image:alt") != card["alt"]:
            fail(f"{route} twitter:image:alt should use generated card alt")
        if meta(parser, "property", "og:image:width") != "1200" or meta(parser, "property", "og:image:height") != "630":
            fail(f"{route} missing 1200x630 OG dimensions")
        if meta(parser, "property", "og:url") != expected_url:
            fail(f"{route} og:url should be {expected_url}")
        og_type = meta(parser, "property", "og:type")
        article_authors = metas(parser, "property", "article:author")
        if og_type == "article":
            if len(article_authors) < 2:
                fail(f"{route} article page missing article:author metadata")
            if not meta(parser, "property", "article:published_time") or not meta(parser, "property", "article:modified_time"):
                fail(f"{route} article page missing article published/modified metadata")
        elif article_authors or meta(parser, "property", "article:published_time") or meta(parser, "property", "article:modified_time"):
            fail(f"{route} non-article page should not emit article:* metadata")
        if '"@id": "' + expected_url + '#social-metadata"' not in html:
            fail(f"{route} missing social metadata JSON-LD graph")
        if '"datePublished"' not in html or '"dateModified"' not in html:
            fail(f"{route} missing JSON-LD date fields")

    fallback_html = built / "404.html"
    if fallback_html.exists():
        parser = MetaParser()
        parser.feed(fallback_html.read_text(encoding="utf-8", errors="ignore"))
        fallback_expected = f"{SITE_HOST}/assets/og/png/index.png"
        if meta(parser, "property", "og:image") != fallback_expected:
            fail("404 fallback og:image should use the v4 generated fallback card")
        if meta(parser, "name", "twitter:image") != fallback_expected:
            fail("404 fallback twitter:image should use the v4 generated fallback card")

    plate_data = (built / "api" / "plates.json").read_text(encoding="utf-8", errors="ignore")
    if "/assets/images/plates/plate-01-public-research-observatory-og.jpg" not in plate_data:
        fail("scientific plate API no longer exposes plate OG assets")
    if not (built / "assets/images/plates/plate-01-public-research-observatory-og.jpg").exists():
        fail("scientific plate OG asset missing from built site")

    print(f"OG pipeline assertion passed: {len(cards)} generated cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

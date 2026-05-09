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

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "meta":
            self.metas.append({key: value or "" for key, value in attrs})


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


def assert_file(path: Path, min_size: int = 500) -> None:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    if path.is_file() and path.stat().st_size < min_size:
        fail(f"file is too small to be valid: {path.relative_to(ROOT)}")


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
        ROOT / "_data/og/generated_cards.yml",
        ROOT / "scripts/generate_og_images.py",
        ROOT / "assets/og/backgrounds/og-background-dark-standard.svg",
        ROOT / "assets/og/backgrounds/og-background-light-standard.svg",
        ROOT / "assets/og/fonts-local/EBGaramond-Regular.ttf",
        ROOT / "assets/og/fonts-local/SourceSans3-Regular.ttf",
        ROOT / "assets/og/fonts-local/SourceCodePro-Regular.ttf",
        ROOT / "assets/og/icons/material-symbols/account_balance.svg",
    ]
    for path in required:
        assert_file(path, min_size=80 if path.suffix == ".svg" else 500)

    manifest = yaml.safe_load((ROOT / "_data/og/generated_cards.yml").read_text(encoding="utf-8"))
    cards = manifest.get("cards", {})
    if len(cards) < 120:
        fail(f"expected at least 120 generated cards, found {len(cards)}")

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

    for slug, card in cards.items():
        for field in ("image", "svg", "webp"):
            rel = card.get(field)
            if not rel:
                fail(f"{slug} missing manifest field {field}")
            assert_file(ROOT / rel.lstrip("/"))
        if not card.get("alt"):
            fail(f"{slug} missing alt text")

    offenders: list[str] = []
    for html_path in built.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="ignore")
        if "/assets/og-cards/" in text:
            offenders.append(str(html_path.relative_to(built)))
            if len(offenders) >= 20:
                break
    if offenders:
        fail("legacy /assets/og-cards references remain: " + ", ".join(offenders))

    sample_routes = sorted(set(launch_routes + ["/", "/program/", "/agenda/", "/impact/", "/engage/"]))
    for route in sample_routes:
        slug = slug_for(route)
        card = cards.get(slug)
        if not card:
            fail(f"{route} missing generated card")
        html_path = route_html(built, route)
        if not html_path.exists():
            fail(f"{route} did not build at {html_path}")
        parser = MetaParser()
        parser.feed(html_path.read_text(encoding="utf-8", errors="ignore"))
        expected = f"{SITE_HOST}{card['image']}"
        if meta(parser, "property", "og:image") != expected:
            fail(f"{route} og:image should be generated card {expected}")
        if meta(parser, "name", "twitter:image") != expected:
            fail(f"{route} twitter:image should be generated card {expected}")
        if meta(parser, "property", "og:image:alt") != card["alt"]:
            fail(f"{route} og:image:alt should use generated card alt")
        if meta(parser, "name", "twitter:image:alt") != card["alt"]:
            fail(f"{route} twitter:image:alt should use generated card alt")
        if meta(parser, "property", "og:image:width") != "1200" or meta(parser, "property", "og:image:height") != "630":
            fail(f"{route} missing 1200x630 OG dimensions")

    plate_data = (built / "api" / "plates.json").read_text(encoding="utf-8", errors="ignore")
    if "/assets/images/plates/plate-01-public-research-observatory-og.jpg" not in plate_data:
        fail("scientific plate API no longer exposes plate OG assets")
    if not (built / "assets/images/plates/plate-01-public-research-observatory-og.jpg").exists():
        fail("scientific plate OG asset missing from built site")

    print(f"OG pipeline assertion passed: {len(cards)} generated cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

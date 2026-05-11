#!/usr/bin/env python3
"""Generate deterministic v4 OG/Twitter card assets.

The public website consumes the generated manifest at
`_data/og/generated_cards.yml`; normal Jekyll builds never generate cards.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SITE_HOST = "panta-rhei.site"
CARD_WIDTH = 1200
CARD_HEIGHT = 630

DATA_DIR = ROOT / "_data" / "og"
SITE_ATLAS_PAGES = ROOT / "_data" / "site_atlas" / "pages.json"
PAGES_OVERRIDES = DATA_DIR / "pages.yml"
GENERATED_MANIFEST = DATA_DIR / "generated_cards.yml"

ASSETS_DIR = ROOT / "assets" / "og"
SVG_DIR = ASSETS_DIR / "svg"
PNG_DIR = ASSETS_DIR / "png"
WEBP_DIR = ASSETS_DIR / "webp"
GALLERY_DIR = ASSETS_DIR / "gallery"
ICON_DIR = ASSETS_DIR / "icons" / "material-symbols"
LOCKUP_SVG = ASSETS_DIR / "logo" / "logo-og-lockup.svg"


LANE_ICONS = {
    "home": "explore",
    "discover": "explore",
    "program": "account_balance",
    "agenda": "checklist",
    "corpus": "deployed_code",
    "results": "inventory_2",
    "verify": "fact_check",
    "publications": "library_books",
    "impact": "public",
    "engage": "handshake",
    "support": "route",
}


ROLE_LABELS = {
    "global_entry": "Global Entry",
    "lane_landing": "Lane Root",
    "doctrine_page": "Doctrine",
    "program_impact_bridge": "Program Bridge",
    "publication_root": "Publications",
}


STATUS_LABELS = {
    "canonical": "Canonical",
    "auxiliary": "Auxiliary",
    "archive": "Archive",
    "deprecated": "Deprecated",
    "redirected": "Redirected",
}


VARIANTS = {
    "dark": {
        "background": "dark",
        "title": "#F8FAF7",
        "subtitle": "#D8E3EC",
        "route": "#B9CFE2",
        "muted": "#C4D4E1",
        "eyebrow_bg": "#F8FAF7",
        "eyebrow_text": "#163E64",
        "icon": "#FFFFFF",
        "lockup": "#F8FAF7",
    },
    "light": {
        "background": "light",
        "title": "#17202B",
        "subtitle": "#44515D",
        "route": "#5B6772",
        "muted": "#6C7884",
        "eyebrow_bg": "#163E64",
        "eyebrow_text": "#F8FAF7",
        "icon": "#163E64",
        "lockup": "#163E64",
    },
}


def fail(message: str) -> None:
    print(f"OG generation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def slug_for(route: str) -> str:
    route = route or "/"
    slug = route.strip("/")
    if not slug:
        return "index"
    return re.sub(r"[^a-zA-Z0-9_.-]", "-", slug.replace("/", "__"))


def display_route(route: str) -> str:
    return SITE_HOST if route == "/" else f"{SITE_HOST}{route.rstrip('/')}"


def fit_route(route: str, max_chars: int = 44) -> str:
    route = str(route)
    if len(route) <= max_chars:
        return route
    return route[: max_chars - 3].rstrip("/_-") + "..."


def humanize(value: str | None) -> str:
    if not value:
        return "Page"
    return ROLE_LABELS.get(value, value.replace("_", " ").replace("-", " ").title())


def status_label(value: str | None) -> str:
    return STATUS_LABELS.get(value or "", humanize(value))


def xml(text: object) -> str:
    return html.escape(str(text), quote=True)


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).replace("&amp;", "&").strip()


def strip_trailing_whitespace(text: str) -> str:
    """Keep generated SVG deterministic and friendly to git diff checks."""
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"


def wrap_text(text: str, max_chars: int, max_lines: int) -> list[str]:
    words = str(text).split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if len(candidate) > max_chars and current:
            lines.append(current)
            current = word
        else:
            current = candidate
        if len(lines) >= max_lines:
            break
    if current and len(lines) < max_lines:
        lines.append(current)
    used = len(" ".join(lines).split())
    if words and used < len(words) and lines:
        lines[-1] = lines[-1].rstrip(".,;:") + "..."
    return lines or [""]


def read_front_matter(source: str | None) -> dict[str, Any]:
    if not source:
        return {}
    path = ROOT / source
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group(1)) or {}
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def source_for_route(route: str) -> str | None:
    if route == "/":
        candidates = ["index.md", "index.html"]
    else:
        clean = route.strip("/")
        candidates = [
            f"{clean}/index.md",
            f"{clean}/index.html",
            f"{clean}.md",
            f"{clean}.html",
        ]
    for candidate in candidates:
        if (ROOT / candidate).exists():
            return candidate
    return None


def load_site_atlas_pages() -> list[dict[str, Any]]:
    data = json.loads(SITE_ATLAS_PAGES.read_text(encoding="utf-8"))
    return data.get("pages", [])


def load_overrides() -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    if not PAGES_OVERRIDES.exists():
        return {}, {}
    data = yaml.safe_load(PAGES_OVERRIDES.read_text(encoding="utf-8")) or {}
    defaults = data.get("defaults", {}) if isinstance(data.get("defaults"), dict) else {}
    pages = {}
    for item in data.get("pages", []) or []:
        if isinstance(item, dict) and item.get("route"):
            route = str(item["route"])
            pages[route] = {**defaults, **item}
    return defaults, pages


def page_subtitle(front: dict[str, Any], page: dict[str, Any], override: dict[str, Any]) -> str:
    for key in ("subtitle", "description", "summary", "excerpt"):
        value = override.get(key) if key in override else front.get(key)
        if value:
            return strip_html(str(value))
    role = humanize(page.get("canonical_role"))
    lane = humanize(page.get("lane"))
    return f"{role} in the {lane} lane of the Panta Rhei public research observatory."


def build_card_records() -> list[dict[str, Any]]:
    _defaults, overrides = load_overrides()
    atlas_by_route: dict[str, dict[str, Any]] = {}
    cards: dict[str, dict[str, Any]] = {}

    for page in load_site_atlas_pages():
        route = str(page.get("route") or "")
        if route:
            atlas_by_route[route] = page
        release = page.get("release") or {}
        if release.get("launch_critical") is True and page.get("status") in {"canonical", "auxiliary"}:
            cards[route] = dict(page)

    for route, override in overrides.items():
        page = dict(atlas_by_route.get(route) or {})
        page.setdefault("route", route)
        page.setdefault("source", source_for_route(route))
        page.setdefault("title", override.get("title") or route.strip("/") or "Panta Rhei Research Program")
        page.setdefault("lane", override.get("lane") or "support")
        page.setdefault("canonical_role", override.get("canonical_role") or "curated_preview")
        page.setdefault("status", override.get("status") or "canonical")
        cards[route] = page

    records: list[dict[str, Any]] = []
    for route in sorted(cards, key=lambda item: (slug_for(item) != "index", item)):
        page = cards[route]
        override = overrides.get(route, {})
        source = page.get("source") or source_for_route(route)
        front = read_front_matter(source)
        og_front = front.get("og") if isinstance(front.get("og"), dict) else {}
        lane = str(override.get("lane") or page.get("lane") or front.get("lane") or "support")
        canonical_role = str(override.get("canonical_role") or page.get("canonical_role") or "page")
        status = str(override.get("status") or page.get("status") or "canonical")
        title = strip_html(str(override.get("title") or og_front.get("title") or front.get("og_card_title") or page.get("title") or front.get("title") or "Panta Rhei Research Program"))
        subtitle = page_subtitle(front, page, override)
        variant = str(override.get("variant") or og_front.get("variant") or ("light" if lane == "publications" else "dark"))
        variant = variant if variant in VARIANTS else "dark"
        icon = str(override.get("icon") or og_front.get("icon") or LANE_ICONS.get(lane, "route"))
        eyebrow = str(
            override.get("eyebrow")
            or og_front.get("eyebrow")
            or f"{humanize(lane)} · {humanize(canonical_role)} · {status_label(status)}"
        ).upper()
        alt = str(override.get("alt") or og_front.get("alt") or f"Panta Rhei preview card for {title}.")
        slug = slug_for(route)
        records.append(
            {
                "slug": slug,
                "route": route,
                "page_key": page.get("page_key"),
                "title": title,
                "subtitle": subtitle,
                "eyebrow": eyebrow,
                "display_route": str(override.get("display_route") or og_front.get("display_route") or display_route(route)),
                "icon": icon,
                "variant": variant,
                "template": str(override.get("template") or og_front.get("template") or f"og-{variant}-standard"),
                "alt": alt,
            }
        )
    return records


def background_svg(variant: str) -> str:
    if variant == "light":
        return """
          <rect width="1200" height="630" fill="#F8F7F0"/>
          <path d="M0 0h1200v630H0z" fill="#F8F7F0"/>
          <path d="M860 0h340v630H760z" fill="#EEF2F5" opacity="0.55"/>
          <rect x="0" y="618" width="1200" height="12" fill="url(#spectrum-rule)"/>
        """
    return """
      <linearGradient id="panta-og-dark-gradient" x1="0" y1="0" x2="1200" y2="630" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#13395E"/><stop offset="48%" stop-color="#163E64"/><stop offset="100%" stop-color="#1A4874"/>
      </linearGradient>
      <rect width="1200" height="630" fill="url(#panta-og-dark-gradient)"/>
      <rect x="0" y="618" width="1200" height="12" fill="url(#spectrum-rule)"/>
    """


def icon_markup(token: str, color: str, opacity: str) -> str:
    path = ICON_DIR / f"{token}.svg"
    if not path.exists():
        path = ICON_DIR / "route.svg"
    if not path.exists():
        return ""
    svg_text = path.read_text(encoding="utf-8", errors="ignore")
    paths = re.findall(r'<path[^>]*\sd="([^"]+)"', svg_text)
    if not paths:
        return ""
    body = "\n".join(f'<path d="{xml(path_d)}" fill="{color}"/>' for path_d in paths)
    return f"""
      <svg x="835" y="220" width="300" height="300" viewBox="0 -960 960 960" opacity="{opacity}" aria-hidden="true">
        {body}
      </svg>
    """


def _load_lockup_inner() -> str:
    """Read the canonical PRRP logo lockup SVG and return the inner content
    (everything inside the outer <svg> element). Result is cached so the file
    is read once per process even when rendering many cards."""
    if not LOCKUP_SVG.exists():
        return ""
    text = LOCKUP_SVG.read_text(encoding="utf-8", errors="ignore")
    # Drop the XML declaration and DOCTYPE if present.
    text = re.sub(r"<\?xml[^?]*\?>", "", text)
    text = re.sub(r"<!DOCTYPE[^>]*>", "", text)
    # Extract the inner content of the outer <svg> element.
    match = re.search(r"<svg\b[^>]*>(.*)</svg>\s*$", text, re.DOTALL)
    return match.group(1) if match else ""


_LOCKUP_INNER_CACHE: str | None = None


def render_lockup(color: str, variant: str = "dark") -> str:
    """Embed the canonical Panta Rhei brand lockup SVG (logo-og-lockup.svg) in
    the upper-right corner of the OG card. The source artwork is a navy chip
    (#163E64) with cream wordmark (#F6F7F3) drawn as outlined paths, viewBox
    2128x1074 (~2:1). We embed it inside a <g> with a translate+scale transform
    so the rendered placement is consistent across all 1200x630 OG cards.

    The `color` argument is accepted for back-compat with the dark/light variant
    plumbing in VARIANTS["lockup"], but the canonical SVG is monochrome by
    design so we don't recolor it. The chip provides its own contrast on light
    backgrounds; on dark backgrounds the navy chip merges with the gradient and
    the cream wordmark remains crisp on the card background."""
    global _LOCKUP_INNER_CACHE
    if _LOCKUP_INNER_CACHE is None:
        _LOCKUP_INNER_CACHE = _load_lockup_inner()
    inner = _LOCKUP_INNER_CACHE
    if not inner:
        # Defensive fallback to the previous text lockup if the SVG goes missing.
        return f"""
      <g transform="translate(785 26)" fill="{color}">
        <text x="0" y="44" font-family="EB Garamond OG, Georgia, serif" font-size="52" font-weight="400">π</text>
        <text x="31" y="67" font-family="EB Garamond OG, Georgia, serif" font-size="52" font-style="italic" font-weight="400">ρ</text>
        <text x="86" y="36" font-family="Source Sans 3 OG, Inter, Arial, sans-serif" font-size="25" font-weight="700">Panta Rhei Research</text>
        <text x="86" y="67" font-family="Source Sans 3 OG, Inter, Arial, sans-serif" font-size="21" opacity="0.82">Independent open research program</text>
      </g>
    """
    # Layout: place the lockup chip in the upper-right of the 1200x630 card.
    # Width 280 -> scale 280/2128 ~= 0.1316 -> height ~= 141.
    # Origin x = 1200 - 280 - 48 (right margin) = 872, y = 28 (top margin).
    target_w = 280.0
    src_w = 2128.0
    scale = target_w / src_w
    x = 872.0
    y = 28.0
    return f'<g transform="translate({x:.0f} {y:.0f}) scale({scale:.6f})">{inner}</g>'


def render_svg(record: dict[str, Any]) -> str:
    variant = VARIANTS[record["variant"]]
    title_size = 112 if len(record["title"]) <= 32 else 94 if len(record["title"]) <= 58 else 80
    title_chars = max(16, int(680 / (title_size * 0.52)))
    title_lines = wrap_text(record["title"], title_chars, 2)
    subtitle_lines = wrap_text(record["subtitle"], 52, 2)
    title_y = 272 if len(title_lines) == 1 else 234
    title_tspans = "\n".join(
        f'<tspan x="78" y="{title_y + i * int(title_size * 0.92)}">{xml(line)}</tspan>'
        for i, line in enumerate(title_lines)
    )
    subtitle_y = title_y + len(title_lines) * int(title_size * 0.92) + 34
    subtitle_tspans = "\n".join(
        f'<tspan x="82" y="{subtitle_y + i * 42}">{xml(line)}</tspan>'
        for i, line in enumerate(subtitle_lines)
    )
    eyebrow_width = min(560, max(210, 38 + len(record["eyebrow"]) * 13))
    eyebrow_font_size = max(15, min(22, int((eyebrow_width - 36) / max(1, len(record["eyebrow"]) * 0.67))))
    icon_opacity = "0.18" if record["variant"] == "dark" else "0.10"

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-label="{xml(record['alt'])}">
  <defs>
    <style>
      @font-face {{ font-family: "EB Garamond OG"; src: url("../fonts-local/EBGaramond-Regular.ttf"); }}
      @font-face {{ font-family: "Source Sans 3 OG"; src: url("../fonts-local/SourceSans3-Regular.ttf"); }}
      @font-face {{ font-family: "Source Code Pro OG"; src: url("../fonts-local/SourceCodePro-Regular.ttf"); }}
    </style>
    <linearGradient id="spectrum-rule" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#5A7EB3"/><stop offset="34%" stop-color="#1B8278"/><stop offset="68%" stop-color="#9F5B5C"/><stop offset="100%" stop-color="#896092"/>
    </linearGradient>
  </defs>
  {background_svg(record["variant"])}
  {icon_markup(record["icon"], variant["icon"], icon_opacity)}
  {render_lockup(variant["lockup"])}
  <g transform="translate(70 76)">
    <rect width="{eyebrow_width}" height="44" rx="22" fill="{variant["eyebrow_bg"]}" opacity="0.96"/>
    <text x="18" y="29" font-family="Source Code Pro OG, ui-monospace, monospace" font-size="{eyebrow_font_size}" font-weight="700" letter-spacing="1.8" fill="{variant["eyebrow_text"]}">{xml(record["eyebrow"])}</text>
  </g>
  <text font-family="EB Garamond OG, Georgia, serif" font-size="{title_size}" font-weight="400" fill="{variant["title"]}">
    {title_tspans}
  </text>
  <text font-family="Source Sans 3 OG, Inter, Arial, sans-serif" font-size="34" font-weight="400" fill="{variant["subtitle"]}">
    {subtitle_tspans}
  </text>
  <text x="82" y="568" font-family="Source Code Pro OG, ui-monospace, monospace" font-size="30" font-weight="500" fill="{variant["route"]}">{xml(fit_route(record["display_route"]))}</text>
</svg>
"""


def clean_outputs() -> None:
    for directory, patterns in [(SVG_DIR, ("*.svg",)), (PNG_DIR, ("*.png",)), (WEBP_DIR, ("*.webp",))]:
        directory.mkdir(parents=True, exist_ok=True)
        for pattern in patterns:
            for path in directory.glob(pattern):
                path.unlink()
    GALLERY_DIR.mkdir(parents=True, exist_ok=True)


def render_assets(records: list[dict[str, Any]], make_png: bool, make_webp: bool) -> None:
    rsvg = shutil.which("rsvg-convert")
    if make_png and not rsvg:
        fail("rsvg-convert is required for PNG output")

    for record in records:
        svg_path = SVG_DIR / f"{record['slug']}.svg"
        svg_path.write_text(strip_trailing_whitespace(render_svg(record)), encoding="utf-8")
        if make_png:
            png_path = PNG_DIR / f"{record['slug']}.png"
            subprocess.run(
                [rsvg, "-w", str(CARD_WIDTH), "-h", str(CARD_HEIGHT), "-o", str(png_path), str(svg_path)],
                check=True,
            )
            if make_webp:
                webp_path = WEBP_DIR / f"{record['slug']}.webp"
                with Image.open(png_path) as image:
                    image.save(webp_path, "WEBP", quality=92, method=6)


def write_manifest(records: list[dict[str, Any]], include_webp: bool) -> None:
    cards: dict[str, dict[str, Any]] = {}
    for record in records:
        slug = record["slug"]
        entry = {
            "route": record["route"],
            "page_key": record.get("page_key"),
            "title": record["title"],
            "image": f"/assets/og/png/{slug}.png",
            "svg": f"/assets/og/svg/{slug}.svg",
            "alt": record["alt"],
            "width": CARD_WIDTH,
            "height": CARD_HEIGHT,
        }
        if include_webp:
            entry["webp"] = f"/assets/og/webp/{slug}.webp"
        cards[slug] = entry

    manifest = {
        "schema_version": 1,
        "source": "Site Atlas launch-critical pages plus _data/og/pages.yml curated overrides",
        "cards": cards,
    }
    GENERATED_MANIFEST.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")


def write_gallery(records: list[dict[str, Any]]) -> None:
    cards = "\n".join(
        f"""<article>
  <img src="../png/{xml(record['slug'])}.png" alt="{xml(record['alt'])}">
  <h2>{xml(record['title'])}</h2>
  <p><code>{xml(record['route'])}</code></p>
</article>"""
        for record in records
    )
    html_doc = f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Panta Rhei OG Card Gallery</title>
<style>
body {{ margin: 0; padding: 32px; font-family: system-ui, sans-serif; background: #f8f7f0; color: #17202b; }}
h1 {{ font: 400 42px Georgia, serif; margin: 0 0 24px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; }}
article {{ background: white; border: 1px solid #d8dfdf; border-radius: 10px; padding: 14px; box-shadow: 0 10px 30px rgba(22, 62, 100, .08); }}
img {{ display: block; width: 100%; height: auto; border-radius: 6px; }}
h2 {{ margin: 12px 0 4px; font-size: 18px; }}
p {{ margin: 0; color: #5b6772; }}
</style>
<h1>Panta Rhei OG Card Gallery</h1>
<div class="grid">
{cards}
</div>
</html>
"""
    (GALLERY_DIR / "index.html").write_text(html_doc, encoding="utf-8")


def check_assets(records: list[dict[str, Any]], require_png: bool, require_webp: bool) -> None:
    missing: list[str] = []
    for record in records:
        for directory, suffix, required in [
            (SVG_DIR, ".svg", True),
            (PNG_DIR, ".png", require_png),
            (WEBP_DIR, ".webp", require_webp),
        ]:
            path = directory / f"{record['slug']}{suffix}"
            if required and (not path.exists() or path.stat().st_size < 500):
                missing.append(str(path.relative_to(ROOT)))
    if missing:
        fail("missing or invalid generated assets: " + ", ".join(missing[:20]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--png", action="store_true")
    parser.add_argument("--webp", action="store_true")
    parser.add_argument("--gallery", action="store_true")
    parser.add_argument("--check", action="store_true", help="validate existing generated outputs")
    args = parser.parse_args()

    records = build_card_records()
    if not records:
        fail("no card records found")

    if args.check:
        check_assets(records, require_png=True, require_webp=True)
        print(f"OG generated assets validated: {len(records)} cards")
        return 0

    clean_outputs()
    render_assets(records, make_png=args.png or args.webp, make_webp=args.webp)
    write_manifest(records, include_webp=args.webp)
    if args.gallery:
        write_gallery(records)
    check_assets(records, require_png=args.png or args.webp, require_webp=args.webp)
    print(f"Generated {len(records)} OG cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

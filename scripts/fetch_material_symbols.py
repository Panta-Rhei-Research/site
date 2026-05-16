#!/usr/bin/env python3
"""Fetch the selected Material Symbols SVG files for OG card generation.

This helper is intentionally separate from the production generator. The
generator must be able to run without network access once the SVGs are vendored.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import yaml


ROOT = Path(__file__).resolve().parents[1]
TOKEN_MAP = ROOT / "_data" / "og" / "icon-token-map.yml"
OG_OVERRIDE_FILES = [
    ROOT / "_data" / "og" / "pages.yml",
    ROOT / "_data" / "og" / "sitemap_pages.yml",
]
OUT_DIR = ROOT / "assets" / "og" / "icons" / "material-symbols"
RAW_BASE = (
    "https://raw.githubusercontent.com/google/material-design-icons/master/"
    "symbols/web/{token}/materialsymbolsoutlined/{token}_24px.svg"
)


ALIASES = {
    # The briefing uses two editorial tokens that are not official Material
    # Symbols names. Keep the public token stable, but fetch a close symbol.
    "orbit": "orbit",
    "owl": "psychology",
}


def fail(message: str) -> None:
    print(f"material symbol fetch failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def collect_tokens() -> list[str]:
    data = yaml.safe_load(TOKEN_MAP.read_text(encoding="utf-8"))
    tokens: set[str] = set()

    def walk(value: object) -> None:
        if isinstance(value, dict):
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
        elif isinstance(value, str) and value.strip():
            token = value.strip()
            if token.startswith("http") or token in {"Google Material Symbols", "Outlined", "Apache-2.0"}:
                return
            tokens.add(token)

    walk(data)
    for override_file in OG_OVERRIDE_FILES:
        if not override_file.exists():
            continue
        override_data = yaml.safe_load(override_file.read_text(encoding="utf-8")) or {}
        for item in override_data.get("pages", []) or []:
            if isinstance(item, dict) and isinstance(item.get("icon"), str):
                tokens.add(item["icon"].strip())
    return sorted(tokens)


def fetch_svg(token: str) -> str:
    source_token = ALIASES.get(token, token)
    url = RAW_BASE.format(token=source_token)
    try:
        with urlopen(url, timeout=30) as response:
            if response.status != 200:
                fail(f"{token}: HTTP {response.status} from {url}")
            text = response.read().decode("utf-8")
    except HTTPError as exc:
        fail(f"{token}: HTTP {exc.code} from {url}")
    except URLError as exc:
        fail(f"{token}: {exc.reason}")
    if "<svg" not in text or "<path" not in text:
        fail(f"{token}: fetched file is not an SVG path asset")
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-existing", action="store_true")
    args = parser.parse_args()

    tokens = collect_tokens()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    missing = [token for token in tokens if not (OUT_DIR / f"{token}.svg").exists()]
    if args.check_existing:
        if missing:
            fail("missing vendored SVGs: " + ", ".join(missing))
        print(f"Material Symbols vendored: {len(tokens)}")
        return 0

    for token in tokens:
        path = OUT_DIR / f"{token}.svg"
        path.write_text(fetch_svg(token), encoding="utf-8")
        print(f"fetched {token} -> {path.relative_to(ROOT)}")

    print(f"Fetched {len(tokens)} Material Symbols SVGs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Assert that normal site builds do not depend on generated OG-card assets."""

from __future__ import annotations

import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"social preview separation assertion failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: assert_social_preview_separation.py <built-site-root>")

    site_root = Path(sys.argv[1])
    if not site_root.exists():
        fail(f"built site root does not exist: {site_root}")

    og_dir = site_root / "assets" / "og-cards"
    if og_dir.exists() and any(og_dir.rglob("*")):
        fail(f"normal build generated social-preview card assets at {og_dir}")

    offenders: list[str] = []
    for html_path in site_root.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="ignore")
        if "/assets/og-cards/" in text:
            offenders.append(str(html_path.relative_to(site_root)))
            if len(offenders) >= 20:
                break

    if offenders:
        fail(
            "normal build rendered references to generated social-preview cards: "
            + ", ".join(offenders)
        )

    print("social preview separation assertion passed")


if __name__ == "__main__":
    main()

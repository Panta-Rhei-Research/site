#!/usr/bin/env python3
"""Fail on visible deprecated v1 terminology in built public HTML."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


HIDDEN_TAGS = {"head", "script", "style", "template", "svg", "noscript"}
APPROVED_STATUSES = {"archive", "deprecated", "redirected"}


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_stack: list[bool] = []
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = {key.lower(): value or "" for key, value in attrs}
        classes = set(attr_map.get("class", "").split())
        hidden = (
            tag in HIDDEN_TAGS
            or "hidden" in attr_map
            or attr_map.get("aria-hidden", "").lower() == "true"
            or "sr-only" in classes
            or "visually-hidden" in classes
        )
        self.hidden_stack.append(hidden)

    def handle_endtag(self, tag: str) -> None:
        if self.hidden_stack:
            self.hidden_stack.pop()

    def handle_data(self, data: str) -> None:
        if not any(self.hidden_stack) and data.strip():
            self.parts.append(data)

    @property
    def text(self) -> str:
        return " ".join(" ".join(self.parts).split())


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def route_for_html(path: Path, built_root: Path) -> str:
    rel = path.relative_to(built_root).as_posix()
    if rel == "index.html":
        return "/"
    return "/" + rel.removesuffix("index.html")


def visible_text(path: Path) -> str:
    parser = VisibleTextParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
    parser.close()
    return parser.text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("built_root", type=Path)
    parser.add_argument("--site-root", type=Path, default=Path("."))
    args = parser.parse_args()

    route_index = load_json(args.site_root / "_data/site_atlas/route_index.json")
    terminology = load_json(args.site_root / "_data/site_atlas/terminology.json")
    route_status = {route: page.get("status") for route, page in route_index.items()}
    patterns = [
        (
            item["term"],
            item.get("replacement", ""),
            re.compile(re.escape(item["term"]), re.IGNORECASE),
        )
        for item in terminology.get("deprecated_terms", [])
        if item.get("term")
    ]
    findings: list[str] = []
    for html in sorted(args.built_root.rglob("*.html")):
        route = route_for_html(html, args.built_root)
        if route_status.get(route) in APPROVED_STATUSES or route.startswith("/changelog/"):
            continue
        text = visible_text(html)
        for term, replacement, pattern in patterns:
            match = pattern.search(text)
            if not match:
                continue
            start = max(0, match.start() - 90)
            end = min(len(text), match.end() + 90)
            findings.append(f"{route}: {term!r} should be {replacement!r}. Snippet: {text[start:end]}")

    if findings:
        print("Site Atlas visible terminology check failed:")
        for finding in findings[:100]:
            print(f"- {finding}")
        if len(findings) > 100:
            print(f"... {len(findings) - 100} more findings")
        return 1
    print("Site Atlas visible terminology check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

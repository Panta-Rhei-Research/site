#!/usr/bin/env python3
"""Assertions for the v2.3 Corpus projection architecture cleanup."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing expected file: {path}")
    return path.read_text(encoding="utf-8")


def html_path(site: Path, url: str) -> Path:
    return site / url.strip("/") / "index.html"


def assert_one_h1(path: Path) -> None:
    html = read(path)
    count = len(re.findall(r"<h1\b", html, flags=re.I))
    if count != 1:
        fail(f"{path} should contain exactly one h1, found {count}")


def assert_redirect(site: Path, old_url: str, new_url: str) -> None:
    html = read(html_path(site, old_url))
    if f'content="0; url={new_url}"' not in html:
        fail(f"{old_url} missing meta redirect to {new_url}")
    if f'href="https://panta-rhei.site{new_url}"' not in html:
        fail(f"{old_url} missing canonical redirect target {new_url}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: assert_v2_3_corpus_projection.py _site", file=sys.stderr)
        return 2

    built = Path(sys.argv[1]).resolve()
    repo = Path(__file__).resolve().parents[1]

    books = json.loads(read(repo / "_data/publications/books.json"))
    parts = json.loads(read(repo / "_data/publications/parts.json"))
    chapters = json.loads(read(repo / "_data/publications/chapters.json"))

    if len(books) != 7:
        fail(f"Expected 7 books, found {len(books)}")
    if len(parts) != 79:
        fail(f"Expected 79 parts, found {len(parts)}")
    if len(chapters) != 535:
        fail(f"Expected 535 chapters, found {len(chapters)}")

    for book in books:
        corpus_url = book.get("corpus_url", "")
        if not corpus_url.startswith("/corpus/monographs/book-"):
            fail(f"{book['id']} has invalid corpus_url: {corpus_url}")
        if not book.get("url", "").startswith("/publications/books/book-"):
            fail(f"{book['id']} publication artifact URL changed unexpectedly")

    for collection_name, items in [("parts", parts), ("chapters", chapters)]:
        for item in items:
            if not item.get("url", "").startswith("/corpus/monographs/"):
                fail(f"{collection_name} item {item.get('id')} not canonicalized to Corpus")
            if not item.get("legacy_publication_url", "").startswith("/publications/books/"):
                fail(f"{collection_name} item {item.get('id')} missing legacy publication URL")

    required_urls = [
        "/corpus/monographs/",
        "/corpus/monographs/book-i/",
        "/corpus/monographs/book-i/part-01-the-coherence-kernel/",
        "/corpus/monographs/book-i/part-01-the-coherence-kernel/chapter-02-the-five-generators/",
        "/publications/books/book-i/",
        "/publications/research-monographs/",
        "/corpus/",
    ]
    for url in required_urls:
        assert_one_h1(html_path(built, url))

    assert_redirect(
        built,
        "/publications/books/book-i/part-01-the-coherence-kernel/",
        "/corpus/monographs/book-i/part-01-the-coherence-kernel/",
    )
    assert_redirect(
        built,
        "/publications/books/book-i/part-01-the-coherence-kernel/chapter-02-the-five-generators/",
        "/corpus/monographs/book-i/part-01-the-coherence-kernel/chapter-02-the-five-generators/",
    )
    assert_redirect(built, "/framework/about/", "/corpus/")
    assert_redirect(
        built,
        "/framework/prior-art/",
        "/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/",
    )

    corpus_root = read(html_path(built, "/corpus/"))
    if "Corpus Monographs" not in corpus_root:
        fail("Corpus root should foreground Corpus Monographs")

    publication_book = read(html_path(built, "/publications/books/book-i/"))
    if "Open Corpus edition" not in publication_book:
        fail("Book artifact page should link to the Corpus edition")

    active_html = [
        path for path in built.rglob("*.html")
        if "/framework/" not in path.as_posix() and "/changelog/" not in path.as_posix()
    ]
    offenders = []
    invalid_monograph_links = []
    for path in active_html:
        html = path.read_text(encoding="utf-8", errors="ignore")
        if "Framework Modules" in html or "framework modules" in html or 'href="/framework/' in html:
            offenders.append(str(path.relative_to(built)))
            if len(offenders) >= 10:
                break
        for match in re.finditer(r'href="(?:https://panta-rhei\.site)?(/corpus/monographs/[^"#?]*)"', html):
            link = match.group(1)
            if link != "/corpus/monographs/" and not link.startswith("/corpus/monographs/book-"):
                invalid_monograph_links.append(f"{path.relative_to(built)} -> {link}")
                if len(invalid_monograph_links) >= 10:
                    break
    if offenders:
        fail("Active pages still expose legacy framework-module language/links: " + ", ".join(offenders))
    if invalid_monograph_links:
        fail("Active pages link to non-canonical Corpus Monograph slug routes: " + ", ".join(invalid_monograph_links))

    print(
        "v2.3 corpus projection assertions passed: "
        f"{len(books)} books, {len(parts)} parts, {len(chapters)} chapters"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

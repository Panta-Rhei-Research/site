#!/usr/bin/env python3
"""Assert that v4 archive/prune legacy surfaces are reduced to compatibility stubs."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


RETIRED_SOURCE_PATHS = [
    "_problem_ledger",
    "_data/problem_ledger",
    "_data/problem_answers",
    "assets/data/problem-ledger",
    "assets/data/problem-answers",
    "_layouts/problem-ledger-item.html",
]

FORBIDDEN_TEMPLATE_PATTERNS = [
    "site.data.problem_answers",
    "site.data.problem_ledger",
    "site.problem_ledger",
    "_data/problem_answers",
    "_data/problem_ledger",
]

RETIRED_BUILT_ROUTES = [
    "agenda/problem-ledger/physics/hubble-tension/index.html",
    "agenda/problem-ledger/life/origin-of-life/index.html",
    "results/problem-ledger-answers/physics/hubble-tension/index.html",
    "results/problem-ledger-answers/mathematics/riemann-hypothesis/index.html",
    "framework/about/index.html",
    "framework/mathematics-coherence-kernel/index.html",
]

STUB_ROUTES = [
    "agenda/problem-ledger/index.html",
    "agenda/problem-ledger-source-policy/index.html",
    "results/problem-ledger-answers/index.html",
    "results/problem-answers/index.html",
    "results/problem-ledger/index.html",
    "results/by-problem/index.html",
    "framework/index.html",
    "framework/prior-art/index.html",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def assert_redirect_stub(path: Path, target: str) -> None:
    if not path.exists():
        raise AssertionError(f"compatibility stub missing: {path}")
    markup = read(path)
    if target not in markup:
        raise AssertionError(f"{path}: does not reference redirect target {target}")
    if "noindex" not in markup.lower():
        raise AssertionError(f"{path}: missing noindex marker")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("built_root", type=Path)
    parser.add_argument("--site-root", type=Path, default=Path("."))
    args = parser.parse_args()

    site_root = args.site_root.resolve()
    built_root = args.built_root.resolve()
    errors: list[str] = []

    for rel in RETIRED_SOURCE_PATHS:
        if (site_root / rel).exists():
            errors.append(f"retired source path still exists: {rel}")

    framework_files = sorted(path.relative_to(site_root).as_posix() for path in (site_root / "framework").rglob("*.md"))
    expected_framework = ["framework/index.md", "framework/prior-art/index.md"]
    if framework_files != expected_framework:
        errors.append(f"framework source should contain only redirect stubs; found {framework_files}")

    for rel in RETIRED_BUILT_ROUTES:
        if (built_root / rel).exists():
            errors.append(f"retired full-content route still builds: /{rel.removesuffix('index.html')}")

    for rel in STUB_ROUTES:
        if not (built_root / rel).exists():
            errors.append(f"expected compatibility route missing: /{rel.removesuffix('index.html')}")

    stub_targets = {
        "agenda/problem-ledger/index.html": "/agenda/structural-challenge-ledger/",
        "agenda/problem-ledger-source-policy/index.html": "/agenda/structural-challenge-ledger/source-policy/",
        "results/problem-ledger-answers/index.html": "/results/challenge-responses/",
        "results/problem-answers/index.html": "/results/challenge-responses/",
        "results/problem-ledger/index.html": "/results/challenge-responses/",
        "results/by-problem/index.html": "/results/challenge-responses/",
        "framework/index.html": "/corpus/",
        "framework/prior-art/index.html": "/program/research-agenda/kernel-model-reality/related-approaches/deep-comparison/",
    }
    for rel, target in stub_targets.items():
        try:
            assert_redirect_stub(built_root / rel, target)
        except AssertionError as exc:
            errors.append(str(exc))

    active_sources = list((site_root / "_includes").rglob("*.html")) + list((site_root / "_layouts").rglob("*.html"))
    for path in active_sources:
        text = read(path)
        for pattern in FORBIDDEN_TEMPLATE_PATTERNS:
            if pattern in text:
                errors.append(f"{path.relative_to(site_root)}: forbidden legacy reference {pattern!r}")

    worker = read(site_root / "workers/site-edge-headers.js")
    for phrase in (
        'pathname.startsWith("/agenda/problem-ledger/")',
        'pathname.startsWith("/program/research-agenda/problem-ledger/")',
        'pathname.startsWith("/results/problem-ledger-answers/")',
        'pathname.startsWith("/framework/")',
    ):
        if phrase not in worker:
            errors.append(f"worker redirect rule missing: {phrase}")

    hubble = built_root / "results/problem/hubble-tension/index.html"
    if hubble.exists():
        markup = read(hubble)
        if "Related Challenge Responses" not in re.sub(r"\s+", " ", markup):
            errors.append("Hubble result page no longer exposes Related Challenge Responses")
        if "/results/problem-ledger-answers/" in markup:
            errors.append("Hubble result page still links to retired Problem Ledger Answers")

    if errors:
        print("Site Atlas archive/prune assertion failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Site Atlas archive/prune assertion passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Materialize generated Jekyll proxy pages for dossier exports."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CI installs PyYAML.
    raise SystemExit("PyYAML is required: python3 -m pip install PyYAML") from exc


SKIP_DIRS = {
    ".git",
    ".github",
    ".jekyll-cache",
    ".sass-cache",
    "_dossier_exports",
    "_site",
    "node_modules",
    "vendor",
}


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Missing YAML input: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise SystemExit(f"Expected mapping in {path}")
    return data


def split_front_matter(text: str, path: Path) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise SystemExit(f"Malformed front matter in {path}")
    front = yaml.safe_load(parts[1]) or {}
    if not isinstance(front, dict):
        raise SystemExit(f"Expected front matter mapping in {path}")
    return front, parts[2]


def normalize_route(route: str) -> str:
    if not route.startswith("/"):
        route = f"/{route}"
    if not route.endswith("/"):
        route = f"{route}/"
    return route


def slug_from_route(route: str) -> str:
    route = normalize_route(route)
    slug = route.strip("/").replace("/", "--")
    return slug or "home"


def relative_source_for_page(site_root: Path, path: Path) -> str:
    return str(path.relative_to(site_root)).replace("\\", "/")


def discover_front_matter_entries(site_root: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for path in site_root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(site_root).parts):
            continue
        text = path.read_text(encoding="utf-8")
        front, _body = split_front_matter(text, path)
        if front.get("dossier") is not True:
            continue
        permalink = front.get("permalink")
        if not permalink:
            inferred = "/" + str(path.relative_to(site_root).with_suffix("")).replace("\\", "/")
            inferred = re.sub(r"/index$", "/", inferred)
            permalink = inferred
        entries.append(
            {
                "route": normalize_route(str(permalink)),
                "source": relative_source_for_page(site_root, path),
                "kind": front.get("dossier_kind", front.get("type", "Dossier page")),
                "review_angle": front.get("dossier_review_angle", "General review"),
                "priority": front.get("dossier_priority", 1000),
            }
        )
    return entries


def public_entry(scope: dict[str, Any], raw_entry: dict[str, Any], site_root: Path, generated_at: str) -> dict[str, Any]:
    route = normalize_route(str(raw_entry["route"]))
    source_path = Path(str(raw_entry["source"]))
    source_abs = site_root / source_path
    if not source_abs.exists():
        raise SystemExit(f"Dossier source does not exist: {source_path}")
    front, _body = split_front_matter(source_abs.read_text(encoding="utf-8"), source_abs)
    slug = slug_from_route(route)
    public_site_url = str(scope.get("public_site_url", "https://panta-rhei.site")).rstrip("/")
    title = str(front.get("title") or front.get("page_title") or slug.replace("--", " ").title())
    description = str(front.get("summary_short") or front.get("summary") or front.get("description") or "").strip()
    status = str(raw_entry.get("status") or front.get("dossier_status") or front.get("build_status_label") or front.get("status") or "Canonical")
    kind = str(raw_entry.get("kind") or front.get("dossier_kind") or front.get("type") or "Dossier page")
    review_angle = str(raw_entry.get("review_angle") or front.get("dossier_review_angle") or "General review")
    markdown_path = f"/exports/markdown/{slug}.md"
    typst_path = f"/exports/typst/{slug}.typ"
    pdf_path = f"/exports/pdf/{slug}-dossier.pdf"
    return {
        "slug": slug,
        "route": route,
        "url": f"{public_site_url}{route}",
        "title": title,
        "description": description,
        "kind": kind,
        "status": status,
        "review_angle": review_angle,
        "source_path": str(source_path).replace("\\", "/"),
        "priority": int(raw_entry.get("priority", 1000)),
        "markdown_path": markdown_path,
        "typst_path": typst_path,
        "pdf_path": pdf_path,
        "generated_at": generated_at,
    }


def proxy_front_matter(source_front: dict[str, Any], entry: dict[str, Any]) -> dict[str, Any]:
    front = dict(source_front)
    front.update(
        {
            "layout": "dossier_markdown",
            "permalink": entry["markdown_path"],
            "sitemap": False,
            "dossier_slug": entry["slug"],
            "dossier_title": entry["title"],
            "dossier_description": entry["description"],
            "dossier_canonical_url": entry["url"],
            "dossier_status": entry["status"],
            "dossier_review_angle": entry["review_angle"],
            "dossier_source_path": entry["source_path"],
        }
    )
    return front


def write_proxy(site_root: Path, entry: dict[str, Any]) -> None:
    source_abs = site_root / entry["source_path"]
    source_front, body = split_front_matter(source_abs.read_text(encoding="utf-8"), source_abs)
    out_path = site_root / "_dossier_exports" / "markdown" / f"{entry['slug']}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    front = proxy_front_matter(source_front, entry)
    out_path.write_text(
        "---\n"
        + yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
        + "---\n\n"
        + body.strip()
        + "\n",
        encoding="utf-8",
    )


def write_manifest(site_root: Path, scope: dict[str, Any], entries: list[dict[str, Any]], generated_at: str) -> None:
    manifest = {
        "schema_version": "1.0",
        "scope_id": scope.get("scope_id", "dossier-scope"),
        "title": scope.get("title", "Dossier exports"),
        "artifact_policy": scope.get("artifact_policy", "ci_generated"),
        "generated_at": generated_at,
        "entries": sorted(entries, key=lambda item: (item.get("priority", 1000), item["route"])),
    }
    manifest["entries_by_path"] = {entry["route"]: entry for entry in manifest["entries"]}
    manifest["entries_by_slug"] = {entry["slug"]: entry for entry in manifest["entries"]}
    manifest_path = site_root / "_data" / "dossier_manifest.yml"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def materialize(site_root: Path, include_front_matter: bool) -> None:
    scope = load_yaml(site_root / "_data" / "dossier_scope.yml")
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    raw_entries = list(scope.get("entries", []))
    if include_front_matter:
        raw_entries.extend(discover_front_matter_entries(site_root))

    seen_routes: set[str] = set()
    entries: list[dict[str, Any]] = []
    for raw_entry in raw_entries:
        route = normalize_route(str(raw_entry["route"]))
        if route in seen_routes:
            continue
        seen_routes.add(route)
        entries.append(public_entry(scope, raw_entry, site_root, generated_at))

    exports_root = site_root / "_dossier_exports"
    if exports_root.exists():
        shutil.rmtree(exports_root)
    manifest_path = site_root / "_data" / "dossier_manifest.yml"
    if manifest_path.exists():
        manifest_path.unlink()

    for entry in entries:
        write_proxy(site_root, entry)
    write_manifest(site_root, scope, entries, generated_at)
    print(f"Materialized {len(entries)} dossier proxy pages")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", default=".", help="Site repository root")
    parser.add_argument(
        "--include-front-matter",
        action="store_true",
        help="Also include pages with dossier: true front matter",
    )
    args = parser.parse_args()
    materialize(Path(args.site_root).resolve(), args.include_front_matter)
    return 0


if __name__ == "__main__":
    sys.exit(main())

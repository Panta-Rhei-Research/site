#!/usr/bin/env python3
"""
fix_delta_v2.py — QA Delta Sprint v2 fixes.

P0.1: Convert Markdown body links to use {{ relative_url }} Liquid filter.
P0.2: Add lane: frontmatter to registry/impact/engage descendant pages.
P1.1: Fix publication fidelity (counts, encoding, Genesis).
P1.3: Fix "and more" imprecise language in results.
"""

import os
import re
import glob

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Known internal path prefixes that need baseurl treatment
INTERNAL_PREFIXES = [
    "/results/", "/registry/", "/impact/", "/engage/", "/publications/",
    "/framework/", "/research-program/", "/verify/",
]

# ---------------------------------------------------------------------------
# P0.1: Fix Markdown body links to use relative_url
# ---------------------------------------------------------------------------

def fix_body_links(filepath):
    """Convert Markdown body links from ](/path/) to ]({{ '/path/' | relative_url }}).
    Only processes body content (after frontmatter), not frontmatter values."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return 0

    # Split frontmatter and body
    end_idx = content.index("---", 3)
    frontmatter = content[:end_idx + 3]
    body = content[end_idx + 3:]

    # Pattern: ](/ followed by a known prefix, ending with )
    # But NOT already wrapped in {{ ... | relative_url }}
    count = 0

    def replace_link(m):
        nonlocal count
        path = m.group(1)
        # Skip if already uses relative_url
        if "relative_url" in path:
            return m.group(0)
        # Skip external links
        if path.startswith("http"):
            return m.group(0)
        # Only fix internal links matching known prefixes
        for prefix in INTERNAL_PREFIXES:
            if path.startswith(prefix):
                count += 1
                return f"]({{{{ '{path}' | relative_url }}}})"
        return m.group(0)

    # Match Markdown link targets: ](/something/...)
    new_body = re.sub(r'\]\((/[^)]+)\)', replace_link, body)

    if count > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + new_body)

    return count


def fix_all_body_links():
    """Fix body links across all .md files."""
    print("=" * 60)
    print("P0.1: Fixing Markdown body links for baseurl")
    print("=" * 60)

    total = 0
    files_fixed = 0

    # All .md files in the site (except _site/)
    for root, dirs, files in os.walk(SITE_DIR):
        # Skip build output and hidden dirs
        dirs[:] = [d for d in dirs if d not in ("_site", ".git", "node_modules", "vendor", "scripts")]
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            count = fix_body_links(path)
            if count > 0:
                rel = os.path.relpath(path, SITE_DIR)
                print(f"  {rel}: {count} links fixed")
                total += count
                files_fixed += 1

    print(f"\n  Total: {total} links in {files_fixed} files")
    return total


# ---------------------------------------------------------------------------
# P0.2: Add lane: frontmatter to descendant pages
# ---------------------------------------------------------------------------

LANE_PATTERNS = {
    "registry": [
        "registry/books/*.md",
        "registry/dashboards/*.md",
        "registry/object/*.md",
    ],
    "impact": [
        "impact/portfolio/*.md",
        "impact/papers/*.md",
        "impact/by-*.md",
    ],
    "engage": [
        "engage/*.md",
    ],
}


def add_lane_to_file(filepath, lane):
    """Add lane: field to frontmatter if missing."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return False

    # Check if lane already exists
    end_idx = content.index("---", 3)
    fm = content[3:end_idx]

    if re.search(r'^lane:', fm, re.MULTILINE):
        return False  # already has lane

    # Insert lane after layout line (or at start of frontmatter)
    lines = fm.split("\n")
    insert_idx = 1  # after first line
    for i, line in enumerate(lines):
        if line.strip().startswith("layout:"):
            insert_idx = i + 1
            break

    lines.insert(insert_idx, f"lane: {lane}")
    new_fm = "\n".join(lines)
    new_content = "---" + new_fm + "---" + content[end_idx + 3:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def fix_lane_metadata():
    """Add lane: frontmatter to descendant pages."""
    print("\n" + "=" * 60)
    print("P0.2: Adding lane metadata to descendant pages")
    print("=" * 60)

    total = 0
    for lane, patterns in LANE_PATTERNS.items():
        lane_count = 0
        for pattern in patterns:
            full_pattern = os.path.join(SITE_DIR, pattern)
            for path in glob.glob(full_pattern):
                if add_lane_to_file(path, lane):
                    lane_count += 1
        if lane_count > 0:
            print(f"  {lane}: {lane_count} pages updated")
            total += lane_count

    print(f"\n  Total: {total} pages updated")
    return total


# ---------------------------------------------------------------------------
# P1.1: Publications fidelity fixes
# ---------------------------------------------------------------------------

def fix_publication_fidelity():
    """Fix specific publication fidelity issues."""
    print("\n" + "=" * 60)
    print("P1.1: Fixing publication fidelity issues")
    print("=" * 60)

    fixes = 0

    # Fix Book I: "seventy-three chapters" → "seventy-nine chapters"
    book_i_prologue = os.path.join(
        SITE_DIR, "publications/books/book-i/part-00-earned-foundations/index.md"
    )
    if os.path.isfile(book_i_prologue):
        with open(book_i_prologue, "r", encoding="utf-8") as f:
            content = f.read()
        if "seventy-three chapters" in content:
            content = content.replace("seventy-three chapters", "seventy-nine chapters")
            with open(book_i_prologue, "w", encoding="utf-8") as f:
                f.write(content)
            print("  Fixed Book I prologue: seventy-three → seventy-nine chapters")
            fixes += 1

    # Also fix in book-i.md if present
    book_i_page = os.path.join(SITE_DIR, "publications/books/book-i.md")
    if os.path.isfile(book_i_page):
        with open(book_i_page, "r", encoding="utf-8") as f:
            content = f.read()
        if "seventy-three chapters" in content:
            content = content.replace("seventy-three chapters", "seventy-nine chapters")
            with open(book_i_page, "w", encoding="utf-8") as f:
                f.write(content)
            print("  Fixed Book I page: seventy-three → seventy-nine chapters")
            fixes += 1

    # Fix Schrödinger encoding across all publication pages
    for root, dirs, files in os.walk(os.path.join(SITE_DIR, "publications")):
        dirs[:] = [d for d in dirs if d != "_site"]
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            # Fix various broken Schrödinger encodings
            new_content = content
            new_content = new_content.replace('Schr\\"odinger', 'Schrödinger')
            new_content = new_content.replace('Schr"odinger', 'Schrödinger')
            new_content = new_content.replace("Schr\\'odinger", "Schrödinger")
            # Fix other common LaTeX encoding issues
            new_content = new_content.replace('\\&', '&')
            new_content = new_content.replace("``", "\u201c")  # opening smart quote
            new_content = new_content.replace("''", "\u201d")  # closing smart quote
            if new_content != content:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
                rel = os.path.relpath(path, SITE_DIR)
                print(f"  Fixed encoding: {rel}")
                fixes += 1

    print(f"\n  Total fidelity fixes: {fixes}")
    return fixes


# ---------------------------------------------------------------------------
# P1.3: Results copy precision
# ---------------------------------------------------------------------------

def fix_results_precision():
    """Remove 'and more' and similar imprecise language from results pages."""
    print("\n" + "=" * 60)
    print("P1.3: Fixing results copy precision")
    print("=" * 60)

    fixes = 0
    results_dir = os.path.join(SITE_DIR, "results")

    for f in os.listdir(results_dir):
        if not f.endswith(".md"):
            continue
        path = os.path.join(results_dir, f)
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()

        new_content = content
        # Remove "and more" after count statements
        new_content = re.sub(r', and more\.', '.', new_content)
        new_content = re.sub(r' and more\.', '.', new_content)

        if new_content != content:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_content)
            print(f"  Fixed: {f}")
            fixes += 1

    print(f"\n  Total precision fixes: {fixes}")
    return fixes


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    fix_all_body_links()
    fix_lane_metadata()
    fix_publication_fidelity()
    fix_results_precision()

    print("\n" + "=" * 60)
    print("ALL DELTA FIXES COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()

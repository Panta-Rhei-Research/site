---
title: "FAQ projection — /faq/ index, 5 layer pages, 73 corpus-mirrored entities"
date: 2026-05-09
change_type: "site-release"
summary_short: "Adds the FAQ projection surface that mirrors the 73 canonical FAQ entities from corpus/faqs/. Ships /faq/ index, 5 layer pages (First Contact, First Orientation, Journalist DD, Technical Credibility, Expert Handoff), 6 reusable Liquid includes for embedding FAQs into other pages, JSON-LD FAQPage emit, and a sync script."
affected_lanes:
  - support
right_rail:
  toc: false
  related:
    - title: "FAQ"
      url: /faq/
    - title: "Discover"
      url: /discover/
    - title: "Verify"
      url: /verify/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "May 2026"
---

## Changes

Closes the FAQ entity collection loop. The corpus repo owns the canonical entities (corpus#59 merged 2026-05-09); this site PR ships the projection surface.

> **The Corpus owns the FAQ entities. The website renders FAQ projections.**

### What lands

- **`/faq/`** — main index with 5 layer overview cards, "Five-minute orientation" featured strip (FAQ-FC-001 through FAQ-OR-002), and the full 73-entry accordion stack grouped by layer.
- **5 layer pages** at `/faq/first-contact/`, `/faq/first-orientation/`, `/faq/journalist-due-diligence/`, `/faq/technical-credibility/`, `/faq/expert-handoff/` — each renders the corresponding layer's entries with intro, layer nav, and read-next links.
- **6 reusable Liquid includes** (`_includes/faqs/`):
  - `faq-list.html` — universal renderer with `layer` / `audience` / `category` / `ids` / `limit` / `style` parameters
  - `faq-accordion.html` — single entry as native `<details>`/`<summary>` (no JS needed)
  - `faq-card.html` — single entry as a compact card linking to the layer page
  - `faq-related-links.html` — render an entry's related_pages as inline link buttons
  - `faq-jsonld.html` — emit schema.org FAQPage JSON-LD (only on full FAQ pages, not embeds)
  - `faq-layer-nav.html` — pill row across the 5 layers + main index
- **`_data/faqs/`** — mirrored from corpus/faqs/ via the new `scripts/sync_faqs_from_corpus.py` (auto-generates `index.yml` with counts and ID rosters)
- **`_sass/_faq.scss`** — design-system aligned styles (paper-50 surface, 8px radius, native accordion, lane-token left edge-rule, reduced-motion override)

### Layer counts

| Layer | Page | Entries |
|---:|---|---:|
| 0 First Contact | `/faq/first-contact/` | 7 |
| 1 First Orientation | `/faq/first-orientation/` | 12 |
| 2 Journalist / Editor Due Diligence | `/faq/journalist-due-diligence/` | 18 |
| 3 Technical Credibility | `/faq/technical-credibility/` | 20 |
| 4 Expert Handoff | `/faq/expert-handoff/` | 16 |
| **Total** | | **73** |

### Layer 4 Expert Handoff

Each entry surfaces a candidate expert type and a **bounded first question** to ask them — the question they can actually answer with their own discipline's tools, not the program's full claim set. This shows in a dedicated highlighted block within each accordion entry.

### Embed pattern (for follow-up wave)

The `faq-list` include is parameterized so the next wave can replace duplicate FAQ prose on Discover, Journalist FAQ, Verify, Review Kit, Media Kit, etc.:

```liquid
{% raw %}{% include faqs/faq-list.html layer=0 limit=5 audience="journalist" %}
{% include faqs/faq-list.html category="taulib,custom_axioms" %}
{% include faqs/faq-list.html ids="FAQ-FC-001,FAQ-FC-002,FAQ-FC-003" %}{% endraw %}
```

Page-integration embeds (sprint 3 in the briefing) are deferred to a follow-up PR.

### Sync model

- `scripts/sync_faqs_from_corpus.py` mirrors corpus/faqs/*.yml → site/_data/faqs/
- Resolves corpus root via `--corpus-root` flag, `PRRP_CORPUS_ROOT` env, or `../corpus`
- Writes `_data/faqs/index.yml` with per-layer counts and a global ID roster
- Validates each YAML parses and has `faqs` array before copying

### Progressive enhancement

- All 73 entries render server-side
- Native `<details>`/`<summary>` accordion — works without JS, screen-reader friendly
- `prefers-reduced-motion: reduce` disables transitions
- ARIA labels on all major sections; layer-aware `aria-labelledby`

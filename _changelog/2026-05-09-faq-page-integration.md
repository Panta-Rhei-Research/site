---
title: "FAQ page integration — embed entities into 7 surfaces + create Review Kit"
date: 2026-05-09
change_type: "site-release"
summary_short: "Embeds the canonical 73-entry FAQ entity collection into 7 existing site surfaces (Homepage, Discover, Verify, Corpus, Results, Journalist FAQ, Media Kit) via the faq-list include, and creates the missing /media/review-kit/ page that journalist_due_diligence FAQ entries reference."
affected_lanes:
  - discover
  - corpus
  - results
  - verify
  - support
right_rail:
  toc: false
  related:
    - title: "FAQ"
      url: /faq/
    - title: "Review Kit"
      url: /media/review-kit/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "May 2026"
---

## Changes

Sprint 3 of the FAQ entity collection workstream (briefing §16). The `/faq/` projection surface (PR #153) is now wired into the broader site so structured FAQ entities replace duplicated prose where it existed.

### Additive embeds (5 pages)

These pages previously had no FAQ-style prose. The embeds are pure additions.

| Page | Embed | What it surfaces |
|---|---|---|
| **Homepage** (`/`) | `ids="FAQ-FC-001..005"` | New "First-contact questions" section right after the hero, before route-routing |
| **Discover** (`/discover/`) | `layer=0` + `layer=1` | Two FAQ subsections: First Contact (7 entries) + First Orientation (12 entries), placed before "Deep links" |
| **Verify** (`/verify/`) | `layer=3 limit=10` | Technical Credibility FAQ — TauLib, sorry, custom axioms, Mathlib, build reproduction, release manifest |
| **Corpus** (`/corpus/`) | curated 4 IDs | What is the Corpus / Registry vs TauLib / count drift / how to cite |
| **Results** (`/results/`) | curated 7 IDs | Are Results accepted / Biggest claims / ι_τ / fitting / hinge failure / where it can fail / formalization scope |

### Prose replacements (2 pages)

Per the wave's policy of "delete duplicate prose, keep only the include":

- **Journalist FAQ** (`/media/journalist-faq/`) — 4 sections (~85 lines of prose) replaced with 3 structured includes covering First Contact (`FAQ-FC-*`), Journalist Due Diligence (`FAQ-JD-*`), and Expert Handoff (`FAQ-EH-*`). Press-specific sections retained: citation discipline, quotes, embargo policy, headshots, story angles, contact.
- **Media Kit** (`/media/`) — "What journalists can responsibly say" + "What should not be said" lists replaced with a Responsible Coverage embed (9 entries spanning Journalist DD + the Theory-of-Everything framing entries).

### New page

- **Review Kit** (`/media/review-kit/`) — was referenced 5+ times by `journalist_due_diligence.yml` related_pages but didn't yet exist. Now ships as a bounded-question kit for editors and journalists routing claims to expert reviewers. Surfaces the full Layer 4 Expert Handoff (16 entries) plus a curated Layer 3 Technical Credibility subset (8 entries). Each entry pairs a candidate expert type with the bounded first question to ask them.

### How the embeds work

All 12 `faq-list` includes across the 8 pages reference IDs that exist in `_data/faqs/`. The `faq-list` Liquid include accepts `layer`, `audience`, `category`, `ids`, `limit`, and `style` parameters; this PR uses all of them in different combinations. Native `<details>`/`<summary>` accordions remain JS-free.

### Source-of-truth discipline preserved

> The Corpus owns the FAQ entities. The website renders FAQ projections.

All embedded prose is mirrored from `corpus/faqs/`. To edit any answer: change it in the corpus repo, then re-run `python3 scripts/sync_faqs_from_corpus.py` and rebuild. No prose is now duplicated between FAQ entities and these surfaces.

### Validation

- ✓ All 12 `faq-list` include references map to existing FAQ IDs (73/73 IDs in the data).
- ✓ The 5 layer pages and `/faq/` master index from PR #153 are unchanged.
- ✓ Native `<details>` accordions render server-side; no new JS dependency.

### Files

| Path | Type |
|---|---|
| `index.md` | modified — Homepage FAQ section |
| `discover/index.md` | modified — First Contact + First Orientation embeds |
| `verify/index.md` | modified — Technical Credibility embed |
| `corpus/index.md` | modified — Corpus FAQ section |
| `results/index.md` | modified — Results FAQ section |
| `media/journalist-faq.md` | modified — duplicate prose replaced with structured embeds |
| `media/index.md` | modified — Responsible Coverage embed replaces two bullet lists |
| `media/review-kit.md` | new — Review Kit page (Layer 4 + curated Layer 3) |
| `_changelog/2026-05-09-faq-page-integration.md` | new — release note |

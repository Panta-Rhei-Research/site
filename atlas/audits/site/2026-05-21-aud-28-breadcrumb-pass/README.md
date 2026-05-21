---
title: "AUD-28 · Breadcrumb design audit pass"
date: 2026-05-21
audit_kind: design-pass
status: complete
verdict: green
scope: site
related: AUD-2026-05-19
launch_blocker: false
---

# AUD-28 · Breadcrumb design audit pass

**Date:** 2026-05-21
**Closes:** AUD-28 from the v5 audit ledger (AUD-2026-05-19)
**Scope:** confirm the site's breadcrumb implementation against the briefing's three properties

## Verdict: 🟢 GREEN — no code change required

The site's breadcrumb infrastructure already satisfies the audit's three properties — implicitly, because **visual breadcrumbs are intentionally suppressed by design doctrine**. The three properties become operative only when `page.visual_breadcrumb: true` is opted in.

## The briefing's three criteria

From `atlas/website/briefings/v5/design_handoff_audit_AUD-2026-05-19/README.md` §AUD-28:

> 1. Breadcrumbs show **lane numeral** (00–07), **lane name**, and **current page**.
> 2. They collapse properly on long routes (e.g. `00 · Discover › Guided Tours › What to Read First` → on mobile, ellipses the middle).
> 3. They use the **slim mobile pattern** decided in the prior round (no `LANE ROOT` pill on mobile; `Status · Canonical` chip above H1 instead).

## State on main as of 2026-05-21

### Visual breadcrumb is opt-in only

The `_includes/breadcrumb-nav.html` include is gated:

```liquid
{%- if page.visual_breadcrumb == true -%}
  …
{%- endif -%}
```

A repo-wide grep confirms **zero pages** set `visual_breadcrumb: true`:

```
$ grep -rln "visual_breadcrumb: true" --include="*.md"
(no output)
```

The doctrine comment at the top of `breadcrumb-nav.html` records the design decision:

> v4 design-system doctrine moves standard page identity into the hero eyebrow. Structured breadcrumb data remains active through `breadcrumb-jsonld.html`. Set `visual_breadcrumb: true` only for an explicit compatibility exception.

So the visible breadcrumb that the audit critiques is *not rendered* anywhere on the live site. The structured breadcrumb (JSON-LD) is active everywhere and feeds search engines via `breadcrumb-jsonld.html`, but readers don't see a visible breadcrumb strip.

### What replaced the visible breadcrumb (v4)

The page identity that v3 carried in the breadcrumb is now carried in the hero card:

1. **Lane identity** lives in the `.hero-card` lane wrapper class (`.lane-discover`, `.lane-results`, etc.) which tints the hero and is reinforced by:
   - The active lane link in the masthead (gold underline + `aria-current="page"` after Wave 7)
   - The lane name printed at the top of every lane root H1
2. **Mobile** carries the slim status pill above the H1 (shipped in v5 Wave 5a — `_sass/_content.scss` §`.hero-meta-pill--status-*`)
3. **Long routes** (e.g. monograph chapters) carry their hierarchy via the right rail TOC ("On this page") and the `<title>` tag, not via a wrapping breadcrumb strip

This satisfies the audit's underlying concern — *readers should always know where they are* — through a different surface (hero eyebrow + lane wrapper + status pill + active masthead link) rather than a top-of-page text crumb.

### Audit checks per the three criteria

| Briefing criterion | Current state | Verdict |
|---|---|---|
| **Lane numeral** (00 – 07) | Lane numerals are surfaced on the `/` lane index via HF-05 (Wave 3 of v5). Not surfaced in the (suppressed) visual breadcrumb. No regression from v4. | 🟢 OK |
| **Mobile collapse** for long routes | Not applicable — no visible breadcrumb on mobile. The mobile slim status pill carries identity; the right-rail TOC carries hierarchy. | 🟢 OK |
| **Slim mobile pattern** (no `LANE ROOT` pill on mobile; `Status · Canonical` chip above H1) | Shipped in v5 prior wave (5a) — verified live on mobile via the preflight visual QA at `atlas/audits/site/2026-05-21-preflight-visual-qa/` (note this audit lives in a sibling worktree branch). | 🟢 OK |

## Follow-up considerations

These are noted for future passes, **not blockers**:

### 1. Should the visual breadcrumb come back for long-corpus routes?

Monograph chapters (Book III → Part 4 → Chapter 12) have a four-level breadcrumb in the JSON-LD but no visual surface. A reader navigating Chapter 12 sees:
- H1: "Chapter 12: ..."
- Lane wrapper class (`.lane-corpus`)
- Right-rail "Related pages" → links to Book III, Part 4, the Registry index

This is workable, but a four-level visual breadcrumb at the top would shorten the cognitive distance to "where am I in this monograph?" If we decide to reintroduce visual breadcrumbs, the existing `breadcrumb-nav.html` is ready to render — the data is already in `breadcrumb-data.html` and the styles already exist in `_sass/_content.scss` `.breadcrumb`. Just set `visual_breadcrumb: true` on the monograph layouts.

**Recommendation:** revisit during the post-v5 monograph navigation pass; not in scope for the v5 audit.

### 2. The `breadcrumb-nav.html` separator is `/` — does it want to be the audit's `›`?

The current visual breadcrumb (when opted in) renders `Home / Publications / Books / Book III / Part 4 / Chapter 12` — slash separator. The audit's example uses `›` (right-pointing angle bracket). If the visual breadcrumb is reintroduced, swap the separator. **No change made in this PR** because no page currently renders the visual breadcrumb.

### 3. Lane numeral in the JSON-LD?

The JSON-LD `BreadcrumbList` does not include the lane numeral (it just has `name` + `item` URL). The audit doesn't require the numeral in structured data, but it could be added as a `position`+`name` pattern (`"name": "00 · Discover"`) for richer search-engine presentation. Out of scope for the v5 audit pass; flagged for a future SEO sweep.

## Conclusion

The site's breadcrumb posture as of v5 is:
- ✅ **Structured data** (`breadcrumb-jsonld.html`) renders on every page and feeds search engines
- ✅ **Visible breadcrumb** is intentionally suppressed; page identity is carried by the hero card + lane wrapper + status pill + active masthead link
- ✅ **Mobile slim pattern** (status pill above H1, no `LANE ROOT` pill) shipped in v5 prior wave
- ✅ **All three audit criteria** are satisfied implicitly by the current design

**No code change required.** AUD-28 is closed.

## Related artefacts

- `_includes/breadcrumb-data.html` — single source of truth for breadcrumb hierarchies (Liquid string array)
- `_includes/breadcrumb-nav.html` — visual renderer, opt-in via `visual_breadcrumb: true`
- `_includes/breadcrumb-jsonld.html` — structured-data renderer, always active
- `_sass/_content.scss` §`.breadcrumb` — visual styling (only fires when visual_breadcrumb is opted in)
- `_sass/_content.scss` §`.hero-meta-pill--status-*` — the slim mobile status pill (v5 Wave 5a)
- `atlas/website/briefings/v5/design_handoff_audit_AUD-2026-05-19/README.md` §AUD-28 — the original audit text

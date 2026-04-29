---
{
  "projection_kind": "taulib_declaration",
  "title": "vert_comp_assoc",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/vert-comp-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::vert_comp_assoc",
  "declaration_slug": "vert-comp-assoc",
  "kind": "theorem",
  "name": "vert_comp_assoc",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 436,
  "source_line_end": 439,
  "registry_ids": [
    "II.D55"
  ],
  "related_registry_items": [
    {
      "id": "II.D55",
      "title": "2-Category Structure",
      "url": "/registry/object/II.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L436-L439",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/verify/taulib/docs/book-ii-enrichment-two-categories/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L436-L439",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L436-L439)
- Source range: L436-L439
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D55` — 2-Category Structure

## Immediate Comment / Docstring

```lean
/-- [II.D55] Formal proof: vertical composition is associative.
    vert_comp f (vert_comp g h) = vert_comp (vert_comp f g) h.
    Both sides are fun n k => f(g(h(n, k), k), k). -/
```

## Source Excerpt

```lean
theorem vert_comp_assoc (f g h : TwoCell) (n k : TauIdx) :
    vert_comp f (vert_comp g h) n k =
    vert_comp (vert_comp f g) h n k := by
  rfl
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "two_morph_tower_8_3",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/two-morph-tower-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::two_morph_tower_8_3",
  "declaration_slug": "two-morph-tower-8-3",
  "kind": "theorem",
  "name": "two_morph_tower_8_3",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 398,
  "source_line_end": 399,
  "registry_ids": [
    "II.D56"
  ],
  "related_registry_items": [
    {
      "id": "II.D56",
      "title": "2-Morphism",
      "url": "/registry/object/II.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L398-L399",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L398-L399",
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
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L398-L399)
- Source range: L398-L399
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D56` — 2-Morphism

## Immediate Comment / Docstring

```lean
-- 2-morphism tower coherence [II.D56]
```

## Source Excerpt

```lean
theorem two_morph_tower_8_3 :
    two_morph_tower_check 8 3 = true := by native_decide
```

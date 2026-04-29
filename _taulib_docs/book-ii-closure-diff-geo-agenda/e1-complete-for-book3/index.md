---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_complete_for_book3",
  "permalink": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/e1-complete-for-book3/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.DiffGeoAgenda`.",
  "declaration_id": "TauLib.BookII.Closure.DiffGeoAgenda::e1_complete_for_book3",
  "declaration_slug": "e1-complete-for-book3",
  "kind": "def",
  "name": "e1_complete_for_book3",
  "module_name": "TauLib.BookII.Closure.DiffGeoAgenda",
  "module_url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/",
  "source_line_start": 90,
  "source_line_end": 91,
  "registry_ids": [
    "II.R22"
  ],
  "related_registry_items": [
    {
      "id": "II.R22",
      "title": "Enrichment Ladder Forward Declaration",
      "url": "/registry/object/II.R22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L90-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.DiffGeoAgenda",
        "url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L90-L91",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.Closure.DiffGeoAgenda](/verify/taulib/docs/book-ii-closure-diff-geo-agenda/)
- Source path: [`TauLib/BookII/Closure/DiffGeoAgenda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L90-L91)
- Source range: L90-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R22` — Enrichment Ladder Forward Declaration

## Immediate Comment / Docstring

```lean
/-- [II.R22] E1 layer completeness check: verify that all E1 components
    are present as the starting point for Book III. Delegates to
    e1_layer_check from SelfDescribing.lean. -/
```

## Source Excerpt

```lean
def e1_complete_for_book3 (bound db k_max : TauIdx) : Bool :=
  e1_layer_check bound db k_max
```

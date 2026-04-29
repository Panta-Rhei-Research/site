---
{
  "projection_kind": "taulib_declaration",
  "title": "depth_max_20_4",
  "permalink": "/verify/taulib/docs/book-ii-regularity-positive-regularity/depth-max-20-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.PositiveRegularity`.",
  "declaration_id": "TauLib.BookII.Regularity.PositiveRegularity::depth_max_20_4",
  "declaration_slug": "depth-max-20-4",
  "kind": "theorem",
  "name": "depth_max_20_4",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/",
  "source_line_start": 340,
  "source_line_end": 341,
  "registry_ids": [
    "II.T34"
  ],
  "related_registry_items": [
    {
      "id": "II.T34",
      "title": "Regularity Criterion",
      "url": "/registry/object/II.T34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L340-L341",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PositiveRegularity",
        "url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L340-L341",
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

- Module: [TauLib.BookII.Regularity.PositiveRegularity](/verify/taulib/docs/book-ii-regularity-positive-regularity/)
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L340-L341)
- Source range: L340-L341
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T34` — Regularity Criterion

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- Regularity depth = max [II.T34]
```

## Source Excerpt

```lean
theorem depth_max_20_4 :
    regularity_depth_max_check 20 4 = true := by native_decide
```

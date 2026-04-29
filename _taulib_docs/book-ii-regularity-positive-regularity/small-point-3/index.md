---
{
  "projection_kind": "taulib_declaration",
  "title": "small_point_3",
  "permalink": "/verify/taulib/docs/book-ii-regularity-positive-regularity/small-point-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.PositiveRegularity`.",
  "declaration_id": "TauLib.BookII.Regularity.PositiveRegularity::small_point_3",
  "declaration_slug": "small-point-3",
  "kind": "theorem",
  "name": "small_point_3",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/",
  "source_line_start": 348,
  "source_line_end": 349,
  "registry_ids": [
    "II.D49"
  ],
  "related_registry_items": [
    {
      "id": "II.D49",
      "title": "Tau-Regularity",
      "url": "/registry/object/II.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L348-L349",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L348-L349",
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
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L348-L349)
- Source range: L348-L349
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D49` — Tau-Regularity

## Immediate Comment / Docstring

```lean
-- Small point regularity [II.D49]
```

## Source Excerpt

```lean
theorem small_point_3 :
    small_point_regularity_check 3 = true := by native_decide
```

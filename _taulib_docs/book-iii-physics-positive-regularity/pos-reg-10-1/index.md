---
{
  "projection_kind": "taulib_declaration",
  "title": "pos_reg_10_1",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/pos-reg-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::pos_reg_10_1",
  "declaration_slug": "pos-reg-10-1",
  "kind": "theorem",
  "name": "pos_reg_10_1",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 219,
  "source_line_end": 220,
  "registry_ids": [
    "III.T25"
  ],
  "related_registry_items": [
    {
      "id": "III.T25",
      "title": "Positive Regularity Theorem",
      "url": "/registry/object/III.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L219-L220",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/verify/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L219-L220",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/verify/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L219-L220)
- Source range: L219-L220
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T25` — Positive Regularity Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T25] Structural: positive regularity at depth 1. -/
```

## Source Excerpt

```lean
theorem pos_reg_10_1 :
    positive_regularity_check 10 1 = true := by native_decide
```

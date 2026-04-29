---
{
  "projection_kind": "taulib_declaration",
  "title": "positive_regularity_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/positive-regularity-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::positive_regularity_check",
  "declaration_slug": "positive-regularity-check",
  "kind": "def",
  "name": "positive_regularity_check",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 93,
  "source_line_end": 100,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L93-L100",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L93-L100",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/verify/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L93-L100)
- Source range: L93-L100
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T25` — Positive Regularity Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T25] Positive regularity: combines clopen locality, tower
    determinacy, and defect contractivity. All three conditions hold
    at every primorial level. -/
```

## Source Excerpt

```lean
def positive_regularity_check (bound db : TauIdx) : Bool :=
  -- Condition 1: clopen locality
  let cond1 := clopen_locality_check bound db
  -- Condition 2: tower determinacy
  let cond2 := tower_determinacy_check bound db
  -- Condition 3: defect contractivity
  let cond3 := defect_monotone_check db
  cond1 && cond2 && cond3
```

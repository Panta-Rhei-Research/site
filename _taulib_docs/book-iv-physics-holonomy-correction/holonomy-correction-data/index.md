---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyCorrectionData",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/holonomy-correction-data/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::HolonomyCorrectionData",
  "declaration_slug": "holonomy-correction-data",
  "kind": "structure",
  "name": "HolonomyCorrectionData",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 161,
  "source_line_end": 170,
  "registry_ids": [
    "IV.D45"
  ],
  "related_registry_items": [
    {
      "id": "IV.D45",
      "title": "Holonomy Correction",
      "url": "/registry/object/IV.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L161-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L161-L170",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/verify/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L161-L170)
- Source range: L161-L170
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D45` — Holonomy Correction

## Immediate Comment / Docstring

```lean
/-- [IV.D45] The holonomy correction π³α².

    Stored as (numer, denom) = (pi_cubed_numer × alpha_sq_numer,
                                 pi_cubed_denom × alpha_sq_denom).

    π³α² ≈ 31.006 × 5.3 × 10⁻⁵ ≈ 0.00164 -/
```

## Source Excerpt

```lean
structure HolonomyCorrectionData where
  /-- Numerator of π³α². -/
  numer : Nat
  /-- Denominator of π³α². -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```

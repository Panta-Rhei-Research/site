---
{
  "projection_kind": "taulib_declaration",
  "title": "PolarityImbalance",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/polarity-imbalance/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::PolarityImbalance",
  "declaration_slug": "polarity-imbalance",
  "kind": "structure",
  "name": "PolarityImbalance",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 96,
  "source_line_end": 103,
  "registry_ids": [
    "V.D169"
  ],
  "related_registry_items": [
    {
      "id": "V.D169",
      "title": "Polarity Imbalance",
      "url": "/registry/object/V.D169/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L96-L103",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L96-L103",
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L96-L103)
- Source range: L96-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D169` — Polarity Imbalance

## Immediate Comment / Docstring

```lean
/-- [V.D169] Polarity imbalance I_BH.

    I_BH = (||χ⁺|| − ||χ⁻||) / (||χ⁺|| + ||χ⁻||)

    Encoded as a pair (numerator, denominator) where numerator
    can be negative (using Int). The imbalance is strictly between
    −1 and 1 because both lobes are nonzero. -/
```

## Source Excerpt

```lean
structure PolarityImbalance where
  /-- Imbalance numerator (can be negative). -/
  numer : Int
  /-- Imbalance denominator (always positive). -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  deriving Repr
```

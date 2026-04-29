---
{
  "projection_kind": "taulib_declaration",
  "title": "PlanckCharacterExt",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/planck-character-ext/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::PlanckCharacterExt",
  "declaration_slug": "planck-character-ext",
  "kind": "structure",
  "name": "PlanckCharacterExt",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 220,
  "source_line_end": 235,
  "registry_ids": [
    "IV.D298"
  ],
  "related_registry_items": [
    {
      "id": "IV.D298",
      "title": "Planck character",
      "url": "/registry/object/IV.D298/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L220-L235",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L220-L235",
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridgeExt](/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L220-L235)
- Source range: L220-L235
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D298` — Planck character

## Immediate Comment / Docstring

```lean
/-- [IV.D298] The Planck character ℏ_τ in the ch13 dimensional-bridge context.
    This is the σ-fixed sector lift of ι_τ into the QM regime,
    re-recorded here with its ch13 registry label.

    Key properties:
    - label = "hbar_tau"
    - sector = "QM"
    - σ-fixed = true (lives at lemniscate crossing point)
    - is_minimum = true (attained, not merely infimum) -/
```

## Source Excerpt

```lean
structure PlanckCharacterExt where
  /-- Symbolic label. -/
  label : String
  /-- Source sector. -/
  sector : String
  /-- σ-fixed: invariant under lobe swap. -/
  is_sigma_fixed : Bool
  /-- Attained minimum of the sector lift functional. -/
  is_minimum : Bool
  /-- ℏ_τ numerator (scaled rational: ℏ_τ ≈ ι_τ/4). -/
  numer : Nat
  /-- ℏ_τ denominator. -/
  denom : Nat
  /-- Denominator is positive. -/
  denom_pos : denom > 0
  deriving Repr
```

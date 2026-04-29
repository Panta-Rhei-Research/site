---
{
  "projection_kind": "taulib_declaration",
  "title": "CorrectionFactor",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/correction-factor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessAlpha::CorrectionFactor",
  "declaration_slug": "correction-factor",
  "kind": "structure",
  "name": "CorrectionFactor",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "source_line_start": 118,
  "source_line_end": 126,
  "registry_ids": [
    "IV.D288"
  ],
  "related_registry_items": [
    {
      "id": "IV.D288",
      "title": "Holonomy Correction Factor",
      "url": "/registry/object/IV.D288/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L118-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L118-L126",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessAlpha](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L118-L126)
- Source range: L118-L126
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D288` — Holonomy Correction Factor

## Immediate Comment / Docstring

```lean
/-- [IV.D288] The holonomy correction factor R(ι_τ) ≈ 1.006 measures
    the deviation of the spectral approximation from the exact holonomy
    formula. Wraps HolonomyCorrection module. -/
```

## Source Excerpt

```lean
structure CorrectionFactor where
  /-- Correction is close to 1 (> 1000/1000). -/
  near_unity_numer : Nat
  near_unity_denom : Nat
  denom_pos : near_unity_denom > 0
  /-- π³ ≈ 31 holonomy circles. -/
  pi_cubed_approx : Nat
  pi_cubed_eq : pi_cubed_approx = 31
  deriving Repr
```

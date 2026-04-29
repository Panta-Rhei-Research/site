---
{
  "projection_kind": "taulib_declaration",
  "title": "Level0FormulaSummary",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-formula-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::Level0FormulaSummary",
  "declaration_slug": "level0-formula-summary",
  "kind": "structure",
  "name": "Level0FormulaSummary",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 150,
  "source_line_end": 163,
  "registry_ids": [
    "IV.T109"
  ],
  "related_registry_items": [
    {
      "id": "IV.T109",
      "title": "Level~0 mass ratio formula",
      "url": "/registry/object/IV.T109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L150-L163",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
        "url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L150-L163",
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

- Module: [TauLib.BookIV.Calibration.CalibrationAnchorExt](/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/)
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L150-L163)
- Source range: L150-L163
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T109` — Level~0 mass ratio formula

## Immediate Comment / Docstring

```lean
/-- [IV.T109] Structural summary of the Level 0 mass ratio formula.

    R₀ = ι_τ^(-7) − √3·ι_τ^(-2)

    The full derivation with range proofs is in MassRatioFormula.lean.
    This structure records the key structural parameters. -/
```

## Source Excerpt

```lean
structure Level0FormulaSummary where
  /-- Bulk exponent: ι_τ raised to this (negative) power. -/
  bulk_exponent : Nat
  /-- Label for the correction factor coefficient. -/
  correction_factor_label : String
  /-- Correction exponent: ι_τ raised to this (negative) power. -/
  correction_exponent : Nat
  /-- Result range lower bound (inclusive). -/
  result_range_lo : Nat
  /-- Result range upper bound (exclusive). -/
  result_range_hi : Nat
  /-- Accuracy at exact ι_τ (in ppm). -/
  accuracy_ppm_exact : String
  deriving Repr
```

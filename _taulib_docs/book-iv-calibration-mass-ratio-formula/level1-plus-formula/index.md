---
{
  "projection_kind": "taulib_declaration",
  "title": "Level1PlusFormula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/level1-plus-formula/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "declaration_id": "TauLib.BookIV.Calibration.MassRatioFormula::Level1PlusFormula",
  "declaration_slug": "level1-plus-formula",
  "kind": "structure",
  "name": "Level1PlusFormula",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "source_line_start": 270,
  "source_line_end": 281,
  "registry_ids": [
    "IV.D48"
  ],
  "related_registry_items": [
    {
      "id": "IV.D48",
      "title": "Level 1+ Formula",
      "url": "/registry/object/IV.D48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L270-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.MassRatioFormula",
        "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L270-L281",
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

- Module: [TauLib.BookIV.Calibration.MassRatioFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/)
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean#L270-L281)
- Source range: L270-L281
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D48` — Level 1+ Formula

## Immediate Comment / Docstring

```lean
/-- [IV.D48] Level 1+ mass ratio formula structure.

    R₁ = ι_τ^(-7) − (√3 + π³α²)·ι_τ^(-2)

    At exact ι_τ = 2/(π+e), this gives R₁ = 1838.683709(46),
    matching CODATA R = 1838.68366173(89) to 0.025 ppm.

    The Level 1+ formula is recorded here as a STRUCTURE:
    the numerical evaluation requires the exact ι_τ (not the
    6-digit rational approximation). -/
```

## Source Excerpt

```lean
structure Level1PlusFormula where
  /-- Bulk exponent: ι_τ^(-7). -/
  bulk_exp : Int := -7
  /-- Correction coefficient: √3 + π³α². -/
  correction_coeff : String := "√3 + π³α²"
  /-- Correction ι_τ power: ι_τ^(-2). -/
  correction_exp : Int := -2
  /-- Accuracy at exact ι_τ (in ppm). -/
  accuracy_ppm : String := "0.025"
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```

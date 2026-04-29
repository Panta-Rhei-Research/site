---
{
  "projection_kind": "taulib_declaration",
  "title": "Level1PlusFormulaSummary",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1-plus-formula-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::Level1PlusFormulaSummary",
  "declaration_slug": "level1-plus-formula-summary",
  "kind": "structure",
  "name": "Level1PlusFormulaSummary",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 194,
  "source_line_end": 207,
  "registry_ids": [
    "IV.T110"
  ],
  "related_registry_items": [
    {
      "id": "IV.T110",
      "title": "Level~1+ mass ratio formula",
      "url": "/registry/object/IV.T110/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L194-L207",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L194-L207",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L194-L207)
- Source range: L194-L207
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T110` — Level~1+ mass ratio formula

## Immediate Comment / Docstring

```lean
/-- [IV.T110] Structural summary of the Level 1+ mass ratio formula.

    R₁ = ι_τ^(-7) − (√3 + π³α²)·ι_τ^(-2)

    Adds the holonomy correction π³α² (three U(1) circles in τ³,
    second-order EM). At exact ι_τ, this achieves 0.025 ppm. -/
```

## Source Excerpt

```lean
structure Level1PlusFormulaSummary where
  /-- Label for the holonomy correction. -/
  holonomy_correction_label : String
  /-- Full correction coefficient label. -/
  correction_label : String
  /-- Accuracy in ppm (scaled by 1000: 25 = 0.025 ppm). -/
  result_ppm_scaled : Nat
  /-- Scale factor for ppm (1000 means divide by 1000). -/
  ppm_scale : Nat
  /-- Number of holonomy circles. -/
  holonomy_circles : Nat
  /-- EM correction order. -/
  em_order : Nat
  deriving Repr
```

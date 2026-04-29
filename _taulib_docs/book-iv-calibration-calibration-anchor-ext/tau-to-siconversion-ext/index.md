---
{
  "projection_kind": "taulib_declaration",
  "title": "TauToSIConversionExt",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-to-siconversion-ext/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::TauToSIConversionExt",
  "declaration_slug": "tau-to-siconversion-ext",
  "kind": "structure",
  "name": "TauToSIConversionExt",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 359,
  "source_line_end": 368,
  "registry_ids": [
    "IV.D292"
  ],
  "related_registry_items": [
    {
      "id": "IV.D292",
      "title": "tau-to-SI conversion",
      "url": "/registry/object/IV.D292/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L359-L368",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L359-L368",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L359-L368)
- Source range: L359-L368
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D292` — tau-to-SI conversion

## Immediate Comment / Docstring

```lean
/-- [IV.D292] Extended τ-to-SI conversion structure.

    In τ-native units, m_n = 1. The conversion to SI requires
    exactly one anchor measurement (the neutron mass in kg).
    All other SI values follow from ι_τ-determined ratios. -/
```

## Source Excerpt

```lean
structure TauToSIConversionExt where
  /-- Type of conversion: "mass_anchor". -/
  conversion_type : String
  /-- Number of independent anchors needed. -/
  anchor_count : Nat
  /-- The anchor constant name. -/
  anchor_name : String
  /-- Whether all dimensionless ratios are ι_τ-determined. -/
  all_ratios_determined : Bool
  deriving Repr
```

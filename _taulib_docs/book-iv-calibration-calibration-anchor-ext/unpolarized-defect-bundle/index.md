---
{
  "projection_kind": "taulib_declaration",
  "title": "UnpolarizedDefectBundle",
  "permalink": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/unpolarized-defect-bundle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.CalibrationAnchorExt::UnpolarizedDefectBundle",
  "declaration_slug": "unpolarized-defect-bundle",
  "kind": "structure",
  "name": "UnpolarizedDefectBundle",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "source_line_start": 241,
  "source_line_end": 248,
  "registry_ids": [
    "IV.D290"
  ],
  "related_registry_items": [
    {
      "id": "IV.D290",
      "title": "Unpolarized defect bundle",
      "url": "/registry/object/IV.D290/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L241-L248",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L241-L248",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean#L241-L248)
- Source range: L241-L248
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D290` — Unpolarized defect bundle

## Immediate Comment / Docstring

```lean
/-- [IV.D290] An unpolarized defect bundle on the fiber T².

    The three polarization properties that must ALL be zero/balanced
    for a defect bundle to qualify as "unpolarized":
    - charge_zero: net electric charge = 0
    - isospin_zero: net isospin projection = 0
    - chi_balanced: χ₊ and χ₋ characters in balance -/
```

## Source Excerpt

```lean
structure UnpolarizedDefectBundle where
  /-- Net electric charge is zero. -/
  charge_zero : Bool := true
  /-- Net isospin projection is zero. -/
  isospin_zero : Bool := true
  /-- Bipolar characters χ₊, χ₋ are balanced. -/
  chi_balanced : Bool := true
  deriving Repr
```

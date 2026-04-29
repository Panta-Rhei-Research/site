---
{
  "projection_kind": "taulib_declaration",
  "title": "h_formula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/h-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::h_formula",
  "declaration_slug": "h-formula",
  "kind": "def",
  "name": "h_formula",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 120,
  "source_line_end": 126,
  "registry_ids": [
    "IV.D34"
  ],
  "related_registry_items": [
    {
      "id": "IV.D34",
      "title": "Planck Constant",
      "url": "/registry/object/IV.D34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L120-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionalBridge",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L120-L126",
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridge](/verify/taulib/docs/book-iv-calibration-dimensional-bridge/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L120-L126)
- Source range: L120-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D34` — Planck Constant

## Immediate Comment / Docstring

```lean
/-- [IV.D34] Planck constant: h = M · L² · H.
    Coefficient: 1, π⁰, dimensions: M¹ L² H¹. -/
```

## Source Excerpt

```lean
def h_formula : DimensionalFormula where
  name := "Planck constant h"
  coeff_numer := 1
  coeff_denom := 1
  denom_pos := by omega
  pi_power := 0
  exponents := ⟨1, 2, 1, 0⟩
```

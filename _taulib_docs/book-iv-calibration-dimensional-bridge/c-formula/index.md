---
{
  "projection_kind": "taulib_declaration",
  "title": "c_formula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/c-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::c_formula",
  "declaration_slug": "c-formula",
  "kind": "def",
  "name": "c_formula",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 110,
  "source_line_end": 116,
  "registry_ids": [
    "IV.D33"
  ],
  "related_registry_items": [
    {
      "id": "IV.D33",
      "title": "Speed of Light",
      "url": "/registry/object/IV.D33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L110-L116",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L110-L116",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L110-L116)
- Source range: L110-L116
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D33` — Speed of Light

## Immediate Comment / Docstring

```lean
/-- [IV.D33] Speed of light: c = L · H.
    Coefficient: 1, π⁰, dimensions: L¹ H¹. -/
```

## Source Excerpt

```lean
def c_formula : DimensionalFormula where
  name := "Speed of light c"
  coeff_numer := 1
  coeff_denom := 1
  denom_pos := by omega
  pi_power := 0
  exponents := ⟨0, 1, 1, 0⟩
```

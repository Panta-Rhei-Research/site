---
{
  "projection_kind": "taulib_declaration",
  "title": "ke_formula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/ke-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::ke_formula",
  "declaration_slug": "ke-formula",
  "kind": "def",
  "name": "ke_formula",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 130,
  "source_line_end": 136,
  "registry_ids": [
    "IV.D35"
  ],
  "related_registry_items": [
    {
      "id": "IV.D35",
      "title": "Coulomb Constant",
      "url": "/registry/object/IV.D35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L130-L136",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L130-L136",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L130-L136)
- Source range: L130-L136
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D35` — Coulomb Constant

## Immediate Comment / Docstring

```lean
/-- [IV.D35] Coulomb constant: k_e = (π²/32) · Q²/(M · H · L³).
    Coefficient: 1/32, π², dimensions: M⁻¹ L⁻³ H⁻¹ Q². -/
```

## Source Excerpt

```lean
def ke_formula : DimensionalFormula where
  name := "Coulomb constant k_e"
  coeff_numer := 1
  coeff_denom := 32
  denom_pos := by omega
  pi_power := 2
  exponents := ⟨-1, -3, -1, 2⟩
```

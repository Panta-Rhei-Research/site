---
{
  "projection_kind": "taulib_declaration",
  "title": "mu0_formula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/mu0-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::mu0_formula",
  "declaration_slug": "mu0-formula",
  "kind": "def",
  "name": "mu0_formula",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 150,
  "source_line_end": 156,
  "registry_ids": [
    "IV.D37"
  ],
  "related_registry_items": [
    {
      "id": "IV.D37",
      "title": "Vacuum Permeability",
      "url": "/registry/object/IV.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L150-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L150-L156",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L150-L156)
- Source range: L150-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D37` — Vacuum Permeability

## Immediate Comment / Docstring

```lean
/-- [IV.D37] Vacuum permeability: μ₀ = (π³/8) · Q²/(M · H³ · L⁵).
    Coefficient: 1/8, π³, dimensions: M⁻¹ L⁻⁵ H⁻³ Q². -/
```

## Source Excerpt

```lean
def mu0_formula : DimensionalFormula where
  name := "Vacuum permeability μ₀"
  coeff_numer := 1
  coeff_denom := 8
  denom_pos := by omega
  pi_power := 3
  exponents := ⟨-1, -5, -3, 2⟩
```

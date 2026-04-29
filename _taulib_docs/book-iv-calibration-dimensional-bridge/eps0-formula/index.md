---
{
  "projection_kind": "taulib_declaration",
  "title": "eps0_formula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/eps0-formula/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::eps0_formula",
  "declaration_slug": "eps0-formula",
  "kind": "def",
  "name": "eps0_formula",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 140,
  "source_line_end": 146,
  "registry_ids": [
    "IV.D36"
  ],
  "related_registry_items": [
    {
      "id": "IV.D36",
      "title": "Vacuum Permittivity",
      "url": "/registry/object/IV.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L140-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L140-L146",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L140-L146)
- Source range: L140-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D36` — Vacuum Permittivity

## Immediate Comment / Docstring

```lean
/-- [IV.D36] Vacuum permittivity: ε₀ = (8/π³) · M · H · L³ / Q².
    Coefficient: 8, π⁻³, dimensions: M¹ L³ H¹ Q⁻². -/
```

## Source Excerpt

```lean
def eps0_formula : DimensionalFormula where
  name := "Vacuum permittivity ε₀"
  coeff_numer := 8
  coeff_denom := 1
  denom_pos := by omega
  pi_power := -3
  exponents := ⟨1, 3, 1, -2⟩
```

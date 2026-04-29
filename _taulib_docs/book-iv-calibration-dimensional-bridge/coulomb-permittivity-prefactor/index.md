---
{
  "projection_kind": "taulib_declaration",
  "title": "coulomb_permittivity_prefactor",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/coulomb-permittivity-prefactor/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::coulomb_permittivity_prefactor",
  "declaration_slug": "coulomb-permittivity-prefactor",
  "kind": "theorem",
  "name": "coulomb_permittivity_prefactor",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 223,
  "source_line_end": 227,
  "registry_ids": [
    "IV.T08"
  ],
  "related_registry_items": [
    {
      "id": "IV.T08",
      "title": "Coulomb-Permittivity",
      "url": "/registry/object/IV.T08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L223-L227",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L223-L227",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L223-L227)
- Source range: L223-L227
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T08` — Coulomb-Permittivity

## Immediate Comment / Docstring

```lean
/-- [IV.T08] Coulomb-permittivity (prefactor part):
    k_e · 4π · ε₀ = 1.
    - Coefficients: (1/32) × 4 × (8/1) = 32/32 = 1
    - π powers: 2 + 1 + (−3) = 0

    Cross-multiplied: coeff_numer_product × denom_product = coeff_denom_product × numer_product
    k_e: 1/32, ε₀: 8/1, factor 4: 4/1
    Product numerators: 1 × 8 × 4 = 32
    Product denominators: 32 × 1 × 1 = 32
    So 32 = 32 ✓ -/
```

## Source Excerpt

```lean
theorem coulomb_permittivity_prefactor :
    ke_formula.coeff_numer * eps0_formula.coeff_numer * 4 =
    ke_formula.coeff_denom * eps0_formula.coeff_denom * 1 ∧
    ke_formula.pi_power + eps0_formula.pi_power + 1 = 0 := by
  simp [ke_formula, eps0_formula]
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "maxwell_complete",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::maxwell_complete",
  "declaration_slug": "maxwell-complete",
  "kind": "theorem",
  "name": "maxwell_complete",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 191,
  "source_line_end": 200,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L191-L200",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L191-L200",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L191-L200)
- Source range: L191-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Complete Maxwell relation: c² = 1/(ε₀ · μ₀).
    Both dimensional and prefactor parts combine to give
    c² · ε₀ · μ₀ = 1 (dimensionless, coefficient = 1). -/
```

## Source Excerpt

```lean
theorem maxwell_complete :
    -- Dimensional: c² + ε₀ + μ₀ = 0 (dimensionless)
    (c_formula.exponents.scale 2).add
      (eps0_formula.exponents.add mu0_formula.exponents) = DimExponents.zero ∧
    -- Prefactors: 1² × (8 × 1) = 1 × (1 × 8) and π^(0+(-3)+3) = π⁰
    2 * c_formula.pi_power + eps0_formula.pi_power + mu0_formula.pi_power = 0 := by
  constructor
  · simp [c_formula, eps0_formula, mu0_formula,
          DimExponents.add, DimExponents.scale, DimExponents.zero]
  · simp [c_formula, eps0_formula, mu0_formula]
```

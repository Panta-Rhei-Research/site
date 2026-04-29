---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_formula_ch11",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/holonomy-formula-ch11/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionlessAlpha::holonomy_formula_ch11",
  "declaration_slug": "holonomy-formula-ch11",
  "kind": "theorem",
  "name": "holonomy_formula_ch11",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "source_line_start": 95,
  "source_line_end": 102,
  "registry_ids": [
    "IV.T107"
  ],
  "related_registry_items": [
    {
      "id": "IV.T107",
      "title": "Holonomy Fine-Structure Formula",
      "url": "/registry/object/IV.T107/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L95-L102",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L95-L102",
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

- Module: [TauLib.BookIV.Calibration.DimensionlessAlpha](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/)
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean#L95-L102)
- Source range: L95-L102
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T107` — Holonomy Fine-Structure Formula

## Immediate Comment / Docstring

```lean
/-- [IV.T107] Holonomy fine-structure formula:
    α = (π³/16) · Q⁴/(M²·H³·L⁶).
    The factor π³ arises from three independent U(1) holonomy integrations
    around the circles T_π, T_γ, T_η in τ³ = τ¹ ×_f T².
    Wraps FineStructure.holonomy_alpha with holonomy_correction. -/
```

## Source Excerpt

```lean
theorem holonomy_formula_ch11 :
    -- The geometric prefactor is π³/16 ≈ 31/16
    holonomy_alpha.geom_numer = 31 ∧
    holonomy_alpha.geom_denom = 16 ∧
    -- The exponents sum to 4 − 2 − 3 − 6 = −7
    holonomy_alpha.Q_exp + holonomy_alpha.M_exp +
    holonomy_alpha.H_exp + holonomy_alpha.L_exp = -7 := by
  exact ⟨rfl, rfl, by decide⟩
```

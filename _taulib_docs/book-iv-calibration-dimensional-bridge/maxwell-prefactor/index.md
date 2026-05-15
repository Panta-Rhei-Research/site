---
{
  "projection_kind": "taulib_declaration",
  "title": "maxwell_prefactor",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-prefactor/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::maxwell_prefactor",
  "declaration_slug": "maxwell-prefactor",
  "kind": "theorem",
  "name": "maxwell_prefactor",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 182,
  "source_line_end": 186,
  "registry_ids": [
    "IV.T07"
  ],
  "related_registry_items": [
    {
      "id": "IV.T07",
      "title": "Maxwell Relation",
      "url": "/registry/object/IV.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L182-L186",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionalBridge",
        "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L182-L186",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridge](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L182-L186)
- Source range: L182-L186
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.T07` — Maxwell Relation

## Immediate Comment / Docstring

```lean
/-- [IV.T07] Maxwell relation (prefactor part):
    The π-prefactors cancel: (8/1 · π⁻³) × (1/8 · π³) = 1.
    - Coefficient product: 8 × 1 = 1 × 8 (both = 8)
    - π exponent sum: (−3) + 3 = 0 -/
```

## Source Excerpt

```lean
theorem maxwell_prefactor :
    eps0_formula.coeff_numer * mu0_formula.coeff_numer =
    eps0_formula.coeff_denom * mu0_formula.coeff_denom ∧
    eps0_formula.pi_power + mu0_formula.pi_power = 0 := by
  simp [eps0_formula, mu0_formula]
```

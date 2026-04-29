---
{
  "projection_kind": "taulib_declaration",
  "title": "coulomb_permittivity_dimensional",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/coulomb-permittivity-dimensional/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::coulomb_permittivity_dimensional",
  "declaration_slug": "coulomb-permittivity-dimensional",
  "kind": "theorem",
  "name": "coulomb_permittivity_dimensional",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 209,
  "source_line_end": 211,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L209-L211",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L209-L211",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L209-L211)
- Source range: L209-L211
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T08` — Coulomb-Permittivity

## Immediate Comment / Docstring

```lean
/-- [IV.T08] Coulomb-permittivity (dimensional part):
    k_e · ε₀ exponents sum to zero (dimensionless product).
    This is the dimensional content of k_e = 1/(4π · ε₀). -/
```

## Source Excerpt

```lean
theorem coulomb_permittivity_dimensional :
    ke_formula.exponents.add eps0_formula.exponents = DimExponents.zero := by
  simp [ke_formula, eps0_formula, DimExponents.add, DimExponents.zero]
```

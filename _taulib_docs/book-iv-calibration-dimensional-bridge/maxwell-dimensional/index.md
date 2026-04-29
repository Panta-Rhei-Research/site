---
{
  "projection_kind": "taulib_declaration",
  "title": "maxwell_dimensional",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-dimensional/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::maxwell_dimensional",
  "declaration_slug": "maxwell-dimensional",
  "kind": "theorem",
  "name": "maxwell_dimensional",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 172,
  "source_line_end": 176,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L172-L176",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L172-L176",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L172-L176)
- Source range: L172-L176
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T07` — Maxwell Relation

## Immediate Comment / Docstring

```lean
/-- [IV.T07] Maxwell relation (dimensional part):
    ε₀ · μ₀ exponents sum to −2 × c exponents.
    This means ε₀ · μ₀ = (prefactor) / c², i.e. c² = prefactor / (ε₀ · μ₀). -/
```

## Source Excerpt

```lean
theorem maxwell_dimensional :
    eps0_formula.exponents.add mu0_formula.exponents =
    c_formula.exponents.scale (-2) := by
  simp [eps0_formula, mu0_formula, c_formula,
        DimExponents.add, DimExponents.scale]
```

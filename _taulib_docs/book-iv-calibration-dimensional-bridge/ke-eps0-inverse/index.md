---
{
  "projection_kind": "taulib_declaration",
  "title": "ke_eps0_inverse",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/ke-eps0-inverse/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridge::ke_eps0_inverse",
  "declaration_slug": "ke-eps0-inverse",
  "kind": "theorem",
  "name": "ke_eps0_inverse",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "source_line_start": 306,
  "source_line_end": 309,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L306-L309",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L306-L309",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean#L306-L309)
- Source range: L306-L309
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- k_e and ε₀ are dimensional inverses (up to 4π). -/
```

## Source Excerpt

```lean
theorem ke_eps0_inverse :
    ke_formula.exponents.add eps0_formula.exponents =
    DimExponents.zero := by
  simp [ke_formula, eps0_formula, DimExponents.add, DimExponents.zero]
```

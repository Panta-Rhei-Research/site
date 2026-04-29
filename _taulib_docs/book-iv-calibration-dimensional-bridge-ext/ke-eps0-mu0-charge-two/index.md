---
{
  "projection_kind": "taulib_declaration",
  "title": "ke_eps0_mu0_charge_two",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/ke-eps0-mu0-charge-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::ke_eps0_mu0_charge_two",
  "declaration_slug": "ke-eps0-mu0-charge-two",
  "kind": "theorem",
  "name": "ke_eps0_mu0_charge_two",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 419,
  "source_line_end": 423,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L419-L423",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
        "url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L419-L423",
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridgeExt](/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L419-L423)
- Source range: L419-L423
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- k_e, ε₀, μ₀ all have |Q| = 2. -/
```

## Source Excerpt

```lean
theorem ke_eps0_mu0_charge_two :
    ke_relational.exponents.Q = 2 ∧
    eps0_relational.exponents.Q = -2 ∧
    mu0_relational.exponents.Q = 2 := by
  simp [ke_relational, eps0_relational, mu0_relational]
```

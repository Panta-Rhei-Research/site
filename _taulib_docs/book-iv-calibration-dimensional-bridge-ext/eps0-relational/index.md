---
{
  "projection_kind": "taulib_declaration",
  "title": "eps0_relational",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/eps0-relational/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::eps0_relational",
  "declaration_slug": "eps0-relational",
  "kind": "def",
  "name": "eps0_relational",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 133,
  "source_line_end": 139,
  "registry_ids": [
    "IV.D296"
  ],
  "related_registry_items": [
    {
      "id": "IV.D296",
      "title": "Vacuum permittivity in relational units",
      "url": "/registry/object/IV.D296/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L133-L139",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L133-L139",
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

- Module: [TauLib.BookIV.Calibration.DimensionalBridgeExt](/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/)
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L133-L139)
- Source range: L133-L139
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D296` — Vacuum permittivity in relational units

## Immediate Comment / Docstring

```lean
/-- [IV.D296] Vacuum permittivity in relational units:
    ε₀ = (8/π³) · M · H · L³ / Q².
    Prefactor = 8/π³, exponents M¹ L³ H¹ Q⁻². -/
```

## Source Excerpt

```lean
def eps0_relational : RelationalFormula where
  formula_label := "eps_0 = (8/pi^3) * M*H*L^3/Q^2"
  exponents := ⟨1, 3, 1, -2⟩
  prefactor_numer := 8
  prefactor_denom := 1
  denom_pos := by omega
  prefactor_label := "eight_over_pi_cubed"
```

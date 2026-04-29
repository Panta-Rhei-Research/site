---
{
  "projection_kind": "taulib_declaration",
  "title": "mu0_relational",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/mu0-relational/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.DimensionalBridgeExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.DimensionalBridgeExt::mu0_relational",
  "declaration_slug": "mu0-relational",
  "kind": "def",
  "name": "mu0_relational",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridgeExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-dimensional-bridge-ext/",
  "source_line_start": 148,
  "source_line_end": 154,
  "registry_ids": [
    "IV.D297"
  ],
  "related_registry_items": [
    {
      "id": "IV.D297",
      "title": "Vacuum permeability in relational units",
      "url": "/registry/object/IV.D297/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L148-L154",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L148-L154",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridgeExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridgeExt.lean#L148-L154)
- Source range: L148-L154
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D297` — Vacuum permeability in relational units

## Immediate Comment / Docstring

```lean
/-- [IV.D297] Vacuum permeability in relational units:
    μ₀ = (π³/8) · Q²/(M · H³ · L⁵).
    Prefactor = π³/8, exponents M⁻¹ L⁻⁵ H⁻³ Q². -/
```

## Source Excerpt

```lean
def mu0_relational : RelationalFormula where
  formula_label := "mu_0 = (pi^3/8) * Q^2/(M*H^3*L^5)"
  exponents := ⟨-1, -5, -3, 2⟩
  prefactor_numer := 1
  prefactor_denom := 8
  denom_pos := by omega
  prefactor_label := "pi_cubed_over_eight"
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauPlasmaState",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/tau-plasma-state/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::TauPlasmaState",
  "declaration_slug": "tau-plasma-state",
  "kind": "structure",
  "name": "TauPlasmaState",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 64,
  "source_line_end": 77,
  "registry_ids": [
    "V.D104"
  ],
  "related_registry_items": [
    {
      "id": "V.D104",
      "title": "tau-plasma",
      "url": "/registry/object/V.D104/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L64-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauPlasma",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L64-L77",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.FluidMacro.TauPlasma](/verify/taulib/docs/book-v-fluid-macro-tau-plasma/)
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L64-L77)
- Source range: L64-L77
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D104` — tau-plasma

## Immediate Comment / Docstring

```lean
/-- [V.D104] Tau-plasma: a macro defect configuration on τ³ with
    nonzero B-sector defect density and mobile charged carriers.

    Structural plasma conditions:
    - n_B > 0 (nonzero B-sector density)
    - μ_B > μ_crit (carrier mobility above critical threshold) -/
```

## Source Excerpt

```lean
structure TauPlasmaState where
  /-- B-sector defect density (scaled). -/
  b_sector_density : Nat
  /-- B-sector density is nonzero. -/
  density_pos : b_sector_density > 0
  /-- Carrier mobility (scaled). -/
  carrier_mobility : Nat
  /-- Critical mobility threshold. -/
  mobility_threshold : Nat
  /-- Mobility exceeds threshold. -/
  mobile : carrier_mobility > mobility_threshold
  /-- Temperature index (scaled). -/
  temperature_idx : Nat
  deriving Repr
```

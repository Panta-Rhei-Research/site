---
{
  "projection_kind": "taulib_declaration",
  "title": "AlfvenDamping",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::AlfvenDamping",
  "declaration_slug": "alfven-damping",
  "kind": "structure",
  "name": "AlfvenDamping",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 199,
  "source_line_end": 208,
  "registry_ids": [
    "V.R156"
  ],
  "related_registry_items": [
    {
      "id": "V.R156",
      "title": "Sufficient energy flux",
      "url": "/registry/object/V.R156/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L199-L208",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauAlfven",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L199-L208",
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L199-L208)
- Source range: L199-L208
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R156` — Sufficient energy flux

## Immediate Comment / Docstring

```lean
/-- [V.R156] Alfven wave damping: all damping mechanisms are bounded
    in the τ-framework by the defect-budget constraint.

    The damping rate γ ≤ γ_max for each mechanism, where γ_max is
    determined by the defect-budget at the relevant primorial level. -/
```

## Source Excerpt

```lean
structure AlfvenDamping where
  /-- Damping mechanism. -/
  mechanism : AlfvenDampingMechanism
  /-- Damping rate (scaled). -/
  rate : Nat
  /-- Maximum damping rate (from defect budget). -/
  max_rate : Nat
  /-- Rate is bounded. -/
  rate_bounded : rate ≤ max_rate
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "QuasiNeutralityBound",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/quasi-neutrality-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::QuasiNeutralityBound",
  "declaration_slug": "quasi-neutrality-bound",
  "kind": "structure",
  "name": "QuasiNeutralityBound",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 110,
  "source_line_end": 117,
  "registry_ids": [
    "V.T74"
  ],
  "related_registry_items": [
    {
      "id": "V.T74",
      "title": "Forced Quasi-Neutrality",
      "url": "/registry/object/V.T74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L110-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L110-L117",
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
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L110-L117)
- Source range: L110-L117
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T74` — Forced Quasi-Neutrality

## Immediate Comment / Docstring

```lean
/-- [V.T74] Forced Quasi-Neutrality: in a τ-plasma, charge imbalance
    at any scale l > λ_D is exponentially small:
        |n₊(l) - n₋(l)| ≤ n₀ exp(-l/λ_D)

    Quasi-neutrality follows from the B-sector boundary structure. -/
```

## Source Excerpt

```lean
structure QuasiNeutralityBound where
  /-- Scale (in Debye lengths). -/
  scale_in_debye : Nat
  /-- Maximum charge imbalance (scaled). -/
  max_imbalance : Nat
  /-- Exponential suppression: imbalance decreases with scale. -/
  suppressed : scale_in_debye > 1 → max_imbalance < 100
  deriving Repr
```

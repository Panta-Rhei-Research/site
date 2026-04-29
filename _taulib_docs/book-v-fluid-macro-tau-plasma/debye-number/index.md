---
{
  "projection_kind": "taulib_declaration",
  "title": "DebyeNumber",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/debye-number/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.TauPlasma`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauPlasma::DebyeNumber",
  "declaration_slug": "debye-number",
  "kind": "structure",
  "name": "DebyeNumber",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "source_line_start": 243,
  "source_line_end": 250,
  "registry_ids": [
    "V.D105"
  ],
  "related_registry_items": [
    {
      "id": "V.D105",
      "title": "Debye number",
      "url": "/registry/object/V.D105/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L243-L250",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L243-L250",
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
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean#L243-L250)
- Source range: L243-L250
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D105` — Debye number

## Immediate Comment / Docstring

```lean
/-- [V.D105] Debye number: N_D = n₀ λ_D³, the number of charge carriers
    in a Debye sphere.

    When N_D >> 1, collective effects dominate individual two-body
    collisions (strongly collective plasma). -/
```

## Source Excerpt

```lean
structure DebyeNumber where
  /-- Number of carriers in Debye sphere. -/
  n_d : Nat
  /-- Whether collective regime (N_D >> 1). -/
  is_collective : Bool
  /-- Collective when N_D > 10. -/
  collective_correct : is_collective = true → n_d > 10
  deriving Repr
```

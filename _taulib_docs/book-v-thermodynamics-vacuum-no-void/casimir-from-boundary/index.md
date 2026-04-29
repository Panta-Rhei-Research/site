---
{
  "projection_kind": "taulib_declaration",
  "title": "CasimirFromBoundary",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/casimir-from-boundary/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::CasimirFromBoundary",
  "declaration_slug": "casimir-from-boundary",
  "kind": "structure",
  "name": "CasimirFromBoundary",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 214,
  "source_line_end": 225,
  "registry_ids": [
    "V.P39"
  ],
  "related_registry_items": [
    {
      "id": "V.P39",
      "title": "Casimir effect from boundary modes",
      "url": "/registry/object/V.P39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L214-L225",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
        "url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L214-L225",
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

- Module: [TauLib.BookV.Thermodynamics.VacuumNoVoid](/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/)
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L214-L225)
- Source range: L214-L225
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P39` — Casimir effect from boundary modes

## Immediate Comment / Docstring

```lean
/-- [V.P39] Casimir effect from boundary modes: the Casimir force
    F_Cas = -pi^2 hbar c / (240 d^4) * A is reproduced as the
    difference in boundary energies between constrained (plates)
    and unconstrained geometry.

    The result follows from boundary mode counting on L, not from
    summing zero-point energies in momentum space. -/
```

## Source Excerpt

```lean
structure CasimirFromBoundary where
  /-- Plate separation numerator (in natural units). -/
  separation_numer : Nat
  /-- Plate separation denominator. -/
  separation_denom : Nat
  /-- Denominator positive. -/
  denom_pos : separation_denom > 0
  /-- Whether the boundary derivation reproduces the standard result. -/
  reproduces_standard : Bool := true
  /-- Whether mode summation is used. -/
  uses_mode_summation : Bool := false
  deriving Repr
```

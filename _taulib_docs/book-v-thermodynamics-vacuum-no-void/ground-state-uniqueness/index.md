---
{
  "projection_kind": "taulib_declaration",
  "title": "GroundStateUniqueness",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/ground-state-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::GroundStateUniqueness",
  "declaration_slug": "ground-state-uniqueness",
  "kind": "structure",
  "name": "GroundStateUniqueness",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 189,
  "source_line_end": 196,
  "registry_ids": [
    "V.T67"
  ],
  "related_registry_items": [
    {
      "id": "V.T67",
      "title": "H_partial[omega",
      "url": "/registry/object/V.T67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L189-L196",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L189-L196",
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
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L189-L196)
- Source range: L189-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T67` — H_partial[omega

## Immediate Comment / Docstring

```lean
/-- [V.T67] The ground state of H_partial[omega] is the unique vacuum:
    - S_def = 0 (zero defect entropy)
    - E = E_bdry <= E[psi] for all configurations psi (minimal energy)
    - dbar_b omega_0 = 0 on all of tau^3 (holomorphic)

    Uniqueness follows from the convexity of the defect functional
    on the compact base tau^1. -/
```

## Source Excerpt

```lean
structure GroundStateUniqueness where
  /-- The unique vacuum. -/
  vacuum : TauVacuum
  /-- Whether the ground state is unique. -/
  is_unique : Bool := true
  /-- Whether uniqueness follows from convexity. -/
  from_convexity : Bool := true
  deriving Repr
```

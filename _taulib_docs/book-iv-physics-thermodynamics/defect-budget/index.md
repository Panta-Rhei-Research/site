---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectBudget",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/defect-budget/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::DefectBudget",
  "declaration_slug": "defect-budget",
  "kind": "structure",
  "name": "DefectBudget",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 116,
  "source_line_end": 124,
  "registry_ids": [
    "IV.D25"
  ],
  "related_registry_items": [
    {
      "id": "IV.D25",
      "title": "Defect Budget",
      "url": "/registry/object/IV.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L116-L124",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.Thermodynamics",
        "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L116-L124",
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

- Module: [TauLib.BookIV.Physics.Thermodynamics](/verify/taulib/docs/book-iv-physics-thermodynamics/)
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L116-L124)
- Source range: L116-L124
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D25` — Defect Budget

## Immediate Comment / Docstring

```lean
/-- [IV.D25] Defect budget: the conserved total of the 4-component
    defect tuple in the Euler (inviscid) regime.

    In the Euler regime, the defect-budget is preserved under
    boundary-automorphism steps:
    ∑(mobility + vorticity + compression + topological) = const

    This is the τ-native Kelvin circulation theorem. -/
```

## Source Excerpt

```lean
structure DefectBudget where
  /-- The defect tuple. -/
  tuple : DefectTuple
  /-- The conserved total budget. -/
  total : Nat
  /-- Budget equals sum of components. -/
  budget_eq : total = tuple.mobility + tuple.vorticity
                    + tuple.compression + tuple.topological
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauVacuum",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/tau-vacuum/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.VacuumNoVoid`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.VacuumNoVoid::TauVacuum",
  "declaration_slug": "tau-vacuum",
  "kind": "structure",
  "name": "TauVacuum",
  "module_name": "TauLib.BookV.Thermodynamics.VacuumNoVoid",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-vacuum-no-void/",
  "source_line_start": 70,
  "source_line_end": 85,
  "registry_ids": [
    "V.D94"
  ],
  "related_registry_items": [
    {
      "id": "V.D94",
      "title": "The tau-vacuum",
      "url": "/registry/object/V.D94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L70-L85",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L70-L85",
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
- Source path: [`TauLib/BookV/Thermodynamics/VacuumNoVoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/VacuumNoVoid.lean#L70-L85)
- Source range: L70-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D94` — The tau-vacuum

## Immediate Comment / Docstring

```lean
/-- [V.D94] The tau-vacuum: the ground configuration omega_0
    in H_partial[omega] satisfying:
    1. dbar_b omega_0 = 0 everywhere (holomorphic)
    2. S_def[omega_0] = 0 (zero defect entropy)
    3. E[omega_0] = E_bdry (minimal energy = boundary energy)

    The vacuum is NOT "empty space" -- it has definite character
    from the boundary holonomy algebra on L = S^1 v S^1. -/
```

## Source Excerpt

```lean
structure TauVacuum where
  /-- Whether dbar_b omega_0 = 0 (holomorphic). -/
  is_holomorphic : Bool := true
  /-- Defect entropy (zero in vacuum). -/
  s_def : Nat := 0
  /-- Vacuum is at zero defect entropy. -/
  zero_defect : s_def = 0 := by rfl
  /-- Boundary energy numerator. -/
  e_bdry_numer : Nat
  /-- Boundary energy denominator. -/
  e_bdry_denom : Nat
  /-- Denominator positive. -/
  denom_pos : e_bdry_denom > 0
  /-- The vacuum has definite character (not void). -/
  is_not_void : Bool := true
  deriving Repr
```

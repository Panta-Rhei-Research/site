---
{
  "projection_kind": "taulib_declaration",
  "title": "VacuumCirculation",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/vacuum-circulation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::VacuumCirculation",
  "declaration_slug": "vacuum-circulation",
  "kind": "structure",
  "name": "VacuumCirculation",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 279,
  "source_line_end": 290,
  "registry_ids": [
    "V.P31"
  ],
  "related_registry_items": [
    {
      "id": "V.P31",
      "title": "Vacuum circulation is periodic",
      "url": "/registry/object/V.P31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L279-L290",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DefectExhaustion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L279-L290",
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

- Module: [TauLib.BookV.Thermodynamics.DefectExhaustion](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/)
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L279-L290)
- Source range: L279-L290
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P31` — Vacuum circulation is periodic

## Immediate Comment / Docstring

```lean
/-- [V.P31] Vacuum circulation is periodic: in the post-horizon
    regime (n >= n_coh), the evolution on the compact base tau^1
    is periodic with period T_circ > 0.

    The alpha-orbit is holomorphic and defect-free, producing
    eternal coherent circulation. -/
```

## Source Excerpt

```lean
structure VacuumCirculation where
  /-- Period numerator. -/
  period_numer : Nat
  /-- Period denominator. -/
  period_denom : Nat
  /-- Denominator positive. -/
  denom_pos : period_denom > 0
  /-- Period is positive. -/
  period_positive : period_numer > 0
  /-- The circulation is defect-free. -/
  is_defect_free : Bool := true
  deriving Repr
```

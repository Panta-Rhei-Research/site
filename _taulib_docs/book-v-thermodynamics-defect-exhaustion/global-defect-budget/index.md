---
{
  "projection_kind": "taulib_declaration",
  "title": "GlobalDefectBudget",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/global-defect-budget/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::GlobalDefectBudget",
  "declaration_slug": "global-defect-budget",
  "kind": "structure",
  "name": "GlobalDefectBudget",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 89,
  "source_line_end": 101,
  "registry_ids": [
    "V.D88"
  ],
  "related_registry_items": [
    {
      "id": "V.D88",
      "title": "Global defect budget",
      "url": "/registry/object/V.D88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L89-L101",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L89-L101",
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
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L89-L101)
- Source range: L89-L101
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D88` — Global defect budget

## Immediate Comment / Docstring

```lean
/-- [V.D88] Global defect budget: the total defect support summed
    over all orbit depths, measuring the universe's total capacity
    for irreversible processes.

    B_def = sum_{n=0}^{inf} |D_n| -/
```

## Source Excerpt

```lean
structure GlobalDefectBudget where
  /-- Initial defect count. -/
  d_0 : Nat
  /-- Budget upper bound numerator: |D_0| * contraction_denom. -/
  budget_bound_numer : Nat
  /-- Budget upper bound denominator: iota_tau_numer. -/
  budget_bound_denom : Nat
  /-- Denominator positive (iota_tau > 0). -/
  denom_pos : budget_bound_denom > 0
  /-- The budget bound equals |D_0| / iota_tau (scaled). -/
  bound_eq : budget_bound_numer = d_0 * contraction_denom ∧
             budget_bound_denom = iota_tau_numer
  deriving Repr
```

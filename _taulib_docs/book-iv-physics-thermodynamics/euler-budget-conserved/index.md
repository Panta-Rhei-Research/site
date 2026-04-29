---
{
  "projection_kind": "taulib_declaration",
  "title": "euler_budget_conserved",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/euler-budget-conserved/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::euler_budget_conserved",
  "declaration_slug": "euler-budget-conserved",
  "kind": "theorem",
  "name": "euler_budget_conserved",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 203,
  "source_line_end": 205,
  "registry_ids": [
    "IV.T04"
  ],
  "related_registry_items": [
    {
      "id": "IV.T04",
      "title": "Euler Budget Conservation",
      "url": "/registry/object/IV.T04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L203-L205",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L203-L205",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L203-L205)
- Source range: L203-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T04` — Euler Budget Conservation

## Immediate Comment / Docstring

```lean
/-- [IV.T04] Euler budget conservation: the total defect budget
    is well-defined (equals sum of components). -/
```

## Source Excerpt

```lean
theorem euler_budget_conserved (b : DefectBudget) :
    b.total = b.tuple.total := by
  simp [DefectTuple.total, b.budget_eq]
```

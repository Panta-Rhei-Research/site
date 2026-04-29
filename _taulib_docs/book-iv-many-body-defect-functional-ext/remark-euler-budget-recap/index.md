---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_euler_budget_recap",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/remark-euler-budget-recap/",
  "summary_short": "`def` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::remark_euler_budget_recap",
  "declaration_slug": "remark-euler-budget-recap",
  "kind": "def",
  "name": "remark_euler_budget_recap",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 88,
  "source_line_end": 90,
  "registry_ids": [
    "IV.R155"
  ],
  "related_registry_items": [
    {
      "id": "IV.R155",
      "title": "Euler budget recap",
      "url": "/registry/object/IV.R155/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L88-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L88-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L88-L90)
- Source range: L88-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R155` — Euler budget recap

## Immediate Comment / Docstring

```lean
/-- [IV.R155] Recall: for single defect bundles in the inviscid regime,
    the Euler budget conservation mu + nu + kappa + theta = const holds.
    The many-body extension adds interaction corrections that break
    this simple additivity for macroscopic configurations. -/
```

## Source Excerpt

```lean
def remark_euler_budget_recap : String :=
  "Euler budget: mu + nu + kappa + theta = const (single bundle); " ++
  "many-body adds interaction corrections I_X(C)"
```

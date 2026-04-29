---
{
  "projection_kind": "taulib_declaration",
  "title": "TotalTopologicalCharge",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/total-topological-charge/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::TotalTopologicalCharge",
  "declaration_slug": "total-topological-charge",
  "kind": "structure",
  "name": "TotalTopologicalCharge",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 170,
  "source_line_end": 179,
  "registry_ids": [
    "IV.D214"
  ],
  "related_registry_items": [
    {
      "id": "IV.D214",
      "title": "Total topological charge",
      "url": "/registry/object/IV.D214/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L170-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L170-L179",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L170-L179)
- Source range: L170-L179
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D214` — Total topological charge

## Immediate Comment / Docstring

```lean
/-- [IV.D214] Total topological charge: theta^tot(C) = sum_i theta(d_i).
    This is ADDITIVE with NO averaging and NO interaction correction,
    because theta is a homotopy invariant immune to continuous deformation. -/
```

## Source Excerpt

```lean
structure TotalTopologicalCharge where
  /-- Sum of individual topological charges. -/
  total_charge : Int
  /-- Number of contributing bundles. -/
  num_bundles : Nat
  /-- No interaction correction (homotopy invariant). -/
  no_interaction : Bool := true
  /-- No averaging (additive invariant). -/
  no_averaging : Bool := true
  deriving Repr
```

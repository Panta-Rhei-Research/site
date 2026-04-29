---
{
  "projection_kind": "taulib_declaration",
  "title": "LevelnDefectFunctional",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/leveln-defect-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::LevelnDefectFunctional",
  "declaration_slug": "leveln-defect-functional",
  "kind": "structure",
  "name": "LevelnDefectFunctional",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 239,
  "source_line_end": 248,
  "registry_ids": [
    "IV.D216"
  ],
  "related_registry_items": [
    {
      "id": "IV.D216",
      "title": "Level-n defect functional",
      "url": "/registry/object/IV.D216/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L239-L248",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L239-L248",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L239-L248)
- Source range: L239-L248
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D216` — Level-n defect functional

## Immediate Comment / Docstring

```lean
/-- [IV.D216] The level-n defect functional delta_n[omega] maps clopen
    cylinders at depth n to R^3 x Z, assigning to each C_{n,a} the
    sum of defect components (mu, nu, kappa, theta) over all bundles
    whose addresses lie in that cylinder, plus interaction corrections. -/
```

## Source Excerpt

```lean
structure LevelnDefectFunctional where
  /-- Primorial depth. -/
  depth : Nat
  /-- Number of clopen cylinders. -/
  num_cylinders : Nat
  /-- Output: 3 real components + 1 integer. -/
  output_dim : Nat := 4
  /-- Includes interaction corrections. -/
  includes_interaction : Bool := true
  deriving Repr
```

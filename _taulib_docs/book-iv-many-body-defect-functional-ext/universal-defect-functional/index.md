---
{
  "projection_kind": "taulib_declaration",
  "title": "UniversalDefectFunctional",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/universal-defect-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::UniversalDefectFunctional",
  "declaration_slug": "universal-defect-functional",
  "kind": "structure",
  "name": "UniversalDefectFunctional",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 320,
  "source_line_end": 329,
  "registry_ids": [
    "IV.D217"
  ],
  "related_registry_items": [
    {
      "id": "IV.D217",
      "title": "Universal defect functional",
      "url": "/registry/object/IV.D217/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L320-L329",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L320-L329",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L320-L329)
- Source range: L320-L329
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D217` — Universal defect functional

## Immediate Comment / Docstring

```lean
/-- [IV.D217] The universal defect functional delta[omega] = projlim_n delta_n[omega]
    is the projective limit in the category of finitely-additive set functions,
    well-defined because the inverse system satisfies tower compatibility. -/
```

## Source Excerpt

```lean
structure UniversalDefectFunctional where
  /-- Construction: projective limit. -/
  construction : String := "projlim_n delta_n[omega]"
  /-- Well-defined by tower compatibility. -/
  well_defined : Bool := true
  /-- Domain: clopen subsets of Z-hat. -/
  domain : String := "clopen subsets of Z-hat"
  /-- Codomain: R^3 x Z (defect tuple space). -/
  codomain : String := "R^3 x Z"
  deriving Repr
```

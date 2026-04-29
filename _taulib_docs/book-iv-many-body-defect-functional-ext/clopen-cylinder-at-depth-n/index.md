---
{
  "projection_kind": "taulib_declaration",
  "title": "ClopenCylinderAtDepthN",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/clopen-cylinder-at-depth-n/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::ClopenCylinderAtDepthN",
  "declaration_slug": "clopen-cylinder-at-depth-n",
  "kind": "structure",
  "name": "ClopenCylinderAtDepthN",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 214,
  "source_line_end": 225,
  "registry_ids": [
    "IV.D215"
  ],
  "related_registry_items": [
    {
      "id": "IV.D215",
      "title": "Clopen cylinder at depth n",
      "url": "/registry/object/IV.D215/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L214-L225",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L214-L225",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L214-L225)
- Source range: L214-L225
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D215` — Clopen cylinder at depth n

## Immediate Comment / Docstring

```lean
/-- [IV.D215] A clopen cylinder at primorial depth n: the set
    C_{n,a} = {x in Z-hat : x equiv a mod p_n#} for a in Z/p_n#Z.
    There are exactly p_n# such cylinders partitioning Z-hat,
    each simultaneously open and closed in the profinite topology. -/
```

## Source Excerpt

```lean
structure ClopenCylinderAtDepthN where
  /-- Primorial depth n. -/
  depth : Nat
  /-- Residue class label a. -/
  residue : Nat
  /-- Number of cylinders = p_n# (primorial). -/
  num_cylinders : Nat
  /-- Cylinders partition Z-hat. -/
  partition : Bool := true
  /-- Each cylinder is clopen. -/
  clopen : Bool := true
  deriving Repr
```

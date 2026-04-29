---
{
  "projection_kind": "taulib_declaration",
  "title": "ExistenceAndUniquenessOfLimit",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/existence-and-uniqueness-of-limit/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::ExistenceAndUniquenessOfLimit",
  "declaration_slug": "existence-and-uniqueness-of-limit",
  "kind": "structure",
  "name": "ExistenceAndUniquenessOfLimit",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 341,
  "source_line_end": 348,
  "registry_ids": [
    "IV.P135"
  ],
  "related_registry_items": [
    {
      "id": "IV.P135",
      "title": "Existence and uniqueness of limit",
      "url": "/registry/object/IV.P135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L341-L348",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L341-L348",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L341-L348)
- Source range: L341-L348
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P135` — Existence and uniqueness of limit

## Immediate Comment / Docstring

```lean
/-- [IV.P135] The projective limit delta[omega] exists and is unique:
    tower compatibility guarantees the system (delta_n) is a projective
    system of finitely-additive measures, and the universal property
    of the limit in Pro(FinMeas) gives uniqueness. -/
```

## Source Excerpt

```lean
structure ExistenceAndUniquenessOfLimit where
  /-- Exists. -/
  exists_limit : Bool := true
  /-- Unique (universal property). -/
  unique : Bool := true
  /-- Category: Pro(FinMeas). -/
  category : String := "Pro(FinMeas)"
  deriving Repr
```

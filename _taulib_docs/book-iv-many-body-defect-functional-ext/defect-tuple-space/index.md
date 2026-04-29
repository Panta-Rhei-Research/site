---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectTupleSpace",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/defect-tuple-space/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::DefectTupleSpace",
  "declaration_slug": "defect-tuple-space",
  "kind": "structure",
  "name": "DefectTupleSpace",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 364,
  "source_line_end": 375,
  "registry_ids": [
    "IV.D218"
  ],
  "related_registry_items": [
    {
      "id": "IV.D218",
      "title": "Defect tuple space",
      "url": "/registry/object/IV.D218/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L364-L375",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L364-L375",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L364-L375)
- Source range: L364-L375
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D218` — Defect tuple space

## Immediate Comment / Docstring

```lean
/-- [IV.D218] The defect tuple space D = R_{>=0} x R x R x Z, where
    the four factors are: mobility (non-negative), vorticity (signed),
    compression (signed), topological charge (integer).

    This is the codomain of the universal defect functional. -/
```

## Source Excerpt

```lean
structure DefectTupleSpace where
  /-- Mobility: non-negative. -/
  mobility_nonneg : Bool := true
  /-- Vorticity: signed real. -/
  vorticity_signed : Bool := true
  /-- Compression: signed real. -/
  compression_signed : Bool := true
  /-- Topological charge: integer. -/
  topological_integer : Bool := true
  /-- Number of components. -/
  num_components : Nat := 4
  deriving Repr
```

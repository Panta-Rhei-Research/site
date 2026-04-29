---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroscopicDefectTuple",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-defect-tuple/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::MacroscopicDefectTuple",
  "declaration_slug": "macroscopic-defect-tuple",
  "kind": "structure",
  "name": "MacroscopicDefectTuple",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 104,
  "source_line_end": 123,
  "registry_ids": [
    "IV.D210"
  ],
  "related_registry_items": [
    {
      "id": "IV.D210",
      "title": "Macroscopic defect tuple",
      "url": "/registry/object/IV.D210/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L104-L123",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L104-L123",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L104-L123)
- Source range: L104-L123
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D210` — Macroscopic defect tuple

## Immediate Comment / Docstring

```lean
/-- [IV.D210] The macroscopic defect tuple for an N-bundle configuration C
    in sector X: D_X^macro(C) = sum_i D_X(d_i) + I_X(C), where I_X(C)
    is the interaction correction and the total is summed over all five
    sectors {D, A, B, C, omega}.

    The interaction correction I_X encodes collective effects:
    in crystals it locks mobility to zero, in superfluids it
    quantizes circulation. -/
```

## Source Excerpt

```lean
structure MacroscopicDefectTuple where
  /-- Number of bundles in configuration. -/
  num_bundles : Nat
  /-- Sum of individual mobilities. -/
  mobility_sum : Nat
  /-- Sum of individual vorticities. -/
  vorticity_sum : Nat
  /-- Sum of individual compressions. -/
  compression_sum : Nat
  /-- Sum of individual topological charges. -/
  topological_sum : Int
  /-- Interaction correction: mobility component. -/
  interaction_mobility : Int
  /-- Interaction correction: vorticity component. -/
  interaction_vorticity : Int
  /-- Interaction correction: compression component. -/
  interaction_compression : Int
  /-- At least 1 bundle. -/
  nonempty : num_bundles ≥ 1
  deriving Repr
```

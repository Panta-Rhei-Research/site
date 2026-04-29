---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectComponent",
  "permalink": "/verify/taulib/docs/book-iv-physics-defect-functional/defect-component/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.DefectFunctional`.",
  "declaration_id": "TauLib.BookIV.Physics.DefectFunctional::DefectComponent",
  "declaration_slug": "defect-component",
  "kind": "inductive",
  "name": "DefectComponent",
  "module_name": "TauLib.BookIV.Physics.DefectFunctional",
  "module_url": "/verify/taulib/docs/book-iv-physics-defect-functional/",
  "source_line_start": 59,
  "source_line_end": 68,
  "registry_ids": [
    "IV.D16"
  ],
  "related_registry_items": [
    {
      "id": "IV.D16",
      "title": "Defect Component",
      "url": "/registry/object/IV.D16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L59-L68",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.DefectFunctional",
        "url": "/verify/taulib/docs/book-iv-physics-defect-functional/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L59-L68",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Physics.DefectFunctional](/verify/taulib/docs/book-iv-physics-defect-functional/)
- Source path: [`TauLib/BookIV/Physics/DefectFunctional.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L59-L68)
- Source range: L59-L68
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D16` — Defect Component

## Immediate Comment / Docstring

```lean
/-- [IV.D16] The 4 canonical defect components.
    These are the independent degrees of freedom in the defect functional,
    computed on clopen adjacency graphs without importing the reals. -/
```

## Source Excerpt

```lean
inductive DefectComponent where
  /-- Local transport capability (diffusion rate on adjacency graph). -/
  | Mobility
  /-- Rotational motion signature (Kelvin-type circulation invariant). -/
  | Vorticity
  /-- Volumetric density change (∇·u incompressibility measure). -/
  | Compression
  /-- Winding/defect count on clopen tower (topological charge). -/
  | Topological
  deriving Repr, DecidableEq, BEq, Inhabited
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "FirstOrderTransition",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/first-order-transition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::FirstOrderTransition",
  "declaration_slug": "first-order-transition",
  "kind": "structure",
  "name": "FirstOrderTransition",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 356,
  "source_line_end": 363,
  "registry_ids": [
    "IV.D229"
  ],
  "related_registry_items": [
    {
      "id": "IV.D229",
      "title": "First-order phase transition",
      "url": "/registry/object/IV.D229/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L356-L363",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L356-L363",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt2](/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L356-L363)
- Source range: L356-L363
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D229` — First-order phase transition

## Immediate Comment / Docstring

```lean
/-- [IV.D229] A first-order phase transition at defect entropy S_0 is a
    discontinuity in the tau-temperature: lim_{S->S_0^-} T_tau(S) is
    different from lim_{S->S_0^+} T_tau(S). The defect tuple jumps
    discontinuously across a regime boundary. -/
```

## Source Excerpt

```lean
structure FirstOrderTransition where
  /-- Temperature discontinuity. -/
  temp_discontinuous : Bool := true
  /-- Defect tuple jumps. -/
  tuple_jumps : Bool := true
  /-- Latent heat = jump magnitude. -/
  has_latent_heat : Bool := true
  deriving Repr
```

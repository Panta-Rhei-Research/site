---
{
  "projection_kind": "taulib_declaration",
  "title": "PhaseTransitionRegimeCrossing",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/phase-transition-regime-crossing/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::PhaseTransitionRegimeCrossing",
  "declaration_slug": "phase-transition-regime-crossing",
  "kind": "structure",
  "name": "PhaseTransitionRegimeCrossing",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 387,
  "source_line_end": 396,
  "registry_ids": [
    "IV.T92"
  ],
  "related_registry_items": [
    {
      "id": "IV.T92",
      "title": "Phase transition as regime crossing",
      "url": "/registry/object/IV.T92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L387-L396",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L387-L396",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L387-L396)
- Source range: L387-L396
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T92` — Phase transition as regime crossing

## Immediate Comment / Docstring

```lean
/-- [IV.T92] Every phase transition is an inequality crossing in D:
    first-order transitions correspond to the defect tuple jumping
    discontinuously from one regime to another, second-order transitions
    to the tuple arriving at a regime boundary continuously.

    There are no "exotic" phase transitions outside this classification. -/
```

## Source Excerpt

```lean
structure PhaseTransitionRegimeCrossing where
  /-- First-order: discontinuous crossing. -/
  first_order_discontinuous : Bool := true
  /-- Second-order: continuous crossing. -/
  second_order_continuous : Bool := true
  /-- No exotic transitions outside classification. -/
  complete_classification : Bool := true
  /-- All transitions are regime crossings in D. -/
  all_are_regime_crossings : Bool := true
  deriving Repr
```

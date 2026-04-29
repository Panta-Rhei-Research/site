---
{
  "projection_kind": "taulib_declaration",
  "title": "CCCSide",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/cccside/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.StructuralExclusion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.StructuralExclusion::CCCSide",
  "declaration_slug": "cccside",
  "kind": "structure",
  "name": "CCCSide",
  "module_name": "TauLib.BookI.MetaLogic.StructuralExclusion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/",
  "source_line_start": 65,
  "source_line_end": 71,
  "registry_ids": [
    "I.D81"
  ],
  "related_registry_items": [
    {
      "id": "I.D81",
      "title": "CCC-Linear Dichotomy",
      "url": "/registry/object/I.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L65-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.StructuralExclusion",
        "url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L65-L71",
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

- Module: [TauLib.BookI.MetaLogic.StructuralExclusion](/verify/taulib/docs/book-i-meta-logic-structural-exclusion/)
- Source path: [`TauLib/BookI/MetaLogic/StructuralExclusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L65-L71)
- Source range: L65-L71
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D81` — CCC-Linear Dichotomy

## Immediate Comment / Docstring

```lean
/-- [I.D81] The CCC side of the dichotomy: cartesian-closed categories
    have free diagonal maps Δ : A → A × A, which enable the Lawvere
    fixed-point argument. Self-hosting is obstructed. -/
```

## Source Excerpt

```lean
structure CCCSide where
  /-- Free diagonals are available -/
  freeDiagonals : Bool
  /-- The Lawvere barrier applies -/
  lawvereBarrier : Bool
  /-- Consistency: free diagonals imply the barrier -/
  barrier_from_diag : freeDiagonals = true → lawvereBarrier = true
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "StarAutonomousSide",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/star-autonomous-side/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.StructuralExclusion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.StructuralExclusion::StarAutonomousSide",
  "declaration_slug": "star-autonomous-side",
  "kind": "structure",
  "name": "StarAutonomousSide",
  "module_name": "TauLib.BookI.MetaLogic.StructuralExclusion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/",
  "source_line_start": 77,
  "source_line_end": 83,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L77-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L77-L83",
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
- Source path: [`TauLib/BookI/MetaLogic/StructuralExclusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L77-L83)
- Source range: L77-L83
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D81` — CCC-Linear Dichotomy

## Immediate Comment / Docstring

```lean
/-- [I.D81] The star-autonomous side of the dichotomy: star-autonomous
    categories replace the cartesian product × with the tensor ⊗.
    The diagonal Δ : A → A ⊗ A is not freely available — it must be
    earned. The Lawvere barrier does not apply. -/
```

## Source Excerpt

```lean
structure StarAutonomousSide where
  /-- Free diagonals are NOT available -/
  noFreeDiagonals : Bool
  /-- The Lawvere barrier does NOT apply -/
  noLawvereBarrier : Bool
  /-- Consistency: no free diagonals imply no barrier -/
  no_barrier_from_no_diag : noFreeDiagonals = true → noLawvereBarrier = true
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "K5StructuralExclusion",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/k5-structural-exclusion/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.StructuralExclusion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.StructuralExclusion::K5StructuralExclusion",
  "declaration_slug": "k5-structural-exclusion",
  "kind": "structure",
  "name": "K5StructuralExclusion",
  "module_name": "TauLib.BookI.MetaLogic.StructuralExclusion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/",
  "source_line_start": 109,
  "source_line_end": 117,
  "registry_ids": [
    "I.T39"
  ],
  "related_registry_items": [
    {
      "id": "I.T39",
      "title": "K5 Structural Exclusion",
      "url": "/registry/object/I.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L109-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L109-L117",
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
- Source path: [`TauLib/BookI/MetaLogic/StructuralExclusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L109-L117)
- Source range: L109-L117
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.T39` — K5 Structural Exclusion

## Immediate Comment / Docstring

```lean
/-- [I.T39] K5 Structural Exclusion Theorem.

    K5's diagonal discipline (DiagonalAspect.noUnearnedDiagonals) places τ
    on the star-autonomous side of the CCC-linear dichotomy. Specifically:
    1. K5 refuses free diagonals (contraction is refused — from Substrate.lean)
    2. Refusing free diagonals places τ on the star-autonomous side
    3. On the star-autonomous side, the Lawvere barrier does not apply
    4. Therefore: the standard obstruction to self-hosting is excluded -/
```

## Source Excerpt

```lean
structure K5StructuralExclusion where
  /-- K5 refuses contraction (no free diagonals) -/
  contraction_refused : k5_status .contraction = .refused
  /-- The diagonal-to-linear map sends noUnearnedDiagonals to noFreeContraction -/
  diagonal_is_linear : diag_to_linear .noUnearnedDiagonals = .noFreeContraction
  /-- τ is on the star-autonomous side -/
  tau_star_autonomous : StarAutonomousSide
  /-- On the star-autonomous side, the Lawvere barrier does not apply -/
  no_barrier : tau_star_autonomous.noLawvereBarrier = true
```

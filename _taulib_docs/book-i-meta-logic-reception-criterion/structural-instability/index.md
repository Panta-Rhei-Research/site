---
{
  "projection_kind": "taulib_declaration",
  "title": "StructuralInstability",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/structural-instability/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.ReceptionCriterion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.ReceptionCriterion::StructuralInstability",
  "declaration_slug": "structural-instability",
  "kind": "structure",
  "name": "StructuralInstability",
  "module_name": "TauLib.BookI.MetaLogic.ReceptionCriterion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/",
  "source_line_start": 60,
  "source_line_end": 68,
  "registry_ids": [
    "I.D93"
  ],
  "related_registry_items": [
    {
      "id": "I.D93",
      "title": "Structural Instability",
      "url": "/registry/object/I.D93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L60-L68",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.ReceptionCriterion",
        "url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L60-L68",
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

- Module: [TauLib.BookI.MetaLogic.ReceptionCriterion](/verify/taulib/docs/book-i-meta-logic-reception-criterion/)
- Source path: [`TauLib/BookI/MetaLogic/ReceptionCriterion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L60-L68)
- Source range: L60-L68
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D93` — Structural Instability

## Immediate Comment / Docstring

```lean
/-- [I.D93] Structural instability: a foundation exhibits structural instability
    when diagonal resonance prevents canonical, identity-faithful intended semantics. -/
```

## Source Excerpt

```lean
structure StructuralInstability where
  /-- The foundation's resonance profile -/
  resonance : DiagonalResonance
  /-- Full resonance is present -/
  full_resonance : resonance.isFullResonance = true
  /-- Cannot stabilize unique ontic closure -/
  no_unique_closure : Bool := true
  /-- Cannot fix ontology without VM-relativity -/
  vm_relative : Bool := true
```

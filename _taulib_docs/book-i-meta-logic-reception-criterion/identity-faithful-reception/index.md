---
{
  "projection_kind": "taulib_declaration",
  "title": "IdentityFaithfulReception",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/identity-faithful-reception/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.ReceptionCriterion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.ReceptionCriterion::IdentityFaithfulReception",
  "declaration_slug": "identity-faithful-reception",
  "kind": "structure",
  "name": "IdentityFaithfulReception",
  "module_name": "TauLib.BookI.MetaLogic.ReceptionCriterion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/",
  "source_line_start": 39,
  "source_line_end": 45,
  "registry_ids": [
    "I.D92"
  ],
  "related_registry_items": [
    {
      "id": "I.D92",
      "title": "Identity-Faithful Reception",
      "url": "/registry/object/I.D92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L39-L45",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L39-L45",
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
- Source path: [`TauLib/BookI/MetaLogic/ReceptionCriterion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L39-L45)
- Source range: L39-L45
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D92` — Identity-Faithful Reception

## Immediate Comment / Docstring

```lean
/-- [I.D92] Identity-faithful reception: a foundation can receive τ only if
    its resonance profile allows preserving ontic identity. -/
```

## Source Excerpt

```lean
structure IdentityFaithfulReception where
  /-- The host foundation's resonance profile -/
  host_resonance : DiagonalResonance
  /-- All three reception conditions must be satisfiable -/
  all_conditions_met : Bool
  /-- If host has full resonance, conditions CANNOT be met -/
  resonance_blocks : host_resonance.isFullResonance = true → all_conditions_met = false
```

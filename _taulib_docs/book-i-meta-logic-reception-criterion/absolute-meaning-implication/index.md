---
{
  "projection_kind": "taulib_declaration",
  "title": "AbsoluteMeaningImplication",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/absolute-meaning-implication/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.ReceptionCriterion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.ReceptionCriterion::AbsoluteMeaningImplication",
  "declaration_slug": "absolute-meaning-implication",
  "kind": "structure",
  "name": "AbsoluteMeaningImplication",
  "module_name": "TauLib.BookI.MetaLogic.ReceptionCriterion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/",
  "source_line_start": 136,
  "source_line_end": 142,
  "registry_ids": [
    "I.R26"
  ],
  "related_registry_items": [
    {
      "id": "I.R26",
      "title": "Implications for Absolute Meaning",
      "url": "/registry/object/I.R26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L136-L142",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L136-L142",
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
- Source path: [`TauLib/BookI/MetaLogic/ReceptionCriterion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L136-L142)
- Source range: L136-L142
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.R26` — Implications for Absolute Meaning

## Immediate Comment / Docstring

```lean
/-- [I.R26] The relationship between identity coherence and absolute meaning. -/
```

## Source Excerpt

```lean
structure AbsoluteMeaningImplication where
  /-- Identity coherence is a prerequisite for absolute meaning -/
  coherence_required : Bool
  /-- Unique omega is a prerequisite for absolute meaning -/
  omega_required : Bool
  /-- Both are true -/
  both_required : coherence_required = true ∧ omega_required = true
```

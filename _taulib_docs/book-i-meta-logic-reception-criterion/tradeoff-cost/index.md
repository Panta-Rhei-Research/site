---
{
  "projection_kind": "taulib_declaration",
  "title": "TradeoffCost",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/tradeoff-cost/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.ReceptionCriterion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.ReceptionCriterion::TradeoffCost",
  "declaration_slug": "tradeoff-cost",
  "kind": "inductive",
  "name": "TradeoffCost",
  "module_name": "TauLib.BookI.MetaLogic.ReceptionCriterion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/",
  "source_line_start": 170,
  "source_line_end": 174,
  "registry_ids": [
    "I.R27"
  ],
  "related_registry_items": [
    {
      "id": "I.R27",
      "title": "Honest Scope Declaration",
      "url": "/registry/object/I.R27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L170-L174",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L170-L174",
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

- Module: [TauLib.BookI.MetaLogic.ReceptionCriterion](/verify/taulib/docs/book-i-meta-logic-reception-criterion/)
- Source path: [`TauLib/BookI/MetaLogic/ReceptionCriterion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L170-L174)
- Source range: L170-L174
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.R27` — Honest Scope Declaration

## Immediate Comment / Docstring

```lean
/-- [I.R27] What τ must earn in later books because of the trade-off. -/
```

## Source Excerpt

```lean
inductive TradeoffCost where
  | epsilonDelta        -- Earned in Book II
  | localSmoothness     -- Earned in Book II
  | classicalLaplacian  -- Earned in Book III (fourth quadrant)
  deriving DecidableEq, Repr
```

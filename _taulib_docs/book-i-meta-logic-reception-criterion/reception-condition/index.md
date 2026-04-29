---
{
  "projection_kind": "taulib_declaration",
  "title": "ReceptionCondition",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/reception-condition/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.ReceptionCriterion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.ReceptionCriterion::ReceptionCondition",
  "declaration_slug": "reception-condition",
  "kind": "inductive",
  "name": "ReceptionCondition",
  "module_name": "TauLib.BookI.MetaLogic.ReceptionCriterion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-reception-criterion/",
  "source_line_start": 31,
  "source_line_end": 35,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L31-L35",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L31-L35",
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
- Source path: [`TauLib/BookI/MetaLogic/ReceptionCriterion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L31-L35)
- Source range: L31-L35
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.D92` — Identity-Faithful Reception

## Immediate Comment / Docstring

```lean
/-- [I.D92] The three conditions for identity-faithful reception.
    An interpretation functor P : C_τ → C_S must satisfy all three. -/
```

## Source Excerpt

```lean
inductive ReceptionCondition where
  | preservesDistinctness    -- Maps distinct τ-objects to distinct S-objects
  | preservesIdentity        -- P(id_X) = id_{P(X)}
  | reflectsIsomorphism      -- P(X) ≅ P(Y) in S implies X ≅ Y in τ
  deriving DecidableEq, Repr
```

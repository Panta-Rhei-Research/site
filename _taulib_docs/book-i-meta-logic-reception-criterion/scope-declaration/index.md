---
{
  "projection_kind": "taulib_declaration",
  "title": "ScopeDeclaration",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-reception-criterion/scope-declaration/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.ReceptionCriterion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.ReceptionCriterion::ScopeDeclaration",
  "declaration_slug": "scope-declaration",
  "kind": "inductive",
  "name": "ScopeDeclaration",
  "module_name": "TauLib.BookI.MetaLogic.ReceptionCriterion",
  "module_url": "/corpus/taulib/docs/book-i-meta-logic-reception-criterion/",
  "source_line_start": 155,
  "source_line_end": 160,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L155-L160",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.ReceptionCriterion",
        "url": "/corpus/taulib/docs/book-i-meta-logic-reception-criterion/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L155-L160",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.MetaLogic.ReceptionCriterion](/corpus/taulib/docs/book-i-meta-logic-reception-criterion/)
- Source path: [`TauLib/BookI/MetaLogic/ReceptionCriterion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/ReceptionCriterion.lean#L155-L160)
- Source range: L155-L160
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `I.R27` — Honest Scope Declaration

## Immediate Comment / Docstring

```lean
/-- [I.R27] What the structural instability diagnosis does NOT claim. -/
```

## Source Excerpt

```lean
inductive ScopeDeclaration where
  | notInconsistency        -- Not claiming orthodox math is inconsistent
  | structuralDiagnosis     -- A structural diagnosis, not a value judgment
  | tradeoffExists          -- τ pays a cost (no epsilon-delta, etc.)
  | bothDirections          -- Consequences in both directions
  deriving DecidableEq, Repr
```

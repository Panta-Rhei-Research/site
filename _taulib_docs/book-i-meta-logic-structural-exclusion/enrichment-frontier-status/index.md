---
{
  "projection_kind": "taulib_declaration",
  "title": "EnrichmentFrontierStatus",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/enrichment-frontier-status/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.StructuralExclusion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.StructuralExclusion::EnrichmentFrontierStatus",
  "declaration_slug": "enrichment-frontier-status",
  "kind": "inductive",
  "name": "EnrichmentFrontierStatus",
  "module_name": "TauLib.BookI.MetaLogic.StructuralExclusion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/",
  "source_line_start": 132,
  "source_line_end": 138,
  "registry_ids": [
    "I.D82"
  ],
  "related_registry_items": [
    {
      "id": "I.D82",
      "title": "Enrichment Frontier Classification",
      "url": "/registry/object/I.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L132-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L132-L138",
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

- Module: [TauLib.BookI.MetaLogic.StructuralExclusion](/verify/taulib/docs/book-i-meta-logic-structural-exclusion/)
- Source path: [`TauLib/BookI/MetaLogic/StructuralExclusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L132-L138)
- Source range: L132-L138
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.D82` — Enrichment Frontier Classification

## Immediate Comment / Docstring

```lean
/-- [I.D82] The enrichment frontier status classifies each transition
    of the enrichment ladder by its novelty relative to existing work. -/
```

## Source Excerpt

```lean
inductive EnrichmentFrontierStatus where
  | achieved            -- Existing techniques suffice (adaptation needed)
  | partiallyAchieved   -- Known tools exist but novel combination required
  | unprecedented       -- No precedent at meaningful mathematical strength
  deriving DecidableEq, Repr

open EnrichmentFrontierStatus
```

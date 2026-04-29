---
{
  "projection_kind": "taulib_declaration",
  "title": "CellFate",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/cell-fate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::CellFate",
  "declaration_slug": "cell-fate",
  "kind": "structure",
  "name": "CellFate",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 220,
  "source_line_end": 229,
  "registry_ids": [
    "VI.D84"
  ],
  "related_registry_items": [
    {
      "id": "VI.D84",
      "title": "Cell Fate",
      "url": "/registry/object/VI.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L220-L229",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L220-L229",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L220-L229)
- Source range: L220-L229
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D84` — Cell Fate

## Immediate Comment / Docstring

```lean
/-- [VI.D84] Cell Fate.
    Terminal epigenetic state: fully restricted chromatin partition
    at the bottom of the Waddington landscape. The cell expresses
    only the genes required for its specialized function.
    Fixed under SelfDesc maintenance (VI.T03).
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure CellFate where
  /-- Terminal differentiation state. -/
  terminal : Bool := true
  /-- Potency level at terminal state. -/
  potency_level : String := "unipotent"
  /-- Fixed under SelfDesc evaluator maintenance. -/
  fixed_under_selfdesc : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```

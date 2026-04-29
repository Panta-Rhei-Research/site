---
{
  "projection_kind": "taulib_declaration",
  "title": "SecondDistinction",
  "permalink": "/verify/taulib/docs/book-vi-consumer-reproduction/second-distinction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Reproduction`.",
  "declaration_id": "TauLib.BookVI.Consumer.Reproduction::SecondDistinction",
  "declaration_slug": "second-distinction",
  "kind": "structure",
  "name": "SecondDistinction",
  "module_name": "TauLib.BookVI.Consumer.Reproduction",
  "module_url": "/verify/taulib/docs/book-vi-consumer-reproduction/",
  "source_line_start": 70,
  "source_line_end": 79,
  "registry_ids": [
    "VI.T26"
  ],
  "related_registry_items": [
    {
      "id": "VI.T26",
      "title": "Sex as Second Distinction",
      "url": "/registry/object/VI.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L70-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Reproduction",
        "url": "/verify/taulib/docs/book-vi-consumer-reproduction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L70-L79",
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

- Module: [TauLib.BookVI.Consumer.Reproduction](/verify/taulib/docs/book-vi-consumer-reproduction/)
- Source path: [`TauLib/BookVI/Consumer/Reproduction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean#L70-L79)
- Source range: L70-L79
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T26` — Sex as Second Distinction

## Immediate Comment / Docstring

```lean
/-- [VI.T26] Sex as Second Distinction.
    Life's first distinction (VI.D04): self vs non-self.
    Sex introduces a second: self vs other-self.
    This is a refinement (level 1) of the base distinction. -/
```

## Source Excerpt

```lean
structure SecondDistinction where
  /-- First distinction: self vs non-self (VI.D04). -/
  first : String := "self_nonself"
  /-- Second distinction: self vs other-self. -/
  second : String := "self_otherself"
  /-- Refinement level (0 = base, 1 = first refinement). -/
  refinement_level : Nat
  /-- Exactly level 1. -/
  level_eq : refinement_level = 1
  deriving Repr
```

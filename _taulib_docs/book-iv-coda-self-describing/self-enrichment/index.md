---
{
  "projection_kind": "taulib_declaration",
  "title": "SelfEnrichment",
  "permalink": "/verify/taulib/docs/book-iv-coda-self-describing/self-enrichment/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.SelfDescribing`.",
  "declaration_id": "TauLib.BookIV.Coda.SelfDescribing::SelfEnrichment",
  "declaration_slug": "self-enrichment",
  "kind": "structure",
  "name": "SelfEnrichment",
  "module_name": "TauLib.BookIV.Coda.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-iv-coda-self-describing/",
  "source_line_start": 106,
  "source_line_end": 115,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L106-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.SelfDescribing",
        "url": "/verify/taulib/docs/book-iv-coda-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L106-L115",
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

- Module: [TauLib.BookIV.Coda.SelfDescribing](/verify/taulib/docs/book-iv-coda-self-describing/)
- Source path: [`TauLib/BookIV/Coda/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L106-L115)
- Source range: L106-L115
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The self-enrichment property of tau^3: hom-objects are themselves
    objects of tau^3. This is not circular but a structural closure
    analogous to a category enriched over itself (like Set enriched
    over Set, or Cat enriched over Cat).

    The self-enrichment means the universe contains its own instruction set:
    the rules governing tau^3 are encoded as objects within tau^3. -/
```

## Source Excerpt

```lean
structure SelfEnrichment where
  /-- Hom-objects are internal. -/
  hom_internal : Bool := true
  /-- Not logically circular. -/
  not_circular : Bool := true
  /-- Analogous to Set enriched over Set. -/
  analogy : String := "Set enriched over Set"
  /-- Universe contains its own instruction set. -/
  self_instruction : Bool := true
  deriving Repr
```

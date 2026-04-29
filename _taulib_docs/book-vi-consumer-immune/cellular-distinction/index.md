---
{
  "projection_kind": "taulib_declaration",
  "title": "CellularDistinction",
  "permalink": "/verify/taulib/docs/book-vi-consumer-immune/cellular-distinction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Immune`.",
  "declaration_id": "TauLib.BookVI.Consumer.Immune::CellularDistinction",
  "declaration_slug": "cellular-distinction",
  "kind": "structure",
  "name": "CellularDistinction",
  "module_name": "TauLib.BookVI.Consumer.Immune",
  "module_url": "/verify/taulib/docs/book-vi-consumer-immune/",
  "source_line_start": 32,
  "source_line_end": 39,
  "registry_ids": [
    "VI.D51"
  ],
  "related_registry_items": [
    {
      "id": "VI.D51",
      "title": "Cellular Distinction Predicate",
      "url": "/registry/object/VI.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L32-L39",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Immune",
        "url": "/verify/taulib/docs/book-vi-consumer-immune/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L32-L39",
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

- Module: [TauLib.BookVI.Consumer.Immune](/verify/taulib/docs/book-vi-consumer-immune/)
- Source path: [`TauLib/BookVI/Consumer/Immune.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Immune.lean#L32-L39)
- Source range: L32-L39
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D51` — Cellular Distinction Predicate

## Immediate Comment / Docstring

```lean
/-- [VI.D51] Cellular Distinction Predicate (MHC).
    MHC class I + class II implement τ-Distinction (VI.D04)
    at the cellular level: D: Cell → {self, nonself}.
    Book I, Part I provides the abstract binary classifier. -/
```

## Source Excerpt

```lean
structure CellularDistinction where
  /-- MHC class I present (all nucleated cells). -/
  mhc_class_I : Bool := true
  /-- MHC class II present (antigen-presenting cells). -/
  mhc_class_II : Bool := true
  /-- Implements τ-Distinction at cellular level. -/
  distinction_implementation : Bool := true
  deriving Repr
```

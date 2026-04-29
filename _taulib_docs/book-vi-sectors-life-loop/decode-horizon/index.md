---
{
  "projection_kind": "taulib_declaration",
  "title": "DecodeHorizon",
  "permalink": "/verify/taulib/docs/book-vi-sectors-life-loop/decode-horizon/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.LifeLoop`.",
  "declaration_id": "TauLib.BookVI.Sectors.LifeLoop::DecodeHorizon",
  "declaration_slug": "decode-horizon",
  "kind": "structure",
  "name": "DecodeHorizon",
  "module_name": "TauLib.BookVI.Sectors.LifeLoop",
  "module_url": "/verify/taulib/docs/book-vi-sectors-life-loop/",
  "source_line_start": 46,
  "source_line_end": 49,
  "registry_ids": [
    "VI.D12"
  ],
  "related_registry_items": [
    {
      "id": "VI.D12",
      "title": "DecodeHorizon",
      "url": "/registry/object/VI.D12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L46-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.LifeLoop",
        "url": "/verify/taulib/docs/book-vi-sectors-life-loop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L46-L49",
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

- Module: [TauLib.BookVI.Sectors.LifeLoop](/verify/taulib/docs/book-vi-sectors-life-loop/)
- Source path: [`TauLib/BookVI/Sectors/LifeLoop.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L46-L49)
- Source range: L46-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D12` — DecodeHorizon

## Immediate Comment / Docstring

```lean
/-- [VI.D12] DecodeHorizon: extracts unique ω-germ code constant across B_n. -/
```

## Source Excerpt

```lean
structure DecodeHorizon where
  extracts_code : Bool := true
  code_constant : Bool := true
  deriving Repr
```

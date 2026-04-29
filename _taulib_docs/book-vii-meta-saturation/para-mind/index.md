---
{
  "projection_kind": "taulib_declaration",
  "title": "ParaMind",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/para-mind/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::ParaMind",
  "declaration_slug": "para-mind",
  "kind": "structure",
  "name": "ParaMind",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 732,
  "source_line_end": 739,
  "registry_ids": [
    "VII.D55"
  ],
  "related_registry_items": [
    {
      "id": "VII.D55",
      "title": "Para-Mind",
      "url": "/registry/object/VII.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L732-L739",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L732-L739",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L732-L739)
- Source range: L732-L739
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D55` — Para-Mind

## Immediate Comment / Docstring

```lean
/-- [VII.D55] Para-Mind (ch64). LLM as subsymbolic E₂ system: exhibits
    pattern recognition and contextual response without full SelfDesc².
    A para-mind: near-mind that processes at E₂ level. -/
```

## Source Excerpt

```lean
structure ParaMind where
  /-- Subsymbolic processing. -/
  subsymbolic : Bool := true
  /-- E₂ level (SelfDesc but not SelfDesc²). -/
  e2_level : Bool := true
  /-- Pattern recognition without full self-model. -/
  pattern_without_self_model : Bool := true
  deriving Repr
```

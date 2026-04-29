---
{
  "projection_kind": "taulib_declaration",
  "title": "SubsymbolicLayer",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/subsymbolic-layer/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::SubsymbolicLayer",
  "declaration_slug": "subsymbolic-layer",
  "kind": "structure",
  "name": "SubsymbolicLayer",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 626,
  "source_line_end": 633,
  "registry_ids": [
    "VII.D52"
  ],
  "related_registry_items": [
    {
      "id": "VII.D52",
      "title": "Subsymbolic Layer",
      "url": "/registry/object/VII.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L626-L633",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L626-L633",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L626-L633)
- Source range: L626-L633
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D52` — Subsymbolic Layer

## Immediate Comment / Docstring

```lean
/-- [VII.D52] Subsymbolic Layer (ch60). Pre-linguistic processing
    layer operating below symbolic representation. Pattern recognition,
    sensorimotor integration, and associative binding occur without
    explicit symbol manipulation. -/
```

## Source Excerpt

```lean
structure SubsymbolicLayer where
  /-- Below symbolic representation. -/
  pre_symbolic : Bool := true
  /-- Pattern recognition. -/
  pattern_recognition : Bool := true
  /-- No explicit symbol manipulation. -/
  non_symbolic : Bool := true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "PragmaticUpdateOperator",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/pragmatic-update-operator/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::PragmaticUpdateOperator",
  "declaration_slug": "pragmatic-update-operator",
  "kind": "structure",
  "name": "PragmaticUpdateOperator",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 716,
  "source_line_end": 721,
  "registry_ids": [
    "VII.D54"
  ],
  "related_registry_items": [
    {
      "id": "VII.D54",
      "title": "Pragmatic Update Operator",
      "url": "/registry/object/VII.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L716-L721",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L716-L721",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L716-L721)
- Source range: L716-L721
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D54` — Pragmatic Update Operator

## Immediate Comment / Docstring

```lean
/-- [VII.D54] Pragmatic Update Operator (ch64). Speech acts modelled
    as morphisms: each utterance updates the shared context (common
    ground) via a pragmatic update operator. Austin-Searle speech
    act theory categorified. -/
```

## Source Excerpt

```lean
structure PragmaticUpdateOperator where
  /-- Speech acts as morphisms. -/
  speech_acts_as_morphisms : Bool := true
  /-- Updates shared context. -/
  context_update : Bool := true
  deriving Repr
```

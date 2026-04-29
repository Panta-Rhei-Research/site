---
{
  "projection_kind": "taulib_declaration",
  "title": "MetaDecodeOperator",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/meta-decode-operator/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::MetaDecodeOperator",
  "declaration_slug": "meta-decode-operator",
  "kind": "structure",
  "name": "MetaDecodeOperator",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 208,
  "source_line_end": 215,
  "registry_ids": [
    "VII.D05"
  ],
  "related_registry_items": [
    {
      "id": "VII.D05",
      "title": "MetaDecode Operator",
      "url": "/registry/object/VII.D05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L208-L215",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L208-L215",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L208-L215)
- Source range: L208-L215
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D05` — MetaDecode Operator

## Immediate Comment / Docstring

```lean
/-- [VII.D05] MetaDecode operator: maps entire self-describing system
    to internal model of its own code-carrying structure.
    Key distinction from E₂: evaluator takes Φ (decode map) itself as input,
    not just the genetic code G. -/
```

## Source Excerpt

```lean
structure MetaDecodeOperator where
  /-- Faithful: preserves structural relationships. -/
  faithful : Bool := true
  /-- Self-referential: takes decode map Φ as input. -/
  self_referential : Bool := true
  /-- Well-defined: produces consistent internal model. -/
  well_defined : Bool := true
  deriving Repr
```

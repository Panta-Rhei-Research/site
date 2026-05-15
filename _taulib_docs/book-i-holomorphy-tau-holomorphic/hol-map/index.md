---
{
  "projection_kind": "taulib_declaration",
  "title": "HolMap",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-map/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.TauHolomorphic::HolMap",
  "declaration_slug": "hol-map",
  "kind": "structure",
  "name": "HolMap",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "source_line_start": 124,
  "source_line_end": 130,
  "registry_ids": [
    "I.D48"
  ],
  "related_registry_items": [
    {
      "id": "I.D48",
      "title": "Tau-Holomorphic Map",
      "url": "/registry/object/I.D48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L124-L130",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
        "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L124-L130",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.Holomorphy.TauHolomorphic](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L124-L130)
- Source range: L124-L130
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `I.D48` — Tau-Holomorphic Map

## Immediate Comment / Docstring

```lean
/-- [I.D48] A τ-holomorphic map bundles a HolFun with source/target data. -/
```

## Source Excerpt

```lean
structure HolMap where
  /-- The underlying holomorphic function. -/
  fun_ : HolFun
  /-- Source object index in τ-Idx. -/
  source : TauIdx
  /-- Target object index in τ-Idx. -/
  target : TauIdx
```

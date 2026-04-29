---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongConnection",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/strong-connection/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::StrongConnection",
  "declaration_slug": "strong-connection",
  "kind": "structure",
  "name": "StrongConnection",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 75,
  "source_line_end": 82,
  "registry_ids": [
    "IV.D170"
  ],
  "related_registry_items": [
    {
      "id": "IV.D170",
      "title": "Strong connection assignment",
      "url": "/registry/object/IV.D170/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L75-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L75-L82",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L75-L82)
- Source range: L75-L82
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D170` — Strong connection assignment

## Immediate Comment / Docstring

```lean
/-- [IV.D170] A strong connection at stage n: a map assigning
    color phase automorphisms to edges of the finite cell complex.
    The tau-analogue of a gauge connection on a lattice. -/
```

## Source Excerpt

```lean
structure StrongConnection where
  /-- Stage n. -/
  stage : Nat
  /-- Maps edges to color-phase automorphisms. -/
  edge_to_aut : Bool := true
  /-- Finite cell complex. -/
  finite_complex : Bool := true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "transport_in_range",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/transport-in-range/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::transport_in_range",
  "declaration_slug": "transport-in-range",
  "kind": "def",
  "name": "transport_in_range",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 103,
  "source_line_end": 106,
  "registry_ids": [
    "II.D79"
  ],
  "related_registry_items": [
    {
      "id": "II.D79",
      "title": "Parallel Transport",
      "url": "/registry/object/II.D79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L103-L106",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Connection",
        "url": "/verify/taulib/docs/book-ii-closure-connection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L103-L106",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Closure.Connection](/verify/taulib/docs/book-ii-closure-connection/)
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L103-L106)
- Source range: L103-L106
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D79` — Parallel Transport

## Immediate Comment / Docstring

```lean
/-- [II.D79] Transport check: verify that transport along a path
    at stage k stays within Z/M_k Z. -/
```

## Source Excerpt

```lean
def transport_in_range (conn : TauConnection) (k : Nat)
    (x : Nat) (path : List Nat) : Bool :=
  let result := parallel_transport conn k x path
  result < primorial k
```

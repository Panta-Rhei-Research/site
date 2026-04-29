---
{
  "projection_kind": "taulib_declaration",
  "title": "parallel_transport",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/parallel-transport/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::parallel_transport",
  "declaration_slug": "parallel-transport",
  "kind": "def",
  "name": "parallel_transport",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 97,
  "source_line_end": 99,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L97-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L97-L99",
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
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L97-L99)
- Source range: L97-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D79` — Parallel Transport

## Immediate Comment / Docstring

```lean
/-- [II.D79] Transport a value x along a path (list of direction vectors)
    at stage k. -/
```

## Source Excerpt

```lean
def parallel_transport (conn : TauConnection) (k : Nat)
    (x : Nat) (path : List Nat) : Nat :=
  path.foldl (fun pos v => conn.transport k pos v) x
```

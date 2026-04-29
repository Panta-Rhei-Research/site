---
{
  "projection_kind": "taulib_declaration",
  "title": "flatness_check_loop",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/flatness-check-loop/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::flatness_check_loop",
  "declaration_slug": "flatness-check-loop",
  "kind": "def",
  "name": "flatness_check_loop",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 114,
  "source_line_end": 117,
  "registry_ids": [
    "II.T50"
  ],
  "related_registry_items": [
    {
      "id": "II.T50",
      "title": "Flat Connection Existence",
      "url": "/registry/object/II.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L114-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L114-L117",
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
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L114-L117)
- Source range: L114-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T50` — Flat Connection Existence

## Immediate Comment / Docstring

```lean
/-- [II.T50] Flatness check: parallel transport around a closed loop
    (path where sum of directions = 0 mod M_k) returns to start. -/
```

## Source Excerpt

```lean
def flatness_check_loop (conn : TauConnection) (k : Nat)
    (x : Nat) (loop : List Nat) : Bool :=
  let endpoint := parallel_transport conn k x loop
  endpoint == x
```

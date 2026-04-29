---
{
  "projection_kind": "taulib_declaration",
  "title": "TauConnection",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/tau-connection/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::TauConnection",
  "declaration_slug": "tau-connection",
  "kind": "structure",
  "name": "TauConnection",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 54,
  "source_line_end": 55,
  "registry_ids": [
    "II.D78"
  ],
  "related_registry_items": [
    {
      "id": "II.D78",
      "title": "τ-Connection",
      "url": "/registry/object/II.D78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L54-L55",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L54-L55",
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

- Module: [TauLib.BookII.Closure.Connection](/verify/taulib/docs/book-ii-closure-connection/)
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L54-L55)
- Source range: L54-L55
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D78` — τ-Connection

## Immediate Comment / Docstring

```lean
/-- [II.D78] A τ-connection at stage k: a transport function
    Γ(x, v) that moves from x in direction v within Z/M_k Z. -/
```

## Source Excerpt

```lean
structure TauConnection where
  transport : Nat → Nat → Nat → Nat  -- transport(k, x, v) = result
```

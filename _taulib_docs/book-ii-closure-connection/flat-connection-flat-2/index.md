---
{
  "projection_kind": "taulib_declaration",
  "title": "flat_connection_flat_2",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/flat-connection-flat-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::flat_connection_flat_2",
  "declaration_slug": "flat-connection-flat-2",
  "kind": "theorem",
  "name": "flat_connection_flat_2",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 189,
  "source_line_end": 190,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L189-L190",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L189-L190",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L189-L190)
- Source range: L189-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T50` — Flat Connection Existence

## Immediate Comment / Docstring

```lean
/-- [II.T50] Flat connection is flat at stages 1-2. -/
```

## Source Excerpt

```lean
theorem flat_connection_flat_2 :
    flat_connection_check 2 = true := by native_decide
```

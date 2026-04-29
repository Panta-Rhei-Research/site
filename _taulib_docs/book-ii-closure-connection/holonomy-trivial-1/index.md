---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_trivial_1",
  "permalink": "/verify/taulib/docs/book-ii-closure-connection/holonomy-trivial-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::holonomy_trivial_1",
  "declaration_slug": "holonomy-trivial-1",
  "kind": "theorem",
  "name": "holonomy_trivial_1",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/verify/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 193,
  "source_line_end": 194,
  "registry_ids": [
    "II.P16"
  ],
  "related_registry_items": [
    {
      "id": "II.P16",
      "title": "Holonomy Triviality",
      "url": "/registry/object/II.P16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L193-L194",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L193-L194",
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
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L193-L194)
- Source range: L193-L194
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P16` — Holonomy Triviality

## Immediate Comment / Docstring

```lean
/-- [II.P16] Holonomy is trivial at stage 1. -/
```

## Source Excerpt

```lean
theorem holonomy_trivial_1 :
    holonomy_trivial_check 1 = true := by native_decide
```

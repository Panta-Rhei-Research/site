---
{
  "projection_kind": "taulib_declaration",
  "title": "flat_connection",
  "permalink": "/corpus/taulib/docs/book-ii-closure-connection/flat-connection/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.Connection`.",
  "declaration_id": "TauLib.BookII.Closure.Connection::flat_connection",
  "declaration_slug": "flat-connection",
  "kind": "def",
  "name": "flat_connection",
  "module_name": "TauLib.BookII.Closure.Connection",
  "module_url": "/corpus/taulib/docs/book-ii-closure-connection/",
  "source_line_start": 58,
  "source_line_end": 59,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L58-L59",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.Connection",
        "url": "/corpus/taulib/docs/book-ii-closure-connection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L58-L59",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookII.Closure.Connection](/corpus/taulib/docs/book-ii-closure-connection/)
- Source path: [`TauLib/BookII/Closure/Connection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/Connection.lean#L58-L59)
- Source range: L58-L59
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `II.D78` — τ-Connection

## Immediate Comment / Docstring

```lean
/-- [II.D78] The canonical flat connection: additive transport. -/
```

## Source Excerpt

```lean
def flat_connection : TauConnection :=
  { transport := fun k x v => (x + v) % primorial k }
```

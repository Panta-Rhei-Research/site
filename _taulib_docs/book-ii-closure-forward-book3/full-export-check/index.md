---
{
  "projection_kind": "taulib_declaration",
  "title": "full_export_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-forward-book3/full-export-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.ForwardBook3`.",
  "declaration_id": "TauLib.BookII.Closure.ForwardBook3::full_export_check",
  "declaration_slug": "full-export-check",
  "kind": "def",
  "name": "full_export_check",
  "module_name": "TauLib.BookII.Closure.ForwardBook3",
  "module_url": "/verify/taulib/docs/book-ii-closure-forward-book3/",
  "source_line_start": 83,
  "source_line_end": 84,
  "registry_ids": [
    "II.D66"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L83-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.ForwardBook3",
        "url": "/verify/taulib/docs/book-ii-closure-forward-book3/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L83-L84",
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

- Module: [TauLib.BookII.Closure.ForwardBook3](/verify/taulib/docs/book-ii-closure-forward-book3/)
- Source path: [`TauLib/BookII/Closure/ForwardBook3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L83-L84)
- Source range: L83-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D66] Full export check: compute and verify the entire package. -/
```

## Source Excerpt

```lean
def full_export_check (db bound k_max : TauIdx) : Bool :=
  export_package_complete (compute_e1_export db bound k_max)
```

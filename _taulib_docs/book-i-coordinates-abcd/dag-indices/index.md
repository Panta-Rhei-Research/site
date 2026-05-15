---
{
  "projection_kind": "taulib_declaration",
  "title": "dag_indices",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-abcd/dag-indices/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ABCD`.",
  "declaration_id": "TauLib.BookI.Coordinates.ABCD::dag_indices",
  "declaration_slug": "dag-indices",
  "kind": "def",
  "name": "dag_indices",
  "module_name": "TauLib.BookI.Coordinates.ABCD",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-abcd/",
  "source_line_start": 80,
  "source_line_end": 80,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L80-L80",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ABCD",
        "url": "/corpus/taulib/docs/book-i-coordinates-abcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L80-L80",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Coordinates.ABCD](/corpus/taulib/docs/book-i-coordinates-abcd/)
- Source path: [`TauLib/BookI/Coordinates/ABCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L80-L80)
- Source range: L80-L80
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
def dag_indices (x : TauIdx) : List TauIdx := dag_indices_go [x] [] x
```

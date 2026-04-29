---
{
  "projection_kind": "taulib_declaration",
  "title": "coord_D",
  "permalink": "/verify/taulib/docs/book-i-coordinates-abcd/coord-d/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ABCD`.",
  "declaration_id": "TauLib.BookI.Coordinates.ABCD::coord_D",
  "declaration_slug": "coord-d",
  "kind": "def",
  "name": "coord_D",
  "module_name": "TauLib.BookI.Coordinates.ABCD",
  "module_url": "/verify/taulib/docs/book-i-coordinates-abcd/",
  "source_line_start": 53,
  "source_line_end": 53,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L53-L53",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ABCD",
        "url": "/verify/taulib/docs/book-i-coordinates-abcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L53-L53",
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

- Module: [TauLib.BookI.Coordinates.ABCD](/verify/taulib/docs/book-i-coordinates-abcd/)
- Source path: [`TauLib/BookI/Coordinates/ABCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L53-L53)
- Source range: L53-L53
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- D-coordinate (remainder). -/
```

## Source Excerpt

```lean
def coord_D (x : TauIdx) : TauIdx := (abcd_chart x).2.2.2
```

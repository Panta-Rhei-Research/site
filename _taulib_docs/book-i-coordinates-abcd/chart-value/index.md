---
{
  "projection_kind": "taulib_declaration",
  "title": "chart_value",
  "permalink": "/verify/taulib/docs/book-i-coordinates-abcd/chart-value/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ABCD`.",
  "declaration_id": "TauLib.BookI.Coordinates.ABCD::chart_value",
  "declaration_slug": "chart-value",
  "kind": "def",
  "name": "chart_value",
  "module_name": "TauLib.BookI.Coordinates.ABCD",
  "module_url": "/verify/taulib/docs/book-i-coordinates-abcd/",
  "source_line_start": 56,
  "source_line_end": 57,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L56-L57",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L56-L57",
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
- Source path: [`TauLib/BookI/Coordinates/ABCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L56-L57)
- Source range: L56-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Reconstruction: T(A,B,C) * D. -/
```

## Source Excerpt

```lean
def chart_value (x : TauIdx) : TauIdx :=
  tower_atom (coord_A x) (coord_B x) (coord_C x) * coord_D x
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "SCVDimension.le",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/le/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::SCVDimension.le",
  "declaration_slug": "le",
  "kind": "def",
  "name": "SCVDimension.le",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 89,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L89-L90",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L89-L90",
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L89-L90)
- Source range: L89-L90
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The dimension regimes form a total order. -/
```

## Source Excerpt

```lean
def SCVDimension.le (d1 d2 : SCVDimension) : Bool :=
  d1.toNat ≤ d2.toNat
```

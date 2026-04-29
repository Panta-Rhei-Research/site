---
{
  "projection_kind": "taulib_declaration",
  "title": "abcd_coords",
  "permalink": "/verify/taulib/docs/book-ii-topology-dimension-four/abcd-coords/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.DimensionFour`.",
  "declaration_id": "TauLib.BookII.Topology.DimensionFour::abcd_coords",
  "declaration_slug": "abcd-coords",
  "kind": "def",
  "name": "abcd_coords",
  "module_name": "TauLib.BookII.Topology.DimensionFour",
  "module_url": "/verify/taulib/docs/book-ii-topology-dimension-four/",
  "source_line_start": 38,
  "source_line_end": 40,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L38-L40",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.DimensionFour",
        "url": "/verify/taulib/docs/book-ii-topology-dimension-four/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L38-L40",
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

- Module: [TauLib.BookII.Topology.DimensionFour](/verify/taulib/docs/book-ii-topology-dimension-four/)
- Source path: [`TauLib/BookII/Topology/DimensionFour.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L38-L40)
- Source range: L38-L40
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- ABCD coordinates of a τ-index. -/
```

## Source Excerpt

```lean
def abcd_coords (x : TauIdx) : TauIdx × TauIdx × TauIdx × TauIdx :=
  let p := from_tau_idx x
  (p.a, p.b, p.c, p.d)
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "dim_four_check",
  "permalink": "/corpus/taulib/docs/book-ii-topology-dimension-four/dim-four-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.DimensionFour`.",
  "declaration_id": "TauLib.BookII.Topology.DimensionFour::dim_four_check",
  "declaration_slug": "dim-four-check",
  "kind": "def",
  "name": "dim_four_check",
  "module_name": "TauLib.BookII.Topology.DimensionFour",
  "module_url": "/corpus/taulib/docs/book-ii-topology-dimension-four/",
  "source_line_start": 87,
  "source_line_end": 88,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L87-L88",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.DimensionFour",
        "url": "/corpus/taulib/docs/book-ii-topology-dimension-four/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L87-L88",
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

- Module: [TauLib.BookII.Topology.DimensionFour](/corpus/taulib/docs/book-ii-topology-dimension-four/)
- Source path: [`TauLib/BookII/Topology/DimensionFour.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L87-L88)
- Source range: L87-L88
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full dimension 4 verification. -/
```

## Source Excerpt

```lean
def dim_four_check (bound : TauIdx) : Bool :=
  four_suffice_check bound && three_insufficient_check
```

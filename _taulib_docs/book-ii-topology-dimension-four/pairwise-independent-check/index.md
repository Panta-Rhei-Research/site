---
{
  "projection_kind": "taulib_declaration",
  "title": "pairwise_independent_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-dimension-four/pairwise-independent-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.DimensionFour`.",
  "declaration_id": "TauLib.BookII.Topology.DimensionFour::pairwise_independent_check",
  "declaration_slug": "pairwise-independent-check",
  "kind": "def",
  "name": "pairwise_independent_check",
  "module_name": "TauLib.BookII.Topology.DimensionFour",
  "module_url": "/verify/taulib/docs/book-ii-topology-dimension-four/",
  "source_line_start": 117,
  "source_line_end": 127,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L117-L127",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L117-L127",
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
- Source path: [`TauLib/BookII/Topology/DimensionFour.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L117-L127)
- Source range: L117-L127
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pairwise independence of coordinates: for each pair,
    exhibit elements varying one while holding the other fixed. -/
```

## Source Excerpt

```lean
def pairwise_independent_check : Bool :=
  -- A varies, B fixed: 2=(2,1,1,1) vs 3=(3,1,1,1) → A varies, B=1 both
  let p2 := from_tau_idx 2
  let p3 := from_tau_idx 3
  (p2.a != p3.a && p2.b == p3.b) &&
  -- B varies, A fixed: 8=(2,3,1,1) vs 2=(2,1,1,1) → B varies, A=2 both
  let p8 := from_tau_idx 8
  (p8.a == p2.a && p8.b != p2.b) &&
  -- C varies, A fixed: 8=(2,3,1,1) vs 64=(2,3,2,1) → C varies, A=2 both
  let p64 := from_tau_idx 64
  (p8.a == p64.a && p8.c != p64.c)
```

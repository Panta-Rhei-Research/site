---
{
  "projection_kind": "taulib_declaration",
  "title": "three_insufficient_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-dimension-four/three-insufficient-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.DimensionFour`.",
  "declaration_id": "TauLib.BookII.Topology.DimensionFour::three_insufficient_check",
  "declaration_slug": "three-insufficient-check",
  "kind": "def",
  "name": "three_insufficient_check",
  "module_name": "TauLib.BookII.Topology.DimensionFour",
  "module_url": "/verify/taulib/docs/book-ii-topology-dimension-four/",
  "source_line_start": 71,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L71-L84",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L71-L84",
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
- Source path: [`TauLib/BookII/Topology/DimensionFour.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L71-L84)
- Source range: L71-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T11, lower bound] Three coordinates don't suffice:
    exhibit pairs that agree on 3 coords but differ on 4th.

    Missing D: 12=(3,1,1,4) and 3=(3,1,1,1) share A,B,C but differ in D.
    Missing A: 2=(2,1,1,1) and 3=(3,1,1,1) share B,C,D but differ in A.
    Missing B: 8=(2,3,1,1) and 2=(2,1,1,1) share A,C,D but differ in B.
    Missing C: 64=(2,3,2,1) and 8=(2,3,1,1) share A,B,D but differ in C. -/
```

## Source Excerpt

```lean
def three_insufficient_check : Bool :=
  -- Missing D: 12=(3,1,1,4) vs 3=(3,1,1,1)
  let p12 := from_tau_idx 12
  let p3 := from_tau_idx 3
  (p12.a == p3.a && p12.b == p3.b && p12.c == p3.c && p12.d != p3.d) &&
  -- Missing A: 2=(2,1,1,1) vs 3=(3,1,1,1)
  let p2 := from_tau_idx 2
  (p2.b == p3.b && p2.c == p3.c && p2.d == p3.d && p2.a != p3.a) &&
  -- Missing B: 8=(2,3,1,1) vs 2=(2,1,1,1)
  let p8 := from_tau_idx 8
  (p8.a == p2.a && p8.c == p2.c && p8.d == p2.d && p8.b != p2.b) &&
  -- Missing C: 64=(2,3,2,1) vs 8=(2,3,1,1)
  let p64 := from_tau_idx 64
  (p64.a == p8.a && p64.b == p8.b && p64.d == p8.d && p64.c != p8.c)
```

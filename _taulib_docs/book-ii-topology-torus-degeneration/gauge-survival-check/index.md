---
{
  "projection_kind": "taulib_declaration",
  "title": "gauge_survival_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-torus-degeneration/gauge-survival-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.TorusDegeneration`.",
  "declaration_id": "TauLib.BookII.Topology.TorusDegeneration::gauge_survival_check",
  "declaration_slug": "gauge-survival-check",
  "kind": "def",
  "name": "gauge_survival_check",
  "module_name": "TauLib.BookII.Topology.TorusDegeneration",
  "module_url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/",
  "source_line_start": 89,
  "source_line_end": 98,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L89-L98",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.TorusDegeneration",
        "url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L89-L98",
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

- Module: [TauLib.BookII.Topology.TorusDegeneration](/verify/taulib/docs/book-ii-topology-torus-degeneration/)
- Source path: [`TauLib/BookII/Topology/TorusDegeneration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L89-L98)
- Source range: L89-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Gauge survival: both B and C channels act independently.
    B-rotation shifts plus lobe parameter; C-rotation shifts minus lobe.
    Evidence: varying B alone changes lobe parameter while C is fixed. -/
```

## Source Excerpt

```lean
def gauge_survival_check : Bool :=
  -- B varies: 2=(2,1,1,1) vs 8=(2,3,1,1)
  -- Same A,C,D but different B → different lobe position
  let p2 := from_tau_idx 2
  let p8 := from_tau_idx 8
  (p2.b != p8.b && p2.a == p8.a && p2.c == p8.c) &&
  -- C varies: 8=(2,3,1,1) vs 64=(2,3,2,1)
  -- Same A,B,D but different C → different lobe position
  let p64 := from_tau_idx 64
  (p8.c != p64.c && p8.a == p64.a && p8.b == p64.b)
```

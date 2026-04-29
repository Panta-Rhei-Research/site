---
{
  "projection_kind": "taulib_declaration",
  "title": "pinch_fiber",
  "permalink": "/verify/taulib/docs/book-ii-topology-torus-degeneration/pinch-fiber/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.TorusDegeneration`.",
  "declaration_id": "TauLib.BookII.Topology.TorusDegeneration::pinch_fiber",
  "declaration_slug": "pinch-fiber",
  "kind": "def",
  "name": "pinch_fiber",
  "module_name": "TauLib.BookII.Topology.TorusDegeneration",
  "module_url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/",
  "source_line_start": 47,
  "source_line_end": 50,
  "registry_ids": [
    "II.D18"
  ],
  "related_registry_items": [
    {
      "id": "II.D18",
      "title": "Pinch Map",
      "url": "/registry/object/II.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L47-L50",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L47-L50",
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
- Source path: [`TauLib/BookII/Topology/TorusDegeneration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L47-L50)
- Source range: L47-L50
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D18` — Pinch Map

## Immediate Comment / Docstring

```lean
/-- [II.D18] The pinch map on fiber coordinates (B, C):
    (B, C) ↦ wedge if B = C, else lobe by dominance. -/
```

## Source Excerpt

```lean
def pinch_fiber (b c : TauIdx) : PinchImage :=
  if b == c then .wedge
  else if b > c then .plus_lobe (b - c : Int)
  else .minus_lobe (c - b : Int)
```

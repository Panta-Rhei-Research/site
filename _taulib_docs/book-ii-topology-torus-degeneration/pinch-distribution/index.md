---
{
  "projection_kind": "taulib_declaration",
  "title": "pinch_distribution",
  "permalink": "/verify/taulib/docs/book-ii-topology-torus-degeneration/pinch-distribution/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.TorusDegeneration`.",
  "declaration_id": "TauLib.BookII.Topology.TorusDegeneration::pinch_distribution",
  "declaration_slug": "pinch-distribution",
  "kind": "def",
  "name": "pinch_distribution",
  "module_name": "TauLib.BookII.Topology.TorusDegeneration",
  "module_url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/",
  "source_line_start": 135,
  "source_line_end": 145,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L135-L145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L135-L145",
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
- Source path: [`TauLib/BookII/Topology/TorusDegeneration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L135-L145)
- Source range: L135-L145
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Count pinch image distribution in range [2, bound]. -/
```

## Source Excerpt

```lean
def pinch_distribution (bound : TauIdx) : Nat × Nat × Nat :=
  go 2 (bound + 1) 0 0 0
where
  go (x fuel plus minus wedge : Nat) : Nat × Nat × Nat :=
    if fuel = 0 then (plus, minus, wedge)
    else if x > bound then (plus, minus, wedge)
    else match pinch_point x with
      | .plus_lobe _ => go (x + 1) (fuel - 1) (plus + 1) minus wedge
      | .minus_lobe _ => go (x + 1) (fuel - 1) plus (minus + 1) wedge
      | .wedge => go (x + 1) (fuel - 1) plus minus (wedge + 1)
  termination_by fuel
```

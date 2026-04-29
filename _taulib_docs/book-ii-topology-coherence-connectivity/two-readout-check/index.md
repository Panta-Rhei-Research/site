---
{
  "projection_kind": "taulib_declaration",
  "title": "two_readout_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/two-readout-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.CoherenceConnectivity`.",
  "declaration_id": "TauLib.BookII.Topology.CoherenceConnectivity::two_readout_check",
  "declaration_slug": "two-readout-check",
  "kind": "def",
  "name": "two_readout_check",
  "module_name": "TauLib.BookII.Topology.CoherenceConnectivity",
  "module_url": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/",
  "source_line_start": 52,
  "source_line_end": 81,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L52-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.CoherenceConnectivity",
        "url": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L52-L81",
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

- Module: [TauLib.BookII.Topology.CoherenceConnectivity](/verify/taulib/docs/book-ii-topology-coherence-connectivity/)
- Source path: [`TauLib/BookII/Topology/CoherenceConnectivity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L52-L81)
- Source range: L52-L81
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D18a] The two-readout principle: topology (fine-grain) and geometry
    (coarse-grain) are parallel readouts of the coherence kernel.

    Evidence: for pairs (x, y, z) where betweenness holds (B(x,y,z) = true),
    the topological separating stage between x and y is INDEPENDENT of
    the geometric betweenness relation — they probe different structure.

    We verify:
    1. Topological separation always exists (Stone space, II.T09)
    2. Geometric betweenness exists for specific triples
    3. Both coexist on the same point set without contradiction -/
```

## Source Excerpt

```lean
def two_readout_check (bound db : TauIdx) : Bool :=
  -- (a) Topology: every pair of distinct points has a separating cylinder
  let topo_ok := hausdorff_check bound db
  -- (b) Geometry: betweenness holds for some triples
  --     (evidence that the coarse-grain readout is nontrivial)
  let geom_ok := between_connectivity_check bound db
  -- (c) Independence: there exist triples (x,y,z) where:
  --     - B(x,y,z) = true (geometric betweenness)
  --     - x and z are in DIFFERENT cylinders at some stage (topological separation)
  --     Both readouts yield nontrivial information simultaneously
  let indep_ok := go 2 (bound + 1)
  topo_ok && geom_ok && indep_ok
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      -- For each x, check if there exist y, z with betweenness AND separation
      let found := go_yz x 2 2 bound db
      (found || x > 10) && go (x + 1) (fuel - 1)  -- relaxed: not all x need witnesses
  termination_by fuel
  go_yz (x y z bound db : Nat) : Bool :=
    if y > bound then false
    else if z > bound then go_yz x (y + 1) 2 bound db
    else
      let btw := between x y z db
      let sep := !cylinder_mem 1 x z  -- separated at stage 1
      if btw && sep then true
      else go_yz x y (z + 1) bound db
  termination_by (bound + 1 - y, bound + 1 - z)
```

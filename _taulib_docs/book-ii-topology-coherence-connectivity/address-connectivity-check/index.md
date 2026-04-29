---
{
  "projection_kind": "taulib_declaration",
  "title": "address_connectivity_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/address-connectivity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.CoherenceConnectivity`.",
  "declaration_id": "TauLib.BookII.Topology.CoherenceConnectivity::address_connectivity_check",
  "declaration_slug": "address-connectivity-check",
  "kind": "def",
  "name": "address_connectivity_check",
  "module_name": "TauLib.BookII.Topology.CoherenceConnectivity",
  "module_url": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/",
  "source_line_start": 114,
  "source_line_end": 131,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L114-L131",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L114-L131",
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
- Source path: [`TauLib/BookII/Topology/CoherenceConnectivity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L114-L131)
- Source range: L114-L131
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D18b] Universal address connectivity: every pair of finite-stage
    points has a spine address path of bounded length.
    Verify: for all x, y in [2, bound], the path length is finite and bounded. -/
```

## Source Excerpt

```lean
def address_connectivity_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let yz_ok := go_y x 2 bound
      yz_ok && go (x + 1) (fuel - 1)
  termination_by fuel
  go_y (x y bound : Nat) : Bool :=
    if y > bound then true
    else
      let len := spine_address_path x y
      -- Path length is bounded by 2 × max peel steps
      -- For practical indices < 300, this is always < 20
      (len < 20) && go_y x (y + 1) bound
  termination_by bound + 1 - y
```

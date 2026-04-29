---
{
  "projection_kind": "taulib_declaration",
  "title": "spine_address_length",
  "permalink": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/spine-address-length/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.CoherenceConnectivity`.",
  "declaration_id": "TauLib.BookII.Topology.CoherenceConnectivity::spine_address_length",
  "declaration_slug": "spine-address-length",
  "kind": "def",
  "name": "spine_address_length",
  "module_name": "TauLib.BookII.Topology.CoherenceConnectivity",
  "module_url": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/",
  "source_line_start": 93,
  "source_line_end": 105,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L93-L105",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L93-L105",
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
- Source path: [`TauLib/BookII/Topology/CoherenceConnectivity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L93-L105)
- Source range: L93-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D18b] Spine address path: the canonical route from X to Y through α₁ = 2.

    Descent: X → greedy peel → (A,B,C,D) → extract D → continue until base
    Ascent: α₁ → build up Y's ABCD address

    The spine address length ℓ(X,Y) counts total peel steps. -/
```

## Source Excerpt

```lean
def spine_address_length (x : TauIdx) : TauIdx :=
  if x ≤ 2 then 0
  else
    go x 100  -- bounded iteration (100 steps is ample for any practical τ-index)
where
  go (n fuel : Nat) : Nat :=
    if fuel = 0 then 0
    else if n ≤ 2 then 0
    else
      let (a, _b, _c, d) := greedy_peel n
      if a ≤ 1 then 0
      else 1 + go d (fuel - 1)
  termination_by fuel
```

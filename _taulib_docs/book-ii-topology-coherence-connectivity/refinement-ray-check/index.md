---
{
  "projection_kind": "taulib_declaration",
  "title": "refinement_ray_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/refinement-ray-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.CoherenceConnectivity`.",
  "declaration_id": "TauLib.BookII.Topology.CoherenceConnectivity::refinement_ray_check",
  "declaration_slug": "refinement-ray-check",
  "kind": "def",
  "name": "refinement_ray_check",
  "module_name": "TauLib.BookII.Topology.CoherenceConnectivity",
  "module_url": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/",
  "source_line_start": 151,
  "source_line_end": 187,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L151-L187",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L151-L187",
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
- Source path: [`TauLib/BookII/Topology/CoherenceConnectivity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L151-L187)
- Source range: L151-L187
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.R06a] Refinement rays: verify the four orbit rays are
    one-sided (ℕ-indexed), independent, and canonical.

    (i) One-sided: each ray starts at a fixed base element
    (ii) Independent: ABCD coordinates of successive elements differ in one coordinate
    (iii) Discrete: no intermediate points between successive orbit elements -/
```

## Source Excerpt

```lean
def refinement_ray_check : Bool :=
  -- (i) One-sided: the 4 generators produce distinct base elements
  let alpha_base := from_tau_idx 2   -- α₁ = 2
  let pi_base := from_tau_idx 3      -- π₁ = 3
  let gamma_base := from_tau_idx 5   -- γ₁ = 5 (first prime in γ-orbit, not same as coord)
  let eta_base := from_tau_idx 7     -- η₁ = 7

  -- All four base elements have different ABCD charts
  let bases_distinct :=
    alpha_base != pi_base &&
    alpha_base != gamma_base &&
    alpha_base != eta_base &&
    pi_base != gamma_base &&
    pi_base != eta_base &&
    gamma_base != eta_base

  -- (ii) Each ρ-step (multiplication by next prime) changes coordinates
  -- α-ray: 2, 4, 8, ... (powers of 2 → D changes)
  let ray_alpha_step :=
    let p2 := from_tau_idx 2
    let p4 := from_tau_idx 4
    -- 2→4 is a genuine step: coordinates change
    p2 != p4

  -- π-ray: 3, 9, 27, ... (powers of 3)
  let ray_pi_step :=
    let p3 := from_tau_idx 3
    let p9 := from_tau_idx 9
    p3 != p9

  -- (iii) Discrete: for α-ray, no element between 2 and 4 in the orbit
  -- (In the primorial refinement, step sizes are determined by primes)
  let discrete_check :=
    -- 3 is not in the α-orbit (it's in the π-orbit)
    from_tau_idx 3 != from_tau_idx 2

  bases_distinct && ray_alpha_step && ray_pi_step && discrete_check
```

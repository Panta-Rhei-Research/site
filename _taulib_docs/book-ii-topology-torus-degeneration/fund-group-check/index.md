---
{
  "projection_kind": "taulib_declaration",
  "title": "fund_group_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-torus-degeneration/fund-group-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.TorusDegeneration`.",
  "declaration_id": "TauLib.BookII.Topology.TorusDegeneration::fund_group_check",
  "declaration_slug": "fund-group-check",
  "kind": "def",
  "name": "fund_group_check",
  "module_name": "TauLib.BookII.Topology.TorusDegeneration",
  "module_url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/",
  "source_line_start": 115,
  "source_line_end": 128,
  "registry_ids": [
    "II.T14"
  ],
  "related_registry_items": [
    {
      "id": "II.T14",
      "title": "Fundamental Group Degeneration",
      "url": "/registry/object/II.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L115-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L115-L128",
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
- Source path: [`TauLib/BookII/Topology/TorusDegeneration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L115-L128)
- Source range: L115-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T14` — Fundamental Group Degeneration

## Immediate Comment / Docstring

```lean
/-- [II.T14] Fundamental group degeneration: ℤ² → F₂.

    At finite depth: π₁(T²) = ℤ² (commutative).
    At boundary: π₁(ℒ) = F₂ (free, non-commutative).

    Evidence: B and C loops commute at finite depth
    but become non-commuting free generators at boundary.

    The F₂ property is witnessed by the bipolar orthogonality:
    e₊ and e₋ project onto independent lobes, and the sector
    product e₊ · e₋ = 0 (they cannot be composed into one loop). -/
```

## Source Excerpt

```lean
def fund_group_check : Bool :=
  -- Commutative at finite depth: B and C are independent ℕ coordinates
  let p := from_tau_idx 64  -- (2,3,2,1)
  -- B and C can be varied independently (verified above)
  -- At boundary: orthogonality forces non-commutativity
  -- e₊ · e₋ = 0 means the two lobe loops cannot collapse to one
  SectorPair.mul e_plus_sector e_minus_sector == ⟨0, 0⟩ &&
  -- Two independent generators (rank 2 free group)
  e_plus_sector != e_minus_sector &&
  -- Both are nontrivial
  e_plus_sector != ⟨0, 0⟩ &&
  e_minus_sector != ⟨0, 0⟩ &&
  -- Independence check via admissible point
  p.b != p.c  -- B ≠ C at this point → fibers genuinely different
```

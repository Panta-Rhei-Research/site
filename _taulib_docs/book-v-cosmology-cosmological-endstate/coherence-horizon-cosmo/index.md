---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceHorizonCosmo",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/coherence-horizon-cosmo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CosmologicalEndstate`.",
  "declaration_id": "TauLib.BookV.Cosmology.CosmologicalEndstate::CoherenceHorizonCosmo",
  "declaration_slug": "coherence-horizon-cosmo",
  "kind": "structure",
  "name": "CoherenceHorizonCosmo",
  "module_name": "TauLib.BookV.Cosmology.CosmologicalEndstate",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/",
  "source_line_start": 125,
  "source_line_end": 136,
  "registry_ids": [
    "V.D182"
  ],
  "related_registry_items": [
    {
      "id": "V.D182",
      "title": "Coherence horizon",
      "url": "/registry/object/V.D182/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L125-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CosmologicalEndstate",
        "url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L125-L136",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Cosmology.CosmologicalEndstate](/verify/taulib/docs/book-v-cosmology-cosmological-endstate/)
- Source path: [`TauLib/BookV/Cosmology/CosmologicalEndstate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L125-L136)
- Source range: L125-L136
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D182` — Coherence horizon

## Immediate Comment / Docstring

```lean
/-- [V.D182] Coherence horizon H_coh(n): the diameter of the largest
    connected component of τ³ minus the union of BH excisions.

    As BHs grow and merge, H_coh(n) shrinks. This resembles the
    Big Crunch but is structurally different: no recollapse to
    infinite density, just a shrinking inter-BH space. -/
```

## Source Excerpt

```lean
structure CoherenceHorizonCosmo where
  /-- Horizon diameter (scaled). -/
  diameter : Nat
  /-- Diameter positive. -/
  diameter_pos : diameter > 0
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  /-- Diameter decreases with depth (in BH-dominated regime). -/
  shrinking : Bool := true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "EternalCirculation",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/eternal-circulation/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CosmologicalEndstate`.",
  "declaration_id": "TauLib.BookV.Cosmology.CosmologicalEndstate::EternalCirculation",
  "declaration_slug": "eternal-circulation",
  "kind": "structure",
  "name": "EternalCirculation",
  "module_name": "TauLib.BookV.Cosmology.CosmologicalEndstate",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/",
  "source_line_start": 191,
  "source_line_end": 200,
  "registry_ids": [
    "V.T119"
  ],
  "related_registry_items": [
    {
      "id": "V.T119",
      "title": "Eternal Circulation Theorem",
      "url": "/registry/object/V.T119/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L191-L200",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L191-L200",
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
- Source path: [`TauLib/BookV/Cosmology/CosmologicalEndstate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L191-L200)
- Source range: L191-L200
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T119` — Eternal Circulation Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T119] Eternal circulation theorem: the cosmological endstate
    is not heat death but eternal circulation.

    Boundary characters χ₊, χ₋ circulate continuously on the
    lemniscate L = S¹ ∨ S¹. The circulation never stops because:
    1. The profinite tower has infinite depth
    2. The total time t_∞ is finite (Σ p_k⁻¹ converges)
    3. The absorbing pattern is ρ-invariant, not static

    Heat death requires infinite time and maximal entropy.
    The τ endstate has finite time and non-maximal entropy
    (the BH excision entropy is below the maximum). -/
```

## Source Excerpt

```lean
structure EternalCirculation where
  /-- Infinite depth (profinite tower). -/
  infinite_depth : Bool := true
  /-- Finite total time. -/
  finite_time : Bool := true
  /-- Characters circulate (not static). -/
  characters_circulate : Bool := true
  /-- Not heat death. -/
  not_heat_death : Bool := true
  deriving Repr
```

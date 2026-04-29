---
{
  "projection_kind": "taulib_declaration",
  "title": "BHDominatedEpoch",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/bhdominated-epoch/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CosmologicalEndstate`.",
  "declaration_id": "TauLib.BookV.Cosmology.CosmologicalEndstate::BHDominatedEpoch",
  "declaration_slug": "bhdominated-epoch",
  "kind": "structure",
  "name": "BHDominatedEpoch",
  "module_name": "TauLib.BookV.Cosmology.CosmologicalEndstate",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/",
  "source_line_start": 97,
  "source_line_end": 106,
  "registry_ids": [
    "V.D181"
  ],
  "related_registry_items": [
    {
      "id": "V.D181",
      "title": "BH-dominated epoch",
      "url": "/registry/object/V.D181/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L97-L106",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L97-L106",
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
- Source path: [`TauLib/BookV/Cosmology/CosmologicalEndstate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L97-L106)
- Source range: L97-L106
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D181` — BH-dominated epoch

## Immediate Comment / Docstring

```lean
/-- [V.D181] BH-dominated epoch: begins at refinement depth n_BH
    where the BH contribution to S_def exceeds all other contributions.

    Beyond n_BH, the universe's defect budget is almost entirely
    locked in BH excisions. -/
```

## Source Excerpt

```lean
structure BHDominatedEpoch where
  /-- Onset depth. -/
  onset_depth : Nat
  /-- Onset positive. -/
  onset_pos : onset_depth > 0
  /-- BH fraction of total defect entropy (× 100, i.e. percent). -/
  bh_fraction_pct : Nat
  /-- BH fraction exceeds 50%. -/
  bh_dominant : bh_fraction_pct > 50
  deriving Repr
```

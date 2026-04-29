---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L213",
  "permalink": "/verify/taulib/docs/tour-central-theorem/eval-l213/",
  "summary_short": "`eval` declaration in `TauLib.Tour.CentralTheorem`.",
  "declaration_id": "TauLib.Tour.CentralTheorem::#eval:213",
  "declaration_slug": "eval-l213",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.CentralTheorem",
  "module_url": "/verify/taulib/docs/tour-central-theorem/",
  "source_line_start": 213,
  "source_line_end": 238,
  "registry_ids": [
    "II.D60",
    "II.T40"
  ],
  "related_registry_items": [
    {
      "id": "II.D60",
      "title": "Spectral Algebra",
      "url": "/registry/object/II.D60/"
    },
    {
      "id": "II.T40",
      "title": "Central Theorem",
      "url": "/registry/object/II.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L213-L238",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.CentralTheorem",
        "url": "/verify/taulib/docs/tour-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L213-L238",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.Tour.CentralTheorem](/verify/taulib/docs/tour-central-theorem/)
- Source path: [`TauLib/Tour/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L213-L238)
- Source range: L213-L238
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `II.D60` — Spectral Algebra
- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
-- spectral_to_hol(id, id, x, k) = hol_to_spectral(id_stage, x, k)

-- THE CENTRAL THEOREM: all four links combined.
```

## Source Excerpt

```lean
#eval central_theorem_check 3 15              -- true

-- ================================================================
-- PART 6: FORMAL PROOFS — MACHINE-CHECKED
-- ================================================================

-- Each component is not just evaluated — it is formally PROVED
-- correct by Lean's kernel via native_decide.

-- Spectral ring structure [II.D60]:
#check spectral_ring_3_15       -- spectral_algebra_stage_ring_check 3 15 = true
#check spectral_tower_3_15      -- spectral_algebra_tower_check 3 15 = true

-- Central Theorem links [II.T40]:
#check central_fwd_3_15         -- forward direction verified
#check central_inv_3_15         -- inverse direction verified
#check central_rt_3_15          -- round-trip verified

-- The combined Central Theorem:
#check central_theorem_3_15     -- central_theorem_check 3 15 = true

-- Structural theorems (proved by simp/ring, not native_decide):
#check spectral_periodic              -- evaluation is P_k-periodic
#check spectral_idempotent_supported  -- every element is idempotent-supported
#check central_forward_coherent       -- forward map is tower-coherent
#check central_inverse_periodic       -- inverse restriction is periodic
```

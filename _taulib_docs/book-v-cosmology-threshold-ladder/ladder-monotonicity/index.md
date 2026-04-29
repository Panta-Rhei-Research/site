---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_monotonicity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/ladder-monotonicity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::ladder_monotonicity",
  "declaration_slug": "ladder-monotonicity",
  "kind": "theorem",
  "name": "ladder_monotonicity",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 146,
  "source_line_end": 152,
  "registry_ids": [
    "V.T107"
  ],
  "related_registry_items": [
    {
      "id": "V.T107",
      "title": "Ladder Monotonicity",
      "url": "/registry/object/V.T107/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L146-L152",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L146-L152",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L146-L152)
- Source range: L146-L152
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T107` — Ladder Monotonicity

## Immediate Comment / Docstring

```lean
/-- [V.T107] Ladder monotonicity: canonical thresholds occur in
    the order n_EW < n_B < n_N < n_nuc < n_H < n_γ. -/
```

## Source Excerpt

```lean
theorem ladder_monotonicity :
    canonical_ladder.ew.depth_index < canonical_ladder.baryogenesis.depth_index ∧
    canonical_ladder.baryogenesis.depth_index < canonical_ladder.neutron.depth_index ∧
    canonical_ladder.neutron.depth_index < canonical_ladder.nucleosynthesis.depth_index ∧
    canonical_ladder.nucleosynthesis.depth_index < canonical_ladder.hydrogen.depth_index ∧
    canonical_ladder.hydrogen.depth_index < canonical_ladder.photon_decoupling.depth_index :=
  canonical_ladder.monotone
```

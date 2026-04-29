---
{
  "projection_kind": "taulib_declaration",
  "title": "DeuteriumPrediction",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::DeuteriumPrediction",
  "declaration_slug": "deuterium-prediction",
  "kind": "structure",
  "name": "DeuteriumPrediction",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 307,
  "source_line_end": 316,
  "registry_ids": [
    "V.T241"
  ],
  "related_registry_items": [
    {
      "id": "V.T241",
      "title": "D/H from τ-native η_B",
      "url": "/registry/object/V.T241/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L307-L316",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L307-L316",
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

- Module: [TauLib.BookV.Cosmology.BBNNuclearNetwork](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/)
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L307-L316)
- Source range: L307-L316
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T241` — D/H from τ-native η_B

## Immediate Comment / Docstring

```lean
/-- [V.T241] Deuterium prediction from τ-native η_B.
    D/H(τ) ≈ 2.60 × 10⁻⁵. Observed: 2.527 ± 0.030 × 10⁻⁵.
    Using ×10⁻⁷ units: τ-BBN = 260, obs = 253 ± 3. -/
```

## Source Excerpt

```lean
structure DeuteriumPrediction where
  /-- τ-BBN D/H (×10⁻⁷). -/
  dh_x1e7 : Nat := 260
  /-- Observed D/H midpoint (×10⁻⁷). -/
  obs_x1e7 : Nat := 253
  /-- Observed uncertainty (×10⁻⁷). -/
  obs_unc_x1e7 : Nat := 3
  /-- Deviation in σ (×10): +23 means +2.3σ. -/
  deviation_sigma_x10 : Nat := 23
  deriving Repr
```

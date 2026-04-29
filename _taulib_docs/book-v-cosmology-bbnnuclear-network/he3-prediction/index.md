---
{
  "projection_kind": "taulib_declaration",
  "title": "He3Prediction",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/he3-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::He3Prediction",
  "declaration_slug": "he3-prediction",
  "kind": "structure",
  "name": "He3Prediction",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 337,
  "source_line_end": 344,
  "registry_ids": [
    "V.T247"
  ],
  "related_registry_items": [
    {
      "id": "V.T247",
      "title": "He-3/H from τ-native η_B",
      "url": "/registry/object/V.T247/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L337-L344",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L337-L344",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L337-L344)
- Source range: L337-L344
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T247` — He-3/H from τ-native η_B

## Immediate Comment / Docstring

```lean
/-- [V.T247] He-3 prediction from τ-native η_B.
    ³He/H(τ) ≈ 1.01 × 10⁻⁵. Observed: (1.1 ± 0.2) × 10⁻⁵.
    Using ×10⁻⁷ units: τ-BBN = 101, obs = 110 ± 20. -/
```

## Source Excerpt

```lean
structure He3Prediction where
  /-- τ-BBN ³He/H (×10⁻⁷). -/
  he3_x1e7 : Nat := 101
  /-- Observed ³He/H midpoint (×10⁻⁷). -/
  obs_x1e7 : Nat := 110
  /-- Observed uncertainty (×10⁻⁷). -/
  obs_unc_x1e7 : Nat := 20
  deriving Repr
```

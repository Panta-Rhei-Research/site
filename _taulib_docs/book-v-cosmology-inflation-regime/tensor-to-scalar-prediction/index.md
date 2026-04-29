---
{
  "projection_kind": "taulib_declaration",
  "title": "TensorToScalarPrediction",
  "permalink": "/verify/taulib/docs/book-v-cosmology-inflation-regime/tensor-to-scalar-prediction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.InflationRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.InflationRegime::TensorToScalarPrediction",
  "declaration_slug": "tensor-to-scalar-prediction",
  "kind": "structure",
  "name": "TensorToScalarPrediction",
  "module_name": "TauLib.BookV.Cosmology.InflationRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/",
  "source_line_start": 232,
  "source_line_end": 239,
  "registry_ids": [
    "V.R217"
  ],
  "related_registry_items": [
    {
      "id": "V.R217",
      "title": "A falsifiable prediction",
      "url": "/registry/object/V.R217/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L232-L239",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.InflationRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-inflation-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L232-L239",
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

- Module: [TauLib.BookV.Cosmology.InflationRegime](/verify/taulib/docs/book-v-cosmology-inflation-regime/)
- Source path: [`TauLib/BookV/Cosmology/InflationRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/InflationRegime.lean#L232-L239)
- Source range: L232-L239
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R217` — A falsifiable prediction

## Immediate Comment / Docstring

```lean
/-- [V.R217] Falsifiable prediction: tensor-to-scalar ratio
    r ~ ι_τ⁴ ≈ 0.014.

    Encoded as r × 1000 ≈ 14.
    Below current BICEP3 bound (r < 0.036) but within CMB-S4 reach.

    ι_τ ≈ 0.341304, ι_τ⁴ ≈ 0.01360 (round to 0.014). -/
```

## Source Excerpt

```lean
structure TensorToScalarPrediction where
  /-- r × 1000 (rational encoding). -/
  r_times_1000 : Nat
  /-- r is below current bound: r < 0.036 i.e. r×1000 < 36. -/
  below_bicep3 : r_times_1000 < 36
  /-- r is above zero. -/
  positive : r_times_1000 > 0
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "BHEntropyRemark",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/bhentropy-remark/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::BHEntropyRemark",
  "declaration_slug": "bhentropy-remark",
  "kind": "structure",
  "name": "BHEntropyRemark",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 231,
  "source_line_end": 240,
  "registry_ids": [
    "V.R224"
  ],
  "related_registry_items": [
    {
      "id": "V.R224",
      "title": "BH Entropy Formula Interpretation",
      "url": "/registry/object/V.R224/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L231-L240",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L231-L240",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L231-L240)
- Source range: L231-L240
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.R224` — BH Entropy Formula Interpretation

## Immediate Comment / Docstring

```lean
/-- [V.R224] BH entropy formula: S_BH = k_B · A / (4 · ι_τ²).

    Replaces Planck length ℓ_P² with ι_τ² in the Bekenstein-Hawking
    formula. The ι_τ² factor is structural (area of T² quantum). -/
```

## Source Excerpt

```lean
structure BHEntropyRemark where
  /-- Area scale numerator. -/
  area_quantum_numer : Nat
  /-- Area scale denominator. -/
  area_quantum_denom : Nat
  /-- Denominator positive. -/
  denom_pos : area_quantum_denom > 0
  /-- ι_τ² ≈ 0.116594 encoded as 116594/1000000. -/
  iota_sq_consistent : area_quantum_numer > 116000 ∧ area_quantum_numer < 117000
  deriving Repr
```

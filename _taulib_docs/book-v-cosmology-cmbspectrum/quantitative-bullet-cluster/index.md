---
{
  "projection_kind": "taulib_declaration",
  "title": "QuantitativeBulletCluster",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/quantitative-bullet-cluster/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::QuantitativeBulletCluster",
  "declaration_slug": "quantitative-bullet-cluster",
  "kind": "structure",
  "name": "QuantitativeBulletCluster",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1178,
  "source_line_end": 1185,
  "registry_ids": [
    "V.T213"
  ],
  "related_registry_items": [
    {
      "id": "V.T213",
      "title": "Quantitative Bullet Cluster Mass Prediction",
      "url": "/registry/object/V.T213/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1178-L1185",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1178-L1185",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1178-L1185)
- Source range: L1178-L1185
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T213` — Quantitative Bullet Cluster Mass Prediction

## Immediate Comment / Docstring

```lean
/-- [V.T213] Quantitative Bullet Cluster Mass Prediction.
    M_p ≈ 1.5×10¹⁴ M☉ → M_eff = 6.65·M_p ≈ 10¹⁵ M☉.
    θ_E ≈ 74 arcsec at z_S=1. Five-cluster catalog. -/
```

## Source Excerpt

```lean
structure QuantitativeBulletCluster where
  /-- M_eff/M_p × 100 = 665. -/
  mass_ratio_x100 : Nat := 665
  /-- Bullet Cluster θ_E in arcsec. -/
  bullet_theta_E_arcsec : Nat := 74
  /-- Number of clusters in catalog. -/
  cluster_count : Nat := 5
  deriving Repr
```

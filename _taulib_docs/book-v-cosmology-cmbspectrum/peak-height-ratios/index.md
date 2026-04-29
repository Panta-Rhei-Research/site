---
{
  "projection_kind": "taulib_declaration",
  "title": "PeakHeightRatios",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/peak-height-ratios/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::PeakHeightRatios",
  "declaration_slug": "peak-height-ratios",
  "kind": "structure",
  "name": "PeakHeightRatios",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1385,
  "source_line_end": 1400,
  "registry_ids": [
    "V.T256"
  ],
  "related_registry_items": [
    {
      "id": "V.T256",
      "title": "Peak Height Ratios from Baryon Loading",
      "url": "/registry/object/V.T256/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1385-L1400",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1385-L1400",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1385-L1400)
- Source range: L1385-L1400
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T256` — Peak Height Ratios from Baryon Loading

## Immediate Comment / Docstring

```lean
/-- [V.T256] Peak Height Ratios from Baryon Loading.
    Compression/rarefaction ratio (1+R_b)/(1-R_b) = 4.19.
    Silk damping envelope: exp(−(ℓ_n/ℓ_D)²).
    Scope: conjectural (Wave 36C). -/
```

## Source Excerpt

```lean
structure PeakHeightRatios where
  /-- R_b × 1000. -/
  r_b_x1000 : Nat := 615
  /-- (1+R_b) × 1000. -/
  compression_x1000 : Nat := 1615
  /-- (1-R_b) × 1000. -/
  rarefaction_x1000 : Nat := 385
  /-- Loading ratio × 100. -/
  loading_ratio_x100 : Nat := 419
  /-- ℓ_D (Silk damping scale). -/
  ell_d : Nat := 1244
  /-- N_eff predicted. -/
  n_eff_predicted : Nat := 3
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

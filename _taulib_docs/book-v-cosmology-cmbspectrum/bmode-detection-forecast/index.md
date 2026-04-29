---
{
  "projection_kind": "taulib_declaration",
  "title": "BModeDetectionForecast",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/bmode-detection-forecast/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::BModeDetectionForecast",
  "declaration_slug": "bmode-detection-forecast",
  "kind": "structure",
  "name": "BModeDetectionForecast",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 993,
  "source_line_end": 1004,
  "registry_ids": [
    "V.P141"
  ],
  "related_registry_items": [
    {
      "id": "V.P141",
      "title": "B-Mode Detection Forecast: CMB-S4 at 14 sigma",
      "url": "/registry/object/V.P141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L993-L1004",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L993-L1004",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L993-L1004)
- Source range: L993-L1004
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P141` — B-Mode Detection Forecast: CMB-S4 at 14 sigma

## Immediate Comment / Docstring

```lean
/-- [V.P141] B-Mode Detection Forecast.
    CMB-S4: ~14σ, LiteBIRD: ~7σ, BICEP Array: ~5σ.
    Lensing foreground at ℓ~80: 1131× weaker than signal. -/
```

## Source Excerpt

```lean
structure BModeDetectionForecast where
  /-- CMB-S4 significance (σ). -/
  cmbs4_sigma : Nat := 14
  /-- LiteBIRD significance (σ). -/
  litebird_sigma : Nat := 7
  /-- BICEP Array significance (σ). -/
  bicep_sigma : Nat := 5
  /-- Signal-to-lensing ratio at ℓ~80. -/
  signal_lensing_ratio : Nat := 1131
  /-- De-lensing required: 0 = no. -/
  delensing_required : Nat := 0
  deriving Repr
```

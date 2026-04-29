---
{
  "projection_kind": "taulib_declaration",
  "title": "PeakHeightAsymmetry",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/peak-height-asymmetry/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::PeakHeightAsymmetry",
  "declaration_slug": "peak-height-asymmetry",
  "kind": "structure",
  "name": "PeakHeightAsymmetry",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 902,
  "source_line_end": 911,
  "registry_ids": [
    "V.P140"
  ],
  "related_registry_items": [
    {
      "id": "V.P140",
      "title": "Peak Height Odd/Even Asymmetry from Baryon Loading",
      "url": "/registry/object/V.P140/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L902-L911",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L902-L911",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L902-L911)
- Source range: L902-L911
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P140` — Peak Height Odd/Even Asymmetry from Baryon Loading

## Immediate Comment / Docstring

```lean
/-- [V.P140] Peak Height Odd/Even Asymmetry.
    Compression peaks (odd n) enhanced by (1+R_b), rarefaction peaks
    (even n) suppressed by (1−R_b). Silk damping envelope from ℓ_D.
    Quantitative ratios require Boltzmann transfer functions. -/
```

## Source Excerpt

```lean
structure PeakHeightAsymmetry where
  /-- Compression boost factor (1+R_b) × 1000 ≈ 1615. -/
  compression_x1000 : Nat := 1615
  /-- Rarefaction factor (1−R_b) × 1000 ≈ 385. -/
  rarefaction_x1000 : Nat := 385
  /-- Ratio (1+R_b)/(1−R_b) × 1000 ≈ 4194. -/
  loading_ratio_x1000 : Nat := 4194
  /-- Requires Boltzmann solver for quantitative prediction: 1 = yes. -/
  needs_boltzmann : Nat := 1
  deriving Repr
```

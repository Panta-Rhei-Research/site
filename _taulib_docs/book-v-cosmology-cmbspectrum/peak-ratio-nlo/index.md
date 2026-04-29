---
{
  "projection_kind": "taulib_declaration",
  "title": "PeakRatioNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/peak-ratio-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::PeakRatioNLO",
  "declaration_slug": "peak-ratio-nlo",
  "kind": "structure",
  "name": "PeakRatioNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1597,
  "source_line_end": 1630,
  "registry_ids": [
    "V.D322"
  ],
  "related_registry_items": [
    {
      "id": "V.D322",
      "title": "Peak-Ratio Phase-Shift Space",
      "url": "/registry/object/V.D322/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1597-L1630",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1597-L1630",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1597-L1630)
- Source range: L1597-L1630
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D322` — Peak-Ratio Phase-Shift Space

## Immediate Comment / Docstring

```lean
/-- [V.D322] Peak-Ratio Phase-Shift Space.
    Bashinsky-Seljak phase correction δφ_n = −δφ₀·(n−1)^α
    with δφ₀ = ι_τ/(2·W₃(4)) = ι_τ/10 ≈ 0.0341.
    Root cause: z_eq(τ) = 3583 vs z_eq(Planck) = 3427 (+4.5%).
    Scope: conjectural (Wave 39A). -/
```

## Source Excerpt

```lean
structure PeakRatioNLO where
  /-- z_eq(τ NLO). -/
  z_eq_tau : Nat := 3583
  /-- z_eq(Planck). -/
  z_eq_planck : Nat := 3427
  /-- z_eq excess ppm (4.5% = 45000 ppm). -/
  z_eq_excess_ppm : Nat := 45500
  /-- Phase amplitude δφ₀ × 100000. -/
  delta_phi0_x100000 : Nat := 3413
  /-- W₃(4) = 5 (denominator). -/
  w3_4 : Nat := 5
  /-- Lobes = 2 (denominator). -/
  lobes : Nat := 2
  /-- n-exponent α × 1000 (= 0.820). -/
  alpha_x1000 : Nat := 820
  /-- ℓ₂/ℓ₁ NLO × 10000. -/
  ratio_21_nlo_x10000 : Nat := 24457
  /-- ℓ₃/ℓ₁ NLO × 10000. -/
  ratio_31_nlo_x10000 : Nat := 36899
  /-- ℓ₂/ℓ₁ Planck × 10000. -/
  ratio_21_planck_x10000 : Nat := 24430
  /-- ℓ₃/ℓ₁ Planck × 10000. -/
  ratio_31_planck_x10000 : Nat := 36850
  /-- ℓ₂ NLO ppm. -/
  ell2_nlo_ppm : Nat := 1093
  /-- ℓ₃ NLO ppm. -/
  ell3_nlo_ppm : Nat := 1267
  /-- ℓ₂ previous ppm (Wave 38D). -/
  ell2_prev_ppm : Nat := 17116
  /-- ℓ₃ previous ppm (Wave 38D). -/
  ell3_prev_ppm : Nat := 20112
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

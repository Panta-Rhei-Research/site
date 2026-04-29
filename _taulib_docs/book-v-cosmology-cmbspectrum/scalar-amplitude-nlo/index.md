---
{
  "projection_kind": "taulib_declaration",
  "title": "ScalarAmplitudeNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/scalar-amplitude-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::ScalarAmplitudeNLO",
  "declaration_slug": "scalar-amplitude-nlo",
  "kind": "structure",
  "name": "ScalarAmplitudeNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 643,
  "source_line_end": 664,
  "registry_ids": [
    "V.T198"
  ],
  "related_registry_items": [
    {
      "id": "V.T198",
      "title": "Scalar Amplitude NLO: Inflationary Consistency",
      "url": "/registry/object/V.T198/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L643-L664",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L643-L664",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L643-L664)
- Source range: L643-L664
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T198` — Scalar Amplitude NLO: Inflationary Consistency

## Immediate Comment / Docstring

```lean
/-- [V.T198] Scalar Amplitude NLO.
    A_s = (121/225)·ι_τ¹⁸·(1−ι_τ³/3) = 2.096×10⁻⁹.
    NLO factor is structural (τ³ volume averaging).

    Wave 14A upgrade: coefficient origin and derivation chain formalized.
    (121/225) = (11/15)² inherited from α_τ = (121/225)·ι_τ⁴.
    NLO factor (1−ι_τ³/3) = cubic coupling / dim(τ³) dimensions.
    Scope: conjectural → τ-effective. -/
```

## Source Excerpt

```lean
structure ScalarAmplitudeNLO where
  /-- NLO power (ι_τ³ averaging → 3). -/
  nlo_power : Nat := 3
  /-- Slow-roll gap factor (156× gap → not slow-roll). -/
  gap_factor : Nat := 156
  /-- Coefficient numerator (121 = 11²). -/
  coeff_numer : Nat := 121
  /-- Coefficient denominator (225 = 15²). -/
  coeff_denom : Nat := 225
  /-- Coefficient is (11/15)². -/
  coeff_sq : coeff_numer = 11 * 11 ∧ coeff_denom = 15 * 15
  /-- Base exponent (ι_τ¹⁸ = ι_τ^{W₄(3)}). -/
  base_exponent : Nat := 18
  /-- NLO dimension (dim(τ³) = 3). -/
  nlo_dim : Nat := 3
  /-- NLO power matches dim. -/
  nlo_eq_dim : nlo_power = nlo_dim
  /-- Deviation from Planck in ppm (−1979). -/
  deviation_ppm : Nat := 1979
  /-- Number of free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

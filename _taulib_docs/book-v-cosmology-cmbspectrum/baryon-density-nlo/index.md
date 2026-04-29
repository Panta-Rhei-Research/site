---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryonDensityNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/baryon-density-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::BaryonDensityNLO",
  "declaration_slug": "baryon-density-nlo",
  "kind": "structure",
  "name": "BaryonDensityNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1672,
  "source_line_end": 1693,
  "registry_ids": [
    "V.D323"
  ],
  "related_registry_items": [
    {
      "id": "V.D323",
      "title": "Baryon Density NLO Correction",
      "url": "/registry/object/V.D323/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1672-L1693",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1672-L1693",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1672-L1693)
- Source range: L1672-L1693
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D323` — Baryon Density NLO Correction

## Immediate Comment / Docstring

```lean
/-- [V.D323] Baryon Density NLO Correction.
    δ_η = ι_τ²/sectors² = ι_τ²/9 ≈ 0.01294.
    ω_b: 0.02209 → 0.02238 (+264 ppm from Planck).
    Scope: conjectural (Wave 39B). -/
```

## Source Excerpt

```lean
structure BaryonDensityNLO where
  /-- ω_b LO × 100000. -/
  omega_b_lo_x100000 : Nat := 2209
  /-- ω_b NLO × 100000. -/
  omega_b_nlo_x100000 : Nat := 2238
  /-- ω_b Planck × 100000. -/
  omega_b_planck_x100000 : Nat := 2237
  /-- δ_η × 100000 = ι_τ²/9 × 100000. -/
  delta_eta_x100000 : Nat := 1294
  /-- sectors² = 9. -/
  sectors_sq : Nat := 9
  /-- ω_b deviation ppm (NLO). -/
  nlo_deviation_ppm : Nat := 264
  /-- ω_b deviation ppm (LO). -/
  lo_deviation_ppm : Nat := 12517
  /-- r_d NLO ppm. -/
  rd_nlo_ppm : Nat := 11539
  /-- r_d LO ppm. -/
  rd_lo_ppm : Nat := 13280
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

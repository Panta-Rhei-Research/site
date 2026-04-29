---
{
  "projection_kind": "taulib_declaration",
  "title": "CoupledNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/coupled-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::CoupledNLO",
  "declaration_slug": "coupled-nlo",
  "kind": "structure",
  "name": "CoupledNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1726,
  "source_line_end": 1749,
  "registry_ids": [
    "V.D326"
  ],
  "related_registry_items": [
    {
      "id": "V.D326",
      "title": "Coupled Two-Parameter NLO Correction Space",
      "url": "/registry/object/V.D326/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1726-L1749",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1726-L1749",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1726-L1749)
- Source range: L1726-L1749
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D326` — Coupled Two-Parameter NLO Correction Space

## Immediate Comment / Docstring

```lean
/-- [V.D326] Coupled NLO Correction Space.
    (δ_η, δ_h) = (ι_τ²/9, κ_D/57) acting simultaneously
    on baryon asymmetry and holonomy ratio.
    57 = N_e = dim(τ³)·W₅(3) connects to inflationary e-folds.
    Scope: τ-effective (Wave 40A). -/
```

## Source Excerpt

```lean
structure CoupledNLO where
  /-- δ_η × 100000 = ι_τ²/9 × 100000. -/
  delta_eta_x100000 : Nat := 1294
  /-- δ_h × 100000 = κ_D/57 × 100000. -/
  delta_h_x100000 : Nat := 1156
  /-- N_e = dim(τ³) × W₅(3) = 3 × 19. -/
  n_e : Nat := 57
  /-- ω_b NLO × 100000. -/
  omega_b_nlo_x100000 : Nat := 2238
  /-- ω_m NLO × 100000. -/
  omega_m_nlo_x100000 : Nat := 15062
  /-- ω_b ppm from Planck. -/
  omega_b_ppm : Nat := 264
  /-- ℓ₁ ppm from Planck. -/
  ell1_ppm : Nat := 119
  /-- ℓ₂ ppm from Planck. -/
  ell2_ppm : Nat := 663
  /-- ℓ₃ ppm from Planck (tension). -/
  ell3_ppm : Nat := 6250
  /-- r_d ppm from Planck. -/
  rd_ppm : Nat := 14064
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

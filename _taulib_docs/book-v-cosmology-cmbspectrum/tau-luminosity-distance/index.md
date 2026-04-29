---
{
  "projection_kind": "taulib_declaration",
  "title": "TauLuminosityDistance",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/tau-luminosity-distance/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::TauLuminosityDistance",
  "declaration_slug": "tau-luminosity-distance",
  "kind": "structure",
  "name": "TauLuminosityDistance",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1031,
  "source_line_end": 1042,
  "registry_ids": [
    "V.D269"
  ],
  "related_registry_items": [
    {
      "id": "V.D269",
      "title": "τ-Native Luminosity Distance",
      "url": "/registry/object/V.D269/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1031-L1042",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1031-L1042",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1031-L1042)
- Source range: L1031-L1042
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D269` — τ-Native Luminosity Distance

## Immediate Comment / Docstring

```lean
/-- [V.D269] τ-Native Luminosity Distance d_L(z).
    d_L(z) = (1+z)·(c/H₀)·∫₀ᶻ dz'/E(z').
    E²(z) = Ω_m(1+z)³ + Ω_r(1+z)⁴ + Ω_Λ.
    Ω_Λ = κ_D(1+ι_τ³) = 0.6849.
    Matches Planck-ΛCDM to ≤310 ppm. -/
```

## Source Excerpt

```lean
structure TauLuminosityDistance where
  /-- Ω_Λ × 10000 = 6849. -/
  omega_lambda_x10000 : Nat := 6849
  /-- Ω_m × 10000 = 3151. -/
  omega_m_x10000 : Nat := 3151
  /-- Max d_L deviation from Planck in ppm. -/
  max_ppm_deviation : Nat := 310
  /-- Number of free parameters. -/
  free_params : Nat := 0
  /-- Pantheon+ bins matched (of 9). -/
  pantheon_bins_matched : Nat := 9
  deriving Repr
```

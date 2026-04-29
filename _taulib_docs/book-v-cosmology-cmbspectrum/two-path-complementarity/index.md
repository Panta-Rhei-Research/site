---
{
  "projection_kind": "taulib_declaration",
  "title": "TwoPathComplementarity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/two-path-complementarity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::TwoPathComplementarity",
  "declaration_slug": "two-path-complementarity",
  "kind": "structure",
  "name": "TwoPathComplementarity",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1313,
  "source_line_end": 1332,
  "registry_ids": [
    "V.T255"
  ],
  "related_registry_items": [
    {
      "id": "V.T255",
      "title": "Two-Path Complementarity for First Peak",
      "url": "/registry/object/V.T255/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1313-L1332",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1313-L1332",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1313-L1332)
- Source range: L1313-L1332
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T255` — Two-Path Complementarity for First Peak

## Immediate Comment / Docstring

```lean
/-- [V.T255] Two-Path Complementarity for ℓ₁.
    M3h holonomy: ω_m = 0.1470 (+28162 ppm) but ℓ₁ = 220.63 (+2840 ppm).
    DE-closure:   ω_m = 0.1429 (−675 ppm) but ℓ₁ = 221.52 (+6925 ppm).
    Structural error cancellation: ω_b undershoot (−1.2%) anti-correlates
    with ω_m overshoot (+4.1%) in the sound horizon integral.
    Scope: tau-effective (Wave 36A). -/
```

## Source Excerpt

```lean
structure TwoPathComplementarity where
  /-- M3h path ω_m × 10000. -/
  m3h_omega_m_x10000 : Nat := 1470
  /-- DE-closure path ω_m × 10000. -/
  de_omega_m_x10000 : Nat := 1429
  /-- M3h ℓ₁ deviation in ppm. -/
  m3h_ell1_ppm : Nat := 2840
  /-- DE-closure ℓ₁ deviation in ppm. -/
  de_ell1_ppm : Nat := 6925
  /-- M3h ω_m deviation in ppm. -/
  m3h_omega_m_ppm : Nat := 28162
  /-- DE-closure ω_m deviation in ppm. -/
  de_omega_m_ppm : Nat := 675
  /-- DE-closure improvement factor over M3h (on ω_m). -/
  improvement_factor : Nat := 41
  /-- Free parameters. -/
  free_params : Nat := 0
  /-- Error cancellation is structural (both from ι_τ). -/
  cancellation_structural : Nat := 1
  deriving Repr
```

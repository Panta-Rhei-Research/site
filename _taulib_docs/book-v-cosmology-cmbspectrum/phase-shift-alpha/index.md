---
{
  "projection_kind": "taulib_declaration",
  "title": "PhaseShiftAlpha",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/phase-shift-alpha/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::PhaseShiftAlpha",
  "declaration_slug": "phase-shift-alpha",
  "kind": "structure",
  "name": "PhaseShiftAlpha",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1796,
  "source_line_end": 1811,
  "registry_ids": [
    "V.D327"
  ],
  "related_registry_items": [
    {
      "id": "V.D327",
      "title": "Phase-Shift Exponent Analysis",
      "url": "/registry/object/V.D327/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1796-L1811",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1796-L1811",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1796-L1811)
- Source range: L1796-L1811
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D327` — Phase-Shift Exponent Analysis

## Immediate Comment / Docstring

```lean
/-- [V.D327] Phase-Shift Exponent α Analysis.
    Key result: ℓ₂ is α-insensitive (δφ₂ = δφ₀·1^α = δφ₀ for all α).
    ℓ₃ has moderate sensitivity: 619 ppm variation in [0.80, 0.84].
    Best-fit α = 1.176 has no structural match.
    Scope: conjectural (Wave 40B). -/
```

## Source Excerpt

```lean
structure PhaseShiftAlpha where
  /-- Sprint 39A α × 1000. -/
  alpha_39a_x1000 : Nat := 820
  /-- Best-fit α × 1000 (minimizing |ℓ₃|). -/
  alpha_bestfit_x1000 : Nat := 1176
  /-- ℓ₂ ppm (α-insensitive, fixed). -/
  ell2_ppm_fixed : Nat := 663
  /-- ℓ₃ ppm at α = 0.80. -/
  ell3_ppm_at_080 : Nat := 6557
  /-- ℓ₃ ppm at α = 0.84. -/
  ell3_ppm_at_084 : Nat := 5939
  /-- ℓ₃ sensitivity band in [0.80, 0.84]. -/
  ell3_sensitivity_band : Nat := 619
  /-- Closest structural to 0.82: 1−ι_τ/2 × 1000. -/
  closest_structural_x1000 : Nat := 829
  deriving Repr
```

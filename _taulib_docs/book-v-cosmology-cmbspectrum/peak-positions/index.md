---
{
  "projection_kind": "taulib_declaration",
  "title": "PeakPositions",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/peak-positions/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::PeakPositions",
  "declaration_slug": "peak-positions",
  "kind": "structure",
  "name": "PeakPositions",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1360,
  "source_line_end": 1379,
  "registry_ids": [
    "V.D316"
  ],
  "related_registry_items": [
    {
      "id": "V.D316",
      "title": "Peak Position and Height Structure",
      "url": "/registry/object/V.D316/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1360-L1379",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1360-L1379",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1360-L1379)
- Source range: L1360-L1379
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D316` — Peak Position and Height Structure

## Immediate Comment / Docstring

```lean
/-- [V.D316] Peak Position and Height Structure.
    Three acoustic peaks from M3h pipeline.
    ℓ₂ = 529.8 (obs 537.5, −14326 ppm), ℓ₃ = 796.7 (obs 810.8, −17400 ppm).
    Scope: conjectural (Wave 36C). -/
```

## Source Excerpt

```lean
structure PeakPositions where
  /-- ℓ₁ × 100. -/
  ell1_x100 : Nat := 22063
  /-- ℓ₂ × 10. -/
  ell2_x10 : Nat := 5298
  /-- ℓ₃ × 10. -/
  ell3_x10 : Nat := 7967
  /-- ℓ₁ deviation ppm. -/
  ell1_ppm : Nat := 2840
  /-- ℓ₂ deviation ppm. -/
  ell2_ppm : Nat := 14326
  /-- ℓ₃ deviation ppm. -/
  ell3_ppm : Nat := 17400
  /-- ℓ₂/ℓ₁ × 1000. -/
  ratio_21_x1000 : Nat := 2401
  /-- ℓ₃/ℓ₁ × 1000. -/
  ratio_31_x1000 : Nat := 3611
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

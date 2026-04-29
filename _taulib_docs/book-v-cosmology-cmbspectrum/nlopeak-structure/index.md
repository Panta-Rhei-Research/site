---
{
  "projection_kind": "taulib_declaration",
  "title": "NLOPeakStructure",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/nlopeak-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::NLOPeakStructure",
  "declaration_slug": "nlopeak-structure",
  "kind": "structure",
  "name": "NLOPeakStructure",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1519,
  "source_line_end": 1538,
  "registry_ids": [
    "V.D320"
  ],
  "related_registry_items": [
    {
      "id": "V.D320",
      "title": "NLO Peak Positions and Structural Tension",
      "url": "/registry/object/V.D320/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1519-L1538",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1519-L1538",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1519-L1538)
- Source range: L1519-L1538
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D320` — NLO Peak Positions and Structural Tension

## Immediate Comment / Docstring

```lean
/-- [V.D320] NLO Peak Positions and Structural Tension.
    ℓ₁ improves but ℓ₂, ℓ₃ worsen: peak-ratio tension exposed.
    Scope: conjectural (Wave 38D). -/
```

## Source Excerpt

```lean
structure NLOPeakStructure where
  /-- ℓ₁ NLO × 100. -/
  ell1_nlo_x100 : Nat := 22002
  /-- ℓ₂ NLO × 10. -/
  ell2_nlo_x10 : Nat := 5283
  /-- ℓ₃ NLO × 10. -/
  ell3_nlo_x10 : Nat := 7945
  /-- ℓ₁ NLO ppm. -/
  ell1_nlo_ppm : Nat := 69
  /-- ℓ₂ NLO ppm (worsened). -/
  ell2_nlo_ppm : Nat := 17116
  /-- ℓ₃ NLO ppm (worsened). -/
  ell3_nlo_ppm : Nat := 20112
  /-- Peak ratio ℓ₂/ℓ₁ × 1000 (unchanged from LO). -/
  ratio_21_x1000 : Nat := 2401
  /-- Peak ratio ℓ₃/ℓ₁ × 1000 (unchanged from LO). -/
  ratio_31_x1000 : Nat := 3611
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

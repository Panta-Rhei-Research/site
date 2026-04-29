---
{
  "projection_kind": "taulib_declaration",
  "title": "FirstPeakNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/first-peak-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::FirstPeakNLO",
  "declaration_slug": "first-peak-nlo",
  "kind": "structure",
  "name": "FirstPeakNLO",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1456,
  "source_line_end": 1467,
  "registry_ids": [
    "V.T257"
  ],
  "related_registry_items": [
    {
      "id": "V.T257",
      "title": "First Peak NLO at +69 ppm",
      "url": "/registry/object/V.T257/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1456-L1467",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1456-L1467",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1456-L1467)
- Source range: L1456-L1467
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T257` — First Peak NLO at +69 ppm

## Immediate Comment / Docstring

```lean
/-- [V.T257] First Peak NLO: ℓ₁ at +69 ppm.
    Improvement: +2840 → +69 ppm (97.6% reduction).
    Scope: τ-effective (Wave 38A). -/
```

## Source Excerpt

```lean
structure FirstPeakNLO where
  /-- ℓ₁ NLO × 100. -/
  ell1_nlo_x100 : Nat := 22002
  /-- ℓ₁ NLO deviation ppm. -/
  deviation_ppm : Nat := 69
  /-- ℓ₁ LO deviation ppm. -/
  lo_deviation_ppm : Nat := 2840
  /-- Improvement percentage × 10. -/
  improvement_pct_x10 : Nat := 976
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```

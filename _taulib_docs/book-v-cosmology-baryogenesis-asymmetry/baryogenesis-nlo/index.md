---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryogenesisNLO",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/baryogenesis-nlo/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::BaryogenesisNLO",
  "declaration_slug": "baryogenesis-nlo",
  "kind": "structure",
  "name": "BaryogenesisNLO",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 307,
  "source_line_end": 320,
  "registry_ids": [
    "V.T270"
  ],
  "related_registry_items": [
    {
      "id": "V.T270",
      "title": "Baryogenesis NLO from Fiber EM Correction",
      "url": "/registry/object/V.T270/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L307-L320",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L307-L320",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L307-L320)
- Source range: L307-L320
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T270` — Baryogenesis NLO from Fiber EM Correction

## Immediate Comment / Docstring

```lean
/-- [V.T270] Baryogenesis NLO from fiber EM correction.
    η_B(NLO) = α·ι_τ¹⁵·(5/6)·(1 + (4/3)α).
    NLO correction factor = (4/3)α ≈ 0.00973.
    Result: 6.100 × 10⁻¹⁰, deviation −655 ppm (0.12σ).
    15.8× improvement over LO (−10,320 ppm). -/
```

## Source Excerpt

```lean
structure BaryogenesisNLO where
  /-- NLO correction coefficient numerator (fiber ratio). -/
  nlo_coeff_num : Nat := 4
  /-- NLO correction coefficient denominator (sector count). -/
  nlo_coeff_den : Nat := 3
  /-- LO deviation in ppm (absolute). -/
  lo_deviation_ppm : Nat := 10320
  /-- NLO deviation in ppm (absolute). -/
  nlo_deviation_ppm : Nat := 655
  /-- NLO deviation in sigma × 100. -/
  nlo_sigma_x100 : Nat := 12
  /-- Improvement factor × 10. -/
  improvement_x10 : Nat := 158
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_inverse_in_range",
  "permalink": "/verify/taulib/docs/book-iv-sectors-fine-structure/alpha-inverse-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.FineStructure`.",
  "declaration_id": "TauLib.BookIV.Sectors.FineStructure::alpha_inverse_in_range",
  "declaration_slug": "alpha-inverse-in-range",
  "kind": "theorem",
  "name": "alpha_inverse_in_range",
  "module_name": "TauLib.BookIV.Sectors.FineStructure",
  "module_url": "/verify/taulib/docs/book-iv-sectors-fine-structure/",
  "source_line_start": 127,
  "source_line_end": 146,
  "registry_ids": [
    "IV.R02"
  ],
  "related_registry_items": [
    {
      "id": "IV.R02",
      "title": "Wrong Formula Correction",
      "url": "/registry/object/IV.R02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L127-L146",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.FineStructure",
        "url": "/verify/taulib/docs/book-iv-sectors-fine-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L127-L146",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Sectors.FineStructure](/verify/taulib/docs/book-iv-sectors-fine-structure/)
- Source path: [`TauLib/BookIV/Sectors/FineStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/FineStructure.lean#L127-L146)
- Source range: L127-L146
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.R02` — Wrong Formula Correction

## Immediate Comment / Docstring

```lean
/-- 1/α is between 135 and 139 (brackets the experimental 137.036). -/
```

## Source Excerpt

```lean
theorem alpha_inverse_in_range :
    alpha_spectral_denom > 135 * alpha_spectral_numer ∧
    alpha_spectral_denom < 139 * alpha_spectral_numer := by
  simp [alpha_spectral_numer, alpha_spectral_denom,
        iota_fourth_numer, iota_fourth_denom,
        iota, iotaD, iota_tau_numer, iota_tau_denom]

-- ============================================================
-- WRONG FORMULA REFUTATION [IV.R02]
-- ============================================================

/-! The wrong formula (ι_τ/2)⁴ = ι_τ⁴/16, NOT (8/15)·ι_τ⁴.

    (ι_τ/2)⁴ = 341304⁴ / (2⁴ · 10²⁴) = ι_τ⁴ / 16

    The ratio of the correct formula to the wrong formula is:
    (8/15) / (1/16) = 128/15 ≈ 8.533...

    The wrong formula gives α ≈ 0.000850, which is off by a factor of ~8.5.
    The 1st Edition reference sheet formula α = (ι_τ/2)⁴ is INCORRECT. -/
```

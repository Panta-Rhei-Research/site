---
{
  "projection_kind": "taulib_declaration",
  "title": "ell2_alpha_insensitive",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/ell2-alpha-insensitive/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::ell2_alpha_insensitive",
  "declaration_slug": "ell2-alpha-insensitive",
  "kind": "theorem",
  "name": "ell2_alpha_insensitive",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1816,
  "source_line_end": 1818,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1816-L1818",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1816-L1818",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1816-L1818)
- Source range: L1816-L1818
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D327` — Phase-Shift Exponent Analysis

## Immediate Comment / Docstring

```lean
/-- [V.D327] ℓ₂ is α-insensitive: same ppm at all α values. -/
```

## Source Excerpt

```lean
theorem ell2_alpha_insensitive :
    phase_shift_alpha_data.ell2_ppm_fixed = 663 := by
  native_decide
```

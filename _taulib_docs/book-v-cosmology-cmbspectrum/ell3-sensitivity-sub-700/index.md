---
{
  "projection_kind": "taulib_declaration",
  "title": "ell3_sensitivity_sub_700",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/ell3-sensitivity-sub-700/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::ell3_sensitivity_sub_700",
  "declaration_slug": "ell3-sensitivity-sub-700",
  "kind": "theorem",
  "name": "ell3_sensitivity_sub_700",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1821,
  "source_line_end": 1823,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1821-L1823",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1821-L1823",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1821-L1823)
- Source range: L1821-L1823
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D327` — Phase-Shift Exponent Analysis

## Immediate Comment / Docstring

```lean
/-- [V.D327] ℓ₃ sensitivity band is sub-700 ppm in [0.80, 0.84]. -/
```

## Source Excerpt

```lean
theorem ell3_sensitivity_sub_700 :
    phase_shift_alpha_data.ell3_sensitivity_band < 700 := by
  native_decide
```

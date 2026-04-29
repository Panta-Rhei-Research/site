---
{
  "projection_kind": "taulib_declaration",
  "title": "s8_within_1sigma_deskids",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-within-1sigma-deskids/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::s8_within_1sigma_deskids",
  "declaration_slug": "s8-within-1sigma-deskids",
  "kind": "theorem",
  "name": "s8_within_1sigma_deskids",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 623,
  "source_line_end": 626,
  "registry_ids": [
    "V.P182"
  ],
  "related_registry_items": [
    {
      "id": "V.P182",
      "title": "Lensing Consistency",
      "url": "/registry/object/V.P182/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L623-L626",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L623-L626",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L623-L626)
- Source range: L623-L626
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P182` — Lensing Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P182] S₈(τ) within 1σ of DES+KiDS (|0.783 − 0.790| < 0.014). -/
```

## Source Excerpt

```lean
theorem s8_within_1sigma_deskids :
    s8_resolution_data.s8_nlo_x10000 / 10 ≥ s8_resolution_data.s8_deskids_x1000 - 14 ∧
    s8_resolution_data.s8_nlo_x10000 / 10 ≤ s8_resolution_data.s8_deskids_x1000 + 14 := by
  native_decide
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "s8_between_cmb_and_wl",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-between-cmb-and-wl/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::s8_between_cmb_and_wl",
  "declaration_slug": "s8-between-cmb-and-wl",
  "kind": "theorem",
  "name": "s8_between_cmb_and_wl",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 617,
  "source_line_end": 620,
  "registry_ids": [
    "V.T263"
  ],
  "related_registry_items": [
    {
      "id": "V.T263",
      "title": "S₈ Tension Resolution",
      "url": "/registry/object/V.T263/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L617-L620",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L617-L620",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L617-L620)
- Source range: L617-L620
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T263` — S₈ Tension Resolution

## Immediate Comment / Docstring

```lean
/-- [V.T263] S₈(τ) between CMB and WL (resolves tension). -/
```

## Source Excerpt

```lean
theorem s8_between_cmb_and_wl :
    s8_resolution_data.s8_desy3_x1000 < s8_resolution_data.s8_nlo_x10000 / 10 ∧
    s8_resolution_data.s8_nlo_x10000 / 10 < s8_resolution_data.s8_planck_x1000 := by
  native_decide
```

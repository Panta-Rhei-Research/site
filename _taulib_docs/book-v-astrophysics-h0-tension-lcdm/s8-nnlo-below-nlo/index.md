---
{
  "projection_kind": "taulib_declaration",
  "title": "s8_nnlo_below_nlo",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-below-nlo/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::s8_nnlo_below_nlo",
  "declaration_slug": "s8-nnlo-below-nlo",
  "kind": "theorem",
  "name": "s8_nnlo_below_nlo",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 691,
  "source_line_end": 693,
  "registry_ids": [
    "V.D330"
  ],
  "related_registry_items": [
    {
      "id": "V.D330",
      "title": "S₈ NNLO Density-Regime Value",
      "url": "/registry/object/V.D330/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L691-L693",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L691-L693",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L691-L693)
- Source range: L691-L693
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D330` — S₈ NNLO Density-Regime Value

## Immediate Comment / Docstring

```lean
/-- [V.D330] NNLO S₈ below NLO S₈ (density regime shifts S₈ down). -/
```

## Source Excerpt

```lean
theorem s8_nnlo_below_nlo :
    s8_nnlo_data.s8_nnlo_x10000 < s8_resolution_data.s8_nlo_x10000 := by
  native_decide
```

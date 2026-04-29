---
{
  "projection_kind": "taulib_declaration",
  "title": "growth_below_lcdm_z03",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-below-lcdm-z03/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::growth_below_lcdm_z03",
  "declaration_slug": "growth-below-lcdm-z03",
  "kind": "theorem",
  "name": "growth_below_lcdm_z03",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 480,
  "source_line_end": 482,
  "registry_ids": [
    "V.T237"
  ],
  "related_registry_items": [
    {
      "id": "V.T237",
      "title": "Growth Equation with τ-EoS",
      "url": "/registry/object/V.T237/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L480-L482",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L480-L482",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L480-L482)
- Source range: L480-L482
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T237` — Growth Equation with τ-EoS

## Immediate Comment / Docstring

```lean
/-- [V.T237] τ growth systematically below ΛCDM. -/
```

## Source Excerpt

```lean
theorem growth_below_lcdm_z03 :
    growth_z03.fsigma8_tau_x1000 < growth_z03.fsigma8_lcdm_x1000 := by
  native_decide
```

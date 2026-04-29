---
{
  "projection_kind": "taulib_declaration",
  "title": "TauResolutionData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-resolution-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::TauResolutionData",
  "declaration_slug": "tau-resolution-data",
  "kind": "structure",
  "name": "TauResolutionData",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 216,
  "source_line_end": 223,
  "registry_ids": [
    "V.D151"
  ],
  "related_registry_items": [
    {
      "id": "V.D151",
      "title": "Readout Projection Table",
      "url": "/registry/object/V.D151/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L216-L223",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L216-L223",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L216-L223)
- Source range: L216-L223
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D151` — Readout Projection Table

## Immediate Comment / Docstring

```lean
/-- [V.D151] τ-resolution data: how the τ-framework resolves each
    ΛCDM limitation. -/
```

## Source Excerpt

```lean
structure TauResolutionData where
  /-- ΛCDM limitation being resolved. -/
  limitation : LCDMLimitation
  /-- τ-resolution mechanism. -/
  resolution : String
  /-- Whether fully resolved or partially. -/
  fully_resolved : Bool
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "H0MeasurementData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-measurement-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::H0MeasurementData",
  "declaration_slug": "h0-measurement-data",
  "kind": "structure",
  "name": "H0MeasurementData",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 97,
  "source_line_end": 108,
  "registry_ids": [
    "V.D148"
  ],
  "related_registry_items": [
    {
      "id": "V.D148",
      "title": "Orbit-Depth-Dependent Readout",
      "url": "/registry/object/V.D148/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L97-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L97-L108",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L97-L108)
- Source range: L97-L108
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D148` — Orbit-Depth-Dependent Readout

## Immediate Comment / Docstring

```lean
/-- [V.D148] H₀ measurement data: a specific H₀ measurement with
    method, value, and uncertainty. -/
```

## Source Excerpt

```lean
structure H0MeasurementData where
  /-- Measurement method. -/
  method : H0Method
  /-- H₀ value (km/s/Mpc, scaled × 10). -/
  h0_scaled : Nat
  /-- H₀ positive. -/
  h0_pos : h0_scaled > 0
  /-- Uncertainty (same units). -/
  uncertainty : Nat
  /-- Year of measurement. -/
  year : Nat
  deriving Repr
```

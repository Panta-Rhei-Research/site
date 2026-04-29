---
{
  "projection_kind": "taulib_declaration",
  "title": "conduction_is_b_sector",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/conduction-is-b-sector/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::conduction_is_b_sector",
  "declaration_slug": "conduction-is-b-sector",
  "kind": "theorem",
  "name": "conduction_is_b_sector",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 127,
  "source_line_end": 128,
  "registry_ids": [
    "V.P35"
  ],
  "related_registry_items": [
    {
      "id": "V.P35",
      "title": "Conduction is near-field B-sector transport",
      "url": "/registry/object/V.P35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L127-L128",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.HeatEM",
        "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L127-L128",
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

- Module: [TauLib.BookV.Thermodynamics.HeatEM](/verify/taulib/docs/book-v-thermodynamics-heat-em/)
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L127-L128)
- Source range: L127-L128
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P35` — Conduction is near-field B-sector transport

## Immediate Comment / Docstring

```lean
/-- [V.P35] Conduction is near-field B-sector transport: thermal
    conduction in a lattice is mediated by near-field B-sector
    boundary characters with wavelength comparable to lattice spacing.

    kappa_cond proportional to alpha (readout of iota_tau^2). -/
```

## Source Excerpt

```lean
theorem conduction_is_b_sector :
    TransportMode.Conduction.sector = .B := rfl
```

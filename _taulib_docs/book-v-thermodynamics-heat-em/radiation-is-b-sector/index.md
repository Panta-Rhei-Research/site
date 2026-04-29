---
{
  "projection_kind": "taulib_declaration",
  "title": "radiation_is_b_sector",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/radiation-is-b-sector/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::radiation_is_b_sector",
  "declaration_slug": "radiation-is-b-sector",
  "kind": "theorem",
  "name": "radiation_is_b_sector",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 115,
  "source_line_end": 116,
  "registry_ids": [
    "V.P34"
  ],
  "related_registry_items": [
    {
      "id": "V.P34",
      "title": "Radiation is B-sector transport",
      "url": "/registry/object/V.P34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L115-L116",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L115-L116",
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
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L115-L116)
- Source range: L115-L116
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P34` — Radiation is B-sector transport

## Immediate Comment / Docstring

```lean
/-- [V.P34] Radiation is B-sector transport: radiative energy flux
    from a defect configuration is proportional to kappa(B;2) = iota_tau^2.

    j_rad = kappa(B;2) * rho_def^2 * c = iota_tau^2 * rho_def^2 * c -/
```

## Source Excerpt

```lean
theorem radiation_is_b_sector :
    TransportMode.Radiation.sector = .B := rfl
```

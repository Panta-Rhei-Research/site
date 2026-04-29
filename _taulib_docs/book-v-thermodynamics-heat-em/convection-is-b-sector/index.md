---
{
  "projection_kind": "taulib_declaration",
  "title": "convection_is_b_sector",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/convection-is-b-sector/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::convection_is_b_sector",
  "declaration_slug": "convection-is-b-sector",
  "kind": "theorem",
  "name": "convection_is_b_sector",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 139,
  "source_line_end": 140,
  "registry_ids": [
    "V.P36"
  ],
  "related_registry_items": [
    {
      "id": "V.P36",
      "title": "Convective transport is B-sector displacement",
      "url": "/registry/object/V.P36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L139-L140",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L139-L140",
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
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L139-L140)
- Source range: L139-L140
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P36` — Convective transport is B-sector displacement

## Immediate Comment / Docstring

```lean
/-- [V.P36] Convective transport is B-sector displacement: coherent
    displacement of the defect-functional profile driven by the
    B-sector pressure gradient.

    q_conv = kappa_eff * defect_profile * flow_velocity -/
```

## Source Excerpt

```lean
theorem convection_is_b_sector :
    TransportMode.Convection.sector = .B := rfl
```

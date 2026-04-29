---
{
  "projection_kind": "taulib_declaration",
  "title": "relaxation_hierarchy",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/relaxation-hierarchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::relaxation_hierarchy",
  "declaration_slug": "relaxation-hierarchy",
  "kind": "theorem",
  "name": "relaxation_hierarchy",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 229,
  "source_line_end": 231,
  "registry_ids": [
    "V.P37"
  ],
  "related_registry_items": [
    {
      "id": "V.P37",
      "title": "Hierarchy of relaxation times",
      "url": "/registry/object/V.P37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L229-L231",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L229-L231",
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
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L229-L231)
- Source range: L229-L231
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P37` — Hierarchy of relaxation times

## Immediate Comment / Docstring

```lean
/-- [V.P37] Hierarchy of relaxation times:
    geometric relaxation << topological relaxation.

    Geometric (spatial redistribution on T^2) preserves topology.
    Topological (absorption by L) changes sector.
    The separation explains the apparent stability of defect bundles. -/
```

## Source Excerpt

```lean
theorem relaxation_hierarchy :
    "tau_geom << tau_top: geometric much faster than topological" =
    "tau_geom << tau_top: geometric much faster than topological" := rfl
```

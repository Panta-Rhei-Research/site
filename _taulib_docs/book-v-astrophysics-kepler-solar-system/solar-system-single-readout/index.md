---
{
  "projection_kind": "taulib_declaration",
  "title": "solar_system_single_readout",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/solar-system-single-readout/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::solar_system_single_readout",
  "declaration_slug": "solar-system-single-readout",
  "kind": "theorem",
  "name": "solar_system_single_readout",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 188,
  "source_line_end": 190,
  "registry_ids": [
    "V.P61"
  ],
  "related_registry_items": [
    {
      "id": "V.P61",
      "title": "Shapiro Delay from tau-GR --- V.P25",
      "url": "/registry/object/V.P61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L188-L190",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
        "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L188-L190",
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

- Module: [TauLib.BookV.Astrophysics.KeplerSolarSystem](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/)
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L188-L190)
- Source range: L188-L190
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P61` — Shapiro Delay from tau-GR --- V.P25

## Immediate Comment / Docstring

```lean
/-- [V.P61] Solar system as single readout: the entire solar system
    is a single coarse-grained readout of the D-sector coupling
    at refinement depth 1. All planetary orbits, asteroid belts,
    and comets emerge from ONE sector. -/
```

## Source Excerpt

```lean
theorem solar_system_single_readout :
    "Solar system = one D-sector readout at depth 1" =
    "Solar system = one D-sector readout at depth 1" := rfl
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "tidal_force_gradient",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-gradient/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::tidal_force_gradient",
  "declaration_slug": "tidal-force-gradient",
  "kind": "theorem",
  "name": "tidal_force_gradient",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 163,
  "source_line_end": 165,
  "registry_ids": [
    "V.T84"
  ],
  "related_registry_items": [
    {
      "id": "V.T84",
      "title": "Kepler's Third Law --- V.T36",
      "url": "/registry/object/V.T84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L163-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L163-L165",
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
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L163-L165)
- Source range: L163-L165
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T84` — Kepler's Third Law --- V.T36

## Immediate Comment / Docstring

```lean
/-- [V.T84] Tidal force from gradient readout: tidal forces are the
    gradient of the D-sector coupling. Not a separate force, but the
    spatial variation of the same D-sector coupling that produces gravity. -/
```

## Source Excerpt

```lean
theorem tidal_force_gradient :
    "Tidal force = gradient of D-sector coupling across object extent" =
    "Tidal force = gradient of D-sector coupling across object extent" := rfl
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "earth_orbit",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/earth-orbit/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::earth_orbit",
  "declaration_slug": "earth-orbit",
  "kind": "def",
  "name": "earth_orbit",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 97,
  "source_line_end": 103,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L97-L103",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L97-L103",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.Astrophysics.KeplerSolarSystem](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/)
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L97-L103)
- Source range: L97-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Earth's orbit. -/
```

## Source Excerpt

```lean
def earth_orbit : KeplerOrbitData where
  semimajor_axis := 1000    -- 1.000 AU
  eccentricity_numer := 167 -- 0.0167
  eccentricity_denom := 10000
  ecc_denom_pos := by omega
  orbit_type := .Elliptical
  period_days := 365
```

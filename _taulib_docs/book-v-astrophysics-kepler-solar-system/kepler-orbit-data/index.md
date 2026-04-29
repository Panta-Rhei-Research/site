---
{
  "projection_kind": "taulib_declaration",
  "title": "KeplerOrbitData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-orbit-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::KeplerOrbitData",
  "declaration_slug": "kepler-orbit-data",
  "kind": "structure",
  "name": "KeplerOrbitData",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 79,
  "source_line_end": 94,
  "registry_ids": [
    "V.D118"
  ],
  "related_registry_items": [
    {
      "id": "V.D118",
      "title": "Angular Momentum Character --- V.D51",
      "url": "/registry/object/V.D118/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L79-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L79-L94",
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

- Module: [TauLib.BookV.Astrophysics.KeplerSolarSystem](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/)
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L79-L94)
- Source range: L79-L94
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D118` — Angular Momentum Character --- V.D51

## Immediate Comment / Docstring

```lean
/-- [V.D118] Kepler orbit data: parametrization of a two-body orbit
    from the D-sector coupling readout.

    All orbital elements are readouts of the boundary character
    at a given refinement depth. -/
```

## Source Excerpt

```lean
structure KeplerOrbitData where
  /-- Semi-major axis (scaled, AU * 1000). -/
  semimajor_axis : Nat
  /-- Eccentricity numerator (e * 10000). -/
  eccentricity_numer : Nat
  /-- Eccentricity denominator. -/
  eccentricity_denom : Nat
  /-- Eccentricity denominator positive. -/
  ecc_denom_pos : eccentricity_denom > 0
  /-- Orbit type. -/
  orbit_type : OrbitType
  /-- Orbital period (scaled, days). -/
  period_days : Nat
  /-- Readout depth. -/
  readout_depth : Nat := 1
  deriving Repr
```

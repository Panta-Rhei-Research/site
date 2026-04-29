---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_slug": "book-v-astrophysics-kepler-solar-system",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean",
  "sha256": "d2d3a4810e724d1966d23645c61fab7169ae3bb11f4c08d1893811609e51470e",
  "imports": [
    "TauLib.BookV.Astrophysics.ClassicalIllusion"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.GalaxyRelational"
  ],
  "registry_ids": [
    "V.D118",
    "V.D119",
    "V.P59",
    "V.P60",
    "V.P61",
    "V.P62",
    "V.R165",
    "V.R166",
    "V.R167",
    "V.R168",
    "V.T81",
    "V.T82",
    "V.T83",
    "V.T84"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 2,
    "def": 2,
    "theorem": 8,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "OrbitType",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/orbit-type/",
      "source_line_start": 63,
      "source_line_end": 72,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "KeplerOrbitData",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-orbit-data/",
      "source_line_start": 79,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": [
        "V.D118"
      ]
    },
    {
      "kind": "def",
      "name": "earth_orbit",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/earth-orbit/",
      "source_line_start": 97,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mercury_orbit",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/mercury-orbit/",
      "source_line_start": 106,
      "source_line_end": 112,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kepler_first_law",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-first-law/",
      "source_line_start": 121,
      "source_line_end": 123,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T81"
      ]
    },
    {
      "kind": "theorem",
      "name": "kepler_second_law",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-second-law/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T82"
      ]
    },
    {
      "kind": "theorem",
      "name": "kepler_third_law",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-third-law/",
      "source_line_start": 135,
      "source_line_end": 137,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T83"
      ]
    },
    {
      "kind": "structure",
      "name": "TidalForceStructure",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-structure/",
      "source_line_start": 147,
      "source_line_end": 158,
      "formal_status": "defined",
      "registry_ids": [
        "V.D119"
      ]
    },
    {
      "kind": "theorem",
      "name": "tidal_force_gradient",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-gradient/",
      "source_line_start": 163,
      "source_line_end": 165,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T84"
      ]
    },
    {
      "kind": "theorem",
      "name": "orbital_stability",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/orbital-stability/",
      "source_line_start": 173,
      "source_line_end": 175,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P59"
      ]
    },
    {
      "kind": "theorem",
      "name": "resonance_rational",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/resonance-rational/",
      "source_line_start": 180,
      "source_line_end": 182,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P60"
      ]
    },
    {
      "kind": "theorem",
      "name": "solar_system_single_readout",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/solar-system-single-readout/",
      "source_line_start": 188,
      "source_line_end": 190,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P61"
      ]
    },
    {
      "kind": "inductive",
      "name": "PlanetaryType",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-type/",
      "source_line_start": 193,
      "source_line_end": 202,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "planetary_classification",
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-classification/",
      "source_line_start": 207,
      "source_line_end": 210,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P62"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": [
        "V.R165",
        "V.R166",
        "V.R167",
        "V.R168"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 244,
      "formal_status": "computed",
      "registry_ids": []
    }
  ],
  "right_rail": {
    "related": [
      {
        "title": "TauLib Overview",
        "url": "/verify/taulib/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Module",
      "source": "Corpus projection",
      "commit": "cb5e8301"
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
  "type": "TauLib Module"
}
---

## Corpus TauLib Projection

This page is generated directly from the pinned TauLib Lean source snapshot in `corpus/taulib-sources/project`. It is a Corpus-native module view designed for cross-linking Registry, Construction Spine, Results, and Verify surfaces.

## Source Provenance

- Source repository: `Panta-Rhei-Research/taulib`
- Source commit: [`cb5e8301`](https://github.com/Panta-Rhei-Research/taulib/commit/cb5e83015b54dd72eba560953fe2461820078757)
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`
- SHA-256: `d2d3a4810e724d1966d23645c61fab7169ae3bb11f4c08d1893811609e51470e`

## Registry Links

- `V.D118` — Angular Momentum Character --- V.D51
- `V.D119` — Lensing Character --- V.D52
- `V.P59` — Perihelion Advance from tau-GR --- V.P23
- `V.P60` — Light Deflection from tau-GR --- V.P24
- `V.P61` — Shapiro Delay from tau-GR --- V.P25
- `V.P62` — Solar System Concordance --- V.P26
- `V.R165` — Second law is deeper than the first
- `V.R166` — Kepler as theorem, not phenomenology
- `V.R167` — All three tests pass with zero fitting
- `V.R168` — Heliophysics as readout of H_partial[omega
- `V.T81` — Rotational Flux Conservation --- V.T33
- `V.T82` — Kepler's First Law --- V.T34
- `V.T83` — Kepler's Second Law --- V.T35
- `V.T84` — Kepler's Third Law --- V.T36

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.ClassicalIllusion`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.GalaxyRelational`

## Declaration Counts

- `def`: 2
- `eval`: 4
- `inductive`: 2
- `structure`: 2
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [OrbitType](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/orbit-type/) | L63-L72 | defined | — |
| `structure` | [KeplerOrbitData](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-orbit-data/) | L79-L94 | defined | `V.D118` |
| `def` | [earth_orbit](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/earth-orbit/) | L97-L103 | defined | — |
| `def` | [mercury_orbit](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/mercury-orbit/) | L106-L112 | defined | — |
| `theorem` | [kepler_first_law](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-first-law/) | L121-L123 | formalized | `V.T81` |
| `theorem` | [kepler_second_law](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-second-law/) | L128-L130 | formalized | `V.T82` |
| `theorem` | [kepler_third_law](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-third-law/) | L135-L137 | formalized | `V.T83` |
| `structure` | [TidalForceStructure](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-structure/) | L147-L158 | defined | `V.D119` |
| `theorem` | [tidal_force_gradient](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-gradient/) | L163-L165 | formalized | `V.T84` |
| `theorem` | [orbital_stability](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/orbital-stability/) | L173-L175 | formalized | `V.P59` |
| `theorem` | [resonance_rational](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/resonance-rational/) | L180-L182 | formalized | `V.P60` |
| `theorem` | [solar_system_single_readout](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/solar-system-single-readout/) | L188-L190 | formalized | `V.P61` |
| `inductive` | [PlanetaryType](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-type/) | L193-L202 | defined | — |
| `theorem` | [planetary_classification](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-classification/) | L207-L210 | formalized | `V.P62` |
| `eval` | [#eval L239](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l239/) | L239-L239 | computed | `V.R165`, `V.R166`, `V.R167`, `V.R168` |
| `eval` | [#eval L240](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l240/) | L240-L240 | computed | — |
| `eval` | [#eval L241](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l241/) | L241-L241 | computed | — |
| `eval` | [#eval L242](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l242/) | L242-L244 | computed | — |

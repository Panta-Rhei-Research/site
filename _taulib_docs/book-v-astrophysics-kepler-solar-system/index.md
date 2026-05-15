---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/orbit-type/",
      "source_line_start": 63,
      "source_line_end": 72,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "KeplerOrbitData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-orbit-data/",
      "source_line_start": 79,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D118"
      ]
    },
    {
      "kind": "def",
      "name": "earth_orbit",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/earth-orbit/",
      "source_line_start": 97,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mercury_orbit",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/mercury-orbit/",
      "source_line_start": 106,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kepler_first_law",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-first-law/",
      "source_line_start": 121,
      "source_line_end": 123,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T81"
      ]
    },
    {
      "kind": "theorem",
      "name": "kepler_second_law",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-second-law/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T82"
      ]
    },
    {
      "kind": "theorem",
      "name": "kepler_third_law",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-third-law/",
      "source_line_start": 135,
      "source_line_end": 137,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T83"
      ]
    },
    {
      "kind": "structure",
      "name": "TidalForceStructure",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-structure/",
      "source_line_start": 147,
      "source_line_end": 158,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D119"
      ]
    },
    {
      "kind": "theorem",
      "name": "tidal_force_gradient",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-gradient/",
      "source_line_start": 163,
      "source_line_end": 165,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T84"
      ]
    },
    {
      "kind": "theorem",
      "name": "orbital_stability",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/orbital-stability/",
      "source_line_start": 173,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P59"
      ]
    },
    {
      "kind": "theorem",
      "name": "resonance_rational",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/resonance-rational/",
      "source_line_start": 180,
      "source_line_end": 182,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P60"
      ]
    },
    {
      "kind": "theorem",
      "name": "solar_system_single_readout",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/solar-system-single-readout/",
      "source_line_start": 188,
      "source_line_end": 190,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P61"
      ]
    },
    {
      "kind": "inductive",
      "name": "PlanetaryType",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-type/",
      "source_line_start": 193,
      "source_line_end": 202,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "planetary_classification",
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-classification/",
      "source_line_start": 207,
      "source_line_end": 210,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P62"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 244,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
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
        "url": "/corpus/taulib/docs/"
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [OrbitType](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/orbit-type/) | L63-L72 | type/data schema | type/data schema | — |
| `structure` | [KeplerOrbitData](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-orbit-data/) | L79-L94 | type/data schema | type/data schema | `V.D118` |
| `def` | [earth_orbit](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/earth-orbit/) | L97-L103 | definition | definition | — |
| `def` | [mercury_orbit](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/mercury-orbit/) | L106-L112 | definition | definition | — |
| `theorem` | [kepler_first_law](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-first-law/) | L121-L123 | proof obligation | formal proof obligation checked | `V.T81` |
| `theorem` | [kepler_second_law](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-second-law/) | L128-L130 | proof obligation | formal proof obligation checked | `V.T82` |
| `theorem` | [kepler_third_law](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-third-law/) | L135-L137 | proof obligation | formal proof obligation checked | `V.T83` |
| `structure` | [TidalForceStructure](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-structure/) | L147-L158 | type/data schema | type/data schema | `V.D119` |
| `theorem` | [tidal_force_gradient](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/tidal-force-gradient/) | L163-L165 | proof obligation | formal proof obligation checked | `V.T84` |
| `theorem` | [orbital_stability](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/orbital-stability/) | L173-L175 | proof obligation | formal proof obligation checked | `V.P59` |
| `theorem` | [resonance_rational](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/resonance-rational/) | L180-L182 | proof obligation | formal proof obligation checked | `V.P60` |
| `theorem` | [solar_system_single_readout](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/solar-system-single-readout/) | L188-L190 | proof obligation | formal proof obligation checked | `V.P61` |
| `inductive` | [PlanetaryType](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-type/) | L193-L202 | type/data schema | type/data schema | — |
| `theorem` | [planetary_classification](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-classification/) | L207-L210 | proof obligation | formal proof obligation checked | `V.P62` |
| `eval` | [#eval L239](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l239/) | L239-L239 | computed check | computed check | `V.R165`, `V.R166`, `V.R167`, `V.R168` |
| `eval` | [#eval L240](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l240/) | L240-L240 | computed check | computed check | — |
| `eval` | [#eval L241](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l241/) | L241-L241 | computed check | computed check | — |
| `eval` | [#eval L242](/corpus/taulib/docs/book-v-astrophysics-kepler-solar-system/eval-l242/) | L242-L244 | computed check | computed check | — |

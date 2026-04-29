---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.TauAlfven",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.FluidMacro.TauAlfven`.",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_slug": "book-v-fluid-macro-tau-alfven",
  "book": "BookV",
  "family": "FluidMacro",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/FluidMacro/TauAlfven.lean",
  "sha256": "dc88bf060781080e3d246b27b251ea45eb6d3157fa46e3ff05d7b0b9d83bf404",
  "imports": [
    "TauLib.BookV.FluidMacro.TauMHD"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.FluidMacro.PhaseTransitions"
  ],
  "registry_ids": [
    "V.D111",
    "V.D112",
    "V.D312",
    "V.D313",
    "V.P173",
    "V.P52",
    "V.P53",
    "V.R155",
    "V.R156",
    "V.R445",
    "V.T253"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 8,
    "def": 8,
    "theorem": 6,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "MHDPolarization",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/mhdpolarization/",
      "source_line_start": 67,
      "source_line_end": 74,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenWaveMode",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-wave-mode/",
      "source_line_start": 82,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": [
        "V.D111"
      ]
    },
    {
      "kind": "def",
      "name": "AlfvenWaveMode.speedFloat",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/speed-float/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "shear_is_incompressible",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/shear-is-incompressible/",
      "source_line_start": 102,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenDispersion",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion/",
      "source_line_start": 115,
      "source_line_end": 126,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alfven_dispersion",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion-l136/",
      "source_line_start": 136,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P52"
      ]
    },
    {
      "kind": "structure",
      "name": "MagnetoacousticMode",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-mode/",
      "source_line_start": 149,
      "source_line_end": 168,
      "formal_status": "defined",
      "registry_ids": [
        "V.D112"
      ]
    },
    {
      "kind": "theorem",
      "name": "fast_slow_opposite_phase",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/fast-slow-opposite-phase/",
      "source_line_start": 171,
      "source_line_end": 176,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "AlfvenDampingMechanism",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-mechanism/",
      "source_line_start": 183,
      "source_line_end": 192,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenDamping",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping/",
      "source_line_start": 199,
      "source_line_end": 208,
      "formal_status": "defined",
      "registry_ids": [
        "V.R156"
      ]
    },
    {
      "kind": "theorem",
      "name": "alfven_damping",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-l211/",
      "source_line_start": 211,
      "source_line_end": 212,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MagnetoacousticSynthesis",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis/",
      "source_line_start": 224,
      "source_line_end": 233,
      "formal_status": "defined",
      "registry_ids": [
        "V.P53"
      ]
    },
    {
      "kind": "def",
      "name": "MagnetoacousticSynthesis.totalEnergy",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/total-energy/",
      "source_line_start": 236,
      "source_line_end": 237,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetoacoustic_synthesis",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis-l240/",
      "source_line_start": 240,
      "source_line_end": 244,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenDampingRate",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate/",
      "source_line_start": 256,
      "source_line_end": 263,
      "formal_status": "defined",
      "registry_ids": [
        "V.D312"
      ]
    },
    {
      "kind": "def",
      "name": "alfven_damping_rate_tau",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate-tau/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoronalHeatingFlux",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux/",
      "source_line_start": 279,
      "source_line_end": 288,
      "formal_status": "defined",
      "registry_ids": [
        "V.D313"
      ]
    },
    {
      "kind": "def",
      "name": "coronal_heating_flux",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_alfven_damping_rate",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/tau-alfven-damping-rate/",
      "source_line_start": 303,
      "source_line_end": 306,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T253"
      ]
    },
    {
      "kind": "structure",
      "name": "CoronalFluxConsistency",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency/",
      "source_line_start": 319,
      "source_line_end": 324,
      "formal_status": "defined",
      "registry_ids": [
        "V.P173"
      ]
    },
    {
      "kind": "def",
      "name": "coronal_flux_consistency",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_shear_alfven",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/example-shear-alfven/",
      "source_line_start": 343,
      "source_line_end": 349,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_fast_mode",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/example-fast-mode/",
      "source_line_start": 355,
      "source_line_end": 364,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l366/",
      "source_line_start": 366,
      "source_line_end": 366,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_synthesis",
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/example-synthesis/",
      "source_line_start": 369,
      "source_line_end": 372,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l374/",
      "source_line_start": 374,
      "source_line_end": 376,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean",
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
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/FluidMacro/TauAlfven.lean`
- SHA-256: `dc88bf060781080e3d246b27b251ea45eb6d3157fa46e3ff05d7b0b9d83bf404`

## Registry Links

- `V.D111` — Mixed-sector mode
- `V.D112` — Alfv'en orbit
- `V.D312` — Alfvén Damping Rate
- `V.D313` — Coronal Heating Flux
- `V.P173` — Coronal Flux Consistency
- `V.P52` — Alfv'en speed as cross-coupling readout
- `V.P53` — ISM Alfv'en cascade
- `V.R155` — The photon-in-fluid interpretation
- `V.R156` — Sufficient energy flux
- `V.R445` — Parker Solar Probe Testability
- `V.T253` — τ-Alfvén Damping = ι_τ² ω

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.FluidMacro.TauMHD`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.FluidMacro.PhaseTransitions`

## Declaration Counts

- `def`: 8
- `eval`: 4
- `inductive`: 2
- `structure`: 8
- `theorem`: 6

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [MHDPolarization](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/mhdpolarization/) | L67-L74 | defined | — |
| `structure` | [AlfvenWaveMode](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-wave-mode/) | L82-L95 | defined | `V.D111` |
| `def` | [AlfvenWaveMode.speedFloat](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/speed-float/) | L98-L99 | defined | — |
| `theorem` | [shear_is_incompressible](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/shear-is-incompressible/) | L102-L105 | formalized | — |
| `structure` | [AlfvenDispersion](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion/) | L115-L126 | defined | — |
| `theorem` | [alfven_dispersion](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion-l136/) | L136-L138 | formalized | `V.P52` |
| `structure` | [MagnetoacousticMode](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-mode/) | L149-L168 | defined | `V.D112` |
| `theorem` | [fast_slow_opposite_phase](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/fast-slow-opposite-phase/) | L171-L176 | formalized | — |
| `inductive` | [AlfvenDampingMechanism](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-mechanism/) | L183-L192 | defined | — |
| `structure` | [AlfvenDamping](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping/) | L199-L208 | defined | `V.R156` |
| `theorem` | [alfven_damping](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-l211/) | L211-L212 | formalized | — |
| `structure` | [MagnetoacousticSynthesis](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis/) | L224-L233 | defined | `V.P53` |
| `def` | [MagnetoacousticSynthesis.totalEnergy](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/total-energy/) | L236-L237 | defined | — |
| `theorem` | [magnetoacoustic_synthesis](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis-l240/) | L240-L244 | formalized | — |
| `structure` | [AlfvenDampingRate](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate/) | L256-L263 | defined | `V.D312` |
| `def` | [alfven_damping_rate_tau](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate-tau/) | L266-L266 | defined | — |
| `structure` | [CoronalHeatingFlux](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux/) | L279-L288 | defined | `V.D313` |
| `def` | [coronal_heating_flux](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux-l291/) | L291-L291 | defined | — |
| `theorem` | [tau_alfven_damping_rate](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/tau-alfven-damping-rate/) | L303-L306 | formalized | `V.T253` |
| `structure` | [CoronalFluxConsistency](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency/) | L319-L324 | defined | `V.P173` |
| `def` | [coronal_flux_consistency](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency-l327/) | L327-L327 | defined | — |
| `def` | [example_shear_alfven](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/example-shear-alfven/) | L343-L349 | defined | — |
| `eval` | [#eval L351](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l351/) | L351-L351 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l352/) | L352-L352 | computed | — |
| `def` | [example_fast_mode](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/example-fast-mode/) | L355-L364 | defined | — |
| `eval` | [#eval L366](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l366/) | L366-L366 | computed | — |
| `def` | [example_synthesis](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/example-synthesis/) | L369-L372 | defined | — |
| `eval` | [#eval L374](/verify/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l374/) | L374-L376 | computed | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.TauAlfven",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/",
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
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/mhdpolarization/",
      "source_line_start": 67,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenWaveMode",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-wave-mode/",
      "source_line_start": 82,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D111"
      ]
    },
    {
      "kind": "def",
      "name": "AlfvenWaveMode.speedFloat",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/speed-float/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "shear_is_incompressible",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/shear-is-incompressible/",
      "source_line_start": 102,
      "source_line_end": 105,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenDispersion",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion/",
      "source_line_start": 115,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alfven_dispersion",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion-l136/",
      "source_line_start": 136,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P52"
      ]
    },
    {
      "kind": "structure",
      "name": "MagnetoacousticMode",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-mode/",
      "source_line_start": 149,
      "source_line_end": 168,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D112"
      ]
    },
    {
      "kind": "theorem",
      "name": "fast_slow_opposite_phase",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/fast-slow-opposite-phase/",
      "source_line_start": 171,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "AlfvenDampingMechanism",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-mechanism/",
      "source_line_start": 183,
      "source_line_end": 192,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenDamping",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping/",
      "source_line_start": 199,
      "source_line_end": 208,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R156"
      ]
    },
    {
      "kind": "theorem",
      "name": "alfven_damping",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-l211/",
      "source_line_start": 211,
      "source_line_end": 212,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MagnetoacousticSynthesis",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis/",
      "source_line_start": 224,
      "source_line_end": 233,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P53"
      ]
    },
    {
      "kind": "def",
      "name": "MagnetoacousticSynthesis.totalEnergy",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/total-energy/",
      "source_line_start": 236,
      "source_line_end": 237,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetoacoustic_synthesis",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis-l240/",
      "source_line_start": 240,
      "source_line_end": 244,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlfvenDampingRate",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate/",
      "source_line_start": 256,
      "source_line_end": 263,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D312"
      ]
    },
    {
      "kind": "def",
      "name": "alfven_damping_rate_tau",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate-tau/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoronalHeatingFlux",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux/",
      "source_line_start": 279,
      "source_line_end": 288,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D313"
      ]
    },
    {
      "kind": "def",
      "name": "coronal_heating_flux",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_alfven_damping_rate",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/tau-alfven-damping-rate/",
      "source_line_start": 303,
      "source_line_end": 306,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T253"
      ]
    },
    {
      "kind": "structure",
      "name": "CoronalFluxConsistency",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency/",
      "source_line_start": 319,
      "source_line_end": 324,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P173"
      ]
    },
    {
      "kind": "def",
      "name": "coronal_flux_consistency",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_shear_alfven",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/example-shear-alfven/",
      "source_line_start": 343,
      "source_line_end": 349,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l351/",
      "source_line_start": 351,
      "source_line_end": 351,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_fast_mode",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/example-fast-mode/",
      "source_line_start": 355,
      "source_line_end": 364,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l366/",
      "source_line_start": 366,
      "source_line_end": 366,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_synthesis",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/example-synthesis/",
      "source_line_start": 369,
      "source_line_end": 372,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l374/",
      "source_line_start": 374,
      "source_line_end": 376,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [MHDPolarization](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/mhdpolarization/) | L67-L74 | type/data schema | type/data schema | — |
| `structure` | [AlfvenWaveMode](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-wave-mode/) | L82-L95 | type/data schema | type/data schema | `V.D111` |
| `def` | [AlfvenWaveMode.speedFloat](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/speed-float/) | L98-L99 | data/computed value | data/computed value | — |
| `theorem` | [shear_is_incompressible](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/shear-is-incompressible/) | L102-L105 | proof obligation | formal proof obligation checked | — |
| `structure` | [AlfvenDispersion](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion/) | L115-L126 | type/data schema | type/data schema | — |
| `theorem` | [alfven_dispersion](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-dispersion-l136/) | L136-L138 | proof obligation | formal proof obligation checked | `V.P52` |
| `structure` | [MagnetoacousticMode](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-mode/) | L149-L168 | type/data schema | type/data schema | `V.D112` |
| `theorem` | [fast_slow_opposite_phase](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/fast-slow-opposite-phase/) | L171-L176 | proof obligation | formal proof obligation checked | — |
| `inductive` | [AlfvenDampingMechanism](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-mechanism/) | L183-L192 | type/data schema | type/data schema | — |
| `structure` | [AlfvenDamping](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping/) | L199-L208 | type/data schema | type/data schema | `V.R156` |
| `theorem` | [alfven_damping](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-l211/) | L211-L212 | proof obligation | formal proof obligation checked | — |
| `structure` | [MagnetoacousticSynthesis](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis/) | L224-L233 | type/data schema | type/data schema | `V.P53` |
| `def` | [MagnetoacousticSynthesis.totalEnergy](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/total-energy/) | L236-L237 | data/computed value | data/computed value | — |
| `theorem` | [magnetoacoustic_synthesis](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/magnetoacoustic-synthesis-l240/) | L240-L244 | proof obligation | formal proof obligation checked | — |
| `structure` | [AlfvenDampingRate](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate/) | L256-L263 | type/data schema | type/data schema | `V.D312` |
| `def` | [alfven_damping_rate_tau](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-rate-tau/) | L266-L266 | definition | definition | — |
| `structure` | [CoronalHeatingFlux](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux/) | L279-L288 | type/data schema | type/data schema | `V.D313` |
| `def` | [coronal_heating_flux](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-heating-flux-l291/) | L291-L291 | definition | definition | — |
| `theorem` | [tau_alfven_damping_rate](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/tau-alfven-damping-rate/) | L303-L306 | proof obligation | formal proof obligation checked | `V.T253` |
| `structure` | [CoronalFluxConsistency](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency/) | L319-L324 | type/data schema | type/data schema | `V.P173` |
| `def` | [coronal_flux_consistency](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/coronal-flux-consistency-l327/) | L327-L327 | definition | definition | — |
| `def` | [example_shear_alfven](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/example-shear-alfven/) | L343-L349 | definition | definition | — |
| `eval` | [#eval L351](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l351/) | L351-L351 | computed check | computed check | — |
| `eval` | [#eval L352](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l352/) | L352-L352 | computed check | computed check | — |
| `def` | [example_fast_mode](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/example-fast-mode/) | L355-L364 | definition | definition | — |
| `eval` | [#eval L366](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l366/) | L366-L366 | computed check | computed check | — |
| `def` | [example_synthesis](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/example-synthesis/) | L369-L372 | definition | definition | — |
| `eval` | [#eval L374](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/eval-l374/) | L374-L376 | computed check | computed check | — |

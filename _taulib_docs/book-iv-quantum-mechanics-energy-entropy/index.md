---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.QuantumMechanics.EnergyEntropy`.",
  "module_name": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "module_slug": "book-iv-quantum-mechanics-energy-entropy",
  "book": "BookIV",
  "family": "QuantumMechanics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean",
  "sha256": "b00362f5c4e2251a71589dd83a6782517a997c492458d8110877c44dd69dfe56",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.Measurement",
    "TauLib.BookIV.Physics.Thermodynamics"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.PhotonMode",
    "TauLib.BookIV.MassDerivation.BreathingModes"
  ],
  "registry_ids": [
    "IV.D76",
    "IV.D77",
    "IV.D78",
    "IV.D79",
    "IV.D80",
    "IV.D81",
    "IV.P29",
    "IV.P30",
    "IV.P31",
    "IV.T29",
    "IV.T30",
    "IV.T31",
    "IV.T32"
  ],
  "declaration_counts": {
    "structure": 13,
    "def": 4,
    "theorem": 7,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "HolomorphicTension",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/holomorphic-tension/",
      "source_line_start": 39,
      "source_line_end": 43,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D76"
      ]
    },
    {
      "kind": "def",
      "name": "HolomorphicTension.toFloat",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float/",
      "source_line_start": 45,
      "source_line_end": 46,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GraphEnergyDensity",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/graph-energy-density/",
      "source_line_start": 53,
      "source_line_end": 58,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D77"
      ]
    },
    {
      "kind": "def",
      "name": "GraphEnergyDensity.toFloat",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l60/",
      "source_line_start": 60,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LocalizationBound",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-bound/",
      "source_line_start": 68,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P29"
      ]
    },
    {
      "kind": "theorem",
      "name": "localization_energy_bound",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-energy-bound/",
      "source_line_start": 77,
      "source_line_end": 78,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MassFromEigenvalue",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/mass-from-eigenvalue/",
      "source_line_start": 85,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D78"
      ]
    },
    {
      "kind": "structure",
      "name": "FrequencyFromEigenvalue",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/frequency-from-eigenvalue/",
      "source_line_start": 93,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D79"
      ]
    },
    {
      "kind": "structure",
      "name": "DualReading",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading/",
      "source_line_start": 107,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T29"
      ]
    },
    {
      "kind": "theorem",
      "name": "dual_reading",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading-l115/",
      "source_line_start": 115,
      "source_line_end": 116,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EnergyConservation",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation/",
      "source_line_start": 123,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T30"
      ]
    },
    {
      "kind": "theorem",
      "name": "energy_conservation",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation-l132/",
      "source_line_start": 132,
      "source_line_end": 134,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CREntropy",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/crentropy/",
      "source_line_start": 142,
      "source_line_end": 147,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D80"
      ]
    },
    {
      "kind": "def",
      "name": "CREntropy.toFloat",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l149/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EntropyBoundData",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound-data/",
      "source_line_start": 157,
      "source_line_end": 161,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P30"
      ]
    },
    {
      "kind": "theorem",
      "name": "entropy_bound",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound/",
      "source_line_start": 163,
      "source_line_end": 164,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TemporalDirection",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/temporal-direction/",
      "source_line_start": 171,
      "source_line_end": 175,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D81"
      ]
    },
    {
      "kind": "structure",
      "name": "EntropyMonotonicity",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-monotonicity/",
      "source_line_start": 178,
      "source_line_end": 184,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T31"
      ]
    },
    {
      "kind": "theorem",
      "name": "entropy_nondecreasing",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-nondecreasing/",
      "source_line_start": 186,
      "source_line_end": 189,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ArrowOfTime",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time/",
      "source_line_start": 192,
      "source_line_end": 198,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T32"
      ]
    },
    {
      "kind": "theorem",
      "name": "arrow_of_time",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time-l200/",
      "source_line_start": 200,
      "source_line_end": 202,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WithinBetweenLevels",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-between-levels/",
      "source_line_start": 210,
      "source_line_end": 213,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P31"
      ]
    },
    {
      "kind": "theorem",
      "name": "within_vs_between",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-vs-between/",
      "source_line_start": 215,
      "source_line_end": 219,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l225/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l227/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l228/",
      "source_line_start": 228,
      "source_line_end": 229,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l230/",
      "source_line_start": 230,
      "source_line_end": 230,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_within_between",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/example-within-between/",
      "source_line_start": 231,
      "source_line_end": 231,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l232/",
      "source_line_start": 232,
      "source_line_end": 234,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/QuantumMechanics/EnergyEntropy.lean`
- SHA-256: `b00362f5c4e2251a71589dd83a6782517a997c492458d8110877c44dd69dfe56`

## Registry Links

- `IV.D76` — Energy as CR-Tension
- `IV.D77` — Graph Energy Density
- `IV.D78` — Mass as Fiber Stiffness
- `IV.D79` — Frequency as Base Circulation
- `IV.D80` — Holomorphic Entropy
- `IV.D81` — Temporal Direction
- `IV.P29` — Energy-Localization Bound
- `IV.P30` — Entropy-Mode-Count Bound
- `IV.P31` — Reversibility-Irreversibility Resolution
- `IV.T29` — Energy Duality
- `IV.T30` — Energy Conservation
- `IV.T31` — Second Law of Thermodynamics
- `IV.T32` — Structural Arrow of Time

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.Measurement`
- `TauLib.BookIV.Physics.Thermodynamics`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.PhotonMode`
- `TauLib.BookIV.MassDerivation.BreathingModes`

## Declaration Counts

- `def`: 4
- `eval`: 6
- `structure`: 13
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [HolomorphicTension](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/holomorphic-tension/) | L39-L43 | type/data schema | type/data schema | `IV.D76` |
| `def` | [HolomorphicTension.toFloat](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float/) | L45-L46 | data/computed value | data/computed value | — |
| `structure` | [GraphEnergyDensity](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/graph-energy-density/) | L53-L58 | type/data schema | type/data schema | `IV.D77` |
| `def` | [GraphEnergyDensity.toFloat](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l60/) | L60-L61 | data/computed value | data/computed value | — |
| `structure` | [LocalizationBound](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-bound/) | L68-L75 | type/data schema | type/data schema | `IV.P29` |
| `theorem` | [localization_energy_bound](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-energy-bound/) | L77-L78 | proof obligation | formal proof obligation checked | — |
| `structure` | [MassFromEigenvalue](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/mass-from-eigenvalue/) | L85-L90 | type/data schema | type/data schema | `IV.D78` |
| `structure` | [FrequencyFromEigenvalue](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/frequency-from-eigenvalue/) | L93-L98 | type/data schema | type/data schema | `IV.D79` |
| `structure` | [DualReading](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading/) | L107-L113 | type/data schema | type/data schema | `IV.T29` |
| `theorem` | [dual_reading](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading-l115/) | L115-L116 | proof obligation | formal proof obligation checked | — |
| `structure` | [EnergyConservation](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation/) | L123-L130 | type/data schema | type/data schema | `IV.T30` |
| `theorem` | [energy_conservation](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation-l132/) | L132-L134 | proof obligation | formal proof obligation checked | — |
| `structure` | [CREntropy](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/crentropy/) | L142-L147 | type/data schema | type/data schema | `IV.D80` |
| `def` | [CREntropy.toFloat](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l149/) | L149-L150 | data/computed value | data/computed value | — |
| `structure` | [EntropyBoundData](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound-data/) | L157-L161 | type/data schema | type/data schema | `IV.P30` |
| `theorem` | [entropy_bound](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound/) | L163-L164 | proof obligation | formal proof obligation checked | — |
| `structure` | [TemporalDirection](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/temporal-direction/) | L171-L175 | type/data schema | type/data schema | `IV.D81` |
| `structure` | [EntropyMonotonicity](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-monotonicity/) | L178-L184 | type/data schema | type/data schema | `IV.T31` |
| `theorem` | [entropy_nondecreasing](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-nondecreasing/) | L186-L189 | proof obligation | formal proof obligation checked | — |
| `structure` | [ArrowOfTime](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time/) | L192-L198 | type/data schema | type/data schema | `IV.T32` |
| `theorem` | [arrow_of_time](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time-l200/) | L200-L202 | proof obligation | formal proof obligation checked | — |
| `structure` | [WithinBetweenLevels](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-between-levels/) | L210-L213 | type/data schema | type/data schema | `IV.P31` |
| `theorem` | [within_vs_between](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-vs-between/) | L215-L219 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L225](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l225/) | L225-L225 | computed check | computed check | — |
| `eval` | [#eval L226](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l226/) | L226-L226 | computed check | computed check | — |
| `eval` | [#eval L227](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l227/) | L227-L227 | computed check | computed check | — |
| `eval` | [#eval L228](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l228/) | L228-L229 | computed check | computed check | — |
| `eval` | [#eval L230](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l230/) | L230-L230 | computed check | computed check | — |
| `def` | [example_within_between](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/example-within-between/) | L231-L231 | definition | definition | — |
| `eval` | [#eval L232](/corpus/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l232/) | L232-L234 | computed check | computed check | — |

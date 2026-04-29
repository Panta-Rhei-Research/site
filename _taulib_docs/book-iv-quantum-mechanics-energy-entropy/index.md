---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.EnergyEntropy",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/",
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
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/holomorphic-tension/",
      "source_line_start": 39,
      "source_line_end": 43,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D76"
      ]
    },
    {
      "kind": "def",
      "name": "HolomorphicTension.toFloat",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float/",
      "source_line_start": 45,
      "source_line_end": 46,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GraphEnergyDensity",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/graph-energy-density/",
      "source_line_start": 53,
      "source_line_end": 58,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D77"
      ]
    },
    {
      "kind": "def",
      "name": "GraphEnergyDensity.toFloat",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l60/",
      "source_line_start": 60,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LocalizationBound",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-bound/",
      "source_line_start": 68,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P29"
      ]
    },
    {
      "kind": "theorem",
      "name": "localization_energy_bound",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-energy-bound/",
      "source_line_start": 77,
      "source_line_end": 78,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MassFromEigenvalue",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/mass-from-eigenvalue/",
      "source_line_start": 85,
      "source_line_end": 90,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D78"
      ]
    },
    {
      "kind": "structure",
      "name": "FrequencyFromEigenvalue",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/frequency-from-eigenvalue/",
      "source_line_start": 93,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D79"
      ]
    },
    {
      "kind": "structure",
      "name": "DualReading",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading/",
      "source_line_start": 107,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T29"
      ]
    },
    {
      "kind": "theorem",
      "name": "dual_reading",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading-l115/",
      "source_line_start": 115,
      "source_line_end": 116,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EnergyConservation",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation/",
      "source_line_start": 123,
      "source_line_end": 130,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T30"
      ]
    },
    {
      "kind": "theorem",
      "name": "energy_conservation",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation-l132/",
      "source_line_start": 132,
      "source_line_end": 134,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CREntropy",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/crentropy/",
      "source_line_start": 142,
      "source_line_end": 147,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D80"
      ]
    },
    {
      "kind": "def",
      "name": "CREntropy.toFloat",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l149/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EntropyBoundData",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound-data/",
      "source_line_start": 157,
      "source_line_end": 161,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P30"
      ]
    },
    {
      "kind": "theorem",
      "name": "entropy_bound",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound/",
      "source_line_start": 163,
      "source_line_end": 164,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TemporalDirection",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/temporal-direction/",
      "source_line_start": 171,
      "source_line_end": 175,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D81"
      ]
    },
    {
      "kind": "structure",
      "name": "EntropyMonotonicity",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-monotonicity/",
      "source_line_start": 178,
      "source_line_end": 184,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T31"
      ]
    },
    {
      "kind": "theorem",
      "name": "entropy_nondecreasing",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-nondecreasing/",
      "source_line_start": 186,
      "source_line_end": 189,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ArrowOfTime",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time/",
      "source_line_start": 192,
      "source_line_end": 198,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T32"
      ]
    },
    {
      "kind": "theorem",
      "name": "arrow_of_time",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time-l200/",
      "source_line_start": 200,
      "source_line_end": 202,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WithinBetweenLevels",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-between-levels/",
      "source_line_start": 210,
      "source_line_end": 213,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P31"
      ]
    },
    {
      "kind": "theorem",
      "name": "within_vs_between",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-vs-between/",
      "source_line_start": 215,
      "source_line_end": 219,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l225/",
      "source_line_start": 225,
      "source_line_end": 225,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l227/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l228/",
      "source_line_start": 228,
      "source_line_end": 229,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l230/",
      "source_line_start": 230,
      "source_line_end": 230,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_within_between",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/example-within-between/",
      "source_line_start": 231,
      "source_line_end": 231,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l232/",
      "source_line_start": 232,
      "source_line_end": 234,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [HolomorphicTension](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/holomorphic-tension/) | L39-L43 | defined | `IV.D76` |
| `def` | [HolomorphicTension.toFloat](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float/) | L45-L46 | defined | — |
| `structure` | [GraphEnergyDensity](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/graph-energy-density/) | L53-L58 | defined | `IV.D77` |
| `def` | [GraphEnergyDensity.toFloat](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l60/) | L60-L61 | defined | — |
| `structure` | [LocalizationBound](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-bound/) | L68-L75 | defined | `IV.P29` |
| `theorem` | [localization_energy_bound](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/localization-energy-bound/) | L77-L78 | formalized | — |
| `structure` | [MassFromEigenvalue](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/mass-from-eigenvalue/) | L85-L90 | defined | `IV.D78` |
| `structure` | [FrequencyFromEigenvalue](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/frequency-from-eigenvalue/) | L93-L98 | defined | `IV.D79` |
| `structure` | [DualReading](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading/) | L107-L113 | defined | `IV.T29` |
| `theorem` | [dual_reading](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/dual-reading-l115/) | L115-L116 | formalized | — |
| `structure` | [EnergyConservation](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation/) | L123-L130 | defined | `IV.T30` |
| `theorem` | [energy_conservation](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/energy-conservation-l132/) | L132-L134 | formalized | — |
| `structure` | [CREntropy](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/crentropy/) | L142-L147 | defined | `IV.D80` |
| `def` | [CREntropy.toFloat](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/to-float-l149/) | L149-L150 | defined | — |
| `structure` | [EntropyBoundData](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound-data/) | L157-L161 | defined | `IV.P30` |
| `theorem` | [entropy_bound](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-bound/) | L163-L164 | formalized | — |
| `structure` | [TemporalDirection](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/temporal-direction/) | L171-L175 | defined | `IV.D81` |
| `structure` | [EntropyMonotonicity](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-monotonicity/) | L178-L184 | defined | `IV.T31` |
| `theorem` | [entropy_nondecreasing](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/entropy-nondecreasing/) | L186-L189 | formalized | — |
| `structure` | [ArrowOfTime](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time/) | L192-L198 | defined | `IV.T32` |
| `theorem` | [arrow_of_time](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/arrow-of-time-l200/) | L200-L202 | formalized | — |
| `structure` | [WithinBetweenLevels](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-between-levels/) | L210-L213 | defined | `IV.P31` |
| `theorem` | [within_vs_between](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/within-vs-between/) | L215-L219 | formalized | — |
| `eval` | [#eval L225](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l225/) | L225-L225 | computed | — |
| `eval` | [#eval L226](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l226/) | L226-L226 | computed | — |
| `eval` | [#eval L227](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l227/) | L227-L227 | computed | — |
| `eval` | [#eval L228](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l228/) | L228-L229 | computed | — |
| `eval` | [#eval L230](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l230/) | L230-L230 | computed | — |
| `def` | [example_within_between](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/example-within-between/) | L231-L231 | defined | — |
| `eval` | [#eval L232](/verify/taulib/docs/book-iv-quantum-mechanics-energy-entropy/eval-l232/) | L232-L234 | computed | — |

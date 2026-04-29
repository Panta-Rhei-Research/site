---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.QuantumMechanics.QuantumCharacters`.",
  "module_name": "TauLib.BookIV.QuantumMechanics.QuantumCharacters",
  "module_slug": "book-iv-quantum-mechanics-quantum-characters",
  "book": "BookIV",
  "family": "QuantumMechanics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean",
  "sha256": "5b9e4bb84a71a670dcdfa2761300786e25052ed05064c76c2e8e81454c35c2b9",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
    "TauLib.BookIV.Physics.PlanckCharacter"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.QuantumMechanics.HilbertSpace"
  ],
  "registry_ids": [
    "IV.D55",
    "IV.D56",
    "IV.D57",
    "IV.D58",
    "IV.D59",
    "IV.P11",
    "IV.P12",
    "IV.P13",
    "IV.P14",
    "IV.P15",
    "IV.R14",
    "IV.R15"
  ],
  "declaration_counts": {
    "structure": 6,
    "def": 3,
    "theorem": 5,
    "inductive": 1,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "SpaceCharacter",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/space-character/",
      "source_line_start": 43,
      "source_line_end": 50,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D55"
      ]
    },
    {
      "kind": "def",
      "name": "characters_on_torus",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/characters-on-torus/",
      "source_line_start": 58,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P11"
      ]
    },
    {
      "kind": "theorem",
      "name": "characters_determined_by_pair",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/characters-determined-by-pair/",
      "source_line_start": 64,
      "source_line_end": 65,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FiberCharacter",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/fiber-character/",
      "source_line_start": 77,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D56"
      ]
    },
    {
      "kind": "structure",
      "name": "CharacterVariety",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/character-variety/",
      "source_line_start": 87,
      "source_line_end": 94,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D56"
      ]
    },
    {
      "kind": "def",
      "name": "char_variety",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/char-variety/",
      "source_line_start": 97,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "automatic_quantization",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/automatic-quantization/",
      "source_line_start": 110,
      "source_line_end": 111,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P12"
      ]
    },
    {
      "kind": "structure",
      "name": "CharacterPrecision",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/character-precision/",
      "source_line_start": 120,
      "source_line_end": 131,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D57"
      ]
    },
    {
      "kind": "structure",
      "name": "GeometricCharge",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/geometric-charge/",
      "source_line_start": 140,
      "source_line_end": 147,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D58"
      ]
    },
    {
      "kind": "def",
      "name": "unit_charge",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/unit-charge/",
      "source_line_start": 150,
      "source_line_end": 153,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "charge_quantized",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/charge-quantized/",
      "source_line_start": 163,
      "source_line_end": 165,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P13"
      ]
    },
    {
      "kind": "structure",
      "name": "EnergyDuality",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/energy-duality/",
      "source_line_start": 180,
      "source_line_end": 194,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P14"
      ]
    },
    {
      "kind": "theorem",
      "name": "energy_duality",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/energy-duality-l197/",
      "source_line_start": 197,
      "source_line_end": 199,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "StateSharpness",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/state-sharpness/",
      "source_line_start": 207,
      "source_line_end": 212,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D59"
      ]
    },
    {
      "kind": "theorem",
      "name": "conjugate_tradeoff",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/conjugate-tradeoff/",
      "source_line_start": 223,
      "source_line_end": 228,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P15"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "computed",
      "registry_ids": [
        "IV.R15"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l244/",
      "source_line_start": 244,
      "source_line_end": 244,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l245/",
      "source_line_start": 245,
      "source_line_end": 245,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 248,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/QuantumMechanics/QuantumCharacters.lean`
- SHA-256: `5b9e4bb84a71a670dcdfa2761300786e25052ed05064c76c2e8e81454c35c2b9`

## Registry Links

- `IV.D55` — Character on a Space
- `IV.D56` — Character Variety of T²
- `IV.D57` — Address Precision (ch17)
- `IV.D58` — Geometric Charge
- `IV.D59` — Sharp and Spread States
- `IV.P11` — Characters on T²
- `IV.P12` — Automatic Quantization
- `IV.P13` — Charge Quantization from Winding
- `IV.P14` — Energy Duality
- `IV.P15` — Conjugate Precision Trade-off
- `IV.R14` — Fractional Charges and Confinement
- `IV.R15` — Quasi-Ergodic Coverage

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.CRAddressSpace`
- `TauLib.BookIV.Physics.PlanckCharacter`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.QuantumMechanics.HilbertSpace`

## Declaration Counts

- `def`: 3
- `eval`: 7
- `inductive`: 1
- `structure`: 6
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [SpaceCharacter](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/space-character/) | L43-L50 | defined | `IV.D55` |
| `def` | [characters_on_torus](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/characters-on-torus/) | L58-L61 | defined | `IV.P11` |
| `theorem` | [characters_determined_by_pair](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/characters-determined-by-pair/) | L64-L65 | formalized | — |
| `structure` | [FiberCharacter](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/fiber-character/) | L77-L84 | defined | `IV.D56` |
| `structure` | [CharacterVariety](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/character-variety/) | L87-L94 | defined | `IV.D56` |
| `def` | [char_variety](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/char-variety/) | L97-L101 | defined | — |
| `theorem` | [automatic_quantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/automatic-quantization/) | L110-L111 | formalized | `IV.P12` |
| `structure` | [CharacterPrecision](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/character-precision/) | L120-L131 | defined | `IV.D57` |
| `structure` | [GeometricCharge](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/geometric-charge/) | L140-L147 | defined | `IV.D58` |
| `def` | [unit_charge](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/unit-charge/) | L150-L153 | defined | — |
| `theorem` | [charge_quantized](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/charge-quantized/) | L163-L165 | formalized | `IV.P13` |
| `structure` | [EnergyDuality](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/energy-duality/) | L180-L194 | defined | `IV.P14` |
| `theorem` | [energy_duality](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/energy-duality-l197/) | L197-L199 | formalized | — |
| `inductive` | [StateSharpness](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/state-sharpness/) | L207-L212 | defined | `IV.D59` |
| `theorem` | [conjugate_tradeoff](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/conjugate-tradeoff/) | L223-L228 | formalized | `IV.P15` |
| `eval` | [#eval L238](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l238/) | L238-L238 | computed | `IV.R15` |
| `eval` | [#eval L239](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l239/) | L239-L239 | computed | — |
| `eval` | [#eval L240](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l240/) | L240-L240 | computed | — |
| `eval` | [#eval L241](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l241/) | L241-L241 | computed | — |
| `eval` | [#eval L244](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l244/) | L244-L244 | computed | — |
| `eval` | [#eval L245](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l245/) | L245-L245 | computed | — |
| `eval` | [#eval L246](/verify/taulib/docs/book-iv-quantum-mechanics-quantum-characters/eval-l246/) | L246-L248 | computed | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.QuantumMechanics.AddressObstruction`.",
  "module_name": "TauLib.BookIV.QuantumMechanics.AddressObstruction",
  "module_slug": "book-iv-quantum-mechanics-address-obstruction",
  "book": "BookIV",
  "family": "QuantumMechanics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean",
  "sha256": "ad0671a3395d9678c6fa3cb064242d692f4cb9af6d154ee808299655bfab0be5",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.Quantization"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.QuantumMechanics.Measurement"
  ],
  "registry_ids": [
    "IV.D68",
    "IV.D69",
    "IV.D70",
    "IV.D71",
    "IV.D72",
    "IV.D73",
    "IV.P25",
    "IV.R316",
    "IV.R318",
    "IV.R320",
    "IV.T22",
    "IV.T23",
    "IV.T24",
    "IV.T25",
    "IV.T26"
  ],
  "declaration_counts": {
    "structure": 10,
    "theorem": 5,
    "def": 4,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PositionUncertainty",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/position-uncertainty/",
      "source_line_start": 44,
      "source_line_end": 53,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D68"
      ]
    },
    {
      "kind": "structure",
      "name": "MomentumUncertainty",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/momentum-uncertainty/",
      "source_line_start": 57,
      "source_line_end": 66,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "JointAddressNF",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/joint-address-nf/",
      "source_line_start": 76,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D69"
      ]
    },
    {
      "kind": "structure",
      "name": "PhaseTransportWitness",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/phase-transport-witness/",
      "source_line_start": 96,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D70"
      ]
    },
    {
      "kind": "structure",
      "name": "ClopenLocalization",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/clopen-localization/",
      "source_line_start": 114,
      "source_line_end": 123,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D71"
      ]
    },
    {
      "kind": "theorem",
      "name": "phase_transport_monotone",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/phase-transport-monotone/",
      "source_line_start": 133,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T22"
      ]
    },
    {
      "kind": "structure",
      "name": "NoJointMinimum",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/no-joint-minimum/",
      "source_line_start": 156,
      "source_line_end": 168,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T23"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_joint_minimum",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/no-joint-minimum-l171/",
      "source_line_start": 171,
      "source_line_end": 174,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CrossingMediator",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/crossing-mediator/",
      "source_line_start": 183,
      "source_line_end": 196,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D72"
      ]
    },
    {
      "kind": "def",
      "name": "crossing_mediator",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/crossing-mediator-l199/",
      "source_line_start": 199,
      "source_line_end": 206,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "planck_uniqueness",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/planck-uniqueness/",
      "source_line_start": 216,
      "source_line_end": 221,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T24"
      ]
    },
    {
      "kind": "structure",
      "name": "SaturationState",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-state/",
      "source_line_start": 231,
      "source_line_end": 243,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D73"
      ]
    },
    {
      "kind": "def",
      "name": "saturation_state",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-state-l246/",
      "source_line_start": 246,
      "source_line_end": 252,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "saturation_achieves_equality",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-achieves-equality/",
      "source_line_start": 260,
      "source_line_end": 262,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P25"
      ]
    },
    {
      "kind": "structure",
      "name": "HeisenbergXP",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-xp/",
      "source_line_start": 279,
      "source_line_end": 292,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T25"
      ]
    },
    {
      "kind": "def",
      "name": "heisenberg_xp",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-xp-l295/",
      "source_line_start": 295,
      "source_line_end": 303,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HeisenbergTE",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-te/",
      "source_line_start": 315,
      "source_line_end": 325,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T26"
      ]
    },
    {
      "kind": "def",
      "name": "heisenberg_te",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-te-l328/",
      "source_line_start": 328,
      "source_line_end": 333,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "uncertainty_bound_universal",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/uncertainty-bound-universal/",
      "source_line_start": 336,
      "source_line_end": 339,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l360/",
      "source_line_start": 360,
      "source_line_end": 360,
      "formal_status": "computed",
      "registry_ids": [
        "IV.R316",
        "IV.R318",
        "IV.R320"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l361/",
      "source_line_start": 361,
      "source_line_end": 361,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l362/",
      "source_line_start": 362,
      "source_line_end": 362,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l363/",
      "source_line_start": 363,
      "source_line_end": 363,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l364/",
      "source_line_start": 364,
      "source_line_end": 364,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l365/",
      "source_line_start": 365,
      "source_line_end": 365,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l366/",
      "source_line_start": 366,
      "source_line_end": 366,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l367/",
      "source_line_start": 367,
      "source_line_end": 367,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l368/",
      "source_line_start": 368,
      "source_line_end": 368,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l369/",
      "source_line_start": 369,
      "source_line_end": 371,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/QuantumMechanics/AddressObstruction.lean`
- SHA-256: `ad0671a3395d9678c6fa3cb064242d692f4cb9af6d154ee808299655bfab0be5`

## Registry Links

- `IV.D68` — Address Uncertainty
- `IV.D69` — τ-Normal Form for Joint Address
- `IV.D70` — Phase Transport Witness
- `IV.D71` — Clopen Position Localization
- `IV.D72` — σ-Equivariant Crossing-Point Mediator
- `IV.D73` — Canonical Saturation State
- `IV.P25` — Saturation Equality
- `IV.R316` — The mechanism in plain language
- `IV.R318` — Boundary witness budget
- `IV.R320` — Physical interpretation
- `IV.T22` — Phase Transport Monotonicity
- `IV.T23` — No-Joint-Minimum Theorem
- `IV.T24` — Planck Character Uniqueness
- `IV.T25` — Heisenberg Uncertainty (Position-Momentum)
- `IV.T26` — Heisenberg Uncertainty (Time-Energy)

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.Quantization`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.QuantumMechanics.Measurement`

## Declaration Counts

- `def`: 4
- `eval`: 10
- `structure`: 10
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [PositionUncertainty](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/position-uncertainty/) | L44-L53 | defined | `IV.D68` |
| `structure` | [MomentumUncertainty](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/momentum-uncertainty/) | L57-L66 | defined | — |
| `structure` | [JointAddressNF](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/joint-address-nf/) | L76-L87 | defined | `IV.D69` |
| `structure` | [PhaseTransportWitness](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/phase-transport-witness/) | L96-L105 | defined | `IV.D70` |
| `structure` | [ClopenLocalization](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/clopen-localization/) | L114-L123 | defined | `IV.D71` |
| `theorem` | [phase_transport_monotone](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/phase-transport-monotone/) | L133-L143 | formalized | `IV.T22` |
| `structure` | [NoJointMinimum](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/no-joint-minimum/) | L156-L168 | defined | `IV.T23` |
| `theorem` | [no_joint_minimum](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/no-joint-minimum-l171/) | L171-L174 | formalized | — |
| `structure` | [CrossingMediator](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/crossing-mediator/) | L183-L196 | defined | `IV.D72` |
| `def` | [crossing_mediator](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/crossing-mediator-l199/) | L199-L206 | defined | — |
| `theorem` | [planck_uniqueness](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/planck-uniqueness/) | L216-L221 | formalized | `IV.T24` |
| `structure` | [SaturationState](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-state/) | L231-L243 | defined | `IV.D73` |
| `def` | [saturation_state](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-state-l246/) | L246-L252 | defined | — |
| `theorem` | [saturation_achieves_equality](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/saturation-achieves-equality/) | L260-L262 | formalized | `IV.P25` |
| `structure` | [HeisenbergXP](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-xp/) | L279-L292 | defined | `IV.T25` |
| `def` | [heisenberg_xp](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-xp-l295/) | L295-L303 | defined | — |
| `structure` | [HeisenbergTE](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-te/) | L315-L325 | defined | `IV.T26` |
| `def` | [heisenberg_te](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/heisenberg-te-l328/) | L328-L333 | defined | — |
| `theorem` | [uncertainty_bound_universal](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/uncertainty-bound-universal/) | L336-L339 | formalized | — |
| `eval` | [#eval L360](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l360/) | L360-L360 | computed | `IV.R316`, `IV.R318`, `IV.R320` |
| `eval` | [#eval L361](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l361/) | L361-L361 | computed | — |
| `eval` | [#eval L362](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l362/) | L362-L362 | computed | — |
| `eval` | [#eval L363](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l363/) | L363-L363 | computed | — |
| `eval` | [#eval L364](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l364/) | L364-L364 | computed | — |
| `eval` | [#eval L365](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l365/) | L365-L365 | computed | — |
| `eval` | [#eval L366](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l366/) | L366-L366 | computed | — |
| `eval` | [#eval L367](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l367/) | L367-L367 | computed | — |
| `eval` | [#eval L368](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l368/) | L368-L368 | computed | — |
| `eval` | [#eval L369](/verify/taulib/docs/book-iv-quantum-mechanics-address-obstruction/eval-l369/) | L369-L371 | computed | — |

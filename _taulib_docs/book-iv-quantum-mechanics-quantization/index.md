---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.Quantization",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.QuantumMechanics.Quantization`.",
  "module_name": "TauLib.BookIV.QuantumMechanics.Quantization",
  "module_slug": "book-iv-quantum-mechanics-quantization",
  "book": "BookIV",
  "family": "QuantumMechanics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/QuantumMechanics/Quantization.lean",
  "sha256": "bb5a674a6b6363467045644a1e1243ab7f0cc7f9153d50b348d2b48ef43c64a8",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.HilbertSpace",
    "TauLib.BookIV.Physics.PlanckCharacter"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.QuantumMechanics.AddressObstruction"
  ],
  "registry_ids": [
    "IV.D65",
    "IV.D66",
    "IV.D67",
    "IV.P23",
    "IV.P24",
    "IV.R305",
    "IV.R310",
    "IV.R312",
    "IV.R314",
    "IV.T20",
    "IV.T21"
  ],
  "declaration_counts": {
    "structure": 5,
    "def": 8,
    "theorem": 4,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "HolomorphicField",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/holomorphic-field/",
      "source_line_start": 41,
      "source_line_end": 49,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D65"
      ]
    },
    {
      "kind": "def",
      "name": "field_position",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/field-position/",
      "source_line_start": 52,
      "source_line_end": 56,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "field_momentum",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/field-momentum/",
      "source_line_start": 59,
      "source_line_end": 63,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QuantumOperator",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/quantum-operator/",
      "source_line_start": 73,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D66"
      ]
    },
    {
      "kind": "def",
      "name": "op_position",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/op-position/",
      "source_line_start": 84,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "op_momentum",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/op-momentum/",
      "source_line_start": 91,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "commutator_lifts",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/commutator-lifts/",
      "source_line_start": 105,
      "source_line_end": 108,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P23"
      ]
    },
    {
      "kind": "structure",
      "name": "TopologicalQuantization",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/topological-quantization/",
      "source_line_start": 122,
      "source_line_end": 135,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T20"
      ]
    },
    {
      "kind": "def",
      "name": "topological_quantization",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/topological-quantization-l138/",
      "source_line_start": 138,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CanonicalCommutation",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/canonical-commutation/",
      "source_line_start": 161,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T21"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_commutation",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/canonical-commutation-l173/",
      "source_line_start": 173,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "hbar_tau_quarter",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/hbar-tau-quarter/",
      "source_line_start": 180,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Observable",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/observable/",
      "source_line_start": 192,
      "source_line_end": 201,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D67"
      ]
    },
    {
      "kind": "def",
      "name": "obs_position",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/obs-position/",
      "source_line_start": 204,
      "source_line_end": 209,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "obs_momentum",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/obs-momentum/",
      "source_line_start": 212,
      "source_line_end": 217,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "xp_self_adjoint",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/xp-self-adjoint/",
      "source_line_start": 226,
      "source_line_end": 229,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P24"
      ]
    },
    {
      "kind": "theorem",
      "name": "xp_real_eigenvalues",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/xp-real-eigenvalues/",
      "source_line_start": 232,
      "source_line_end": 235,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "computed",
      "registry_ids": [
        "IV.R305",
        "IV.R310",
        "IV.R312",
        "IV.R314"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l258/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l259/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 267,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Quantization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Quantization.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/QuantumMechanics/Quantization.lean`
- SHA-256: `bb5a674a6b6363467045644a1e1243ab7f0cc7f9153d50b348d2b48ef43c64a8`

## Registry Links

- `IV.D65` — Holomorphic Vector Field
- `IV.D66` — Quantum Operator
- `IV.D67` — Observable
- `IV.P23` — Commutator Equals Lifted Lie Bracket
- `IV.P24` — X and P Are Self-Adjoint
- `IV.R305` — Comparison with geometric quantization
- `IV.R310` — Connection to Book~II spectral gap
- `IV.R312` — Born rule derived, not postulated
- `IV.R314` — Why standard QM works
- `IV.T20` — Topological Quantization
- `IV.T21` — Canonical Commutation Relation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.HilbertSpace`
- `TauLib.BookIV.Physics.PlanckCharacter`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.QuantumMechanics.AddressObstruction`

## Declaration Counts

- `def`: 8
- `eval`: 9
- `structure`: 5
- `theorem`: 4

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [HolomorphicField](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/holomorphic-field/) | L41-L49 | defined | `IV.D65` |
| `def` | [field_position](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/field-position/) | L52-L56 | defined | — |
| `def` | [field_momentum](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/field-momentum/) | L59-L63 | defined | — |
| `structure` | [QuantumOperator](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/quantum-operator/) | L73-L81 | defined | `IV.D66` |
| `def` | [op_position](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/op-position/) | L84-L88 | defined | — |
| `def` | [op_momentum](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/op-momentum/) | L91-L95 | defined | — |
| `theorem` | [commutator_lifts](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/commutator-lifts/) | L105-L108 | formalized | `IV.P23` |
| `structure` | [TopologicalQuantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/topological-quantization/) | L122-L135 | defined | `IV.T20` |
| `def` | [topological_quantization](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/topological-quantization-l138/) | L138-L146 | defined | — |
| `structure` | [CanonicalCommutation](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/canonical-commutation/) | L161-L170 | defined | `IV.T21` |
| `def` | [canonical_commutation](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/canonical-commutation-l173/) | L173-L177 | defined | — |
| `theorem` | [hbar_tau_quarter](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/hbar-tau-quarter/) | L180-L183 | formalized | — |
| `structure` | [Observable](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/observable/) | L192-L201 | defined | `IV.D67` |
| `def` | [obs_position](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/obs-position/) | L204-L209 | defined | — |
| `def` | [obs_momentum](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/obs-momentum/) | L212-L217 | defined | — |
| `theorem` | [xp_self_adjoint](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/xp-self-adjoint/) | L226-L229 | formalized | `IV.P24` |
| `theorem` | [xp_real_eigenvalues](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/xp-real-eigenvalues/) | L232-L235 | formalized | — |
| `eval` | [#eval L257](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l257/) | L257-L257 | computed | `IV.R305`, `IV.R310`, `IV.R312`, `IV.R314` |
| `eval` | [#eval L258](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l258/) | L258-L258 | computed | — |
| `eval` | [#eval L259](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l259/) | L259-L259 | computed | — |
| `eval` | [#eval L260](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l260/) | L260-L260 | computed | — |
| `eval` | [#eval L261](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l261/) | L261-L261 | computed | — |
| `eval` | [#eval L262](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l262/) | L262-L262 | computed | — |
| `eval` | [#eval L263](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l263/) | L263-L263 | computed | — |
| `eval` | [#eval L264](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l264/) | L264-L264 | computed | — |
| `eval` | [#eval L265](/verify/taulib/docs/book-iv-quantum-mechanics-quantization/eval-l265/) | L265-L267 | computed | — |

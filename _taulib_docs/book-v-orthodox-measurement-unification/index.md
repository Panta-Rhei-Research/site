---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Orthodox.MeasurementUnification",
  "permalink": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Orthodox.MeasurementUnification`.",
  "module_name": "TauLib.BookV.Orthodox.MeasurementUnification",
  "module_slug": "book-v-orthodox-measurement-unification",
  "book": "BookV",
  "family": "Orthodox",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Orthodox/MeasurementUnification.lean",
  "sha256": "cd0a0de3cfd4002a109c91e6067b676e0632a08eb047236ad50415f72c72c823",
  "imports": [
    "TauLib.BookV.Orthodox.OtherApproaches"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Orthodox.FalsifiableSeams"
  ],
  "registry_ids": [
    "V.D189",
    "V.P107",
    "V.R288",
    "V.R289",
    "V.R290",
    "V.T134",
    "V.T135"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 5,
    "def": 9,
    "theorem": 8,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ReadoutStatus",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/readout-status/",
      "source_line_start": 66,
      "source_line_end": 71,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "VMQuantumState",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/vmquantum-state/",
      "source_line_start": 81,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D189"
      ]
    },
    {
      "kind": "def",
      "name": "VMQuantumState.is_resolved",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/is-resolved/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "VMQuantumState.is_superposition",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/is-superposition/",
      "source_line_start": 99,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MeasurementDissolution",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/measurement-dissolution/",
      "source_line_start": 107,
      "source_line_end": 116,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_measurement_dissolution",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/canonical-measurement-dissolution/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.T134"
      ]
    },
    {
      "kind": "theorem",
      "name": "measurement_dissolution",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/measurement-dissolution-l134/",
      "source_line_start": 134,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_dissolution",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/canonical-dissolution/",
      "source_line_start": 138,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "unitary_is_readout",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/unitary-is-readout/",
      "source_line_start": 141,
      "source_line_end": 142,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "collapse_is_address_resolution",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/collapse-is-address-resolution/",
      "source_line_start": 145,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BellInequality",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/bell-inequality/",
      "source_line_start": 164,
      "source_line_end": 177,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T135"
      ]
    },
    {
      "kind": "def",
      "name": "bell_data",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/bell-data/",
      "source_line_start": 180,
      "source_line_end": 180,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bell_inequality_tau",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/bell-inequality-tau/",
      "source_line_start": 183,
      "source_line_end": 186,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tsirelson_exceeds_classical",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/tsirelson-exceeds-classical/",
      "source_line_start": 189,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DecoherenceShadow",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-shadow/",
      "source_line_start": 210,
      "source_line_end": 221,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P107"
      ]
    },
    {
      "kind": "def",
      "name": "decoherence_example",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-example/",
      "source_line_start": 224,
      "source_line_end": 228,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "decoherence_shadow",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-shadow-l231/",
      "source_line_start": 231,
      "source_line_end": 232,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "decoherence_total",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-total/",
      "source_line_start": 235,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QuantumClassicalTransition",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/quantum-classical-transition/",
      "source_line_start": 251,
      "source_line_end": 258,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_qc_transition",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/canonical-qc-transition/",
      "source_line_start": 261,
      "source_line_end": 262,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_heisenberg_cut",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/no-heisenberg-cut/",
      "source_line_start": 265,
      "source_line_end": 266,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_superposition",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/example-superposition/",
      "source_line_start": 291,
      "source_line_end": 296,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_resolved",
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/example-resolved/",
      "source_line_start": 299,
      "source_line_end": 304,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l308/",
      "source_line_start": 308,
      "source_line_end": 308,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l309/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 312,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean",
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
- Source path: [`TauLib/BookV/Orthodox/MeasurementUnification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/MeasurementUnification.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Orthodox/MeasurementUnification.lean`
- SHA-256: `cd0a0de3cfd4002a109c91e6067b676e0632a08eb047236ad50415f72c72c823`

## Registry Links

- `V.D189` — VM representation of a quantum state
- `V.P107` — Decoherence as address-resolution shadow
- `V.R288` — Superposition in the VM
- `V.R289` — Entanglement as address sharing
- `V.R290` — The century of confusion
- `V.T134` — Measurement problem dissolution
- `V.T135` — Bell inequality in tau

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Orthodox.OtherApproaches`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Orthodox.FalsifiableSeams`

## Declaration Counts

- `def`: 9
- `eval`: 5
- `inductive`: 1
- `structure`: 5
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [ReadoutStatus](/corpus/taulib/docs/book-v-orthodox-measurement-unification/readout-status/) | L66-L71 | type/data schema | type/data schema | — |
| `structure` | [VMQuantumState](/corpus/taulib/docs/book-v-orthodox-measurement-unification/vmquantum-state/) | L81-L92 | type/data schema | type/data schema | `V.D189` |
| `def` | [VMQuantumState.is_resolved](/corpus/taulib/docs/book-v-orthodox-measurement-unification/is-resolved/) | L95-L96 | data/computed value | data/computed value | — |
| `def` | [VMQuantumState.is_superposition](/corpus/taulib/docs/book-v-orthodox-measurement-unification/is-superposition/) | L99-L100 | data/computed value | data/computed value | — |
| `structure` | [MeasurementDissolution](/corpus/taulib/docs/book-v-orthodox-measurement-unification/measurement-dissolution/) | L107-L116 | type/data schema | type/data schema | — |
| `def` | [canonical_measurement_dissolution](/corpus/taulib/docs/book-v-orthodox-measurement-unification/canonical-measurement-dissolution/) | L131-L132 | definition | definition | `V.T134` |
| `theorem` | [measurement_dissolution](/corpus/taulib/docs/book-v-orthodox-measurement-unification/measurement-dissolution-l134/) | L134-L135 | proof obligation | formal proof obligation checked | — |
| `def` | [canonical_dissolution](/corpus/taulib/docs/book-v-orthodox-measurement-unification/canonical-dissolution/) | L138-L138 | definition | definition | — |
| `theorem` | [unitary_is_readout](/corpus/taulib/docs/book-v-orthodox-measurement-unification/unitary-is-readout/) | L141-L142 | proof obligation | formal proof obligation checked | — |
| `theorem` | [collapse_is_address_resolution](/corpus/taulib/docs/book-v-orthodox-measurement-unification/collapse-is-address-resolution/) | L145-L146 | proof obligation | formal proof obligation checked | — |
| `structure` | [BellInequality](/corpus/taulib/docs/book-v-orthodox-measurement-unification/bell-inequality/) | L164-L177 | type/data schema | type/data schema | `V.T135` |
| `def` | [bell_data](/corpus/taulib/docs/book-v-orthodox-measurement-unification/bell-data/) | L180-L180 | definition | definition | — |
| `theorem` | [bell_inequality_tau](/corpus/taulib/docs/book-v-orthodox-measurement-unification/bell-inequality-tau/) | L183-L186 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tsirelson_exceeds_classical](/corpus/taulib/docs/book-v-orthodox-measurement-unification/tsirelson-exceeds-classical/) | L189-L191 | proof obligation | formal proof obligation checked | — |
| `structure` | [DecoherenceShadow](/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-shadow/) | L210-L221 | type/data schema | type/data schema | `V.P107` |
| `def` | [decoherence_example](/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-example/) | L224-L228 | definition | definition | — |
| `theorem` | [decoherence_shadow](/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-shadow-l231/) | L231-L232 | proof obligation | formal proof obligation checked | — |
| `theorem` | [decoherence_total](/corpus/taulib/docs/book-v-orthodox-measurement-unification/decoherence-total/) | L235-L236 | proof obligation | formal proof obligation checked | — |
| `structure` | [QuantumClassicalTransition](/corpus/taulib/docs/book-v-orthodox-measurement-unification/quantum-classical-transition/) | L251-L258 | type/data schema | type/data schema | — |
| `def` | [canonical_qc_transition](/corpus/taulib/docs/book-v-orthodox-measurement-unification/canonical-qc-transition/) | L261-L262 | definition | definition | — |
| `theorem` | [no_heisenberg_cut](/corpus/taulib/docs/book-v-orthodox-measurement-unification/no-heisenberg-cut/) | L265-L266 | proof obligation | formal proof obligation checked | — |
| `def` | [example_superposition](/corpus/taulib/docs/book-v-orthodox-measurement-unification/example-superposition/) | L291-L296 | definition | definition | — |
| `def` | [example_resolved](/corpus/taulib/docs/book-v-orthodox-measurement-unification/example-resolved/) | L299-L304 | definition | definition | — |
| `eval` | [#eval L306](/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l306/) | L306-L306 | computed check | computed check | — |
| `eval` | [#eval L307](/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l307/) | L307-L307 | computed check | computed check | — |
| `eval` | [#eval L308](/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l308/) | L308-L308 | computed check | computed check | — |
| `eval` | [#eval L309](/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l309/) | L309-L309 | computed check | computed check | — |
| `eval` | [#eval L310](/corpus/taulib/docs/book-v-orthodox-measurement-unification/eval-l310/) | L310-L312 | computed check | computed check | — |

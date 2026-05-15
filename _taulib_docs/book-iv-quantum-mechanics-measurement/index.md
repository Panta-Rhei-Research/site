---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.Measurement",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.QuantumMechanics.Measurement`.",
  "module_name": "TauLib.BookIV.QuantumMechanics.Measurement",
  "module_slug": "book-iv-quantum-mechanics-measurement",
  "book": "BookIV",
  "family": "QuantumMechanics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/QuantumMechanics/Measurement.lean",
  "sha256": "ab5b5735678a7909bea62c55b2e9dbd5097e63e81f6ba6ea43113f77b2aac7fc",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.AddressObstruction"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.QuantumMechanics.EnergyEntropy"
  ],
  "registry_ids": [
    "IV.D74",
    "IV.D75",
    "IV.P26",
    "IV.P27",
    "IV.P28",
    "IV.R323",
    "IV.R326",
    "IV.T27",
    "IV.T28"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 4,
    "theorem": 7,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "AddressResolution",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/address-resolution/",
      "source_line_start": 72,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D74"
      ]
    },
    {
      "kind": "def",
      "name": "AddressResolution.probFloat",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/prob-float/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "born_rule_structural",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/born-rule-structural/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T27"
      ]
    },
    {
      "kind": "structure",
      "name": "BornNormalization",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/born-normalization/",
      "source_line_start": 106,
      "source_line_end": 116,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PostResolutionState",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/post-resolution-state/",
      "source_line_start": 128,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P26"
      ]
    },
    {
      "kind": "theorem",
      "name": "projection_idempotent",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/projection-idempotent/",
      "source_line_start": 138,
      "source_line_end": 139,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P26"
      ]
    },
    {
      "kind": "structure",
      "name": "Decoherence",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/decoherence/",
      "source_line_start": 153,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D75"
      ]
    },
    {
      "kind": "structure",
      "name": "SchrodingerEquation",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-equation/",
      "source_line_start": 180,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T28"
      ]
    },
    {
      "kind": "def",
      "name": "schrodinger_canonical",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-canonical/",
      "source_line_start": 194,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ClassicalLimit",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit/",
      "source_line_start": 210,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P27"
      ]
    },
    {
      "kind": "theorem",
      "name": "classical_limit_structural",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit-structural/",
      "source_line_start": 220,
      "source_line_end": 221,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DualTrackCompatibility",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/dual-track-compatibility/",
      "source_line_start": 238,
      "source_line_end": 245,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P28"
      ]
    },
    {
      "kind": "theorem",
      "name": "determinism_probability",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/determinism-probability/",
      "source_line_start": 248,
      "source_line_end": 255,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P28"
      ]
    },
    {
      "kind": "theorem",
      "name": "schrodinger_is_iota_sq",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-iota-sq/",
      "source_line_start": 262,
      "source_line_end": 265,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "schrodinger_is_derived",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-derived/",
      "source_line_start": 268,
      "source_line_end": 269,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resolution_bounded",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/resolution-bounded/",
      "source_line_start": 272,
      "source_line_end": 273,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_decoherence",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/example-decoherence/",
      "source_line_start": 288,
      "source_line_end": 291,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_dual_track",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/example-dual-track/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l296/",
      "source_line_start": 296,
      "source_line_end": 298,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/Measurement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/Measurement.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/QuantumMechanics/Measurement.lean`
- SHA-256: `ab5b5735678a7909bea62c55b2e9dbd5097e63e81f6ba6ea43113f77b2aac7fc`

## Registry Links

- `IV.D74` — Address Resolution
- `IV.D75` — Decoherence
- `IV.P26` — Measurement Repeatability
- `IV.P27` — Classical Limit
- `IV.P28` — Determinism-Probability Reconciliation
- `IV.R323` — Decoherence is not collapse
- `IV.R326` — One Hamiltonian rules all
- `IV.T27` — Born Rule
- `IV.T28` — Schrödinger Equation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.AddressObstruction`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.QuantumMechanics.EnergyEntropy`

## Declaration Counts

- `def`: 4
- `eval`: 5
- `structure`: 7
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [AddressResolution](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/address-resolution/) | L72-L85 | type/data schema | type/data schema | `IV.D74` |
| `def` | [AddressResolution.probFloat](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/prob-float/) | L88-L89 | data/computed value | data/computed value | — |
| `theorem` | [born_rule_structural](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/born-rule-structural/) | L101-L102 | proof obligation | formal proof obligation checked | `IV.T27` |
| `structure` | [BornNormalization](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/born-normalization/) | L106-L116 | type/data schema | type/data schema | — |
| `structure` | [PostResolutionState](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/post-resolution-state/) | L128-L135 | type/data schema | type/data schema | `IV.P26` |
| `theorem` | [projection_idempotent](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/projection-idempotent/) | L138-L139 | proof obligation | formal proof obligation checked | `IV.P26` |
| `structure` | [Decoherence](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/decoherence/) | L153-L164 | type/data schema | type/data schema | `IV.D75` |
| `structure` | [SchrodingerEquation](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-equation/) | L180-L191 | type/data schema | type/data schema | `IV.T28` |
| `def` | [schrodinger_canonical](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-canonical/) | L194-L197 | definition | definition | — |
| `structure` | [ClassicalLimit](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit/) | L210-L217 | type/data schema | type/data schema | `IV.P27` |
| `theorem` | [classical_limit_structural](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit-structural/) | L220-L221 | proof obligation | formal proof obligation checked | — |
| `structure` | [DualTrackCompatibility](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/dual-track-compatibility/) | L238-L245 | type/data schema | type/data schema | `IV.P28` |
| `theorem` | [determinism_probability](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/determinism-probability/) | L248-L255 | proof obligation | formal proof obligation checked | `IV.P28` |
| `theorem` | [schrodinger_is_iota_sq](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-iota-sq/) | L262-L265 | proof obligation | formal proof obligation checked | — |
| `theorem` | [schrodinger_is_derived](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-derived/) | L268-L269 | proof obligation | formal proof obligation checked | — |
| `theorem` | [resolution_bounded](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/resolution-bounded/) | L272-L273 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L280](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l280/) | L280-L280 | computed check | computed check | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l285/) | L285-L285 | computed check | computed check | — |
| `def` | [example_decoherence](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/example-decoherence/) | L288-L291 | definition | definition | — |
| `eval` | [#eval L292](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l292/) | L292-L292 | computed check | computed check | — |
| `def` | [example_dual_track](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/example-dual-track/) | L295-L295 | definition | definition | — |
| `eval` | [#eval L296](/corpus/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l296/) | L296-L298 | computed check | computed check | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.Measurement",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/",
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
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/address-resolution/",
      "source_line_start": 72,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D74"
      ]
    },
    {
      "kind": "def",
      "name": "AddressResolution.probFloat",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/prob-float/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "born_rule_structural",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/born-rule-structural/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T27"
      ]
    },
    {
      "kind": "structure",
      "name": "BornNormalization",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/born-normalization/",
      "source_line_start": 106,
      "source_line_end": 116,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PostResolutionState",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/post-resolution-state/",
      "source_line_start": 128,
      "source_line_end": 135,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P26"
      ]
    },
    {
      "kind": "theorem",
      "name": "projection_idempotent",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/projection-idempotent/",
      "source_line_start": 138,
      "source_line_end": 139,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P26"
      ]
    },
    {
      "kind": "structure",
      "name": "Decoherence",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/decoherence/",
      "source_line_start": 153,
      "source_line_end": 164,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D75"
      ]
    },
    {
      "kind": "structure",
      "name": "SchrodingerEquation",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-equation/",
      "source_line_start": 180,
      "source_line_end": 191,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T28"
      ]
    },
    {
      "kind": "def",
      "name": "schrodinger_canonical",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-canonical/",
      "source_line_start": 194,
      "source_line_end": 197,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ClassicalLimit",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit/",
      "source_line_start": 210,
      "source_line_end": 217,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P27"
      ]
    },
    {
      "kind": "theorem",
      "name": "classical_limit_structural",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit-structural/",
      "source_line_start": 220,
      "source_line_end": 221,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DualTrackCompatibility",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/dual-track-compatibility/",
      "source_line_start": 238,
      "source_line_end": 245,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P28"
      ]
    },
    {
      "kind": "theorem",
      "name": "determinism_probability",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/determinism-probability/",
      "source_line_start": 248,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P28"
      ]
    },
    {
      "kind": "theorem",
      "name": "schrodinger_is_iota_sq",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-iota-sq/",
      "source_line_start": 262,
      "source_line_end": 265,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "schrodinger_is_derived",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-derived/",
      "source_line_start": 268,
      "source_line_end": 269,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resolution_bounded",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/resolution-bounded/",
      "source_line_start": 272,
      "source_line_end": 273,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_decoherence",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/example-decoherence/",
      "source_line_start": 288,
      "source_line_end": 291,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_dual_track",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/example-dual-track/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l296/",
      "source_line_start": 296,
      "source_line_end": 298,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [AddressResolution](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/address-resolution/) | L72-L85 | defined | `IV.D74` |
| `def` | [AddressResolution.probFloat](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/prob-float/) | L88-L89 | defined | — |
| `theorem` | [born_rule_structural](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/born-rule-structural/) | L101-L102 | formalized | `IV.T27` |
| `structure` | [BornNormalization](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/born-normalization/) | L106-L116 | defined | — |
| `structure` | [PostResolutionState](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/post-resolution-state/) | L128-L135 | defined | `IV.P26` |
| `theorem` | [projection_idempotent](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/projection-idempotent/) | L138-L139 | formalized | `IV.P26` |
| `structure` | [Decoherence](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/decoherence/) | L153-L164 | defined | `IV.D75` |
| `structure` | [SchrodingerEquation](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-equation/) | L180-L191 | defined | `IV.T28` |
| `def` | [schrodinger_canonical](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-canonical/) | L194-L197 | defined | — |
| `structure` | [ClassicalLimit](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit/) | L210-L217 | defined | `IV.P27` |
| `theorem` | [classical_limit_structural](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/classical-limit-structural/) | L220-L221 | formalized | — |
| `structure` | [DualTrackCompatibility](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/dual-track-compatibility/) | L238-L245 | defined | `IV.P28` |
| `theorem` | [determinism_probability](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/determinism-probability/) | L248-L255 | formalized | `IV.P28` |
| `theorem` | [schrodinger_is_iota_sq](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-iota-sq/) | L262-L265 | formalized | — |
| `theorem` | [schrodinger_is_derived](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/schrodinger-is-derived/) | L268-L269 | formalized | — |
| `theorem` | [resolution_bounded](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/resolution-bounded/) | L272-L273 | formalized | — |
| `eval` | [#eval L280](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l280/) | L280-L280 | computed | — |
| `eval` | [#eval L284](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l284/) | L284-L284 | computed | — |
| `eval` | [#eval L285](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l285/) | L285-L285 | computed | — |
| `def` | [example_decoherence](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/example-decoherence/) | L288-L291 | defined | — |
| `eval` | [#eval L292](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l292/) | L292-L292 | computed | — |
| `def` | [example_dual_track](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/example-dual-track/) | L295-L295 | defined | — |
| `eval` | [#eval L296](/verify/taulib/docs/book-iv-quantum-mechanics-measurement/eval-l296/) | L296-L298 | computed | — |

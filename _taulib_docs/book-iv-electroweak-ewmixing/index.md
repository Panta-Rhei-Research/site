---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.EWMixing",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.EWMixing`.",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_slug": "book-iv-electroweak-ewmixing",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/EWMixing.lean",
  "sha256": "597b05ced6e677f7b550cbdfb14c6c9e7339b3201b32fa67230e6752c75c29fe",
  "imports": [
    "TauLib.BookIV.Electroweak.NeutrinoMode"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.TauHiggs",
    "TauLib.BookIV.Electroweak.WeinbergNLO"
  ],
  "registry_ids": [
    "IV.D127",
    "IV.D128",
    "IV.D129",
    "IV.D130",
    "IV.D131",
    "IV.D132",
    "IV.D133",
    "IV.P68",
    "IV.P69",
    "IV.P70",
    "IV.P71",
    "IV.R31",
    "IV.T60",
    "IV.T61",
    "IV.T62"
  ],
  "declaration_counts": {
    "structure": 10,
    "def": 17,
    "inductive": 1,
    "theorem": 7,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "Hypercharge",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge/",
      "source_line_start": 67,
      "source_line_end": 76,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D127"
      ]
    },
    {
      "kind": "def",
      "name": "hypercharge_eL",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge-e-l/",
      "source_line_start": 79,
      "source_line_end": 82,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "hypercharge_eR",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge-e-r/",
      "source_line_start": 85,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "hypercharge_qL",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge-q-l/",
      "source_line_start": 91,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PreMixingEWGroup",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/pre-mixing-ewgroup/",
      "source_line_start": 104,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D128"
      ]
    },
    {
      "kind": "def",
      "name": "ew_group",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/ew-group/",
      "source_line_start": 116,
      "source_line_end": 120,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ChargedCurrent",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/charged-current/",
      "source_line_start": 129,
      "source_line_end": 134,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D129"
      ]
    },
    {
      "kind": "def",
      "name": "charged_current_sector",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/charged-current-sector/",
      "source_line_start": 137,
      "source_line_end": 137,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "WeinbergAngleTau",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-angle-tau/",
      "source_line_start": 150,
      "source_line_end": 158,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D130"
      ]
    },
    {
      "kind": "def",
      "name": "weinberg_angle_tau",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-angle-tau-l161/",
      "source_line_start": 161,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "weinberg_float",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-float/",
      "source_line_start": 168,
      "source_line_end": 169,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MixingCompatibility",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-compatibility/",
      "source_line_start": 182,
      "source_line_end": 190,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D131"
      ]
    },
    {
      "kind": "def",
      "name": "mixing_pair",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-pair/",
      "source_line_start": 193,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MaximalMixing",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/maximal-mixing/",
      "source_line_start": 207,
      "source_line_end": 213,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D132"
      ]
    },
    {
      "kind": "def",
      "name": "maximal_mixing",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/maximal-mixing-l215/",
      "source_line_start": 215,
      "source_line_end": 216,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OmegaResolution",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/omega-resolution/",
      "source_line_start": 227,
      "source_line_end": 237,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D133"
      ]
    },
    {
      "kind": "def",
      "name": "omega_resolution",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/omega-resolution-l239/",
      "source_line_start": 239,
      "source_line_end": 244,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutralBosonMixing",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/neutral-boson-mixing/",
      "source_line_start": 258,
      "source_line_end": 271,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T60"
      ]
    },
    {
      "kind": "def",
      "name": "neutral_boson_mixing",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/neutral-boson-mixing-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mixing_orthogonal",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-orthogonal/",
      "source_line_start": 276,
      "source_line_end": 277,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T60"
      ]
    },
    {
      "kind": "theorem",
      "name": "mixing_conserves_count",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-conserves-count/",
      "source_line_start": 280,
      "source_line_end": 281,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weinberg_equals_kappaAD",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-equals-kappa-ad/",
      "source_line_start": 294,
      "source_line_end": 297,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T61"
      ]
    },
    {
      "kind": "theorem",
      "name": "weinberg_in_range",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-in-range/",
      "source_line_start": 300,
      "source_line_end": 303,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "unique_mixing_pair",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/unique-mixing-pair/",
      "source_line_start": 318,
      "source_line_end": 320,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T62"
      ]
    },
    {
      "kind": "theorem",
      "name": "A_unique_balanced",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/a-unique-balanced/",
      "source_line_start": 323,
      "source_line_end": 328,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EMCouplingRelation",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/emcoupling-relation/",
      "source_line_start": 340,
      "source_line_end": 351,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P68"
      ]
    },
    {
      "kind": "def",
      "name": "em_coupling_relation",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/em-coupling-relation/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sin2_exp_numer",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/sin2-exp-numer/",
      "source_line_start": 360,
      "source_line_end": 360,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sin2_exp_denom",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/sin2-exp-denom/",
      "source_line_start": 362,
      "source_line_end": 362,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tree_level_deviation",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/tree-level-deviation/",
      "source_line_start": 369,
      "source_line_end": 375,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P69"
      ]
    },
    {
      "kind": "structure",
      "name": "NoHigherUnification",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/no-higher-unification/",
      "source_line_start": 391,
      "source_line_end": 398,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P70"
      ]
    },
    {
      "kind": "def",
      "name": "no_higher_unification",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/no-higher-unification-l400/",
      "source_line_start": 400,
      "source_line_end": 400,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DualRoleBalanced",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/dual-role-balanced/",
      "source_line_start": 416,
      "source_line_end": 425,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P71"
      ]
    },
    {
      "kind": "def",
      "name": "dual_role_balanced",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/dual-role-balanced-l427/",
      "source_line_start": 427,
      "source_line_end": 427,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_gap_scope",
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/remark-gap-scope/",
      "source_line_start": 441,
      "source_line_end": 442,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R31"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l448/",
      "source_line_start": 448,
      "source_line_end": 448,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l449/",
      "source_line_start": 449,
      "source_line_end": 449,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l450/",
      "source_line_start": 450,
      "source_line_end": 450,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l451/",
      "source_line_start": 451,
      "source_line_end": 451,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l452/",
      "source_line_start": 452,
      "source_line_end": 452,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l453/",
      "source_line_start": 453,
      "source_line_end": 453,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l454/",
      "source_line_start": 454,
      "source_line_end": 454,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l455/",
      "source_line_start": 455,
      "source_line_end": 455,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l456/",
      "source_line_start": 456,
      "source_line_end": 458,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/EWMixing.lean`
- SHA-256: `597b05ced6e677f7b550cbdfb14c6c9e7339b3201b32fa67230e6752c75c29fe`

## Registry Links

- `IV.D127` — τ-Hypercharge
- `IV.D128` — Pre-Mixing Electroweak Gauge Group
- `IV.D129` — Charged W Bosons
- `IV.D130` — Weinberg Angle
- `IV.D131` — Mixing Compatibility
- `IV.D132` — Electroweak Coherence State
- `IV.D133` — Coherence Fixing (Ch33)
- `IV.P68` — Coupling Relations
- `IV.P69` — Weinberg Angle Residual Analysis
- `IV.P70` — No Grand Unification
- `IV.P71` — Parity Bridge and Mixing
- `IV.R31` — Weinberg Angle Gap Assessment
- `IV.T60` — Neutral Boson Mixing
- `IV.T61` — Weinberg Angle Prediction
- `IV.T62` — Mixing Uniqueness Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Electroweak.NeutrinoMode`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.TauHiggs`
- `TauLib.BookIV.Electroweak.WeinbergNLO`

## Declaration Counts

- `def`: 17
- `eval`: 9
- `inductive`: 1
- `structure`: 10
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [Hypercharge](/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge/) | L67-L76 | type/data schema | type/data schema | `IV.D127` |
| `def` | [hypercharge_eL](/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge-e-l/) | L79-L82 | definition | definition | — |
| `def` | [hypercharge_eR](/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge-e-r/) | L85-L88 | definition | definition | — |
| `def` | [hypercharge_qL](/corpus/taulib/docs/book-iv-electroweak-ewmixing/hypercharge-q-l/) | L91-L94 | definition | definition | — |
| `structure` | [PreMixingEWGroup](/corpus/taulib/docs/book-iv-electroweak-ewmixing/pre-mixing-ewgroup/) | L104-L113 | type/data schema | type/data schema | `IV.D128` |
| `def` | [ew_group](/corpus/taulib/docs/book-iv-electroweak-ewmixing/ew-group/) | L116-L120 | definition | definition | — |
| `inductive` | [ChargedCurrent](/corpus/taulib/docs/book-iv-electroweak-ewmixing/charged-current/) | L129-L134 | type/data schema | type/data schema | `IV.D129` |
| `def` | [charged_current_sector](/corpus/taulib/docs/book-iv-electroweak-ewmixing/charged-current-sector/) | L137-L137 | definition | definition | — |
| `structure` | [WeinbergAngleTau](/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-angle-tau/) | L150-L158 | type/data schema | type/data schema | `IV.D130` |
| `def` | [weinberg_angle_tau](/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-angle-tau-l161/) | L161-L165 | definition | definition | — |
| `def` | [weinberg_float](/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-float/) | L168-L169 | data/computed value | data/computed value | — |
| `structure` | [MixingCompatibility](/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-compatibility/) | L182-L190 | type/data schema | type/data schema | `IV.D131` |
| `def` | [mixing_pair](/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-pair/) | L193-L197 | definition | definition | — |
| `structure` | [MaximalMixing](/corpus/taulib/docs/book-iv-electroweak-ewmixing/maximal-mixing/) | L207-L213 | type/data schema | type/data schema | `IV.D132` |
| `def` | [maximal_mixing](/corpus/taulib/docs/book-iv-electroweak-ewmixing/maximal-mixing-l215/) | L215-L216 | definition | definition | — |
| `structure` | [OmegaResolution](/corpus/taulib/docs/book-iv-electroweak-ewmixing/omega-resolution/) | L227-L237 | type/data schema | type/data schema | `IV.D133` |
| `def` | [omega_resolution](/corpus/taulib/docs/book-iv-electroweak-ewmixing/omega-resolution-l239/) | L239-L244 | definition | definition | — |
| `structure` | [NeutralBosonMixing](/corpus/taulib/docs/book-iv-electroweak-ewmixing/neutral-boson-mixing/) | L258-L271 | type/data schema | type/data schema | `IV.T60` |
| `def` | [neutral_boson_mixing](/corpus/taulib/docs/book-iv-electroweak-ewmixing/neutral-boson-mixing-l273/) | L273-L273 | definition | definition | — |
| `theorem` | [mixing_orthogonal](/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-orthogonal/) | L276-L277 | proof obligation | formal proof obligation checked | `IV.T60` |
| `theorem` | [mixing_conserves_count](/corpus/taulib/docs/book-iv-electroweak-ewmixing/mixing-conserves-count/) | L280-L281 | proof obligation | formal proof obligation checked | — |
| `theorem` | [weinberg_equals_kappaAD](/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-equals-kappa-ad/) | L294-L297 | proof obligation | formal proof obligation checked | `IV.T61` |
| `theorem` | [weinberg_in_range](/corpus/taulib/docs/book-iv-electroweak-ewmixing/weinberg-in-range/) | L300-L303 | proof obligation | formal proof obligation checked | — |
| `theorem` | [unique_mixing_pair](/corpus/taulib/docs/book-iv-electroweak-ewmixing/unique-mixing-pair/) | L318-L320 | proof obligation | formal proof obligation checked | `IV.T62` |
| `theorem` | [A_unique_balanced](/corpus/taulib/docs/book-iv-electroweak-ewmixing/a-unique-balanced/) | L323-L328 | proof obligation | formal proof obligation checked | — |
| `structure` | [EMCouplingRelation](/corpus/taulib/docs/book-iv-electroweak-ewmixing/emcoupling-relation/) | L340-L351 | type/data schema | type/data schema | `IV.P68` |
| `def` | [em_coupling_relation](/corpus/taulib/docs/book-iv-electroweak-ewmixing/em-coupling-relation/) | L353-L353 | definition | definition | — |
| `def` | [sin2_exp_numer](/corpus/taulib/docs/book-iv-electroweak-ewmixing/sin2-exp-numer/) | L360-L360 | data/computed value | data/computed value | — |
| `def` | [sin2_exp_denom](/corpus/taulib/docs/book-iv-electroweak-ewmixing/sin2-exp-denom/) | L362-L362 | data/computed value | data/computed value | — |
| `theorem` | [tree_level_deviation](/corpus/taulib/docs/book-iv-electroweak-ewmixing/tree-level-deviation/) | L369-L375 | proof obligation | formal proof obligation checked | `IV.P69` |
| `structure` | [NoHigherUnification](/corpus/taulib/docs/book-iv-electroweak-ewmixing/no-higher-unification/) | L391-L398 | type/data schema | type/data schema | `IV.P70` |
| `def` | [no_higher_unification](/corpus/taulib/docs/book-iv-electroweak-ewmixing/no-higher-unification-l400/) | L400-L400 | definition | definition | — |
| `structure` | [DualRoleBalanced](/corpus/taulib/docs/book-iv-electroweak-ewmixing/dual-role-balanced/) | L416-L425 | type/data schema | type/data schema | `IV.P71` |
| `def` | [dual_role_balanced](/corpus/taulib/docs/book-iv-electroweak-ewmixing/dual-role-balanced-l427/) | L427-L427 | definition | definition | — |
| `def` | [remark_gap_scope](/corpus/taulib/docs/book-iv-electroweak-ewmixing/remark-gap-scope/) | L441-L442 | docstring/data record | docstring/data record | `IV.R31` |
| `eval` | [#eval L448](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l448/) | L448-L448 | computed check | computed check | — |
| `eval` | [#eval L449](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l449/) | L449-L449 | computed check | computed check | — |
| `eval` | [#eval L450](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l450/) | L450-L450 | computed check | computed check | — |
| `eval` | [#eval L451](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l451/) | L451-L451 | computed check | computed check | — |
| `eval` | [#eval L452](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l452/) | L452-L452 | computed check | computed check | — |
| `eval` | [#eval L453](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l453/) | L453-L453 | computed check | computed check | — |
| `eval` | [#eval L454](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l454/) | L454-L454 | computed check | computed check | — |
| `eval` | [#eval L455](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l455/) | L455-L455 | computed check | computed check | — |
| `eval` | [#eval L456](/corpus/taulib/docs/book-iv-electroweak-ewmixing/eval-l456/) | L456-L458 | computed check | computed check | — |

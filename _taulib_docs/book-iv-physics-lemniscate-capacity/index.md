---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.LemniscateCapacity",
  "permalink": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_slug": "book-iv-physics-lemniscate-capacity",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/LemniscateCapacity.lean",
  "sha256": "854134dc20675765e56b0d76f4fa72a64106ad29fda2b224e1337dd5a1f4ab3a",
  "imports": [
    "TauLib.BookI.Boundary.Spectral",
    "TauLib.BookIV.Sectors.SectorParameters"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.MassDerivation.BreathingModes",
    "TauLib.BookIV.Physics.NucleonMassSplitting",
    "TauLib.BookV.Gravity.CoRotorCoupling"
  ],
  "registry_ids": [
    "IV.D42",
    "IV.D43",
    "IV.P06",
    "IV.R11",
    "IV.T11"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 3,
    "def": 8,
    "theorem": 9,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "LemniscateSupport",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-support/",
      "source_line_start": 69,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D42"
      ]
    },
    {
      "kind": "structure",
      "name": "LemniscateThreeFold",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-three-fold/",
      "source_line_start": 76,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "three_fold",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/three-fold/",
      "source_line_start": 86,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "supports_distinct",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/supports-distinct/",
      "source_line_start": 91,
      "source_line_end": 106,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T11"
      ]
    },
    {
      "kind": "def",
      "name": "omega_real_sq",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/omega-real-sq/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_imag_sq",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/omega-imag-sq/",
      "source_line_start": 112,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/omega-denom/",
      "source_line_start": 115,
      "source_line_end": 115,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "threefold_distance_sq",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/threefold-distance-sq/",
      "source_line_start": 127,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T11"
      ]
    },
    {
      "kind": "theorem",
      "name": "distance_numerator",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/distance-numerator/",
      "source_line_start": 132,
      "source_line_end": 134,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distance_denominator",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/distance-denominator/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-numer/",
      "source_line_start": 150,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D43"
      ]
    },
    {
      "kind": "def",
      "name": "sqrt3_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom/",
      "source_line_start": 151,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom-pos/",
      "source_line_start": 154,
      "source_line_end": 155,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3_float",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-float/",
      "source_line_start": 158,
      "source_line_end": 159,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_approx_undershoots",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-undershoots/",
      "source_line_start": 163,
      "source_line_end": 164,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P06"
      ]
    },
    {
      "kind": "theorem",
      "name": "sqrt3_approx_quality",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-quality/",
      "source_line_start": 168,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_in_range",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-in-range/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Sqrt3Triad",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad/",
      "source_line_start": 191,
      "source_line_end": 198,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R11"
      ]
    },
    {
      "kind": "def",
      "name": "sqrt3_triad",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad-l201/",
      "source_line_start": 201,
      "source_line_end": 205,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "triad_count",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/triad-count/",
      "source_line_start": 208,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CapacityIdentity",
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/capacity-identity/",
      "source_line_start": 220,
      "source_line_end": 228,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l243/",
      "source_line_start": 243,
      "source_line_end": 245,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean",
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
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/LemniscateCapacity.lean`
- SHA-256: `854134dc20675765e56b0d76f4fa72a64106ad29fda2b224e1337dd5a1f4ab3a`

## Registry Links

- `IV.D42` — Lemniscate Three-Fold
- `IV.D43` — Spectral Distance √3
- `IV.P06` — √3 Approximation Quality
- `IV.R11` — √3 Triad
- `IV.T11` — Three-Fold Distance Squared

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.Spectral`
- `TauLib.BookIV.Sectors.SectorParameters`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.MassDerivation.BreathingModes`
- `TauLib.BookIV.Physics.NucleonMassSplitting`
- `TauLib.BookV.Gravity.CoRotorCoupling`

## Declaration Counts

- `def`: 8
- `eval`: 5
- `inductive`: 1
- `structure`: 3
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [LemniscateSupport](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-support/) | L69-L73 | type/data schema | type/data schema | `IV.D42` |
| `structure` | [LemniscateThreeFold](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-three-fold/) | L76-L83 | type/data schema | type/data schema | — |
| `def` | [three_fold](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/three-fold/) | L86-L88 | definition | definition | — |
| `theorem` | [supports_distinct](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/supports-distinct/) | L91-L106 | proof obligation | formal proof obligation checked | `IV.T11` |
| `def` | [omega_real_sq](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/omega-real-sq/) | L109-L109 | data/computed value | data/computed value | — |
| `def` | [omega_imag_sq](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/omega-imag-sq/) | L112-L112 | data/computed value | data/computed value | — |
| `def` | [omega_denom](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/omega-denom/) | L115-L115 | data/computed value | data/computed value | — |
| `theorem` | [threefold_distance_sq](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/threefold-distance-sq/) | L127-L129 | proof obligation | formal proof obligation checked | `IV.T11` |
| `theorem` | [distance_numerator](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/distance-numerator/) | L132-L134 | proof obligation | formal proof obligation checked | — |
| `theorem` | [distance_denominator](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/distance-denominator/) | L137-L138 | proof obligation | formal proof obligation checked | — |
| `def` | [sqrt3_numer](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-numer/) | L150-L150 | data/computed value | data/computed value | `IV.D43` |
| `def` | [sqrt3_denom](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom/) | L151-L151 | data/computed value | data/computed value | — |
| `theorem` | [sqrt3_denom_pos](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom-pos/) | L154-L155 | proof obligation | formal proof obligation checked | — |
| `def` | [sqrt3_float](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-float/) | L158-L159 | data/computed value | data/computed value | — |
| `theorem` | [sqrt3_approx_undershoots](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-undershoots/) | L163-L164 | proof obligation | formal proof obligation checked | `IV.P06` |
| `theorem` | [sqrt3_approx_quality](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-quality/) | L168-L169 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sqrt3_in_range](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-in-range/) | L173-L176 | proof obligation | formal proof obligation checked | — |
| `structure` | [Sqrt3Triad](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad/) | L191-L198 | type/data schema | type/data schema | `IV.R11` |
| `def` | [sqrt3_triad](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad-l201/) | L201-L205 | data/computed value | data/computed value | — |
| `theorem` | [triad_count](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/triad-count/) | L208-L208 | proof obligation | formal proof obligation checked | — |
| `structure` | [CapacityIdentity](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/capacity-identity/) | L220-L228 | type/data schema | type/data schema | — |
| `eval` | [#eval L235](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l235/) | L235-L235 | computed check | computed check | — |
| `eval` | [#eval L236](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l236/) | L236-L236 | computed check | computed check | — |
| `eval` | [#eval L239](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l239/) | L239-L239 | computed check | computed check | — |
| `eval` | [#eval L240](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l240/) | L240-L240 | computed check | computed check | — |
| `eval` | [#eval L243](/corpus/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l243/) | L243-L245 | computed check | computed check | — |

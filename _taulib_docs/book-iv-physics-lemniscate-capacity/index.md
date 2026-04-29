---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.LemniscateCapacity",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
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
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-support/",
      "source_line_start": 69,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D42"
      ]
    },
    {
      "kind": "structure",
      "name": "LemniscateThreeFold",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-three-fold/",
      "source_line_start": 76,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "three_fold",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/three-fold/",
      "source_line_start": 86,
      "source_line_end": 88,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "supports_distinct",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/supports-distinct/",
      "source_line_start": 91,
      "source_line_end": 106,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T11"
      ]
    },
    {
      "kind": "def",
      "name": "omega_real_sq",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/omega-real-sq/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_imag_sq",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/omega-imag-sq/",
      "source_line_start": 112,
      "source_line_end": 112,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_denom",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/omega-denom/",
      "source_line_start": 115,
      "source_line_end": 115,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "threefold_distance_sq",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/threefold-distance-sq/",
      "source_line_start": 127,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T11"
      ]
    },
    {
      "kind": "theorem",
      "name": "distance_numerator",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/distance-numerator/",
      "source_line_start": 132,
      "source_line_end": 134,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distance_denominator",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/distance-denominator/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3_numer",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-numer/",
      "source_line_start": 150,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D43"
      ]
    },
    {
      "kind": "def",
      "name": "sqrt3_denom",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom/",
      "source_line_start": 151,
      "source_line_end": 151,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom-pos/",
      "source_line_start": 154,
      "source_line_end": 155,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3_float",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-float/",
      "source_line_start": 158,
      "source_line_end": 159,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_approx_undershoots",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-undershoots/",
      "source_line_start": 163,
      "source_line_end": 164,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P06"
      ]
    },
    {
      "kind": "theorem",
      "name": "sqrt3_approx_quality",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-quality/",
      "source_line_start": 168,
      "source_line_end": 169,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sqrt3_in_range",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-in-range/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Sqrt3Triad",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad/",
      "source_line_start": 191,
      "source_line_end": 198,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R11"
      ]
    },
    {
      "kind": "def",
      "name": "sqrt3_triad",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad-l201/",
      "source_line_start": 201,
      "source_line_end": 205,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "triad_count",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/triad-count/",
      "source_line_start": 208,
      "source_line_end": 208,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CapacityIdentity",
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/capacity-identity/",
      "source_line_start": 220,
      "source_line_end": 228,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l243/",
      "source_line_start": 243,
      "source_line_end": 245,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [LemniscateSupport](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-support/) | L69-L73 | defined | `IV.D42` |
| `structure` | [LemniscateThreeFold](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/lemniscate-three-fold/) | L76-L83 | defined | — |
| `def` | [three_fold](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/three-fold/) | L86-L88 | defined | — |
| `theorem` | [supports_distinct](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/supports-distinct/) | L91-L106 | formalized | `IV.T11` |
| `def` | [omega_real_sq](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/omega-real-sq/) | L109-L109 | defined | — |
| `def` | [omega_imag_sq](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/omega-imag-sq/) | L112-L112 | defined | — |
| `def` | [omega_denom](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/omega-denom/) | L115-L115 | defined | — |
| `theorem` | [threefold_distance_sq](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/threefold-distance-sq/) | L127-L129 | formalized | `IV.T11` |
| `theorem` | [distance_numerator](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/distance-numerator/) | L132-L134 | formalized | — |
| `theorem` | [distance_denominator](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/distance-denominator/) | L137-L138 | formalized | — |
| `def` | [sqrt3_numer](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-numer/) | L150-L150 | defined | `IV.D43` |
| `def` | [sqrt3_denom](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom/) | L151-L151 | defined | — |
| `theorem` | [sqrt3_denom_pos](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-denom-pos/) | L154-L155 | formalized | — |
| `def` | [sqrt3_float](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-float/) | L158-L159 | defined | — |
| `theorem` | [sqrt3_approx_undershoots](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-undershoots/) | L163-L164 | formalized | `IV.P06` |
| `theorem` | [sqrt3_approx_quality](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-approx-quality/) | L168-L169 | formalized | — |
| `theorem` | [sqrt3_in_range](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-in-range/) | L173-L176 | formalized | — |
| `structure` | [Sqrt3Triad](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad/) | L191-L198 | defined | `IV.R11` |
| `def` | [sqrt3_triad](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad-l201/) | L201-L205 | defined | — |
| `theorem` | [triad_count](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/triad-count/) | L208-L208 | formalized | — |
| `structure` | [CapacityIdentity](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/capacity-identity/) | L220-L228 | defined | — |
| `eval` | [#eval L235](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l235/) | L235-L235 | computed | — |
| `eval` | [#eval L236](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l236/) | L236-L236 | computed | — |
| `eval` | [#eval L239](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l239/) | L239-L239 | computed | — |
| `eval` | [#eval L240](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l240/) | L240-L240 | computed | — |
| `eval` | [#eval L243](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/eval-l243/) | L243-L245 | computed | — |

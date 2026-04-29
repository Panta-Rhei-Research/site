---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.DimensionlessNearMatch`.",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessNearMatch",
  "module_slug": "book-iv-calibration-dimensionless-near-match",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean",
  "sha256": "142a78a524fd33fe11709f2ad3db307a52aedaf310240df61ee6dd83f3dd2abe",
  "imports": [
    "TauLib.BookIV.Sectors.FineStructure",
    "TauLib.BookIV.Calibration.SIReference"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.ConstantsLedger"
  ],
  "registry_ids": [
    "IV.D28",
    "IV.D29",
    "IV.P05"
  ],
  "declaration_counts": {
    "structure": 3,
    "theorem": 9,
    "def": 1,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "WeinbergNearMatch",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-near-match/",
      "source_line_start": 50,
      "source_line_end": 56,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D28"
      ]
    },
    {
      "kind": "theorem",
      "name": "weinberg_range",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-range/",
      "source_line_start": 59,
      "source_line_end": 61,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weinberg_undershoots",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-undershoots/",
      "source_line_start": 64,
      "source_line_end": 66,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weinberg_deviation_lt_3pct",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-deviation-lt-3pct/",
      "source_line_start": 71,
      "source_line_end": 74,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "StrongNearMatch",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-near-match/",
      "source_line_start": 85,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D29"
      ]
    },
    {
      "kind": "theorem",
      "name": "strong_range",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-range/",
      "source_line_start": 96,
      "source_line_end": 98,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "strong_overshoots",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-overshoots/",
      "source_line_start": 101,
      "source_line_end": 103,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "strong_deviation_lt_3pct",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-deviation-lt-3pct/",
      "source_line_start": 108,
      "source_line_end": 111,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_spectral_overshoots",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/alpha-spectral-overshoots/",
      "source_line_start": 120,
      "source_line_end": 122,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_near_matches_in_range",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/all-near-matches-in-range/",
      "source_line_start": 131,
      "source_line_end": 141,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P05"
      ]
    },
    {
      "kind": "structure",
      "name": "NearMatchEntry",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/near-match-entry/",
      "source_line_start": 148,
      "source_line_end": 155,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "near_match_table",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/near-match-table/",
      "source_line_start": 158,
      "source_line_end": 171,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "near_match_count",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/near-match-count/",
      "source_line_start": 174,
      "source_line_end": 174,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l181/",
      "source_line_start": 181,
      "source_line_end": 181,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l184/",
      "source_line_start": 184,
      "source_line_end": 184,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l187/",
      "source_line_start": 187,
      "source_line_end": 187,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l190/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l191/",
      "source_line_start": 191,
      "source_line_end": 191,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l192/",
      "source_line_start": 192,
      "source_line_end": 192,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 197,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/DimensionlessNearMatch.lean`
- SHA-256: `142a78a524fd33fe11709f2ad3db307a52aedaf310240df61ee6dd83f3dd2abe`

## Registry Links

- `IV.D28` — Weinberg Near-Match
- `IV.D29` — Strong Near-Match
- `IV.P05` — All Near-Matches in Range

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.FineStructure`
- `TauLib.BookIV.Calibration.SIReference`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.ConstantsLedger`

## Declaration Counts

- `def`: 1
- `eval`: 7
- `structure`: 3
- `theorem`: 9

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [WeinbergNearMatch](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-near-match/) | L50-L56 | defined | `IV.D28` |
| `theorem` | [weinberg_range](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-range/) | L59-L61 | formalized | — |
| `theorem` | [weinberg_undershoots](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-undershoots/) | L64-L66 | formalized | — |
| `theorem` | [weinberg_deviation_lt_3pct](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/weinberg-deviation-lt-3pct/) | L71-L74 | formalized | — |
| `structure` | [StrongNearMatch](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-near-match/) | L85-L93 | defined | `IV.D29` |
| `theorem` | [strong_range](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-range/) | L96-L98 | formalized | — |
| `theorem` | [strong_overshoots](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-overshoots/) | L101-L103 | formalized | — |
| `theorem` | [strong_deviation_lt_3pct](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/strong-deviation-lt-3pct/) | L108-L111 | formalized | — |
| `theorem` | [alpha_spectral_overshoots](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/alpha-spectral-overshoots/) | L120-L122 | formalized | — |
| `theorem` | [all_near_matches_in_range](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/all-near-matches-in-range/) | L131-L141 | formalized | `IV.P05` |
| `structure` | [NearMatchEntry](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/near-match-entry/) | L148-L155 | defined | — |
| `def` | [near_match_table](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/near-match-table/) | L158-L171 | defined | — |
| `theorem` | [near_match_count](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/near-match-count/) | L174-L174 | formalized | — |
| `eval` | [#eval L181](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l181/) | L181-L181 | computed | — |
| `eval` | [#eval L184](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l184/) | L184-L184 | computed | — |
| `eval` | [#eval L187](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l187/) | L187-L187 | computed | — |
| `eval` | [#eval L190](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l190/) | L190-L190 | computed | — |
| `eval` | [#eval L191](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l191/) | L191-L191 | computed | — |
| `eval` | [#eval L192](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l192/) | L192-L192 | computed | — |
| `eval` | [#eval L195](/verify/taulib/docs/book-iv-calibration-dimensionless-near-match/eval-l195/) | L195-L197 | computed | — |

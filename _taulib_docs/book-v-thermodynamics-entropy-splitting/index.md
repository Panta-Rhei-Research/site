---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_slug": "book-v-thermodynamics-entropy-splitting",
  "book": "BookV",
  "family": "Thermodynamics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Thermodynamics/EntropySplitting.lean",
  "sha256": "b768d1a4790676f68bbe8769205045dbb3ba7b87790aa5e7a8b3b501a9b7b165",
  "imports": [
    "TauLib.BookV.Thermodynamics.Inversion"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Thermodynamics.DefectExhaustion"
  ],
  "registry_ids": [
    "V.C06",
    "V.D85",
    "V.D86",
    "V.D87",
    "V.P27",
    "V.P28",
    "V.P29",
    "V.R119",
    "V.R120",
    "V.R121",
    "V.R122",
    "V.T56",
    "V.T57",
    "V.T58",
    "V.T59"
  ],
  "declaration_counts": {
    "structure": 7,
    "theorem": 7,
    "def": 5,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "DefectPartitionOfPaths",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-partition-of-paths/",
      "source_line_start": 68,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": [
        "V.D85"
      ]
    },
    {
      "kind": "theorem",
      "name": "partition_exhaustive",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/partition-exhaustive/",
      "source_line_start": 82,
      "source_line_end": 83,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroDefectEntropy",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-defect-entropy/",
      "source_line_start": 97,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": [
        "V.D86"
      ]
    },
    {
      "kind": "def",
      "name": "MacroDefectEntropy.toFloat",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/to-float/",
      "source_line_start": 109,
      "source_line_end": 110,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroRefinementEntropy",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-refinement-entropy/",
      "source_line_start": 123,
      "source_line_end": 132,
      "formal_status": "defined",
      "registry_ids": [
        "V.D87"
      ]
    },
    {
      "kind": "def",
      "name": "MacroRefinementEntropy.toFloat",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/to-float-l135/",
      "source_line_start": 135,
      "source_line_end": 136,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroEntropySplitThm",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-entropy-split-thm/",
      "source_line_start": 150,
      "source_line_end": 163,
      "formal_status": "defined",
      "registry_ids": [
        "V.T56"
      ]
    },
    {
      "kind": "def",
      "name": "MacroEntropySplitThm.totalFloat",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/total-float/",
      "source_line_start": 166,
      "source_line_end": 168,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "defect_entropy_bounded",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-bounded/",
      "source_line_start": 176,
      "source_line_end": 179,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T57"
      ]
    },
    {
      "kind": "theorem",
      "name": "defect_entropy_monotone",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-monotone/",
      "source_line_start": 190,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T58"
      ]
    },
    {
      "kind": "theorem",
      "name": "defect_entropy_reaches_zero",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-reaches-zero/",
      "source_line_start": 202,
      "source_line_end": 204,
      "formal_status": "formalized",
      "registry_ids": [
        "V.C06"
      ]
    },
    {
      "kind": "theorem",
      "name": "refinement_entropy_unbounded",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/refinement-entropy-unbounded/",
      "source_line_start": 215,
      "source_line_end": 217,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T59"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutProjection",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/readout-projection/",
      "source_line_start": 229,
      "source_line_end": 234,
      "formal_status": "defined",
      "registry_ids": [
        "V.P27"
      ]
    },
    {
      "kind": "structure",
      "name": "SplittingRatioControl",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/splitting-ratio-control/",
      "source_line_start": 245,
      "source_line_end": 250,
      "formal_status": "defined",
      "registry_ids": [
        "V.P28"
      ]
    },
    {
      "kind": "structure",
      "name": "DefectEntropyFromFunctional",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-from-functional/",
      "source_line_start": 261,
      "source_line_end": 266,
      "formal_status": "defined",
      "registry_ids": [
        "V.P29"
      ]
    },
    {
      "kind": "theorem",
      "name": "paradox_resolved",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/paradox-resolved/",
      "source_line_start": 277,
      "source_line_end": 279,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R119",
        "V.R120"
      ]
    },
    {
      "kind": "theorem",
      "name": "noise_dominance",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/noise-dominance/",
      "source_line_start": 283,
      "source_line_end": 285,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R121"
      ]
    },
    {
      "kind": "def",
      "name": "example_early_split",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/example-early-split/",
      "source_line_start": 295,
      "source_line_end": 301,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l303/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l304/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l305/",
      "source_line_start": 305,
      "source_line_end": 305,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_late_split",
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/example-late-split/",
      "source_line_start": 308,
      "source_line_end": 314,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 319,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean",
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
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Thermodynamics/EntropySplitting.lean`
- SHA-256: `b768d1a4790676f68bbe8769205045dbb3ba7b87790aa5e7a8b3b501a9b7b165`

## Registry Links

- `V.C06` — Defect entropy reaches zero
- `V.D85` — Defect partition of paths
- `V.D86` — Defect entropy
- `V.D87` — Refinement entropy
- `V.P27` — Readout projects onto total entropy
- `V.P28` — iota_tau controls the splitting ratio
- `V.P29` — Defect entropy from defect functional
- `V.R119` — Why varepsilon is harmless
- `V.R120` — The paradox resolved
- `V.R121` — The 99.99% that is noise
- `V.R122` — The Penrose puzzle
- `V.T56` — Entropy splitting
- `V.T57` — Defect entropy is bounded
- `V.T58` — Defect entropy is monotonically decreasing
- `V.T59` — Refinement entropy grows without bound

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Thermodynamics.Inversion`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Thermodynamics.DefectExhaustion`

## Declaration Counts

- `def`: 5
- `eval`: 5
- `structure`: 7
- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [DefectPartitionOfPaths](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-partition-of-paths/) | L68-L79 | defined | `V.D85` |
| `theorem` | [partition_exhaustive](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/partition-exhaustive/) | L82-L83 | formalized | — |
| `structure` | [MacroDefectEntropy](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-defect-entropy/) | L97-L106 | defined | `V.D86` |
| `def` | [MacroDefectEntropy.toFloat](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/to-float/) | L109-L110 | defined | — |
| `structure` | [MacroRefinementEntropy](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-refinement-entropy/) | L123-L132 | defined | `V.D87` |
| `def` | [MacroRefinementEntropy.toFloat](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/to-float-l135/) | L135-L136 | defined | — |
| `structure` | [MacroEntropySplitThm](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-entropy-split-thm/) | L150-L163 | defined | `V.T56` |
| `def` | [MacroEntropySplitThm.totalFloat](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/total-float/) | L166-L168 | defined | — |
| `theorem` | [defect_entropy_bounded](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-bounded/) | L176-L179 | formalized | `V.T57` |
| `theorem` | [defect_entropy_monotone](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-monotone/) | L190-L191 | formalized | `V.T58` |
| `theorem` | [defect_entropy_reaches_zero](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-reaches-zero/) | L202-L204 | formalized | `V.C06` |
| `theorem` | [refinement_entropy_unbounded](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/refinement-entropy-unbounded/) | L215-L217 | formalized | `V.T59` |
| `structure` | [ReadoutProjection](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/readout-projection/) | L229-L234 | defined | `V.P27` |
| `structure` | [SplittingRatioControl](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/splitting-ratio-control/) | L245-L250 | defined | `V.P28` |
| `structure` | [DefectEntropyFromFunctional](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-from-functional/) | L261-L266 | defined | `V.P29` |
| `theorem` | [paradox_resolved](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/paradox-resolved/) | L277-L279 | formalized | `V.R119`, `V.R120` |
| `theorem` | [noise_dominance](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/noise-dominance/) | L283-L285 | formalized | `V.R121` |
| `def` | [example_early_split](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/example-early-split/) | L295-L301 | defined | — |
| `eval` | [#eval L303](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l303/) | L303-L303 | computed | — |
| `eval` | [#eval L304](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l304/) | L304-L304 | computed | — |
| `eval` | [#eval L305](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l305/) | L305-L305 | computed | — |
| `def` | [example_late_split](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/example-late-split/) | L308-L314 | defined | — |
| `eval` | [#eval L316](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l316/) | L316-L316 | computed | — |
| `eval` | [#eval L317](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/eval-l317/) | L317-L319 | computed | — |

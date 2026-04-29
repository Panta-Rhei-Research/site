---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Electroweak.EWProjection",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Electroweak.EWProjection`.",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_slug": "book-iv-electroweak-ewprojection",
  "book": "BookIV",
  "family": "Electroweak",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Electroweak/EWProjection.lean",
  "sha256": "b62c5f729b936a8a0e09a2b3cbd4e4eec7448bd14fed5328d3ca77283b56c13a",
  "imports": [
    "TauLib.BookIV.Sectors.ModeCensus",
    "TauLib.BookIV.Sectors.BoundaryFiltration",
    "TauLib.BookI.CF.WindowAlgebra"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.WeinbergNLO"
  ],
  "registry_ids": [
    "IV.D335",
    "IV.D336",
    "IV.P182",
    "IV.R392",
    "IV.T136",
    "IV.T137",
    "IV.T138"
  ],
  "declaration_counts": {
    "def": 7,
    "theorem": 11,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "def",
      "name": "isEWActive",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/is-ewactive/",
      "source_line_start": 66,
      "source_line_end": 70,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D335"
      ]
    },
    {
      "kind": "def",
      "name": "isStrong",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/is-strong/",
      "source_line_start": 73,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "isEWComplement",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/is-ewcomplement/",
      "source_line_start": 78,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ewActiveModes",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-active-modes/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D336"
      ]
    },
    {
      "kind": "def",
      "name": "strongModes",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/strong-modes/",
      "source_line_start": 90,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ewComplement",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-complement/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ew_active_count",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-active-count/",
      "source_line_start": 102,
      "source_line_end": 102,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "strong_mode_count",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/strong-mode-count/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ew_complement_count",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-complement-count/",
      "source_line_start": 108,
      "source_line_end": 108,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mode_partition_EW",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/mode-partition-ew/",
      "source_line_start": 116,
      "source_line_end": 116,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T136"
      ]
    },
    {
      "kind": "theorem",
      "name": "partition_consistent",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/partition-consistent/",
      "source_line_start": 119,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "partition_disjoint",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/partition-disjoint/",
      "source_line_start": 124,
      "source_line_end": 128,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ew_density_is_5_over_7",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-density-is-5-over-7/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T137"
      ]
    },
    {
      "kind": "theorem",
      "name": "ew_complement_characterization",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-complement-characterization/",
      "source_line_start": 146,
      "source_line_end": 154,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P182"
      ]
    },
    {
      "kind": "theorem",
      "name": "complement_structure",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/complement-structure/",
      "source_line_start": 158,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ew_density_equals_window_ratio",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-density-equals-window-ratio/",
      "source_line_start": 167,
      "source_line_end": 174,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T138"
      ]
    },
    {
      "kind": "theorem",
      "name": "strong_equals_solenoidal",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/strong-equals-solenoidal/",
      "source_line_start": 177,
      "source_line_end": 178,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_oq_b2_resolved",
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/remark-oq-b2-resolved/",
      "source_line_start": 195,
      "source_line_end": 197,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R392"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l203/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l204/",
      "source_line_start": 204,
      "source_line_end": 204,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l205/",
      "source_line_start": 205,
      "source_line_end": 205,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l208/",
      "source_line_start": 208,
      "source_line_end": 210,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean",
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
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Electroweak/EWProjection.lean`
- SHA-256: `b62c5f729b936a8a0e09a2b3cbd4e4eec7448bd14fed5328d3ca77283b56c13a`

## Registry Links

- `IV.D335` — EW-Active Mode
- `IV.D336` — EW 3-Way Partition
- `IV.P182` — Complement Characterization
- `IV.R392` — OQ-B2 Resolved
- `IV.T136` — EW Partition Theorem
- `IV.T137` — EW Density = 5/7
- `IV.T138` — EW–CF Bridge

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.ModeCensus`
- `TauLib.BookIV.Sectors.BoundaryFiltration`
- `TauLib.BookI.CF.WindowAlgebra`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.WeinbergNLO`

## Declaration Counts

- `def`: 7
- `eval`: 4
- `theorem`: 11

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [isEWActive](/verify/taulib/docs/book-iv-electroweak-ewprojection/is-ewactive/) | L66-L70 | defined | `IV.D335` |
| `def` | [isStrong](/verify/taulib/docs/book-iv-electroweak-ewprojection/is-strong/) | L73-L75 | defined | — |
| `def` | [isEWComplement](/verify/taulib/docs/book-iv-electroweak-ewprojection/is-ewcomplement/) | L78-L79 | defined | — |
| `def` | [ewActiveModes](/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-active-modes/) | L86-L87 | defined | `IV.D336` |
| `def` | [strongModes](/verify/taulib/docs/book-iv-electroweak-ewprojection/strong-modes/) | L90-L91 | defined | — |
| `def` | [ewComplement](/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-complement/) | L94-L95 | defined | — |
| `theorem` | [ew_active_count](/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-active-count/) | L102-L102 | formalized | — |
| `theorem` | [strong_mode_count](/verify/taulib/docs/book-iv-electroweak-ewprojection/strong-mode-count/) | L105-L105 | formalized | — |
| `theorem` | [ew_complement_count](/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-complement-count/) | L108-L108 | formalized | — |
| `theorem` | [mode_partition_EW](/verify/taulib/docs/book-iv-electroweak-ewprojection/mode-partition-ew/) | L116-L116 | formalized | `IV.T136` |
| `theorem` | [partition_consistent](/verify/taulib/docs/book-iv-electroweak-ewprojection/partition-consistent/) | L119-L121 | formalized | — |
| `theorem` | [partition_disjoint](/verify/taulib/docs/book-iv-electroweak-ewprojection/partition-disjoint/) | L124-L128 | formalized | — |
| `theorem` | [ew_density_is_5_over_7](/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-density-is-5-over-7/) | L137-L138 | formalized | `IV.T137` |
| `theorem` | [ew_complement_characterization](/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-complement-characterization/) | L146-L154 | formalized | `IV.P182` |
| `theorem` | [complement_structure](/verify/taulib/docs/book-iv-electroweak-ewprojection/complement-structure/) | L158-L158 | formalized | — |
| `theorem` | [ew_density_equals_window_ratio](/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-density-equals-window-ratio/) | L167-L174 | formalized | `IV.T138` |
| `theorem` | [strong_equals_solenoidal](/verify/taulib/docs/book-iv-electroweak-ewprojection/strong-equals-solenoidal/) | L177-L178 | formalized | — |
| `def` | [remark_oq_b2_resolved](/verify/taulib/docs/book-iv-electroweak-ewprojection/remark-oq-b2-resolved/) | L195-L197 | defined | `IV.R392` |
| `eval` | [#eval L203](/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l203/) | L203-L203 | computed | — |
| `eval` | [#eval L204](/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l204/) | L204-L204 | computed | — |
| `eval` | [#eval L205](/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l205/) | L205-L205 | computed | — |
| `eval` | [#eval L208](/verify/taulib/docs/book-iv-electroweak-ewprojection/eval-l208/) | L208-L210 | computed | — |

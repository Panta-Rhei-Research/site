---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Arena.CoherenceKernel",
  "permalink": "/verify/taulib/docs/book-iv-arena-coherence-kernel/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Arena.CoherenceKernel`.",
  "module_name": "TauLib.BookIV.Arena.CoherenceKernel",
  "module_slug": "book-iv-arena-coherence-kernel",
  "book": "BookIV",
  "family": "Arena",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Arena/CoherenceKernel.lean",
  "sha256": "71bf5599498889dc4d6593bf402f77152b52c968d3429efdd43b90a9f8fd5416",
  "imports": [
    "TauLib.BookIV.Sectors.SectorParameters",
    "TauLib.BookI.Boundary.Iota"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.RefinementTower"
  ],
  "registry_ids": [
    "IV.D246",
    "IV.D247",
    "IV.D248",
    "IV.P146"
  ],
  "declaration_counts": {
    "def": 6,
    "theorem": 8,
    "structure": 1,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "def",
      "name": "GenSectorAssignment",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/gen-sector-assignment/",
      "source_line_start": 39,
      "source_line_end": 45,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D247"
      ]
    },
    {
      "kind": "theorem",
      "name": "assignment_injective",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-injective/",
      "source_line_start": 48,
      "source_line_end": 59,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "assignment_surjective",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-surjective/",
      "source_line_start": 62,
      "source_line_end": 69,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoherenceKernel",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/coherence-kernel/",
      "source_line_start": 78,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D246"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_kernel",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/canonical-kernel/",
      "source_line_start": 90,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gen_polarity",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/gen-polarity/",
      "source_line_start": 102,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gen_depth",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/gen-depth/",
      "source_line_start": 106,
      "source_line_end": 107,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_polarity",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/sp-polarity/",
      "source_line_start": 110,
      "source_line_end": 115,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sp_depth",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/sp-depth/",
      "source_line_start": 118,
      "source_line_end": 122,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "assignment_unique",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-unique/",
      "source_line_start": 127,
      "source_line_end": 136,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P146"
      ]
    },
    {
      "kind": "def",
      "name": "all_generators",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/all-generators/",
      "source_line_start": 143,
      "source_line_end": 143,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "covered_sectors",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/covered-sectors/",
      "source_line_start": 146,
      "source_line_end": 147,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ontic_minimality",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/ontic-minimality/",
      "source_line_start": 151,
      "source_line_end": 167,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D248"
      ]
    },
    {
      "kind": "theorem",
      "name": "kernel_generator_count",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/kernel-generator-count/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "assignment_agrees_with_params",
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-agrees-with-params/",
      "source_line_start": 176,
      "source_line_end": 182,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l188/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l189/",
      "source_line_start": 189,
      "source_line_end": 189,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l190/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l191/",
      "source_line_start": 191,
      "source_line_end": 191,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l192/",
      "source_line_start": 192,
      "source_line_end": 192,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l193/",
      "source_line_start": 193,
      "source_line_end": 193,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l196/",
      "source_line_start": 196,
      "source_line_end": 196,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l197/",
      "source_line_start": 197,
      "source_line_end": 199,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean",
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
- Source path: [`TauLib/BookIV/Arena/CoherenceKernel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/CoherenceKernel.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Arena/CoherenceKernel.lean`
- SHA-256: `71bf5599498889dc4d6593bf402f77152b52c968d3429efdd43b90a9f8fd5416`

## Registry Links

- `IV.D246` — Coherence Kernel --- Physics Presentation
- `IV.D247` — Generator--Sector Assignment
- `IV.D248` — Ontic Minimality
- `IV.P146` — Uniqueness of Assignment

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.SectorParameters`
- `TauLib.BookI.Boundary.Iota`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.RefinementTower`

## Declaration Counts

- `def`: 6
- `eval`: 10
- `structure`: 1
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [GenSectorAssignment](/verify/taulib/docs/book-iv-arena-coherence-kernel/gen-sector-assignment/) | L39-L45 | defined | `IV.D247` |
| `theorem` | [assignment_injective](/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-injective/) | L48-L59 | formalized | — |
| `theorem` | [assignment_surjective](/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-surjective/) | L62-L69 | formalized | — |
| `structure` | [CoherenceKernel](/verify/taulib/docs/book-iv-arena-coherence-kernel/coherence-kernel/) | L78-L87 | defined | `IV.D246` |
| `def` | [canonical_kernel](/verify/taulib/docs/book-iv-arena-coherence-kernel/canonical-kernel/) | L90-L95 | defined | — |
| `def` | [gen_polarity](/verify/taulib/docs/book-iv-arena-coherence-kernel/gen-polarity/) | L102-L103 | defined | — |
| `def` | [gen_depth](/verify/taulib/docs/book-iv-arena-coherence-kernel/gen-depth/) | L106-L107 | defined | — |
| `theorem` | [sp_polarity](/verify/taulib/docs/book-iv-arena-coherence-kernel/sp-polarity/) | L110-L115 | formalized | — |
| `theorem` | [sp_depth](/verify/taulib/docs/book-iv-arena-coherence-kernel/sp-depth/) | L118-L122 | formalized | — |
| `theorem` | [assignment_unique](/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-unique/) | L127-L136 | formalized | `IV.P146` |
| `def` | [all_generators](/verify/taulib/docs/book-iv-arena-coherence-kernel/all-generators/) | L143-L143 | defined | — |
| `def` | [covered_sectors](/verify/taulib/docs/book-iv-arena-coherence-kernel/covered-sectors/) | L146-L147 | defined | — |
| `theorem` | [ontic_minimality](/verify/taulib/docs/book-iv-arena-coherence-kernel/ontic-minimality/) | L151-L167 | formalized | `IV.D248` |
| `theorem` | [kernel_generator_count](/verify/taulib/docs/book-iv-arena-coherence-kernel/kernel-generator-count/) | L169-L169 | formalized | — |
| `theorem` | [assignment_agrees_with_params](/verify/taulib/docs/book-iv-arena-coherence-kernel/assignment-agrees-with-params/) | L176-L182 | formalized | — |
| `eval` | [#eval L188](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l188/) | L188-L188 | computed | — |
| `eval` | [#eval L189](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l189/) | L189-L189 | computed | — |
| `eval` | [#eval L190](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l190/) | L190-L190 | computed | — |
| `eval` | [#eval L191](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l191/) | L191-L191 | computed | — |
| `eval` | [#eval L192](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l192/) | L192-L192 | computed | — |
| `eval` | [#eval L193](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l193/) | L193-L193 | computed | — |
| `eval` | [#eval L194](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l194/) | L194-L194 | computed | — |
| `eval` | [#eval L195](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l195/) | L195-L195 | computed | — |
| `eval` | [#eval L196](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l196/) | L196-L196 | computed | — |
| `eval` | [#eval L197](/verify/taulib/docs/book-iv-arena-coherence-kernel/eval-l197/) | L197-L199 | computed | — |

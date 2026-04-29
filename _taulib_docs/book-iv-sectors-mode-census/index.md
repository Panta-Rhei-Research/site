---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Sectors.ModeCensus",
  "permalink": "/verify/taulib/docs/book-iv-sectors-mode-census/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Sectors.ModeCensus`.",
  "module_name": "TauLib.BookIV.Sectors.ModeCensus",
  "module_slug": "book-iv-sectors-mode-census",
  "book": "BookIV",
  "family": "Sectors",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Sectors/ModeCensus.lean",
  "sha256": "30b7c854a59c09475e73b207c3167f210ec5eeb8539ef68848abe43c383f8969",
  "imports": [],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.EWProjection",
    "TauLib.BookIV.Sectors.BoundaryFiltration",
    "TauLib.BookIV.Sectors.SpectralPage"
  ],
  "registry_ids": [
    "IV.D49",
    "IV.P08",
    "IV.T16"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 1,
    "def": 4,
    "theorem": 9,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "Gen5",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/gen5/",
      "source_line_start": 45,
      "source_line_end": 51,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "LobeConfig",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/lobe-config/",
      "source_line_start": 54,
      "source_line_end": 58,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BoundaryMode",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/boundary-mode/",
      "source_line_start": 62,
      "source_line_end": 65,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D49"
      ]
    },
    {
      "kind": "def",
      "name": "BoundaryMode.emActive",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/em-active/",
      "source_line_start": 79,
      "source_line_end": 86,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allModes",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/all-modes/",
      "source_line_start": 93,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D49"
      ]
    },
    {
      "kind": "def",
      "name": "activeModes",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/active-modes/",
      "source_line_start": 101,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "silentModes",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/silent-modes/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mode_total",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/mode-total/",
      "source_line_start": 111,
      "source_line_end": 111,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T16"
      ]
    },
    {
      "kind": "theorem",
      "name": "active_count",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/active-count/",
      "source_line_start": 114,
      "source_line_end": 114,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T16"
      ]
    },
    {
      "kind": "theorem",
      "name": "silent_count",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/silent-count/",
      "source_line_start": 117,
      "source_line_end": 117,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T16"
      ]
    },
    {
      "kind": "theorem",
      "name": "active_plus_silent",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/active-plus-silent/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "charge_fraction_square",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/charge-fraction-square/",
      "source_line_start": 129,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P08"
      ]
    },
    {
      "kind": "theorem",
      "name": "silent_modes_are_gravity_plus_Z0",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/silent-modes-are-gravity-plus-z0/",
      "source_line_start": 132,
      "source_line_end": 137,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_sieve_identity",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/euler-sieve-identity/",
      "source_line_start": 145,
      "source_line_end": 146,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "s5_correction",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/s5-correction/",
      "source_line_start": 149,
      "source_line_end": 149,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mode_product",
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/mode-product/",
      "source_line_start": 152,
      "source_line_end": 152,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/eval-l158/",
      "source_line_start": 158,
      "source_line_end": 158,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/eval-l159/",
      "source_line_start": 159,
      "source_line_end": 159,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-sectors-mode-census/eval-l160/",
      "source_line_start": 160,
      "source_line_end": 162,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean",
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
- Source path: [`TauLib/BookIV/Sectors/ModeCensus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Sectors/ModeCensus.lean`
- SHA-256: `30b7c854a59c09475e73b207c3167f210ec5eeb8539ef68848abe43c383f8969`

## Registry Links

- `IV.D49` — CR-Manifold
- `IV.P08` — Integrability Criterion
- `IV.T16` — CR Parity Constraint

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- This module has no Lean imports.

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.EWProjection`
- `TauLib.BookIV.Sectors.BoundaryFiltration`
- `TauLib.BookIV.Sectors.SpectralPage`

## Declaration Counts

- `def`: 4
- `eval`: 3
- `inductive`: 2
- `structure`: 1
- `theorem`: 9

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [Gen5](/verify/taulib/docs/book-iv-sectors-mode-census/gen5/) | L45-L51 | defined | — |
| `inductive` | [LobeConfig](/verify/taulib/docs/book-iv-sectors-mode-census/lobe-config/) | L54-L58 | defined | — |
| `structure` | [BoundaryMode](/verify/taulib/docs/book-iv-sectors-mode-census/boundary-mode/) | L62-L65 | defined | `IV.D49` |
| `def` | [BoundaryMode.emActive](/verify/taulib/docs/book-iv-sectors-mode-census/em-active/) | L79-L86 | defined | — |
| `def` | [allModes](/verify/taulib/docs/book-iv-sectors-mode-census/all-modes/) | L93-L98 | defined | `IV.D49` |
| `def` | [activeModes](/verify/taulib/docs/book-iv-sectors-mode-census/active-modes/) | L101-L101 | defined | — |
| `def` | [silentModes](/verify/taulib/docs/book-iv-sectors-mode-census/silent-modes/) | L104-L104 | defined | — |
| `theorem` | [mode_total](/verify/taulib/docs/book-iv-sectors-mode-census/mode-total/) | L111-L111 | formalized | `IV.T16` |
| `theorem` | [active_count](/verify/taulib/docs/book-iv-sectors-mode-census/active-count/) | L114-L114 | formalized | `IV.T16` |
| `theorem` | [silent_count](/verify/taulib/docs/book-iv-sectors-mode-census/silent-count/) | L117-L117 | formalized | `IV.T16` |
| `theorem` | [active_plus_silent](/verify/taulib/docs/book-iv-sectors-mode-census/active-plus-silent/) | L120-L121 | formalized | — |
| `theorem` | [charge_fraction_square](/verify/taulib/docs/book-iv-sectors-mode-census/charge-fraction-square/) | L129-L129 | formalized | `IV.P08` |
| `theorem` | [silent_modes_are_gravity_plus_Z0](/verify/taulib/docs/book-iv-sectors-mode-census/silent-modes-are-gravity-plus-z0/) | L132-L137 | formalized | — |
| `theorem` | [euler_sieve_identity](/verify/taulib/docs/book-iv-sectors-mode-census/euler-sieve-identity/) | L145-L146 | formalized | — |
| `theorem` | [s5_correction](/verify/taulib/docs/book-iv-sectors-mode-census/s5-correction/) | L149-L149 | formalized | — |
| `theorem` | [mode_product](/verify/taulib/docs/book-iv-sectors-mode-census/mode-product/) | L152-L152 | formalized | — |
| `eval` | [#eval L158](/verify/taulib/docs/book-iv-sectors-mode-census/eval-l158/) | L158-L158 | computed | — |
| `eval` | [#eval L159](/verify/taulib/docs/book-iv-sectors-mode-census/eval-l159/) | L159-L159 | computed | — |
| `eval` | [#eval L160](/verify/taulib/docs/book-iv-sectors-mode-census/eval-l160/) | L160-L162 | computed | — |

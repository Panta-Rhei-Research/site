---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.Interior.BipolarDecomposition",
  "permalink": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.Interior.BipolarDecomposition`.",
  "module_name": "TauLib.BookII.Interior.BipolarDecomposition",
  "module_slug": "book-ii-interior-bipolar-decomposition",
  "book": "BookII",
  "family": "Interior",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/Interior/BipolarDecomposition.lean",
  "sha256": "1159b9f75c063f3ec8a0f26771af4697dc6f030cf5479bdd879dbf152308cc75",
  "imports": [
    "TauLib.BookII.Interior.Tau3Fibration",
    "TauLib.BookII.Interior.OmegaReadout",
    "TauLib.BookI.Polarity.BipolarAlgebra",
    "TauLib.BookI.Boundary.SplitComplex"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.Hartogs.MutualDetermination",
    "TauLib.BookII.Interior.ABCDRigidity",
    "TauLib.BookII.Topology.BoundaryMinimality",
    "TauLib.BookII.Transcendentals.JReplacesI"
  ],
  "registry_ids": [
    "II.D08",
    "II.P02"
  ],
  "declaration_counts": {
    "def": 8,
    "theorem": 3,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "def",
      "name": "interior_bipolar",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/interior-bipolar/",
      "source_line_start": 48,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "II.D08"
      ]
    },
    {
      "kind": "def",
      "name": "s_plus",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/s-plus/",
      "source_line_start": 52,
      "source_line_end": 52,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "s_minus",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/s-minus/",
      "source_line_start": 55,
      "source_line_end": 55,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "interior_split_complex",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/interior-split-complex/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_orthogonal",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-orthogonal/",
      "source_line_start": 72,
      "source_line_end": 74,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_orthogonal'",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-orthogonal-l76/",
      "source_line_start": 76,
      "source_line_end": 78,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_complete",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-complete/",
      "source_line_start": 83,
      "source_line_end": 89,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sector_lobe",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-lobe/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "char_plus",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/char-plus/",
      "source_line_start": 103,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "char_minus",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/char-minus/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "char_to_sectors",
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/char-to-sectors/",
      "source_line_start": 113,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l121/",
      "source_line_start": 121,
      "source_line_end": 121,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l122/",
      "source_line_start": 122,
      "source_line_end": 122,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l123/",
      "source_line_start": 123,
      "source_line_end": 123,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l126/",
      "source_line_start": 126,
      "source_line_end": 126,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l129/",
      "source_line_start": 129,
      "source_line_end": 129,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l130/",
      "source_line_start": 130,
      "source_line_end": 130,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l133/",
      "source_line_start": 133,
      "source_line_end": 133,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l134/",
      "source_line_start": 134,
      "source_line_end": 136,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean",
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
- Source path: [`TauLib/BookII/Interior/BipolarDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/Interior/BipolarDecomposition.lean`
- SHA-256: `1159b9f75c063f3ec8a0f26771af4697dc6f030cf5479bdd879dbf152308cc75`

## Registry Links

- `II.D08` — Interior Bipolar Decomposition
- `II.P02` — Sector Inheritance

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Interior.Tau3Fibration`
- `TauLib.BookII.Interior.OmegaReadout`
- `TauLib.BookI.Polarity.BipolarAlgebra`
- `TauLib.BookI.Boundary.SplitComplex`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.Hartogs.MutualDetermination`
- `TauLib.BookII.Interior.ABCDRigidity`
- `TauLib.BookII.Topology.BoundaryMinimality`
- `TauLib.BookII.Transcendentals.JReplacesI`

## Declaration Counts

- `def`: 8
- `eval`: 8
- `theorem`: 3

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [interior_bipolar](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/interior-bipolar/) | L48-L49 | definition | definition | `II.D08` |
| `def` | [s_plus](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/s-plus/) | L52-L52 | data/computed value | data/computed value | — |
| `def` | [s_minus](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/s-minus/) | L55-L55 | data/computed value | data/computed value | — |
| `def` | [interior_split_complex](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/interior-split-complex/) | L58-L59 | definition | definition | — |
| `theorem` | [sector_orthogonal](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-orthogonal/) | L72-L74 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sector_orthogonal'](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-orthogonal-l76/) | L76-L78 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sector_complete](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-complete/) | L83-L89 | proof obligation | formal proof obligation checked | — |
| `def` | [sector_lobe](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/sector-lobe/) | L93-L94 | definition | definition | — |
| `def` | [char_plus](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/char-plus/) | L103-L103 | data/computed value | data/computed value | — |
| `def` | [char_minus](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/char-minus/) | L104-L104 | data/computed value | data/computed value | — |
| `def` | [char_to_sectors](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/char-to-sectors/) | L113-L114 | definition | definition | — |
| `eval` | [#eval L121](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l121/) | L121-L121 | computed check | computed check | — |
| `eval` | [#eval L122](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l122/) | L122-L122 | computed check | computed check | — |
| `eval` | [#eval L123](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l123/) | L123-L123 | computed check | computed check | — |
| `eval` | [#eval L126](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l126/) | L126-L126 | computed check | computed check | — |
| `eval` | [#eval L129](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l129/) | L129-L129 | computed check | computed check | — |
| `eval` | [#eval L130](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l130/) | L130-L130 | computed check | computed check | — |
| `eval` | [#eval L133](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l133/) | L133-L133 | computed check | computed check | — |
| `eval` | [#eval L134](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/eval-l134/) | L134-L136 | computed check | computed check | — |

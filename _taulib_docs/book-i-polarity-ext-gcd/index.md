---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.ExtGCD",
  "permalink": "/verify/taulib/docs/book-i-polarity-ext-gcd/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Polarity.ExtGCD`.",
  "module_name": "TauLib.BookI.Polarity.ExtGCD",
  "module_slug": "book-i-polarity-ext-gcd",
  "book": "BookI",
  "family": "Polarity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Polarity/ExtGCD.lean",
  "sha256": "261df7d3ec661844259ebc176b298d52ae89ebad3c1561e67cb8d71fc9d47473",
  "imports": [
    "TauLib.BookI.Polarity.ModArith",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Polarity.ChineseRemainder"
  ],
  "registry_ids": [],
  "declaration_counts": {
    "def": 1,
    "theorem": 4,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "def",
      "name": "ext_gcd",
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd/",
      "source_line_start": 27,
      "source_line_end": 33,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ext_gcd_fst",
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-fst/",
      "source_line_start": 40,
      "source_line_end": 53,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ext_gcd_bezout",
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-bezout/",
      "source_line_start": 56,
      "source_line_end": 78,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ext_gcd_spec",
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-spec/",
      "source_line_start": 81,
      "source_line_end": 84,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_inv_exists",
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/mod-inv-exists/",
      "source_line_start": 91,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/eval-l136/",
      "source_line_start": 136,
      "source_line_end": 136,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/eval-l137/",
      "source_line_start": 137,
      "source_line_end": 137,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/eval-l138/",
      "source_line_start": 138,
      "source_line_end": 140,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean",
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
- Source path: [`TauLib/BookI/Polarity/ExtGCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Polarity/ExtGCD.lean`
- SHA-256: `261df7d3ec661844259ebc176b298d52ae89ebad3c1561e67cb8d71fc9d47473`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.ModArith`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Polarity.ChineseRemainder`

## Declaration Counts

- `def`: 1
- `eval`: 3
- `theorem`: 4

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [ext_gcd](/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd/) | L27-L33 | defined | — |
| `theorem` | [ext_gcd_fst](/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-fst/) | L40-L53 | formalized | — |
| `theorem` | [ext_gcd_bezout](/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-bezout/) | L56-L78 | formalized | — |
| `theorem` | [ext_gcd_spec](/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-spec/) | L81-L84 | formalized | — |
| `theorem` | [mod_inv_exists](/verify/taulib/docs/book-i-polarity-ext-gcd/mod-inv-exists/) | L91-L130 | formalized | — |
| `eval` | [#eval L136](/verify/taulib/docs/book-i-polarity-ext-gcd/eval-l136/) | L136-L136 | computed | — |
| `eval` | [#eval L137](/verify/taulib/docs/book-i-polarity-ext-gcd/eval-l137/) | L137-L137 | computed | — |
| `eval` | [#eval L138](/verify/taulib/docs/book-i-polarity-ext-gcd/eval-l138/) | L138-L140 | computed | — |

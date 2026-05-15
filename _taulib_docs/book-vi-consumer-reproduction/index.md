---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.Consumer.Reproduction",
  "permalink": "/corpus/taulib/docs/book-vi-consumer-reproduction/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.Consumer.Reproduction`.",
  "module_name": "TauLib.BookVI.Consumer.Reproduction",
  "module_slug": "book-vi-consumer-reproduction",
  "book": "BookVI",
  "family": "Consumer",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/Consumer/Reproduction.lean",
  "sha256": "62481c208ad51b69c041a4ae591dd9d10c0055b64b272a0d2acc665f5108a78b",
  "imports": [
    "TauLib.BookVI.Consumer.ConsumerMixer"
  ],
  "imported_by": [
    "TauLib.BookVI",
    "TauLib.BookVI.Consumer.Evolution"
  ],
  "registry_ids": [
    "VI.D49",
    "VI.T26"
  ],
  "declaration_counts": {
    "structure": 2,
    "def": 2,
    "theorem": 2
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "RecombinationFunctor",
      "url": "/corpus/taulib/docs/book-vi-consumer-reproduction/recombination-functor/",
      "source_line_start": 34,
      "source_line_end": 47,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.D49"
      ]
    },
    {
      "kind": "def",
      "name": "recomb",
      "url": "/corpus/taulib/docs/book-vi-consumer-reproduction/recomb/",
      "source_line_start": 49,
      "source_line_end": 53,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recombination_is_functor",
      "url": "/corpus/taulib/docs/book-vi-consumer-reproduction/recombination-is-functor/",
      "source_line_start": 55,
      "source_line_end": 60,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SecondDistinction",
      "url": "/corpus/taulib/docs/book-vi-consumer-reproduction/second-distinction/",
      "source_line_start": 70,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.T26"
      ]
    },
    {
      "kind": "def",
      "name": "second_dist",
      "url": "/corpus/taulib/docs/book-vi-consumer-reproduction/second-dist/",
      "source_line_start": 81,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sex_is_second_distinction",
      "url": "/corpus/taulib/docs/book-vi-consumer-reproduction/sex-is-second-distinction/",
      "source_line_start": 85,
      "source_line_end": 91,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean",
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
- Source path: [`TauLib/BookVI/Consumer/Reproduction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Reproduction.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/Consumer/Reproduction.lean`
- SHA-256: `62481c208ad51b69c041a4ae591dd9d10c0055b64b272a0d2acc665f5108a78b`

## Registry Links

- `VI.D49` — Recombination Functor
- `VI.T26` — Sex as Second Distinction

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.Consumer.ConsumerMixer`

## Imported By

- `TauLib.BookVI`
- `TauLib.BookVI.Consumer.Evolution`

## Declaration Counts

- `def`: 2
- `structure`: 2
- `theorem`: 2

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [RecombinationFunctor](/corpus/taulib/docs/book-vi-consumer-reproduction/recombination-functor/) | L34-L47 | type/data schema | type/data schema | `VI.D49` |
| `def` | [recomb](/corpus/taulib/docs/book-vi-consumer-reproduction/recomb/) | L49-L53 | definition | definition | — |
| `theorem` | [recombination_is_functor](/corpus/taulib/docs/book-vi-consumer-reproduction/recombination-is-functor/) | L55-L60 | proof obligation | formal proof obligation checked | — |
| `structure` | [SecondDistinction](/corpus/taulib/docs/book-vi-consumer-reproduction/second-distinction/) | L70-L79 | type/data schema | type/data schema | `VI.T26` |
| `def` | [second_dist](/corpus/taulib/docs/book-vi-consumer-reproduction/second-dist/) | L81-L83 | definition | definition | — |
| `theorem` | [sex_is_second_distinction](/corpus/taulib/docs/book-vi-consumer-reproduction/sex-is-second-distinction/) | L85-L91 | proof obligation | formal proof obligation checked | — |

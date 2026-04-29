---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Orbit.Saturation",
  "permalink": "/verify/taulib/docs/book-i-orbit-saturation/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Orbit.Saturation`.",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_slug": "book-i-orbit-saturation",
  "book": "BookI",
  "family": "Orbit",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Orbit/Saturation.lean",
  "sha256": "e676842095e8b34a36d26ea16f7506643197887bcbb1e1d941c98f462ac9b506",
  "imports": [
    "TauLib.BookI.Orbit.TooMany",
    "TauLib.BookI.Orbit.TooFew",
    "TauLib.BookI.Orbit.Ladder"
  ],
  "imported_by": [
    "TauLib.BookI"
  ],
  "registry_ids": [
    "I.T09",
    "I.T11"
  ],
  "declaration_counts": {
    "theorem": 7,
    "structure": 2
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "tetration_non_comm",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/tetration-non-comm/",
      "source_line_start": 38,
      "source_line_end": 39,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tetration_non_assoc",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/tetration-non-assoc/",
      "source_line_start": 43,
      "source_line_end": 45,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tetration_no_left_identity",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/tetration-no-left-identity/",
      "source_line_start": 57,
      "source_line_end": 67,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "lower_ops_have_identities",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/lower-ops-have-identities/",
      "source_line_start": 72,
      "source_line_end": 74,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AlgebraicDegradation",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/algebraic-degradation/",
      "source_line_start": 83,
      "source_line_end": 86,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tetration_algebraic_degradation",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/tetration-algebraic-degradation/",
      "source_line_start": 90,
      "source_line_end": 91,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MinimalAlphabetSpec",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/minimal-alphabet-spec/",
      "source_line_start": 98,
      "source_line_end": 110,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_gen_spec",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/five-gen-spec/",
      "source_line_start": 113,
      "source_line_end": 119,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "minimal_alphabet",
      "url": "/verify/taulib/docs/book-i-orbit-saturation/minimal-alphabet/",
      "source_line_start": 146,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T09"
      ]
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean",
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
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Orbit/Saturation.lean`
- SHA-256: `e676842095e8b34a36d26ea16f7506643197887bcbb1e1d941c98f462ac9b506`

## Registry Links

- `I.T09` — FTA on tau-Idx
- `I.T11` — Minimal Alphabet Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Orbit.TooMany`
- `TauLib.BookI.Orbit.TooFew`
- `TauLib.BookI.Orbit.Ladder`

## Imported By

- `TauLib.BookI`

## Declaration Counts

- `structure`: 2
- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [tetration_non_comm](/verify/taulib/docs/book-i-orbit-saturation/tetration-non-comm/) | L38-L39 | formalized | — |
| `theorem` | [tetration_non_assoc](/verify/taulib/docs/book-i-orbit-saturation/tetration-non-assoc/) | L43-L45 | formalized | — |
| `theorem` | [tetration_no_left_identity](/verify/taulib/docs/book-i-orbit-saturation/tetration-no-left-identity/) | L57-L67 | formalized | — |
| `theorem` | [lower_ops_have_identities](/verify/taulib/docs/book-i-orbit-saturation/lower-ops-have-identities/) | L72-L74 | formalized | — |
| `structure` | [AlgebraicDegradation](/verify/taulib/docs/book-i-orbit-saturation/algebraic-degradation/) | L83-L86 | defined | — |
| `theorem` | [tetration_algebraic_degradation](/verify/taulib/docs/book-i-orbit-saturation/tetration-algebraic-degradation/) | L90-L91 | formalized | — |
| `structure` | [MinimalAlphabetSpec](/verify/taulib/docs/book-i-orbit-saturation/minimal-alphabet-spec/) | L98-L110 | defined | — |
| `theorem` | [five_gen_spec](/verify/taulib/docs/book-i-orbit-saturation/five-gen-spec/) | L113-L119 | formalized | — |
| `theorem` | [minimal_alphabet](/verify/taulib/docs/book-i-orbit-saturation/minimal-alphabet/) | L146-L163 | formalized | `I.T09` |

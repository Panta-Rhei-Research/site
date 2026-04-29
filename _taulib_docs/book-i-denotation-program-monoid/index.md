---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Denotation.ProgramMonoid",
  "permalink": "/verify/taulib/docs/book-i-denotation-program-monoid/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Denotation.ProgramMonoid`.",
  "module_name": "TauLib.BookI.Denotation.ProgramMonoid",
  "module_slug": "book-i-denotation-program-monoid",
  "book": "BookI",
  "family": "Denotation",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Denotation/ProgramMonoid.lean",
  "sha256": "d960fe40611fab2780fb582b968fab1b0a38e1269dafc982a1e18d86ad9aaf4a",
  "imports": [
    "TauLib.BookI.Denotation.Arithmetic"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Addressability.CayleyMetric",
    "TauLib.BookI.Denotation.Equality",
    "TauLib.BookI.MetaLogic.LinearDiscipline",
    "TauLib.BookIII.Spectrum.TTM"
  ],
  "registry_ids": [
    "I.D14",
    "I.L02",
    "I.T03"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 7,
    "structure": 1,
    "theorem": 9
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "Instruction",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/instruction/",
      "source_line_start": 37,
      "source_line_end": 43,
      "formal_status": "defined",
      "registry_ids": [
        "I.D14"
      ]
    },
    {
      "kind": "def",
      "name": "execInstruction",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/exec-instruction/",
      "source_line_start": 46,
      "source_line_end": 49,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "execProgram",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/exec-program/",
      "source_line_start": 52,
      "source_line_end": 53,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NormalForm",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/normal-form/",
      "source_line_start": 60,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "countRho",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/count-rho/",
      "source_line_start": 65,
      "source_line_end": 68,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "NormalForm.id",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/id/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "NormalForm.compose",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/compose/",
      "source_line_start": 76,
      "source_line_end": 78,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "execNF",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/exec-nf/",
      "source_line_start": 81,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Program.compose",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/compose-l90/",
      "source_line_start": 90,
      "source_line_end": 90,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "compose_assoc",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/compose-assoc/",
      "source_line_start": 93,
      "source_line_end": 95,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T03"
      ]
    },
    {
      "kind": "theorem",
      "name": "compose_id_left",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/compose-id-left/",
      "source_line_start": 98,
      "source_line_end": 100,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "compose_id_right",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/compose-id-right/",
      "source_line_start": 103,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_compose",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/exec-compose/",
      "source_line_start": 112,
      "source_line_end": 114,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_nil",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/exec-nil/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_rho",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/exec-rho/",
      "source_line_start": 121,
      "source_line_end": 123,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_sigma",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/exec-sigma/",
      "source_line_start": 126,
      "source_line_end": 128,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rho_count_compose",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/rho-count-compose/",
      "source_line_start": 136,
      "source_line_end": 149,
      "formal_status": "formalized",
      "registry_ids": [
        "I.L02"
      ]
    },
    {
      "kind": "theorem",
      "name": "rho_count_nil",
      "url": "/verify/taulib/docs/book-i-denotation-program-monoid/rho-count-nil/",
      "source_line_start": 152,
      "source_line_end": 154,
      "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean",
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
- Source path: [`TauLib/BookI/Denotation/ProgramMonoid.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/ProgramMonoid.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Denotation/ProgramMonoid.lean`
- SHA-256: `d960fe40611fab2780fb582b968fab1b0a38e1269dafc982a1e18d86ad9aaf4a`

## Registry Links

- `I.D14` — Program Monoid
- `I.L02` — NF-Confluence
- `I.T03` — Composition Associativity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Denotation.Arithmetic`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Addressability.CayleyMetric`
- `TauLib.BookI.Denotation.Equality`
- `TauLib.BookI.MetaLogic.LinearDiscipline`
- `TauLib.BookIII.Spectrum.TTM`

## Declaration Counts

- `def`: 7
- `inductive`: 1
- `structure`: 1
- `theorem`: 9

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [Instruction](/verify/taulib/docs/book-i-denotation-program-monoid/instruction/) | L37-L43 | defined | `I.D14` |
| `def` | [execInstruction](/verify/taulib/docs/book-i-denotation-program-monoid/exec-instruction/) | L46-L49 | defined | — |
| `def` | [execProgram](/verify/taulib/docs/book-i-denotation-program-monoid/exec-program/) | L52-L53 | defined | — |
| `structure` | [NormalForm](/verify/taulib/docs/book-i-denotation-program-monoid/normal-form/) | L60-L62 | defined | — |
| `def` | [countRho](/verify/taulib/docs/book-i-denotation-program-monoid/count-rho/) | L65-L68 | defined | — |
| `def` | [NormalForm.id](/verify/taulib/docs/book-i-denotation-program-monoid/id/) | L71-L73 | defined | — |
| `def` | [NormalForm.compose](/verify/taulib/docs/book-i-denotation-program-monoid/compose/) | L76-L78 | defined | — |
| `def` | [execNF](/verify/taulib/docs/book-i-denotation-program-monoid/exec-nf/) | L81-L83 | defined | — |
| `def` | [Program.compose](/verify/taulib/docs/book-i-denotation-program-monoid/compose-l90/) | L90-L90 | defined | — |
| `theorem` | [compose_assoc](/verify/taulib/docs/book-i-denotation-program-monoid/compose-assoc/) | L93-L95 | formalized | `I.T03` |
| `theorem` | [compose_id_left](/verify/taulib/docs/book-i-denotation-program-monoid/compose-id-left/) | L98-L100 | formalized | — |
| `theorem` | [compose_id_right](/verify/taulib/docs/book-i-denotation-program-monoid/compose-id-right/) | L103-L105 | formalized | — |
| `theorem` | [exec_compose](/verify/taulib/docs/book-i-denotation-program-monoid/exec-compose/) | L112-L114 | formalized | — |
| `theorem` | [exec_nil](/verify/taulib/docs/book-i-denotation-program-monoid/exec-nil/) | L117-L118 | formalized | — |
| `theorem` | [exec_rho](/verify/taulib/docs/book-i-denotation-program-monoid/exec-rho/) | L121-L123 | formalized | — |
| `theorem` | [exec_sigma](/verify/taulib/docs/book-i-denotation-program-monoid/exec-sigma/) | L126-L128 | formalized | — |
| `theorem` | [rho_count_compose](/verify/taulib/docs/book-i-denotation-program-monoid/rho-count-compose/) | L136-L149 | formalized | `I.L02` |
| `theorem` | [rho_count_nil](/verify/taulib/docs/book-i-denotation-program-monoid/rho-count-nil/) | L152-L154 | formalized | — |

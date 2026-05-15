---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Denotation.ProgramMonoid",
  "permalink": "/corpus/taulib/docs/book-i-denotation-program-monoid/",
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
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/instruction/",
      "source_line_start": 37,
      "source_line_end": 43,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D14"
      ]
    },
    {
      "kind": "def",
      "name": "execInstruction",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-instruction/",
      "source_line_start": 46,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "execProgram",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-program/",
      "source_line_start": 52,
      "source_line_end": 53,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NormalForm",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/normal-form/",
      "source_line_start": 60,
      "source_line_end": 62,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "countRho",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/count-rho/",
      "source_line_start": 65,
      "source_line_end": 68,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "NormalForm.id",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/id/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "NormalForm.compose",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/compose/",
      "source_line_start": 76,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "execNF",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-nf/",
      "source_line_start": 81,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Program.compose",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/compose-l90/",
      "source_line_start": 90,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "compose_assoc",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/compose-assoc/",
      "source_line_start": 93,
      "source_line_end": 95,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.T03"
      ]
    },
    {
      "kind": "theorem",
      "name": "compose_id_left",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/compose-id-left/",
      "source_line_start": 98,
      "source_line_end": 100,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "compose_id_right",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/compose-id-right/",
      "source_line_start": 103,
      "source_line_end": 105,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_compose",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-compose/",
      "source_line_start": 112,
      "source_line_end": 114,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_nil",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-nil/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_rho",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-rho/",
      "source_line_start": 121,
      "source_line_end": 123,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exec_sigma",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/exec-sigma/",
      "source_line_start": 126,
      "source_line_end": 128,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rho_count_compose",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/rho-count-compose/",
      "source_line_start": 136,
      "source_line_end": 149,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.L02"
      ]
    },
    {
      "kind": "theorem",
      "name": "rho_count_nil",
      "url": "/corpus/taulib/docs/book-i-denotation-program-monoid/rho-count-nil/",
      "source_line_start": 152,
      "source_line_end": 154,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [Instruction](/corpus/taulib/docs/book-i-denotation-program-monoid/instruction/) | L37-L43 | type/data schema | type/data schema | `I.D14` |
| `def` | [execInstruction](/corpus/taulib/docs/book-i-denotation-program-monoid/exec-instruction/) | L46-L49 | definition | definition | — |
| `def` | [execProgram](/corpus/taulib/docs/book-i-denotation-program-monoid/exec-program/) | L52-L53 | definition | definition | — |
| `structure` | [NormalForm](/corpus/taulib/docs/book-i-denotation-program-monoid/normal-form/) | L60-L62 | type/data schema | type/data schema | — |
| `def` | [countRho](/corpus/taulib/docs/book-i-denotation-program-monoid/count-rho/) | L65-L68 | definition | definition | — |
| `def` | [NormalForm.id](/corpus/taulib/docs/book-i-denotation-program-monoid/id/) | L71-L73 | definition | definition | — |
| `def` | [NormalForm.compose](/corpus/taulib/docs/book-i-denotation-program-monoid/compose/) | L76-L78 | definition | definition | — |
| `def` | [execNF](/corpus/taulib/docs/book-i-denotation-program-monoid/exec-nf/) | L81-L83 | definition | definition | — |
| `def` | [Program.compose](/corpus/taulib/docs/book-i-denotation-program-monoid/compose-l90/) | L90-L90 | definition | definition | — |
| `theorem` | [compose_assoc](/corpus/taulib/docs/book-i-denotation-program-monoid/compose-assoc/) | L93-L95 | proof obligation | formal proof obligation checked | `I.T03` |
| `theorem` | [compose_id_left](/corpus/taulib/docs/book-i-denotation-program-monoid/compose-id-left/) | L98-L100 | proof obligation | formal proof obligation checked | — |
| `theorem` | [compose_id_right](/corpus/taulib/docs/book-i-denotation-program-monoid/compose-id-right/) | L103-L105 | proof obligation | formal proof obligation checked | — |
| `theorem` | [exec_compose](/corpus/taulib/docs/book-i-denotation-program-monoid/exec-compose/) | L112-L114 | proof obligation | formal proof obligation checked | — |
| `theorem` | [exec_nil](/corpus/taulib/docs/book-i-denotation-program-monoid/exec-nil/) | L117-L118 | proof obligation | formal proof obligation checked | — |
| `theorem` | [exec_rho](/corpus/taulib/docs/book-i-denotation-program-monoid/exec-rho/) | L121-L123 | proof obligation | formal proof obligation checked | — |
| `theorem` | [exec_sigma](/corpus/taulib/docs/book-i-denotation-program-monoid/exec-sigma/) | L126-L128 | proof obligation | formal proof obligation checked | — |
| `theorem` | [rho_count_compose](/corpus/taulib/docs/book-i-denotation-program-monoid/rho-count-compose/) | L136-L149 | proof obligation | formal proof obligation checked | `I.L02` |
| `theorem` | [rho_count_nil](/corpus/taulib/docs/book-i-denotation-program-monoid/rho-count-nil/) | L152-L154 | proof obligation | formal proof obligation checked | — |

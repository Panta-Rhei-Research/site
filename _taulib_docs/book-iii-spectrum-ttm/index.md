---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Spectrum.TTM",
  "permalink": "/corpus/taulib/docs/book-iii-spectrum-ttm/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Spectrum.TTM`.",
  "module_name": "TauLib.BookIII.Spectrum.TTM",
  "module_slug": "book-iii-spectrum-ttm",
  "book": "BookIII",
  "family": "Spectrum",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Spectrum/TTM.lean",
  "sha256": "783c0fddb723baccd32d50681a47ecd480a72490228cf8454f0011720896d2ef",
  "imports": [
    "TauLib.BookI.Denotation.ProgramMonoid",
    "TauLib.BookI.Kernel.Signature"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Spectrum.KernelHinge"
  ],
  "registry_ids": [
    "I.D69",
    "I.D70"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 3,
    "def": 13,
    "theorem": 7,
    "eval": 1
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "TTMOp",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/ttmop/",
      "source_line_start": 50,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D69"
      ]
    },
    {
      "kind": "inductive",
      "name": "TTMGuard",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/ttmguard/",
      "source_line_start": 72,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TTMRule",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/ttmrule/",
      "source_line_start": 86,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TTMConfig",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/ttmconfig/",
      "source_line_start": 102,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D69"
      ]
    },
    {
      "kind": "structure",
      "name": "TTM",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/ttm/",
      "source_line_start": 117,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D69"
      ]
    },
    {
      "kind": "def",
      "name": "TTM.initConfig",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/init-config/",
      "source_line_start": 135,
      "source_line_end": 140,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TTM.isAccepting",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/is-accepting/",
      "source_line_start": 147,
      "source_line_end": 148,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TTM.isHalted",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/is-halted/",
      "source_line_start": 151,
      "source_line_end": 152,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "readReg",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/read-reg/",
      "source_line_start": 159,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "writeReg",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/write-reg/",
      "source_line_start": 163,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "execOp",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/exec-op/",
      "source_line_start": 171,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "execOps",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/exec-ops/",
      "source_line_start": 200,
      "source_line_end": 201,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "evalGuard",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/eval-guard/",
      "source_line_start": 208,
      "source_line_end": 218,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TTM.findRule",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/find-rule/",
      "source_line_start": 225,
      "source_line_end": 226,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TTM.step",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/step/",
      "source_line_start": 230,
      "source_line_end": 235,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TTM.run",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/run/",
      "source_line_start": 238,
      "source_line_end": 243,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauComputable",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/tau-computable/",
      "source_line_start": 252,
      "source_line_end": 256,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D70"
      ]
    },
    {
      "kind": "theorem",
      "name": "generator_symbols_distinct",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/generator-symbols-distinct/",
      "source_line_start": 263,
      "source_line_end": 275,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ttm_tau_native",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/ttm-tau-native/",
      "source_line_start": 279,
      "source_line_end": 282,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ttm_register_bounded",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/ttm-register-bounded/",
      "source_line_start": 286,
      "source_line_end": 287,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "trivial_ttm",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-ttm/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "trivial_accepts",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-accepts/",
      "source_line_start": 297,
      "source_line_end": 299,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "trivial_halted",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-halted/",
      "source_line_start": 302,
      "source_line_end": 304,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "trivial_halted_any",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-halted-any/",
      "source_line_start": 307,
      "source_line_end": 309,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "trivial_run",
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-run/",
      "source_line_start": 312,
      "source_line_end": 325,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectrum-ttm/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 328,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean",
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
- Source path: [`TauLib/BookIII/Spectrum/TTM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Spectrum/TTM.lean`
- SHA-256: `783c0fddb723baccd32d50681a47ecd480a72490228cf8454f0011720896d2ef`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Denotation.ProgramMonoid`
- `TauLib.BookI.Kernel.Signature`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Spectrum.KernelHinge`

## Declaration Counts

- `def`: 13
- `eval`: 1
- `inductive`: 2
- `structure`: 3
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [TTMOp](/corpus/taulib/docs/book-iii-spectrum-ttm/ttmop/) | L50-L65 | type/data schema | type/data schema | `I.D69` |
| `inductive` | [TTMGuard](/corpus/taulib/docs/book-iii-spectrum-ttm/ttmguard/) | L72-L79 | type/data schema | type/data schema | — |
| `structure` | [TTMRule](/corpus/taulib/docs/book-iii-spectrum-ttm/ttmrule/) | L86-L95 | type/data schema | type/data schema | — |
| `structure` | [TTMConfig](/corpus/taulib/docs/book-iii-spectrum-ttm/ttmconfig/) | L102-L109 | type/data schema | type/data schema | `I.D69` |
| `structure` | [TTM](/corpus/taulib/docs/book-iii-spectrum-ttm/ttm/) | L117-L128 | type/data schema | type/data schema | `I.D69` |
| `def` | [TTM.initConfig](/corpus/taulib/docs/book-iii-spectrum-ttm/init-config/) | L135-L140 | definition | definition | — |
| `def` | [TTM.isAccepting](/corpus/taulib/docs/book-iii-spectrum-ttm/is-accepting/) | L147-L148 | data/computed value | data/computed value | — |
| `def` | [TTM.isHalted](/corpus/taulib/docs/book-iii-spectrum-ttm/is-halted/) | L151-L152 | data/computed value | data/computed value | — |
| `def` | [readReg](/corpus/taulib/docs/book-iii-spectrum-ttm/read-reg/) | L159-L160 | data/computed value | data/computed value | — |
| `def` | [writeReg](/corpus/taulib/docs/book-iii-spectrum-ttm/write-reg/) | L163-L164 | data/computed value | data/computed value | — |
| `def` | [execOp](/corpus/taulib/docs/book-iii-spectrum-ttm/exec-op/) | L171-L197 | definition | definition | — |
| `def` | [execOps](/corpus/taulib/docs/book-iii-spectrum-ttm/exec-ops/) | L200-L201 | data/computed value | data/computed value | — |
| `def` | [evalGuard](/corpus/taulib/docs/book-iii-spectrum-ttm/eval-guard/) | L208-L218 | data/computed value | data/computed value | — |
| `def` | [TTM.findRule](/corpus/taulib/docs/book-iii-spectrum-ttm/find-rule/) | L225-L226 | definition | definition | — |
| `def` | [TTM.step](/corpus/taulib/docs/book-iii-spectrum-ttm/step/) | L230-L235 | definition | definition | — |
| `def` | [TTM.run](/corpus/taulib/docs/book-iii-spectrum-ttm/run/) | L238-L243 | data/computed value | data/computed value | — |
| `def` | [TauComputable](/corpus/taulib/docs/book-iii-spectrum-ttm/tau-computable/) | L252-L256 | definition | definition | `I.D70` |
| `theorem` | [generator_symbols_distinct](/corpus/taulib/docs/book-iii-spectrum-ttm/generator-symbols-distinct/) | L263-L275 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ttm_tau_native](/corpus/taulib/docs/book-iii-spectrum-ttm/ttm-tau-native/) | L279-L282 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ttm_register_bounded](/corpus/taulib/docs/book-iii-spectrum-ttm/ttm-register-bounded/) | L286-L287 | proof obligation | formal proof obligation checked | — |
| `def` | [trivial_ttm](/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-ttm/) | L294-L294 | definition | definition | — |
| `theorem` | [trivial_accepts](/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-accepts/) | L297-L299 | proof obligation | formal proof obligation checked | — |
| `theorem` | [trivial_halted](/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-halted/) | L302-L304 | proof obligation | formal proof obligation checked | — |
| `theorem` | [trivial_halted_any](/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-halted-any/) | L307-L309 | proof obligation | formal proof obligation checked | — |
| `theorem` | [trivial_run](/corpus/taulib/docs/book-iii-spectrum-ttm/trivial-run/) | L312-L325 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-iii-spectrum-ttm/eval-l326/) | L326-L328 | computed check | computed check | — |

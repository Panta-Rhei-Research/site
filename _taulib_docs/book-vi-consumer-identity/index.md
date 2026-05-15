---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.Consumer.Identity",
  "permalink": "/corpus/taulib/docs/book-vi-consumer-identity/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.Consumer.Identity`.",
  "module_name": "TauLib.BookVI.Consumer.Identity",
  "module_slug": "book-vi-consumer-identity",
  "book": "BookVI",
  "family": "Consumer",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/Consumer/Identity.lean",
  "sha256": "d7285ddd252ad3ac376fe31152ab38a01bcee5fd3638994fcb29110ada1c745e",
  "imports": [
    "TauLib.BookVI.LifeCore.SelfDesc"
  ],
  "imported_by": [
    "TauLib.BookVI"
  ],
  "registry_ids": [
    "VI.D53",
    "VI.L08",
    "VI.R29",
    "VI.T50"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 3,
    "theorem": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "SelfDescOverCode",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/self-desc-over-code/",
      "source_line_start": 32,
      "source_line_end": 39,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.D53"
      ]
    },
    {
      "kind": "def",
      "name": "selfdesc_code",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/selfdesc-code/",
      "source_line_start": 41,
      "source_line_end": 41,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SubstrateReplacement",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/substrate-replacement/",
      "source_line_start": 52,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.L08"
      ]
    },
    {
      "kind": "def",
      "name": "substrate_repl",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/substrate-repl/",
      "source_line_start": 63,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "identity_is_code_not_carrier",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/identity-is-code-not-carrier/",
      "source_line_start": 65,
      "source_line_end": 68,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "substrate_replacement_preserves_life",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/substrate-replacement-preserves-life/",
      "source_line_start": 70,
      "source_line_end": 75,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SubstrateAbstraction",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/substrate-abstraction/",
      "source_line_start": 91,
      "source_line_end": 102,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.T50"
      ]
    },
    {
      "kind": "def",
      "name": "substrate_abs",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/substrate-abs/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "substrate_abstraction",
      "url": "/corpus/taulib/docs/book-vi-consumer-identity/substrate-abstraction-l106/",
      "source_line_start": 106,
      "source_line_end": 125,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VI.R29"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean",
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
- Source path: [`TauLib/BookVI/Consumer/Identity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/Consumer/Identity.lean`
- SHA-256: `d7285ddd252ad3ac376fe31152ab38a01bcee5fd3638994fcb29110ada1c745e`

## Registry Links

- `VI.D53` — SelfDesc over Code, Not Carrier
- `VI.L08` — Substrate Replacement Preserves Life-Equivalence
- `VI.R29` — Scope: structural, not empirical
- `VI.T50` — Substrate Abstraction

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.LifeCore.SelfDesc`

## Imported By

- `TauLib.BookVI`

## Declaration Counts

- `def`: 3
- `structure`: 3
- `theorem`: 3

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [SelfDescOverCode](/corpus/taulib/docs/book-vi-consumer-identity/self-desc-over-code/) | L32-L39 | type/data schema | type/data schema | `VI.D53` |
| `def` | [selfdesc_code](/corpus/taulib/docs/book-vi-consumer-identity/selfdesc-code/) | L41-L41 | definition | definition | — |
| `structure` | [SubstrateReplacement](/corpus/taulib/docs/book-vi-consumer-identity/substrate-replacement/) | L52-L61 | type/data schema | type/data schema | `VI.L08` |
| `def` | [substrate_repl](/corpus/taulib/docs/book-vi-consumer-identity/substrate-repl/) | L63-L63 | definition | definition | — |
| `theorem` | [identity_is_code_not_carrier](/corpus/taulib/docs/book-vi-consumer-identity/identity-is-code-not-carrier/) | L65-L68 | proof obligation | formal proof obligation checked | — |
| `theorem` | [substrate_replacement_preserves_life](/corpus/taulib/docs/book-vi-consumer-identity/substrate-replacement-preserves-life/) | L70-L75 | proof obligation | formal proof obligation checked | — |
| `structure` | [SubstrateAbstraction](/corpus/taulib/docs/book-vi-consumer-identity/substrate-abstraction/) | L91-L102 | type/data schema | type/data schema | `VI.T50` |
| `def` | [substrate_abs](/corpus/taulib/docs/book-vi-consumer-identity/substrate-abs/) | L104-L104 | definition | definition | — |
| `theorem` | [substrate_abstraction](/corpus/taulib/docs/book-vi-consumer-identity/substrate-abstraction-l106/) | L106-L125 | proof obligation | formal proof obligation checked | `VI.R29` |

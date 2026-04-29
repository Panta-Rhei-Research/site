---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Denotation.Equality",
  "permalink": "/verify/taulib/docs/book-i-denotation-equality/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Denotation.Equality`.",
  "module_name": "TauLib.BookI.Denotation.Equality",
  "module_slug": "book-i-denotation-equality",
  "book": "BookI",
  "family": "Denotation",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Denotation/Equality.lean",
  "sha256": "aa5e4900d45ad5605506950da886911e46c741f72d284ace763e7182699c4a22",
  "imports": [
    "TauLib.BookI.Denotation.ProgramMonoid"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Denotation.Order"
  ],
  "registry_ids": [
    "I.D15"
  ],
  "declaration_counts": {
    "def": 3,
    "theorem": 7
  },
  "declarations": [
    {
      "kind": "def",
      "name": "ontic_eq",
      "url": "/verify/taulib/docs/book-i-denotation-equality/ontic-eq/",
      "source_line_start": 32,
      "source_line_end": 32,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "addr_equiv",
      "url": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv/",
      "source_line_start": 36,
      "source_line_end": 37,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "shadow_eq",
      "url": "/verify/taulib/docs/book-i-denotation-equality/shadow-eq/",
      "source_line_start": 42,
      "source_line_end": 50,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "addr_equiv_refl",
      "url": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv-refl/",
      "source_line_start": 53,
      "source_line_end": 54,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "addr_equiv_symm",
      "url": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv-symm/",
      "source_line_start": 57,
      "source_line_end": 58,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "addr_equiv_trans",
      "url": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv-trans/",
      "source_line_start": 61,
      "source_line_end": 63,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "addr_equiv_nil",
      "url": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv-nil/",
      "source_line_start": 66,
      "source_line_end": 67,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "shadow_implies_ontic",
      "url": "/verify/taulib/docs/book-i-denotation-equality/shadow-implies-ontic/",
      "source_line_start": 70,
      "source_line_end": 71,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "addr_equiv_compose_left",
      "url": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv-compose-left/",
      "source_line_start": 74,
      "source_line_end": 77,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "addr_equiv_compose_right",
      "url": "/verify/taulib/docs/book-i-denotation-equality/addr-equiv-compose-right/",
      "source_line_start": 80,
      "source_line_end": 85,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean",
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
- Source path: [`TauLib/BookI/Denotation/Equality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Equality.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Denotation/Equality.lean`
- SHA-256: `aa5e4900d45ad5605506950da886911e46c741f72d284ace763e7182699c4a22`

## Registry Links

- `I.D15` — Three-Level Equality

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Denotation.ProgramMonoid`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Denotation.Order`

## Declaration Counts

- `def`: 3
- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [ontic_eq](/verify/taulib/docs/book-i-denotation-equality/ontic-eq/) | L32-L32 | defined | — |
| `def` | [addr_equiv](/verify/taulib/docs/book-i-denotation-equality/addr-equiv/) | L36-L37 | defined | — |
| `def` | [shadow_eq](/verify/taulib/docs/book-i-denotation-equality/shadow-eq/) | L42-L50 | defined | — |
| `theorem` | [addr_equiv_refl](/verify/taulib/docs/book-i-denotation-equality/addr-equiv-refl/) | L53-L54 | formalized | — |
| `theorem` | [addr_equiv_symm](/verify/taulib/docs/book-i-denotation-equality/addr-equiv-symm/) | L57-L58 | formalized | — |
| `theorem` | [addr_equiv_trans](/verify/taulib/docs/book-i-denotation-equality/addr-equiv-trans/) | L61-L63 | formalized | — |
| `theorem` | [addr_equiv_nil](/verify/taulib/docs/book-i-denotation-equality/addr-equiv-nil/) | L66-L67 | formalized | — |
| `theorem` | [shadow_implies_ontic](/verify/taulib/docs/book-i-denotation-equality/shadow-implies-ontic/) | L70-L71 | formalized | — |
| `theorem` | [addr_equiv_compose_left](/verify/taulib/docs/book-i-denotation-equality/addr-equiv-compose-left/) | L74-L77 | formalized | — |
| `theorem` | [addr_equiv_compose_right](/verify/taulib/docs/book-i-denotation-equality/addr-equiv-compose-right/) | L80-L85 | formalized | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_slug": "book-i-holomorphy-diagonal-protection",
  "book": "BookI",
  "family": "Holomorphy",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Holomorphy/DiagonalProtection.lean",
  "sha256": "a8a97932db294e847aeb9fecd6ef8ea0e81050400492bafe48a072a96045f9ec",
  "imports": [
    "TauLib.BookI.Holomorphy.TauHolomorphic",
    "TauLib.BookI.Kernel.Diagonal",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
    "TauLib.BookI.Holomorphy.IdentityTheorem",
    "TauLib.BookI.Topos.EarnedArrows"
  ],
  "registry_ids": [
    "I.P23",
    "I.P24",
    "I.T19",
    "I.T20"
  ],
  "declaration_counts": {
    "theorem": 11,
    "structure": 1,
    "def": 5,
    "example": 3,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "no_simul_projection_b",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/no-simul-projection-b/",
      "source_line_start": 57,
      "source_line_end": 60,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P23"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_simul_projection_c",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/no-simul-projection-c/",
      "source_line_start": 62,
      "source_line_end": 65,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diagonal_free_protection",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/diagonal-free-protection/",
      "source_line_start": 78,
      "source_line_end": 80,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T19"
      ]
    },
    {
      "kind": "theorem",
      "name": "diagonal_free_protection_int",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/diagonal-free-protection-int/",
      "source_line_start": 83,
      "source_line_end": 85,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReduceForm",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/reduce-form/",
      "source_line_start": 92,
      "source_line_end": 100,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_reduce_form",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/chi-plus-reduce-form/",
      "source_line_start": 103,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_reduce_form",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/chi-minus-reduce-form/",
      "source_line_start": 109,
      "source_line_end": 112,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_reduce_form",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/id-reduce-form/",
      "source_line_start": 115,
      "source_line_end": 118,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ReduceCompat",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/reduce-compat/",
      "source_line_start": 121,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "id_reduce_compat",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/id-reduce-compat/",
      "source_line_start": 125,
      "source_line_end": 126,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "const_zero_reduce_compat",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/const-zero-reduce-compat/",
      "source_line_start": 129,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "comp_reduce_coherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/comp-reduce-coherent/",
      "source_line_start": 134,
      "source_line_end": 160,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "holfun_comp_rf",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/holfun-comp-rf/",
      "source_line_start": 163,
      "source_line_end": 168,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "stagefun_comp_assoc",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/stagefun-comp-assoc/",
      "source_line_start": 175,
      "source_line_end": 177,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P24"
      ]
    },
    {
      "kind": "theorem",
      "name": "stagefun_id_comp",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/stagefun-id-comp/",
      "source_line_start": 180,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_comp_assoc'",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/sector-comp-assoc/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gt_comp_assoc",
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/gt-comp-assoc/",
      "source_line_start": 191,
      "source_line_end": 204,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/example-l207/",
      "source_line_start": 207,
      "source_line_end": 208,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/example-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/example-l212/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/eval-l219/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/eval-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/eval-l223/",
      "source_line_start": 223,
      "source_line_end": 225,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean",
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
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Holomorphy/DiagonalProtection.lean`
- SHA-256: `a8a97932db294e847aeb9fecd6ef8ea0e81050400492bafe48a072a96045f9ec`

## Registry Links

- `I.P23` — No Simultaneous Projection
- `I.P24` — HolFun Associativity
- `I.T19` — Diagonal-Free Protection
- `I.T20` — Composition Closure

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Holomorphy.TauHolomorphic`
- `TauLib.BookI.Kernel.Diagonal`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Holomorphy.H6DiagonalDiscipline`
- `TauLib.BookI.Holomorphy.IdentityTheorem`
- `TauLib.BookI.Topos.EarnedArrows`

## Declaration Counts

- `def`: 5
- `eval`: 3
- `example`: 3
- `structure`: 1
- `theorem`: 11

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [no_simul_projection_b](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/no-simul-projection-b/) | L57-L60 | formalized | `I.P23` |
| `theorem` | [no_simul_projection_c](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/no-simul-projection-c/) | L62-L65 | formalized | — |
| `theorem` | [diagonal_free_protection](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/diagonal-free-protection/) | L78-L80 | formalized | `I.T19` |
| `theorem` | [diagonal_free_protection_int](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/diagonal-free-protection-int/) | L83-L85 | formalized | — |
| `structure` | [ReduceForm](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/reduce-form/) | L92-L100 | defined | — |
| `def` | [chi_plus_reduce_form](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/chi-plus-reduce-form/) | L103-L106 | defined | — |
| `def` | [chi_minus_reduce_form](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/chi-minus-reduce-form/) | L109-L112 | defined | — |
| `def` | [id_reduce_form](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/id-reduce-form/) | L115-L118 | defined | — |
| `def` | [ReduceCompat](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/reduce-compat/) | L121-L122 | defined | — |
| `theorem` | [id_reduce_compat](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/id-reduce-compat/) | L125-L126 | formalized | — |
| `theorem` | [const_zero_reduce_compat](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/const-zero-reduce-compat/) | L129-L130 | formalized | — |
| `theorem` | [comp_reduce_coherent](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/comp-reduce-coherent/) | L134-L160 | formalized | — |
| `def` | [holfun_comp_rf](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/holfun-comp-rf/) | L163-L168 | defined | — |
| `theorem` | [stagefun_comp_assoc](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/stagefun-comp-assoc/) | L175-L177 | formalized | `I.P24` |
| `theorem` | [stagefun_id_comp](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/stagefun-id-comp/) | L180-L183 | formalized | — |
| `theorem` | [sector_comp_assoc'](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/sector-comp-assoc/) | L186-L188 | formalized | — |
| `theorem` | [gt_comp_assoc](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/gt-comp-assoc/) | L191-L204 | formalized | — |
| `example` | [#eval L207](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/example-l207/) | L207-L208 | example | — |
| `example` | [#eval L211](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/example-l211/) | L211-L211 | example | — |
| `example` | [#eval L212](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/example-l212/) | L212-L212 | example | — |
| `eval` | [#eval L219](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/eval-l219/) | L219-L219 | computed | — |
| `eval` | [#eval L222](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/eval-l222/) | L222-L222 | computed | — |
| `eval` | [#eval L223](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/eval-l223/) | L223-L225 | computed | — |

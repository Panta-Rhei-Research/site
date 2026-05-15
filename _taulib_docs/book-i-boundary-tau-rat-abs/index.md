---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TauRatAbs",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TauRatAbs`.",
  "module_name": "TauLib.BookI.Boundary.TauRatAbs",
  "module_slug": "book-i-boundary-tau-rat-abs",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TauRatAbs.lean",
  "sha256": "1c4c0bb1d82648bb2a8627700353e9974a758b3045d9b2e705ce6c04c1353d94",
  "imports": [
    "TauLib.BookI.Boundary.TauRatOrder",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Push"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.ConstructiveReals",
    "TauLib.BookI.Boundary.TauRatInv"
  ],
  "registry_ids": [
    "I.D107",
    "I.D109",
    "I.D35",
    "I.D84",
    "I.P48"
  ],
  "declaration_counts": {
    "def": 2,
    "theorem": 12,
    "example": 3
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauRat.abs",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs/",
      "source_line_start": 62,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.toRat_nonneg_iff_num_nonneg",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-nonneg-iff-num-nonneg/",
      "source_line_start": 72,
      "source_line_end": 84,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.toRat_neg_iff_num_neg",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-neg-iff-num-neg/",
      "source_line_start": 87,
      "source_line_end": 98,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_abs_of_nonneg",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-abs-of-nonneg/",
      "source_line_start": 105,
      "source_line_end": 108,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_abs_of_neg",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-abs-of-neg/",
      "source_line_start": 111,
      "source_line_end": 114,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.abs_nonneg",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-nonneg/",
      "source_line_start": 121,
      "source_line_end": 126,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.abs_equiv_zero_iff_equiv_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-equiv-zero-iff-equiv-zero/",
      "source_line_start": 133,
      "source_line_end": 144,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.abs_of_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-of-equiv/",
      "source_line_start": 151,
      "source_line_end": 160,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.toRat_abs",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-abs/",
      "source_line_start": 168,
      "source_line_end": 172,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.abs_triangle",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-triangle/",
      "source_line_start": 179,
      "source_line_end": 182,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.abs_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-negate/",
      "source_line_start": 185,
      "source_line_end": 197,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.ofNatRecip",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/of-nat-recip/",
      "source_line_start": 207,
      "source_line_end": 208,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.ofNatRecip_pos",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/of-nat-recip-pos/",
      "source_line_start": 211,
      "source_line_end": 219,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.ofNatRecip_toRat",
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/of-nat-recip-to-rat/",
      "source_line_start": 222,
      "source_line_end": 225,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/example-l232/",
      "source_line_start": 232,
      "source_line_end": 237,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/example-l240/",
      "source_line_start": 240,
      "source_line_end": 245,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/example-l248/",
      "source_line_start": 248,
      "source_line_end": 251,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean",
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
- Source path: [`TauLib/BookI/Boundary/TauRatAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TauRatAbs.lean`
- SHA-256: `1c4c0bb1d82648bb2a8627700353e9974a758b3045d9b2e705ce6c04c1353d94`

## Registry Links

- `I.D35` — Number Tower
- `I.D84` — Constructive Reals

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TauRatOrder`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Push`

## Imported By

- `TauLib.BookI.Boundary.ConstructiveReals`
- `TauLib.BookI.Boundary.TauRatInv`

## Declaration Counts

- `def`: 2
- `example`: 3
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauRat.abs](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs/) | L62-L63 | definition | definition | — |
| `theorem` | [TauRat.toRat_nonneg_iff_num_nonneg](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-nonneg-iff-num-nonneg/) | L72-L84 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.toRat_neg_iff_num_neg](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-neg-iff-num-neg/) | L87-L98 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_abs_of_nonneg](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-abs-of-nonneg/) | L105-L108 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toRat_abs_of_neg](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-abs-of-neg/) | L111-L114 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.abs_nonneg](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-nonneg/) | L121-L126 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.abs_equiv_zero_iff_equiv_zero](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-equiv-zero-iff-equiv-zero/) | L133-L144 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.abs_of_equiv](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-of-equiv/) | L151-L160 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.toRat_abs](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-abs/) | L168-L172 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.abs_triangle](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-triangle/) | L179-L182 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.abs_negate](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-negate/) | L185-L197 | proof obligation | formal proof obligation checked | — |
| `def` | [TauRat.ofNatRecip](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/of-nat-recip/) | L207-L208 | data/computed value | data/computed value | — |
| `theorem` | [TauRat.ofNatRecip_pos](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/of-nat-recip-pos/) | L211-L219 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.ofNatRecip_toRat](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/of-nat-recip-to-rat/) | L222-L225 | proof obligation | formal proof obligation checked | — |
| `example` | [#eval L232](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/example-l232/) | L232-L237 | example check | example | — |
| `example` | [#eval L240](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/example-l240/) | L240-L245 | example check | example | — |
| `example` | [#eval L248](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/example-l248/) | L248-L251 | example check | example | — |

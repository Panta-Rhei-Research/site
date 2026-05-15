---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Holomorphy.DHolomorphic",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Holomorphy.DHolomorphic`.",
  "module_name": "TauLib.BookI.Holomorphy.DHolomorphic",
  "module_slug": "book-i-holomorphy-dholomorphic",
  "book": "BookI",
  "family": "Holomorphy",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Holomorphy/DHolomorphic.lean",
  "sha256": "6120d5da13c1394999ebc1fe49e25854643667dffef079dcbb358cc1bae0095d",
  "imports": [
    "TauLib.BookI.Polarity.BipolarAlgebra",
    "TauLib.BookI.Boundary.SplitComplex",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Holomorphy.TauHolomorphic",
    "TauLib.Tour.GuidedTour.BookI"
  ],
  "registry_ids": [
    "I.D42",
    "I.D43",
    "I.P22"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 10,
    "theorem": 12,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "SectorFun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-fun/",
      "source_line_start": 45,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D42"
      ]
    },
    {
      "kind": "def",
      "name": "SectorFun.apply",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/apply/",
      "source_line_start": 52,
      "source_line_end": 53,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorFun.apply_sc",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/apply-sc/",
      "source_line_start": 56,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "is_sector_independent",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/is-sector-independent/",
      "source_line_start": 66,
      "source_line_end": 69,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.P22"
      ]
    },
    {
      "kind": "theorem",
      "name": "sector_fun_independent",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-fun-independent/",
      "source_line_start": 72,
      "source_line_end": 78,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.P22"
      ]
    },
    {
      "kind": "def",
      "name": "has_split_cr_form",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/has-split-cr-form/",
      "source_line_start": 87,
      "source_line_end": 88,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D43"
      ]
    },
    {
      "kind": "def",
      "name": "SectorFun.comp",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/comp/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_comp_apply",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-comp-apply/",
      "source_line_start": 99,
      "source_line_end": 101,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_comp_assoc",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-comp-assoc/",
      "source_line_start": 104,
      "source_line_end": 105,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorFun.id",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/id/",
      "source_line_start": 108,
      "source_line_end": 108,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_id_comp",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-id-comp/",
      "source_line_start": 111,
      "source_line_end": 113,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_comp_id",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-comp-id/",
      "source_line_start": 116,
      "source_line_end": 118,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zero_div_sectors",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/zero-div-sectors/",
      "source_line_start": 127,
      "source_line_end": 128,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zero_div_sc",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/zero-div-sc/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "b_only_fun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/b-only-fun/",
      "source_line_start": 140,
      "source_line_end": 140,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "c_only_fun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/c-only-fun/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "b_only_comp_c_only",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/b-only-comp-c-only/",
      "source_line_start": 148,
      "source_line_end": 150,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_sf",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-plus-sf/",
      "source_line_start": 157,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_sf",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-minus-sf/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_sf_apply",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-plus-sf-apply/",
      "source_line_start": 163,
      "source_line_end": 165,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_sf_apply",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-minus-sf-apply/",
      "source_line_start": 168,
      "source_line_end": 170,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_sector_complete",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-sector-complete/",
      "source_line_start": 173,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_sector_orthogonal",
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-sector-orthogonal/",
      "source_line_start": 178,
      "source_line_end": 180,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l187/",
      "source_line_start": 187,
      "source_line_end": 187,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l188/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l189/",
      "source_line_start": 189,
      "source_line_end": 189,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l190/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l193/",
      "source_line_start": 193,
      "source_line_end": 195,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean",
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
- Source path: [`TauLib/BookI/Holomorphy/DHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Holomorphy/DHolomorphic.lean`
- SHA-256: `6120d5da13c1394999ebc1fe49e25854643667dffef079dcbb358cc1bae0095d`

## Registry Links

- `I.D42` — D-Differentiability
- `I.D43` — Split-CR Equations
- `I.P22` — Sector Independence

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.BipolarAlgebra`
- `TauLib.BookI.Boundary.SplitComplex`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Holomorphy.TauHolomorphic`
- `TauLib.Tour.GuidedTour.BookI`

## Declaration Counts

- `def`: 10
- `eval`: 5
- `structure`: 1
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [SectorFun](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-fun/) | L45-L49 | type/data schema | type/data schema | `I.D42` |
| `def` | [SectorFun.apply](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/apply/) | L52-L53 | definition | definition | — |
| `def` | [SectorFun.apply_sc](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/apply-sc/) | L56-L57 | definition | definition | — |
| `def` | [is_sector_independent](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/is-sector-independent/) | L66-L69 | definition | definition | `I.P22` |
| `theorem` | [sector_fun_independent](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-fun-independent/) | L72-L78 | proof obligation | formal proof obligation checked | `I.P22` |
| `def` | [has_split_cr_form](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/has-split-cr-form/) | L87-L88 | definition | definition | `I.D43` |
| `def` | [SectorFun.comp](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/comp/) | L95-L96 | definition | definition | — |
| `theorem` | [sector_comp_apply](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-comp-apply/) | L99-L101 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sector_comp_assoc](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-comp-assoc/) | L104-L105 | proof obligation | formal proof obligation checked | — |
| `def` | [SectorFun.id](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/id/) | L108-L108 | definition | definition | — |
| `theorem` | [sector_id_comp](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-id-comp/) | L111-L113 | proof obligation | formal proof obligation checked | — |
| `theorem` | [sector_comp_id](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/sector-comp-id/) | L116-L118 | proof obligation | formal proof obligation checked | — |
| `theorem` | [zero_div_sectors](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/zero-div-sectors/) | L127-L128 | proof obligation | formal proof obligation checked | — |
| `theorem` | [zero_div_sc](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/zero-div-sc/) | L131-L132 | proof obligation | formal proof obligation checked | — |
| `def` | [b_only_fun](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/b-only-fun/) | L140-L140 | data/computed value | data/computed value | — |
| `def` | [c_only_fun](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/c-only-fun/) | L144-L144 | data/computed value | data/computed value | — |
| `theorem` | [b_only_comp_c_only](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/b-only-comp-c-only/) | L148-L150 | proof obligation | formal proof obligation checked | — |
| `def` | [chi_plus_sf](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-plus-sf/) | L157-L157 | definition | definition | — |
| `def` | [chi_minus_sf](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-minus-sf/) | L160-L160 | definition | definition | — |
| `theorem` | [chi_plus_sf_apply](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-plus-sf-apply/) | L163-L165 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_minus_sf_apply](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-minus-sf-apply/) | L168-L170 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_sector_complete](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-sector-complete/) | L173-L175 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_sector_orthogonal](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/chi-sector-orthogonal/) | L178-L180 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L187](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l187/) | L187-L187 | computed check | computed check | — |
| `eval` | [#eval L188](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l188/) | L188-L188 | computed check | computed check | — |
| `eval` | [#eval L189](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l189/) | L189-L189 | computed check | computed check | — |
| `eval` | [#eval L190](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l190/) | L190-L190 | computed check | computed check | — |
| `eval` | [#eval L193](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/eval-l193/) | L193-L195 | computed check | computed check | — |

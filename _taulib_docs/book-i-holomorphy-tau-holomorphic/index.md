---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_slug": "book-i-holomorphy-tau-holomorphic",
  "book": "BookI",
  "family": "Holomorphy",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Holomorphy/TauHolomorphic.lean",
  "sha256": "b215ab2375e79385d6f9cc4cfa0a3a9e4010cd747f4e3a22bc0fb201df473b63",
  "imports": [
    "TauLib.BookI.Holomorphy.DHolomorphic",
    "TauLib.BookI.Polarity.OmegaGerms",
    "TauLib.BookI.Polarity.ModArith",
    "TauLib.BookI.Polarity.ChineseRemainder",
    "TauLib.BookI.Boundary.Characters",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Holomorphy.DiagonalProtection",
    "TauLib.BookI.Holomorphy.IdentityTheorem",
    "TauLib.BookII.Domains.HolImpliesCont",
    "TauLib.BookIII.Spectrum.InterfaceWidth"
  ],
  "registry_ids": [
    "I.D45",
    "I.D46",
    "I.D47",
    "I.D48",
    "I.T18"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 14,
    "theorem": 7,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "StageFun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/stage-fun/",
      "source_line_start": 53,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TowerCoherent",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D46"
      ]
    },
    {
      "kind": "def",
      "name": "tower_coherent_check",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent-check/",
      "source_line_start": 76,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GermTransformer",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/germ-transformer/",
      "source_line_start": 92,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D45"
      ]
    },
    {
      "kind": "def",
      "name": "GermTransformer.eval",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval/",
      "source_line_start": 103,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolFun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-fun/",
      "source_line_start": 117,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D47"
      ]
    },
    {
      "kind": "structure",
      "name": "HolMap",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-map/",
      "source_line_start": 124,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D48"
      ]
    },
    {
      "kind": "def",
      "name": "chi_plus_stage",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-stage/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_stage",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-stage/",
      "source_line_start": 141,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_stage",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-stage/",
      "source_line_start": 145,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_gt",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-gt/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_gt",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-gt/",
      "source_line_start": 153,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_gt",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-gt/",
      "source_line_start": 157,
      "source_line_end": 158,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reduce_zero",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-zero/",
      "source_line_start": 165,
      "source_line_end": 166,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reduce_compat",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-compat/",
      "source_line_start": 169,
      "source_line_end": 171,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_coherent",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-coherent/",
      "source_line_start": 174,
      "source_line_end": 181,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_coherent",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-coherent/",
      "source_line_start": 184,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "id_coherent",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-coherent/",
      "source_line_start": 194,
      "source_line_end": 197,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_holfun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-holfun/",
      "source_line_start": 200,
      "source_line_end": 201,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_holfun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-holfun/",
      "source_line_start": 204,
      "source_line_end": 205,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_holfun",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-holfun/",
      "source_line_start": 208,
      "source_line_end": 209,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_crt",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-crt/",
      "source_line_start": 222,
      "source_line_end": 225,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_crt",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-crt/",
      "source_line_start": 228,
      "source_line_end": 231,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "StageFun.comp",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/comp/",
      "source_line_start": 241,
      "source_line_end": 243,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GermTransformer.comp",
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/comp-l246/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l256/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 268,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean",
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
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Holomorphy/TauHolomorphic.lean`
- SHA-256: `b215ab2375e79385d6f9cc4cfa0a3a9e4010cd747f4e3a22bc0fb201df473b63`

## Registry Links

- `I.D45` — Omega-Germ Transformer
- `I.D46` — Tower Coherence
- `I.D47` — Tau-Holomorphic Function
- `I.D48` — Tau-Holomorphic Map
- `I.T18` — CRT Coherence Constraint

## Construction Spine Links

- [Build the τ-Kernel](/corpus/construction-spine/build-the-kernel/)

## Imports

- `TauLib.BookI.Holomorphy.DHolomorphic`
- `TauLib.BookI.Polarity.OmegaGerms`
- `TauLib.BookI.Polarity.ModArith`
- `TauLib.BookI.Polarity.ChineseRemainder`
- `TauLib.BookI.Boundary.Characters`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Holomorphy.DiagonalProtection`
- `TauLib.BookI.Holomorphy.IdentityTheorem`
- `TauLib.BookII.Domains.HolImpliesCont`
- `TauLib.BookIII.Spectrum.InterfaceWidth`

## Declaration Counts

- `def`: 14
- `eval`: 7
- `structure`: 4
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [StageFun](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/stage-fun/) | L53-L57 | type/data schema | type/data schema | — |
| `def` | [TowerCoherent](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent/) | L71-L73 | definition | definition | `I.D46` |
| `def` | [tower_coherent_check](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent-check/) | L76-L80 | data/computed value | data/computed value | — |
| `structure` | [GermTransformer](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/germ-transformer/) | L92-L100 | type/data schema | type/data schema | `I.D45` |
| `def` | [GermTransformer.eval](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval/) | L103-L104 | definition | definition | — |
| `structure` | [HolFun](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-fun/) | L117-L121 | type/data schema | type/data schema | `I.D47` |
| `structure` | [HolMap](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-map/) | L124-L130 | type/data schema | type/data schema | `I.D48` |
| `def` | [chi_plus_stage](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-stage/) | L137-L138 | definition | definition | — |
| `def` | [chi_minus_stage](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-stage/) | L141-L142 | definition | definition | — |
| `def` | [id_stage](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-stage/) | L145-L146 | definition | definition | — |
| `def` | [chi_plus_gt](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-gt/) | L149-L150 | definition | definition | — |
| `def` | [chi_minus_gt](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-gt/) | L153-L154 | definition | definition | — |
| `def` | [id_gt](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-gt/) | L157-L158 | definition | definition | — |
| `theorem` | [reduce_zero](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-zero/) | L165-L166 | proof obligation | formal proof obligation checked | — |
| `theorem` | [reduce_compat](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-compat/) | L169-L171 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_plus_coherent](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-coherent/) | L174-L181 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_minus_coherent](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-coherent/) | L184-L191 | proof obligation | formal proof obligation checked | — |
| `theorem` | [id_coherent](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-coherent/) | L194-L197 | proof obligation | formal proof obligation checked | — |
| `def` | [chi_plus_holfun](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-holfun/) | L200-L201 | definition | definition | — |
| `def` | [chi_minus_holfun](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-holfun/) | L204-L205 | definition | definition | — |
| `def` | [id_holfun](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/id-holfun/) | L208-L209 | definition | definition | — |
| `theorem` | [chi_plus_crt](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-crt/) | L222-L225 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chi_minus_crt](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-crt/) | L228-L231 | proof obligation | formal proof obligation checked | — |
| `def` | [StageFun.comp](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/comp/) | L241-L243 | definition | definition | — |
| `def` | [GermTransformer.comp](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/comp-l246/) | L246-L249 | definition | definition | — |
| `eval` | [#eval L256](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l256/) | L256-L256 | computed check | computed check | — |
| `eval` | [#eval L257](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l257/) | L257-L257 | computed check | computed check | — |
| `eval` | [#eval L260](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l260/) | L260-L260 | computed check | computed check | — |
| `eval` | [#eval L261](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l261/) | L261-L261 | computed check | computed check | — |
| `eval` | [#eval L262](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l262/) | L262-L262 | computed check | computed check | — |
| `eval` | [#eval L265](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l265/) | L265-L265 | computed check | computed check | — |
| `eval` | [#eval L266](/corpus/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l266/) | L266-L268 | computed check | computed check | — |

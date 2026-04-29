---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/",
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
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/stage-fun/",
      "source_line_start": 53,
      "source_line_end": 57,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TowerCoherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": [
        "I.D46"
      ]
    },
    {
      "kind": "def",
      "name": "tower_coherent_check",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent-check/",
      "source_line_start": 76,
      "source_line_end": 80,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GermTransformer",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/germ-transformer/",
      "source_line_start": 92,
      "source_line_end": 100,
      "formal_status": "defined",
      "registry_ids": [
        "I.D45"
      ]
    },
    {
      "kind": "def",
      "name": "GermTransformer.eval",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval/",
      "source_line_start": 103,
      "source_line_end": 104,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolFun",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-fun/",
      "source_line_start": 117,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": [
        "I.D47"
      ]
    },
    {
      "kind": "structure",
      "name": "HolMap",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-map/",
      "source_line_start": 124,
      "source_line_end": 130,
      "formal_status": "defined",
      "registry_ids": [
        "I.D48"
      ]
    },
    {
      "kind": "def",
      "name": "chi_plus_stage",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-stage/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_stage",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-stage/",
      "source_line_start": 141,
      "source_line_end": 142,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_stage",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-stage/",
      "source_line_start": 145,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_gt",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-gt/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_gt",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-gt/",
      "source_line_start": 153,
      "source_line_end": 154,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_gt",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-gt/",
      "source_line_start": 157,
      "source_line_end": 158,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reduce_zero",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-zero/",
      "source_line_start": 165,
      "source_line_end": 166,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reduce_compat",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-compat/",
      "source_line_start": 169,
      "source_line_end": 171,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_coherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-coherent/",
      "source_line_start": 174,
      "source_line_end": 181,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_coherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-coherent/",
      "source_line_start": 184,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "id_coherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-coherent/",
      "source_line_start": 194,
      "source_line_end": 197,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_holfun",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-holfun/",
      "source_line_start": 200,
      "source_line_end": 201,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_holfun",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-holfun/",
      "source_line_start": 204,
      "source_line_end": 205,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_holfun",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-holfun/",
      "source_line_start": 208,
      "source_line_end": 209,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_crt",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-crt/",
      "source_line_start": 222,
      "source_line_end": 225,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_minus_crt",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-crt/",
      "source_line_start": 228,
      "source_line_end": 231,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "StageFun.comp",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/comp/",
      "source_line_start": 241,
      "source_line_end": 243,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "GermTransformer.comp",
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/comp-l246/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l256/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 268,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [StageFun](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/stage-fun/) | L53-L57 | defined | — |
| `def` | [TowerCoherent](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent/) | L71-L73 | defined | `I.D46` |
| `def` | [tower_coherent_check](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent-check/) | L76-L80 | defined | — |
| `structure` | [GermTransformer](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/germ-transformer/) | L92-L100 | defined | `I.D45` |
| `def` | [GermTransformer.eval](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval/) | L103-L104 | defined | — |
| `structure` | [HolFun](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-fun/) | L117-L121 | defined | `I.D47` |
| `structure` | [HolMap](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/hol-map/) | L124-L130 | defined | `I.D48` |
| `def` | [chi_plus_stage](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-stage/) | L137-L138 | defined | — |
| `def` | [chi_minus_stage](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-stage/) | L141-L142 | defined | — |
| `def` | [id_stage](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-stage/) | L145-L146 | defined | — |
| `def` | [chi_plus_gt](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-gt/) | L149-L150 | defined | — |
| `def` | [chi_minus_gt](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-gt/) | L153-L154 | defined | — |
| `def` | [id_gt](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-gt/) | L157-L158 | defined | — |
| `theorem` | [reduce_zero](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-zero/) | L165-L166 | formalized | — |
| `theorem` | [reduce_compat](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-compat/) | L169-L171 | formalized | — |
| `theorem` | [chi_plus_coherent](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-coherent/) | L174-L181 | formalized | — |
| `theorem` | [chi_minus_coherent](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-coherent/) | L184-L191 | formalized | — |
| `theorem` | [id_coherent](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-coherent/) | L194-L197 | formalized | — |
| `def` | [chi_plus_holfun](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-holfun/) | L200-L201 | defined | — |
| `def` | [chi_minus_holfun](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-holfun/) | L204-L205 | defined | — |
| `def` | [id_holfun](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/id-holfun/) | L208-L209 | defined | — |
| `theorem` | [chi_plus_crt](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-plus-crt/) | L222-L225 | formalized | — |
| `theorem` | [chi_minus_crt](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-crt/) | L228-L231 | formalized | — |
| `def` | [StageFun.comp](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/comp/) | L241-L243 | defined | — |
| `def` | [GermTransformer.comp](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/comp-l246/) | L246-L249 | defined | — |
| `eval` | [#eval L256](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l256/) | L256-L256 | computed | — |
| `eval` | [#eval L257](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l257/) | L257-L257 | computed | — |
| `eval` | [#eval L260](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l260/) | L260-L260 | computed | — |
| `eval` | [#eval L261](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l261/) | L261-L261 | computed | — |
| `eval` | [#eval L262](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l262/) | L262-L262 | computed | — |
| `eval` | [#eval L265](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l265/) | L265-L265 | computed | — |
| `eval` | [#eval L266](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/eval-l266/) | L266-L268 | computed | — |

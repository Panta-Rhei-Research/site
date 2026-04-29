---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_slug": "book-i-holomorphy-identity-theorem",
  "book": "BookI",
  "family": "Holomorphy",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Holomorphy/IdentityTheorem.lean",
  "sha256": "3effd54a2c87433ad5c4a60e82d972e33a5e340e5ee5bb77277ffde96b1dae72",
  "imports": [
    "TauLib.BookI.Holomorphy.TauHolomorphic",
    "TauLib.BookI.Holomorphy.DiagonalProtection",
    "TauLib.BookI.Polarity.OmegaGerms",
    "TauLib.BookI.Polarity.ModArith",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Holomorphy.SpectralCoefficients",
    "TauLib.BookI.Topos.EarnedArrows"
  ],
  "registry_ids": [
    "I.D49",
    "I.L07",
    "I.T21"
  ],
  "declaration_counts": {
    "def": 4,
    "theorem": 9,
    "structure": 1,
    "example": 1,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "def",
      "name": "agree_at",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-at/",
      "source_line_start": 48,
      "source_line_end": 49,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "agree_at_check",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-at-check/",
      "source_line_start": 52,
      "source_line_end": 53,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "agree_up_to",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-up-to/",
      "source_line_start": 57,
      "source_line_end": 58,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "agree_all",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-all/",
      "source_line_start": 61,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tail_agree_downward",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tail-agree-downward/",
      "source_line_start": 77,
      "source_line_end": 95,
      "formal_status": "formalized",
      "registry_ids": [
        "I.L07"
      ]
    },
    {
      "kind": "theorem",
      "name": "tail_agree_propagation",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tail-agree-propagation/",
      "source_line_start": 100,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_identity_reduce",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-reduce/",
      "source_line_start": 118,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T21"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_identity_nat",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-nat/",
      "source_line_start": 134,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_identity_finite_witness",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-finite-witness/",
      "source_line_start": 147,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HolL",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/hol-l/",
      "source_line_start": 192,
      "source_line_end": 194,
      "formal_status": "defined",
      "registry_ids": [
        "I.D49"
      ]
    },
    {
      "kind": "theorem",
      "name": "hol_L_identity",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/hol-l-identity/",
      "source_line_start": 200,
      "source_line_end": 206,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/example-l214/",
      "source_line_start": 214,
      "source_line_end": 214,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_self_agree",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/chi-plus-self-agree/",
      "source_line_start": 217,
      "source_line_end": 219,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "id_eq_chi_sum",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/id-eq-chi-sum/",
      "source_line_start": 224,
      "source_line_end": 226,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "id_eq_chi_sum_c",
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/id-eq-chi-sum-c/",
      "source_line_start": 228,
      "source_line_end": 230,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l237/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l242/",
      "source_line_start": 242,
      "source_line_end": 244,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean",
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
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Holomorphy/IdentityTheorem.lean`
- SHA-256: `3effd54a2c87433ad5c4a60e82d972e33a5e340e5ee5bb77277ffde96b1dae72`

## Registry Links

- `I.D49` — Hol(L)
- `I.L07` — Tail Agreement Propagation
- `I.T21` — Tau-Identity Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Holomorphy.TauHolomorphic`
- `TauLib.BookI.Holomorphy.DiagonalProtection`
- `TauLib.BookI.Polarity.OmegaGerms`
- `TauLib.BookI.Polarity.ModArith`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Holomorphy.SpectralCoefficients`
- `TauLib.BookI.Topos.EarnedArrows`

## Declaration Counts

- `def`: 4
- `eval`: 4
- `example`: 1
- `structure`: 1
- `theorem`: 9

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [agree_at](/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-at/) | L48-L49 | defined | — |
| `def` | [agree_at_check](/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-at-check/) | L52-L53 | defined | — |
| `def` | [agree_up_to](/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-up-to/) | L57-L58 | defined | — |
| `def` | [agree_all](/verify/taulib/docs/book-i-holomorphy-identity-theorem/agree-all/) | L61-L62 | defined | — |
| `theorem` | [tail_agree_downward](/verify/taulib/docs/book-i-holomorphy-identity-theorem/tail-agree-downward/) | L77-L95 | formalized | `I.L07` |
| `theorem` | [tail_agree_propagation](/verify/taulib/docs/book-i-holomorphy-identity-theorem/tail-agree-propagation/) | L100-L105 | formalized | — |
| `theorem` | [tau_identity_reduce](/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-reduce/) | L118-L125 | formalized | `I.T21` |
| `theorem` | [tau_identity_nat](/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-nat/) | L134-L138 | formalized | — |
| `theorem` | [tau_identity_finite_witness](/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-finite-witness/) | L147-L183 | formalized | — |
| `structure` | [HolL](/verify/taulib/docs/book-i-holomorphy-identity-theorem/hol-l/) | L192-L194 | defined | `I.D49` |
| `theorem` | [hol_L_identity](/verify/taulib/docs/book-i-holomorphy-identity-theorem/hol-l-identity/) | L200-L206 | formalized | — |
| `example` | [#eval L214](/verify/taulib/docs/book-i-holomorphy-identity-theorem/example-l214/) | L214-L214 | example | — |
| `theorem` | [chi_plus_self_agree](/verify/taulib/docs/book-i-holomorphy-identity-theorem/chi-plus-self-agree/) | L217-L219 | formalized | — |
| `theorem` | [id_eq_chi_sum](/verify/taulib/docs/book-i-holomorphy-identity-theorem/id-eq-chi-sum/) | L224-L226 | formalized | — |
| `theorem` | [id_eq_chi_sum_c](/verify/taulib/docs/book-i-holomorphy-identity-theorem/id-eq-chi-sum-c/) | L228-L230 | formalized | — |
| `eval` | [#eval L237](/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l237/) | L237-L237 | computed | — |
| `eval` | [#eval L238](/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l238/) | L238-L238 | computed | — |
| `eval` | [#eval L239](/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l239/) | L239-L239 | computed | — |
| `eval` | [#eval L242](/verify/taulib/docs/book-i-holomorphy-identity-theorem/eval-l242/) | L242-L244 | computed | — |

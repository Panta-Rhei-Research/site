---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Topos.CircularityResolution",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Topos.CircularityResolution`.",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_slug": "book-i-topos-circularity-resolution",
  "book": "BookI",
  "family": "Topos",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Topos/CircularityResolution.lean",
  "sha256": "374ecaed4f690f95f45b144a59f4888eecf02e3f4255641f5028ab477f77eeca",
  "imports": [
    "TauLib.BookI.Topos.EarnedTopos",
    "TauLib.BookI.Polarity.InverseLimit"
  ],
  "imported_by": [
    "TauLib.BookI.Topos.H7CircularityFull",
    "TauLib.BookI.Topos.ParaconsistentSoundness"
  ],
  "registry_ids": [
    "I.D122",
    "I.D21",
    "I.D58",
    "I.D59"
  ],
  "declaration_counts": {
    "def": 8,
    "theorem": 16,
    "inductive": 1
  },
  "declarations": [
    {
      "kind": "def",
      "name": "sigmaSwap",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap/",
      "source_line_start": 107,
      "source_line_end": 116,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigmaSwap_involutive",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap-involutive/",
      "source_line_start": 119,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigmaSwap_fixes_B",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap-fixes-b/",
      "source_line_start": 124,
      "source_line_end": 124,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sigmaSwap_fixes_N",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap-fixes-n/",
      "source_line_start": 127,
      "source_line_end": 127,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cauchyIter",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/cauchy-iter/",
      "source_line_start": 136,
      "source_line_end": 145,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "EventuallyConst",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/eventually-const/",
      "source_line_start": 153,
      "source_line_end": 155,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Period2OnLobes",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/period2-on-lobes/",
      "source_line_start": 161,
      "source_line_end": 164,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "StabilisedValue",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/stabilised-value/",
      "source_line_start": 186,
      "source_line_end": 195,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "liarTemplate",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-template/",
      "source_line_start": 205,
      "source_line_end": 205,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "liar_iter_alternates",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-iter-alternates/",
      "source_line_start": 208,
      "source_line_end": 225,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "liar_period2",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-period2/",
      "source_line_start": 228,
      "source_line_end": 244,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "liar_stabilises_at_Both",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-stabilises-at-both/",
      "source_line_start": 251,
      "source_line_end": 253,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "truthTellerTemplate",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-template/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth_teller_constant_at_seed",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-constant-at-seed/",
      "source_line_start": 264,
      "source_line_end": 270,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth_teller_stabilises_T",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-stabilises-t/",
      "source_line_start": 273,
      "source_line_end": 276,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth_teller_stabilises_F",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-stabilises-f/",
      "source_line_start": 280,
      "source_line_end": 283,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth_teller_ambiguity",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-ambiguity/",
      "source_line_start": 288,
      "source_line_end": 291,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "curryTemplate",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/curry-template/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "curry_eq_liar",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/curry-eq-liar/",
      "source_line_start": 310,
      "source_line_end": 311,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "curry_stabilises_at_Both",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/curry-stabilises-at-both/",
      "source_line_start": 316,
      "source_line_end": 318,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_sector_witness_liar",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/four-sector-witness-liar/",
      "source_line_start": 347,
      "source_line_end": 349,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_sector_witness_truthteller",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/four-sector-witness-truthteller/",
      "source_line_start": 351,
      "source_line_end": 353,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "both_equals_lobe_sum",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/both-equals-lobe-sum/",
      "source_line_start": 370,
      "source_line_end": 379,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "both_equals_one_witness",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/both-equals-one-witness/",
      "source_line_start": 400,
      "source_line_end": 404,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cauchyTrace",
      "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/cauchy-trace/",
      "source_line_start": 422,
      "source_line_end": 435,
      "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean",
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
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Topos/CircularityResolution.lean`
- SHA-256: `374ecaed4f690f95f45b144a59f4888eecf02e3f4255641f5028ab477f77eeca`

## Registry Links

- `I.D21` — Truth4 Logic
- `I.D58` — Characteristic Morphism
- `I.D59` — Earned Topos

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Topos.EarnedTopos`
- `TauLib.BookI.Polarity.InverseLimit`

## Imported By

- `TauLib.BookI.Topos.H7CircularityFull`
- `TauLib.BookI.Topos.ParaconsistentSoundness`

## Declaration Counts

- `def`: 8
- `inductive`: 1
- `theorem`: 16

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [sigmaSwap](/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap/) | L107-L116 | defined | — |
| `theorem` | [sigmaSwap_involutive](/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap-involutive/) | L119-L121 | formalized | — |
| `theorem` | [sigmaSwap_fixes_B](/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap-fixes-b/) | L124-L124 | formalized | — |
| `theorem` | [sigmaSwap_fixes_N](/verify/taulib/docs/book-i-topos-circularity-resolution/sigma-swap-fixes-n/) | L127-L127 | formalized | — |
| `def` | [cauchyIter](/verify/taulib/docs/book-i-topos-circularity-resolution/cauchy-iter/) | L136-L145 | defined | — |
| `def` | [EventuallyConst](/verify/taulib/docs/book-i-topos-circularity-resolution/eventually-const/) | L153-L155 | defined | — |
| `def` | [Period2OnLobes](/verify/taulib/docs/book-i-topos-circularity-resolution/period2-on-lobes/) | L161-L164 | defined | — |
| `inductive` | [StabilisedValue](/verify/taulib/docs/book-i-topos-circularity-resolution/stabilised-value/) | L186-L195 | defined | — |
| `def` | [liarTemplate](/verify/taulib/docs/book-i-topos-circularity-resolution/liar-template/) | L205-L205 | defined | — |
| `theorem` | [liar_iter_alternates](/verify/taulib/docs/book-i-topos-circularity-resolution/liar-iter-alternates/) | L208-L225 | formalized | — |
| `theorem` | [liar_period2](/verify/taulib/docs/book-i-topos-circularity-resolution/liar-period2/) | L228-L244 | formalized | — |
| `theorem` | [liar_stabilises_at_Both](/verify/taulib/docs/book-i-topos-circularity-resolution/liar-stabilises-at-both/) | L251-L253 | formalized | — |
| `def` | [truthTellerTemplate](/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-template/) | L261-L261 | defined | — |
| `theorem` | [truth_teller_constant_at_seed](/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-constant-at-seed/) | L264-L270 | formalized | — |
| `theorem` | [truth_teller_stabilises_T](/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-stabilises-t/) | L273-L276 | formalized | — |
| `theorem` | [truth_teller_stabilises_F](/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-stabilises-f/) | L280-L283 | formalized | — |
| `theorem` | [truth_teller_ambiguity](/verify/taulib/docs/book-i-topos-circularity-resolution/truth-teller-ambiguity/) | L288-L291 | formalized | — |
| `def` | [curryTemplate](/verify/taulib/docs/book-i-topos-circularity-resolution/curry-template/) | L307-L307 | defined | — |
| `theorem` | [curry_eq_liar](/verify/taulib/docs/book-i-topos-circularity-resolution/curry-eq-liar/) | L310-L311 | formalized | — |
| `theorem` | [curry_stabilises_at_Both](/verify/taulib/docs/book-i-topos-circularity-resolution/curry-stabilises-at-both/) | L316-L318 | formalized | — |
| `theorem` | [four_sector_witness_liar](/verify/taulib/docs/book-i-topos-circularity-resolution/four-sector-witness-liar/) | L347-L349 | formalized | — |
| `theorem` | [four_sector_witness_truthteller](/verify/taulib/docs/book-i-topos-circularity-resolution/four-sector-witness-truthteller/) | L351-L353 | formalized | — |
| `theorem` | [both_equals_lobe_sum](/verify/taulib/docs/book-i-topos-circularity-resolution/both-equals-lobe-sum/) | L370-L379 | formalized | — |
| `theorem` | [both_equals_one_witness](/verify/taulib/docs/book-i-topos-circularity-resolution/both-equals-one-witness/) | L400-L404 | formalized | — |
| `def` | [cauchyTrace](/verify/taulib/docs/book-i-topos-circularity-resolution/cauchy-trace/) | L422-L435 | defined | — |

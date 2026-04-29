---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.MassRatioFormula",
  "permalink": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.MassRatioFormula`.",
  "module_name": "TauLib.BookIV.Calibration.MassRatioFormula",
  "module_slug": "book-iv-calibration-mass-ratio-formula",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/MassRatioFormula.lean",
  "sha256": "c7a60b89f63256fb2370bc7b843be91c1b5a1cb120105c115188f02732ab2be8",
  "imports": [
    "TauLib.BookIV.Calibration.SIReference",
    "TauLib.BookIV.Sectors.FineStructure"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.ConstantsLedgerExt",
    "TauLib.BookIV.MassDerivation.ElectronMass",
    "TauLib.BookIV.MassDerivation.HolonomyDetail",
    "TauLib.BookIV.Physics.InternalEquations",
    "TauLib.BookV.Prologue.ExportContract"
  ],
  "registry_ids": [
    "IV.D46",
    "IV.D47",
    "IV.D48",
    "IV.P07",
    "IV.T13",
    "IV.T14",
    "IV.T15"
  ],
  "declaration_counts": {
    "def": 13,
    "theorem": 20,
    "structure": 4,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "def",
      "name": "bulk_numer",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-numer/",
      "source_line_start": 89,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D46"
      ]
    },
    {
      "kind": "def",
      "name": "bulk_denom",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom/",
      "source_line_start": 92,
      "source_line_end": 92,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_denom_pos",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom-pos/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bulk_float",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-float/",
      "source_line_start": 99,
      "source_line_end": 100,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_gt_1853",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-gt-1853/",
      "source_line_start": 107,
      "source_line_end": 108,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_lt_1855",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-lt-1855/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_in_range",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-in-range/",
      "source_line_start": 115,
      "source_line_end": 118,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_neg2_numer",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-numer/",
      "source_line_start": 125,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_neg2_denom",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-denom/",
      "source_line_start": 128,
      "source_line_end": 128,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_neg2_gt_8",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-gt-8/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_neg2_lt_9",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-lt-9/",
      "source_line_start": 135,
      "source_line_end": 136,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3N",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-n/",
      "source_line_start": 143,
      "source_line_end": 143,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3D",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-d/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "correction0_numer",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-numer/",
      "source_line_start": 151,
      "source_line_end": 151,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "correction0_denom",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom/",
      "source_line_start": 154,
      "source_line_end": 154,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction0_denom_pos",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom-pos/",
      "source_line_start": 157,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction0_gt_14",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-gt-14/",
      "source_line_start": 161,
      "source_line_end": 162,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction0_lt_16",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-lt-16/",
      "source_line_start": 165,
      "source_line_end": 166,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_overshoots_codata",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-overshoots-codata/",
      "source_line_start": 176,
      "source_line_end": 178,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T13"
      ]
    },
    {
      "kind": "theorem",
      "name": "r0_gt_1837",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-gt-1837/",
      "source_line_start": 189,
      "source_line_end": 192,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T14"
      ]
    },
    {
      "kind": "theorem",
      "name": "r0_lt_1840",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-lt-1840/",
      "source_line_start": 196,
      "source_line_end": 199,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "r0_in_range",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-in-range/",
      "source_line_start": 202,
      "source_line_end": 207,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "r0_deviation_lt_1pct",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-deviation-lt-1pct/",
      "source_line_start": 227,
      "source_line_end": 254,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Level1PlusFormula",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/level1-plus-formula/",
      "source_line_start": 270,
      "source_line_end": 281,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D48"
      ]
    },
    {
      "kind": "def",
      "name": "level1plus",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/level1plus/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "perturbative_terms",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-terms/",
      "source_line_start": 295,
      "source_line_end": 299,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "perturbative_count",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-count/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ElectronMassDerivation",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-derivation/",
      "source_line_start": 315,
      "source_line_end": 324,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "electron_mass_consistent",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-consistent/",
      "source_line_start": 329,
      "source_line_end": 332,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RDerivationLink",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/rderivation-link/",
      "source_line_start": 339,
      "source_line_end": 346,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "r_derivation_chain",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r-derivation-chain/",
      "source_line_start": 349,
      "source_line_end": 360,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_length",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-length/",
      "source_line_start": 363,
      "source_line_end": 363,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T15"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_all_tau_effective",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-all-tau-effective/",
      "source_line_start": 366,
      "source_line_end": 368,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P07"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_scope_count",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-scope-count/",
      "source_line_start": 371,
      "source_line_end": 374,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FormulaLevel",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level/",
      "source_line_start": 381,
      "source_line_end": 390,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "formula_levels",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-levels/",
      "source_line_start": 393,
      "source_line_end": 403,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "formula_level_count",
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level-count/",
      "source_line_start": 406,
      "source_line_end": 406,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l416/",
      "source_line_start": 416,
      "source_line_end": 416,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l419/",
      "source_line_start": 419,
      "source_line_end": 419,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l423/",
      "source_line_start": 423,
      "source_line_end": 423,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l424/",
      "source_line_start": 424,
      "source_line_end": 424,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l427/",
      "source_line_start": 427,
      "source_line_end": 429,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean",
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
- Source path: [`TauLib/BookIV/Calibration/MassRatioFormula.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/MassRatioFormula.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/MassRatioFormula.lean`
- SHA-256: `c7a60b89f63256fb2370bc7b843be91c1b5a1cb120105c115188f02732ab2be8`

## Registry Links

- `IV.D46` — Mass Ratio Bulk Term
- `IV.D47` — Level 0 Formula
- `IV.D48` — Level 1+ Formula
- `IV.P07` — All Links Tau-Effective
- `IV.T13` — Bulk Overshoots
- `IV.T14` — Level 0 Range
- `IV.T15` — Derivation Chain Complete

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Calibration.SIReference`
- `TauLib.BookIV.Sectors.FineStructure`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.ConstantsLedgerExt`
- `TauLib.BookIV.MassDerivation.ElectronMass`
- `TauLib.BookIV.MassDerivation.HolonomyDetail`
- `TauLib.BookIV.Physics.InternalEquations`
- `TauLib.BookV.Prologue.ExportContract`

## Declaration Counts

- `def`: 13
- `eval`: 6
- `structure`: 4
- `theorem`: 20

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [bulk_numer](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-numer/) | L89-L89 | defined | `IV.D46` |
| `def` | [bulk_denom](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom/) | L92-L92 | defined | — |
| `theorem` | [bulk_denom_pos](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom-pos/) | L95-L96 | formalized | — |
| `def` | [bulk_float](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-float/) | L99-L100 | defined | — |
| `theorem` | [bulk_gt_1853](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-gt-1853/) | L107-L108 | formalized | — |
| `theorem` | [bulk_lt_1855](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-lt-1855/) | L111-L112 | formalized | — |
| `theorem` | [bulk_in_range](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-in-range/) | L115-L118 | formalized | — |
| `def` | [iota_neg2_numer](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-numer/) | L125-L125 | defined | — |
| `def` | [iota_neg2_denom](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-denom/) | L128-L128 | defined | — |
| `theorem` | [iota_neg2_gt_8](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-gt-8/) | L131-L132 | formalized | — |
| `theorem` | [iota_neg2_lt_9](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-lt-9/) | L135-L136 | formalized | — |
| `def` | [sqrt3N](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-n/) | L143-L143 | defined | — |
| `def` | [sqrt3D](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-d/) | L144-L144 | defined | — |
| `def` | [correction0_numer](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-numer/) | L151-L151 | defined | — |
| `def` | [correction0_denom](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom/) | L154-L154 | defined | — |
| `theorem` | [correction0_denom_pos](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom-pos/) | L157-L158 | formalized | — |
| `theorem` | [correction0_gt_14](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-gt-14/) | L161-L162 | formalized | — |
| `theorem` | [correction0_lt_16](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-lt-16/) | L165-L166 | formalized | — |
| `theorem` | [bulk_overshoots_codata](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-overshoots-codata/) | L176-L178 | formalized | `IV.T13` |
| `theorem` | [r0_gt_1837](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-gt-1837/) | L189-L192 | formalized | `IV.T14` |
| `theorem` | [r0_lt_1840](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-lt-1840/) | L196-L199 | formalized | — |
| `theorem` | [r0_in_range](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-in-range/) | L202-L207 | formalized | — |
| `theorem` | [r0_deviation_lt_1pct](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-deviation-lt-1pct/) | L227-L254 | formalized | — |
| `structure` | [Level1PlusFormula](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/level1-plus-formula/) | L270-L281 | defined | `IV.D48` |
| `def` | [level1plus](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/level1plus/) | L284-L284 | defined | — |
| `def` | [perturbative_terms](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-terms/) | L295-L299 | defined | — |
| `theorem` | [perturbative_count](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-count/) | L302-L302 | formalized | — |
| `structure` | [ElectronMassDerivation](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-derivation/) | L315-L324 | defined | — |
| `theorem` | [electron_mass_consistent](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-consistent/) | L329-L332 | formalized | — |
| `structure` | [RDerivationLink](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/rderivation-link/) | L339-L346 | defined | — |
| `def` | [r_derivation_chain](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/r-derivation-chain/) | L349-L360 | defined | — |
| `theorem` | [chain_length](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-length/) | L363-L363 | formalized | `IV.T15` |
| `theorem` | [chain_all_tau_effective](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-all-tau-effective/) | L366-L368 | formalized | `IV.P07` |
| `theorem` | [chain_scope_count](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-scope-count/) | L371-L374 | formalized | — |
| `structure` | [FormulaLevel](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level/) | L381-L390 | defined | — |
| `def` | [formula_levels](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-levels/) | L393-L403 | defined | — |
| `theorem` | [formula_level_count](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level-count/) | L406-L406 | formalized | — |
| `eval` | [#eval L413](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l413/) | L413-L413 | computed | — |
| `eval` | [#eval L416](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l416/) | L416-L416 | computed | — |
| `eval` | [#eval L419](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l419/) | L419-L419 | computed | — |
| `eval` | [#eval L423](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l423/) | L423-L423 | computed | — |
| `eval` | [#eval L424](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l424/) | L424-L424 | computed | — |
| `eval` | [#eval L427](/verify/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l427/) | L427-L429 | computed | — |

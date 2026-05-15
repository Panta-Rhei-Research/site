---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.MassRatioFormula",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/",
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
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-numer/",
      "source_line_start": 89,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D46"
      ]
    },
    {
      "kind": "def",
      "name": "bulk_denom",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom/",
      "source_line_start": 92,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom-pos/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "bulk_float",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-float/",
      "source_line_start": 99,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_gt_1853",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-gt-1853/",
      "source_line_start": 107,
      "source_line_end": 108,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_lt_1855",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-lt-1855/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_in_range",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-in-range/",
      "source_line_start": 115,
      "source_line_end": 118,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_neg2_numer",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-numer/",
      "source_line_start": 125,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_neg2_denom",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-denom/",
      "source_line_start": 128,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_neg2_gt_8",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-gt-8/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_neg2_lt_9",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-lt-9/",
      "source_line_start": 135,
      "source_line_end": 136,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3N",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-n/",
      "source_line_start": 143,
      "source_line_end": 143,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sqrt3D",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-d/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "correction0_numer",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-numer/",
      "source_line_start": 151,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "correction0_denom",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom/",
      "source_line_start": 154,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction0_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom-pos/",
      "source_line_start": 157,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction0_gt_14",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-gt-14/",
      "source_line_start": 161,
      "source_line_end": 162,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correction0_lt_16",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-lt-16/",
      "source_line_start": 165,
      "source_line_end": 166,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_overshoots_codata",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-overshoots-codata/",
      "source_line_start": 176,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T13"
      ]
    },
    {
      "kind": "theorem",
      "name": "r0_gt_1837",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-gt-1837/",
      "source_line_start": 189,
      "source_line_end": 192,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T14"
      ]
    },
    {
      "kind": "theorem",
      "name": "r0_lt_1840",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-lt-1840/",
      "source_line_start": 196,
      "source_line_end": 199,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "r0_in_range",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-in-range/",
      "source_line_start": 202,
      "source_line_end": 207,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "r0_deviation_lt_1pct",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-deviation-lt-1pct/",
      "source_line_start": 227,
      "source_line_end": 254,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Level1PlusFormula",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/level1-plus-formula/",
      "source_line_start": 270,
      "source_line_end": 281,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D48"
      ]
    },
    {
      "kind": "def",
      "name": "level1plus",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/level1plus/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "perturbative_terms",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-terms/",
      "source_line_start": 295,
      "source_line_end": 299,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "perturbative_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-count/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ElectronMassDerivation",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-derivation/",
      "source_line_start": 315,
      "source_line_end": 324,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "electron_mass_consistent",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-consistent/",
      "source_line_start": 329,
      "source_line_end": 332,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RDerivationLink",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/rderivation-link/",
      "source_line_start": 339,
      "source_line_end": 346,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "r_derivation_chain",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r-derivation-chain/",
      "source_line_start": 349,
      "source_line_end": 360,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_length",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-length/",
      "source_line_start": 363,
      "source_line_end": 363,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T15"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_all_tau_effective",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-all-tau-effective/",
      "source_line_start": 366,
      "source_line_end": 368,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P07"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_scope_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-scope-count/",
      "source_line_start": 371,
      "source_line_end": 374,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "FormulaLevel",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level/",
      "source_line_start": 381,
      "source_line_end": 390,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "formula_levels",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-levels/",
      "source_line_start": 393,
      "source_line_end": 403,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "formula_level_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level-count/",
      "source_line_start": 406,
      "source_line_end": 406,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l416/",
      "source_line_start": 416,
      "source_line_end": 416,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l419/",
      "source_line_start": 419,
      "source_line_end": 419,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l423/",
      "source_line_start": 423,
      "source_line_end": 423,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l424/",
      "source_line_start": 424,
      "source_line_end": 424,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l427/",
      "source_line_start": 427,
      "source_line_end": 429,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [bulk_numer](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-numer/) | L89-L89 | data/computed value | data/computed value | `IV.D46` |
| `def` | [bulk_denom](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom/) | L92-L92 | data/computed value | data/computed value | — |
| `theorem` | [bulk_denom_pos](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-denom-pos/) | L95-L96 | proof obligation | formal proof obligation checked | — |
| `def` | [bulk_float](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-float/) | L99-L100 | data/computed value | data/computed value | — |
| `theorem` | [bulk_gt_1853](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-gt-1853/) | L107-L108 | proof obligation | formal proof obligation checked | — |
| `theorem` | [bulk_lt_1855](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-lt-1855/) | L111-L112 | proof obligation | formal proof obligation checked | — |
| `theorem` | [bulk_in_range](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-in-range/) | L115-L118 | proof obligation | formal proof obligation checked | — |
| `def` | [iota_neg2_numer](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-numer/) | L125-L125 | data/computed value | data/computed value | — |
| `def` | [iota_neg2_denom](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-denom/) | L128-L128 | data/computed value | data/computed value | — |
| `theorem` | [iota_neg2_gt_8](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-gt-8/) | L131-L132 | proof obligation | formal proof obligation checked | — |
| `theorem` | [iota_neg2_lt_9](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/iota-neg2-lt-9/) | L135-L136 | proof obligation | formal proof obligation checked | — |
| `def` | [sqrt3N](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-n/) | L143-L143 | data/computed value | data/computed value | — |
| `def` | [sqrt3D](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/sqrt3-d/) | L144-L144 | data/computed value | data/computed value | — |
| `def` | [correction0_numer](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-numer/) | L151-L151 | data/computed value | data/computed value | — |
| `def` | [correction0_denom](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom/) | L154-L154 | data/computed value | data/computed value | — |
| `theorem` | [correction0_denom_pos](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-denom-pos/) | L157-L158 | proof obligation | formal proof obligation checked | — |
| `theorem` | [correction0_gt_14](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-gt-14/) | L161-L162 | proof obligation | formal proof obligation checked | — |
| `theorem` | [correction0_lt_16](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/correction0-lt-16/) | L165-L166 | proof obligation | formal proof obligation checked | — |
| `theorem` | [bulk_overshoots_codata](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/bulk-overshoots-codata/) | L176-L178 | proof obligation | formal proof obligation checked | `IV.T13` |
| `theorem` | [r0_gt_1837](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-gt-1837/) | L189-L192 | proof obligation | formal proof obligation checked | `IV.T14` |
| `theorem` | [r0_lt_1840](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-lt-1840/) | L196-L199 | proof obligation | formal proof obligation checked | — |
| `theorem` | [r0_in_range](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-in-range/) | L202-L207 | proof obligation | formal proof obligation checked | — |
| `theorem` | [r0_deviation_lt_1pct](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r0-deviation-lt-1pct/) | L227-L254 | proof obligation | formal proof obligation checked | — |
| `structure` | [Level1PlusFormula](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/level1-plus-formula/) | L270-L281 | type/data schema | type/data schema | `IV.D48` |
| `def` | [level1plus](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/level1plus/) | L284-L284 | definition | definition | — |
| `def` | [perturbative_terms](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-terms/) | L295-L299 | data/computed value | data/computed value | — |
| `theorem` | [perturbative_count](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/perturbative-count/) | L302-L302 | proof obligation | formal proof obligation checked | — |
| `structure` | [ElectronMassDerivation](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-derivation/) | L315-L324 | type/data schema | type/data schema | — |
| `theorem` | [electron_mass_consistent](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/electron-mass-consistent/) | L329-L332 | proof obligation | formal proof obligation checked | — |
| `structure` | [RDerivationLink](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/rderivation-link/) | L339-L346 | type/data schema | type/data schema | — |
| `def` | [r_derivation_chain](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/r-derivation-chain/) | L349-L360 | data/computed value | data/computed value | — |
| `theorem` | [chain_length](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-length/) | L363-L363 | proof obligation | formal proof obligation checked | `IV.T15` |
| `theorem` | [chain_all_tau_effective](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-all-tau-effective/) | L366-L368 | proof obligation | formal proof obligation checked | `IV.P07` |
| `theorem` | [chain_scope_count](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/chain-scope-count/) | L371-L374 | proof obligation | formal proof obligation checked | — |
| `structure` | [FormulaLevel](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level/) | L381-L390 | type/data schema | type/data schema | — |
| `def` | [formula_levels](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-levels/) | L393-L403 | data/computed value | data/computed value | — |
| `theorem` | [formula_level_count](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/formula-level-count/) | L406-L406 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L413](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l413/) | L413-L413 | computed check | computed check | — |
| `eval` | [#eval L416](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l416/) | L416-L416 | computed check | computed check | — |
| `eval` | [#eval L419](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l419/) | L419-L419 | computed check | computed check | — |
| `eval` | [#eval L423](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l423/) | L423-L423 | computed check | computed check | — |
| `eval` | [#eval L424](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l424/) | L424-L424 | computed check | computed check | — |
| `eval` | [#eval L427](/corpus/taulib/docs/book-iv-calibration-mass-ratio-formula/eval-l427/) | L427-L429 | computed check | computed check | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.MassDerivation.ElectronMass",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_slug": "book-iv-mass-derivation-electron-mass",
  "book": "BookIV",
  "family": "MassDerivation",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/MassDerivation/ElectronMass.lean",
  "sha256": "2efe3af4ad298fe7100ee8f14433cb6188b385cad3e73bd6f263cc6497f66349",
  "imports": [
    "TauLib.BookIV.MassDerivation.HolonomyDetail",
    "TauLib.BookIV.Calibration.MassRatioFormula"
  ],
  "imported_by": [
    "TauLib.BookIV"
  ],
  "registry_ids": [
    "IV.D316",
    "IV.D317",
    "IV.D318",
    "IV.P172",
    "IV.T117",
    "IV.T118",
    "IV.T119"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 6,
    "def": 6,
    "theorem": 16,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ChainScope",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-scope/",
      "source_line_start": 35,
      "source_line_end": 38,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ChainLink",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-link/",
      "source_line_start": 41,
      "source_line_end": 45,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "derivation_chain",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/derivation-chain/",
      "source_line_start": 48,
      "source_line_end": 59,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T117"
      ]
    },
    {
      "kind": "theorem",
      "name": "chain_link_count",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-link-count/",
      "source_line_start": 61,
      "source_line_end": 61,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_indices",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-indices/",
      "source_line_start": 63,
      "source_line_end": 65,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ScopeDistribution",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/scope-distribution/",
      "source_line_start": 72,
      "source_line_end": 78,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P172"
      ]
    },
    {
      "kind": "def",
      "name": "scope_distribution",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/scope-distribution-l80/",
      "source_line_start": 80,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_scope_distribution",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-scope-distribution/",
      "source_line_start": 87,
      "source_line_end": 90,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_no_conjectural",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-no-conjectural/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_established_count",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-established-count/",
      "source_line_start": 95,
      "source_line_end": 97,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chain_tau_effective_count",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-tau-effective-count/",
      "source_line_start": 99,
      "source_line_end": 101,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BulkTerm",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-term/",
      "source_line_start": 108,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D316"
      ]
    },
    {
      "kind": "def",
      "name": "bulk_term",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-term-l115/",
      "source_line_start": 115,
      "source_line_end": 118,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_numer_match",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-numer-match/",
      "source_line_start": 120,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_denom_match",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-denom-match/",
      "source_line_start": 121,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bulk_overshoots",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-overshoots/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T118"
      ]
    },
    {
      "kind": "theorem",
      "name": "bulk_range",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-range/",
      "source_line_start": 132,
      "source_line_end": 135,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Level0Formula",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-formula/",
      "source_line_start": 142,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D317"
      ]
    },
    {
      "kind": "def",
      "name": "level0_formula",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-formula-l148/",
      "source_line_start": 148,
      "source_line_end": 148,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "level0_range",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-range/",
      "source_line_start": 151,
      "source_line_end": 156,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T119"
      ]
    },
    {
      "kind": "theorem",
      "name": "level0_deviation_small",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-deviation-small/",
      "source_line_start": 158,
      "source_line_end": 162,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Level1PlusDetail",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level1-plus-detail/",
      "source_line_start": 170,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D318"
      ]
    },
    {
      "kind": "def",
      "name": "level1plus_detail",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level1plus-detail/",
      "source_line_start": 179,
      "source_line_end": 179,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "level1plus_no_free_params",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level1plus-no-free-params/",
      "source_line_start": 181,
      "source_line_end": 182,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ElectronMassSummary",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/electron-mass-summary/",
      "source_line_start": 189,
      "source_line_end": 196,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "electron_mass_summary",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/electron-mass-summary-l198/",
      "source_line_start": 198,
      "source_line_end": 199,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "summary_chain_length",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/summary-chain-length/",
      "source_line_start": 201,
      "source_line_end": 201,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "summary_no_free_params",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/summary-no-free-params/",
      "source_line_start": 202,
      "source_line_end": 202,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "summary_no_conjectural",
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/summary-no-conjectural/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l209/",
      "source_line_start": 209,
      "source_line_end": 209,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l210/",
      "source_line_start": 210,
      "source_line_end": 210,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l212/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l213/",
      "source_line_start": 213,
      "source_line_end": 213,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l214/",
      "source_line_start": 214,
      "source_line_end": 214,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l215/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l216/",
      "source_line_start": 216,
      "source_line_end": 216,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l217/",
      "source_line_start": 217,
      "source_line_end": 217,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l218/",
      "source_line_start": 218,
      "source_line_end": 220,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean",
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
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/MassDerivation/ElectronMass.lean`
- SHA-256: `2efe3af4ad298fe7100ee8f14433cb6188b385cad3e73bd6f263cc6497f66349`

## Registry Links

- `IV.D316` — Mass Ratio Bulk Term --- IV.D46
- `IV.D317` — Level 0 Formula --- IV.D47
- `IV.D318` — Level 1+ Formula --- IV.D48
- `IV.P172` — All Links tau-Effective --- IV.P07
- `IV.T117` — Derivation Chain Complete --- IV.T15
- `IV.T118` — Bulk Overshoots --- IV.T13
- `IV.T119` — Level 0 Range --- IV.T14

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.MassDerivation.HolonomyDetail`
- `TauLib.BookIV.Calibration.MassRatioFormula`

## Imported By

- `TauLib.BookIV`

## Declaration Counts

- `def`: 6
- `eval`: 10
- `inductive`: 1
- `structure`: 6
- `theorem`: 16

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [ChainScope](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-scope/) | L35-L38 | defined | — |
| `structure` | [ChainLink](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-link/) | L41-L45 | defined | — |
| `def` | [derivation_chain](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/derivation-chain/) | L48-L59 | defined | `IV.T117` |
| `theorem` | [chain_link_count](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-link-count/) | L61-L61 | formalized | — |
| `theorem` | [chain_indices](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-indices/) | L63-L65 | formalized | — |
| `structure` | [ScopeDistribution](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/scope-distribution/) | L72-L78 | defined | `IV.P172` |
| `def` | [scope_distribution](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/scope-distribution-l80/) | L80-L85 | defined | — |
| `theorem` | [chain_scope_distribution](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-scope-distribution/) | L87-L90 | formalized | — |
| `theorem` | [chain_no_conjectural](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-no-conjectural/) | L92-L93 | formalized | — |
| `theorem` | [chain_established_count](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-established-count/) | L95-L97 | formalized | — |
| `theorem` | [chain_tau_effective_count](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-tau-effective-count/) | L99-L101 | formalized | — |
| `structure` | [BulkTerm](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-term/) | L108-L113 | defined | `IV.D316` |
| `def` | [bulk_term](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-term-l115/) | L115-L118 | defined | — |
| `theorem` | [bulk_numer_match](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-numer-match/) | L120-L120 | formalized | — |
| `theorem` | [bulk_denom_match](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-denom-match/) | L121-L121 | formalized | — |
| `theorem` | [bulk_overshoots](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-overshoots/) | L128-L130 | formalized | `IV.T118` |
| `theorem` | [bulk_range](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-range/) | L132-L135 | formalized | — |
| `structure` | [Level0Formula](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-formula/) | L142-L146 | defined | `IV.D317` |
| `def` | [level0_formula](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-formula-l148/) | L148-L148 | defined | — |
| `theorem` | [level0_range](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-range/) | L151-L156 | formalized | `IV.T119` |
| `theorem` | [level0_deviation_small](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-deviation-small/) | L158-L162 | formalized | — |
| `structure` | [Level1PlusDetail](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level1-plus-detail/) | L170-L177 | defined | `IV.D318` |
| `def` | [level1plus_detail](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level1plus-detail/) | L179-L179 | defined | — |
| `theorem` | [level1plus_no_free_params](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level1plus-no-free-params/) | L181-L182 | formalized | — |
| `structure` | [ElectronMassSummary](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/electron-mass-summary/) | L189-L196 | defined | — |
| `def` | [electron_mass_summary](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/electron-mass-summary-l198/) | L198-L199 | defined | — |
| `theorem` | [summary_chain_length](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/summary-chain-length/) | L201-L201 | formalized | — |
| `theorem` | [summary_no_free_params](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/summary-no-free-params/) | L202-L202 | formalized | — |
| `theorem` | [summary_no_conjectural](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/summary-no-conjectural/) | L203-L203 | formalized | — |
| `eval` | [#eval L209](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l209/) | L209-L209 | computed | — |
| `eval` | [#eval L210](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l210/) | L210-L210 | computed | — |
| `eval` | [#eval L211](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l211/) | L211-L211 | computed | — |
| `eval` | [#eval L212](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l212/) | L212-L212 | computed | — |
| `eval` | [#eval L213](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l213/) | L213-L213 | computed | — |
| `eval` | [#eval L214](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l214/) | L214-L214 | computed | — |
| `eval` | [#eval L215](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l215/) | L215-L215 | computed | — |
| `eval` | [#eval L216](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l216/) | L216-L216 | computed | — |
| `eval` | [#eval L217](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l217/) | L217-L217 | computed | — |
| `eval` | [#eval L218](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/eval-l218/) | L218-L220 | computed | — |

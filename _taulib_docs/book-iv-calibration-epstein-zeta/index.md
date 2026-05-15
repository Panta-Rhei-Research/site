---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.EpsteinZeta",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.EpsteinZeta`.",
  "module_name": "TauLib.BookIV.Calibration.EpsteinZeta",
  "module_slug": "book-iv-calibration-epstein-zeta",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/EpsteinZeta.lean",
  "sha256": "a1db0eb76ee72425c3ec04f9c6124d27ff876255ce6afc24653136a725865159",
  "imports": [
    "TauLib.BookIV.Sectors.FineStructure"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.MassDerivation.BreathingModes"
  ],
  "registry_ids": [
    "IV.D40",
    "IV.D41",
    "IV.R10",
    "IV.T10"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 3,
    "theorem": 6,
    "inductive": 1,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "EpsteinZetaStructure",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/epstein-zeta-structure/",
      "source_line_start": 74,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D40"
      ]
    },
    {
      "kind": "def",
      "name": "epstein_at_T2",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/epstein-at-t2/",
      "source_line_start": 88,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ChowlaSelbergTerms",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/chowla-selberg-terms/",
      "source_line_start": 105,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D41"
      ]
    },
    {
      "kind": "def",
      "name": "chowla_selberg_s4",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/chowla-selberg-s4/",
      "source_line_start": 117,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "leading_exponent_is_neg7",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/leading-exponent-is-neg7/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T10"
      ]
    },
    {
      "kind": "theorem",
      "name": "exponent_formula_s4",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/exponent-formula-s4/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "s4_unique_from_neg7",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/s4-unique-from-neg7/",
      "source_line_start": 140,
      "source_line_end": 141,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "LatticeMode",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/lattice-mode/",
      "source_line_start": 148,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NAxisDominance",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/naxis-dominance/",
      "source_line_start": 157,
      "source_line_end": 162,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "n_axis_dominant",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/n-axis-dominant/",
      "source_line_start": 165,
      "source_line_end": 167,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NormalizationRemark",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/normalization-remark/",
      "source_line_start": 186,
      "source_line_end": 193,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R10"
      ]
    },
    {
      "kind": "theorem",
      "name": "shape_is_iota",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/shape-is-iota/",
      "source_line_start": 200,
      "source_line_end": 203,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "eval_at_s4",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-at-s4/",
      "source_line_start": 206,
      "source_line_end": 206,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chowla_selberg_consistent",
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/chowla-selberg-consistent/",
      "source_line_start": 209,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l218/",
      "source_line_start": 218,
      "source_line_end": 218,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l219/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l223/",
      "source_line_start": 223,
      "source_line_end": 223,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l224/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l227/",
      "source_line_start": 227,
      "source_line_end": 229,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean",
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
- Source path: [`TauLib/BookIV/Calibration/EpsteinZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/EpsteinZeta.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/EpsteinZeta.lean`
- SHA-256: `a1db0eb76ee72425c3ec04f9c6124d27ff876255ce6afc24653136a725865159`

## Registry Links

- `IV.D40` — Epstein Zeta Structure
- `IV.D41` — Chowla-Selberg Decomposition
- `IV.R10` — Normalization
- `IV.T10` — Leading Exponent

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.FineStructure`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.MassDerivation.BreathingModes`

## Declaration Counts

- `def`: 3
- `eval`: 6
- `inductive`: 1
- `structure`: 4
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [EpsteinZetaStructure](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/epstein-zeta-structure/) | L74-L85 | type/data schema | type/data schema | `IV.D40` |
| `def` | [epstein_at_T2](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/epstein-at-t2/) | L88-L92 | definition | definition | — |
| `structure` | [ChowlaSelbergTerms](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/chowla-selberg-terms/) | L105-L114 | type/data schema | type/data schema | `IV.D41` |
| `def` | [chowla_selberg_s4](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/chowla-selberg-s4/) | L117-L121 | definition | definition | — |
| `theorem` | [leading_exponent_is_neg7](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/leading-exponent-is-neg7/) | L132-L133 | proof obligation | formal proof obligation checked | `IV.T10` |
| `theorem` | [exponent_formula_s4](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/exponent-formula-s4/) | L136-L137 | proof obligation | formal proof obligation checked | — |
| `theorem` | [s4_unique_from_neg7](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/s4-unique-from-neg7/) | L140-L141 | proof obligation | formal proof obligation checked | — |
| `inductive` | [LatticeMode](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/lattice-mode/) | L148-L151 | type/data schema | type/data schema | — |
| `structure` | [NAxisDominance](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/naxis-dominance/) | L157-L162 | type/data schema | type/data schema | — |
| `def` | [n_axis_dominant](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/n-axis-dominant/) | L165-L167 | definition | definition | — |
| `structure` | [NormalizationRemark](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/normalization-remark/) | L186-L193 | type/data schema | type/data schema | `IV.R10` |
| `theorem` | [shape_is_iota](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/shape-is-iota/) | L200-L203 | proof obligation | formal proof obligation checked | — |
| `theorem` | [eval_at_s4](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-at-s4/) | L206-L206 | proof obligation | formal proof obligation checked | — |
| `theorem` | [chowla_selberg_consistent](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/chowla-selberg-consistent/) | L209-L211 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L218](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l218/) | L218-L218 | computed check | computed check | — |
| `eval` | [#eval L219](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l219/) | L219-L219 | computed check | computed check | — |
| `eval` | [#eval L220](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l220/) | L220-L220 | computed check | computed check | — |
| `eval` | [#eval L223](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l223/) | L223-L223 | computed check | computed check | — |
| `eval` | [#eval L224](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l224/) | L224-L224 | computed check | computed check | — |
| `eval` | [#eval L227](/corpus/taulib/docs/book-iv-calibration-epstein-zeta/eval-l227/) | L227-L229 | computed check | computed check | — |

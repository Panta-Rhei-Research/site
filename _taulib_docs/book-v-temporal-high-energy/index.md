---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.HighEnergy",
  "permalink": "/corpus/taulib/docs/book-v-temporal-high-energy/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Temporal.HighEnergy`.",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_slug": "book-v-temporal-high-energy",
  "book": "BookV",
  "family": "Temporal",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Temporal/HighEnergy.lean",
  "sha256": "9bf90797f154fc52a4f205d0d44f8a302f593a61af586ce67a0079c7aec3a9d3",
  "imports": [
    "TauLib.BookV.Temporal.TemporalIgnition",
    "TauLib.BookIV.Arena.FiveSectors"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Temporal.MacroReadout"
  ],
  "registry_ids": [
    "V.D24",
    "V.D25",
    "V.D26",
    "V.P05",
    "V.R33",
    "V.T13"
  ],
  "declaration_counts": {
    "theorem": 7,
    "structure": 4,
    "def": 2,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "full_spectrum_at_ignition",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/full-spectrum-at-ignition/",
      "source_line_start": 74,
      "source_line_end": 79,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P05"
      ]
    },
    {
      "kind": "structure",
      "name": "MaximalCouplingCondition",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/maximal-coupling-condition/",
      "source_line_start": 95,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D24"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_maximal_coupling",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/canonical-maximal-coupling/",
      "source_line_start": 106,
      "source_line_end": 110,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OpeningRegime",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/opening-regime/",
      "source_line_start": 124,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D25"
      ]
    },
    {
      "kind": "theorem",
      "name": "opening_regime_width",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/opening-regime-width/",
      "source_line_start": 136,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "opening_has_solution",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/opening-has-solution/",
      "source_line_start": 153,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T13"
      ]
    },
    {
      "kind": "theorem",
      "name": "opening_all_depths_solved",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/opening-all-depths-solved/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RefinementRate",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/refinement-rate/",
      "source_line_start": 180,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D26"
      ]
    },
    {
      "kind": "def",
      "name": "RefinementRate.toFloat",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/to-float/",
      "source_line_start": 194,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "progression_is_positive",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/progression-is-positive/",
      "source_line_start": 198,
      "source_line_end": 201,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InflationaryInterpretation",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/inflationary-interpretation/",
      "source_line_start": 217,
      "source_line_end": 226,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R33"
      ]
    },
    {
      "kind": "theorem",
      "name": "inflation_remark",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/inflation-remark/",
      "source_line_start": 229,
      "source_line_end": 231,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rate_hierarchy",
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/rate-hierarchy/",
      "source_line_start": 238,
      "source_line_end": 242,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/eval-l248/",
      "source_line_start": 248,
      "source_line_end": 248,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/eval-l249/",
      "source_line_start": 249,
      "source_line_end": 249,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/eval-l252/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/eval-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-high-energy/eval-l256/",
      "source_line_start": 256,
      "source_line_end": 258,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean",
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
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Temporal/HighEnergy.lean`
- SHA-256: `9bf90797f154fc52a4f205d0d44f8a302f593a61af586ce67a0079c7aec3a9d3`

## Registry Links

- `V.D24` — Maximal Coupling Condition
- `V.D25` — Opening Regime
- `V.D26` — Refinement Progression Rate
- `V.P05` — Mode Counting at Early Depths
- `V.R33` — Inflation as Progression
- `V.T13` — Opening Regime Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Temporal.TemporalIgnition`
- `TauLib.BookIV.Arena.FiveSectors`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Temporal.MacroReadout`

## Declaration Counts

- `def`: 2
- `eval`: 5
- `structure`: 4
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `theorem` | [full_spectrum_at_ignition](/corpus/taulib/docs/book-v-temporal-high-energy/full-spectrum-at-ignition/) | L74-L79 | proof obligation | formal proof obligation checked | `V.P05` |
| `structure` | [MaximalCouplingCondition](/corpus/taulib/docs/book-v-temporal-high-energy/maximal-coupling-condition/) | L95-L103 | type/data schema | type/data schema | `V.D24` |
| `def` | [canonical_maximal_coupling](/corpus/taulib/docs/book-v-temporal-high-energy/canonical-maximal-coupling/) | L106-L110 | definition | definition | — |
| `structure` | [OpeningRegime](/corpus/taulib/docs/book-v-temporal-high-energy/opening-regime/) | L124-L133 | type/data schema | type/data schema | `V.D25` |
| `theorem` | [opening_regime_width](/corpus/taulib/docs/book-v-temporal-high-energy/opening-regime-width/) | L136-L138 | proof obligation | formal proof obligation checked | — |
| `theorem` | [opening_has_solution](/corpus/taulib/docs/book-v-temporal-high-energy/opening-has-solution/) | L153-L158 | proof obligation | formal proof obligation checked | `V.T13` |
| `theorem` | [opening_all_depths_solved](/corpus/taulib/docs/book-v-temporal-high-energy/opening-all-depths-solved/) | L161-L163 | proof obligation | formal proof obligation checked | — |
| `structure` | [RefinementRate](/corpus/taulib/docs/book-v-temporal-high-energy/refinement-rate/) | L180-L191 | type/data schema | type/data schema | `V.D26` |
| `def` | [RefinementRate.toFloat](/corpus/taulib/docs/book-v-temporal-high-energy/to-float/) | L194-L195 | data/computed value | data/computed value | — |
| `theorem` | [progression_is_positive](/corpus/taulib/docs/book-v-temporal-high-energy/progression-is-positive/) | L198-L201 | proof obligation | formal proof obligation checked | — |
| `structure` | [InflationaryInterpretation](/corpus/taulib/docs/book-v-temporal-high-energy/inflationary-interpretation/) | L217-L226 | type/data schema | type/data schema | `V.R33` |
| `theorem` | [inflation_remark](/corpus/taulib/docs/book-v-temporal-high-energy/inflation-remark/) | L229-L231 | proof obligation | formal proof obligation checked | — |
| `theorem` | [rate_hierarchy](/corpus/taulib/docs/book-v-temporal-high-energy/rate-hierarchy/) | L238-L242 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L248](/corpus/taulib/docs/book-v-temporal-high-energy/eval-l248/) | L248-L248 | computed check | computed check | — |
| `eval` | [#eval L249](/corpus/taulib/docs/book-v-temporal-high-energy/eval-l249/) | L249-L249 | computed check | computed check | — |
| `eval` | [#eval L252](/corpus/taulib/docs/book-v-temporal-high-energy/eval-l252/) | L252-L252 | computed check | computed check | — |
| `eval` | [#eval L253](/corpus/taulib/docs/book-v-temporal-high-energy/eval-l253/) | L253-L253 | computed check | computed check | — |
| `eval` | [#eval L256](/corpus/taulib/docs/book-v-temporal-high-energy/eval-l256/) | L256-L258 | computed check | computed check | — |

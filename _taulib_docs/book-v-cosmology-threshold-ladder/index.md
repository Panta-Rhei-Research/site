---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.ThresholdLadder",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_slug": "book-v-cosmology-threshold-ladder",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/ThresholdLadder.lean",
  "sha256": "e527e6a6c324f20e50b3c7cad5ff6be49ccf70b54d868f44b58c22bef6af23df",
  "imports": [
    "TauLib.BookV.Cosmology.InflationRegime"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Cosmology.BBNBaryogenesis",
    "TauLib.BookV.Cosmology.BHBirthTopology",
    "TauLib.BookV.Cosmology.HeliumFraction"
  ],
  "registry_ids": [
    "V.D158",
    "V.D159",
    "V.D160",
    "V.D161",
    "V.D162",
    "V.P92",
    "V.R218",
    "V.R219",
    "V.R220",
    "V.R221",
    "V.T107",
    "V.T108"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 9,
    "def": 5,
    "theorem": 3,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ThresholdType",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/threshold-type/",
      "source_line_start": 64,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdRegimeBoundary",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/threshold-regime-boundary/",
      "source_line_start": 84,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D158"
      ]
    },
    {
      "kind": "structure",
      "name": "CanonicalThresholds",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/canonical-thresholds/",
      "source_line_start": 103,
      "source_line_end": 122,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D159"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_ladder",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/canonical-ladder/",
      "source_line_start": 125,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladder_monotonicity",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/ladder-monotonicity/",
      "source_line_start": 146,
      "source_line_end": 152,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T107"
      ]
    },
    {
      "kind": "structure",
      "name": "NeutronThreshold",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/neutron-threshold/",
      "source_line_start": 166,
      "source_line_end": 173,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D160"
      ]
    },
    {
      "kind": "structure",
      "name": "SakharovConditions",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/sakharov-conditions/",
      "source_line_start": 185,
      "source_line_end": 194,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R220"
      ]
    },
    {
      "kind": "structure",
      "name": "NucleosyntheticWindow",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthetic-window/",
      "source_line_start": 205,
      "source_line_end": 214,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D161"
      ]
    },
    {
      "kind": "structure",
      "name": "NucleosynthesisResult",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-result/",
      "source_line_start": 228,
      "source_line_end": 233,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T108"
      ]
    },
    {
      "kind": "def",
      "name": "tau_yp",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/tau-yp/",
      "source_line_start": 236,
      "source_line_end": 238,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleosynthesis_from_tau",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-from-tau/",
      "source_line_start": 241,
      "source_line_end": 243,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CmbOrigin",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin/",
      "source_line_start": 257,
      "source_line_end": 264,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P92"
      ]
    },
    {
      "kind": "def",
      "name": "observed_cmb",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/observed-cmb/",
      "source_line_start": 267,
      "source_line_end": 270,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cmb_origin",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MassHierarchyAtLN",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-at-ln/",
      "source_line_start": 283,
      "source_line_end": 288,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R218"
      ]
    },
    {
      "kind": "def",
      "name": "mass_hierarchy_r",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-r/",
      "source_line_start": 291,
      "source_line_end": 293,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdLadderComplete",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/threshold-ladder-complete/",
      "source_line_start": 301,
      "source_line_end": 308,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D162"
      ]
    },
    {
      "kind": "def",
      "name": "complete_ladder",
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/complete-ladder/",
      "source_line_start": 311,
      "source_line_end": 314,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R219",
        "V.R221"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l337/",
      "source_line_start": 337,
      "source_line_end": 339,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean",
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
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/ThresholdLadder.lean`
- SHA-256: `e527e6a6c324f20e50b3c7cad5ff6be49ccf70b54d868f44b58c22bef6af23df`

## Registry Links

- `V.D158` — Threshold (Regime Boundary)
- `V.D159` — Canonical Thresholds
- `V.D160` — Neutron Threshold L_N
- `V.D161` — Nucleosynthetic Window
- `V.D162` — Threshold Ladder
- `V.P92` — CMB Origin
- `V.R218` — The mass hierarchy at L_N
- `V.R219` — Sphaleron Open Question
- `V.R220` — Sakharov Conditions
- `V.R221` — The lithium problem
- `V.T107` — Ladder Monotonicity
- `V.T108` — Nucleosynthesis from tau

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.InflationRegime`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Cosmology.BBNBaryogenesis`
- `TauLib.BookV.Cosmology.BHBirthTopology`
- `TauLib.BookV.Cosmology.HeliumFraction`

## Declaration Counts

- `def`: 5
- `eval`: 6
- `inductive`: 1
- `structure`: 9
- `theorem`: 3

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [ThresholdType](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/threshold-type/) | L64-L77 | type/data schema | type/data schema | — |
| `structure` | [ThresholdRegimeBoundary](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/threshold-regime-boundary/) | L84-L95 | type/data schema | type/data schema | `V.D158` |
| `structure` | [CanonicalThresholds](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/canonical-thresholds/) | L103-L122 | type/data schema | type/data schema | `V.D159` |
| `def` | [canonical_ladder](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/canonical-ladder/) | L125-L138 | definition | definition | — |
| `theorem` | [ladder_monotonicity](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/ladder-monotonicity/) | L146-L152 | proof obligation | formal proof obligation checked | `V.T107` |
| `structure` | [NeutronThreshold](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/neutron-threshold/) | L166-L173 | type/data schema | type/data schema | `V.D160` |
| `structure` | [SakharovConditions](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/sakharov-conditions/) | L185-L194 | type/data schema | type/data schema | `V.R220` |
| `structure` | [NucleosyntheticWindow](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthetic-window/) | L205-L214 | type/data schema | type/data schema | `V.D161` |
| `structure` | [NucleosynthesisResult](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-result/) | L228-L233 | type/data schema | type/data schema | `V.T108` |
| `def` | [tau_yp](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/tau-yp/) | L236-L238 | definition | definition | — |
| `theorem` | [nucleosynthesis_from_tau](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-from-tau/) | L241-L243 | proof obligation | formal proof obligation checked | — |
| `structure` | [CmbOrigin](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin/) | L257-L264 | type/data schema | type/data schema | `V.P92` |
| `def` | [observed_cmb](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/observed-cmb/) | L267-L270 | definition | definition | — |
| `theorem` | [cmb_origin](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin-l273/) | L273-L273 | proof obligation | formal proof obligation checked | — |
| `structure` | [MassHierarchyAtLN](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-at-ln/) | L283-L288 | type/data schema | type/data schema | `V.R218` |
| `def` | [mass_hierarchy_r](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-r/) | L291-L293 | definition | definition | — |
| `structure` | [ThresholdLadderComplete](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/threshold-ladder-complete/) | L301-L308 | type/data schema | type/data schema | `V.D162` |
| `def` | [complete_ladder](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/complete-ladder/) | L311-L314 | definition | definition | — |
| `eval` | [#eval L332](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l332/) | L332-L332 | computed check | computed check | `V.R219`, `V.R221` |
| `eval` | [#eval L333](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l333/) | L333-L333 | computed check | computed check | — |
| `eval` | [#eval L334](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l334/) | L334-L334 | computed check | computed check | — |
| `eval` | [#eval L335](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l335/) | L335-L335 | computed check | computed check | — |
| `eval` | [#eval L336](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l336/) | L336-L336 | computed check | computed check | — |
| `eval` | [#eval L337](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/eval-l337/) | L337-L339 | computed check | computed check | — |

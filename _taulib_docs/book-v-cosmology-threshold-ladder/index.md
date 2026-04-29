---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.ThresholdLadder",
  "permalink": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/",
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
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-type/",
      "source_line_start": 64,
      "source_line_end": 77,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdRegimeBoundary",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-regime-boundary/",
      "source_line_start": 84,
      "source_line_end": 95,
      "formal_status": "defined",
      "registry_ids": [
        "V.D158"
      ]
    },
    {
      "kind": "structure",
      "name": "CanonicalThresholds",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/canonical-thresholds/",
      "source_line_start": 103,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": [
        "V.D159"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_ladder",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/canonical-ladder/",
      "source_line_start": 125,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ladder_monotonicity",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/ladder-monotonicity/",
      "source_line_start": 146,
      "source_line_end": 152,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T107"
      ]
    },
    {
      "kind": "structure",
      "name": "NeutronThreshold",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/neutron-threshold/",
      "source_line_start": 166,
      "source_line_end": 173,
      "formal_status": "defined",
      "registry_ids": [
        "V.D160"
      ]
    },
    {
      "kind": "structure",
      "name": "SakharovConditions",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/sakharov-conditions/",
      "source_line_start": 185,
      "source_line_end": 194,
      "formal_status": "defined",
      "registry_ids": [
        "V.R220"
      ]
    },
    {
      "kind": "structure",
      "name": "NucleosyntheticWindow",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthetic-window/",
      "source_line_start": 205,
      "source_line_end": 214,
      "formal_status": "defined",
      "registry_ids": [
        "V.D161"
      ]
    },
    {
      "kind": "structure",
      "name": "NucleosynthesisResult",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-result/",
      "source_line_start": 228,
      "source_line_end": 233,
      "formal_status": "defined",
      "registry_ids": [
        "V.T108"
      ]
    },
    {
      "kind": "def",
      "name": "tau_yp",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/tau-yp/",
      "source_line_start": 236,
      "source_line_end": 238,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleosynthesis_from_tau",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-from-tau/",
      "source_line_start": 241,
      "source_line_end": 243,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CmbOrigin",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin/",
      "source_line_start": 257,
      "source_line_end": 264,
      "formal_status": "defined",
      "registry_ids": [
        "V.P92"
      ]
    },
    {
      "kind": "def",
      "name": "observed_cmb",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/observed-cmb/",
      "source_line_start": 267,
      "source_line_end": 270,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cmb_origin",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MassHierarchyAtLN",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-at-ln/",
      "source_line_start": 283,
      "source_line_end": 288,
      "formal_status": "defined",
      "registry_ids": [
        "V.R218"
      ]
    },
    {
      "kind": "def",
      "name": "mass_hierarchy_r",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-r/",
      "source_line_start": 291,
      "source_line_end": 293,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ThresholdLadderComplete",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-ladder-complete/",
      "source_line_start": 301,
      "source_line_end": 308,
      "formal_status": "defined",
      "registry_ids": [
        "V.D162"
      ]
    },
    {
      "kind": "def",
      "name": "complete_ladder",
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/complete-ladder/",
      "source_line_start": 311,
      "source_line_end": 314,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "registry_ids": [
        "V.R219",
        "V.R221"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l337/",
      "source_line_start": 337,
      "source_line_end": 339,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [ThresholdType](/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-type/) | L64-L77 | defined | — |
| `structure` | [ThresholdRegimeBoundary](/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-regime-boundary/) | L84-L95 | defined | `V.D158` |
| `structure` | [CanonicalThresholds](/verify/taulib/docs/book-v-cosmology-threshold-ladder/canonical-thresholds/) | L103-L122 | defined | `V.D159` |
| `def` | [canonical_ladder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/canonical-ladder/) | L125-L138 | defined | — |
| `theorem` | [ladder_monotonicity](/verify/taulib/docs/book-v-cosmology-threshold-ladder/ladder-monotonicity/) | L146-L152 | formalized | `V.T107` |
| `structure` | [NeutronThreshold](/verify/taulib/docs/book-v-cosmology-threshold-ladder/neutron-threshold/) | L166-L173 | defined | `V.D160` |
| `structure` | [SakharovConditions](/verify/taulib/docs/book-v-cosmology-threshold-ladder/sakharov-conditions/) | L185-L194 | defined | `V.R220` |
| `structure` | [NucleosyntheticWindow](/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthetic-window/) | L205-L214 | defined | `V.D161` |
| `structure` | [NucleosynthesisResult](/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-result/) | L228-L233 | defined | `V.T108` |
| `def` | [tau_yp](/verify/taulib/docs/book-v-cosmology-threshold-ladder/tau-yp/) | L236-L238 | defined | — |
| `theorem` | [nucleosynthesis_from_tau](/verify/taulib/docs/book-v-cosmology-threshold-ladder/nucleosynthesis-from-tau/) | L241-L243 | formalized | — |
| `structure` | [CmbOrigin](/verify/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin/) | L257-L264 | defined | `V.P92` |
| `def` | [observed_cmb](/verify/taulib/docs/book-v-cosmology-threshold-ladder/observed-cmb/) | L267-L270 | defined | — |
| `theorem` | [cmb_origin](/verify/taulib/docs/book-v-cosmology-threshold-ladder/cmb-origin-l273/) | L273-L273 | formalized | — |
| `structure` | [MassHierarchyAtLN](/verify/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-at-ln/) | L283-L288 | defined | `V.R218` |
| `def` | [mass_hierarchy_r](/verify/taulib/docs/book-v-cosmology-threshold-ladder/mass-hierarchy-r/) | L291-L293 | defined | — |
| `structure` | [ThresholdLadderComplete](/verify/taulib/docs/book-v-cosmology-threshold-ladder/threshold-ladder-complete/) | L301-L308 | defined | `V.D162` |
| `def` | [complete_ladder](/verify/taulib/docs/book-v-cosmology-threshold-ladder/complete-ladder/) | L311-L314 | defined | — |
| `eval` | [#eval L332](/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l332/) | L332-L332 | computed | `V.R219`, `V.R221` |
| `eval` | [#eval L333](/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l333/) | L333-L333 | computed | — |
| `eval` | [#eval L334](/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l334/) | L334-L334 | computed | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L336](/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l336/) | L336-L336 | computed | — |
| `eval` | [#eval L337](/verify/taulib/docs/book-v-cosmology-threshold-ladder/eval-l337/) | L337-L339 | computed | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_slug": "book-v-fluid-macro-navier-stokes-macro",
  "book": "BookV",
  "family": "FluidMacro",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/FluidMacro/NavierStokesMacro.lean",
  "sha256": "1742b34a5558084801ed38dece63f1a63c57bf3b96029f60cc68a4a97b0a46fa",
  "imports": [
    "TauLib.BookV.GravityField.ClosingIdentity"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.FluidMacro.Turbulence"
  ],
  "registry_ids": [
    "V.C09",
    "V.D314",
    "V.D315",
    "V.D96",
    "V.D97",
    "V.D98",
    "V.P174",
    "V.P42",
    "V.P43",
    "V.R137",
    "V.R138",
    "V.R139",
    "V.R140",
    "V.R141",
    "V.R142",
    "V.R143",
    "V.R144",
    "V.R446",
    "V.T254",
    "V.T70",
    "V.T71"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 8,
    "theorem": 11,
    "inductive": 1,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "MacroDefectTransport",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-defect-transport/",
      "source_line_start": 68,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D96"
      ]
    },
    {
      "kind": "def",
      "name": "MacroDefectTransport.totalBudget",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/total-budget/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroTauNSFlow",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-nsflow/",
      "source_line_start": 98,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D97"
      ]
    },
    {
      "kind": "structure",
      "name": "Tau3Compactness",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compactness/",
      "source_line_start": 120,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P42"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau3_compact",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compact/",
      "source_line_start": 135,
      "source_line_end": 143,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "MacroRegCondition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reg-condition/",
      "source_line_start": 150,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroThreeConditions",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-conditions/",
      "source_line_start": 162,
      "source_line_end": 169,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T70"
      ]
    },
    {
      "kind": "theorem",
      "name": "macro_three_condition_sufficiency",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-condition-sufficiency/",
      "source_line_start": 172,
      "source_line_end": 177,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "macro_tau_ns_regularity",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-ns-regularity/",
      "source_line_start": 189,
      "source_line_end": 195,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T71"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_temporal_blowup",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/no-temporal-blowup/",
      "source_line_start": 205,
      "source_line_end": 209,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C09"
      ]
    },
    {
      "kind": "structure",
      "name": "MacroReynoldsNumber",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reynolds-number/",
      "source_line_start": 220,
      "source_line_end": 229,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D98"
      ]
    },
    {
      "kind": "def",
      "name": "MacroReynoldsNumber.ratio",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/ratio/",
      "source_line_start": 232,
      "source_line_end": 233,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reynolds_bounded",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/reynolds-bounded/",
      "source_line_start": 236,
      "source_line_end": 240,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "enrichment_independent",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/enrichment-independent/",
      "source_line_start": 250,
      "source_line_end": 254,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R137"
      ]
    },
    {
      "kind": "def",
      "name": "convective_overshooting",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting/",
      "source_line_start": 263,
      "source_line_end": 265,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R141"
      ]
    },
    {
      "kind": "theorem",
      "name": "convective_overshooting_holds",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting-holds/",
      "source_line_start": 267,
      "source_line_end": 269,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "classical_ns_as_readout",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/classical-ns-as-readout/",
      "source_line_start": 282,
      "source_line_end": 284,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P43"
      ]
    },
    {
      "kind": "structure",
      "name": "DecompactificationBound",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompactification-bound/",
      "source_line_start": 298,
      "source_line_end": 311,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D314"
      ]
    },
    {
      "kind": "def",
      "name": "decompact_depth3",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth3/",
      "source_line_start": 314,
      "source_line_end": 320,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "decompact_depth5",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth5/",
      "source_line_start": 323,
      "source_line_end": 329,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AdmissibilityClass",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class/",
      "source_line_start": 340,
      "source_line_end": 349,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D315"
      ]
    },
    {
      "kind": "def",
      "name": "admissibility_class",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_convergence",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/primorial-convergence/",
      "source_line_start": 364,
      "source_line_end": 366,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T254"
      ]
    },
    {
      "kind": "theorem",
      "name": "depth5_near_leray",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/depth5-near-leray/",
      "source_line_start": 369,
      "source_line_end": 372,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "leray_limit_recovery",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/leray-limit-recovery/",
      "source_line_start": 382,
      "source_line_end": 384,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P174"
      ]
    },
    {
      "kind": "def",
      "name": "example_transport",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-transport/",
      "source_line_start": 421,
      "source_line_end": 426,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l428/",
      "source_line_start": 428,
      "source_line_end": 428,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l429/",
      "source_line_start": 429,
      "source_line_end": 429,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_reynolds",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-reynolds/",
      "source_line_start": 432,
      "source_line_end": 436,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l438/",
      "source_line_start": 438,
      "source_line_end": 440,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean",
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
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/FluidMacro/NavierStokesMacro.lean`
- SHA-256: `1742b34a5558084801ed38dece63f1a63c57bf3b96029f60cc68a4a97b0a46fa`

## Registry Links

- `V.C09` — No temporal blow-up
- `V.D314` — Decompactification Bound
- `V.D315` — Admissibility Class
- `V.D96` — Macro defect-transport equation
- `V.D97` — Macro tau-Navier--Stokes flow
- `V.D98` — Macro tau-Reynolds number
- `V.P174` — Leray Limit Recovery
- `V.P42` — Compactness of tau^3
- `V.P43` — Classical NS as readout
- `V.R137` — III.T25 is enrichment-layer independent
- `V.R138` — Fiber contributions are not discarded
- `V.R139` — Contrast with mathbbR
- `V.R140` — The Reynolds number is bounded
- `V.R141` — Convective overshooting
- `V.R142` — No singularity at the innermost stable orbit
- `V.R143` — Honest claim
- `V.R144` — The chart domain is compact
- `V.R446` — Clay Bridge Status
- `V.T254` — Primorial Convergence Rate
- `V.T70` — Macro three-condition sufficiency
- `V.T71` — Macro tau-NS regularity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.ClosingIdentity`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.FluidMacro.Turbulence`

## Declaration Counts

- `def`: 8
- `eval`: 3
- `inductive`: 1
- `structure`: 7
- `theorem`: 11

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [MacroDefectTransport](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-defect-transport/) | L68-L83 | type/data schema | type/data schema | `V.D96` |
| `def` | [MacroDefectTransport.totalBudget](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/total-budget/) | L86-L87 | data/computed value | data/computed value | — |
| `structure` | [MacroTauNSFlow](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-nsflow/) | L98-L107 | type/data schema | type/data schema | `V.D97` |
| `structure` | [Tau3Compactness](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compactness/) | L120-L132 | type/data schema | type/data schema | `V.P42` |
| `theorem` | [tau3_compact](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compact/) | L135-L143 | proof obligation | formal proof obligation checked | — |
| `inductive` | [MacroRegCondition](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reg-condition/) | L150-L157 | type/data schema | type/data schema | — |
| `structure` | [MacroThreeConditions](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-conditions/) | L162-L169 | type/data schema | type/data schema | `V.T70` |
| `theorem` | [macro_three_condition_sufficiency](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-condition-sufficiency/) | L172-L177 | proof obligation | formal proof obligation checked | — |
| `theorem` | [macro_tau_ns_regularity](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-ns-regularity/) | L189-L195 | proof obligation | formal proof obligation checked | `V.T71` |
| `theorem` | [no_temporal_blowup](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/no-temporal-blowup/) | L205-L209 | proof obligation | formal proof obligation checked | `V.C09` |
| `structure` | [MacroReynoldsNumber](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reynolds-number/) | L220-L229 | type/data schema | type/data schema | `V.D98` |
| `def` | [MacroReynoldsNumber.ratio](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/ratio/) | L232-L233 | data/computed value | data/computed value | — |
| `theorem` | [reynolds_bounded](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/reynolds-bounded/) | L236-L240 | proof obligation | formal proof obligation checked | — |
| `theorem` | [enrichment_independent](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/enrichment-independent/) | L250-L254 | proof obligation | formal proof obligation checked | `V.R137` |
| `def` | [convective_overshooting](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting/) | L263-L265 | definition | definition | `V.R141` |
| `theorem` | [convective_overshooting_holds](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting-holds/) | L267-L269 | proof obligation | formal proof obligation checked | — |
| `theorem` | [classical_ns_as_readout](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/classical-ns-as-readout/) | L282-L284 | proof obligation | formal proof obligation checked | `V.P43` |
| `structure` | [DecompactificationBound](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompactification-bound/) | L298-L311 | type/data schema | type/data schema | `V.D314` |
| `def` | [decompact_depth3](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth3/) | L314-L320 | definition | definition | — |
| `def` | [decompact_depth5](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth5/) | L323-L329 | definition | definition | — |
| `structure` | [AdmissibilityClass](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class/) | L340-L349 | type/data schema | type/data schema | `V.D315` |
| `def` | [admissibility_class](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class-l352/) | L352-L352 | definition | definition | — |
| `theorem` | [primorial_convergence](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/primorial-convergence/) | L364-L366 | proof obligation | formal proof obligation checked | `V.T254` |
| `theorem` | [depth5_near_leray](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/depth5-near-leray/) | L369-L372 | proof obligation | formal proof obligation checked | — |
| `theorem` | [leray_limit_recovery](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/leray-limit-recovery/) | L382-L384 | proof obligation | formal proof obligation checked | `V.P174` |
| `def` | [example_transport](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-transport/) | L421-L426 | definition | definition | — |
| `eval` | [#eval L428](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l428/) | L428-L428 | computed check | computed check | — |
| `eval` | [#eval L429](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l429/) | L429-L429 | computed check | computed check | — |
| `def` | [example_reynolds](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-reynolds/) | L432-L436 | definition | definition | — |
| `eval` | [#eval L438](/corpus/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l438/) | L438-L440 | computed check | computed check | — |

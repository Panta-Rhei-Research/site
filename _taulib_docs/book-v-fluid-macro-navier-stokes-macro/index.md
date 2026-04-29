---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
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
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-defect-transport/",
      "source_line_start": 68,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": [
        "V.D96"
      ]
    },
    {
      "kind": "def",
      "name": "MacroDefectTransport.totalBudget",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/total-budget/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroTauNSFlow",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-nsflow/",
      "source_line_start": 98,
      "source_line_end": 107,
      "formal_status": "defined",
      "registry_ids": [
        "V.D97"
      ]
    },
    {
      "kind": "structure",
      "name": "Tau3Compactness",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compactness/",
      "source_line_start": 120,
      "source_line_end": 132,
      "formal_status": "defined",
      "registry_ids": [
        "V.P42"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau3_compact",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compact/",
      "source_line_start": 135,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "MacroRegCondition",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reg-condition/",
      "source_line_start": 150,
      "source_line_end": 157,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroThreeConditions",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-conditions/",
      "source_line_start": 162,
      "source_line_end": 169,
      "formal_status": "defined",
      "registry_ids": [
        "V.T70"
      ]
    },
    {
      "kind": "theorem",
      "name": "macro_three_condition_sufficiency",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-condition-sufficiency/",
      "source_line_start": 172,
      "source_line_end": 177,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "macro_tau_ns_regularity",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-ns-regularity/",
      "source_line_start": 189,
      "source_line_end": 195,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T71"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_temporal_blowup",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/no-temporal-blowup/",
      "source_line_start": 205,
      "source_line_end": 209,
      "formal_status": "formalized",
      "registry_ids": [
        "V.C09"
      ]
    },
    {
      "kind": "structure",
      "name": "MacroReynoldsNumber",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reynolds-number/",
      "source_line_start": 220,
      "source_line_end": 229,
      "formal_status": "defined",
      "registry_ids": [
        "V.D98"
      ]
    },
    {
      "kind": "def",
      "name": "MacroReynoldsNumber.ratio",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/ratio/",
      "source_line_start": 232,
      "source_line_end": 233,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reynolds_bounded",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/reynolds-bounded/",
      "source_line_start": 236,
      "source_line_end": 240,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "enrichment_independent",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/enrichment-independent/",
      "source_line_start": 250,
      "source_line_end": 254,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R137"
      ]
    },
    {
      "kind": "def",
      "name": "convective_overshooting",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting/",
      "source_line_start": 263,
      "source_line_end": 265,
      "formal_status": "defined",
      "registry_ids": [
        "V.R141"
      ]
    },
    {
      "kind": "theorem",
      "name": "convective_overshooting_holds",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting-holds/",
      "source_line_start": 267,
      "source_line_end": 269,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "classical_ns_as_readout",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/classical-ns-as-readout/",
      "source_line_start": 282,
      "source_line_end": 284,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P43"
      ]
    },
    {
      "kind": "structure",
      "name": "DecompactificationBound",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompactification-bound/",
      "source_line_start": 298,
      "source_line_end": 311,
      "formal_status": "defined",
      "registry_ids": [
        "V.D314"
      ]
    },
    {
      "kind": "def",
      "name": "decompact_depth3",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth3/",
      "source_line_start": 314,
      "source_line_end": 320,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "decompact_depth5",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth5/",
      "source_line_start": 323,
      "source_line_end": 329,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AdmissibilityClass",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class/",
      "source_line_start": 340,
      "source_line_end": 349,
      "formal_status": "defined",
      "registry_ids": [
        "V.D315"
      ]
    },
    {
      "kind": "def",
      "name": "admissibility_class",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_convergence",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/primorial-convergence/",
      "source_line_start": 364,
      "source_line_end": 366,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T254"
      ]
    },
    {
      "kind": "theorem",
      "name": "depth5_near_leray",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/depth5-near-leray/",
      "source_line_start": 369,
      "source_line_end": 372,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "leray_limit_recovery",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/leray-limit-recovery/",
      "source_line_start": 382,
      "source_line_end": 384,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P174"
      ]
    },
    {
      "kind": "def",
      "name": "example_transport",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-transport/",
      "source_line_start": 421,
      "source_line_end": 426,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l428/",
      "source_line_start": 428,
      "source_line_end": 428,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l429/",
      "source_line_start": 429,
      "source_line_end": 429,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_reynolds",
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-reynolds/",
      "source_line_start": 432,
      "source_line_end": 436,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l438/",
      "source_line_start": 438,
      "source_line_end": 440,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [MacroDefectTransport](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-defect-transport/) | L68-L83 | defined | `V.D96` |
| `def` | [MacroDefectTransport.totalBudget](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/total-budget/) | L86-L87 | defined | — |
| `structure` | [MacroTauNSFlow](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-nsflow/) | L98-L107 | defined | `V.D97` |
| `structure` | [Tau3Compactness](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compactness/) | L120-L132 | defined | `V.P42` |
| `theorem` | [tau3_compact](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/tau3-compact/) | L135-L143 | formalized | — |
| `inductive` | [MacroRegCondition](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reg-condition/) | L150-L157 | defined | — |
| `structure` | [MacroThreeConditions](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-conditions/) | L162-L169 | defined | `V.T70` |
| `theorem` | [macro_three_condition_sufficiency](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-three-condition-sufficiency/) | L172-L177 | formalized | — |
| `theorem` | [macro_tau_ns_regularity](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-tau-ns-regularity/) | L189-L195 | formalized | `V.T71` |
| `theorem` | [no_temporal_blowup](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/no-temporal-blowup/) | L205-L209 | formalized | `V.C09` |
| `structure` | [MacroReynoldsNumber](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/macro-reynolds-number/) | L220-L229 | defined | `V.D98` |
| `def` | [MacroReynoldsNumber.ratio](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/ratio/) | L232-L233 | defined | — |
| `theorem` | [reynolds_bounded](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/reynolds-bounded/) | L236-L240 | formalized | — |
| `theorem` | [enrichment_independent](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/enrichment-independent/) | L250-L254 | formalized | `V.R137` |
| `def` | [convective_overshooting](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting/) | L263-L265 | defined | `V.R141` |
| `theorem` | [convective_overshooting_holds](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/convective-overshooting-holds/) | L267-L269 | formalized | — |
| `theorem` | [classical_ns_as_readout](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/classical-ns-as-readout/) | L282-L284 | formalized | `V.P43` |
| `structure` | [DecompactificationBound](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompactification-bound/) | L298-L311 | defined | `V.D314` |
| `def` | [decompact_depth3](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth3/) | L314-L320 | defined | — |
| `def` | [decompact_depth5](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/decompact-depth5/) | L323-L329 | defined | — |
| `structure` | [AdmissibilityClass](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class/) | L340-L349 | defined | `V.D315` |
| `def` | [admissibility_class](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class-l352/) | L352-L352 | defined | — |
| `theorem` | [primorial_convergence](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/primorial-convergence/) | L364-L366 | formalized | `V.T254` |
| `theorem` | [depth5_near_leray](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/depth5-near-leray/) | L369-L372 | formalized | — |
| `theorem` | [leray_limit_recovery](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/leray-limit-recovery/) | L382-L384 | formalized | `V.P174` |
| `def` | [example_transport](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-transport/) | L421-L426 | defined | — |
| `eval` | [#eval L428](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l428/) | L428-L428 | computed | — |
| `eval` | [#eval L429](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l429/) | L429-L429 | computed | — |
| `def` | [example_reynolds](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/example-reynolds/) | L432-L436 | defined | — |
| `eval` | [#eval L438](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/eval-l438/) | L438-L440 | computed | — |

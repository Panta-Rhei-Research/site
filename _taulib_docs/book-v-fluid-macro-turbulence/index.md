---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.Turbulence",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.FluidMacro.Turbulence`.",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_slug": "book-v-fluid-macro-turbulence",
  "book": "BookV",
  "family": "FluidMacro",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/FluidMacro/Turbulence.lean",
  "sha256": "d181fd77929452355641117e25ff12860749acd5aad569e8f120ebd79cabb7c8",
  "imports": [
    "TauLib.BookV.FluidMacro.NavierStokesMacro"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.FluidMacro.ChargeObstruction"
  ],
  "registry_ids": [
    "V.D100",
    "V.D308",
    "V.D309",
    "V.D310",
    "V.D99",
    "V.P170",
    "V.P171",
    "V.P44",
    "V.P45",
    "V.R145",
    "V.R146",
    "V.R147",
    "V.R439",
    "V.R440",
    "V.R441",
    "V.R442",
    "V.T248",
    "V.T249",
    "V.T250",
    "V.T251",
    "V.T72"
  ],
  "declaration_counts": {
    "structure": 11,
    "def": 12,
    "theorem": 9,
    "inductive": 1,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauTurbulentFlow",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/tau-turbulent-flow/",
      "source_line_start": 77,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D99"
      ]
    },
    {
      "kind": "def",
      "name": "TauTurbulentFlow.inertialWidth",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/inertial-width/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "KolmogorovExponent",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-exponent/",
      "source_line_start": 101,
      "source_line_end": 108,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "kolmogorov_53",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-53/",
      "source_line_start": 111,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "macro_energy_spectrum",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/macro-energy-spectrum/",
      "source_line_start": 120,
      "source_line_end": 122,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T72"
      ]
    },
    {
      "kind": "theorem",
      "name": "kolmogorov_exponent_check",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-exponent-check/",
      "source_line_start": 125,
      "source_line_end": 127,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "KolmogorovConstant",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant/",
      "source_line_start": 137,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R146"
      ]
    },
    {
      "kind": "def",
      "name": "kolmogorov_constant",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant-l145/",
      "source_line_start": 145,
      "source_line_end": 147,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauEnstrophy",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/tau-enstrophy/",
      "source_line_start": 157,
      "source_line_end": 162,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D100"
      ]
    },
    {
      "kind": "def",
      "name": "TauEnstrophy.fromTransport",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/from-transport/",
      "source_line_start": 165,
      "source_line_end": 167,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CascadeDirection",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/cascade-direction/",
      "source_line_start": 174,
      "source_line_end": 179,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DualCascade",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/dual-cascade/",
      "source_line_start": 185,
      "source_line_end": 192,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P44"
      ]
    },
    {
      "kind": "theorem",
      "name": "dual_cascade_decomposition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/dual-cascade-decomposition/",
      "source_line_start": 195,
      "source_line_end": 201,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BatchelorKraichnanSpectrum",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/batchelor-kraichnan-spectrum/",
      "source_line_start": 210,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R147"
      ]
    },
    {
      "kind": "def",
      "name": "batchelor_kraichnan",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/batchelor-kraichnan/",
      "source_line_start": 220,
      "source_line_end": 224,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "vortex_stretching_bound",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/vortex-stretching-bound/",
      "source_line_start": 235,
      "source_line_end": 237,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P45"
      ]
    },
    {
      "kind": "structure",
      "name": "FiberCodimension",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/fiber-codimension/",
      "source_line_start": 248,
      "source_line_end": 257,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D308"
      ]
    },
    {
      "kind": "def",
      "name": "fiber_codimension",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/fiber-codimension-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SheLevequeDecomposition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-decomposition/",
      "source_line_start": 276,
      "source_line_end": 299,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D309"
      ]
    },
    {
      "kind": "def",
      "name": "she_leveque_decomposition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-decomposition-l302/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "she_leveque_from_tau",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-from-tau/",
      "source_line_start": 317,
      "source_line_end": 322,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T248"
      ]
    },
    {
      "kind": "structure",
      "name": "SheLevequeAgreement",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-agreement/",
      "source_line_start": 339,
      "source_line_end": 352,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T249"
      ]
    },
    {
      "kind": "def",
      "name": "she_leveque_agreement",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-agreement-l355/",
      "source_line_start": 355,
      "source_line_end": 355,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "zeta_p_experimental_consistency",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/zeta-p-experimental-consistency/",
      "source_line_start": 366,
      "source_line_end": 367,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P170"
      ]
    },
    {
      "kind": "structure",
      "name": "KolmogorovDecomposition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-decomposition/",
      "source_line_start": 379,
      "source_line_end": 396,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D310"
      ]
    },
    {
      "kind": "def",
      "name": "kolmogorov_decomposition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-decomposition-l399/",
      "source_line_start": 399,
      "source_line_end": 399,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kolmogorov_53_from_tau",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-53-from-tau/",
      "source_line_start": 410,
      "source_line_end": 414,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T250"
      ]
    },
    {
      "kind": "structure",
      "name": "KolmogorovConstantDerived",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant-derived/",
      "source_line_start": 424,
      "source_line_end": 437,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T251"
      ]
    },
    {
      "kind": "def",
      "name": "ck_derived",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/ck-derived/",
      "source_line_start": 440,
      "source_line_end": 440,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ck_is_three_halves",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/ck-is-three-halves/",
      "source_line_start": 443,
      "source_line_end": 444,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ck_observational_match",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/ck-observational-match/",
      "source_line_start": 455,
      "source_line_end": 456,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P171"
      ]
    },
    {
      "kind": "def",
      "name": "example_turbulent",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/example-turbulent/",
      "source_line_start": 483,
      "source_line_end": 497,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/eval-l499/",
      "source_line_start": 499,
      "source_line_end": 499,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/eval-l500/",
      "source_line_start": 500,
      "source_line_end": 500,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_enstrophy",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/example-enstrophy/",
      "source_line_start": 503,
      "source_line_end": 503,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-turbulence/eval-l504/",
      "source_line_start": 504,
      "source_line_end": 506,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean",
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
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/FluidMacro/Turbulence.lean`
- SHA-256: `d181fd77929452355641117e25ff12860749acd5aad569e8f120ebd79cabb7c8`

## Registry Links

- `V.D100` — tau-enstrophy
- `V.D308` — Fiber Co-dimension of Dissipative Structures
- `V.D309` — She-Lévêque τ-Decomposition
- `V.D310` — Kolmogorov Exponent Decomposition
- `V.D99` — tau-turbulent flow
- `V.P170` — ζ_p Experimental Consistency
- `V.P171` — C_K Observational Match
- `V.P44` — Dual cascade decomposition
- `V.P45` — Vortex stretching bound
- `V.R145` — Limitations of K41
- `V.R146` — The Kolmogorov constant C_K
- `V.R147` — Batchelor--Kraichnan spectrum
- `V.R439` — Fitted→Derived
- `V.R440` — Fiber Filament Interpretation
- `V.R441` — Two-Thirds Law
- `V.R442` — 5=|gen|+dim(T²) Interpretation
- `V.T248` — She-Lévêque from τ³ Dimensions
- `V.T249` — Intermittency Exponent Agreement
- `V.T250` — -5/3 from τ Dimensions
- `V.T251` — C_K = 3/2
- `V.T72` — Macro energy spectrum

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.FluidMacro.NavierStokesMacro`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.FluidMacro.ChargeObstruction`

## Declaration Counts

- `def`: 12
- `eval`: 3
- `inductive`: 1
- `structure`: 11
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauTurbulentFlow](/corpus/taulib/docs/book-v-fluid-macro-turbulence/tau-turbulent-flow/) | L77-L90 | type/data schema | type/data schema | `V.D99` |
| `def` | [TauTurbulentFlow.inertialWidth](/corpus/taulib/docs/book-v-fluid-macro-turbulence/inertial-width/) | L93-L94 | data/computed value | data/computed value | — |
| `structure` | [KolmogorovExponent](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-exponent/) | L101-L108 | type/data schema | type/data schema | — |
| `def` | [kolmogorov_53](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-53/) | L111-L114 | definition | definition | — |
| `theorem` | [macro_energy_spectrum](/corpus/taulib/docs/book-v-fluid-macro-turbulence/macro-energy-spectrum/) | L120-L122 | proof obligation | formal proof obligation checked | `V.T72` |
| `theorem` | [kolmogorov_exponent_check](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-exponent-check/) | L125-L127 | proof obligation | formal proof obligation checked | — |
| `structure` | [KolmogorovConstant](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant/) | L137-L142 | type/data schema | type/data schema | `V.R146` |
| `def` | [kolmogorov_constant](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant-l145/) | L145-L147 | definition | definition | — |
| `structure` | [TauEnstrophy](/corpus/taulib/docs/book-v-fluid-macro-turbulence/tau-enstrophy/) | L157-L162 | type/data schema | type/data schema | `V.D100` |
| `def` | [TauEnstrophy.fromTransport](/corpus/taulib/docs/book-v-fluid-macro-turbulence/from-transport/) | L165-L167 | definition | definition | — |
| `inductive` | [CascadeDirection](/corpus/taulib/docs/book-v-fluid-macro-turbulence/cascade-direction/) | L174-L179 | type/data schema | type/data schema | — |
| `structure` | [DualCascade](/corpus/taulib/docs/book-v-fluid-macro-turbulence/dual-cascade/) | L185-L192 | type/data schema | type/data schema | `V.P44` |
| `theorem` | [dual_cascade_decomposition](/corpus/taulib/docs/book-v-fluid-macro-turbulence/dual-cascade-decomposition/) | L195-L201 | proof obligation | formal proof obligation checked | — |
| `structure` | [BatchelorKraichnanSpectrum](/corpus/taulib/docs/book-v-fluid-macro-turbulence/batchelor-kraichnan-spectrum/) | L210-L217 | type/data schema | type/data schema | `V.R147` |
| `def` | [batchelor_kraichnan](/corpus/taulib/docs/book-v-fluid-macro-turbulence/batchelor-kraichnan/) | L220-L224 | definition | definition | — |
| `theorem` | [vortex_stretching_bound](/corpus/taulib/docs/book-v-fluid-macro-turbulence/vortex-stretching-bound/) | L235-L237 | proof obligation | formal proof obligation checked | `V.P45` |
| `structure` | [FiberCodimension](/corpus/taulib/docs/book-v-fluid-macro-turbulence/fiber-codimension/) | L248-L257 | type/data schema | type/data schema | `V.D308` |
| `def` | [fiber_codimension](/corpus/taulib/docs/book-v-fluid-macro-turbulence/fiber-codimension-l260/) | L260-L260 | definition | definition | — |
| `structure` | [SheLevequeDecomposition](/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-decomposition/) | L276-L299 | type/data schema | type/data schema | `V.D309` |
| `def` | [she_leveque_decomposition](/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-decomposition-l302/) | L302-L302 | definition | definition | — |
| `theorem` | [she_leveque_from_tau](/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-from-tau/) | L317-L322 | proof obligation | formal proof obligation checked | `V.T248` |
| `structure` | [SheLevequeAgreement](/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-agreement/) | L339-L352 | type/data schema | type/data schema | `V.T249` |
| `def` | [she_leveque_agreement](/corpus/taulib/docs/book-v-fluid-macro-turbulence/she-leveque-agreement-l355/) | L355-L355 | definition | definition | — |
| `theorem` | [zeta_p_experimental_consistency](/corpus/taulib/docs/book-v-fluid-macro-turbulence/zeta-p-experimental-consistency/) | L366-L367 | proof obligation | formal proof obligation checked | `V.P170` |
| `structure` | [KolmogorovDecomposition](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-decomposition/) | L379-L396 | type/data schema | type/data schema | `V.D310` |
| `def` | [kolmogorov_decomposition](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-decomposition-l399/) | L399-L399 | definition | definition | — |
| `theorem` | [kolmogorov_53_from_tau](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-53-from-tau/) | L410-L414 | proof obligation | formal proof obligation checked | `V.T250` |
| `structure` | [KolmogorovConstantDerived](/corpus/taulib/docs/book-v-fluid-macro-turbulence/kolmogorov-constant-derived/) | L424-L437 | type/data schema | type/data schema | `V.T251` |
| `def` | [ck_derived](/corpus/taulib/docs/book-v-fluid-macro-turbulence/ck-derived/) | L440-L440 | definition | definition | — |
| `theorem` | [ck_is_three_halves](/corpus/taulib/docs/book-v-fluid-macro-turbulence/ck-is-three-halves/) | L443-L444 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ck_observational_match](/corpus/taulib/docs/book-v-fluid-macro-turbulence/ck-observational-match/) | L455-L456 | proof obligation | formal proof obligation checked | `V.P171` |
| `def` | [example_turbulent](/corpus/taulib/docs/book-v-fluid-macro-turbulence/example-turbulent/) | L483-L497 | definition | definition | — |
| `eval` | [#eval L499](/corpus/taulib/docs/book-v-fluid-macro-turbulence/eval-l499/) | L499-L499 | computed check | computed check | — |
| `eval` | [#eval L500](/corpus/taulib/docs/book-v-fluid-macro-turbulence/eval-l500/) | L500-L500 | computed check | computed check | — |
| `def` | [example_enstrophy](/corpus/taulib/docs/book-v-fluid-macro-turbulence/example-enstrophy/) | L503-L503 | definition | definition | — |
| `eval` | [#eval L504](/corpus/taulib/docs/book-v-fluid-macro-turbulence/eval-l504/) | L504-L506 | computed check | computed check | — |

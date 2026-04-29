---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.ManyBody.FluidRegimes",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_slug": "book-iv-many-body-fluid-regimes",
  "book": "BookIV",
  "family": "ManyBody",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/ManyBody/FluidRegimes.lean",
  "sha256": "66666d599a7662401939d71bab4eeaae0aafac2a0e7f209a7c77bde2343bf57c",
  "imports": [
    "TauLib.BookIV.ManyBody.DefectFunctionalExt2"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.ManyBody.CondensedMatter",
    "TauLib.BookIV.ManyBody.Magnetism",
    "TauLib.BookIV.ManyBody.NFLBoundary"
  ],
  "registry_ids": [
    "IV.D231",
    "IV.D232",
    "IV.D233",
    "IV.D234",
    "IV.D235",
    "IV.D236",
    "IV.D237",
    "IV.D238",
    "IV.D239",
    "IV.P140",
    "IV.P141",
    "IV.P142",
    "IV.R170",
    "IV.R171",
    "IV.R172",
    "IV.R173",
    "IV.R174",
    "IV.R175",
    "IV.R176",
    "IV.R177",
    "IV.T93"
  ],
  "declaration_counts": {
    "structure": 14,
    "def": 15,
    "theorem": 6,
    "inductive": 1,
    "eval": 16
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauEulerFlow",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-euler-flow/",
      "source_line_start": 64,
      "source_line_end": 77,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D231"
      ]
    },
    {
      "kind": "def",
      "name": "remark_kelvin_budget",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/remark-kelvin-budget/",
      "source_line_start": 82,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R170"
      ]
    },
    {
      "kind": "structure",
      "name": "TauNSFlow",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-nsflow/",
      "source_line_start": 95,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D232"
      ]
    },
    {
      "kind": "structure",
      "name": "FiniteAtEveryLevel",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/finite-at-every-level/",
      "source_line_start": 116,
      "source_line_end": 127,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P140"
      ]
    },
    {
      "kind": "def",
      "name": "finite_every_level",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/finite-every-level/",
      "source_line_start": 129,
      "source_line_end": 130,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "finiteness_unconditional",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/finiteness-unconditional/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauNSRegularity",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-nsregularity/",
      "source_line_start": 150,
      "source_line_end": 159,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T93"
      ]
    },
    {
      "kind": "def",
      "name": "tau_ns_regularity",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-ns-regularity/",
      "source_line_start": 161,
      "source_line_end": 161,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SuperfluidRegimeCh53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/superfluid-regime-ch53/",
      "source_line_start": 176,
      "source_line_end": 189,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D233"
      ]
    },
    {
      "kind": "def",
      "name": "superfluid_ch53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/superfluid-ch53/",
      "source_line_start": 191,
      "source_line_end": 192,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QuantizedCirculationProp",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/quantized-circulation-prop/",
      "source_line_start": 201,
      "source_line_end": 210,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P141"
      ]
    },
    {
      "kind": "def",
      "name": "quantized_circulation",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/quantized-circulation/",
      "source_line_start": 212,
      "source_line_end": 213,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SuperconductorRegimeCh53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/superconductor-regime-ch53/",
      "source_line_start": 222,
      "source_line_end": 231,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D234"
      ]
    },
    {
      "kind": "def",
      "name": "superconductor_ch53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/superconductor-ch53/",
      "source_line_start": 233,
      "source_line_end": 233,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CrystalRegimeCh53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/crystal-regime-ch53/",
      "source_line_start": 245,
      "source_line_end": 254,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D235"
      ]
    },
    {
      "kind": "def",
      "name": "crystal_ch53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/crystal-ch53/",
      "source_line_start": 256,
      "source_line_end": 257,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_crystal_symmetry",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/remark-crystal-symmetry/",
      "source_line_start": 261,
      "source_line_end": 262,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R174"
      ]
    },
    {
      "kind": "structure",
      "name": "GlassRegimeCh53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/glass-regime-ch53/",
      "source_line_start": 267,
      "source_line_end": 278,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D236"
      ]
    },
    {
      "kind": "def",
      "name": "glass_ch53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/glass-ch53/",
      "source_line_start": 280,
      "source_line_end": 281,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QuasicrystalRegime",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/quasicrystal-regime/",
      "source_line_start": 294,
      "source_line_end": 305,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D237"
      ]
    },
    {
      "kind": "def",
      "name": "quasicrystal_regime",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/quasicrystal-regime-l307/",
      "source_line_start": 307,
      "source_line_end": 308,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_penrose",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/remark-penrose/",
      "source_line_start": 313,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R176"
      ]
    },
    {
      "kind": "structure",
      "name": "FirstOrderCh53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/first-order-ch53/",
      "source_line_start": 325,
      "source_line_end": 334,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D238"
      ]
    },
    {
      "kind": "def",
      "name": "first_order_ch53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/first-order-ch53-l336/",
      "source_line_start": 336,
      "source_line_end": 337,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SecondOrderCh53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/second-order-ch53/",
      "source_line_start": 343,
      "source_line_end": 352,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D239"
      ]
    },
    {
      "kind": "def",
      "name": "second_order_ch53",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/second-order-ch53-l354/",
      "source_line_start": 354,
      "source_line_end": 355,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "UniversalOrderParameter",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/universal-order-parameter/",
      "source_line_start": 368,
      "source_line_end": 379,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P142"
      ]
    },
    {
      "kind": "def",
      "name": "universal_order_parameter",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/universal-order-parameter-l381/",
      "source_line_start": 381,
      "source_line_end": 382,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "order_param_unifies_three",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/order-param-unifies-three/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "order_param_four_components",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/order-param-four-components/",
      "source_line_start": 387,
      "source_line_end": 388,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ExtendedRegime",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/extended-regime/",
      "source_line_start": 398,
      "source_line_end": 408,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nine_extended_regimes",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/nine-extended-regimes/",
      "source_line_start": 411,
      "source_line_end": 415,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l421/",
      "source_line_start": 421,
      "source_line_end": 421,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l422/",
      "source_line_start": 422,
      "source_line_end": 422,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l423/",
      "source_line_start": 423,
      "source_line_end": 423,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l424/",
      "source_line_start": 424,
      "source_line_end": 424,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l425/",
      "source_line_start": 425,
      "source_line_end": 425,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l426/",
      "source_line_start": 426,
      "source_line_end": 426,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l427/",
      "source_line_start": 427,
      "source_line_end": 427,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l428/",
      "source_line_start": 428,
      "source_line_end": 428,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l429/",
      "source_line_start": 429,
      "source_line_end": 429,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l430/",
      "source_line_start": 430,
      "source_line_end": 430,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l431/",
      "source_line_start": 431,
      "source_line_end": 431,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l432/",
      "source_line_start": 432,
      "source_line_end": 432,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l433/",
      "source_line_start": 433,
      "source_line_end": 433,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l434/",
      "source_line_start": 434,
      "source_line_end": 434,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DefectContractivity",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/defect-contractivity/",
      "source_line_start": 455,
      "source_line_end": 470,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "defect_contractivity",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/defect-contractivity-l472/",
      "source_line_start": 472,
      "source_line_end": 474,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c3_defect_contractivity",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/c3-defect-contractivity/",
      "source_line_start": 477,
      "source_line_end": 481,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "regularity_t2_scope",
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/regularity-t2-scope/",
      "source_line_start": 486,
      "source_line_end": 489,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l492/",
      "source_line_start": 492,
      "source_line_end": 492,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l493/",
      "source_line_start": 493,
      "source_line_end": 495,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/ManyBody/FluidRegimes.lean`
- SHA-256: `66666d599a7662401939d71bab4eeaae0aafac2a0e7f209a7c77bde2343bf57c`

## Registry Links

- `IV.D231` — tau-Euler flow
- `IV.D232` — tau-Navier-Stokes flow
- `IV.D233` — Superfluid regime
- `IV.D234` — Superconductor regime
- `IV.D235` — Crystal regime
- `IV.D236` — Glass regime
- `IV.D237` — Quasicrystal regime
- `IV.D238` — First-order phase transition
- `IV.D239` — Second-order phase transition
- `IV.P140` — Finite at every primorial level
- `IV.P141` — Quantized circulation
- `IV.P142` — Defect tuple as universal order parameter
- `IV.R170` — Kelvin theorem as budget law
- `IV.R171` — Viscosity coefficient eta_tau
- `IV.R172` — Honesty about the Clay problem
- `IV.R173` — BCS gap as spectral gap
- `IV.R174` — Crystal symmetry from torus subgroups
- `IV.R175` — Glass transition not a true phase transition
- `IV.R176` — Penrose tilings on the torus
- `IV.R177` — Universality from sector structure
- `IV.T93` — τ-NS Regularity on T² Fiber (C3 Defect Contractivity)

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.ManyBody.DefectFunctionalExt2`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.ManyBody.CondensedMatter`
- `TauLib.BookIV.ManyBody.Magnetism`
- `TauLib.BookIV.ManyBody.NFLBoundary`

## Declaration Counts

- `def`: 15
- `eval`: 16
- `inductive`: 1
- `structure`: 14
- `theorem`: 6

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [TauEulerFlow](/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-euler-flow/) | L64-L77 | defined | `IV.D231` |
| `def` | [remark_kelvin_budget](/verify/taulib/docs/book-iv-many-body-fluid-regimes/remark-kelvin-budget/) | L82-L83 | defined | `IV.R170` |
| `structure` | [TauNSFlow](/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-nsflow/) | L95-L106 | defined | `IV.D232` |
| `structure` | [FiniteAtEveryLevel](/verify/taulib/docs/book-iv-many-body-fluid-regimes/finite-at-every-level/) | L116-L127 | defined | `IV.P140` |
| `def` | [finite_every_level](/verify/taulib/docs/book-iv-many-body-fluid-regimes/finite-every-level/) | L129-L130 | defined | — |
| `theorem` | [finiteness_unconditional](/verify/taulib/docs/book-iv-many-body-fluid-regimes/finiteness-unconditional/) | L132-L133 | formalized | — |
| `structure` | [TauNSRegularity](/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-nsregularity/) | L150-L159 | defined | `IV.T93` |
| `def` | [tau_ns_regularity](/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-ns-regularity/) | L161-L161 | defined | — |
| `structure` | [SuperfluidRegimeCh53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/superfluid-regime-ch53/) | L176-L189 | defined | `IV.D233` |
| `def` | [superfluid_ch53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/superfluid-ch53/) | L191-L192 | defined | — |
| `structure` | [QuantizedCirculationProp](/verify/taulib/docs/book-iv-many-body-fluid-regimes/quantized-circulation-prop/) | L201-L210 | defined | `IV.P141` |
| `def` | [quantized_circulation](/verify/taulib/docs/book-iv-many-body-fluid-regimes/quantized-circulation/) | L212-L213 | defined | — |
| `structure` | [SuperconductorRegimeCh53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/superconductor-regime-ch53/) | L222-L231 | defined | `IV.D234` |
| `def` | [superconductor_ch53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/superconductor-ch53/) | L233-L233 | defined | — |
| `structure` | [CrystalRegimeCh53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/crystal-regime-ch53/) | L245-L254 | defined | `IV.D235` |
| `def` | [crystal_ch53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/crystal-ch53/) | L256-L257 | defined | — |
| `def` | [remark_crystal_symmetry](/verify/taulib/docs/book-iv-many-body-fluid-regimes/remark-crystal-symmetry/) | L261-L262 | defined | `IV.R174` |
| `structure` | [GlassRegimeCh53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/glass-regime-ch53/) | L267-L278 | defined | `IV.D236` |
| `def` | [glass_ch53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/glass-ch53/) | L280-L281 | defined | — |
| `structure` | [QuasicrystalRegime](/verify/taulib/docs/book-iv-many-body-fluid-regimes/quasicrystal-regime/) | L294-L305 | defined | `IV.D237` |
| `def` | [quasicrystal_regime](/verify/taulib/docs/book-iv-many-body-fluid-regimes/quasicrystal-regime-l307/) | L307-L308 | defined | — |
| `def` | [remark_penrose](/verify/taulib/docs/book-iv-many-body-fluid-regimes/remark-penrose/) | L313-L315 | defined | `IV.R176` |
| `structure` | [FirstOrderCh53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/first-order-ch53/) | L325-L334 | defined | `IV.D238` |
| `def` | [first_order_ch53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/first-order-ch53-l336/) | L336-L337 | defined | — |
| `structure` | [SecondOrderCh53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/second-order-ch53/) | L343-L352 | defined | `IV.D239` |
| `def` | [second_order_ch53](/verify/taulib/docs/book-iv-many-body-fluid-regimes/second-order-ch53-l354/) | L354-L355 | defined | — |
| `structure` | [UniversalOrderParameter](/verify/taulib/docs/book-iv-many-body-fluid-regimes/universal-order-parameter/) | L368-L379 | defined | `IV.P142` |
| `def` | [universal_order_parameter](/verify/taulib/docs/book-iv-many-body-fluid-regimes/universal-order-parameter-l381/) | L381-L382 | defined | — |
| `theorem` | [order_param_unifies_three](/verify/taulib/docs/book-iv-many-body-fluid-regimes/order-param-unifies-three/) | L384-L385 | formalized | — |
| `theorem` | [order_param_four_components](/verify/taulib/docs/book-iv-many-body-fluid-regimes/order-param-four-components/) | L387-L388 | formalized | — |
| `inductive` | [ExtendedRegime](/verify/taulib/docs/book-iv-many-body-fluid-regimes/extended-regime/) | L398-L408 | defined | — |
| `theorem` | [nine_extended_regimes](/verify/taulib/docs/book-iv-many-body-fluid-regimes/nine-extended-regimes/) | L411-L415 | formalized | — |
| `eval` | [#eval L421](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l421/) | L421-L421 | computed | — |
| `eval` | [#eval L422](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l422/) | L422-L422 | computed | — |
| `eval` | [#eval L423](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l423/) | L423-L423 | computed | — |
| `eval` | [#eval L424](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l424/) | L424-L424 | computed | — |
| `eval` | [#eval L425](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l425/) | L425-L425 | computed | — |
| `eval` | [#eval L426](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l426/) | L426-L426 | computed | — |
| `eval` | [#eval L427](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l427/) | L427-L427 | computed | — |
| `eval` | [#eval L428](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l428/) | L428-L428 | computed | — |
| `eval` | [#eval L429](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l429/) | L429-L429 | computed | — |
| `eval` | [#eval L430](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l430/) | L430-L430 | computed | — |
| `eval` | [#eval L431](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l431/) | L431-L431 | computed | — |
| `eval` | [#eval L432](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l432/) | L432-L432 | computed | — |
| `eval` | [#eval L433](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l433/) | L433-L433 | computed | — |
| `eval` | [#eval L434](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l434/) | L434-L434 | computed | — |
| `structure` | [DefectContractivity](/verify/taulib/docs/book-iv-many-body-fluid-regimes/defect-contractivity/) | L455-L470 | defined | — |
| `def` | [defect_contractivity](/verify/taulib/docs/book-iv-many-body-fluid-regimes/defect-contractivity-l472/) | L472-L474 | defined | — |
| `theorem` | [c3_defect_contractivity](/verify/taulib/docs/book-iv-many-body-fluid-regimes/c3-defect-contractivity/) | L477-L481 | formalized | — |
| `theorem` | [regularity_t2_scope](/verify/taulib/docs/book-iv-many-body-fluid-regimes/regularity-t2-scope/) | L486-L489 | formalized | — |
| `eval` | [#eval L492](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l492/) | L492-L492 | computed | — |
| `eval` | [#eval L493](/verify/taulib/docs/book-iv-many-body-fluid-regimes/eval-l493/) | L493-L495 | computed | — |

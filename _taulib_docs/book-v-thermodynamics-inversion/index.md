---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Thermodynamics.Inversion",
  "permalink": "/corpus/taulib/docs/book-v-thermodynamics-inversion/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Thermodynamics.Inversion`.",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_slug": "book-v-thermodynamics-inversion",
  "book": "BookV",
  "family": "Thermodynamics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Thermodynamics/Inversion.lean",
  "sha256": "7e99d0ee1537c1e422b022b3d323d3c60b5104d07bd5e3c3bd9d2cb5b53602b9",
  "imports": [
    "TauLib.BookV.GravityField.ClosingIdentity"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Thermodynamics.EntropySplitting"
  ],
  "registry_ids": [
    "V.C05",
    "V.D83",
    "V.D84",
    "V.L02",
    "V.P24",
    "V.P25",
    "V.P26",
    "V.R111",
    "V.R112",
    "V.R113",
    "V.R114",
    "V.R115",
    "V.R116",
    "V.R117",
    "V.R118",
    "V.T55"
  ],
  "declaration_counts": {
    "def": 4,
    "theorem": 8,
    "structure": 7,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "def",
      "name": "contraction_numer",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-numer/",
      "source_line_start": 64,
      "source_line_end": 64,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "contraction_denom",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-denom/",
      "source_line_start": 67,
      "source_line_end": 67,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "contraction_pos",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-pos/",
      "source_line_start": 70,
      "source_line_end": 71,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "contraction_lt_one",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-lt-one/",
      "source_line_start": 74,
      "source_line_end": 75,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CategoricalSecondLaw",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/categorical-second-law/",
      "source_line_start": 89,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T55"
      ]
    },
    {
      "kind": "def",
      "name": "categorical_second_law",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/categorical-second-law-l103/",
      "source_line_start": 103,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CategoricalEquilibrium",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/categorical-equilibrium/",
      "source_line_start": 119,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D83"
      ]
    },
    {
      "kind": "structure",
      "name": "DefectAbsorptionRate",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/defect-absorption-rate/",
      "source_line_start": 140,
      "source_line_end": 149,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P24"
      ]
    },
    {
      "kind": "structure",
      "name": "WeakRedistribution",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/weak-redistribution/",
      "source_line_start": 161,
      "source_line_end": 168,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P25"
      ]
    },
    {
      "kind": "theorem",
      "name": "weak_preserves",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/weak-preserves/",
      "source_line_start": 171,
      "source_line_end": 172,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GeometricContraction",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/geometric-contraction/",
      "source_line_start": 186,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.L02"
      ]
    },
    {
      "kind": "theorem",
      "name": "geometric_series_bound",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/geometric-series-bound/",
      "source_line_start": 201,
      "source_line_end": 204,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "defect_support_exhaustion",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/defect-support-exhaustion/",
      "source_line_start": 216,
      "source_line_end": 217,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.C05"
      ]
    },
    {
      "kind": "structure",
      "name": "ThermalCoherenceHorizon",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/thermal-coherence-horizon/",
      "source_line_start": 229,
      "source_line_end": 236,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D84"
      ]
    },
    {
      "kind": "def",
      "name": "coherence_horizon_bound",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/coherence-horizon-bound/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "inversion_180",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/inversion-180/",
      "source_line_start": 255,
      "source_line_end": 257,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P26"
      ]
    },
    {
      "kind": "structure",
      "name": "OrbitStepsVsTime",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/orbit-steps-vs-time/",
      "source_line_start": 269,
      "source_line_end": 274,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R118"
      ]
    },
    {
      "kind": "theorem",
      "name": "pixel_analogy",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/pixel-analogy/",
      "source_line_start": 287,
      "source_line_end": 289,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R111",
        "V.R112"
      ]
    },
    {
      "kind": "theorem",
      "name": "contraction_is_kappa_D",
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-is-kappa-d/",
      "source_line_start": 301,
      "source_line_end": 302,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R113",
        "V.R114",
        "V.R115",
        "V.R116"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l311/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R117"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l312/",
      "source_line_start": 312,
      "source_line_end": 312,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l313/",
      "source_line_start": 313,
      "source_line_end": 313,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 320,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean",
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
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Thermodynamics/Inversion.lean`
- SHA-256: `7e99d0ee1537c1e422b022b3d323d3c60b5104d07bd5e3c3bd9d2cb5b53602b9`

## Registry Links

- `V.C05` — Defect support exhaustion
- `V.D83` — Thermodynamic equilibrium---categorical
- `V.D84` — Coherence horizon
- `V.L02` — Geometric contraction of defect support
- `V.P24` — Defect absorption rate
- `V.P25` — Weak redistribution preserves defect count
- `V.P26` — The 180^circ inversion
- `V.R111` — The explanatory gap
- `V.R112` — An analogy: pixels and noise
- `V.R113` — Compatibility with Book~IV
- `V.R114` — Not the same as thermal equilibrium
- `V.R115` — The role of gravity in ordering
- `V.R116` — The contraction rate is the gravitational coupling
- `V.R117` — Circulation, not stasis
- `V.R118` — Orbit steps versus physical time
- `V.T55` — The Categorical Second Law

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.ClosingIdentity`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Thermodynamics.EntropySplitting`

## Declaration Counts

- `def`: 4
- `eval`: 6
- `structure`: 7
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [contraction_numer](/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-numer/) | L64-L64 | data/computed value | data/computed value | — |
| `def` | [contraction_denom](/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-denom/) | L67-L67 | data/computed value | data/computed value | — |
| `theorem` | [contraction_pos](/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-pos/) | L70-L71 | proof obligation | formal proof obligation checked | — |
| `theorem` | [contraction_lt_one](/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-lt-one/) | L74-L75 | proof obligation | formal proof obligation checked | — |
| `structure` | [CategoricalSecondLaw](/corpus/taulib/docs/book-v-thermodynamics-inversion/categorical-second-law/) | L89-L100 | type/data schema | type/data schema | `V.T55` |
| `def` | [categorical_second_law](/corpus/taulib/docs/book-v-thermodynamics-inversion/categorical-second-law-l103/) | L103-L107 | definition | definition | — |
| `structure` | [CategoricalEquilibrium](/corpus/taulib/docs/book-v-thermodynamics-inversion/categorical-equilibrium/) | L119-L126 | type/data schema | type/data schema | `V.D83` |
| `structure` | [DefectAbsorptionRate](/corpus/taulib/docs/book-v-thermodynamics-inversion/defect-absorption-rate/) | L140-L149 | type/data schema | type/data schema | `V.P24` |
| `structure` | [WeakRedistribution](/corpus/taulib/docs/book-v-thermodynamics-inversion/weak-redistribution/) | L161-L168 | type/data schema | type/data schema | `V.P25` |
| `theorem` | [weak_preserves](/corpus/taulib/docs/book-v-thermodynamics-inversion/weak-preserves/) | L171-L172 | proof obligation | formal proof obligation checked | — |
| `structure` | [GeometricContraction](/corpus/taulib/docs/book-v-thermodynamics-inversion/geometric-contraction/) | L186-L197 | type/data schema | type/data schema | `V.L02` |
| `theorem` | [geometric_series_bound](/corpus/taulib/docs/book-v-thermodynamics-inversion/geometric-series-bound/) | L201-L204 | proof obligation | formal proof obligation checked | — |
| `theorem` | [defect_support_exhaustion](/corpus/taulib/docs/book-v-thermodynamics-inversion/defect-support-exhaustion/) | L216-L217 | proof obligation | formal proof obligation checked | `V.C05` |
| `structure` | [ThermalCoherenceHorizon](/corpus/taulib/docs/book-v-thermodynamics-inversion/thermal-coherence-horizon/) | L229-L236 | type/data schema | type/data schema | `V.D84` |
| `def` | [coherence_horizon_bound](/corpus/taulib/docs/book-v-thermodynamics-inversion/coherence-horizon-bound/) | L241-L241 | data/computed value | data/computed value | — |
| `theorem` | [inversion_180](/corpus/taulib/docs/book-v-thermodynamics-inversion/inversion-180/) | L255-L257 | proof obligation | formal proof obligation checked | `V.P26` |
| `structure` | [OrbitStepsVsTime](/corpus/taulib/docs/book-v-thermodynamics-inversion/orbit-steps-vs-time/) | L269-L274 | type/data schema | type/data schema | `V.R118` |
| `theorem` | [pixel_analogy](/corpus/taulib/docs/book-v-thermodynamics-inversion/pixel-analogy/) | L287-L289 | proof obligation | formal proof obligation checked | `V.R111`, `V.R112` |
| `theorem` | [contraction_is_kappa_D](/corpus/taulib/docs/book-v-thermodynamics-inversion/contraction-is-kappa-d/) | L301-L302 | proof obligation | formal proof obligation checked | `V.R113`, `V.R114`, `V.R115`, `V.R116` |
| `eval` | [#eval L311](/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l311/) | L311-L311 | computed check | computed check | `V.R117` |
| `eval` | [#eval L312](/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l312/) | L312-L312 | computed check | computed check | — |
| `eval` | [#eval L313](/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l313/) | L313-L313 | computed check | computed check | — |
| `eval` | [#eval L315](/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l315/) | L315-L315 | computed check | computed check | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l316/) | L316-L316 | computed check | computed check | — |
| `eval` | [#eval L318](/corpus/taulib/docs/book-v-thermodynamics-inversion/eval-l318/) | L318-L320 | computed check | computed check | — |

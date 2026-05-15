---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_slug": "book-v-gravity-field-tovphase-boundary",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/TOVPhaseBoundary.lean",
  "sha256": "58f7df36cd13c1956acb4f5091923f76e99f03f92623af474474b2f60a845369",
  "imports": [
    "TauLib.BookV.GravityField.TOVStarBuilder"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.CalibrationTriangle"
  ],
  "registry_ids": [
    "V.C04",
    "V.D75",
    "V.D76",
    "V.D77",
    "V.L01",
    "V.R94",
    "V.R95",
    "V.R96",
    "V.R98",
    "V.R99",
    "V.T45",
    "V.T46",
    "V.T47",
    "V.T48"
  ],
  "declaration_counts": {
    "structure": 5,
    "def": 7,
    "theorem": 4,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PhaseTension",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/phase-tension/",
      "source_line_start": 66,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D75"
      ]
    },
    {
      "kind": "def",
      "name": "PhaseTension.s2Float",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/s2-float/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "PhaseTension.t2Float",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/t2-float/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoherenceHorizon",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon/",
      "source_line_start": 103,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D76"
      ]
    },
    {
      "kind": "def",
      "name": "CoherenceHorizon.massFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/mass-float/",
      "source_line_start": 117,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TopologyCrossing",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/topology-crossing/",
      "source_line_start": 130,
      "source_line_end": 137,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D77"
      ]
    },
    {
      "kind": "structure",
      "name": "CoherenceHorizonAxiom",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon-axiom/",
      "source_line_start": 149,
      "source_line_end": 156,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.C04"
      ]
    },
    {
      "kind": "def",
      "name": "coherence_horizon_axiom",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon-axiom-l159/",
      "source_line_start": 159,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SurfaceBoundaryCondition",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/surface-boundary-condition/",
      "source_line_start": 175,
      "source_line_end": 184,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.L01"
      ]
    },
    {
      "kind": "def",
      "name": "surface_boundary_condition",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/surface-boundary-condition-l187/",
      "source_line_start": 187,
      "source_line_end": 188,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tension_monotone",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/tension-monotone/",
      "source_line_start": 198,
      "source_line_end": 200,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T45"
      ]
    },
    {
      "kind": "theorem",
      "name": "threshold_exists",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/threshold-exists/",
      "source_line_start": 204,
      "source_line_end": 205,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T46"
      ]
    },
    {
      "kind": "theorem",
      "name": "torus_above_threshold",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/torus-above-threshold/",
      "source_line_start": 211,
      "source_line_end": 213,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T47"
      ]
    },
    {
      "kind": "theorem",
      "name": "defect_cost_equality",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/defect-cost-equality/",
      "source_line_start": 219,
      "source_line_end": 221,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T48"
      ]
    },
    {
      "kind": "def",
      "name": "example_coherence_horizon",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/example-coherence-horizon/",
      "source_line_start": 245,
      "source_line_end": 249,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l251/",
      "source_line_start": 251,
      "source_line_end": 251,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l252/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_crossing",
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/example-crossing/",
      "source_line_start": 255,
      "source_line_end": 256,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l258/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l259/",
      "source_line_start": 259,
      "source_line_end": 261,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean",
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
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/TOVPhaseBoundary.lean`
- SHA-256: `58f7df36cd13c1956acb4f5091923f76e99f03f92623af474474b2f60a845369`

## Registry Links

- `V.C04` — TOV Limit
- `V.D75` — GR Tension Functional
- `V.D76` — Coherence Horizon
- `V.D77` — Topology Crossing Event
- `V.L01` — Surface Matter Bound
- `V.R94` — No ``tension maximum''
- `V.R95` — Chandrasekhar limit as the electron-degenerate case
- `V.R96` — No singularity
- `V.R98` — Defect minimization drives topology selection
- `V.R99` — Observational tests
- `V.T45` — Tension Monotonicity
- `V.T46` — Structural Threshold --- Forced Topology Relaxation
- `V.T47` — Topology Crossing Admissibility
- `V.T48` — Defect Cost Jump at Phase Boundary

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.TOVStarBuilder`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.CalibrationTriangle`

## Declaration Counts

- `def`: 7
- `eval`: 4
- `structure`: 5
- `theorem`: 4

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [PhaseTension](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/phase-tension/) | L66-L81 | type/data schema | type/data schema | `V.D75` |
| `def` | [PhaseTension.s2Float](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/s2-float/) | L84-L85 | data/computed value | data/computed value | — |
| `def` | [PhaseTension.t2Float](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/t2-float/) | L88-L89 | data/computed value | data/computed value | — |
| `structure` | [CoherenceHorizon](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon/) | L103-L114 | type/data schema | type/data schema | `V.D76` |
| `def` | [CoherenceHorizon.massFloat](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/mass-float/) | L117-L118 | data/computed value | data/computed value | — |
| `structure` | [TopologyCrossing](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/topology-crossing/) | L130-L137 | type/data schema | type/data schema | `V.D77` |
| `structure` | [CoherenceHorizonAxiom](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon-axiom/) | L149-L156 | type/data schema | type/data schema | `V.C04` |
| `def` | [coherence_horizon_axiom](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon-axiom-l159/) | L159-L160 | definition | definition | — |
| `structure` | [SurfaceBoundaryCondition](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/surface-boundary-condition/) | L175-L184 | type/data schema | type/data schema | `V.L01` |
| `def` | [surface_boundary_condition](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/surface-boundary-condition-l187/) | L187-L188 | definition | definition | — |
| `theorem` | [tension_monotone](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/tension-monotone/) | L198-L200 | proof obligation | formal proof obligation checked | `V.T45` |
| `theorem` | [threshold_exists](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/threshold-exists/) | L204-L205 | proof obligation | formal proof obligation checked | `V.T46` |
| `theorem` | [torus_above_threshold](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/torus-above-threshold/) | L211-L213 | proof obligation | formal proof obligation checked | `V.T47` |
| `theorem` | [defect_cost_equality](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/defect-cost-equality/) | L219-L221 | proof obligation | formal proof obligation checked | `V.T48` |
| `def` | [example_coherence_horizon](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/example-coherence-horizon/) | L245-L249 | definition | definition | — |
| `eval` | [#eval L251](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l251/) | L251-L251 | computed check | computed check | — |
| `eval` | [#eval L252](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l252/) | L252-L252 | computed check | computed check | — |
| `def` | [example_crossing](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/example-crossing/) | L255-L256 | definition | definition | — |
| `eval` | [#eval L258](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l258/) | L258-L258 | computed check | computed check | — |
| `eval` | [#eval L259](/corpus/taulib/docs/book-v-gravity-field-tovphase-boundary/eval-l259/) | L259-L261 | computed check | computed check | — |

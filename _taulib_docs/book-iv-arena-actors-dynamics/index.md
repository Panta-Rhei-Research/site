---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Arena.ActorsDynamics",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Arena.ActorsDynamics`.",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_slug": "book-iv-arena-actors-dynamics",
  "book": "BookIV",
  "family": "Arena",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Arena/ActorsDynamics.lean",
  "sha256": "a11c8c85234703a9722316167d3f7f526f95347c721763b6ac7ee2a3c78606c2",
  "imports": [
    "TauLib.BookIV.Arena.FiveSectors",
    "TauLib.BookIV.Physics.QuantityFramework",
    "TauLib.BookIV.Physics.PlanckCharacter",
    "TauLib.BookIV.Physics.DefectFunctional"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.SharedOntology",
    "TauLib.BookV.Prologue.HermeticPrinciple"
  ],
  "registry_ids": [
    "IV.D267",
    "IV.D268",
    "IV.D269",
    "IV.D270",
    "IV.D271",
    "IV.D272",
    "IV.D273",
    "IV.D274",
    "IV.P157",
    "IV.P158",
    "IV.R230",
    "IV.R233",
    "IV.R236",
    "IV.R237",
    "IV.T102",
    "IV.T103"
  ],
  "declaration_counts": {
    "structure": 5,
    "def": 2,
    "theorem": 5,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "DefectBundle",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/defect-bundle/",
      "source_line_start": 47,
      "source_line_end": 54,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D267"
      ]
    },
    {
      "kind": "structure",
      "name": "RadiationMode",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/radiation-mode/",
      "source_line_start": 62,
      "source_line_end": 69,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D268"
      ]
    },
    {
      "kind": "def",
      "name": "photon_mode",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/photon-mode/",
      "source_line_start": 72,
      "source_line_end": 76,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "VirtualMode",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/virtual-mode/",
      "source_line_start": 84,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D269"
      ]
    },
    {
      "kind": "def",
      "name": "primary_invariants",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/primary-invariants/",
      "source_line_start": 102,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D270"
      ]
    },
    {
      "kind": "theorem",
      "name": "primary_invariant_count",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/primary-invariant-count/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "second_law_inv",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/second-law-inv/",
      "source_line_start": 114,
      "source_line_end": 121,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P157"
      ]
    },
    {
      "kind": "structure",
      "name": "MassFiberStiffness",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/mass-fiber-stiffness/",
      "source_line_start": 130,
      "source_line_end": 136,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D271"
      ]
    },
    {
      "kind": "structure",
      "name": "PropagationOp",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/propagation-op/",
      "source_line_start": 147,
      "source_line_end": 152,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D272"
      ]
    },
    {
      "kind": "theorem",
      "name": "schrodinger_shadow",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/schrodinger-shadow/",
      "source_line_start": 160,
      "source_line_end": 178,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D273",
        "IV.P158",
        "IV.T102"
      ]
    },
    {
      "kind": "theorem",
      "name": "heisenberg_ineq",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/heisenberg-ineq/",
      "source_line_start": 181,
      "source_line_end": 202,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D274",
        "IV.R236",
        "IV.T103"
      ]
    },
    {
      "kind": "theorem",
      "name": "euler_budget",
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/euler-budget/",
      "source_line_start": 204,
      "source_line_end": 206,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/eval-l214/",
      "source_line_start": 214,
      "source_line_end": 214,
      "formal_status": "computed",
      "registry_ids": [
        "IV.R237"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/eval-l215/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/eval-l216/",
      "source_line_start": 216,
      "source_line_end": 218,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean",
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
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Arena/ActorsDynamics.lean`
- SHA-256: `a11c8c85234703a9722316167d3f7f526f95347c721763b6ac7ee2a3c78606c2`

## Registry Links

- `IV.D267` — Defect bundle (ontic particle)
- `IV.D268` — Radiation
- `IV.D269` — Virtual particle
- `IV.D270` — Five primary invariants
- `IV.D271` — Mass as fiber stiffness
- `IV.D272` — Propagation operator
- `IV.D273` — Planck character
- `IV.D274` — Defect functional
- `IV.P157` — Second-law inversion
- `IV.P158` — Schr"odinger shadow
- `IV.R230` — Lean formalization
- `IV.R233` — Why gravity is weak
- `IV.R236` — Lean formalization
- `IV.R237` — Lean formalization
- `IV.T102` — tau-Heisenberg inequality
- `IV.T103` — Euler budget conservation

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Arena.FiveSectors`
- `TauLib.BookIV.Physics.QuantityFramework`
- `TauLib.BookIV.Physics.PlanckCharacter`
- `TauLib.BookIV.Physics.DefectFunctional`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.SharedOntology`
- `TauLib.BookV.Prologue.HermeticPrinciple`

## Declaration Counts

- `def`: 2
- `eval`: 3
- `structure`: 5
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [DefectBundle](/verify/taulib/docs/book-iv-arena-actors-dynamics/defect-bundle/) | L47-L54 | defined | `IV.D267` |
| `structure` | [RadiationMode](/verify/taulib/docs/book-iv-arena-actors-dynamics/radiation-mode/) | L62-L69 | defined | `IV.D268` |
| `def` | [photon_mode](/verify/taulib/docs/book-iv-arena-actors-dynamics/photon-mode/) | L72-L76 | defined | — |
| `structure` | [VirtualMode](/verify/taulib/docs/book-iv-arena-actors-dynamics/virtual-mode/) | L84-L91 | defined | `IV.D269` |
| `def` | [primary_invariants](/verify/taulib/docs/book-iv-arena-actors-dynamics/primary-invariants/) | L102-L103 | defined | `IV.D270` |
| `theorem` | [primary_invariant_count](/verify/taulib/docs/book-iv-arena-actors-dynamics/primary-invariant-count/) | L105-L105 | formalized | — |
| `theorem` | [second_law_inv](/verify/taulib/docs/book-iv-arena-actors-dynamics/second-law-inv/) | L114-L121 | formalized | `IV.P157` |
| `structure` | [MassFiberStiffness](/verify/taulib/docs/book-iv-arena-actors-dynamics/mass-fiber-stiffness/) | L130-L136 | defined | `IV.D271` |
| `structure` | [PropagationOp](/verify/taulib/docs/book-iv-arena-actors-dynamics/propagation-op/) | L147-L152 | defined | `IV.D272` |
| `theorem` | [schrodinger_shadow](/verify/taulib/docs/book-iv-arena-actors-dynamics/schrodinger-shadow/) | L160-L178 | formalized | `IV.D273`, `IV.P158`, `IV.T102` |
| `theorem` | [heisenberg_ineq](/verify/taulib/docs/book-iv-arena-actors-dynamics/heisenberg-ineq/) | L181-L202 | formalized | `IV.D274`, `IV.R236`, `IV.T103` |
| `theorem` | [euler_budget](/verify/taulib/docs/book-iv-arena-actors-dynamics/euler-budget/) | L204-L206 | formalized | — |
| `eval` | [#eval L214](/verify/taulib/docs/book-iv-arena-actors-dynamics/eval-l214/) | L214-L214 | computed | `IV.R237` |
| `eval` | [#eval L215](/verify/taulib/docs/book-iv-arena-actors-dynamics/eval-l215/) | L215-L215 | computed | — |
| `eval` | [#eval L216](/verify/taulib/docs/book-iv-arena-actors-dynamics/eval-l216/) | L216-L218 | computed | — |

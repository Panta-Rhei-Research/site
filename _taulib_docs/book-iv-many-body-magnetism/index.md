---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.ManyBody.Magnetism",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-magnetism/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.ManyBody.Magnetism`.",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_slug": "book-iv-many-body-magnetism",
  "book": "BookIV",
  "family": "ManyBody",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/ManyBody/Magnetism.lean",
  "sha256": "da2c534166f5f6189735ab40b951c63a26381350acec10ad24c9f9b39682e961",
  "imports": [
    "TauLib.BookIV.ManyBody.FluidRegimes"
  ],
  "imported_by": [
    "TauLib.BookIV"
  ],
  "registry_ids": [
    "IV.D387",
    "IV.D388",
    "IV.D389",
    "IV.P226",
    "IV.P227",
    "IV.P228",
    "IV.T208",
    "IV.T209"
  ],
  "declaration_counts": {
    "structure": 8,
    "def": 8,
    "theorem": 7,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "MagneticMoment",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-moment/",
      "source_line_start": 54,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D387"
      ]
    },
    {
      "kind": "def",
      "name": "magnetic_moment",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-moment-l63/",
      "source_line_start": 63,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IsingHamiltonian",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian/",
      "source_line_start": 73,
      "source_line_end": 82,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D388"
      ]
    },
    {
      "kind": "def",
      "name": "ising_hamiltonian",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian-l84/",
      "source_line_start": 84,
      "source_line_end": 84,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ising_periodic_bc",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/ising-periodic-bc/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SpontaneousMagnetization",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization/",
      "source_line_start": 97,
      "source_line_end": 108,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P226"
      ]
    },
    {
      "kind": "def",
      "name": "spontaneous_magnetization",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization-l110/",
      "source_line_start": 110,
      "source_line_end": 110,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetization_transition",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/magnetization-transition/",
      "source_line_start": 112,
      "source_line_end": 113,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoMonopoles",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/no-monopoles/",
      "source_line_start": 131,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T208"
      ]
    },
    {
      "kind": "def",
      "name": "no_monopoles",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/no-monopoles-l146/",
      "source_line_start": 146,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_char_T2_zero",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/euler-char-t2-zero/",
      "source_line_start": 148,
      "source_line_end": 149,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_monopoles_topological",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/no-monopoles-topological/",
      "source_line_start": 151,
      "source_line_end": 152,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DomainWall",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall/",
      "source_line_start": 162,
      "source_line_end": 171,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D389"
      ]
    },
    {
      "kind": "def",
      "name": "domain_wall",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall-l173/",
      "source_line_start": 173,
      "source_line_end": 173,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DomainWallEnergy",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy/",
      "source_line_start": 183,
      "source_line_end": 192,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P227"
      ]
    },
    {
      "kind": "def",
      "name": "domain_wall_energy",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CurieTransition",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/curie-transition/",
      "source_line_start": 207,
      "source_line_end": 218,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T209"
      ]
    },
    {
      "kind": "def",
      "name": "curie_transition",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/curie-transition-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "curie_is_second_order",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/curie-is-second-order/",
      "source_line_start": 222,
      "source_line_end": 223,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MagneticOrders",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-orders/",
      "source_line_start": 235,
      "source_line_end": 244,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P228"
      ]
    },
    {
      "kind": "def",
      "name": "magnetic_orders",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_magnetic_orders",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/five-magnetic-orders/",
      "source_line_start": 248,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetic_orders_count",
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-count/",
      "source_line_start": 251,
      "source_line_end": 252,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l258/",
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
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l259/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 268,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean",
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
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/ManyBody/Magnetism.lean`
- SHA-256: `da2c534166f5f6189735ab40b951c63a26381350acec10ad24c9f9b39682e961`

## Registry Links

- `IV.D387` — Magnetic Moment on T²
- `IV.D388` — τ-Ising Hamiltonian on T²
- `IV.D389` — Magnetic Domain Wall on T²
- `IV.P226` — Spontaneous Magnetization on T²
- `IV.P227` — Domain Wall Energy from T² Winding
- `IV.P228` — Magnetic Orders as Defect-Tuple Signatures
- `IV.T208` — No Magnetic Monopoles on T²
- `IV.T209` — Curie Transition as T² Symmetry Breaking

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.ManyBody.FluidRegimes`

## Imported By

- `TauLib.BookIV`

## Declaration Counts

- `def`: 8
- `eval`: 9
- `structure`: 8
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [MagneticMoment](/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-moment/) | L54-L61 | type/data schema | type/data schema | `IV.D387` |
| `def` | [magnetic_moment](/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-moment-l63/) | L63-L63 | definition | definition | — |
| `structure` | [IsingHamiltonian](/corpus/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian/) | L73-L82 | type/data schema | type/data schema | `IV.D388` |
| `def` | [ising_hamiltonian](/corpus/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian-l84/) | L84-L84 | definition | definition | — |
| `theorem` | [ising_periodic_bc](/corpus/taulib/docs/book-iv-many-body-magnetism/ising-periodic-bc/) | L86-L87 | proof obligation | formal proof obligation checked | — |
| `structure` | [SpontaneousMagnetization](/corpus/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization/) | L97-L108 | type/data schema | type/data schema | `IV.P226` |
| `def` | [spontaneous_magnetization](/corpus/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization-l110/) | L110-L110 | definition | definition | — |
| `theorem` | [magnetization_transition](/corpus/taulib/docs/book-iv-many-body-magnetism/magnetization-transition/) | L112-L113 | proof obligation | formal proof obligation checked | — |
| `structure` | [NoMonopoles](/corpus/taulib/docs/book-iv-many-body-magnetism/no-monopoles/) | L131-L144 | type/data schema | type/data schema | `IV.T208` |
| `def` | [no_monopoles](/corpus/taulib/docs/book-iv-many-body-magnetism/no-monopoles-l146/) | L146-L146 | definition | definition | — |
| `theorem` | [euler_char_T2_zero](/corpus/taulib/docs/book-iv-many-body-magnetism/euler-char-t2-zero/) | L148-L149 | proof obligation | formal proof obligation checked | — |
| `theorem` | [no_monopoles_topological](/corpus/taulib/docs/book-iv-many-body-magnetism/no-monopoles-topological/) | L151-L152 | proof obligation | formal proof obligation checked | — |
| `structure` | [DomainWall](/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall/) | L162-L171 | type/data schema | type/data schema | `IV.D389` |
| `def` | [domain_wall](/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall-l173/) | L173-L173 | definition | definition | — |
| `structure` | [DomainWallEnergy](/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy/) | L183-L192 | type/data schema | type/data schema | `IV.P227` |
| `def` | [domain_wall_energy](/corpus/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy-l194/) | L194-L194 | definition | definition | — |
| `structure` | [CurieTransition](/corpus/taulib/docs/book-iv-many-body-magnetism/curie-transition/) | L207-L218 | type/data schema | type/data schema | `IV.T209` |
| `def` | [curie_transition](/corpus/taulib/docs/book-iv-many-body-magnetism/curie-transition-l220/) | L220-L220 | definition | definition | — |
| `theorem` | [curie_is_second_order](/corpus/taulib/docs/book-iv-many-body-magnetism/curie-is-second-order/) | L222-L223 | proof obligation | formal proof obligation checked | — |
| `structure` | [MagneticOrders](/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-orders/) | L235-L244 | type/data schema | type/data schema | `IV.P228` |
| `def` | [magnetic_orders](/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-l246/) | L246-L246 | definition | definition | — |
| `theorem` | [five_magnetic_orders](/corpus/taulib/docs/book-iv-many-body-magnetism/five-magnetic-orders/) | L248-L249 | proof obligation | formal proof obligation checked | — |
| `theorem` | [magnetic_orders_count](/corpus/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-count/) | L251-L252 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L258](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l258/) | L258-L258 | computed check | computed check | — |
| `eval` | [#eval L259](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l259/) | L259-L259 | computed check | computed check | — |
| `eval` | [#eval L260](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l260/) | L260-L260 | computed check | computed check | — |
| `eval` | [#eval L261](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l261/) | L261-L261 | computed check | computed check | — |
| `eval` | [#eval L262](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l262/) | L262-L262 | computed check | computed check | — |
| `eval` | [#eval L263](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l263/) | L263-L263 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l264/) | L264-L264 | computed check | computed check | — |
| `eval` | [#eval L265](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l265/) | L265-L265 | computed check | computed check | — |
| `eval` | [#eval L266](/corpus/taulib/docs/book-iv-many-body-magnetism/eval-l266/) | L266-L268 | computed check | computed check | — |

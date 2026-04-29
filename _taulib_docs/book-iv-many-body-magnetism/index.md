---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.ManyBody.Magnetism",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/",
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
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-moment/",
      "source_line_start": 54,
      "source_line_end": 61,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D387"
      ]
    },
    {
      "kind": "def",
      "name": "magnetic_moment",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-moment-l63/",
      "source_line_start": 63,
      "source_line_end": 63,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IsingHamiltonian",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian/",
      "source_line_start": 73,
      "source_line_end": 82,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D388"
      ]
    },
    {
      "kind": "def",
      "name": "ising_hamiltonian",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian-l84/",
      "source_line_start": 84,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ising_periodic_bc",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/ising-periodic-bc/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SpontaneousMagnetization",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization/",
      "source_line_start": 97,
      "source_line_end": 108,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P226"
      ]
    },
    {
      "kind": "def",
      "name": "spontaneous_magnetization",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization-l110/",
      "source_line_start": 110,
      "source_line_end": 110,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetization_transition",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetization-transition/",
      "source_line_start": 112,
      "source_line_end": 113,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoMonopoles",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/no-monopoles/",
      "source_line_start": 131,
      "source_line_end": 144,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T208"
      ]
    },
    {
      "kind": "def",
      "name": "no_monopoles",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/no-monopoles-l146/",
      "source_line_start": 146,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euler_char_T2_zero",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/euler-char-t2-zero/",
      "source_line_start": 148,
      "source_line_end": 149,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_monopoles_topological",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/no-monopoles-topological/",
      "source_line_start": 151,
      "source_line_end": 152,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DomainWall",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall/",
      "source_line_start": 162,
      "source_line_end": 171,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D389"
      ]
    },
    {
      "kind": "def",
      "name": "domain_wall",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall-l173/",
      "source_line_start": 173,
      "source_line_end": 173,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DomainWallEnergy",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy/",
      "source_line_start": 183,
      "source_line_end": 192,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P227"
      ]
    },
    {
      "kind": "def",
      "name": "domain_wall_energy",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CurieTransition",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/curie-transition/",
      "source_line_start": 207,
      "source_line_end": 218,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T209"
      ]
    },
    {
      "kind": "def",
      "name": "curie_transition",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/curie-transition-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "curie_is_second_order",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/curie-is-second-order/",
      "source_line_start": 222,
      "source_line_end": 223,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MagneticOrders",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-orders/",
      "source_line_start": 235,
      "source_line_end": 244,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P228"
      ]
    },
    {
      "kind": "def",
      "name": "magnetic_orders",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_magnetic_orders",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/five-magnetic-orders/",
      "source_line_start": 248,
      "source_line_end": 249,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "magnetic_orders_count",
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-count/",
      "source_line_start": 251,
      "source_line_end": 252,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l258/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l259/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-magnetism/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 268,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [MagneticMoment](/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-moment/) | L54-L61 | defined | `IV.D387` |
| `def` | [magnetic_moment](/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-moment-l63/) | L63-L63 | defined | — |
| `structure` | [IsingHamiltonian](/verify/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian/) | L73-L82 | defined | `IV.D388` |
| `def` | [ising_hamiltonian](/verify/taulib/docs/book-iv-many-body-magnetism/ising-hamiltonian-l84/) | L84-L84 | defined | — |
| `theorem` | [ising_periodic_bc](/verify/taulib/docs/book-iv-many-body-magnetism/ising-periodic-bc/) | L86-L87 | formalized | — |
| `structure` | [SpontaneousMagnetization](/verify/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization/) | L97-L108 | defined | `IV.P226` |
| `def` | [spontaneous_magnetization](/verify/taulib/docs/book-iv-many-body-magnetism/spontaneous-magnetization-l110/) | L110-L110 | defined | — |
| `theorem` | [magnetization_transition](/verify/taulib/docs/book-iv-many-body-magnetism/magnetization-transition/) | L112-L113 | formalized | — |
| `structure` | [NoMonopoles](/verify/taulib/docs/book-iv-many-body-magnetism/no-monopoles/) | L131-L144 | defined | `IV.T208` |
| `def` | [no_monopoles](/verify/taulib/docs/book-iv-many-body-magnetism/no-monopoles-l146/) | L146-L146 | defined | — |
| `theorem` | [euler_char_T2_zero](/verify/taulib/docs/book-iv-many-body-magnetism/euler-char-t2-zero/) | L148-L149 | formalized | — |
| `theorem` | [no_monopoles_topological](/verify/taulib/docs/book-iv-many-body-magnetism/no-monopoles-topological/) | L151-L152 | formalized | — |
| `structure` | [DomainWall](/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall/) | L162-L171 | defined | `IV.D389` |
| `def` | [domain_wall](/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall-l173/) | L173-L173 | defined | — |
| `structure` | [DomainWallEnergy](/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy/) | L183-L192 | defined | `IV.P227` |
| `def` | [domain_wall_energy](/verify/taulib/docs/book-iv-many-body-magnetism/domain-wall-energy-l194/) | L194-L194 | defined | — |
| `structure` | [CurieTransition](/verify/taulib/docs/book-iv-many-body-magnetism/curie-transition/) | L207-L218 | defined | `IV.T209` |
| `def` | [curie_transition](/verify/taulib/docs/book-iv-many-body-magnetism/curie-transition-l220/) | L220-L220 | defined | — |
| `theorem` | [curie_is_second_order](/verify/taulib/docs/book-iv-many-body-magnetism/curie-is-second-order/) | L222-L223 | formalized | — |
| `structure` | [MagneticOrders](/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-orders/) | L235-L244 | defined | `IV.P228` |
| `def` | [magnetic_orders](/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-l246/) | L246-L246 | defined | — |
| `theorem` | [five_magnetic_orders](/verify/taulib/docs/book-iv-many-body-magnetism/five-magnetic-orders/) | L248-L249 | formalized | — |
| `theorem` | [magnetic_orders_count](/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-orders-count/) | L251-L252 | formalized | — |
| `eval` | [#eval L258](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l258/) | L258-L258 | computed | — |
| `eval` | [#eval L259](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l259/) | L259-L259 | computed | — |
| `eval` | [#eval L260](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l260/) | L260-L260 | computed | — |
| `eval` | [#eval L261](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l261/) | L261-L261 | computed | — |
| `eval` | [#eval L262](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l262/) | L262-L262 | computed | — |
| `eval` | [#eval L263](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l263/) | L263-L263 | computed | — |
| `eval` | [#eval L264](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l264/) | L264-L264 | computed | — |
| `eval` | [#eval L265](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l265/) | L265-L265 | computed | — |
| `eval` | [#eval L266](/verify/taulib/docs/book-iv-many-body-magnetism/eval-l266/) | L266-L268 | computed | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "permalink": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_slug": "book-iv-quantum-mechanics-craddress-space",
  "book": "BookIV",
  "family": "QuantumMechanics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean",
  "sha256": "d96eed2e9c8f83a6d21692432ab1d3db3b88177c469cde18920161ad05984609",
  "imports": [
    "TauLib.BookIV.Arena.Tau3Arena",
    "TauLib.BookIV.Arena.BoundaryHolonomy"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.QuantumMechanics.QuantumCharacters"
  ],
  "registry_ids": [
    "IV.D49",
    "IV.D50",
    "IV.D51",
    "IV.D52",
    "IV.D53",
    "IV.D54",
    "IV.L01",
    "IV.P08",
    "IV.P09",
    "IV.P10",
    "IV.R292",
    "IV.R294",
    "IV.R295",
    "IV.T16",
    "IV.T17"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 5,
    "theorem": 6,
    "example": 3,
    "eval": 11
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CRManifold",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/crmanifold/",
      "source_line_start": 45,
      "source_line_end": 54,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D49"
      ]
    },
    {
      "kind": "def",
      "name": "CRManifold.mk_auto",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/mk-auto/",
      "source_line_start": 57,
      "source_line_end": 61,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IntegrableCR",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/integrable-cr/",
      "source_line_start": 70,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P08"
      ]
    },
    {
      "kind": "theorem",
      "name": "integrability_criterion",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/integrability-criterion/",
      "source_line_start": 77,
      "source_line_end": 78,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cr_structure_tau3",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-structure-tau3/",
      "source_line_start": 88,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D50"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau3_cr_integrable",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/tau3-cr-integrable/",
      "source_line_start": 103,
      "source_line_end": 103,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P09"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau3_cr_dim",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/tau3-cr-dim/",
      "source_line_start": 106,
      "source_line_end": 106,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CharacterMode",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/character-mode/",
      "source_line_start": 115,
      "source_line_end": 129,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D51",
        "IV.D52"
      ]
    },
    {
      "kind": "structure",
      "name": "AddressPrecision",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/address-precision/",
      "source_line_start": 138,
      "source_line_end": 149,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D53"
      ]
    },
    {
      "kind": "structure",
      "name": "WedgeHolonomy",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/wedge-holonomy/",
      "source_line_start": 159,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.L01"
      ]
    },
    {
      "kind": "def",
      "name": "wedge_holonomy",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/wedge-holonomy-l168/",
      "source_line_start": 168,
      "source_line_end": 171,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cr_admissible",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-admissible/",
      "source_line_start": 180,
      "source_line_end": 185,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.T16"
      ]
    },
    {
      "kind": "theorem",
      "name": "cr_parity_constraint",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-parity-constraint/",
      "source_line_start": 188,
      "source_line_end": 190,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/example-l193/",
      "source_line_start": 193,
      "source_line_end": 193,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/example-l196/",
      "source_line_start": 196,
      "source_line_end": 196,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/example-l199/",
      "source_line_start": 199,
      "source_line_end": 199,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AdmissibleLattice",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/admissible-lattice/",
      "source_line_start": 207,
      "source_line_end": 211,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D54"
      ]
    },
    {
      "kind": "theorem",
      "name": "density_halving",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/density-halving/",
      "source_line_start": 220,
      "source_line_end": 223,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P10"
      ]
    },
    {
      "kind": "theorem",
      "name": "density_halving_converse",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/density-halving-converse/",
      "source_line_start": 226,
      "source_line_end": 229,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SpinHalfEmergence",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/spin-half-emergence/",
      "source_line_start": 242,
      "source_line_end": 251,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T17"
      ]
    },
    {
      "kind": "def",
      "name": "spin_half_emergence",
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/spin-half-emergence-l254/",
      "source_line_start": 254,
      "source_line_end": 259,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l275/",
      "source_line_start": 275,
      "source_line_end": 275,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "IV.R292",
        "IV.R294",
        "IV.R295"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l276/",
      "source_line_start": 276,
      "source_line_end": 276,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l277/",
      "source_line_start": 277,
      "source_line_end": 277,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l278/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l279/",
      "source_line_start": 279,
      "source_line_end": 279,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 289,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`
- SHA-256: `d96eed2e9c8f83a6d21692432ab1d3db3b88177c469cde18920161ad05984609`

## Registry Links

- `IV.D49` — CR-Manifold
- `IV.D50` — CR-Structure on τ³
- `IV.D51` — Character Modes
- `IV.D52` — CR-Address
- `IV.D53` — Address Precision (ch16)
- `IV.D54` — CR-Admissible Sublattice
- `IV.L01` — Wedge Holonomy
- `IV.P08` — Integrability Criterion
- `IV.P09` — Integrability of τ³ CR-Structure
- `IV.P10` — Density Halving
- `IV.R292` — CR-type (1,1) and three-dimensionality
- `IV.R294` — Spin-frac1
- `IV.R295` — Bosons and fermions
- `IV.T16` — CR Parity Constraint
- `IV.T17` — Emergence of Spin-1/2

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Arena.Tau3Arena`
- `TauLib.BookIV.Arena.BoundaryHolonomy`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.QuantumMechanics.QuantumCharacters`

## Declaration Counts

- `def`: 5
- `eval`: 11
- `example`: 3
- `structure`: 7
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CRManifold](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/crmanifold/) | L45-L54 | type/data schema | type/data schema | `IV.D49` |
| `def` | [CRManifold.mk_auto](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/mk-auto/) | L57-L61 | data/computed value | data/computed value | — |
| `structure` | [IntegrableCR](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/integrable-cr/) | L70-L74 | type/data schema | type/data schema | `IV.P08` |
| `theorem` | [integrability_criterion](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/integrability-criterion/) | L77-L78 | proof obligation | formal proof obligation checked | — |
| `def` | [cr_structure_tau3](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-structure-tau3/) | L88-L94 | data/computed value | data/computed value | `IV.D50` |
| `theorem` | [tau3_cr_integrable](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/tau3-cr-integrable/) | L103-L103 | proof obligation | formal proof obligation checked | `IV.P09` |
| `theorem` | [tau3_cr_dim](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/tau3-cr-dim/) | L106-L106 | proof obligation | formal proof obligation checked | — |
| `structure` | [CharacterMode](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/character-mode/) | L115-L129 | type/data schema | type/data schema | `IV.D51`, `IV.D52` |
| `structure` | [AddressPrecision](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/address-precision/) | L138-L149 | type/data schema | type/data schema | `IV.D53` |
| `structure` | [WedgeHolonomy](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/wedge-holonomy/) | L159-L165 | type/data schema | type/data schema | `IV.L01` |
| `def` | [wedge_holonomy](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/wedge-holonomy-l168/) | L168-L171 | definition | definition | — |
| `def` | [cr_admissible](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-admissible/) | L180-L185 | definition | definition | `IV.T16` |
| `theorem` | [cr_parity_constraint](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/cr-parity-constraint/) | L188-L190 | proof obligation | formal proof obligation checked | — |
| `example` | [#eval L193](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/example-l193/) | L193-L193 | example check | example | — |
| `example` | [#eval L196](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/example-l196/) | L196-L196 | example check | example | — |
| `example` | [#eval L199](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/example-l199/) | L199-L199 | example check | example | — |
| `structure` | [AdmissibleLattice](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/admissible-lattice/) | L207-L211 | type/data schema | type/data schema | `IV.D54` |
| `theorem` | [density_halving](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/density-halving/) | L220-L223 | proof obligation | formal proof obligation checked | `IV.P10` |
| `theorem` | [density_halving_converse](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/density-halving-converse/) | L226-L229 | proof obligation | formal proof obligation checked | — |
| `structure` | [SpinHalfEmergence](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/spin-half-emergence/) | L242-L251 | type/data schema | type/data schema | `IV.T17` |
| `def` | [spin_half_emergence](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/spin-half-emergence-l254/) | L254-L259 | definition | definition | — |
| `eval` | [#eval L275](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l275/) | L275-L275 | computed check | computed check | `IV.R292`, `IV.R294`, `IV.R295` |
| `eval` | [#eval L276](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l276/) | L276-L276 | computed check | computed check | — |
| `eval` | [#eval L277](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l277/) | L277-L277 | computed check | computed check | — |
| `eval` | [#eval L278](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l278/) | L278-L278 | computed check | computed check | — |
| `eval` | [#eval L279](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l279/) | L279-L279 | computed check | computed check | — |
| `eval` | [#eval L280](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l280/) | L280-L280 | computed check | computed check | — |
| `eval` | [#eval L283](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l283/) | L283-L283 | computed check | computed check | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l286/) | L286-L286 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-iv-quantum-mechanics-craddress-space/eval-l287/) | L287-L289 | computed check | computed check | — |

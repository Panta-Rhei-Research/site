---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_slug": "book-iv-quantum-mechanics-hilbert-space",
  "book": "BookIV",
  "family": "QuantumMechanics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean",
  "sha256": "ac8c78f8e3f735f05a0104da59574b119abe49c70f79e3e6f03ef7f762edcf56",
  "imports": [
    "TauLib.BookIV.QuantumMechanics.QuantumCharacters"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.QuantumMechanics.Quantization"
  ],
  "registry_ids": [
    "IV.D60",
    "IV.D61",
    "IV.D62",
    "IV.D63",
    "IV.D64",
    "IV.P16",
    "IV.P17",
    "IV.P18",
    "IV.P19",
    "IV.P20",
    "IV.P21",
    "IV.P22",
    "IV.T18",
    "IV.T19"
  ],
  "declaration_counts": {
    "structure": 8,
    "def": 7,
    "theorem": 6,
    "inductive": 1,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CRFunctionSpace",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/crfunction-space/",
      "source_line_start": 48,
      "source_line_end": 58,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D60"
      ]
    },
    {
      "kind": "def",
      "name": "cr_function_space",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/cr-function-space/",
      "source_line_start": 61,
      "source_line_end": 67,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cr_space_algebraic",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/cr-space-algebraic/",
      "source_line_start": 75,
      "source_line_end": 79,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P16"
      ]
    },
    {
      "kind": "structure",
      "name": "TauInnerProduct",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/tau-inner-product/",
      "source_line_start": 89,
      "source_line_end": 99,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D61"
      ]
    },
    {
      "kind": "def",
      "name": "tau_inner_product",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/tau-inner-product-l102/",
      "source_line_start": 102,
      "source_line_end": 108,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "inner_product_properties",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-properties/",
      "source_line_start": 116,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P17"
      ]
    },
    {
      "kind": "structure",
      "name": "InnerProductUniqueness",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-uniqueness/",
      "source_line_start": 131,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P18"
      ]
    },
    {
      "kind": "def",
      "name": "inner_product_unique",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-unique/",
      "source_line_start": 141,
      "source_line_end": 145,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "HilbertSpaceTau",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/hilbert-space-tau/",
      "source_line_start": 153,
      "source_line_end": 163,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D62"
      ]
    },
    {
      "kind": "def",
      "name": "hilbert_tau",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/hilbert-tau/",
      "source_line_start": 166,
      "source_line_end": 172,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "von_neumann_axioms",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/von-neumann-axioms/",
      "source_line_start": 181,
      "source_line_end": 185,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T18"
      ]
    },
    {
      "kind": "structure",
      "name": "BoundaryDetermination",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/boundary-determination/",
      "source_line_start": 195,
      "source_line_end": 204,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P19"
      ]
    },
    {
      "kind": "def",
      "name": "boundary_determines_states",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/boundary-determines-states/",
      "source_line_start": 207,
      "source_line_end": 212,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ONBStructure",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onbstructure/",
      "source_line_start": 221,
      "source_line_end": 234,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T19"
      ]
    },
    {
      "kind": "def",
      "name": "onb_admissible",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onb-admissible/",
      "source_line_start": 237,
      "source_line_end": 245,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "onb_is_admissible_characters",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onb-is-admissible-characters/",
      "source_line_start": 248,
      "source_line_end": 253,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T19"
      ]
    },
    {
      "kind": "theorem",
      "name": "spectral_completeness",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/spectral-completeness/",
      "source_line_start": 262,
      "source_line_end": 263,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P20"
      ]
    },
    {
      "kind": "structure",
      "name": "PhysicalState",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/physical-state/",
      "source_line_start": 271,
      "source_line_end": 278,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D63"
      ]
    },
    {
      "kind": "inductive",
      "name": "EntanglementClass",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entanglement-class/",
      "source_line_start": 286,
      "source_line_end": 291,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D64"
      ]
    },
    {
      "kind": "structure",
      "name": "EntanglementGenericity",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entanglement-genericity/",
      "source_line_start": 300,
      "source_line_end": 307,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P21"
      ]
    },
    {
      "kind": "def",
      "name": "entangled_is_generic",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entangled-is-generic/",
      "source_line_start": 310,
      "source_line_end": 314,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "superposition_from_linearity",
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/superposition-from-linearity/",
      "source_line_start": 324,
      "source_line_end": 325,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P22"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l337/",
      "source_line_start": 337,
      "source_line_end": 339,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`
- SHA-256: `ac8c78f8e3f735f05a0104da59574b119abe49c70f79e3e6f03ef7f762edcf56`

## Registry Links

- `IV.D60` — Space of CR-Functions
- `IV.D61` — Canonical Inner Product
- `IV.D62` — Holomorphic Hilbert Space
- `IV.D63` — Physical State Space
- `IV.D64` — Entanglement
- `IV.P16` — Algebraic Properties of CR(τ³)
- `IV.P17` — Inner Product Properties
- `IV.P18` — Inner Product Uniqueness
- `IV.P19` — Central Theorem Implies Boundary Determination
- `IV.P20` — Spectral Completeness
- `IV.P21` — Generic Entanglement
- `IV.P22` — Superposition from Linearity
- `IV.T18` — Hilbert Space Properties
- `IV.T19` — Orthonormal Basis

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.QuantumMechanics.QuantumCharacters`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.QuantumMechanics.Quantization`

## Declaration Counts

- `def`: 7
- `eval`: 7
- `inductive`: 1
- `structure`: 8
- `theorem`: 6

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [CRFunctionSpace](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/crfunction-space/) | L48-L58 | defined | `IV.D60` |
| `def` | [cr_function_space](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/cr-function-space/) | L61-L67 | defined | — |
| `theorem` | [cr_space_algebraic](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/cr-space-algebraic/) | L75-L79 | formalized | `IV.P16` |
| `structure` | [TauInnerProduct](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/tau-inner-product/) | L89-L99 | defined | `IV.D61` |
| `def` | [tau_inner_product](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/tau-inner-product-l102/) | L102-L108 | defined | — |
| `theorem` | [inner_product_properties](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-properties/) | L116-L120 | formalized | `IV.P17` |
| `structure` | [InnerProductUniqueness](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-uniqueness/) | L131-L138 | defined | `IV.P18` |
| `def` | [inner_product_unique](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-unique/) | L141-L145 | defined | — |
| `structure` | [HilbertSpaceTau](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/hilbert-space-tau/) | L153-L163 | defined | `IV.D62` |
| `def` | [hilbert_tau](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/hilbert-tau/) | L166-L172 | defined | — |
| `theorem` | [von_neumann_axioms](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/von-neumann-axioms/) | L181-L185 | formalized | `IV.T18` |
| `structure` | [BoundaryDetermination](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/boundary-determination/) | L195-L204 | defined | `IV.P19` |
| `def` | [boundary_determines_states](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/boundary-determines-states/) | L207-L212 | defined | — |
| `structure` | [ONBStructure](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onbstructure/) | L221-L234 | defined | `IV.T19` |
| `def` | [onb_admissible](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onb-admissible/) | L237-L245 | defined | — |
| `theorem` | [onb_is_admissible_characters](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/onb-is-admissible-characters/) | L248-L253 | formalized | `IV.T19` |
| `theorem` | [spectral_completeness](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/spectral-completeness/) | L262-L263 | formalized | `IV.P20` |
| `structure` | [PhysicalState](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/physical-state/) | L271-L278 | defined | `IV.D63` |
| `inductive` | [EntanglementClass](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entanglement-class/) | L286-L291 | defined | `IV.D64` |
| `structure` | [EntanglementGenericity](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entanglement-genericity/) | L300-L307 | defined | `IV.P21` |
| `def` | [entangled_is_generic](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/entangled-is-generic/) | L310-L314 | defined | — |
| `theorem` | [superposition_from_linearity](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/superposition-from-linearity/) | L324-L325 | formalized | `IV.P22` |
| `eval` | [#eval L331](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l331/) | L331-L331 | computed | — |
| `eval` | [#eval L332](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l332/) | L332-L332 | computed | — |
| `eval` | [#eval L333](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l333/) | L333-L333 | computed | — |
| `eval` | [#eval L334](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l334/) | L334-L334 | computed | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L336](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l336/) | L336-L336 | computed | — |
| `eval` | [#eval L337](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/eval-l337/) | L337-L339 | computed | — |

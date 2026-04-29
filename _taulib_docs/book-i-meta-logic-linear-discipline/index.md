---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.MetaLogic.LinearDiscipline`.",
  "module_name": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "module_slug": "book-i-meta-logic-linear-discipline",
  "book": "BookI",
  "family": "MetaLogic",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/MetaLogic/LinearDiscipline.lean",
  "sha256": "80f602ca6c7c11bd580301f121c5741d42eab7783e3eb37b6083fe60852753ac",
  "imports": [
    "TauLib.BookI.MetaLogic.Substrate",
    "TauLib.BookI.Denotation.ProgramMonoid",
    "TauLib.BookI.Logic.Truth4"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.KernelFoundation.H8KernelSynthesis",
    "TauLib.BookI.MetaLogic.LinearityAudit",
    "TauLib.BookI.MetaLogic.StructuralExclusion"
  ],
  "registry_ids": [
    "I.D78",
    "I.D79",
    "I.T37"
  ],
  "declaration_counts": {
    "inductive": 3,
    "def": 8,
    "theorem": 22,
    "structure": 1,
    "eval": 16
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "LinearAspect",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect/",
      "source_line_start": 36,
      "source_line_end": 40,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "DiagonalAspect",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect/",
      "source_line_start": 43,
      "source_line_end": 49,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "diag_to_linear",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear/",
      "source_line_start": 56,
      "source_line_end": 59,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "linear_to_diag",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag/",
      "source_line_start": 62,
      "source_line_end": 65,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diag_linear_roundtrip",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diag-linear-roundtrip/",
      "source_line_start": 68,
      "source_line_end": 70,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "linear_diag_roundtrip",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-diag-roundtrip/",
      "source_line_start": 73,
      "source_line_end": 75,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diag_to_linear_injective",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear-injective/",
      "source_line_start": 78,
      "source_line_end": 80,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "linear_to_diag_injective",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag-injective/",
      "source_line_start": 83,
      "source_line_end": 85,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allDiagonalAspects",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/all-diagonal-aspects/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allLinearAspects",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/all-linear-aspects/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diagonal_aspect_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect-count/",
      "source_line_start": 96,
      "source_line_end": 96,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "linear_aspect_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect-count/",
      "source_line_start": 99,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "isRhoPure",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/is-rho-pure/",
      "source_line_start": 110,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "empty_is_rho_pure",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/empty-is-rho-pure/",
      "source_line_start": 116,
      "source_line_end": 116,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rho_pure_compose",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/rho-pure-compose/",
      "source_line_start": 121,
      "source_line_end": 133,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cut_elimination_additive",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/cut-elimination-additive/",
      "source_line_start": 138,
      "source_line_end": 141,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "identity_zero_resource",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/identity-zero-resource/",
      "source_line_start": 144,
      "source_line_end": 146,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ResourceState",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-state/",
      "source_line_start": 157,
      "source_line_end": 164,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "truth4_to_resource",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource/",
      "source_line_start": 167,
      "source_line_end": 171,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "resource_to_truth4",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4/",
      "source_line_start": 174,
      "source_line_end": 178,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth4_resource_roundtrip",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/truth4-resource-roundtrip/",
      "source_line_start": 181,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resource_truth4_roundtrip",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-truth4-roundtrip/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth4_to_resource_injective",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource-injective/",
      "source_line_start": 191,
      "source_line_end": 193,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resource_to_truth4_injective",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4-injective/",
      "source_line_start": 196,
      "source_line_end": 198,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "overdetermined_is_contraction_artifact",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/overdetermined-is-contraction-artifact/",
      "source_line_start": 207,
      "source_line_end": 208,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "underdetermined_is_weakening_artifact",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/underdetermined-is-weakening-artifact/",
      "source_line_start": 213,
      "source_line_end": 214,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "present_is_T",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/present-is-t/",
      "source_line_start": 217,
      "source_line_end": 218,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "absent_is_F",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/absent-is-f/",
      "source_line_start": 221,
      "source_line_end": 222,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allResourceStates",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/all-resource-states/",
      "source_line_start": 225,
      "source_line_end": 226,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resource_state_count",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-state-count/",
      "source_line_start": 229,
      "source_line_end": 229,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "contraction_produces_overdetermined",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/contraction-produces-overdetermined/",
      "source_line_start": 238,
      "source_line_end": 241,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weakening_produces_underdetermined",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/weakening-produces-underdetermined/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DiagonalLinearCorrespondence",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence/",
      "source_line_start": 264,
      "source_line_end": 280,
      "formal_status": "defined",
      "registry_ids": [
        "I.T37"
      ]
    },
    {
      "kind": "theorem",
      "name": "diagonal_linear_correspondence",
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence-l283/",
      "source_line_start": 283,
      "source_line_end": 291,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l298/",
      "source_line_start": 298,
      "source_line_end": 298,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l299/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l301/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l302/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l303/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l308/",
      "source_line_start": 308,
      "source_line_end": 308,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l309/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 310,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l311/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 321,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean",
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
- Source path: [`TauLib/BookI/MetaLogic/LinearDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/MetaLogic/LinearDiscipline.lean`
- SHA-256: `80f602ca6c7c11bd580301f121c5741d42eab7783e3eb37b6083fe60852753ac`

## Registry Links

- `I.D78` — Diagonal-Linear Correspondence
- `I.D79` — Program Monoid as Linear Calculus
- `I.T37` — Diagonal-Linear Correspondence

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.MetaLogic.Substrate`
- `TauLib.BookI.Denotation.ProgramMonoid`
- `TauLib.BookI.Logic.Truth4`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.KernelFoundation.H8KernelSynthesis`
- `TauLib.BookI.MetaLogic.LinearityAudit`
- `TauLib.BookI.MetaLogic.StructuralExclusion`

## Declaration Counts

- `def`: 8
- `eval`: 16
- `inductive`: 3
- `structure`: 1
- `theorem`: 22

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [LinearAspect](/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect/) | L36-L40 | defined | — |
| `inductive` | [DiagonalAspect](/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect/) | L43-L49 | defined | — |
| `def` | [diag_to_linear](/verify/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear/) | L56-L59 | defined | — |
| `def` | [linear_to_diag](/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag/) | L62-L65 | defined | — |
| `theorem` | [diag_linear_roundtrip](/verify/taulib/docs/book-i-meta-logic-linear-discipline/diag-linear-roundtrip/) | L68-L70 | formalized | — |
| `theorem` | [linear_diag_roundtrip](/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-diag-roundtrip/) | L73-L75 | formalized | — |
| `theorem` | [diag_to_linear_injective](/verify/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear-injective/) | L78-L80 | formalized | — |
| `theorem` | [linear_to_diag_injective](/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag-injective/) | L83-L85 | formalized | — |
| `def` | [allDiagonalAspects](/verify/taulib/docs/book-i-meta-logic-linear-discipline/all-diagonal-aspects/) | L88-L89 | defined | — |
| `def` | [allLinearAspects](/verify/taulib/docs/book-i-meta-logic-linear-discipline/all-linear-aspects/) | L92-L93 | defined | — |
| `theorem` | [diagonal_aspect_count](/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect-count/) | L96-L96 | formalized | — |
| `theorem` | [linear_aspect_count](/verify/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect-count/) | L99-L99 | formalized | — |
| `def` | [isRhoPure](/verify/taulib/docs/book-i-meta-logic-linear-discipline/is-rho-pure/) | L110-L113 | defined | — |
| `theorem` | [empty_is_rho_pure](/verify/taulib/docs/book-i-meta-logic-linear-discipline/empty-is-rho-pure/) | L116-L116 | formalized | — |
| `theorem` | [rho_pure_compose](/verify/taulib/docs/book-i-meta-logic-linear-discipline/rho-pure-compose/) | L121-L133 | formalized | — |
| `theorem` | [cut_elimination_additive](/verify/taulib/docs/book-i-meta-logic-linear-discipline/cut-elimination-additive/) | L138-L141 | formalized | — |
| `theorem` | [identity_zero_resource](/verify/taulib/docs/book-i-meta-logic-linear-discipline/identity-zero-resource/) | L144-L146 | formalized | — |
| `inductive` | [ResourceState](/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-state/) | L157-L164 | defined | — |
| `def` | [truth4_to_resource](/verify/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource/) | L167-L171 | defined | — |
| `def` | [resource_to_truth4](/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4/) | L174-L178 | defined | — |
| `theorem` | [truth4_resource_roundtrip](/verify/taulib/docs/book-i-meta-logic-linear-discipline/truth4-resource-roundtrip/) | L181-L183 | formalized | — |
| `theorem` | [resource_truth4_roundtrip](/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-truth4-roundtrip/) | L186-L188 | formalized | — |
| `theorem` | [truth4_to_resource_injective](/verify/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource-injective/) | L191-L193 | formalized | — |
| `theorem` | [resource_to_truth4_injective](/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4-injective/) | L196-L198 | formalized | — |
| `theorem` | [overdetermined_is_contraction_artifact](/verify/taulib/docs/book-i-meta-logic-linear-discipline/overdetermined-is-contraction-artifact/) | L207-L208 | formalized | — |
| `theorem` | [underdetermined_is_weakening_artifact](/verify/taulib/docs/book-i-meta-logic-linear-discipline/underdetermined-is-weakening-artifact/) | L213-L214 | formalized | — |
| `theorem` | [present_is_T](/verify/taulib/docs/book-i-meta-logic-linear-discipline/present-is-t/) | L217-L218 | formalized | — |
| `theorem` | [absent_is_F](/verify/taulib/docs/book-i-meta-logic-linear-discipline/absent-is-f/) | L221-L222 | formalized | — |
| `def` | [allResourceStates](/verify/taulib/docs/book-i-meta-logic-linear-discipline/all-resource-states/) | L225-L226 | defined | — |
| `theorem` | [resource_state_count](/verify/taulib/docs/book-i-meta-logic-linear-discipline/resource-state-count/) | L229-L229 | formalized | — |
| `theorem` | [contraction_produces_overdetermined](/verify/taulib/docs/book-i-meta-logic-linear-discipline/contraction-produces-overdetermined/) | L238-L241 | formalized | — |
| `theorem` | [weakening_produces_underdetermined](/verify/taulib/docs/book-i-meta-logic-linear-discipline/weakening-produces-underdetermined/) | L246-L249 | formalized | — |
| `structure` | [DiagonalLinearCorrespondence](/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence/) | L264-L280 | defined | `I.T37` |
| `theorem` | [diagonal_linear_correspondence](/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence-l283/) | L283-L291 | formalized | — |
| `eval` | [#eval L298](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l298/) | L298-L298 | computed | — |
| `eval` | [#eval L299](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l299/) | L299-L299 | computed | — |
| `eval` | [#eval L300](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l300/) | L300-L300 | computed | — |
| `eval` | [#eval L301](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l301/) | L301-L301 | computed | — |
| `eval` | [#eval L302](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l302/) | L302-L302 | computed | — |
| `eval` | [#eval L303](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l303/) | L303-L303 | computed | — |
| `eval` | [#eval L306](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l306/) | L306-L306 | computed | — |
| `eval` | [#eval L307](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l307/) | L307-L307 | computed | — |
| `eval` | [#eval L308](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l308/) | L308-L308 | computed | — |
| `eval` | [#eval L309](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l309/) | L309-L309 | computed | — |
| `eval` | [#eval L310](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l310/) | L310-L310 | computed | — |
| `eval` | [#eval L311](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l311/) | L311-L311 | computed | — |
| `eval` | [#eval L314](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l314/) | L314-L314 | computed | — |
| `eval` | [#eval L315](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l315/) | L315-L315 | computed | — |
| `eval` | [#eval L316](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l316/) | L316-L316 | computed | — |
| `eval` | [#eval L319](/verify/taulib/docs/book-i-meta-logic-linear-discipline/eval-l319/) | L319-L321 | computed | — |

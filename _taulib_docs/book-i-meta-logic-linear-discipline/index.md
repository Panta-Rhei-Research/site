---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "permalink": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/",
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
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect/",
      "source_line_start": 36,
      "source_line_end": 40,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "DiagonalAspect",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect/",
      "source_line_start": 43,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "diag_to_linear",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear/",
      "source_line_start": 56,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "linear_to_diag",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag/",
      "source_line_start": 62,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diag_linear_roundtrip",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diag-linear-roundtrip/",
      "source_line_start": 68,
      "source_line_end": 70,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "linear_diag_roundtrip",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-diag-roundtrip/",
      "source_line_start": 73,
      "source_line_end": 75,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diag_to_linear_injective",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear-injective/",
      "source_line_start": 78,
      "source_line_end": 80,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "linear_to_diag_injective",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag-injective/",
      "source_line_start": 83,
      "source_line_end": 85,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allDiagonalAspects",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/all-diagonal-aspects/",
      "source_line_start": 88,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allLinearAspects",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/all-linear-aspects/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diagonal_aspect_count",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect-count/",
      "source_line_start": 96,
      "source_line_end": 96,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "linear_aspect_count",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect-count/",
      "source_line_start": 99,
      "source_line_end": 99,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "isRhoPure",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/is-rho-pure/",
      "source_line_start": 110,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "empty_is_rho_pure",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/empty-is-rho-pure/",
      "source_line_start": 116,
      "source_line_end": 116,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rho_pure_compose",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/rho-pure-compose/",
      "source_line_start": 121,
      "source_line_end": 133,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cut_elimination_additive",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/cut-elimination-additive/",
      "source_line_start": 138,
      "source_line_end": 141,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "identity_zero_resource",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/identity-zero-resource/",
      "source_line_start": 144,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ResourceState",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-state/",
      "source_line_start": 157,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "truth4_to_resource",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource/",
      "source_line_start": 167,
      "source_line_end": 171,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "resource_to_truth4",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4/",
      "source_line_start": 174,
      "source_line_end": 178,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth4_resource_roundtrip",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/truth4-resource-roundtrip/",
      "source_line_start": 181,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resource_truth4_roundtrip",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-truth4-roundtrip/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truth4_to_resource_injective",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource-injective/",
      "source_line_start": 191,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resource_to_truth4_injective",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4-injective/",
      "source_line_start": 196,
      "source_line_end": 198,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "overdetermined_is_contraction_artifact",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/overdetermined-is-contraction-artifact/",
      "source_line_start": 207,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "underdetermined_is_weakening_artifact",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/underdetermined-is-weakening-artifact/",
      "source_line_start": 213,
      "source_line_end": 214,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "present_is_T",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/present-is-t/",
      "source_line_start": 217,
      "source_line_end": 218,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "absent_is_F",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/absent-is-f/",
      "source_line_start": 221,
      "source_line_end": 222,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allResourceStates",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/all-resource-states/",
      "source_line_start": 225,
      "source_line_end": 226,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "resource_state_count",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-state-count/",
      "source_line_start": 229,
      "source_line_end": 229,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "contraction_produces_overdetermined",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/contraction-produces-overdetermined/",
      "source_line_start": 238,
      "source_line_end": 241,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weakening_produces_underdetermined",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/weakening-produces-underdetermined/",
      "source_line_start": 246,
      "source_line_end": 249,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DiagonalLinearCorrespondence",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence/",
      "source_line_start": 264,
      "source_line_end": 280,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.T37"
      ]
    },
    {
      "kind": "theorem",
      "name": "diagonal_linear_correspondence",
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence-l283/",
      "source_line_start": 283,
      "source_line_end": 291,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l298/",
      "source_line_start": 298,
      "source_line_end": 298,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l299/",
      "source_line_start": 299,
      "source_line_end": 299,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l301/",
      "source_line_start": 301,
      "source_line_end": 301,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l302/",
      "source_line_start": 302,
      "source_line_end": 302,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l303/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l307/",
      "source_line_start": 307,
      "source_line_end": 307,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l308/",
      "source_line_start": 308,
      "source_line_end": 308,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l309/",
      "source_line_start": 309,
      "source_line_end": 309,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 310,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l311/",
      "source_line_start": 311,
      "source_line_end": 311,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l315/",
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
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l316/",
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
      "url": "/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 321,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [LinearAspect](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect/) | L36-L40 | type/data schema | type/data schema | — |
| `inductive` | [DiagonalAspect](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect/) | L43-L49 | type/data schema | type/data schema | — |
| `def` | [diag_to_linear](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear/) | L56-L59 | definition | definition | — |
| `def` | [linear_to_diag](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag/) | L62-L65 | definition | definition | — |
| `theorem` | [diag_linear_roundtrip](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diag-linear-roundtrip/) | L68-L70 | proof obligation | formal proof obligation checked | — |
| `theorem` | [linear_diag_roundtrip](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-diag-roundtrip/) | L73-L75 | proof obligation | formal proof obligation checked | — |
| `theorem` | [diag_to_linear_injective](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diag-to-linear-injective/) | L78-L80 | proof obligation | formal proof obligation checked | — |
| `theorem` | [linear_to_diag_injective](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-to-diag-injective/) | L83-L85 | proof obligation | formal proof obligation checked | — |
| `def` | [allDiagonalAspects](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/all-diagonal-aspects/) | L88-L89 | data/computed value | data/computed value | — |
| `def` | [allLinearAspects](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/all-linear-aspects/) | L92-L93 | data/computed value | data/computed value | — |
| `theorem` | [diagonal_aspect_count](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-aspect-count/) | L96-L96 | proof obligation | formal proof obligation checked | — |
| `theorem` | [linear_aspect_count](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/linear-aspect-count/) | L99-L99 | proof obligation | formal proof obligation checked | — |
| `def` | [isRhoPure](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/is-rho-pure/) | L110-L113 | definition | definition | — |
| `theorem` | [empty_is_rho_pure](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/empty-is-rho-pure/) | L116-L116 | proof obligation | formal proof obligation checked | — |
| `theorem` | [rho_pure_compose](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/rho-pure-compose/) | L121-L133 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cut_elimination_additive](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/cut-elimination-additive/) | L138-L141 | proof obligation | formal proof obligation checked | — |
| `theorem` | [identity_zero_resource](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/identity-zero-resource/) | L144-L146 | proof obligation | formal proof obligation checked | — |
| `inductive` | [ResourceState](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-state/) | L157-L164 | type/data schema | type/data schema | — |
| `def` | [truth4_to_resource](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource/) | L167-L171 | definition | definition | — |
| `def` | [resource_to_truth4](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4/) | L174-L178 | definition | definition | — |
| `theorem` | [truth4_resource_roundtrip](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/truth4-resource-roundtrip/) | L181-L183 | proof obligation | formal proof obligation checked | — |
| `theorem` | [resource_truth4_roundtrip](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-truth4-roundtrip/) | L186-L188 | proof obligation | formal proof obligation checked | — |
| `theorem` | [truth4_to_resource_injective](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/truth4-to-resource-injective/) | L191-L193 | proof obligation | formal proof obligation checked | — |
| `theorem` | [resource_to_truth4_injective](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-to-truth4-injective/) | L196-L198 | proof obligation | formal proof obligation checked | — |
| `theorem` | [overdetermined_is_contraction_artifact](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/overdetermined-is-contraction-artifact/) | L207-L208 | proof obligation | formal proof obligation checked | — |
| `theorem` | [underdetermined_is_weakening_artifact](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/underdetermined-is-weakening-artifact/) | L213-L214 | proof obligation | formal proof obligation checked | — |
| `theorem` | [present_is_T](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/present-is-t/) | L217-L218 | proof obligation | formal proof obligation checked | — |
| `theorem` | [absent_is_F](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/absent-is-f/) | L221-L222 | proof obligation | formal proof obligation checked | — |
| `def` | [allResourceStates](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/all-resource-states/) | L225-L226 | data/computed value | data/computed value | — |
| `theorem` | [resource_state_count](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/resource-state-count/) | L229-L229 | proof obligation | formal proof obligation checked | — |
| `theorem` | [contraction_produces_overdetermined](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/contraction-produces-overdetermined/) | L238-L241 | proof obligation | formal proof obligation checked | — |
| `theorem` | [weakening_produces_underdetermined](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/weakening-produces-underdetermined/) | L246-L249 | proof obligation | formal proof obligation checked | — |
| `structure` | [DiagonalLinearCorrespondence](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence/) | L264-L280 | type/data schema | type/data schema | `I.T37` |
| `theorem` | [diagonal_linear_correspondence](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence-l283/) | L283-L291 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L298](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l298/) | L298-L298 | computed check | computed check | — |
| `eval` | [#eval L299](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l299/) | L299-L299 | computed check | computed check | — |
| `eval` | [#eval L300](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l300/) | L300-L300 | computed check | computed check | — |
| `eval` | [#eval L301](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l301/) | L301-L301 | computed check | computed check | — |
| `eval` | [#eval L302](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l302/) | L302-L302 | computed check | computed check | — |
| `eval` | [#eval L303](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l303/) | L303-L303 | computed check | computed check | — |
| `eval` | [#eval L306](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l306/) | L306-L306 | computed check | computed check | — |
| `eval` | [#eval L307](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l307/) | L307-L307 | computed check | computed check | — |
| `eval` | [#eval L308](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l308/) | L308-L308 | computed check | computed check | — |
| `eval` | [#eval L309](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l309/) | L309-L309 | computed check | computed check | — |
| `eval` | [#eval L310](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l310/) | L310-L310 | computed check | computed check | — |
| `eval` | [#eval L311](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l311/) | L311-L311 | computed check | computed check | — |
| `eval` | [#eval L314](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l314/) | L314-L314 | computed check | computed check | — |
| `eval` | [#eval L315](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l315/) | L315-L315 | computed check | computed check | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l316/) | L316-L316 | computed check | computed check | — |
| `eval` | [#eval L319](/corpus/taulib/docs/book-i-meta-logic-linear-discipline/eval-l319/) | L319-L321 | computed check | computed check | — |

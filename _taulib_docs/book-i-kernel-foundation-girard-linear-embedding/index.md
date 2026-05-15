---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "permalink": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.KernelFoundation.GirardLinearEmbedding`.",
  "module_name": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "module_slug": "book-i-kernel-foundation-girard-linear-embedding",
  "book": "BookI",
  "family": "KernelFoundation",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean",
  "sha256": "69611ed8bdb345e2ffb570803cc9eef33f1d5cd15dfb081e3b6c177908b96c9d",
  "imports": [
    "TauLib.BookI.KernelFoundation.H8KernelSynthesis"
  ],
  "imported_by": [],
  "registry_ids": [
    "I.D78",
    "I.T175",
    "I.T37"
  ],
  "declaration_counts": {
    "inductive": 3,
    "structure": 1,
    "def": 4,
    "theorem": 5,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "Formula",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/formula/",
      "source_line_start": 115,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Sequent",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/sequent/",
      "source_line_start": 124,
      "source_line_end": 127,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "StructuralRule",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/structural-rule/",
      "source_line_start": 134,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "StructuralRule.admittedInLinear",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/admitted-in-linear/",
      "source_line_start": 142,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "allStructuralRules",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/all-structural-rules/",
      "source_line_start": 157,
      "source_line_end": 158,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "structural_rule_count",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/structural-rule-count/",
      "source_line_start": 160,
      "source_line_end": 160,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "linear_fragment_signature",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/linear-fragment-signature/",
      "source_line_start": 164,
      "source_line_end": 166,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ConnectiveTier",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/connective-tier/",
      "source_line_start": 173,
      "source_line_end": 176,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Formula.tier",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/tier/",
      "source_line_start": 179,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "cutSequent",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/cut-sequent/",
      "source_line_start": 206,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cut_produces_sequent_when_applicable",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/cut-produces-sequent-when-applicable/",
      "source_line_start": 224,
      "source_line_end": 231,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diagonal_linear_correspondence_witness",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/diagonal-linear-correspondence-witness/",
      "source_line_start": 247,
      "source_line_end": 252,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h8_girard_linear_embedding_synthesis",
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/h8-girard-linear-embedding-synthesis/",
      "source_line_start": 273,
      "source_line_end": 293,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l299/",
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
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l300/",
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
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l301/",
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
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l302/",
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
      "url": "/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l303/",
      "source_line_start": 303,
      "source_line_end": 305,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean",
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
- Source path: [`TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`
- SHA-256: `69611ed8bdb345e2ffb570803cc9eef33f1d5cd15dfb081e3b6c177908b96c9d`

## Registry Links

- `I.D78` — Diagonal-Linear Correspondence
- `I.T37` — Diagonal-Linear Correspondence

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.KernelFoundation.H8KernelSynthesis`

## Imported By

- No TauLib module in the snapshot imports this module.

## Declaration Counts

- `def`: 4
- `eval`: 5
- `inductive`: 3
- `structure`: 1
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [Formula](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/formula/) | L115-L121 | type/data schema | type/data schema | — |
| `structure` | [Sequent](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/sequent/) | L124-L127 | type/data schema | type/data schema | — |
| `inductive` | [StructuralRule](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/structural-rule/) | L134-L138 | type/data schema | type/data schema | — |
| `def` | [StructuralRule.admittedInLinear](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/admitted-in-linear/) | L142-L154 | definition | definition | — |
| `def` | [allStructuralRules](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/all-structural-rules/) | L157-L158 | data/computed value | data/computed value | — |
| `theorem` | [structural_rule_count](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/structural-rule-count/) | L160-L160 | proof obligation | formal proof obligation checked | — |
| `theorem` | [linear_fragment_signature](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/linear-fragment-signature/) | L164-L166 | proof obligation | formal proof obligation checked | — |
| `inductive` | [ConnectiveTier](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/connective-tier/) | L173-L176 | type/data schema | type/data schema | — |
| `def` | [Formula.tier](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/tier/) | L179-L196 | definition | definition | — |
| `def` | [cutSequent](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/cut-sequent/) | L206-L210 | definition | definition | — |
| `theorem` | [cut_produces_sequent_when_applicable](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/cut-produces-sequent-when-applicable/) | L224-L231 | proof obligation | formal proof obligation checked | — |
| `theorem` | [diagonal_linear_correspondence_witness](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/diagonal-linear-correspondence-witness/) | L247-L252 | proof obligation | formal proof obligation checked | — |
| `theorem` | [h8_girard_linear_embedding_synthesis](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/h8-girard-linear-embedding-synthesis/) | L273-L293 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L299](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l299/) | L299-L299 | computed check | computed check | — |
| `eval` | [#eval L300](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l300/) | L300-L300 | computed check | computed check | — |
| `eval` | [#eval L301](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l301/) | L301-L301 | computed check | computed check | — |
| `eval` | [#eval L302](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l302/) | L302-L302 | computed check | computed check | — |
| `eval` | [#eval L303](/corpus/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/eval-l303/) | L303-L305 | computed check | computed check | — |

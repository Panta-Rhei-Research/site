---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "permalink": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_slug": "book-v-orthodox-correspondence-map",
  "book": "BookV",
  "family": "Orthodox",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Orthodox/CorrespondenceMap.lean",
  "sha256": "2740558c3108d71aafb0d8d6bc3cf755a7844cee3207430d0098413714ed75c3",
  "imports": [
    "TauLib.BookV.GravityField.ClosingIdentity"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Orthodox.EmergentGeometry"
  ],
  "registry_ids": [
    "V.D185",
    "V.D186",
    "V.D187",
    "V.R252",
    "V.R253",
    "V.R254",
    "V.R255",
    "V.R256",
    "V.R257",
    "V.R258",
    "V.R259",
    "V.T121"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 4,
    "def": 4,
    "theorem": 9,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ArtifactStatus",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/artifact-status/",
      "source_line_start": 70,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "StructuralArtifact",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/structural-artifact/",
      "source_line_start": 89,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D185"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_artifacts",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/canonical-artifacts/",
      "source_line_start": 103,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "canonical_artifact_count",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/canonical-artifact-count/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "OntologicalLayer",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/ontological-layer/",
      "source_line_start": 139,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "OnticReadoutLayers",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/ontic-readout-layers/",
      "source_line_start": 153,
      "source_line_end": 162,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D186"
      ]
    },
    {
      "kind": "def",
      "name": "two_layers",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/two-layers/",
      "source_line_start": 165,
      "source_line_end": 167,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReadoutProtocol",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/readout-protocol/",
      "source_line_start": 180,
      "source_line_end": 191,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D187"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_protocol",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/canonical-protocol/",
      "source_line_start": 194,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CorrespondenceFunctor",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor/",
      "source_line_start": 216,
      "source_line_end": 225,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T121"
      ]
    },
    {
      "kind": "def",
      "name": "correspondence_functor",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-l228/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correspondence_functor_well_defined",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-well-defined/",
      "source_line_start": 231,
      "source_line_end": 232,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correspondence_functor_functorial",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-functorial/",
      "source_line_start": 235,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correspondence_functor_not_surjective",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-not-surjective/",
      "source_line_start": 239,
      "source_line_end": 240,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correspondence_functor_not_injective",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-not-injective/",
      "source_line_start": 243,
      "source_line_end": 244,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "correspondence_functor_props",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-props/",
      "source_line_start": 247,
      "source_line_end": 252,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T121"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_counterpart_count",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/no-counterpart-count/",
      "source_line_start": 262,
      "source_line_end": 263,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R252"
      ]
    },
    {
      "kind": "theorem",
      "name": "orthodox_not_wrong",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/orthodox-not-wrong/",
      "source_line_start": 268,
      "source_line_end": 270,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R255"
      ]
    },
    {
      "kind": "theorem",
      "name": "vacuum_catastrophe_diagnostic",
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/vacuum-catastrophe-diagnostic/",
      "source_line_start": 275,
      "source_line_end": 277,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R257"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l306/",
      "source_line_start": 306,
      "source_line_end": 306,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R253",
        "V.R254",
        "V.R256",
        "V.R258",
        "V.R259"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l307/",
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
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l308/",
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
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l309/",
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
      "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l310/",
      "source_line_start": 310,
      "source_line_end": 312,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean",
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
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Orthodox/CorrespondenceMap.lean`
- SHA-256: `2740558c3108d71aafb0d8d6bc3cf755a7844cee3207430d0098413714ed75c3`

## Registry Links

- `V.D185` — Structural artifact
- `V.D186` — Ontic and readout layers
- `V.D187` — Readout interpretation protocol
- `V.R252` — Entries with ``No counterpart''
- `V.R253` — Preservation does not mean identity
- `V.R254` — The common thread
- `V.R255` — Orthodox physics is not wrong
- `V.R256` — Where tau adds value
- `V.R257` — The vacuum catastrophe as diagnostic
- `V.R258` — The analogy of cartography
- `V.R259` — Non-surjectivity is a feature
- `V.T121` — Properties of the correspondence functor

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.ClosingIdentity`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Orthodox.EmergentGeometry`

## Declaration Counts

- `def`: 4
- `eval`: 5
- `inductive`: 2
- `structure`: 4
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [ArtifactStatus](/corpus/taulib/docs/book-v-orthodox-correspondence-map/artifact-status/) | L70-L77 | type/data schema | type/data schema | — |
| `structure` | [StructuralArtifact](/corpus/taulib/docs/book-v-orthodox-correspondence-map/structural-artifact/) | L89-L100 | type/data schema | type/data schema | `V.D185` |
| `def` | [canonical_artifacts](/corpus/taulib/docs/book-v-orthodox-correspondence-map/canonical-artifacts/) | L103-L128 | data/computed value | data/computed value | — |
| `theorem` | [canonical_artifact_count](/corpus/taulib/docs/book-v-orthodox-correspondence-map/canonical-artifact-count/) | L131-L132 | proof obligation | formal proof obligation checked | — |
| `inductive` | [OntologicalLayer](/corpus/taulib/docs/book-v-orthodox-correspondence-map/ontological-layer/) | L139-L144 | type/data schema | type/data schema | — |
| `structure` | [OnticReadoutLayers](/corpus/taulib/docs/book-v-orthodox-correspondence-map/ontic-readout-layers/) | L153-L162 | type/data schema | type/data schema | `V.D186` |
| `def` | [two_layers](/corpus/taulib/docs/book-v-orthodox-correspondence-map/two-layers/) | L165-L167 | definition | definition | — |
| `structure` | [ReadoutProtocol](/corpus/taulib/docs/book-v-orthodox-correspondence-map/readout-protocol/) | L180-L191 | type/data schema | type/data schema | `V.D187` |
| `def` | [canonical_protocol](/corpus/taulib/docs/book-v-orthodox-correspondence-map/canonical-protocol/) | L194-L196 | definition | definition | — |
| `structure` | [CorrespondenceFunctor](/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor/) | L216-L225 | type/data schema | type/data schema | `V.T121` |
| `def` | [correspondence_functor](/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-l228/) | L228-L228 | definition | definition | — |
| `theorem` | [correspondence_functor_well_defined](/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-well-defined/) | L231-L232 | proof obligation | formal proof obligation checked | — |
| `theorem` | [correspondence_functor_functorial](/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-functorial/) | L235-L236 | proof obligation | formal proof obligation checked | — |
| `theorem` | [correspondence_functor_not_surjective](/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-not-surjective/) | L239-L240 | proof obligation | formal proof obligation checked | — |
| `theorem` | [correspondence_functor_not_injective](/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-not-injective/) | L243-L244 | proof obligation | formal proof obligation checked | — |
| `theorem` | [correspondence_functor_props](/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-props/) | L247-L252 | proof obligation | formal proof obligation checked | `V.T121` |
| `theorem` | [no_counterpart_count](/corpus/taulib/docs/book-v-orthodox-correspondence-map/no-counterpart-count/) | L262-L263 | proof obligation | formal proof obligation checked | `V.R252` |
| `theorem` | [orthodox_not_wrong](/corpus/taulib/docs/book-v-orthodox-correspondence-map/orthodox-not-wrong/) | L268-L270 | proof obligation | formal proof obligation checked | `V.R255` |
| `theorem` | [vacuum_catastrophe_diagnostic](/corpus/taulib/docs/book-v-orthodox-correspondence-map/vacuum-catastrophe-diagnostic/) | L275-L277 | proof obligation | formal proof obligation checked | `V.R257` |
| `eval` | [#eval L306](/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l306/) | L306-L306 | computed check | computed check | `V.R253`, `V.R254`, `V.R256`, `V.R258`, `V.R259` |
| `eval` | [#eval L307](/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l307/) | L307-L307 | computed check | computed check | — |
| `eval` | [#eval L308](/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l308/) | L308-L308 | computed check | computed check | — |
| `eval` | [#eval L309](/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l309/) | L309-L309 | computed check | computed check | — |
| `eval` | [#eval L310](/corpus/taulib/docs/book-v-orthodox-correspondence-map/eval-l310/) | L310-L312 | computed check | computed check | — |

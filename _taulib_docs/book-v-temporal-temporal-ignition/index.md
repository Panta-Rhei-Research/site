---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.TemporalIgnition",
  "permalink": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Temporal.TemporalIgnition`.",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_slug": "book-v-temporal-temporal-ignition",
  "book": "BookV",
  "family": "Temporal",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Temporal/TemporalIgnition.lean",
  "sha256": "15e96d73480c14d7fcd25c2e60a33236ad248f3c0848f25fba2567330f07acf0",
  "imports": [
    "TauLib.BookV.Temporal.BaseCircle"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Temporal.HighEnergy"
  ],
  "registry_ids": [
    "V.D20",
    "V.D21",
    "V.D22",
    "V.D23",
    "V.P04",
    "V.T11",
    "V.T12"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 3,
    "def": 2,
    "theorem": 5,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "TemporalEpoch",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/temporal-epoch/",
      "source_line_start": 69,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D20"
      ]
    },
    {
      "kind": "structure",
      "name": "IgnitionDepth",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/ignition-depth/",
      "source_line_start": 90,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D21"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_ignition",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/canonical-ignition/",
      "source_line_start": 104,
      "source_line_end": 108,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "epoch_classification",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/epoch-classification/",
      "source_line_start": 115,
      "source_line_end": 118,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_epochs_nonempty",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/three-epochs-nonempty/",
      "source_line_start": 132,
      "source_line_end": 143,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T11"
      ]
    },
    {
      "kind": "theorem",
      "name": "pre_temporal_no_labels",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/pre-temporal-no-labels/",
      "source_line_start": 156,
      "source_line_end": 159,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P04"
      ]
    },
    {
      "kind": "structure",
      "name": "NowHypersurface",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/now-hypersurface/",
      "source_line_start": 171,
      "source_line_end": 178,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D22"
      ]
    },
    {
      "kind": "theorem",
      "name": "current_depth_exceeds_ignition",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/current-depth-exceeds-ignition/",
      "source_line_start": 189,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T12"
      ]
    },
    {
      "kind": "structure",
      "name": "CoherenceHorizon",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/coherence-horizon/",
      "source_line_start": 207,
      "source_line_end": 214,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D23"
      ]
    },
    {
      "kind": "theorem",
      "name": "epoch_exhaust",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/epoch-exhaust/",
      "source_line_start": 221,
      "source_line_end": 223,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_is_stable",
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/temporal-is-stable/",
      "source_line_start": 226,
      "source_line_end": 228,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l236/",
      "source_line_start": 236,
      "source_line_end": 236,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l237/",
      "source_line_start": 237,
      "source_line_end": 237,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l239/",
      "source_line_start": 239,
      "source_line_end": 241,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean",
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
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Temporal/TemporalIgnition.lean`
- SHA-256: `15e96d73480c14d7fcd25c2e60a33236ad248f3c0848f25fba2567330f07acf0`

## Registry Links

- `V.D20` — Three Temporal Epochs
- `V.D21` — Ignition Depth
- `V.D22` — Sigma-Now Hypersurface
- `V.D23` — Coherence Horizon
- `V.P04` — Pre-Temporal Indistinguishability
- `V.T11` — Epoch Existence Theorem
- `V.T12` — Now-Within-Epoch Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Temporal.BaseCircle`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Temporal.HighEnergy`

## Declaration Counts

- `def`: 2
- `eval`: 6
- `inductive`: 1
- `structure`: 3
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [TemporalEpoch](/corpus/taulib/docs/book-v-temporal-temporal-ignition/temporal-epoch/) | L69-L79 | type/data schema | type/data schema | `V.D20` |
| `structure` | [IgnitionDepth](/corpus/taulib/docs/book-v-temporal-temporal-ignition/ignition-depth/) | L90-L99 | type/data schema | type/data schema | `V.D21` |
| `def` | [canonical_ignition](/corpus/taulib/docs/book-v-temporal-temporal-ignition/canonical-ignition/) | L104-L108 | definition | definition | — |
| `def` | [epoch_classification](/corpus/taulib/docs/book-v-temporal-temporal-ignition/epoch-classification/) | L115-L118 | data/computed value | data/computed value | — |
| `theorem` | [three_epochs_nonempty](/corpus/taulib/docs/book-v-temporal-temporal-ignition/three-epochs-nonempty/) | L132-L143 | proof obligation | formal proof obligation checked | `V.T11` |
| `theorem` | [pre_temporal_no_labels](/corpus/taulib/docs/book-v-temporal-temporal-ignition/pre-temporal-no-labels/) | L156-L159 | proof obligation | formal proof obligation checked | `V.P04` |
| `structure` | [NowHypersurface](/corpus/taulib/docs/book-v-temporal-temporal-ignition/now-hypersurface/) | L171-L178 | type/data schema | type/data schema | `V.D22` |
| `theorem` | [current_depth_exceeds_ignition](/corpus/taulib/docs/book-v-temporal-temporal-ignition/current-depth-exceeds-ignition/) | L189-L191 | proof obligation | formal proof obligation checked | `V.T12` |
| `structure` | [CoherenceHorizon](/corpus/taulib/docs/book-v-temporal-temporal-ignition/coherence-horizon/) | L207-L214 | type/data schema | type/data schema | `V.D23` |
| `theorem` | [epoch_exhaust](/corpus/taulib/docs/book-v-temporal-temporal-ignition/epoch-exhaust/) | L221-L223 | proof obligation | formal proof obligation checked | — |
| `theorem` | [temporal_is_stable](/corpus/taulib/docs/book-v-temporal-temporal-ignition/temporal-is-stable/) | L226-L228 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L234](/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l234/) | L234-L234 | computed check | computed check | — |
| `eval` | [#eval L235](/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l235/) | L235-L235 | computed check | computed check | — |
| `eval` | [#eval L236](/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l236/) | L236-L236 | computed check | computed check | — |
| `eval` | [#eval L237](/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l237/) | L237-L237 | computed check | computed check | — |
| `eval` | [#eval L238](/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l238/) | L238-L238 | computed check | computed check | — |
| `eval` | [#eval L239](/corpus/taulib/docs/book-v-temporal-temporal-ignition/eval-l239/) | L239-L241 | computed check | computed check | — |

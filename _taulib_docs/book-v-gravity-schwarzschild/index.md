---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Gravity.Schwarzschild",
  "permalink": "/corpus/taulib/docs/book-v-gravity-schwarzschild/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Gravity.Schwarzschild`.",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_slug": "book-v-gravity-schwarzschild",
  "book": "BookV",
  "family": "Gravity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Gravity/Schwarzschild.lean",
  "sha256": "91f2a747c88e09439937c4b0c1e7cbd1b73da7d160b76b25776a978f6027c991",
  "imports": [
    "TauLib.BookV.Gravity.EinsteinEquation"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Gravity.BHTopoModes",
    "TauLib.BookV.GravityField.TauSchwarzschild",
    "TauLib.BookV.Temporal.DistanceLadder"
  ],
  "registry_ids": [
    "V.D07",
    "V.D08",
    "V.D09",
    "V.R02",
    "V.T03"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 4,
    "inductive": 1,
    "theorem": 7,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BHMassIndex",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/bhmass-index/",
      "source_line_start": 81,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D07"
      ]
    },
    {
      "kind": "def",
      "name": "BHMassIndex.toFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/to-float/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SchwarzschildRelation",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/schwarzschild-relation/",
      "source_line_start": 113,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D08"
      ]
    },
    {
      "kind": "def",
      "name": "SchwarzschildRelation.radiusFloat",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/radius-float/",
      "source_line_start": 131,
      "source_line_end": 132,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoShrinkProperty",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/no-shrink-property/",
      "source_line_start": 147,
      "source_line_end": 152,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T03"
      ]
    },
    {
      "kind": "inductive",
      "name": "BHEvolutionMode",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/bhevolution-mode/",
      "source_line_start": 166,
      "source_line_end": 177,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D09"
      ]
    },
    {
      "kind": "def",
      "name": "BHEvolutionMode.preserves_mass",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/preserves-mass/",
      "source_line_start": 184,
      "source_line_end": 187,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "BHEvolutionMode.is_internal",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/is-internal/",
      "source_line_start": 190,
      "source_line_end": 193,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ChandrasekharLimit",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/chandrasekhar-limit/",
      "source_line_start": 210,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R02"
      ]
    },
    {
      "kind": "theorem",
      "name": "three_evolution_modes",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/three-evolution-modes/",
      "source_line_start": 224,
      "source_line_end": 226,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "fusion_increases_mass",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/fusion-increases-mass/",
      "source_line_start": 229,
      "source_line_end": 230,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ringdown_preserves_mass",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/ringdown-preserves-mass/",
      "source_line_start": 233,
      "source_line_end": 234,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "transport_preserves_mass",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/transport-preserves-mass/",
      "source_line_start": 237,
      "source_line_end": 238,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ringdown_internal",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/ringdown-internal/",
      "source_line_start": 241,
      "source_line_end": 242,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_shrink_requires_maturity",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/no-shrink-requires-maturity/",
      "source_line_start": 245,
      "source_line_end": 246,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "schwarzschild_linear",
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/schwarzschild-linear/",
      "source_line_start": 250,
      "source_line_end": 253,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/eval-l260/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/eval-l261/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-schwarzschild/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 264,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean",
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
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Gravity/Schwarzschild.lean`
- SHA-256: `91f2a747c88e09439937c4b0c1e7cbd1b73da7d160b76b25776a978f6027c991`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Gravity.EinsteinEquation`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Gravity.BHTopoModes`
- `TauLib.BookV.GravityField.TauSchwarzschild`
- `TauLib.BookV.Temporal.DistanceLadder`

## Declaration Counts

- `def`: 4
- `eval`: 3
- `inductive`: 1
- `structure`: 4
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [BHMassIndex](/corpus/taulib/docs/book-v-gravity-schwarzschild/bhmass-index/) | L81-L92 | type/data schema | type/data schema | `V.D07` |
| `def` | [BHMassIndex.toFloat](/corpus/taulib/docs/book-v-gravity-schwarzschild/to-float/) | L95-L96 | data/computed value | data/computed value | — |
| `structure` | [SchwarzschildRelation](/corpus/taulib/docs/book-v-gravity-schwarzschild/schwarzschild-relation/) | L113-L128 | type/data schema | type/data schema | `V.D08` |
| `def` | [SchwarzschildRelation.radiusFloat](/corpus/taulib/docs/book-v-gravity-schwarzschild/radius-float/) | L131-L132 | data/computed value | data/computed value | — |
| `structure` | [NoShrinkProperty](/corpus/taulib/docs/book-v-gravity-schwarzschild/no-shrink-property/) | L147-L152 | type/data schema | type/data schema | `V.T03` |
| `inductive` | [BHEvolutionMode](/corpus/taulib/docs/book-v-gravity-schwarzschild/bhevolution-mode/) | L166-L177 | type/data schema | type/data schema | `V.D09` |
| `def` | [BHEvolutionMode.preserves_mass](/corpus/taulib/docs/book-v-gravity-schwarzschild/preserves-mass/) | L184-L187 | definition | definition | — |
| `def` | [BHEvolutionMode.is_internal](/corpus/taulib/docs/book-v-gravity-schwarzschild/is-internal/) | L190-L193 | definition | definition | — |
| `structure` | [ChandrasekharLimit](/corpus/taulib/docs/book-v-gravity-schwarzschild/chandrasekhar-limit/) | L210-L217 | type/data schema | type/data schema | `V.R02` |
| `theorem` | [three_evolution_modes](/corpus/taulib/docs/book-v-gravity-schwarzschild/three-evolution-modes/) | L224-L226 | proof obligation | formal proof obligation checked | — |
| `theorem` | [fusion_increases_mass](/corpus/taulib/docs/book-v-gravity-schwarzschild/fusion-increases-mass/) | L229-L230 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ringdown_preserves_mass](/corpus/taulib/docs/book-v-gravity-schwarzschild/ringdown-preserves-mass/) | L233-L234 | proof obligation | formal proof obligation checked | — |
| `theorem` | [transport_preserves_mass](/corpus/taulib/docs/book-v-gravity-schwarzschild/transport-preserves-mass/) | L237-L238 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ringdown_internal](/corpus/taulib/docs/book-v-gravity-schwarzschild/ringdown-internal/) | L241-L242 | proof obligation | formal proof obligation checked | — |
| `theorem` | [no_shrink_requires_maturity](/corpus/taulib/docs/book-v-gravity-schwarzschild/no-shrink-requires-maturity/) | L245-L246 | proof obligation | formal proof obligation checked | — |
| `theorem` | [schwarzschild_linear](/corpus/taulib/docs/book-v-gravity-schwarzschild/schwarzschild-linear/) | L250-L253 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L260](/corpus/taulib/docs/book-v-gravity-schwarzschild/eval-l260/) | L260-L260 | computed check | computed check | — |
| `eval` | [#eval L261](/corpus/taulib/docs/book-v-gravity-schwarzschild/eval-l261/) | L261-L261 | computed check | computed check | — |
| `eval` | [#eval L262](/corpus/taulib/docs/book-v-gravity-schwarzschild/eval-l262/) | L262-L264 | computed check | computed check | — |

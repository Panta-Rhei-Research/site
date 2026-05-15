---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_slug": "book-v-astrophysics-binary-mergers-gw",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/BinaryMergersGW.lean",
  "sha256": "8f2162ed74a4fb56bb9ea932dd18cbbaf7693e876cc7c7ab7c351f641b0cb31b",
  "imports": [
    "TauLib.BookV.Astrophysics.AccretionJets"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.EHTReread"
  ],
  "registry_ids": [
    "V.D133",
    "V.D134",
    "V.D135",
    "V.D136",
    "V.P80",
    "V.P81",
    "V.R192",
    "V.R193",
    "V.R194",
    "V.R195",
    "V.T93",
    "V.T94"
  ],
  "declaration_counts": {
    "inductive": 2,
    "def": 7,
    "structure": 4,
    "theorem": 6,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "BinarySystemType",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/binary-system-type/",
      "source_line_start": 70,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D133"
      ]
    },
    {
      "kind": "def",
      "name": "BinarySystemType.canProduceKilonova",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/can-produce-kilonova/",
      "source_line_start": 82,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GWSignalData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gwsignal-data/",
      "source_line_start": 96,
      "source_line_end": 116,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D134"
      ]
    },
    {
      "kind": "theorem",
      "name": "chirp_mass_formula",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/chirp-mass-formula/",
      "source_line_start": 129,
      "source_line_end": 131,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T93"
      ]
    },
    {
      "kind": "theorem",
      "name": "orbital_decay_gw",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/orbital-decay-gw/",
      "source_line_start": 149,
      "source_line_end": 151,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P80"
      ]
    },
    {
      "kind": "inductive",
      "name": "MergerOutcome",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-outcome/",
      "source_line_start": 158,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D135"
      ]
    },
    {
      "kind": "structure",
      "name": "MergerOutcomeData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-outcome-data/",
      "source_line_start": 168,
      "source_line_end": 181,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_hair_after_merger",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/no-hair-after-merger/",
      "source_line_start": 193,
      "source_line_end": 195,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T94"
      ]
    },
    {
      "kind": "structure",
      "name": "KilonovaData",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/kilonova-data/",
      "source_line_start": 206,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D136"
      ]
    },
    {
      "kind": "theorem",
      "name": "merger_rate_population",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-rate-population/",
      "source_line_start": 231,
      "source_line_end": 233,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P81"
      ]
    },
    {
      "kind": "def",
      "name": "gw150914",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gw150914/",
      "source_line_start": 264,
      "source_line_end": 274,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gw170817_kilonova",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gw170817-kilonova/",
      "source_line_start": 277,
      "source_line_end": 282,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l284/",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l285/",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l286/",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GWEventComparison",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gwevent-comparison/",
      "source_line_start": 294,
      "source_line_end": 301,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gw_event_catalog",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gw-event-catalog/",
      "source_line_start": 304,
      "source_line_end": 312,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "t2_ringdown_ratio_x1000",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/t2-ringdown-ratio-x1000/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bbh_events_have_final_mass",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/bbh-events-have-final-mass/",
      "source_line_start": 318,
      "source_line_end": 320,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bns_no_ringdown",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/bns-no-ringdown/",
      "source_line_start": 323,
      "source_line_end": 325,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chirp_mass_consistency_remark",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/chirp-mass-consistency-remark/",
      "source_line_start": 328,
      "source_line_end": 330,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ligo_comparison_remark",
      "url": "/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/ligo-comparison-remark/",
      "source_line_start": 333,
      "source_line_end": 337,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/BinaryMergersGW.lean`
- SHA-256: `8f2162ed74a4fb56bb9ea932dd18cbbaf7693e876cc7c7ab7c351f641b0cb31b`

## Registry Links

- `V.D133` — Binary Coherent-Instance System
- `V.D134` — GW Boundary-Character Wave
- `V.D135` — Ringdown Readout
- `V.D136` — Standard Siren (tau)
- `V.P80` — GW Energy Flux
- `V.P81` — Merger Graviton Count
- `V.R192` — Why two polarizations, not six
- `V.R193` — LIGO GW150914 Re-Read
- `V.R194` — No-hair test via ringdown
- `V.R195` — Multi-Messenger GW170817
- `V.T93` — Chirp Mass from Boundary Holonomy
- `V.T94` — Ringdown Uniqueness Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.AccretionJets`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.EHTReread`

## Declaration Counts

- `def`: 7
- `eval`: 4
- `inductive`: 2
- `structure`: 4
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [BinarySystemType](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/binary-system-type/) | L70-L79 | type/data schema | type/data schema | `V.D133` |
| `def` | [BinarySystemType.canProduceKilonova](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/can-produce-kilonova/) | L82-L85 | definition | definition | — |
| `structure` | [GWSignalData](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gwsignal-data/) | L96-L116 | type/data schema | type/data schema | `V.D134` |
| `theorem` | [chirp_mass_formula](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/chirp-mass-formula/) | L129-L131 | proof obligation | formal proof obligation checked | `V.T93` |
| `theorem` | [orbital_decay_gw](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/orbital-decay-gw/) | L149-L151 | proof obligation | formal proof obligation checked | `V.P80` |
| `inductive` | [MergerOutcome](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-outcome/) | L158-L165 | type/data schema | type/data schema | `V.D135` |
| `structure` | [MergerOutcomeData](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-outcome-data/) | L168-L181 | type/data schema | type/data schema | — |
| `theorem` | [no_hair_after_merger](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/no-hair-after-merger/) | L193-L195 | proof obligation | formal proof obligation checked | `V.T94` |
| `structure` | [KilonovaData](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/kilonova-data/) | L206-L217 | type/data schema | type/data schema | `V.D136` |
| `theorem` | [merger_rate_population](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-rate-population/) | L231-L233 | proof obligation | formal proof obligation checked | `V.P81` |
| `def` | [gw150914](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gw150914/) | L264-L274 | definition | definition | — |
| `def` | [gw170817_kilonova](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gw170817-kilonova/) | L277-L282 | definition | definition | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l286/) | L286-L286 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/eval-l287/) | L287-L287 | computed check | computed check | — |
| `structure` | [GWEventComparison](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gwevent-comparison/) | L294-L301 | type/data schema | type/data schema | — |
| `def` | [gw_event_catalog](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/gw-event-catalog/) | L304-L312 | data/computed value | data/computed value | — |
| `def` | [t2_ringdown_ratio_x1000](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/t2-ringdown-ratio-x1000/) | L315-L315 | data/computed value | data/computed value | — |
| `theorem` | [bbh_events_have_final_mass](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/bbh-events-have-final-mass/) | L318-L320 | proof obligation | formal proof obligation checked | — |
| `theorem` | [bns_no_ringdown](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/bns-no-ringdown/) | L323-L325 | proof obligation | formal proof obligation checked | — |
| `def` | [chirp_mass_consistency_remark](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/chirp-mass-consistency-remark/) | L328-L330 | docstring/data record | docstring/data record | — |
| `def` | [ligo_comparison_remark](/corpus/taulib/docs/book-v-astrophysics-binary-mergers-gw/ligo-comparison-remark/) | L333-L337 | docstring/data record | docstring/data record | — |

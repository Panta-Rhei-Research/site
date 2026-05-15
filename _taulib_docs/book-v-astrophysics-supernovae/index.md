---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.Supernovae",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-supernovae/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.Supernovae`.",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_slug": "book-v-astrophysics-supernovae",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/Supernovae.lean",
  "sha256": "9faaa013e40be6b0ca5ae971ddf688885c868b330faf5f9282d509bba722d542",
  "imports": [
    "TauLib.BookV.Astrophysics.CompactObjects"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.AccretionJets"
  ],
  "registry_ids": [
    "V.D126",
    "V.D127",
    "V.D128",
    "V.P73",
    "V.P74",
    "V.P75",
    "V.P76",
    "V.R181",
    "V.R182",
    "V.R183",
    "V.R184",
    "V.T89"
  ],
  "declaration_counts": {
    "inductive": 3,
    "def": 5,
    "theorem": 6,
    "structure": 2,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "SupernovaType",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/supernova-type/",
      "source_line_start": 69,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D126"
      ]
    },
    {
      "kind": "def",
      "name": "SupernovaType.isCoreCollapse",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/is-core-collapse/",
      "source_line_start": 81,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SupernovaType.isThermonuclear",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/is-thermonuclear/",
      "source_line_start": 88,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "core_collapse_topology",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/core-collapse-topology/",
      "source_line_start": 102,
      "source_line_end": 104,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T89"
      ]
    },
    {
      "kind": "inductive",
      "name": "CollapsePhase",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/collapse-phase/",
      "source_line_start": 111,
      "source_line_end": 124,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CoreCollapseMechanism",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/core-collapse-mechanism/",
      "source_line_start": 129,
      "source_line_end": 142,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D127"
      ]
    },
    {
      "kind": "theorem",
      "name": "collapse_phases_complete",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/collapse-phases-complete/",
      "source_line_start": 145,
      "source_line_end": 149,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutrino_from_defect",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/neutrino-from-defect/",
      "source_line_start": 162,
      "source_line_end": 164,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P73"
      ]
    },
    {
      "kind": "theorem",
      "name": "type_ia_chandrasekhar",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/type-ia-chandrasekhar/",
      "source_line_start": 176,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P74"
      ]
    },
    {
      "kind": "inductive",
      "name": "ElementGroup",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/element-group/",
      "source_line_start": 185,
      "source_line_end": 194,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NucleosynthesisProducts",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/nucleosynthesis-products/",
      "source_line_start": 202,
      "source_line_end": 209,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D128"
      ]
    },
    {
      "kind": "def",
      "name": "cc_sn_products",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/cc-sn-products/",
      "source_line_start": 212,
      "source_line_end": 215,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ia_sn_products",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/ia-sn-products/",
      "source_line_start": 218,
      "source_line_end": 221,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "standardizable_candle",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/standardizable-candle/",
      "source_line_start": 233,
      "source_line_end": 235,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P75"
      ]
    },
    {
      "kind": "theorem",
      "name": "sn_rate_sfh",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/sn-rate-sfh/",
      "source_line_start": 244,
      "source_line_end": 246,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P76"
      ]
    },
    {
      "kind": "def",
      "name": "example_cc",
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/example-cc/",
      "source_line_start": 277,
      "source_line_end": 283,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l285/",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l286/",
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
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l288/",
      "source_line_start": 288,
      "source_line_end": 290,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/Supernovae.lean`
- SHA-256: `9faaa013e40be6b0ca5ae971ddf688885c868b330faf5f9282d509bba722d542`

## Registry Links

- `V.D126` — Topological Channel --- V.D59
- `V.D127` — Channel Reversal --- V.D60
- `V.D128` — r-Process as Rapid Charge Loading --- V.D61
- `V.P73` — Neutrino Heating Condition --- V.P37
- `V.P74` — Plateau Duration as Readout --- V.P38
- `V.P75` — Proto-Neutron Star Evolution --- V.P39
- `V.P76` — Birth Kick and Spin --- V.P40
- `V.R181` — The trigger is structural, not thermal
- `V.R182` — Explosion energy and the mass cut
- `V.R183` — Gold and the r-process
- `V.R184` — The carbon connection
- `V.T89` — Core Collapse Trigger --- V.T41

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.CompactObjects`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.AccretionJets`

## Declaration Counts

- `def`: 5
- `eval`: 4
- `inductive`: 3
- `structure`: 2
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [SupernovaType](/corpus/taulib/docs/book-v-astrophysics-supernovae/supernova-type/) | L69-L78 | type/data schema | type/data schema | `V.D126` |
| `def` | [SupernovaType.isCoreCollapse](/corpus/taulib/docs/book-v-astrophysics-supernovae/is-core-collapse/) | L81-L85 | definition | definition | — |
| `def` | [SupernovaType.isThermonuclear](/corpus/taulib/docs/book-v-astrophysics-supernovae/is-thermonuclear/) | L88-L90 | definition | definition | — |
| `theorem` | [core_collapse_topology](/corpus/taulib/docs/book-v-astrophysics-supernovae/core-collapse-topology/) | L102-L104 | proof obligation | formal proof obligation checked | `V.T89` |
| `inductive` | [CollapsePhase](/corpus/taulib/docs/book-v-astrophysics-supernovae/collapse-phase/) | L111-L124 | type/data schema | type/data schema | — |
| `structure` | [CoreCollapseMechanism](/corpus/taulib/docs/book-v-astrophysics-supernovae/core-collapse-mechanism/) | L129-L142 | type/data schema | type/data schema | `V.D127` |
| `theorem` | [collapse_phases_complete](/corpus/taulib/docs/book-v-astrophysics-supernovae/collapse-phases-complete/) | L145-L149 | proof obligation | formal proof obligation checked | — |
| `theorem` | [neutrino_from_defect](/corpus/taulib/docs/book-v-astrophysics-supernovae/neutrino-from-defect/) | L162-L164 | proof obligation | formal proof obligation checked | `V.P73` |
| `theorem` | [type_ia_chandrasekhar](/corpus/taulib/docs/book-v-astrophysics-supernovae/type-ia-chandrasekhar/) | L176-L178 | proof obligation | formal proof obligation checked | `V.P74` |
| `inductive` | [ElementGroup](/corpus/taulib/docs/book-v-astrophysics-supernovae/element-group/) | L185-L194 | type/data schema | type/data schema | — |
| `structure` | [NucleosynthesisProducts](/corpus/taulib/docs/book-v-astrophysics-supernovae/nucleosynthesis-products/) | L202-L209 | type/data schema | type/data schema | `V.D128` |
| `def` | [cc_sn_products](/corpus/taulib/docs/book-v-astrophysics-supernovae/cc-sn-products/) | L212-L215 | definition | definition | — |
| `def` | [ia_sn_products](/corpus/taulib/docs/book-v-astrophysics-supernovae/ia-sn-products/) | L218-L221 | definition | definition | — |
| `theorem` | [standardizable_candle](/corpus/taulib/docs/book-v-astrophysics-supernovae/standardizable-candle/) | L233-L235 | proof obligation | formal proof obligation checked | `V.P75` |
| `theorem` | [sn_rate_sfh](/corpus/taulib/docs/book-v-astrophysics-supernovae/sn-rate-sfh/) | L244-L246 | proof obligation | formal proof obligation checked | `V.P76` |
| `def` | [example_cc](/corpus/taulib/docs/book-v-astrophysics-supernovae/example-cc/) | L277-L283 | definition | definition | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l286/) | L286-L286 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l287/) | L287-L287 | computed check | computed check | — |
| `eval` | [#eval L288](/corpus/taulib/docs/book-v-astrophysics-supernovae/eval-l288/) | L288-L290 | computed check | computed check | — |

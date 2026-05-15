---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.BoundaryData",
  "permalink": "/corpus/taulib/docs/book-v-temporal-boundary-data/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Temporal.BoundaryData`.",
  "module_name": "TauLib.BookV.Temporal.BoundaryData",
  "module_slug": "book-v-temporal-boundary-data",
  "book": "BookV",
  "family": "Temporal",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Temporal/BoundaryData.lean",
  "sha256": "6114c65252dd374717a3c6f471f33b1befda4750256a66264e7cb78cea4f798e",
  "imports": [
    "TauLib.BookV.Temporal.DistanceLadder"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Temporal.CosmicAPI"
  ],
  "registry_ids": [
    "V.D36",
    "V.D37",
    "V.D38",
    "V.D39",
    "V.P07",
    "V.P08",
    "V.P09",
    "V.R47",
    "V.R48"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 6,
    "theorem": 11,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "RecombinationDepth",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/recombination-depth/",
      "source_line_start": 72,
      "source_line_end": 79,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D36"
      ]
    },
    {
      "kind": "structure",
      "name": "CMBSurface",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cmbsurface/",
      "source_line_start": 92,
      "source_line_end": 105,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D37"
      ]
    },
    {
      "kind": "def",
      "name": "CMBSurface.tempFloat",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/temp-float/",
      "source_line_start": 108,
      "source_line_end": 109,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutrinoDecoupling",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/neutrino-decoupling/",
      "source_line_start": 121,
      "source_line_end": 128,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D38"
      ]
    },
    {
      "kind": "structure",
      "name": "CnuBSurface",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cnu-bsurface/",
      "source_line_start": 142,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D39"
      ]
    },
    {
      "kind": "def",
      "name": "CnuBSurface.tempFloat",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/temp-float-l158/",
      "source_line_start": 158,
      "source_line_end": 159,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_cmb",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-cmb/",
      "source_line_start": 166,
      "source_line_end": 170,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_cnub",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-cnub/",
      "source_line_start": 173,
      "source_line_end": 175,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_recomb",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-recomb/",
      "source_line_start": 178,
      "source_line_end": 180,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_nu_decoupling",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-nu-decoupling/",
      "source_line_start": 183,
      "source_line_end": 185,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recomb_is_physical",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/recomb-is-physical/",
      "source_line_start": 192,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cmb_is_boundary_data",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cmb-is-boundary-data/",
      "source_line_start": 198,
      "source_line_end": 199,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P07"
      ]
    },
    {
      "kind": "theorem",
      "name": "cmb_standard_temperature",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cmb-standard-temperature/",
      "source_line_start": 203,
      "source_line_end": 204,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R47"
      ]
    },
    {
      "kind": "theorem",
      "name": "blackbody_maximizes_entropy",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/blackbody-maximizes-entropy/",
      "source_line_start": 209,
      "source_line_end": 210,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P08"
      ]
    },
    {
      "kind": "theorem",
      "name": "cnub_temperature_standard",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-temperature-standard/",
      "source_line_start": 213,
      "source_line_end": 216,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.R48"
      ]
    },
    {
      "kind": "theorem",
      "name": "cnub_three_species",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-three-species/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cnub_mass_constraint",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-mass-constraint/",
      "source_line_start": 225,
      "source_line_end": 227,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P09"
      ]
    },
    {
      "kind": "theorem",
      "name": "cnub_mass_value",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-mass-value/",
      "source_line_start": 230,
      "source_line_end": 231,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recomb_after_nu",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/recomb-after-nu/",
      "source_line_start": 234,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cmb_multipole_count",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/cmb-multipole-count/",
      "source_line_start": 239,
      "source_line_end": 240,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recomb_redshift",
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/recomb-redshift/",
      "source_line_start": 243,
      "source_line_end": 244,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l251/",
      "source_line_start": 251,
      "source_line_end": 251,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l260/",
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
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 267,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean",
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
- Source path: [`TauLib/BookV/Temporal/BoundaryData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/BoundaryData.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Temporal/BoundaryData.lean`
- SHA-256: `6114c65252dd374717a3c6f471f33b1befda4750256a66264e7cb78cea4f798e`

## Registry Links

- `V.D36` — Recombination orbit depth
- `V.D37` — CMB constraint surface
- `V.D38` — Neutrino decoupling orbit depth
- `V.D39` — CnuB echo surface
- `V.P07` — CMB multipoles as boundary characters
- `V.P08` — Blackbody as coherence equilibrium
- `V.P09` — CnuB mass constraint
- `V.R47` — No new information, new interpretation
- `V.R48` — No new prediction for T_mathrmC

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Temporal.DistanceLadder`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Temporal.CosmicAPI`

## Declaration Counts

- `def`: 6
- `eval`: 7
- `structure`: 4
- `theorem`: 11

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [RecombinationDepth](/corpus/taulib/docs/book-v-temporal-boundary-data/recombination-depth/) | L72-L79 | type/data schema | type/data schema | `V.D36` |
| `structure` | [CMBSurface](/corpus/taulib/docs/book-v-temporal-boundary-data/cmbsurface/) | L92-L105 | type/data schema | type/data schema | `V.D37` |
| `def` | [CMBSurface.tempFloat](/corpus/taulib/docs/book-v-temporal-boundary-data/temp-float/) | L108-L109 | data/computed value | data/computed value | — |
| `structure` | [NeutrinoDecoupling](/corpus/taulib/docs/book-v-temporal-boundary-data/neutrino-decoupling/) | L121-L128 | type/data schema | type/data schema | `V.D38` |
| `structure` | [CnuBSurface](/corpus/taulib/docs/book-v-temporal-boundary-data/cnu-bsurface/) | L142-L155 | type/data schema | type/data schema | `V.D39` |
| `def` | [CnuBSurface.tempFloat](/corpus/taulib/docs/book-v-temporal-boundary-data/temp-float-l158/) | L158-L159 | data/computed value | data/computed value | — |
| `def` | [canonical_cmb](/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-cmb/) | L166-L170 | definition | definition | — |
| `def` | [canonical_cnub](/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-cnub/) | L173-L175 | definition | definition | — |
| `def` | [canonical_recomb](/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-recomb/) | L178-L180 | definition | definition | — |
| `def` | [canonical_nu_decoupling](/corpus/taulib/docs/book-v-temporal-boundary-data/canonical-nu-decoupling/) | L183-L185 | definition | definition | — |
| `theorem` | [recomb_is_physical](/corpus/taulib/docs/book-v-temporal-boundary-data/recomb-is-physical/) | L192-L193 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cmb_is_boundary_data](/corpus/taulib/docs/book-v-temporal-boundary-data/cmb-is-boundary-data/) | L198-L199 | proof obligation | formal proof obligation checked | `V.P07` |
| `theorem` | [cmb_standard_temperature](/corpus/taulib/docs/book-v-temporal-boundary-data/cmb-standard-temperature/) | L203-L204 | proof obligation | formal proof obligation checked | `V.R47` |
| `theorem` | [blackbody_maximizes_entropy](/corpus/taulib/docs/book-v-temporal-boundary-data/blackbody-maximizes-entropy/) | L209-L210 | proof obligation | formal proof obligation checked | `V.P08` |
| `theorem` | [cnub_temperature_standard](/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-temperature-standard/) | L213-L216 | proof obligation | formal proof obligation checked | `V.R48` |
| `theorem` | [cnub_three_species](/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-three-species/) | L219-L220 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cnub_mass_constraint](/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-mass-constraint/) | L225-L227 | proof obligation | formal proof obligation checked | `V.P09` |
| `theorem` | [cnub_mass_value](/corpus/taulib/docs/book-v-temporal-boundary-data/cnub-mass-value/) | L230-L231 | proof obligation | formal proof obligation checked | — |
| `theorem` | [recomb_after_nu](/corpus/taulib/docs/book-v-temporal-boundary-data/recomb-after-nu/) | L234-L236 | proof obligation | formal proof obligation checked | — |
| `theorem` | [cmb_multipole_count](/corpus/taulib/docs/book-v-temporal-boundary-data/cmb-multipole-count/) | L239-L240 | proof obligation | formal proof obligation checked | — |
| `theorem` | [recomb_redshift](/corpus/taulib/docs/book-v-temporal-boundary-data/recomb-redshift/) | L243-L244 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L251](/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l251/) | L251-L251 | computed check | computed check | — |
| `eval` | [#eval L254](/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l254/) | L254-L254 | computed check | computed check | — |
| `eval` | [#eval L257](/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l257/) | L257-L257 | computed check | computed check | — |
| `eval` | [#eval L260](/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l260/) | L260-L260 | computed check | computed check | — |
| `eval` | [#eval L263](/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l263/) | L263-L263 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l264/) | L264-L264 | computed check | computed check | — |
| `eval` | [#eval L265](/corpus/taulib/docs/book-v-temporal-boundary-data/eval-l265/) | L265-L267 | computed check | computed check | — |

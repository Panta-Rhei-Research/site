---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Temporal.BoundaryData",
  "permalink": "/verify/taulib/docs/book-v-temporal-boundary-data/",
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
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/recombination-depth/",
      "source_line_start": 72,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": [
        "V.D36"
      ]
    },
    {
      "kind": "structure",
      "name": "CMBSurface",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cmbsurface/",
      "source_line_start": 92,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": [
        "V.D37"
      ]
    },
    {
      "kind": "def",
      "name": "CMBSurface.tempFloat",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/temp-float/",
      "source_line_start": 108,
      "source_line_end": 109,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutrinoDecoupling",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/neutrino-decoupling/",
      "source_line_start": 121,
      "source_line_end": 128,
      "formal_status": "defined",
      "registry_ids": [
        "V.D38"
      ]
    },
    {
      "kind": "structure",
      "name": "CnuBSurface",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cnu-bsurface/",
      "source_line_start": 142,
      "source_line_end": 155,
      "formal_status": "defined",
      "registry_ids": [
        "V.D39"
      ]
    },
    {
      "kind": "def",
      "name": "CnuBSurface.tempFloat",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/temp-float-l158/",
      "source_line_start": 158,
      "source_line_end": 159,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_cmb",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/canonical-cmb/",
      "source_line_start": 166,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_cnub",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/canonical-cnub/",
      "source_line_start": 173,
      "source_line_end": 175,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_recomb",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/canonical-recomb/",
      "source_line_start": 178,
      "source_line_end": 180,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_nu_decoupling",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/canonical-nu-decoupling/",
      "source_line_start": 183,
      "source_line_end": 185,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recomb_is_physical",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/recomb-is-physical/",
      "source_line_start": 192,
      "source_line_end": 193,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cmb_is_boundary_data",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cmb-is-boundary-data/",
      "source_line_start": 198,
      "source_line_end": 199,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P07"
      ]
    },
    {
      "kind": "theorem",
      "name": "cmb_standard_temperature",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cmb-standard-temperature/",
      "source_line_start": 203,
      "source_line_end": 204,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R47"
      ]
    },
    {
      "kind": "theorem",
      "name": "blackbody_maximizes_entropy",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/blackbody-maximizes-entropy/",
      "source_line_start": 209,
      "source_line_end": 210,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P08"
      ]
    },
    {
      "kind": "theorem",
      "name": "cnub_temperature_standard",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cnub-temperature-standard/",
      "source_line_start": 213,
      "source_line_end": 216,
      "formal_status": "formalized",
      "registry_ids": [
        "V.R48"
      ]
    },
    {
      "kind": "theorem",
      "name": "cnub_three_species",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cnub-three-species/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cnub_mass_constraint",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cnub-mass-constraint/",
      "source_line_start": 225,
      "source_line_end": 227,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P09"
      ]
    },
    {
      "kind": "theorem",
      "name": "cnub_mass_value",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cnub-mass-value/",
      "source_line_start": 230,
      "source_line_end": 231,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recomb_after_nu",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/recomb-after-nu/",
      "source_line_start": 234,
      "source_line_end": 236,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "cmb_multipole_count",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/cmb-multipole-count/",
      "source_line_start": 239,
      "source_line_end": 240,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "recomb_redshift",
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/recomb-redshift/",
      "source_line_start": 243,
      "source_line_end": 244,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/eval-l251/",
      "source_line_start": 251,
      "source_line_end": 251,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-temporal-boundary-data/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 267,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [RecombinationDepth](/verify/taulib/docs/book-v-temporal-boundary-data/recombination-depth/) | L72-L79 | defined | `V.D36` |
| `structure` | [CMBSurface](/verify/taulib/docs/book-v-temporal-boundary-data/cmbsurface/) | L92-L105 | defined | `V.D37` |
| `def` | [CMBSurface.tempFloat](/verify/taulib/docs/book-v-temporal-boundary-data/temp-float/) | L108-L109 | defined | — |
| `structure` | [NeutrinoDecoupling](/verify/taulib/docs/book-v-temporal-boundary-data/neutrino-decoupling/) | L121-L128 | defined | `V.D38` |
| `structure` | [CnuBSurface](/verify/taulib/docs/book-v-temporal-boundary-data/cnu-bsurface/) | L142-L155 | defined | `V.D39` |
| `def` | [CnuBSurface.tempFloat](/verify/taulib/docs/book-v-temporal-boundary-data/temp-float-l158/) | L158-L159 | defined | — |
| `def` | [canonical_cmb](/verify/taulib/docs/book-v-temporal-boundary-data/canonical-cmb/) | L166-L170 | defined | — |
| `def` | [canonical_cnub](/verify/taulib/docs/book-v-temporal-boundary-data/canonical-cnub/) | L173-L175 | defined | — |
| `def` | [canonical_recomb](/verify/taulib/docs/book-v-temporal-boundary-data/canonical-recomb/) | L178-L180 | defined | — |
| `def` | [canonical_nu_decoupling](/verify/taulib/docs/book-v-temporal-boundary-data/canonical-nu-decoupling/) | L183-L185 | defined | — |
| `theorem` | [recomb_is_physical](/verify/taulib/docs/book-v-temporal-boundary-data/recomb-is-physical/) | L192-L193 | formalized | — |
| `theorem` | [cmb_is_boundary_data](/verify/taulib/docs/book-v-temporal-boundary-data/cmb-is-boundary-data/) | L198-L199 | formalized | `V.P07` |
| `theorem` | [cmb_standard_temperature](/verify/taulib/docs/book-v-temporal-boundary-data/cmb-standard-temperature/) | L203-L204 | formalized | `V.R47` |
| `theorem` | [blackbody_maximizes_entropy](/verify/taulib/docs/book-v-temporal-boundary-data/blackbody-maximizes-entropy/) | L209-L210 | formalized | `V.P08` |
| `theorem` | [cnub_temperature_standard](/verify/taulib/docs/book-v-temporal-boundary-data/cnub-temperature-standard/) | L213-L216 | formalized | `V.R48` |
| `theorem` | [cnub_three_species](/verify/taulib/docs/book-v-temporal-boundary-data/cnub-three-species/) | L219-L220 | formalized | — |
| `theorem` | [cnub_mass_constraint](/verify/taulib/docs/book-v-temporal-boundary-data/cnub-mass-constraint/) | L225-L227 | formalized | `V.P09` |
| `theorem` | [cnub_mass_value](/verify/taulib/docs/book-v-temporal-boundary-data/cnub-mass-value/) | L230-L231 | formalized | — |
| `theorem` | [recomb_after_nu](/verify/taulib/docs/book-v-temporal-boundary-data/recomb-after-nu/) | L234-L236 | formalized | — |
| `theorem` | [cmb_multipole_count](/verify/taulib/docs/book-v-temporal-boundary-data/cmb-multipole-count/) | L239-L240 | formalized | — |
| `theorem` | [recomb_redshift](/verify/taulib/docs/book-v-temporal-boundary-data/recomb-redshift/) | L243-L244 | formalized | — |
| `eval` | [#eval L251](/verify/taulib/docs/book-v-temporal-boundary-data/eval-l251/) | L251-L251 | computed | — |
| `eval` | [#eval L254](/verify/taulib/docs/book-v-temporal-boundary-data/eval-l254/) | L254-L254 | computed | — |
| `eval` | [#eval L257](/verify/taulib/docs/book-v-temporal-boundary-data/eval-l257/) | L257-L257 | computed | — |
| `eval` | [#eval L260](/verify/taulib/docs/book-v-temporal-boundary-data/eval-l260/) | L260-L260 | computed | — |
| `eval` | [#eval L263](/verify/taulib/docs/book-v-temporal-boundary-data/eval-l263/) | L263-L263 | computed | — |
| `eval` | [#eval L264](/verify/taulib/docs/book-v-temporal-boundary-data/eval-l264/) | L264-L264 | computed | — |
| `eval` | [#eval L265](/verify/taulib/docs/book-v-temporal-boundary-data/eval-l265/) | L265-L267 | computed | — |

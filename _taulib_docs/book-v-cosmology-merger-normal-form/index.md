---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.MergerNormalForm",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_slug": "book-v-cosmology-merger-normal-form",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/MergerNormalForm.lean",
  "sha256": "3d9bb2c4f7bdec15d324b161edcc478245cfb4ae3a71919b9987c43f7a3020a8",
  "imports": [
    "TauLib.BookV.Cosmology.NoShrinkExtended"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Cosmology.GlobalFiniteness"
  ],
  "registry_ids": [
    "V.D175",
    "V.D176",
    "V.D177",
    "V.D282",
    "V.P100",
    "V.P101",
    "V.P150",
    "V.P97",
    "V.P98",
    "V.P99",
    "V.R228",
    "V.R229",
    "V.R230",
    "V.R231",
    "V.R232",
    "V.R233",
    "V.T115",
    "V.T224"
  ],
  "declaration_counts": {
    "structure": 8,
    "theorem": 11,
    "def": 7,
    "inductive": 1,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "MergerNormalFormData",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/merger-normal-form-data/",
      "source_line_start": 76,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T115"
      ]
    },
    {
      "kind": "theorem",
      "name": "merger_normal_form",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/merger-normal-form/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RingdownMode",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/ringdown-mode/",
      "source_line_start": 108,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D175"
      ]
    },
    {
      "kind": "theorem",
      "name": "ringdown_damping_structural",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/ringdown-damping-structural/",
      "source_line_start": 129,
      "source_line_end": 130,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P97"
      ]
    },
    {
      "kind": "structure",
      "name": "BHMassScale",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/bhmass-scale/",
      "source_line_start": 141,
      "source_line_end": 152,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D176"
      ]
    },
    {
      "kind": "structure",
      "name": "PrimorialMassGap",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/primorial-mass-gap/",
      "source_line_start": 164,
      "source_line_end": 175,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P98"
      ]
    },
    {
      "kind": "theorem",
      "name": "mass_gap_primorial",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/mass-gap-primorial/",
      "source_line_start": 178,
      "source_line_end": 179,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "scope_note_mass_spectrum",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/scope-note-mass-spectrum/",
      "source_line_start": 188,
      "source_line_end": 190,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R231"
      ]
    },
    {
      "kind": "theorem",
      "name": "scope_note_holds",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/scope-note-holds/",
      "source_line_start": 192,
      "source_line_end": 192,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "WilsonLawType",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/wilson-law-type/",
      "source_line_start": 204,
      "source_line_end": 209,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D177"
      ]
    },
    {
      "kind": "structure",
      "name": "BaseWilsonLoop",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/base-wilson-loop/",
      "source_line_start": 212,
      "source_line_end": 221,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gravitational_deconfinement",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/gravitational-deconfinement/",
      "source_line_start": 232,
      "source_line_end": 234,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P99"
      ]
    },
    {
      "kind": "structure",
      "name": "BHABPhase",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/bhabphase/",
      "source_line_start": 245,
      "source_line_end": 252,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P100"
      ]
    },
    {
      "kind": "theorem",
      "name": "bh_ab_phase",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/bh-ab-phase/",
      "source_line_start": 255,
      "source_line_end": 256,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RadiatedEnergyBound",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/radiated-energy-bound/",
      "source_line_start": 267,
      "source_line_end": 276,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P101"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_energy_bound",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/canonical-energy-bound/",
      "source_line_start": 279,
      "source_line_end": 283,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "radiated_energy_bound",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/radiated-energy-bound-l286/",
      "source_line_start": 286,
      "source_line_end": 289,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "the_sqrt2_remark",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/the-sqrt2-remark/",
      "source_line_start": 299,
      "source_line_end": 301,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R233"
      ]
    },
    {
      "kind": "theorem",
      "name": "sqrt2_remark_holds",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/sqrt2-remark-holds/",
      "source_line_start": 303,
      "source_line_end": 303,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_merger",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/example-merger/",
      "source_line_start": 330,
      "source_line_end": 338,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mode1",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/mode1/",
      "source_line_start": 345,
      "source_line_end": 351,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BlueprintFusionEnergy",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/blueprint-fusion-energy/",
      "source_line_start": 366,
      "source_line_end": 370,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D282"
      ]
    },
    {
      "kind": "def",
      "name": "merger_energy_formula",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/merger-energy-formula/",
      "source_line_start": 374,
      "source_line_end": 377,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.T224"
      ]
    },
    {
      "kind": "def",
      "name": "equal_mass_eta_ppm",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/equal-mass-eta-ppm/",
      "source_line_start": 381,
      "source_line_end": 381,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.P150"
      ]
    },
    {
      "kind": "theorem",
      "name": "equal_mass_eta_positive",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/equal-mass-eta-positive/",
      "source_line_start": 384,
      "source_line_end": 384,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equal_mass_eta_below_bound",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/equal-mass-eta-below-bound/",
      "source_line_start": 387,
      "source_line_end": 387,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota_sq_canonical",
      "url": "/corpus/taulib/docs/book-v-cosmology-merger-normal-form/iota-sq-canonical/",
      "source_line_start": 390,
      "source_line_end": 392,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/MergerNormalForm.lean`
- SHA-256: `3d9bb2c4f7bdec15d324b161edcc478245cfb4ae3a71919b9987c43f7a3020a8`

## Registry Links

- `V.D175` — Ringdown mode
- `V.D176` — BH mass scale at depth n
- `V.D177` — Base Wilson loop
- `V.D282` — Blueprint Fusion Energy
- `V.P100` — BH gravitational Aharonov--Bohm phase
- `V.P101` — Radiated energy bound
- `V.P150` — Equal-Mass Energy Fraction
- `V.P97` — Ringdown damping is structural
- `V.P98` — Mass gap between adjacent primorial levels
- `V.P99` — Gravitational deconfinement
- `V.R228` — Why overlap forces merger
- `V.R229` — What the Normal Form does not give
- `V.R230` — The mass gap and the IMBH desert
- `V.R231` — Scope note on mass spectrum predictions
- `V.R232` — Contrast with the strong sector
- `V.R233` — The 1/sqrt2
- `V.T115` — Merger Normal Form
- `V.T224` — Merger Energy Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.NoShrinkExtended`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Cosmology.GlobalFiniteness`

## Declaration Counts

- `def`: 7
- `eval`: 4
- `inductive`: 1
- `structure`: 8
- `theorem`: 11

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [MergerNormalFormData](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/merger-normal-form-data/) | L76-L92 | type/data schema | type/data schema | `V.T115` |
| `theorem` | [merger_normal_form](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/merger-normal-form/) | L95-L96 | proof obligation | formal proof obligation checked | — |
| `structure` | [RingdownMode](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/ringdown-mode/) | L108-L121 | type/data schema | type/data schema | `V.D175` |
| `theorem` | [ringdown_damping_structural](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/ringdown-damping-structural/) | L129-L130 | proof obligation | formal proof obligation checked | `V.P97` |
| `structure` | [BHMassScale](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/bhmass-scale/) | L141-L152 | type/data schema | type/data schema | `V.D176` |
| `structure` | [PrimorialMassGap](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/primorial-mass-gap/) | L164-L175 | type/data schema | type/data schema | `V.P98` |
| `theorem` | [mass_gap_primorial](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/mass-gap-primorial/) | L178-L179 | proof obligation | formal proof obligation checked | — |
| `def` | [scope_note_mass_spectrum](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/scope-note-mass-spectrum/) | L188-L190 | definition | definition | `V.R231` |
| `theorem` | [scope_note_holds](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/scope-note-holds/) | L192-L192 | proof obligation | formal proof obligation checked | — |
| `inductive` | [WilsonLawType](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/wilson-law-type/) | L204-L209 | type/data schema | type/data schema | `V.D177` |
| `structure` | [BaseWilsonLoop](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/base-wilson-loop/) | L212-L221 | type/data schema | type/data schema | — |
| `theorem` | [gravitational_deconfinement](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/gravitational-deconfinement/) | L232-L234 | proof obligation | formal proof obligation checked | `V.P99` |
| `structure` | [BHABPhase](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/bhabphase/) | L245-L252 | type/data schema | type/data schema | `V.P100` |
| `theorem` | [bh_ab_phase](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/bh-ab-phase/) | L255-L256 | proof obligation | formal proof obligation checked | — |
| `structure` | [RadiatedEnergyBound](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/radiated-energy-bound/) | L267-L276 | type/data schema | type/data schema | `V.P101` |
| `def` | [canonical_energy_bound](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/canonical-energy-bound/) | L279-L283 | definition | definition | — |
| `theorem` | [radiated_energy_bound](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/radiated-energy-bound-l286/) | L286-L289 | proof obligation | formal proof obligation checked | — |
| `def` | [the_sqrt2_remark](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/the-sqrt2-remark/) | L299-L301 | definition | definition | `V.R233` |
| `theorem` | [sqrt2_remark_holds](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/sqrt2-remark-holds/) | L303-L303 | proof obligation | formal proof obligation checked | — |
| `def` | [example_merger](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/example-merger/) | L330-L338 | definition | definition | — |
| `eval` | [#eval L340](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l340/) | L340-L340 | computed check | computed check | — |
| `eval` | [#eval L341](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l341/) | L341-L341 | computed check | computed check | — |
| `eval` | [#eval L342](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l342/) | L342-L342 | computed check | computed check | — |
| `def` | [mode1](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/mode1/) | L345-L351 | definition | definition | — |
| `eval` | [#eval L353](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/eval-l353/) | L353-L353 | computed check | computed check | — |
| `structure` | [BlueprintFusionEnergy](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/blueprint-fusion-energy/) | L366-L370 | type/data schema | type/data schema | `V.D282` |
| `def` | [merger_energy_formula](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/merger-energy-formula/) | L374-L377 | definition | definition | `V.T224` |
| `def` | [equal_mass_eta_ppm](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/equal-mass-eta-ppm/) | L381-L381 | data/computed value | data/computed value | `V.P150` |
| `theorem` | [equal_mass_eta_positive](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/equal-mass-eta-positive/) | L384-L384 | proof obligation | formal proof obligation checked | — |
| `theorem` | [equal_mass_eta_below_bound](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/equal-mass-eta-below-bound/) | L387-L387 | proof obligation | formal proof obligation checked | — |
| `theorem` | [iota_sq_canonical](/corpus/taulib/docs/book-v-cosmology-merger-normal-form/iota-sq-canonical/) | L390-L392 | proof obligation | formal proof obligation checked | — |

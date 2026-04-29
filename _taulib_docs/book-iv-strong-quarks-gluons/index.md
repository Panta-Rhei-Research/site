---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Strong.QuarksGluons",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Strong.QuarksGluons`.",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_slug": "book-iv-strong-quarks-gluons",
  "book": "BookIV",
  "family": "Strong",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Strong/QuarksGluons.lean",
  "sha256": "ba6d39c15491dfec07d3ed2e5627b5f67c3fb947e4fb807a174f14c4abc02b43",
  "imports": [
    "TauLib.BookIV.Strong.StrongCoupling"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Strong.VacuumCatastrophe"
  ],
  "registry_ids": [
    "IV.D187",
    "IV.D188",
    "IV.D189",
    "IV.D190",
    "IV.D191",
    "IV.P113",
    "IV.P114",
    "IV.P115",
    "IV.P116",
    "IV.P117",
    "IV.P118"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 11,
    "def": 13,
    "theorem": 15,
    "eval": 12
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "QuarkType",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-type/",
      "source_line_start": 46,
      "source_line_end": 51,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QuarkMode",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-mode/",
      "source_line_start": 56,
      "source_line_end": 67,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D187"
      ]
    },
    {
      "kind": "structure",
      "name": "QuarkChargeSpec",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-charge-spec/",
      "source_line_start": 78,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P113"
      ]
    },
    {
      "kind": "def",
      "name": "down_type_charge",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/down-type-charge/",
      "source_line_start": 87,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "up_type_charge",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/up-type-charge/",
      "source_line_start": 91,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "down_charge_minus_third",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/down-charge-minus-third/",
      "source_line_start": 96,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "up_charge_plus_two_thirds",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/up-charge-plus-two-thirds/",
      "source_line_start": 102,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ud_charge_sum",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/ud-charge-sum/",
      "source_line_start": 108,
      "source_line_end": 110,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proton_charge",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/proton-charge/",
      "source_line_start": 113,
      "source_line_end": 116,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutron_charge",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/neutron-charge/",
      "source_line_start": 119,
      "source_line_end": 122,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AntiquarkMode",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/antiquark-mode/",
      "source_line_start": 130,
      "source_line_end": 139,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D188"
      ]
    },
    {
      "kind": "def",
      "name": "quark_to_antiquark",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-to-antiquark/",
      "source_line_start": 142,
      "source_line_end": 148,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "LemniscateModeClass",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/lemniscate-mode-class/",
      "source_line_start": 155,
      "source_line_end": 162,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QuarkGenerations",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-generations/",
      "source_line_start": 168,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D189"
      ]
    },
    {
      "kind": "def",
      "name": "quark_generations",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-generations-l179/",
      "source_line_start": 179,
      "source_line_end": 179,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_generations",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/three-generations/",
      "source_line_start": 181,
      "source_line_end": 182,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mode_classes_distinct",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/mode-classes-distinct/",
      "source_line_start": 185,
      "source_line_end": 189,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GenerationMassOrdering",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/generation-mass-ordering/",
      "source_line_start": 200,
      "source_line_end": 207,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P114"
      ]
    },
    {
      "kind": "def",
      "name": "generation_mass_ordering",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/generation-mass-ordering-l209/",
      "source_line_start": 209,
      "source_line_end": 209,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GluonCount",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-count/",
      "source_line_start": 217,
      "source_line_end": 224,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P115"
      ]
    },
    {
      "kind": "def",
      "name": "gluon_count",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-count-l226/",
      "source_line_start": 226,
      "source_line_end": 226,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "eight_gluons",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eight-gluons/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gluon_dim_formula",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-dim-formula/",
      "source_line_start": 231,
      "source_line_end": 231,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GluonVertices",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-vertices/",
      "source_line_start": 241,
      "source_line_end": 248,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P116"
      ]
    },
    {
      "kind": "def",
      "name": "gluon_vertices",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-vertices-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "two_vertex_types",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/two-vertex-types/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "StructuralAF",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/structural-af/",
      "source_line_start": 260,
      "source_line_end": 267,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P117"
      ]
    },
    {
      "kind": "def",
      "name": "structural_af",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/structural-af-l269/",
      "source_line_start": 269,
      "source_line_end": 269,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AFFromNcNf",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/affrom-nc-nf/",
      "source_line_start": 278,
      "source_line_end": 287,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P118"
      ]
    },
    {
      "kind": "def",
      "name": "af_from_nc_nf",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/af-from-nc-nf/",
      "source_line_start": 289,
      "source_line_end": 289,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "af_condition",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/af-condition/",
      "source_line_start": 292,
      "source_line_end": 293,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "six_flavors",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/six-flavors/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MesonState",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/meson-state/",
      "source_line_start": 304,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D190"
      ]
    },
    {
      "kind": "def",
      "name": "mk_meson",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/mk-meson/",
      "source_line_start": 318,
      "source_line_end": 323,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "pi_plus",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/pi-plus/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "pi_plus_singlet",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/pi-plus-singlet/",
      "source_line_start": 329,
      "source_line_end": 329,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BaryonState",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/baryon-state/",
      "source_line_start": 337,
      "source_line_end": 348,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D191"
      ]
    },
    {
      "kind": "def",
      "name": "proton_state",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/proton-state/",
      "source_line_start": 351,
      "source_line_end": 354,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "neutron_state",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/neutron-state/",
      "source_line_start": 357,
      "source_line_end": 360,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "proton_singlet",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/proton-singlet/",
      "source_line_start": 363,
      "source_line_end": 365,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutron_singlet",
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/neutron-singlet/",
      "source_line_start": 368,
      "source_line_end": 370,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l376/",
      "source_line_start": 376,
      "source_line_end": 376,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l377/",
      "source_line_start": 377,
      "source_line_end": 377,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l378/",
      "source_line_start": 378,
      "source_line_end": 378,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l379/",
      "source_line_start": 379,
      "source_line_end": 379,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l380/",
      "source_line_start": 380,
      "source_line_end": 380,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l381/",
      "source_line_start": 381,
      "source_line_end": 381,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l382/",
      "source_line_start": 382,
      "source_line_end": 382,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l383/",
      "source_line_start": 383,
      "source_line_end": 383,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l384/",
      "source_line_start": 384,
      "source_line_end": 384,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l385/",
      "source_line_start": 385,
      "source_line_end": 385,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l386/",
      "source_line_start": 386,
      "source_line_end": 386,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l387/",
      "source_line_start": 387,
      "source_line_end": 389,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean",
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
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Strong/QuarksGluons.lean`
- SHA-256: `ba6d39c15491dfec07d3ed2e5627b5f67c3fb947e4fb807a174f14c4abc02b43`

## Registry Links

- `IV.D187` — Quark mode
- `IV.D188` — Antiquark mode
- `IV.D189` — Quark generations from \Lemniscate
- `IV.D190` — Meson state
- `IV.D191` — Baryon state
- `IV.P113` — Quark electric charges
- `IV.P114` — Generation mass ordering
- `IV.P115` — Gluon count
- `IV.P116` — Gluon self-interaction vertices
- `IV.P117` — Structural asymptotic freedom
- `IV.P118` — Asymptotic freedom from N_c and N_f

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Strong.StrongCoupling`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Strong.VacuumCatastrophe`

## Declaration Counts

- `def`: 13
- `eval`: 12
- `inductive`: 2
- `structure`: 11
- `theorem`: 15

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [QuarkType](/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-type/) | L46-L51 | defined | — |
| `structure` | [QuarkMode](/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-mode/) | L56-L67 | defined | `IV.D187` |
| `structure` | [QuarkChargeSpec](/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-charge-spec/) | L78-L85 | defined | `IV.P113` |
| `def` | [down_type_charge](/verify/taulib/docs/book-iv-strong-quarks-gluons/down-type-charge/) | L87-L89 | defined | — |
| `def` | [up_type_charge](/verify/taulib/docs/book-iv-strong-quarks-gluons/up-type-charge/) | L91-L93 | defined | — |
| `theorem` | [down_charge_minus_third](/verify/taulib/docs/book-iv-strong-quarks-gluons/down-charge-minus-third/) | L96-L99 | formalized | — |
| `theorem` | [up_charge_plus_two_thirds](/verify/taulib/docs/book-iv-strong-quarks-gluons/up-charge-plus-two-thirds/) | L102-L105 | formalized | — |
| `theorem` | [ud_charge_sum](/verify/taulib/docs/book-iv-strong-quarks-gluons/ud-charge-sum/) | L108-L110 | formalized | — |
| `theorem` | [proton_charge](/verify/taulib/docs/book-iv-strong-quarks-gluons/proton-charge/) | L113-L116 | formalized | — |
| `theorem` | [neutron_charge](/verify/taulib/docs/book-iv-strong-quarks-gluons/neutron-charge/) | L119-L122 | formalized | — |
| `structure` | [AntiquarkMode](/verify/taulib/docs/book-iv-strong-quarks-gluons/antiquark-mode/) | L130-L139 | defined | `IV.D188` |
| `def` | [quark_to_antiquark](/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-to-antiquark/) | L142-L148 | defined | — |
| `inductive` | [LemniscateModeClass](/verify/taulib/docs/book-iv-strong-quarks-gluons/lemniscate-mode-class/) | L155-L162 | defined | — |
| `structure` | [QuarkGenerations](/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-generations/) | L168-L177 | defined | `IV.D189` |
| `def` | [quark_generations](/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-generations-l179/) | L179-L179 | defined | — |
| `theorem` | [three_generations](/verify/taulib/docs/book-iv-strong-quarks-gluons/three-generations/) | L181-L182 | formalized | — |
| `theorem` | [mode_classes_distinct](/verify/taulib/docs/book-iv-strong-quarks-gluons/mode-classes-distinct/) | L185-L189 | formalized | — |
| `structure` | [GenerationMassOrdering](/verify/taulib/docs/book-iv-strong-quarks-gluons/generation-mass-ordering/) | L200-L207 | defined | `IV.P114` |
| `def` | [generation_mass_ordering](/verify/taulib/docs/book-iv-strong-quarks-gluons/generation-mass-ordering-l209/) | L209-L209 | defined | — |
| `structure` | [GluonCount](/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-count/) | L217-L224 | defined | `IV.P115` |
| `def` | [gluon_count](/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-count-l226/) | L226-L226 | defined | — |
| `theorem` | [eight_gluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/eight-gluons/) | L228-L228 | formalized | — |
| `theorem` | [gluon_dim_formula](/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-dim-formula/) | L231-L231 | formalized | — |
| `structure` | [GluonVertices](/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-vertices/) | L241-L248 | defined | `IV.P116` |
| `def` | [gluon_vertices](/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-vertices-l250/) | L250-L250 | defined | — |
| `theorem` | [two_vertex_types](/verify/taulib/docs/book-iv-strong-quarks-gluons/two-vertex-types/) | L252-L252 | formalized | — |
| `structure` | [StructuralAF](/verify/taulib/docs/book-iv-strong-quarks-gluons/structural-af/) | L260-L267 | defined | `IV.P117` |
| `def` | [structural_af](/verify/taulib/docs/book-iv-strong-quarks-gluons/structural-af-l269/) | L269-L269 | defined | — |
| `structure` | [AFFromNcNf](/verify/taulib/docs/book-iv-strong-quarks-gluons/affrom-nc-nf/) | L278-L287 | defined | `IV.P118` |
| `def` | [af_from_nc_nf](/verify/taulib/docs/book-iv-strong-quarks-gluons/af-from-nc-nf/) | L289-L289 | defined | — |
| `theorem` | [af_condition](/verify/taulib/docs/book-iv-strong-quarks-gluons/af-condition/) | L292-L293 | formalized | — |
| `theorem` | [six_flavors](/verify/taulib/docs/book-iv-strong-quarks-gluons/six-flavors/) | L296-L296 | formalized | — |
| `structure` | [MesonState](/verify/taulib/docs/book-iv-strong-quarks-gluons/meson-state/) | L304-L315 | defined | `IV.D190` |
| `def` | [mk_meson](/verify/taulib/docs/book-iv-strong-quarks-gluons/mk-meson/) | L318-L323 | defined | — |
| `def` | [pi_plus](/verify/taulib/docs/book-iv-strong-quarks-gluons/pi-plus/) | L326-L326 | defined | — |
| `theorem` | [pi_plus_singlet](/verify/taulib/docs/book-iv-strong-quarks-gluons/pi-plus-singlet/) | L329-L329 | formalized | — |
| `structure` | [BaryonState](/verify/taulib/docs/book-iv-strong-quarks-gluons/baryon-state/) | L337-L348 | defined | `IV.D191` |
| `def` | [proton_state](/verify/taulib/docs/book-iv-strong-quarks-gluons/proton-state/) | L351-L354 | defined | — |
| `def` | [neutron_state](/verify/taulib/docs/book-iv-strong-quarks-gluons/neutron-state/) | L357-L360 | defined | — |
| `theorem` | [proton_singlet](/verify/taulib/docs/book-iv-strong-quarks-gluons/proton-singlet/) | L363-L365 | formalized | — |
| `theorem` | [neutron_singlet](/verify/taulib/docs/book-iv-strong-quarks-gluons/neutron-singlet/) | L368-L370 | formalized | — |
| `eval` | [#eval L376](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l376/) | L376-L376 | computed | — |
| `eval` | [#eval L377](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l377/) | L377-L377 | computed | — |
| `eval` | [#eval L378](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l378/) | L378-L378 | computed | — |
| `eval` | [#eval L379](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l379/) | L379-L379 | computed | — |
| `eval` | [#eval L380](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l380/) | L380-L380 | computed | — |
| `eval` | [#eval L381](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l381/) | L381-L381 | computed | — |
| `eval` | [#eval L382](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l382/) | L382-L382 | computed | — |
| `eval` | [#eval L383](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l383/) | L383-L383 | computed | — |
| `eval` | [#eval L384](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l384/) | L384-L384 | computed | — |
| `eval` | [#eval L385](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l385/) | L385-L385 | computed | — |
| `eval` | [#eval L386](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l386/) | L386-L386 | computed | — |
| `eval` | [#eval L387](/verify/taulib/docs/book-iv-strong-quarks-gluons/eval-l387/) | L387-L389 | computed | — |

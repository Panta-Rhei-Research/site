---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_slug": "book-iv-physics-nucleon-mass-splitting",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/NucleonMassSplitting.lean",
  "sha256": "1b836154db748a5b6222b2a14632a6c6d1d80ac0267ff3ddfb67390da1960eb4",
  "imports": [
    "TauLib.BookIV.Physics.LemniscateCapacity",
    "TauLib.BookIV.Physics.MassEnergy",
    "TauLib.BookIV.Sectors.FineStructure"
  ],
  "imported_by": [
    "TauLib.BookIV"
  ],
  "registry_ids": [
    "IV.D340",
    "IV.D341",
    "IV.D342",
    "IV.P183",
    "IV.P184",
    "IV.P201",
    "IV.R394",
    "IV.T141",
    "IV.T142"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 20,
    "theorem": 26,
    "lemma": 6,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "NucleonMode",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-mode/",
      "source_line_start": 59,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D340"
      ]
    },
    {
      "kind": "def",
      "name": "neutronIsChiMinus",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/neutron-is-chi-minus/",
      "source_line_start": 65,
      "source_line_end": 65,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "protonIsChiPlus",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/proton-is-chi-plus/",
      "source_line_start": 68,
      "source_line_end": 68,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleon_modes_distinct",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-modes-distinct/",
      "source_line_start": 71,
      "source_line_end": 89,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota5_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-numer/",
      "source_line_start": 92,
      "source_line_end": 92,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota5_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom/",
      "source_line_start": 93,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota2_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-numer/",
      "source_line_start": 96,
      "source_line_end": 96,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota2_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom/",
      "source_line_start": 97,
      "source_line_end": 97,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota6_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-numer/",
      "source_line_start": 100,
      "source_line_end": 100,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota6_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom/",
      "source_line_start": 101,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota11_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-numer/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota11_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-denom/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota5_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom-pos/",
      "source_line_start": 108,
      "source_line_end": 108,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota2_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom-pos/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota6_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom-pos/",
      "source_line_start": 110,
      "source_line_end": 124,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D341"
      ]
    },
    {
      "kind": "def",
      "name": "qcd_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer/",
      "source_line_start": 127,
      "source_line_end": 127,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D341"
      ]
    },
    {
      "kind": "def",
      "name": "qcd_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom/",
      "source_line_start": 130,
      "source_line_end": 130,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D341"
      ]
    },
    {
      "kind": "theorem",
      "name": "qcd_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-pos/",
      "source_line_start": 133,
      "source_line_end": 134,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "qcd_float",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-float/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "qcd_numer_val",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer-val/",
      "source_line_start": 142,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "qcd_denom_val",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-val/",
      "source_line_start": 144,
      "source_line_end": 145,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_in_range",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-in-range/",
      "source_line_start": 150,
      "source_line_end": 172,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D341",
        "IV.D342"
      ]
    },
    {
      "kind": "def",
      "name": "em_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D342"
      ]
    },
    {
      "kind": "def",
      "name": "em_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom/",
      "source_line_start": 180,
      "source_line_end": 180,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D342"
      ]
    },
    {
      "kind": "theorem",
      "name": "em_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-pos/",
      "source_line_start": 183,
      "source_line_end": 184,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "em_float",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-float/",
      "source_line_start": 187,
      "source_line_end": 188,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "em_numer_val",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-val/",
      "source_line_start": 190,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "em_denom_val",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-val/",
      "source_line_start": 192,
      "source_line_end": 193,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_in_range",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-in-range/",
      "source_line_start": 198,
      "source_line_end": 215,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.D342",
        "IV.T141"
      ]
    },
    {
      "kind": "def",
      "name": "tree_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer/",
      "source_line_start": 218,
      "source_line_end": 218,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T141"
      ]
    },
    {
      "kind": "def",
      "name": "tree_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T141"
      ]
    },
    {
      "kind": "theorem",
      "name": "tree_denom_pos",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-pos/",
      "source_line_start": 224,
      "source_line_end": 225,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "tree_numer_val",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer-val/",
      "source_line_start": 227,
      "source_line_end": 228,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "tree_denom_val",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-val/",
      "source_line_start": 229,
      "source_line_end": 230,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "deltaMassTree_range",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-tree-range/",
      "source_line_start": 235,
      "source_line_end": 258,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T141",
        "IV.T142"
      ]
    },
    {
      "kind": "theorem",
      "name": "pn_sign_positive",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/pn-sign-positive/",
      "source_line_start": 263,
      "source_line_end": 265,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P183"
      ]
    },
    {
      "kind": "theorem",
      "name": "deltaMassTwoSector_range",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-two-sector-range/",
      "source_line_start": 270,
      "source_line_end": 276,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T142"
      ]
    },
    {
      "kind": "theorem",
      "name": "nlo_factor_65_numer",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-numer/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P184"
      ]
    },
    {
      "kind": "theorem",
      "name": "nlo_factor_65_denom",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-denom/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P184"
      ]
    },
    {
      "kind": "theorem",
      "name": "nlo_lobe_color_product",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-lobe-color-product/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nlo_generator_count",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-generator-count/",
      "source_line_start": 293,
      "source_line_end": 293,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nlo_factor_65",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "quarkColors",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/quark-colors/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_has_color_factor",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-has-color-factor/",
      "source_line_start": 307,
      "source_line_end": 308,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_has_color_factor",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-has-color-factor/",
      "source_line_start": 311,
      "source_line_end": 312,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_denominator_channel_counting",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denominator-channel-counting/",
      "source_line_start": 321,
      "source_line_end": 322,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_denom_is_2_pow_4",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-is-2-pow-4/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_denominator_channel_counting",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denominator-channel-counting/",
      "source_line_start": 330,
      "source_line_end": 331,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_denom_decomp",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-decomp/",
      "source_line_start": 334,
      "source_line_end": 335,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "both_coefficients_share_Nc",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/both-coefficients-share-nc/",
      "source_line_start": 339,
      "source_line_end": 341,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_numer_factor",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-factor/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_denom_factor",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-factor/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_cottingham_comparison",
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/remark-cottingham-comparison/",
      "source_line_start": 372,
      "source_line_end": 375,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R394"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l382/",
      "source_line_start": 382,
      "source_line_end": 382,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l383/",
      "source_line_start": 383,
      "source_line_end": 383,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l386/",
      "source_line_start": 386,
      "source_line_end": 391,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean",
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
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/NucleonMassSplitting.lean`
- SHA-256: `1b836154db748a5b6222b2a14632a6c6d1d80ac0267ff3ddfb67390da1960eb4`

## Registry Links

- `IV.D340` — Nucleon Boundary Mode
- `IV.D341` — QCD Contribution to p-n splitting
- `IV.D342` — EM Coulomb Contribution to p-n splitting
- `IV.P183` — Sign of p-n splitting: QCD > EM
- `IV.P184` — NLO Color-Generator Correction 6/5
- `IV.P201` — C.5 Coefficients: 3/16 = N_c/2⁴ and 3/20 = N_c/(4·W₃(4))
- `IV.R394` — Comparison to Cottingham decomposition
- `IV.T141` — Proton-Neutron Mass Difference — Tree Level [SUPERSEDED]
- `IV.T142` — Proton-Neutron Mass Difference — Two-Sector

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.LemniscateCapacity`
- `TauLib.BookIV.Physics.MassEnergy`
- `TauLib.BookIV.Sectors.FineStructure`

## Imported By

- `TauLib.BookIV`

## Declaration Counts

- `def`: 20
- `eval`: 3
- `inductive`: 1
- `lemma`: 6
- `theorem`: 26

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [NucleonMode](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-mode/) | L59-L62 | defined | `IV.D340` |
| `def` | [neutronIsChiMinus](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/neutron-is-chi-minus/) | L65-L65 | defined | — |
| `def` | [protonIsChiPlus](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/proton-is-chi-plus/) | L68-L68 | defined | — |
| `theorem` | [nucleon_modes_distinct](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-modes-distinct/) | L71-L89 | formalized | — |
| `def` | [iota5_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-numer/) | L92-L92 | defined | — |
| `def` | [iota5_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom/) | L93-L93 | defined | — |
| `def` | [iota2_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-numer/) | L96-L96 | defined | — |
| `def` | [iota2_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom/) | L97-L97 | defined | — |
| `def` | [iota6_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-numer/) | L100-L100 | defined | — |
| `def` | [iota6_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom/) | L101-L101 | defined | — |
| `def` | [iota11_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-numer/) | L104-L104 | defined | — |
| `def` | [iota11_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-denom/) | L105-L105 | defined | — |
| `theorem` | [iota5_denom_pos](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom-pos/) | L108-L108 | formalized | — |
| `theorem` | [iota2_denom_pos](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom-pos/) | L109-L109 | formalized | — |
| `theorem` | [iota6_denom_pos](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom-pos/) | L110-L124 | formalized | `IV.D341` |
| `def` | [qcd_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer/) | L127-L127 | defined | `IV.D341` |
| `def` | [qcd_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom/) | L130-L130 | defined | `IV.D341` |
| `theorem` | [qcd_denom_pos](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-pos/) | L133-L134 | formalized | — |
| `def` | [qcd_float](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-float/) | L137-L138 | defined | — |
| `lemma` | [qcd_numer_val](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer-val/) | L142-L143 | formalized | — |
| `lemma` | [qcd_denom_val](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-val/) | L144-L145 | formalized | — |
| `theorem` | [qcd_in_range](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-in-range/) | L150-L172 | formalized | `IV.D341`, `IV.D342` |
| `def` | [em_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer/) | L176-L176 | defined | `IV.D342` |
| `def` | [em_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom/) | L180-L180 | defined | `IV.D342` |
| `theorem` | [em_denom_pos](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-pos/) | L183-L184 | formalized | — |
| `def` | [em_float](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-float/) | L187-L188 | defined | — |
| `lemma` | [em_numer_val](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-val/) | L190-L191 | formalized | — |
| `lemma` | [em_denom_val](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-val/) | L192-L193 | formalized | — |
| `theorem` | [em_in_range](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-in-range/) | L198-L215 | formalized | `IV.D342`, `IV.T141` |
| `def` | [tree_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer/) | L218-L218 | defined | `IV.T141` |
| `def` | [tree_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom/) | L221-L221 | defined | `IV.T141` |
| `theorem` | [tree_denom_pos](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-pos/) | L224-L225 | formalized | — |
| `lemma` | [tree_numer_val](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer-val/) | L227-L228 | formalized | — |
| `lemma` | [tree_denom_val](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-val/) | L229-L230 | formalized | — |
| `theorem` | [deltaMassTree_range](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-tree-range/) | L235-L258 | formalized | `IV.T141`, `IV.T142` |
| `theorem` | [pn_sign_positive](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/pn-sign-positive/) | L263-L265 | formalized | `IV.P183` |
| `theorem` | [deltaMassTwoSector_range](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-two-sector-range/) | L270-L276 | formalized | `IV.T142` |
| `theorem` | [nlo_factor_65_numer](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-numer/) | L284-L284 | formalized | `IV.P184` |
| `theorem` | [nlo_factor_65_denom](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-denom/) | L287-L287 | formalized | `IV.P184` |
| `theorem` | [nlo_lobe_color_product](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-lobe-color-product/) | L290-L290 | formalized | — |
| `theorem` | [nlo_generator_count](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-generator-count/) | L293-L293 | formalized | — |
| `theorem` | [nlo_factor_65](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65/) | L296-L296 | formalized | — |
| `def` | [quarkColors](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/quark-colors/) | L304-L304 | defined | — |
| `theorem` | [qcd_has_color_factor](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-has-color-factor/) | L307-L308 | formalized | — |
| `theorem` | [em_has_color_factor](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-has-color-factor/) | L311-L312 | formalized | — |
| `theorem` | [qcd_denominator_channel_counting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denominator-channel-counting/) | L321-L322 | formalized | — |
| `theorem` | [qcd_denom_is_2_pow_4](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-is-2-pow-4/) | L325-L325 | formalized | — |
| `theorem` | [em_denominator_channel_counting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denominator-channel-counting/) | L330-L331 | formalized | — |
| `theorem` | [em_denom_decomp](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-decomp/) | L334-L335 | formalized | — |
| `theorem` | [both_coefficients_share_Nc](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/both-coefficients-share-nc/) | L339-L341 | formalized | — |
| `theorem` | [em_numer_factor](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-factor/) | L345-L345 | formalized | — |
| `theorem` | [em_denom_factor](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-factor/) | L348-L348 | formalized | — |
| `def` | [remark_cottingham_comparison](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/remark-cottingham-comparison/) | L372-L375 | defined | `IV.R394` |
| `eval` | [#eval L382](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l382/) | L382-L382 | computed | — |
| `eval` | [#eval L383](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l383/) | L383-L383 | computed | — |
| `eval` | [#eval L386](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l386/) | L386-L391 | computed | — |

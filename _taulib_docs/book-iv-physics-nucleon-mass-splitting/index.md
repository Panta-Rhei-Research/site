---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "permalink": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
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
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-mode/",
      "source_line_start": 59,
      "source_line_end": 62,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D340"
      ]
    },
    {
      "kind": "def",
      "name": "neutronIsChiMinus",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/neutron-is-chi-minus/",
      "source_line_start": 65,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "protonIsChiPlus",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/proton-is-chi-plus/",
      "source_line_start": 68,
      "source_line_end": 68,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nucleon_modes_distinct",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-modes-distinct/",
      "source_line_start": 71,
      "source_line_end": 89,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota5_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-numer/",
      "source_line_start": 92,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota5_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom/",
      "source_line_start": 93,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota2_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-numer/",
      "source_line_start": 96,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota2_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom/",
      "source_line_start": 97,
      "source_line_end": 97,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota6_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-numer/",
      "source_line_start": 100,
      "source_line_end": 100,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota6_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom/",
      "source_line_start": 101,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota11_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-numer/",
      "source_line_start": 104,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota11_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-denom/",
      "source_line_start": 105,
      "source_line_end": 105,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota5_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom-pos/",
      "source_line_start": 108,
      "source_line_end": 108,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota2_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom-pos/",
      "source_line_start": 109,
      "source_line_end": 109,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "iota6_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom-pos/",
      "source_line_start": 110,
      "source_line_end": 124,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.D341"
      ]
    },
    {
      "kind": "def",
      "name": "qcd_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer/",
      "source_line_start": 127,
      "source_line_end": 127,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D341"
      ]
    },
    {
      "kind": "def",
      "name": "qcd_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom/",
      "source_line_start": 130,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D341"
      ]
    },
    {
      "kind": "theorem",
      "name": "qcd_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-pos/",
      "source_line_start": 133,
      "source_line_end": 134,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "qcd_float",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-float/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "qcd_numer_val",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer-val/",
      "source_line_start": 142,
      "source_line_end": 143,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "qcd_denom_val",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-val/",
      "source_line_start": 144,
      "source_line_end": 145,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_in_range",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-in-range/",
      "source_line_start": 150,
      "source_line_end": 172,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.D341",
        "IV.D342"
      ]
    },
    {
      "kind": "def",
      "name": "em_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D342"
      ]
    },
    {
      "kind": "def",
      "name": "em_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom/",
      "source_line_start": 180,
      "source_line_end": 180,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D342"
      ]
    },
    {
      "kind": "theorem",
      "name": "em_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-pos/",
      "source_line_start": 183,
      "source_line_end": 184,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "em_float",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-float/",
      "source_line_start": 187,
      "source_line_end": 188,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "em_numer_val",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-val/",
      "source_line_start": 190,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "em_denom_val",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-val/",
      "source_line_start": 192,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_in_range",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-in-range/",
      "source_line_start": 198,
      "source_line_end": 215,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.D342",
        "IV.T141"
      ]
    },
    {
      "kind": "def",
      "name": "tree_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer/",
      "source_line_start": 218,
      "source_line_end": 218,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.T141"
      ]
    },
    {
      "kind": "def",
      "name": "tree_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.T141"
      ]
    },
    {
      "kind": "theorem",
      "name": "tree_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-pos/",
      "source_line_start": 224,
      "source_line_end": 225,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "tree_numer_val",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer-val/",
      "source_line_start": 227,
      "source_line_end": 228,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "lemma",
      "name": "tree_denom_val",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-val/",
      "source_line_start": 229,
      "source_line_end": 230,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "deltaMassTree_range",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-tree-range/",
      "source_line_start": 235,
      "source_line_end": 258,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T141",
        "IV.T142"
      ]
    },
    {
      "kind": "theorem",
      "name": "pn_sign_positive",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/pn-sign-positive/",
      "source_line_start": 263,
      "source_line_end": 265,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P183"
      ]
    },
    {
      "kind": "theorem",
      "name": "deltaMassTwoSector_range",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-two-sector-range/",
      "source_line_start": 270,
      "source_line_end": 276,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T142"
      ]
    },
    {
      "kind": "theorem",
      "name": "nlo_factor_65_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-numer/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P184"
      ]
    },
    {
      "kind": "theorem",
      "name": "nlo_factor_65_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-denom/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P184"
      ]
    },
    {
      "kind": "theorem",
      "name": "nlo_lobe_color_product",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-lobe-color-product/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nlo_generator_count",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-generator-count/",
      "source_line_start": 293,
      "source_line_end": 293,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nlo_factor_65",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65/",
      "source_line_start": 296,
      "source_line_end": 296,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "quarkColors",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/quark-colors/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_has_color_factor",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-has-color-factor/",
      "source_line_start": 307,
      "source_line_end": 308,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_has_color_factor",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-has-color-factor/",
      "source_line_start": 311,
      "source_line_end": 312,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_denominator_channel_counting",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denominator-channel-counting/",
      "source_line_start": 321,
      "source_line_end": 322,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "qcd_denom_is_2_pow_4",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-is-2-pow-4/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_denominator_channel_counting",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denominator-channel-counting/",
      "source_line_start": 330,
      "source_line_end": 331,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_denom_decomp",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-decomp/",
      "source_line_start": 334,
      "source_line_end": 335,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "both_coefficients_share_Nc",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/both-coefficients-share-nc/",
      "source_line_start": 339,
      "source_line_end": 341,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_numer_factor",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-factor/",
      "source_line_start": 345,
      "source_line_end": 345,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_denom_factor",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-factor/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_cottingham_comparison",
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/remark-cottingham-comparison/",
      "source_line_start": 372,
      "source_line_end": 375,
      "formal_status": "defined",
      "declaration_role": "docstring/data record",
      "formal_status_label": "docstring/data record",
      "registry_ids": [
        "IV.R394"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l382/",
      "source_line_start": 382,
      "source_line_end": 382,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l383/",
      "source_line_start": 383,
      "source_line_end": 383,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l386/",
      "source_line_start": 386,
      "source_line_end": 391,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [NucleonMode](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-mode/) | L59-L62 | type/data schema | type/data schema | `IV.D340` |
| `def` | [neutronIsChiMinus](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/neutron-is-chi-minus/) | L65-L65 | definition | definition | — |
| `def` | [protonIsChiPlus](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/proton-is-chi-plus/) | L68-L68 | definition | definition | — |
| `theorem` | [nucleon_modes_distinct](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-modes-distinct/) | L71-L89 | proof obligation | formal proof obligation checked | — |
| `def` | [iota5_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-numer/) | L92-L92 | data/computed value | data/computed value | — |
| `def` | [iota5_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom/) | L93-L93 | data/computed value | data/computed value | — |
| `def` | [iota2_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-numer/) | L96-L96 | data/computed value | data/computed value | — |
| `def` | [iota2_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom/) | L97-L97 | data/computed value | data/computed value | — |
| `def` | [iota6_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-numer/) | L100-L100 | data/computed value | data/computed value | — |
| `def` | [iota6_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom/) | L101-L101 | data/computed value | data/computed value | — |
| `def` | [iota11_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-numer/) | L104-L104 | data/computed value | data/computed value | — |
| `def` | [iota11_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota11-denom/) | L105-L105 | data/computed value | data/computed value | — |
| `theorem` | [iota5_denom_pos](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota5-denom-pos/) | L108-L108 | proof obligation | formal proof obligation checked | — |
| `theorem` | [iota2_denom_pos](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota2-denom-pos/) | L109-L109 | proof obligation | formal proof obligation checked | — |
| `theorem` | [iota6_denom_pos](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom-pos/) | L110-L124 | proof obligation | formal proof obligation checked | `IV.D341` |
| `def` | [qcd_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer/) | L127-L127 | data/computed value | data/computed value | `IV.D341` |
| `def` | [qcd_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom/) | L130-L130 | data/computed value | data/computed value | `IV.D341` |
| `theorem` | [qcd_denom_pos](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-pos/) | L133-L134 | proof obligation | formal proof obligation checked | — |
| `def` | [qcd_float](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-float/) | L137-L138 | data/computed value | data/computed value | — |
| `lemma` | [qcd_numer_val](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-numer-val/) | L142-L143 | proof obligation | formal proof obligation checked | — |
| `lemma` | [qcd_denom_val](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-val/) | L144-L145 | proof obligation | formal proof obligation checked | — |
| `theorem` | [qcd_in_range](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-in-range/) | L150-L172 | proof obligation | formal proof obligation checked | `IV.D341`, `IV.D342` |
| `def` | [em_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer/) | L176-L176 | data/computed value | data/computed value | `IV.D342` |
| `def` | [em_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom/) | L180-L180 | data/computed value | data/computed value | `IV.D342` |
| `theorem` | [em_denom_pos](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-pos/) | L183-L184 | proof obligation | formal proof obligation checked | — |
| `def` | [em_float](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-float/) | L187-L188 | data/computed value | data/computed value | — |
| `lemma` | [em_numer_val](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-val/) | L190-L191 | proof obligation | formal proof obligation checked | — |
| `lemma` | [em_denom_val](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-val/) | L192-L193 | proof obligation | formal proof obligation checked | — |
| `theorem` | [em_in_range](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-in-range/) | L198-L215 | proof obligation | formal proof obligation checked | `IV.D342`, `IV.T141` |
| `def` | [tree_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer/) | L218-L218 | data/computed value | data/computed value | `IV.T141` |
| `def` | [tree_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom/) | L221-L221 | data/computed value | data/computed value | `IV.T141` |
| `theorem` | [tree_denom_pos](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-pos/) | L224-L225 | proof obligation | formal proof obligation checked | — |
| `lemma` | [tree_numer_val](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-numer-val/) | L227-L228 | proof obligation | formal proof obligation checked | — |
| `lemma` | [tree_denom_val](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom-val/) | L229-L230 | proof obligation | formal proof obligation checked | — |
| `theorem` | [deltaMassTree_range](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-tree-range/) | L235-L258 | proof obligation | formal proof obligation checked | `IV.T141`, `IV.T142` |
| `theorem` | [pn_sign_positive](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/pn-sign-positive/) | L263-L265 | proof obligation | formal proof obligation checked | `IV.P183` |
| `theorem` | [deltaMassTwoSector_range](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-two-sector-range/) | L270-L276 | proof obligation | formal proof obligation checked | `IV.T142` |
| `theorem` | [nlo_factor_65_numer](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-numer/) | L284-L284 | proof obligation | formal proof obligation checked | `IV.P184` |
| `theorem` | [nlo_factor_65_denom](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-denom/) | L287-L287 | proof obligation | formal proof obligation checked | `IV.P184` |
| `theorem` | [nlo_lobe_color_product](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-lobe-color-product/) | L290-L290 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nlo_generator_count](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-generator-count/) | L293-L293 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nlo_factor_65](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65/) | L296-L296 | proof obligation | formal proof obligation checked | — |
| `def` | [quarkColors](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/quark-colors/) | L304-L304 | data/computed value | data/computed value | — |
| `theorem` | [qcd_has_color_factor](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-has-color-factor/) | L307-L308 | proof obligation | formal proof obligation checked | — |
| `theorem` | [em_has_color_factor](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-has-color-factor/) | L311-L312 | proof obligation | formal proof obligation checked | — |
| `theorem` | [qcd_denominator_channel_counting](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denominator-channel-counting/) | L321-L322 | proof obligation | formal proof obligation checked | — |
| `theorem` | [qcd_denom_is_2_pow_4](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-denom-is-2-pow-4/) | L325-L325 | proof obligation | formal proof obligation checked | — |
| `theorem` | [em_denominator_channel_counting](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denominator-channel-counting/) | L330-L331 | proof obligation | formal proof obligation checked | — |
| `theorem` | [em_denom_decomp](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-decomp/) | L334-L335 | proof obligation | formal proof obligation checked | — |
| `theorem` | [both_coefficients_share_Nc](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/both-coefficients-share-nc/) | L339-L341 | proof obligation | formal proof obligation checked | — |
| `theorem` | [em_numer_factor](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-numer-factor/) | L345-L345 | proof obligation | formal proof obligation checked | — |
| `theorem` | [em_denom_factor](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-denom-factor/) | L348-L348 | proof obligation | formal proof obligation checked | — |
| `def` | [remark_cottingham_comparison](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/remark-cottingham-comparison/) | L372-L375 | docstring/data record | docstring/data record | `IV.R394` |
| `eval` | [#eval L382](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l382/) | L382-L382 | computed check | computed check | — |
| `eval` | [#eval L383](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l383/) | L383-L383 | computed check | computed check | — |
| `eval` | [#eval L386](/corpus/taulib/docs/book-iv-physics-nucleon-mass-splitting/eval-l386/) | L386-L391 | computed check | computed check | — |

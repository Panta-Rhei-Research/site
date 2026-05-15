---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.NumberTower",
  "permalink": "/corpus/taulib/docs/book-i-boundary-number-tower/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.NumberTower`.",
  "module_name": "TauLib.BookI.Boundary.NumberTower",
  "module_slug": "book-i-boundary-number-tower",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/NumberTower.lean",
  "sha256": "6b9e18b32208095c80cd5a1957a0c97b7d089c6d890fc64f8375fadeb6895e73",
  "imports": [
    "TauLib.BookI.Denotation.Arithmetic",
    "Mathlib.Tactic.Ring",
    "Mathlib.Tactic.LinearCombination",
    "Mathlib.Tactic.NormNum"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
    "TauLib.BookI.Boundary.Cyclotomic",
    "TauLib.BookI.Boundary.TauRatField"
  ],
  "registry_ids": [
    "I.D14",
    "I.D15",
    "I.D16"
  ],
  "declaration_counts": {
    "structure": 2,
    "def": 22,
    "theorem": 40,
    "eval": 7
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauInt",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tau-int/",
      "source_line_start": 50,
      "source_line_end": 53,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D14"
      ]
    },
    {
      "kind": "def",
      "name": "TauInt.zero",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/zero/",
      "source_line_start": 56,
      "source_line_end": 56,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.one",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/one/",
      "source_line_start": 59,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.add",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/add/",
      "source_line_start": 62,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.negate",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/negate/",
      "source_line_start": 66,
      "source_line_end": 67,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.mul",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/mul/",
      "source_line_start": 70,
      "source_line_end": 71,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.sub",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/sub/",
      "source_line_start": 74,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.fromNat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/from-nat/",
      "source_line_start": 78,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauInt.equiv_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-refl/",
      "source_line_start": 90,
      "source_line_end": 91,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauInt.equiv_symm",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-symm/",
      "source_line_start": 94,
      "source_line_end": 98,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauInt.equiv_trans",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-trans/",
      "source_line_start": 101,
      "source_line_end": 107,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.toInt",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_of_int_eq",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-of-int-eq/",
      "source_line_start": 118,
      "source_line_end": 122,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "int_eq_of_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/int-eq-of-equiv/",
      "source_line_start": 125,
      "source_line_end": 129,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "equiv_iff_toInt_eq",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-iff-to-int-eq/",
      "source_line_start": 132,
      "source_line_end": 136,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toInt_add",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int-add/",
      "source_line_start": 139,
      "source_line_end": 141,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toInt_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int-mul/",
      "source_line_start": 144,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toInt_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int-negate/",
      "source_line_start": 149,
      "source_line_end": 151,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toInt_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int-zero/",
      "source_line_start": 154,
      "source_line_end": 155,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toInt_one",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int-one/",
      "source_line_start": 158,
      "source_line_end": 159,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toInt_fromNat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int-from-nat/",
      "source_line_start": 162,
      "source_line_end": 164,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_add_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-comm/",
      "source_line_start": 171,
      "source_line_end": 173,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_add_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-assoc/",
      "source_line_start": 176,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_add_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-zero/",
      "source_line_start": 181,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_zero_add",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-zero-add/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_add_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-negate/",
      "source_line_start": 191,
      "source_line_end": 193,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_negate_add",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-negate-add/",
      "source_line_start": 196,
      "source_line_end": 198,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_mul_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-comm/",
      "source_line_start": 201,
      "source_line_end": 203,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_mul_assoc",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-assoc/",
      "source_line_start": 206,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_mul_one",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-one/",
      "source_line_start": 211,
      "source_line_end": 213,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_one_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-one-mul/",
      "source_line_start": 216,
      "source_line_end": 218,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_distrib",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-distrib/",
      "source_line_start": 221,
      "source_line_end": 223,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_distrib_right",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-distrib-right/",
      "source_line_start": 226,
      "source_line_end": 228,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauint_mul_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-zero/",
      "source_line_start": 231,
      "source_line_end": 233,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nat_to_tauint",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_to_tauint_injective",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint-injective/",
      "source_line_start": 243,
      "source_line_end": 246,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toInt_nat_to_tauint",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/to-int-nat-to-tauint/",
      "source_line_start": 249,
      "source_line_end": 251,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_to_tauint_add",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint-add/",
      "source_line_start": 254,
      "source_line_end": 258,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_to_tauint_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint-mul/",
      "source_line_start": 261,
      "source_line_end": 265,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauRat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/tau-rat/",
      "source_line_start": 273,
      "source_line_end": 277,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D15"
      ]
    },
    {
      "kind": "def",
      "name": "TauRat.zero",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/zero-l280/",
      "source_line_start": 280,
      "source_line_end": 281,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.one",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/one-l284/",
      "source_line_start": 284,
      "source_line_end": 285,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.add",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/add-l288/",
      "source_line_start": 288,
      "source_line_end": 291,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.mul",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/mul-l294/",
      "source_line_start": 294,
      "source_line_end": 297,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.negate",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/negate-l300/",
      "source_line_start": 300,
      "source_line_end": 301,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.sub",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/sub-l304/",
      "source_line_start": 304,
      "source_line_end": 305,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-l313/",
      "source_line_start": 313,
      "source_line_end": 315,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.equiv_refl",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-refl-l318/",
      "source_line_start": 318,
      "source_line_end": 320,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.equiv_symm",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/equiv-symm-l323/",
      "source_line_start": 323,
      "source_line_end": 326,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_add_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/taurat-add-comm/",
      "source_line_start": 333,
      "source_line_end": 338,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_add_zero",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/taurat-add-zero/",
      "source_line_start": 341,
      "source_line_end": 346,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_add_negate",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/taurat-add-negate/",
      "source_line_start": 349,
      "source_line_end": 354,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_mul_comm",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/taurat-mul-comm/",
      "source_line_start": 357,
      "source_line_end": 362,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "taurat_mul_one",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/taurat-mul-one/",
      "source_line_start": 365,
      "source_line_end": 370,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "int_to_taurat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat/",
      "source_line_start": 377,
      "source_line_end": 378,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "int_to_taurat_injective",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat-injective/",
      "source_line_start": 381,
      "source_line_end": 384,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "int_to_taurat_add",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat-add/",
      "source_line_start": 387,
      "source_line_end": 393,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "int_to_taurat_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat-mul/",
      "source_line_start": 396,
      "source_line_end": 400,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nat_to_taurat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-taurat/",
      "source_line_start": 407,
      "source_line_end": 408,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_to_taurat_injective",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-taurat-injective/",
      "source_line_start": 411,
      "source_line_end": 413,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/eval-l428/",
      "source_line_start": 428,
      "source_line_end": 428,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/eval-l429/",
      "source_line_start": 429,
      "source_line_end": 429,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/eval-l430/",
      "source_line_start": 430,
      "source_line_end": 430,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/eval-l431/",
      "source_line_start": 431,
      "source_line_end": 431,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "halfRat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/half-rat/",
      "source_line_start": 434,
      "source_line_end": 434,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "thirdRat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/third-rat/",
      "source_line_start": 435,
      "source_line_end": 435,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "twoFifthsRat",
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/two-fifths-rat/",
      "source_line_start": 436,
      "source_line_end": 436,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/eval-l437/",
      "source_line_start": 437,
      "source_line_end": 437,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/eval-l438/",
      "source_line_start": 438,
      "source_line_end": 438,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-boundary-number-tower/eval-l439/",
      "source_line_start": 439,
      "source_line_end": 441,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean",
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
- Source path: [`TauLib/BookI/Boundary/NumberTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/NumberTower.lean`
- SHA-256: `6b9e18b32208095c80cd5a1957a0c97b7d089c6d890fc64f8375fadeb6895e73`

## Registry Links

- `I.D14` — Program Monoid
- `I.D15` — Three-Level Equality
- `I.D16` — NF Address Encoding

## Construction Spine Links

- [Recover Core Mathematics](/corpus/construction-spine/recover-core-mathematics/)

## Imports

- `TauLib.BookI.Denotation.Arithmetic`
- `Mathlib.Tactic.Ring`
- `Mathlib.Tactic.LinearCombination`
- `Mathlib.Tactic.NormNum`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Bridge.TauIntQuotient`
- `TauLib.BookI.Boundary.Cyclotomic`
- `TauLib.BookI.Boundary.TauRatField`

## Declaration Counts

- `def`: 22
- `eval`: 7
- `structure`: 2
- `theorem`: 40

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauInt](/corpus/taulib/docs/book-i-boundary-number-tower/tau-int/) | L50-L53 | type/data schema | type/data schema | `I.D14` |
| `def` | [TauInt.zero](/corpus/taulib/docs/book-i-boundary-number-tower/zero/) | L56-L56 | definition | definition | — |
| `def` | [TauInt.one](/corpus/taulib/docs/book-i-boundary-number-tower/one/) | L59-L59 | definition | definition | — |
| `def` | [TauInt.add](/corpus/taulib/docs/book-i-boundary-number-tower/add/) | L62-L63 | definition | definition | — |
| `def` | [TauInt.negate](/corpus/taulib/docs/book-i-boundary-number-tower/negate/) | L66-L67 | definition | definition | — |
| `def` | [TauInt.mul](/corpus/taulib/docs/book-i-boundary-number-tower/mul/) | L70-L71 | definition | definition | — |
| `def` | [TauInt.sub](/corpus/taulib/docs/book-i-boundary-number-tower/sub/) | L74-L75 | definition | definition | — |
| `def` | [TauInt.fromNat](/corpus/taulib/docs/book-i-boundary-number-tower/from-nat/) | L78-L78 | definition | definition | — |
| `def` | [TauInt.equiv](/corpus/taulib/docs/book-i-boundary-number-tower/equiv/) | L86-L87 | definition | definition | — |
| `theorem` | [TauInt.equiv_refl](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-refl/) | L90-L91 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauInt.equiv_symm](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-symm/) | L94-L98 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauInt.equiv_trans](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-trans/) | L101-L107 | proof obligation | formal proof obligation checked | — |
| `def` | [TauInt.toInt](/corpus/taulib/docs/book-i-boundary-number-tower/to-int/) | L114-L115 | data/computed value | data/computed value | — |
| `theorem` | [equiv_of_int_eq](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-of-int-eq/) | L118-L122 | proof obligation | formal proof obligation checked | — |
| `theorem` | [int_eq_of_equiv](/corpus/taulib/docs/book-i-boundary-number-tower/int-eq-of-equiv/) | L125-L129 | proof obligation | formal proof obligation checked | — |
| `theorem` | [equiv_iff_toInt_eq](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-iff-to-int-eq/) | L132-L136 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toInt_add](/corpus/taulib/docs/book-i-boundary-number-tower/to-int-add/) | L139-L141 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toInt_mul](/corpus/taulib/docs/book-i-boundary-number-tower/to-int-mul/) | L144-L146 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toInt_negate](/corpus/taulib/docs/book-i-boundary-number-tower/to-int-negate/) | L149-L151 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toInt_zero](/corpus/taulib/docs/book-i-boundary-number-tower/to-int-zero/) | L154-L155 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toInt_one](/corpus/taulib/docs/book-i-boundary-number-tower/to-int-one/) | L158-L159 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toInt_fromNat](/corpus/taulib/docs/book-i-boundary-number-tower/to-int-from-nat/) | L162-L164 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_add_comm](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-comm/) | L171-L173 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_add_assoc](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-assoc/) | L176-L178 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_add_zero](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-zero/) | L181-L183 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_zero_add](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-zero-add/) | L186-L188 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_add_negate](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-add-negate/) | L191-L193 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_negate_add](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-negate-add/) | L196-L198 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_mul_comm](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-comm/) | L201-L203 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_mul_assoc](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-assoc/) | L206-L208 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_mul_one](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-one/) | L211-L213 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_one_mul](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-one-mul/) | L216-L218 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_distrib](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-distrib/) | L221-L223 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_distrib_right](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-distrib-right/) | L226-L228 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tauint_mul_zero](/corpus/taulib/docs/book-i-boundary-number-tower/tauint-mul-zero/) | L231-L233 | proof obligation | formal proof obligation checked | — |
| `def` | [nat_to_tauint](/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint/) | L240-L240 | definition | definition | — |
| `theorem` | [nat_to_tauint_injective](/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint-injective/) | L243-L246 | proof obligation | formal proof obligation checked | — |
| `theorem` | [toInt_nat_to_tauint](/corpus/taulib/docs/book-i-boundary-number-tower/to-int-nat-to-tauint/) | L249-L251 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nat_to_tauint_add](/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint-add/) | L254-L258 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nat_to_tauint_mul](/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-tauint-mul/) | L261-L265 | proof obligation | formal proof obligation checked | — |
| `structure` | [TauRat](/corpus/taulib/docs/book-i-boundary-number-tower/tau-rat/) | L273-L277 | type/data schema | type/data schema | `I.D15` |
| `def` | [TauRat.zero](/corpus/taulib/docs/book-i-boundary-number-tower/zero-l280/) | L280-L281 | definition | definition | — |
| `def` | [TauRat.one](/corpus/taulib/docs/book-i-boundary-number-tower/one-l284/) | L284-L285 | definition | definition | — |
| `def` | [TauRat.add](/corpus/taulib/docs/book-i-boundary-number-tower/add-l288/) | L288-L291 | definition | definition | — |
| `def` | [TauRat.mul](/corpus/taulib/docs/book-i-boundary-number-tower/mul-l294/) | L294-L297 | definition | definition | — |
| `def` | [TauRat.negate](/corpus/taulib/docs/book-i-boundary-number-tower/negate-l300/) | L300-L301 | definition | definition | — |
| `def` | [TauRat.sub](/corpus/taulib/docs/book-i-boundary-number-tower/sub-l304/) | L304-L305 | definition | definition | — |
| `def` | [TauRat.equiv](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-l313/) | L313-L315 | definition | definition | — |
| `theorem` | [TauRat.equiv_refl](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-refl-l318/) | L318-L320 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauRat.equiv_symm](/corpus/taulib/docs/book-i-boundary-number-tower/equiv-symm-l323/) | L323-L326 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_add_comm](/corpus/taulib/docs/book-i-boundary-number-tower/taurat-add-comm/) | L333-L338 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_add_zero](/corpus/taulib/docs/book-i-boundary-number-tower/taurat-add-zero/) | L341-L346 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_add_negate](/corpus/taulib/docs/book-i-boundary-number-tower/taurat-add-negate/) | L349-L354 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_mul_comm](/corpus/taulib/docs/book-i-boundary-number-tower/taurat-mul-comm/) | L357-L362 | proof obligation | formal proof obligation checked | — |
| `theorem` | [taurat_mul_one](/corpus/taulib/docs/book-i-boundary-number-tower/taurat-mul-one/) | L365-L370 | proof obligation | formal proof obligation checked | — |
| `def` | [int_to_taurat](/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat/) | L377-L378 | definition | definition | — |
| `theorem` | [int_to_taurat_injective](/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat-injective/) | L381-L384 | proof obligation | formal proof obligation checked | — |
| `theorem` | [int_to_taurat_add](/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat-add/) | L387-L393 | proof obligation | formal proof obligation checked | — |
| `theorem` | [int_to_taurat_mul](/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat-mul/) | L396-L400 | proof obligation | formal proof obligation checked | — |
| `def` | [nat_to_taurat](/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-taurat/) | L407-L408 | definition | definition | — |
| `theorem` | [nat_to_taurat_injective](/corpus/taulib/docs/book-i-boundary-number-tower/nat-to-taurat-injective/) | L411-L413 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L428](/corpus/taulib/docs/book-i-boundary-number-tower/eval-l428/) | L428-L428 | computed check | computed check | — |
| `eval` | [#eval L429](/corpus/taulib/docs/book-i-boundary-number-tower/eval-l429/) | L429-L429 | computed check | computed check | — |
| `eval` | [#eval L430](/corpus/taulib/docs/book-i-boundary-number-tower/eval-l430/) | L430-L430 | computed check | computed check | — |
| `eval` | [#eval L431](/corpus/taulib/docs/book-i-boundary-number-tower/eval-l431/) | L431-L431 | computed check | computed check | — |
| `def` | [halfRat](/corpus/taulib/docs/book-i-boundary-number-tower/half-rat/) | L434-L434 | definition | definition | — |
| `def` | [thirdRat](/corpus/taulib/docs/book-i-boundary-number-tower/third-rat/) | L435-L435 | definition | definition | — |
| `def` | [twoFifthsRat](/corpus/taulib/docs/book-i-boundary-number-tower/two-fifths-rat/) | L436-L436 | definition | definition | — |
| `eval` | [#eval L437](/corpus/taulib/docs/book-i-boundary-number-tower/eval-l437/) | L437-L437 | computed check | computed check | — |
| `eval` | [#eval L438](/corpus/taulib/docs/book-i-boundary-number-tower/eval-l438/) | L438-L438 | computed check | computed check | — |
| `eval` | [#eval L439](/corpus/taulib/docs/book-i-boundary-number-tower/eval-l439/) | L439-L441 | computed check | computed check | — |

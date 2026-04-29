---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Holomorphy.PresheafEssence",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_slug": "book-i-holomorphy-presheaf-essence",
  "book": "BookI",
  "family": "Holomorphy",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Holomorphy/PresheafEssence.lean",
  "sha256": "8e1c470082689bb27b8a760c057000165184eee88e15250046a83274fff27f35",
  "imports": [
    "TauLib.BookI.Holomorphy.BoundaryInterior",
    "TauLib.BookI.Holomorphy.SpectralCoefficients"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookII.Closure.GeometricBiSquare"
  ],
  "registry_ids": [
    "I.D83",
    "I.T31",
    "I.T40",
    "I.T41"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 10,
    "theorem": 12,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PrimorialPresheaf",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/primorial-presheaf/",
      "source_line_start": 49,
      "source_line_end": 51,
      "formal_status": "defined",
      "registry_ids": [
        "I.D83"
      ]
    },
    {
      "kind": "def",
      "name": "presheaf_of_nat",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/presheaf-of-nat/",
      "source_line_start": 55,
      "source_line_end": 57,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "presheaf_value_reduced",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/presheaf-value-reduced/",
      "source_line_start": 60,
      "source_line_end": 62,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "IsNatTrans",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/is-nat-trans/",
      "source_line_start": 70,
      "source_line_end": 70,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_trans_iff_tower_coherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/nat-trans-iff-tower-coherent/",
      "source_line_start": 73,
      "source_line_end": 74,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "presheaf_characterization",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/presheaf-characterization/",
      "source_line_start": 82,
      "source_line_end": 84,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T40"
      ]
    },
    {
      "kind": "theorem",
      "name": "nat_trans_gives_holfun",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/nat-trans-gives-holfun/",
      "source_line_start": 87,
      "source_line_end": 90,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BiSquare",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/bi-square/",
      "source_line_start": 102,
      "source_line_end": 109,
      "formal_status": "defined",
      "registry_ids": [
        "I.T41"
      ]
    },
    {
      "kind": "def",
      "name": "BiSquare.tower_coherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/tower-coherent/",
      "source_line_start": 116,
      "source_line_end": 117,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "BiSquare.of_coherent",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/of-coherent/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bi_square_characterization",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/bi-square-characterization/",
      "source_line_start": 125,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T41"
      ]
    },
    {
      "kind": "def",
      "name": "BiSquare.toHolFun",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/to-hol-fun/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "HolFun.toBiSquare",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/to-bi-square/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "holfun_bisquare_roundtrip",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/holfun-bisquare-roundtrip/",
      "source_line_start": 140,
      "source_line_end": 141,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "spectral_coeff_ext",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/spectral-coeff-ext/",
      "source_line_start": 148,
      "source_line_end": 151,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "right_from_left",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/right-from-left/",
      "source_line_start": 160,
      "source_line_end": 170,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "right_from_left'",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/right-from-left-l173/",
      "source_line_start": 173,
      "source_line_end": 178,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "limit_determines_stages",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/limit-determines-stages/",
      "source_line_start": 186,
      "source_line_end": 191,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "limit_determines_spectral",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/limit-determines-spectral/",
      "source_line_start": 194,
      "source_line_end": 202,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_bisquare",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/chi-plus-bisquare/",
      "source_line_start": 209,
      "source_line_end": 210,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_bisquare",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/chi-minus-bisquare/",
      "source_line_start": 213,
      "source_line_end": 214,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "id_bisquare",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/id-bisquare/",
      "source_line_start": 217,
      "source_line_end": 218,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "chi_plus_right_square",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/chi-plus-right-square/",
      "source_line_start": 221,
      "source_line_end": 225,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BookICrownJewel",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/book-icrown-jewel/",
      "source_line_start": 234,
      "source_line_end": 252,
      "formal_status": "defined",
      "registry_ids": [
        "I.T31",
        "I.T40",
        "I.T41"
      ]
    },
    {
      "kind": "def",
      "name": "book_i_crown_jewel",
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/book-i-crown-jewel/",
      "source_line_start": 256,
      "source_line_end": 260,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/eval-l267/",
      "source_line_start": 267,
      "source_line_end": 267,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/eval-l268/",
      "source_line_start": 268,
      "source_line_end": 268,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/eval-l269/",
      "source_line_start": 269,
      "source_line_end": 287,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean",
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
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Holomorphy/PresheafEssence.lean`
- SHA-256: `8e1c470082689bb27b8a760c057000165184eee88e15250046a83274fff27f35`

## Registry Links

- `I.D83` — Primorial Presheaf
- `I.T31` — Global Hartogs Extension
- `I.T40` — Presheaf Characterization
- `I.T41` — Bi-Square Characterization

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Holomorphy.BoundaryInterior`
- `TauLib.BookI.Holomorphy.SpectralCoefficients`

## Imported By

- `TauLib.BookI`
- `TauLib.BookII.Closure.GeometricBiSquare`

## Declaration Counts

- `def`: 10
- `eval`: 3
- `structure`: 3
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [PrimorialPresheaf](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/primorial-presheaf/) | L49-L51 | defined | `I.D83` |
| `def` | [presheaf_of_nat](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/presheaf-of-nat/) | L55-L57 | defined | — |
| `theorem` | [presheaf_value_reduced](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/presheaf-value-reduced/) | L60-L62 | formalized | — |
| `def` | [IsNatTrans](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/is-nat-trans/) | L70-L70 | defined | — |
| `theorem` | [nat_trans_iff_tower_coherent](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/nat-trans-iff-tower-coherent/) | L73-L74 | formalized | — |
| `theorem` | [presheaf_characterization](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/presheaf-characterization/) | L82-L84 | formalized | `I.T40` |
| `theorem` | [nat_trans_gives_holfun](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/nat-trans-gives-holfun/) | L87-L90 | formalized | — |
| `structure` | [BiSquare](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/bi-square/) | L102-L109 | defined | `I.T41` |
| `def` | [BiSquare.tower_coherent](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/tower-coherent/) | L116-L117 | defined | — |
| `def` | [BiSquare.of_coherent](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/of-coherent/) | L120-L121 | defined | — |
| `theorem` | [bi_square_characterization](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/bi-square-characterization/) | L125-L129 | formalized | `I.T41` |
| `def` | [BiSquare.toHolFun](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/to-hol-fun/) | L132-L133 | defined | — |
| `def` | [HolFun.toBiSquare](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/to-bi-square/) | L136-L137 | defined | — |
| `theorem` | [holfun_bisquare_roundtrip](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/holfun-bisquare-roundtrip/) | L140-L141 | formalized | — |
| `theorem` | [spectral_coeff_ext](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/spectral-coeff-ext/) | L148-L151 | formalized | — |
| `theorem` | [right_from_left](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/right-from-left/) | L160-L170 | formalized | — |
| `theorem` | [right_from_left'](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/right-from-left-l173/) | L173-L178 | formalized | — |
| `theorem` | [limit_determines_stages](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/limit-determines-stages/) | L186-L191 | formalized | — |
| `theorem` | [limit_determines_spectral](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/limit-determines-spectral/) | L194-L202 | formalized | — |
| `def` | [chi_plus_bisquare](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/chi-plus-bisquare/) | L209-L210 | defined | — |
| `def` | [chi_minus_bisquare](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/chi-minus-bisquare/) | L213-L214 | defined | — |
| `def` | [id_bisquare](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/id-bisquare/) | L217-L218 | defined | — |
| `theorem` | [chi_plus_right_square](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/chi-plus-right-square/) | L221-L225 | formalized | — |
| `structure` | [BookICrownJewel](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/book-icrown-jewel/) | L234-L252 | defined | `I.T31`, `I.T40`, `I.T41` |
| `def` | [book_i_crown_jewel](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/book-i-crown-jewel/) | L256-L260 | defined | — |
| `eval` | [#eval L267](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/eval-l267/) | L267-L267 | computed | — |
| `eval` | [#eval L268](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/eval-l268/) | L268-L268 | computed | — |
| `eval` | [#eval L269](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/eval-l269/) | L269-L287 | computed | — |

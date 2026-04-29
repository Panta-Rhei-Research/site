---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_slug": "book-ii-central-theorem-boundary-characters",
  "book": "BookII",
  "family": "CentralTheorem",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean",
  "sha256": "037bf20172937ecc178274d017d00dfabf874db2c9ff02d09f335cc609d5f736",
  "imports": [
    "TauLib.BookII.Enrichment.EnrichmentLadder"
  ],
  "imported_by": [
    "TauLib.BookII",
    "TauLib.BookII.CentralTheorem.HartogsExtension",
    "TauLib.Tour.CentralTheorem"
  ],
  "registry_ids": [
    "II.D59",
    "II.P14"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 16,
    "theorem": 15,
    "eval": 11
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "IdempotentCharacter",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idempotent-character/",
      "source_line_start": 58,
      "source_line_end": 63,
      "formal_status": "defined",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "def",
      "name": "IdempotentCharacter.eval",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval/",
      "source_line_start": 66,
      "source_line_end": 67,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_character",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/canonical-character/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_plus_character",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/chi-plus-character/",
      "source_line_start": 76,
      "source_line_end": 78,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chi_minus_character",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/chi-minus-character/",
      "source_line_start": 81,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idemp_character_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-character-check/",
      "source_line_start": 95,
      "source_line_end": 115,
      "formal_status": "defined",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "def",
      "name": "character_tower_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-tower-check/",
      "source_line_start": 129,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "IdempotentCharacter.add",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/add/",
      "source_line_start": 153,
      "source_line_end": 155,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "character_add_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-add-check/",
      "source_line_start": 164,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "def",
      "name": "IdempotentCharacter.mul",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/mul/",
      "source_line_start": 189,
      "source_line_end": 191,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "character_mul_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-check/",
      "source_line_start": 201,
      "source_line_end": 219,
      "formal_status": "defined",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "def",
      "name": "zero_character",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/zero-character/",
      "source_line_start": 226,
      "source_line_end": 227,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "unit_character",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/unit-character/",
      "source_line_start": 230,
      "source_line_end": 231,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "character_add_identity_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-add-identity-check/",
      "source_line_start": 235,
      "source_line_end": 246,
      "formal_status": "defined",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "def",
      "name": "character_mul_identity_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-identity-check/",
      "source_line_start": 250,
      "source_line_end": 261,
      "formal_status": "defined",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "def",
      "name": "character_distributive_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-distributive-check/",
      "source_line_start": 265,
      "source_line_end": 283,
      "formal_status": "defined",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "def",
      "name": "full_boundary_characters_check",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/full-boundary-characters-check/",
      "source_line_start": 295,
      "source_line_end": 302,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idemp_decomp_recovery",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-decomp-recovery/",
      "source_line_start": 311,
      "source_line_end": 314,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "theorem",
      "name": "b_channel_kills_c",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/b-channel-kills-c/",
      "source_line_start": 317,
      "source_line_end": 319,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "theorem",
      "name": "c_channel_kills_b",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/c-channel-kills-b/",
      "source_line_start": 322,
      "source_line_end": 324,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "theorem",
      "name": "character_tower_structural",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-tower-structural/",
      "source_line_start": 329,
      "source_line_end": 331,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "theorem",
      "name": "character_add_structural",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-add-structural/",
      "source_line_start": 335,
      "source_line_end": 339,
      "formal_status": "formalized",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "theorem",
      "name": "character_mul_structural",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-structural/",
      "source_line_start": 343,
      "source_line_end": 347,
      "formal_status": "formalized",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "theorem",
      "name": "sector_distributive",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/sector-distributive/",
      "source_line_start": 350,
      "source_line_end": 354,
      "formal_status": "formalized",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l361/",
      "source_line_start": 361,
      "source_line_end": 361,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l362/",
      "source_line_start": 362,
      "source_line_end": 362,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l363/",
      "source_line_start": 363,
      "source_line_end": 363,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l366/",
      "source_line_start": 366,
      "source_line_end": 366,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l369/",
      "source_line_start": 369,
      "source_line_end": 369,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l372/",
      "source_line_start": 372,
      "source_line_end": 372,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l375/",
      "source_line_start": 375,
      "source_line_end": 375,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l378/",
      "source_line_start": 378,
      "source_line_end": 378,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l379/",
      "source_line_start": 379,
      "source_line_end": 379,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l380/",
      "source_line_start": 380,
      "source_line_end": 380,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l383/",
      "source_line_start": 383,
      "source_line_end": 383,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idemp_char_20_4",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-char-20-4/",
      "source_line_start": 390,
      "source_line_end": 391,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "theorem",
      "name": "char_tower_20_4",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-tower-20-4/",
      "source_line_start": 394,
      "source_line_end": 395,
      "formal_status": "formalized",
      "registry_ids": [
        "II.D59"
      ]
    },
    {
      "kind": "theorem",
      "name": "char_add_15_3",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-add-15-3/",
      "source_line_start": 398,
      "source_line_end": 399,
      "formal_status": "formalized",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "theorem",
      "name": "char_mul_15_3",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-mul-15-3/",
      "source_line_start": 402,
      "source_line_end": 403,
      "formal_status": "formalized",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "theorem",
      "name": "char_add_id_15_3",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-add-id-15-3/",
      "source_line_start": 406,
      "source_line_end": 407,
      "formal_status": "formalized",
      "registry_ids": [
        "II.P14"
      ]
    },
    {
      "kind": "theorem",
      "name": "char_mul_id_15_3",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-mul-id-15-3/",
      "source_line_start": 409,
      "source_line_end": 410,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "char_distrib_15_3",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-distrib-15-3/",
      "source_line_start": 412,
      "source_line_end": 413,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "full_bnd_char_15_3",
      "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/full-bnd-char-15-3/",
      "source_line_start": 416,
      "source_line_end": 419,
      "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean",
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
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`
- SHA-256: `037bf20172937ecc178274d017d00dfabf874db2c9ff02d09f335cc609d5f736`

## Registry Links

- `II.D59` — Idempotent-Supported Character
- `II.P14` — Character Algebra Ring Structure

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookII.Enrichment.EnrichmentLadder`

## Imported By

- `TauLib.BookII`
- `TauLib.BookII.CentralTheorem.HartogsExtension`
- `TauLib.Tour.CentralTheorem`

## Declaration Counts

- `def`: 16
- `eval`: 11
- `structure`: 1
- `theorem`: 15

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [IdempotentCharacter](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idempotent-character/) | L58-L63 | defined | `II.D59` |
| `def` | [IdempotentCharacter.eval](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval/) | L66-L67 | defined | — |
| `def` | [canonical_character](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/canonical-character/) | L71-L73 | defined | — |
| `def` | [chi_plus_character](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/chi-plus-character/) | L76-L78 | defined | — |
| `def` | [chi_minus_character](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/chi-minus-character/) | L81-L83 | defined | — |
| `def` | [idemp_character_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-character-check/) | L95-L115 | defined | `II.D59` |
| `def` | [character_tower_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-tower-check/) | L129-L146 | defined | — |
| `def` | [IdempotentCharacter.add](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/add/) | L153-L155 | defined | — |
| `def` | [character_add_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-add-check/) | L164-L182 | defined | `II.P14` |
| `def` | [IdempotentCharacter.mul](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/mul/) | L189-L191 | defined | — |
| `def` | [character_mul_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-check/) | L201-L219 | defined | `II.P14` |
| `def` | [zero_character](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/zero-character/) | L226-L227 | defined | — |
| `def` | [unit_character](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/unit-character/) | L230-L231 | defined | — |
| `def` | [character_add_identity_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-add-identity-check/) | L235-L246 | defined | `II.P14` |
| `def` | [character_mul_identity_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-identity-check/) | L250-L261 | defined | `II.P14` |
| `def` | [character_distributive_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-distributive-check/) | L265-L283 | defined | `II.P14` |
| `def` | [full_boundary_characters_check](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/full-boundary-characters-check/) | L295-L302 | defined | — |
| `theorem` | [idemp_decomp_recovery](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-decomp-recovery/) | L311-L314 | formalized | `II.D59` |
| `theorem` | [b_channel_kills_c](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/b-channel-kills-c/) | L317-L319 | formalized | `II.D59` |
| `theorem` | [c_channel_kills_b](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/c-channel-kills-b/) | L322-L324 | formalized | `II.D59` |
| `theorem` | [character_tower_structural](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-tower-structural/) | L329-L331 | formalized | `II.D59` |
| `theorem` | [character_add_structural](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-add-structural/) | L335-L339 | formalized | `II.P14` |
| `theorem` | [character_mul_structural](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-mul-structural/) | L343-L347 | formalized | `II.P14` |
| `theorem` | [sector_distributive](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/sector-distributive/) | L350-L354 | formalized | `II.P14` |
| `eval` | [#eval L361](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l361/) | L361-L361 | computed | — |
| `eval` | [#eval L362](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l362/) | L362-L362 | computed | — |
| `eval` | [#eval L363](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l363/) | L363-L363 | computed | — |
| `eval` | [#eval L366](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l366/) | L366-L366 | computed | — |
| `eval` | [#eval L369](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l369/) | L369-L369 | computed | — |
| `eval` | [#eval L372](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l372/) | L372-L372 | computed | — |
| `eval` | [#eval L375](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l375/) | L375-L375 | computed | — |
| `eval` | [#eval L378](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l378/) | L378-L378 | computed | — |
| `eval` | [#eval L379](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l379/) | L379-L379 | computed | — |
| `eval` | [#eval L380](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l380/) | L380-L380 | computed | — |
| `eval` | [#eval L383](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/eval-l383/) | L383-L383 | computed | — |
| `theorem` | [idemp_char_20_4](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-char-20-4/) | L390-L391 | formalized | `II.D59` |
| `theorem` | [char_tower_20_4](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-tower-20-4/) | L394-L395 | formalized | `II.D59` |
| `theorem` | [char_add_15_3](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-add-15-3/) | L398-L399 | formalized | `II.P14` |
| `theorem` | [char_mul_15_3](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-mul-15-3/) | L402-L403 | formalized | `II.P14` |
| `theorem` | [char_add_id_15_3](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-add-id-15-3/) | L406-L407 | formalized | `II.P14` |
| `theorem` | [char_mul_id_15_3](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-mul-id-15-3/) | L409-L410 | formalized | — |
| `theorem` | [char_distrib_15_3](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/char-distrib-15-3/) | L412-L413 | formalized | — |
| `theorem` | [full_bnd_char_15_3](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/full-bnd-char-15-3/) | L416-L419 | formalized | — |

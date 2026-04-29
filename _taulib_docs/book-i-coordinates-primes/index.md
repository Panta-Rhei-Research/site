---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Coordinates.Primes",
  "permalink": "/verify/taulib/docs/book-i-coordinates-primes/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Coordinates.Primes`.",
  "module_name": "TauLib.BookI.Coordinates.Primes",
  "module_slug": "book-i-coordinates-primes",
  "book": "BookI",
  "family": "Coordinates",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Coordinates/Primes.lean",
  "sha256": "75fa54f9990c10aa751fde51ba62770944c5941d6cd88ae84b3432f84678c29e",
  "imports": [
    "TauLib.BookI.Denotation.Arithmetic"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Coordinates.PrimeEnumeration",
    "TauLib.BookI.Coordinates.TowerAtoms",
    "TauLib.BookI.Polarity.ModArith",
    "TauLib.BookI.Polarity.PrimeBridge",
    "TauLib.BookI.Sets.Membership",
    "TauLib.BookII.Interior.TauAdmissible"
  ],
  "registry_ids": [
    "I.T09"
  ],
  "declaration_counts": {
    "theorem": 29,
    "def": 11,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "nat_dvd_refl",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-refl/",
      "source_line_start": 26,
      "source_line_end": 26,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_dvd_trans",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-trans/",
      "source_line_start": 28,
      "source_line_end": 30,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_dvd_mul_right",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-mul-right/",
      "source_line_start": 32,
      "source_line_end": 32,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_dvd_mul_of_dvd",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-mul-of-dvd/",
      "source_line_start": 34,
      "source_line_end": 36,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_divides",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides/",
      "source_line_start": 43,
      "source_line_end": 43,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_divides_iff_nat_dvd",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides-iff-nat-dvd/",
      "source_line_start": 46,
      "source_line_end": 52,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_divides_refl",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides-refl/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_divides_trans",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides-trans/",
      "source_line_start": 61,
      "source_line_end": 65,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_one_divides",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-one-divides/",
      "source_line_start": 67,
      "source_line_end": 68,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_divides_zero",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides-zero/",
      "source_line_start": 70,
      "source_line_end": 71,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_divides_le",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides-le/",
      "source_line_start": 73,
      "source_line_end": 74,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_divides_antisymm",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-divides-antisymm/",
      "source_line_start": 76,
      "source_line_end": 79,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_prime",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-prime/",
      "source_line_start": 86,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "no_factor_below",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/no-factor-below/",
      "source_line_start": 90,
      "source_line_end": 96,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "is_prime_bool",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/is-prime-bool/",
      "source_line_start": 99,
      "source_line_end": 99,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "exists_prime_divisor",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/exists-prime-divisor/",
      "source_line_start": 106,
      "source_line_end": 135,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_gcd",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-gcd/",
      "source_line_start": 141,
      "source_line_end": 141,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_gcd_dvd_left",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-gcd-dvd-left/",
      "source_line_start": 143,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_gcd_dvd_right",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-gcd-dvd-right/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_dvd_gcd",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-dvd-gcd/",
      "source_line_start": 146,
      "source_line_end": 147,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_coprime",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-coprime/",
      "source_line_start": 153,
      "source_line_end": 153,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "prime_coprime_of_not_dvd",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/prime-coprime-of-not-dvd/",
      "source_line_start": 155,
      "source_line_end": 161,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "coprime_dvd_of_dvd_mul",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/coprime-dvd-of-dvd-mul/",
      "source_line_start": 164,
      "source_line_end": 167,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "euclid_lemma",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/euclid-lemma/",
      "source_line_start": 170,
      "source_line_end": 174,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "idx_factorial",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-factorial/",
      "source_line_start": 180,
      "source_line_end": 182,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "idx_factorial_pos",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/idx-factorial-pos/",
      "source_line_start": 184,
      "source_line_end": 187,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "prime_dvd_factorial",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/prime-dvd-factorial/",
      "source_line_start": 190,
      "source_line_end": 204,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "not_dvd_succ_of_ge_two",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/not-dvd-succ-of-ge-two/",
      "source_line_start": 207,
      "source_line_end": 223,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primes_infinite",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/primes-infinite/",
      "source_line_start": 226,
      "source_line_end": 232,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "list_prod",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/list-prod/",
      "source_line_start": 238,
      "source_line_end": 240,
      "formal_status": "defined",
      "registry_ids": [
        "I.T09"
      ]
    },
    {
      "kind": "theorem",
      "name": "prime_product_exists",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/prime-product-exists/",
      "source_line_start": 243,
      "source_line_end": 273,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "list_prod_pos_of_primes",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/list-prod-pos-of-primes/",
      "source_line_start": 280,
      "source_line_end": 289,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "prod_one_implies_nil",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/prod-one-implies-nil/",
      "source_line_start": 292,
      "source_line_end": 302,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "prime_mem_of_dvd_prod",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/prime-mem-of-dvd-prod/",
      "source_line_start": 305,
      "source_line_end": 320,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_mul_cancel_left",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/nat-mul-cancel-left/",
      "source_line_start": 323,
      "source_line_end": 334,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_ge",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/all-ge/",
      "source_line_start": 339,
      "source_line_end": 341,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mem_ge_of_all_ge",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/mem-ge-of-all-ge/",
      "source_line_start": 343,
      "source_line_end": 350,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sorted_nd",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/sorted-nd/",
      "source_line_start": 353,
      "source_line_end": 355,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "prime_product_unique",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/prime-product-unique/",
      "source_line_start": 359,
      "source_line_end": 407,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T09"
      ]
    },
    {
      "kind": "def",
      "name": "p_adic_val",
      "url": "/verify/taulib/docs/book-i-coordinates-primes/p-adic-val/",
      "source_line_start": 414,
      "source_line_end": 424,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-coordinates-primes/eval-l430/",
      "source_line_start": 430,
      "source_line_end": 430,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-coordinates-primes/eval-l431/",
      "source_line_start": 431,
      "source_line_end": 431,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-coordinates-primes/eval-l432/",
      "source_line_start": 432,
      "source_line_end": 432,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-coordinates-primes/eval-l433/",
      "source_line_start": 433,
      "source_line_end": 433,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-coordinates-primes/eval-l434/",
      "source_line_start": 434,
      "source_line_end": 434,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-coordinates-primes/eval-l435/",
      "source_line_start": 435,
      "source_line_end": 437,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean",
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
- Source path: [`TauLib/BookI/Coordinates/Primes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Primes.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Coordinates/Primes.lean`
- SHA-256: `75fa54f9990c10aa751fde51ba62770944c5941d6cd88ae84b3432f84678c29e`

## Registry Links

- `I.T09` — FTA on tau-Idx

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Denotation.Arithmetic`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Coordinates.PrimeEnumeration`
- `TauLib.BookI.Coordinates.TowerAtoms`
- `TauLib.BookI.Polarity.ModArith`
- `TauLib.BookI.Polarity.PrimeBridge`
- `TauLib.BookI.Sets.Membership`
- `TauLib.BookII.Interior.TauAdmissible`

## Declaration Counts

- `def`: 11
- `eval`: 6
- `theorem`: 29

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [nat_dvd_refl](/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-refl/) | L26-L26 | formalized | — |
| `theorem` | [nat_dvd_trans](/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-trans/) | L28-L30 | formalized | — |
| `theorem` | [nat_dvd_mul_right](/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-mul-right/) | L32-L32 | formalized | — |
| `theorem` | [nat_dvd_mul_of_dvd](/verify/taulib/docs/book-i-coordinates-primes/nat-dvd-mul-of-dvd/) | L34-L36 | formalized | — |
| `def` | [idx_divides](/verify/taulib/docs/book-i-coordinates-primes/idx-divides/) | L43-L43 | defined | — |
| `theorem` | [idx_divides_iff_nat_dvd](/verify/taulib/docs/book-i-coordinates-primes/idx-divides-iff-nat-dvd/) | L46-L52 | formalized | — |
| `theorem` | [idx_divides_refl](/verify/taulib/docs/book-i-coordinates-primes/idx-divides-refl/) | L58-L59 | formalized | — |
| `theorem` | [idx_divides_trans](/verify/taulib/docs/book-i-coordinates-primes/idx-divides-trans/) | L61-L65 | formalized | — |
| `theorem` | [idx_one_divides](/verify/taulib/docs/book-i-coordinates-primes/idx-one-divides/) | L67-L68 | formalized | — |
| `theorem` | [idx_divides_zero](/verify/taulib/docs/book-i-coordinates-primes/idx-divides-zero/) | L70-L71 | formalized | — |
| `theorem` | [idx_divides_le](/verify/taulib/docs/book-i-coordinates-primes/idx-divides-le/) | L73-L74 | formalized | — |
| `theorem` | [idx_divides_antisymm](/verify/taulib/docs/book-i-coordinates-primes/idx-divides-antisymm/) | L76-L79 | formalized | — |
| `def` | [idx_prime](/verify/taulib/docs/book-i-coordinates-primes/idx-prime/) | L86-L87 | defined | — |
| `def` | [no_factor_below](/verify/taulib/docs/book-i-coordinates-primes/no-factor-below/) | L90-L96 | defined | — |
| `def` | [is_prime_bool](/verify/taulib/docs/book-i-coordinates-primes/is-prime-bool/) | L99-L99 | defined | — |
| `theorem` | [exists_prime_divisor](/verify/taulib/docs/book-i-coordinates-primes/exists-prime-divisor/) | L106-L135 | formalized | — |
| `def` | [idx_gcd](/verify/taulib/docs/book-i-coordinates-primes/idx-gcd/) | L141-L141 | defined | — |
| `theorem` | [idx_gcd_dvd_left](/verify/taulib/docs/book-i-coordinates-primes/idx-gcd-dvd-left/) | L143-L143 | formalized | — |
| `theorem` | [idx_gcd_dvd_right](/verify/taulib/docs/book-i-coordinates-primes/idx-gcd-dvd-right/) | L144-L144 | formalized | — |
| `theorem` | [idx_dvd_gcd](/verify/taulib/docs/book-i-coordinates-primes/idx-dvd-gcd/) | L146-L147 | formalized | — |
| `def` | [idx_coprime](/verify/taulib/docs/book-i-coordinates-primes/idx-coprime/) | L153-L153 | defined | — |
| `theorem` | [prime_coprime_of_not_dvd](/verify/taulib/docs/book-i-coordinates-primes/prime-coprime-of-not-dvd/) | L155-L161 | formalized | — |
| `theorem` | [coprime_dvd_of_dvd_mul](/verify/taulib/docs/book-i-coordinates-primes/coprime-dvd-of-dvd-mul/) | L164-L167 | formalized | — |
| `theorem` | [euclid_lemma](/verify/taulib/docs/book-i-coordinates-primes/euclid-lemma/) | L170-L174 | formalized | — |
| `def` | [idx_factorial](/verify/taulib/docs/book-i-coordinates-primes/idx-factorial/) | L180-L182 | defined | — |
| `theorem` | [idx_factorial_pos](/verify/taulib/docs/book-i-coordinates-primes/idx-factorial-pos/) | L184-L187 | formalized | — |
| `theorem` | [prime_dvd_factorial](/verify/taulib/docs/book-i-coordinates-primes/prime-dvd-factorial/) | L190-L204 | formalized | — |
| `theorem` | [not_dvd_succ_of_ge_two](/verify/taulib/docs/book-i-coordinates-primes/not-dvd-succ-of-ge-two/) | L207-L223 | formalized | — |
| `theorem` | [primes_infinite](/verify/taulib/docs/book-i-coordinates-primes/primes-infinite/) | L226-L232 | formalized | — |
| `def` | [list_prod](/verify/taulib/docs/book-i-coordinates-primes/list-prod/) | L238-L240 | defined | `I.T09` |
| `theorem` | [prime_product_exists](/verify/taulib/docs/book-i-coordinates-primes/prime-product-exists/) | L243-L273 | formalized | — |
| `theorem` | [list_prod_pos_of_primes](/verify/taulib/docs/book-i-coordinates-primes/list-prod-pos-of-primes/) | L280-L289 | formalized | — |
| `theorem` | [prod_one_implies_nil](/verify/taulib/docs/book-i-coordinates-primes/prod-one-implies-nil/) | L292-L302 | formalized | — |
| `theorem` | [prime_mem_of_dvd_prod](/verify/taulib/docs/book-i-coordinates-primes/prime-mem-of-dvd-prod/) | L305-L320 | formalized | — |
| `theorem` | [nat_mul_cancel_left](/verify/taulib/docs/book-i-coordinates-primes/nat-mul-cancel-left/) | L323-L334 | formalized | — |
| `def` | [all_ge](/verify/taulib/docs/book-i-coordinates-primes/all-ge/) | L339-L341 | defined | — |
| `theorem` | [mem_ge_of_all_ge](/verify/taulib/docs/book-i-coordinates-primes/mem-ge-of-all-ge/) | L343-L350 | formalized | — |
| `def` | [sorted_nd](/verify/taulib/docs/book-i-coordinates-primes/sorted-nd/) | L353-L355 | defined | — |
| `theorem` | [prime_product_unique](/verify/taulib/docs/book-i-coordinates-primes/prime-product-unique/) | L359-L407 | formalized | `I.T09` |
| `def` | [p_adic_val](/verify/taulib/docs/book-i-coordinates-primes/p-adic-val/) | L414-L424 | defined | — |
| `eval` | [#eval L430](/verify/taulib/docs/book-i-coordinates-primes/eval-l430/) | L430-L430 | computed | — |
| `eval` | [#eval L431](/verify/taulib/docs/book-i-coordinates-primes/eval-l431/) | L431-L431 | computed | — |
| `eval` | [#eval L432](/verify/taulib/docs/book-i-coordinates-primes/eval-l432/) | L432-L432 | computed | — |
| `eval` | [#eval L433](/verify/taulib/docs/book-i-coordinates-primes/eval-l433/) | L433-L433 | computed | — |
| `eval` | [#eval L434](/verify/taulib/docs/book-i-coordinates-primes/eval-l434/) | L434-L434 | computed | — |
| `eval` | [#eval L435](/verify/taulib/docs/book-i-coordinates-primes/eval-l435/) | L435-L437 | computed | — |

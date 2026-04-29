---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_slug": "book-iii-spectral-sieve-infrastructure",
  "book": "BookIII",
  "family": "Spectral",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Spectral/SieveInfrastructure.lean",
  "sha256": "e3314a48c9a4c2cadb5254c3eee22b13ee25a5ca1c27d2956d3e61cecee0adbb",
  "imports": [
    "TauLib.BookIII.Spectral.CRT"
  ],
  "imported_by": [
    "TauLib.BookIII",
    "TauLib.BookIII.Arithmetic.ABCDeep",
    "TauLib.BookIII.Spectral.GoldbachDeep",
    "TauLib.BookIII.Spectral.TwinPrimeDeep"
  ],
  "registry_ids": [
    "III.D100",
    "III.D101",
    "III.D99",
    "III.P42",
    "III.T66",
    "III.T67"
  ],
  "declaration_counts": {
    "def": 15,
    "theorem": 12,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "def",
      "name": "is_prime_sieve",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/is-prime-sieve/",
      "source_line_start": 58,
      "source_line_end": 67,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "eratosthenes_sieve",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eratosthenes-sieve/",
      "source_line_start": 74,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": [
        "III.D99"
      ]
    },
    {
      "kind": "def",
      "name": "sieve_primes",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-primes/",
      "source_line_start": 78,
      "source_line_end": 87,
      "formal_status": "defined",
      "registry_ids": [
        "III.D99"
      ]
    },
    {
      "kind": "def",
      "name": "sieve_prime_count",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-prime-count/",
      "source_line_start": 94,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": [
        "III.D100"
      ]
    },
    {
      "kind": "def",
      "name": "is_coprime_to_small_primes",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/is-coprime-to-small-primes/",
      "source_line_start": 110,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "divisible_by_small_prime",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/divisible-by-small-prime/",
      "source_line_start": 124,
      "source_line_end": 134,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "brun_sieve_count",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-sieve-count/",
      "source_line_start": 139,
      "source_line_end": 149,
      "formal_status": "defined",
      "registry_ids": [
        "III.D101"
      ]
    },
    {
      "kind": "def",
      "name": "brun_sieve_density",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-sieve-density/",
      "source_line_start": 153,
      "source_line_end": 154,
      "formal_status": "defined",
      "registry_ids": [
        "III.D101"
      ]
    },
    {
      "kind": "def",
      "name": "sieve_agrees_check",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-agrees-check/",
      "source_line_start": 162,
      "source_line_end": 170,
      "formal_status": "defined",
      "registry_ids": [
        "III.T66"
      ]
    },
    {
      "kind": "def",
      "name": "sieve_count_known_check",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-count-known-check/",
      "source_line_start": 173,
      "source_line_end": 178,
      "formal_status": "defined",
      "registry_ids": [
        "III.T66"
      ]
    },
    {
      "kind": "def",
      "name": "check_prime_factors_of_primorial",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/check-prime-factors-of-primorial/",
      "source_line_start": 185,
      "source_line_end": 195,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sieve_tower_compat_check",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-tower-compat-check/",
      "source_line_start": 201,
      "source_line_end": 213,
      "formal_status": "defined",
      "registry_ids": [
        "III.T67"
      ]
    },
    {
      "kind": "def",
      "name": "euler_phi_primorial",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/euler-phi-primorial/",
      "source_line_start": 216,
      "source_line_end": 225,
      "formal_status": "defined",
      "registry_ids": [
        "III.T67"
      ]
    },
    {
      "kind": "def",
      "name": "brun_euler_check",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-euler-check/",
      "source_line_start": 228,
      "source_line_end": 239,
      "formal_status": "defined",
      "registry_ids": [
        "III.T67"
      ]
    },
    {
      "kind": "def",
      "name": "sieve_crt_compat_check",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-crt-compat-check/",
      "source_line_start": 247,
      "source_line_end": 259,
      "formal_status": "defined",
      "registry_ids": [
        "III.P42"
      ]
    },
    {
      "kind": "theorem",
      "name": "sieve_correct_50",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-correct-50/",
      "source_line_start": 266,
      "source_line_end": 267,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T66"
      ]
    },
    {
      "kind": "theorem",
      "name": "sieve_correct_200",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-correct-200/",
      "source_line_start": 270,
      "source_line_end": 271,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T66"
      ]
    },
    {
      "kind": "theorem",
      "name": "sieve_count_known",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-count-known/",
      "source_line_start": 274,
      "source_line_end": 275,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T66"
      ]
    },
    {
      "kind": "theorem",
      "name": "sieve_tower_compat_3",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-tower-compat-3/",
      "source_line_start": 278,
      "source_line_end": 279,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T67"
      ]
    },
    {
      "kind": "theorem",
      "name": "brun_euler_4",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-euler-4/",
      "source_line_start": 282,
      "source_line_end": 283,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T67"
      ]
    },
    {
      "kind": "theorem",
      "name": "sieve_crt_compat_3",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-crt-compat-3/",
      "source_line_start": 286,
      "source_line_end": 287,
      "formal_status": "formalized",
      "registry_ids": [
        "III.P42"
      ]
    },
    {
      "kind": "theorem",
      "name": "pi_10",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/pi-10/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D100"
      ]
    },
    {
      "kind": "theorem",
      "name": "pi_30",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/pi-30/",
      "source_line_start": 297,
      "source_line_end": 297,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D100"
      ]
    },
    {
      "kind": "theorem",
      "name": "pi_100",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/pi-100/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D100"
      ]
    },
    {
      "kind": "theorem",
      "name": "brun_30_3",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-30-3/",
      "source_line_start": 304,
      "source_line_end": 304,
      "formal_status": "formalized",
      "registry_ids": [
        "III.D101"
      ]
    },
    {
      "kind": "theorem",
      "name": "euler_phi_primorial_3",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/euler-phi-primorial-3/",
      "source_line_start": 307,
      "source_line_end": 308,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T67"
      ]
    },
    {
      "kind": "theorem",
      "name": "euler_phi_primorial_4",
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/euler-phi-primorial-4/",
      "source_line_start": 311,
      "source_line_end": 312,
      "formal_status": "formalized",
      "registry_ids": [
        "III.T67"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 329,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Spectral/SieveInfrastructure.lean`
- SHA-256: `e3314a48c9a4c2cadb5254c3eee22b13ee25a5ca1c27d2956d3e61cecee0adbb`

## Registry Links

- `III.D100` — Sieve Prime Count
- `III.D101` — Brun Sieve Count
- `III.D99` — Eratosthenes Sieve
- `III.P42` — Sieve-CRT Compatibility
- `III.T66` — Sieve Correctness
- `III.T67` — Sieve-Tower Compatibility

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Spectral.CRT`

## Imported By

- `TauLib.BookIII`
- `TauLib.BookIII.Arithmetic.ABCDeep`
- `TauLib.BookIII.Spectral.GoldbachDeep`
- `TauLib.BookIII.Spectral.TwinPrimeDeep`

## Declaration Counts

- `def`: 15
- `eval`: 10
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [is_prime_sieve](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/is-prime-sieve/) | L58-L67 | defined | — |
| `def` | [eratosthenes_sieve](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eratosthenes-sieve/) | L74-L75 | defined | `III.D99` |
| `def` | [sieve_primes](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-primes/) | L78-L87 | defined | `III.D99` |
| `def` | [sieve_prime_count](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-prime-count/) | L94-L103 | defined | `III.D100` |
| `def` | [is_coprime_to_small_primes](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/is-coprime-to-small-primes/) | L110-L121 | defined | — |
| `def` | [divisible_by_small_prime](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/divisible-by-small-prime/) | L124-L134 | defined | — |
| `def` | [brun_sieve_count](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-sieve-count/) | L139-L149 | defined | `III.D101` |
| `def` | [brun_sieve_density](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-sieve-density/) | L153-L154 | defined | `III.D101` |
| `def` | [sieve_agrees_check](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-agrees-check/) | L162-L170 | defined | `III.T66` |
| `def` | [sieve_count_known_check](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-count-known-check/) | L173-L178 | defined | `III.T66` |
| `def` | [check_prime_factors_of_primorial](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/check-prime-factors-of-primorial/) | L185-L195 | defined | — |
| `def` | [sieve_tower_compat_check](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-tower-compat-check/) | L201-L213 | defined | `III.T67` |
| `def` | [euler_phi_primorial](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/euler-phi-primorial/) | L216-L225 | defined | `III.T67` |
| `def` | [brun_euler_check](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-euler-check/) | L228-L239 | defined | `III.T67` |
| `def` | [sieve_crt_compat_check](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-crt-compat-check/) | L247-L259 | defined | `III.P42` |
| `theorem` | [sieve_correct_50](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-correct-50/) | L266-L267 | formalized | `III.T66` |
| `theorem` | [sieve_correct_200](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-correct-200/) | L270-L271 | formalized | `III.T66` |
| `theorem` | [sieve_count_known](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-count-known/) | L274-L275 | formalized | `III.T66` |
| `theorem` | [sieve_tower_compat_3](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-tower-compat-3/) | L278-L279 | formalized | `III.T67` |
| `theorem` | [brun_euler_4](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-euler-4/) | L282-L283 | formalized | `III.T67` |
| `theorem` | [sieve_crt_compat_3](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-crt-compat-3/) | L286-L287 | formalized | `III.P42` |
| `theorem` | [pi_10](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/pi-10/) | L294-L294 | formalized | `III.D100` |
| `theorem` | [pi_30](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/pi-30/) | L297-L297 | formalized | `III.D100` |
| `theorem` | [pi_100](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/pi-100/) | L300-L300 | formalized | `III.D100` |
| `theorem` | [brun_30_3](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-30-3/) | L304-L304 | formalized | `III.D101` |
| `theorem` | [euler_phi_primorial_3](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/euler-phi-primorial-3/) | L307-L308 | formalized | `III.T67` |
| `theorem` | [euler_phi_primorial_4](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/euler-phi-primorial-4/) | L311-L312 | formalized | `III.T67` |
| `eval` | [#eval L318](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l318/) | L318-L318 | computed | — |
| `eval` | [#eval L319](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l319/) | L319-L319 | computed | — |
| `eval` | [#eval L320](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l320/) | L320-L320 | computed | — |
| `eval` | [#eval L321](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l321/) | L321-L321 | computed | — |
| `eval` | [#eval L322](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l322/) | L322-L322 | computed | — |
| `eval` | [#eval L323](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l323/) | L323-L323 | computed | — |
| `eval` | [#eval L324](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l324/) | L324-L324 | computed | — |
| `eval` | [#eval L325](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l325/) | L325-L325 | computed | — |
| `eval` | [#eval L326](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l326/) | L326-L326 | computed | — |
| `eval` | [#eval L327](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/eval-l327/) | L327-L329 | computed | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_slug": "book-iii-spectral-twin-prime-deep",
  "book": "BookIII",
  "family": "Spectral",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIII/Spectral/TwinPrimeDeep.lean",
  "sha256": "27e221c238ae5ac72301032e653f390511ddd6582f9a8eb0150b56675bd2334f",
  "imports": [
    "TauLib.BookIII.Spectral.SieveInfrastructure",
    "TauLib.BookIII.Spectral.AdditiveConjectures"
  ],
  "imported_by": [
    "TauLib.BookIII"
  ],
  "registry_ids": [
    "III.D105",
    "III.D106",
    "III.D107",
    "III.P45",
    "III.P46",
    "III.T72",
    "III.T73",
    "III.T74",
    "III.T75"
  ],
  "declaration_counts": {
    "def": 9,
    "theorem": 12,
    "eval": 14
  },
  "declarations": [
    {
      "kind": "def",
      "name": "twin_prime_sieve_count",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-prime-sieve-count/",
      "source_line_start": 50,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D105"
      ]
    },
    {
      "kind": "def",
      "name": "hl_twin_constant_approx",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-twin-constant-approx/",
      "source_line_start": 68,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D106"
      ]
    },
    {
      "kind": "def",
      "name": "hl_constant_decreasing_check",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-constant-decreasing-check/",
      "source_line_start": 84,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T74"
      ]
    },
    {
      "kind": "def",
      "name": "is_twin_admissible",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/is-twin-admissible/",
      "source_line_start": 103,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_twin_admissible",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/crt-twin-admissible/",
      "source_line_start": 120,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.D107"
      ]
    },
    {
      "kind": "def",
      "name": "crt_admissible_positive_check",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/crt-admissible-positive-check/",
      "source_line_start": 133,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T75"
      ]
    },
    {
      "kind": "def",
      "name": "twin_density_primorial_check",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-density-primorial-check/",
      "source_line_start": 150,
      "source_line_end": 161,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.T73"
      ]
    },
    {
      "kind": "def",
      "name": "count_admissible_at_prime",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/count-admissible-at-prime/",
      "source_line_start": 168,
      "source_line_end": 177,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "twin_admissibility_fraction_check",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissibility-fraction-check/",
      "source_line_start": 184,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "III.P45"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_primes_500",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-primes-500/",
      "source_line_start": 203,
      "source_line_end": 204,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T72"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_density_primorial_5",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-density-primorial-5/",
      "source_line_start": 207,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T73"
      ]
    },
    {
      "kind": "theorem",
      "name": "hl_constant_decreasing_5",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-constant-decreasing-5/",
      "source_line_start": 211,
      "source_line_end": 212,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T74"
      ]
    },
    {
      "kind": "theorem",
      "name": "crt_admissible_positive_4",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/crt-admissible-positive-4/",
      "source_line_start": 215,
      "source_line_end": 216,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.T75"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_admissibility_fraction_5",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissibility-fraction-5/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P45"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_count_100",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-count-100/",
      "source_line_start": 227,
      "source_line_end": 228,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D105"
      ]
    },
    {
      "kind": "theorem",
      "name": "hl_depth_2",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-depth-2/",
      "source_line_start": 231,
      "source_line_end": 232,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D106"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_admissible_1",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissible-1/",
      "source_line_start": 235,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D107"
      ]
    },
    {
      "kind": "theorem",
      "name": "twin_admissible_3_pos",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissible-3-pos/",
      "source_line_start": 239,
      "source_line_end": 240,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.D107"
      ]
    },
    {
      "kind": "theorem",
      "name": "admissible_at_3",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-3/",
      "source_line_start": 243,
      "source_line_end": 244,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P45"
      ]
    },
    {
      "kind": "theorem",
      "name": "admissible_at_5",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-5/",
      "source_line_start": 247,
      "source_line_end": 248,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P45"
      ]
    },
    {
      "kind": "theorem",
      "name": "admissible_at_7",
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-7/",
      "source_line_start": 251,
      "source_line_end": 252,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "III.P45"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l258/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l259/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l267/",
      "source_line_start": 267,
      "source_line_end": 267,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l268/",
      "source_line_start": 268,
      "source_line_end": 268,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l269/",
      "source_line_start": 269,
      "source_line_end": 269,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l270/",
      "source_line_start": 270,
      "source_line_end": 270,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l271/",
      "source_line_start": 271,
      "source_line_end": 273,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean",
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
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIII/Spectral/TwinPrimeDeep.lean`
- SHA-256: `27e221c238ae5ac72301032e653f390511ddd6582f9a8eb0150b56675bd2334f`

## Registry Links

- `III.D105` — Twin Prime Sieve Count
- `III.D106` — Hardy-Littlewood Constant
- `III.D107` — CRT Twin Admissibility
- `III.P45` — Twin Admissibility Fraction
- `III.P46` — Twin Gap Characterization
- `III.T72` — Twin Primes to 500
- `III.T73` — Twin Density Primorial
- `III.T74` — HL Constant Convergence
- `III.T75` — CRT Admissible Positive

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Spectral.SieveInfrastructure`
- `TauLib.BookIII.Spectral.AdditiveConjectures`

## Imported By

- `TauLib.BookIII`

## Declaration Counts

- `def`: 9
- `eval`: 14
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [twin_prime_sieve_count](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-prime-sieve-count/) | L50-L59 | data/computed value | data/computed value | `III.D105` |
| `def` | [hl_twin_constant_approx](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-twin-constant-approx/) | L68-L81 | data/computed value | data/computed value | `III.D106` |
| `def` | [hl_constant_decreasing_check](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-constant-decreasing-check/) | L84-L94 | data/computed value | data/computed value | `III.T74` |
| `def` | [is_twin_admissible](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/is-twin-admissible/) | L103-L117 | data/computed value | data/computed value | — |
| `def` | [crt_twin_admissible](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/crt-twin-admissible/) | L120-L130 | data/computed value | data/computed value | `III.D107` |
| `def` | [crt_admissible_positive_check](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/crt-admissible-positive-check/) | L133-L141 | data/computed value | data/computed value | `III.T75` |
| `def` | [twin_density_primorial_check](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-density-primorial-check/) | L150-L161 | data/computed value | data/computed value | `III.T73` |
| `def` | [count_admissible_at_prime](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/count-admissible-at-prime/) | L168-L177 | data/computed value | data/computed value | — |
| `def` | [twin_admissibility_fraction_check](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissibility-fraction-check/) | L184-L196 | data/computed value | data/computed value | `III.P45` |
| `theorem` | [twin_primes_500](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-primes-500/) | L203-L204 | proof obligation | formal proof obligation checked | `III.T72` |
| `theorem` | [twin_density_primorial_5](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-density-primorial-5/) | L207-L208 | proof obligation | formal proof obligation checked | `III.T73` |
| `theorem` | [hl_constant_decreasing_5](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-constant-decreasing-5/) | L211-L212 | proof obligation | formal proof obligation checked | `III.T74` |
| `theorem` | [crt_admissible_positive_4](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/crt-admissible-positive-4/) | L215-L216 | proof obligation | formal proof obligation checked | `III.T75` |
| `theorem` | [twin_admissibility_fraction_5](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissibility-fraction-5/) | L219-L220 | proof obligation | formal proof obligation checked | `III.P45` |
| `theorem` | [twin_count_100](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-count-100/) | L227-L228 | proof obligation | formal proof obligation checked | `III.D105` |
| `theorem` | [hl_depth_2](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-depth-2/) | L231-L232 | proof obligation | formal proof obligation checked | `III.D106` |
| `theorem` | [twin_admissible_1](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissible-1/) | L235-L236 | proof obligation | formal proof obligation checked | `III.D107` |
| `theorem` | [twin_admissible_3_pos](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissible-3-pos/) | L239-L240 | proof obligation | formal proof obligation checked | `III.D107` |
| `theorem` | [admissible_at_3](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-3/) | L243-L244 | proof obligation | formal proof obligation checked | `III.P45` |
| `theorem` | [admissible_at_5](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-5/) | L247-L248 | proof obligation | formal proof obligation checked | `III.P45` |
| `theorem` | [admissible_at_7](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-7/) | L251-L252 | proof obligation | formal proof obligation checked | `III.P45` |
| `eval` | [#eval L258](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l258/) | L258-L258 | computed check | computed check | — |
| `eval` | [#eval L259](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l259/) | L259-L259 | computed check | computed check | — |
| `eval` | [#eval L260](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l260/) | L260-L260 | computed check | computed check | — |
| `eval` | [#eval L261](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l261/) | L261-L261 | computed check | computed check | — |
| `eval` | [#eval L262](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l262/) | L262-L262 | computed check | computed check | — |
| `eval` | [#eval L263](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l263/) | L263-L263 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l264/) | L264-L264 | computed check | computed check | — |
| `eval` | [#eval L265](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l265/) | L265-L265 | computed check | computed check | — |
| `eval` | [#eval L266](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l266/) | L266-L266 | computed check | computed check | — |
| `eval` | [#eval L267](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l267/) | L267-L267 | computed check | computed check | — |
| `eval` | [#eval L268](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l268/) | L268-L268 | computed check | computed check | — |
| `eval` | [#eval L269](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l269/) | L269-L269 | computed check | computed check | — |
| `eval` | [#eval L270](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l270/) | L270-L270 | computed check | computed check | — |
| `eval` | [#eval L271](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/eval-l271/) | L271-L273 | computed check | computed check | — |

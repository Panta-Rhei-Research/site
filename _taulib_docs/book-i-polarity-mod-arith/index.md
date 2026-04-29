---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.ModArith",
  "permalink": "/verify/taulib/docs/book-i-polarity-mod-arith/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Polarity.ModArith`.",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_slug": "book-i-polarity-mod-arith",
  "book": "BookI",
  "family": "Polarity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Polarity/ModArith.lean",
  "sha256": "e5c59d4c4b718db4c6223ef42b8648b8abb2e476ae32eb183db5a6e59ad93965",
  "imports": [
    "TauLib.BookI.Coordinates.Primes"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Measure",
    "TauLib.BookI.Denotation.GrowthEscape",
    "TauLib.BookI.Holomorphy.IdentityTheorem",
    "TauLib.BookI.Holomorphy.TauHolomorphic",
    "TauLib.BookI.Polarity.ChineseRemainder",
    "TauLib.BookI.Polarity.ExtGCD",
    "TauLib.BookI.Polarity.NthPrime",
    "TauLib.BookI.Polarity.OmegaGerms",
    "TauLib.BookI.Topos.Functors",
    "TauLib.BookII.Domains.Cylinders"
  ],
  "registry_ids": [],
  "declaration_counts": {
    "def": 6,
    "theorem": 11,
    "eval": 17
  },
  "declarations": [
    {
      "kind": "def",
      "name": "nth_prime_go",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-go/",
      "source_line_start": 30,
      "source_line_end": 39,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nth_prime",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime/",
      "source_line_start": 42,
      "source_line_end": 44,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/primorial/",
      "source_line_start": 52,
      "source_line_end": 54,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "reduce",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/reduce/",
      "source_line_start": 62,
      "source_line_end": 62,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_dvd_check",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/primorial-dvd-check/",
      "source_line_start": 66,
      "source_line_end": 67,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "reduction_compat_check",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/reduction-compat-check/",
      "source_line_start": 70,
      "source_line_end": 72,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_add_eq",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/mod-add-eq/",
      "source_line_start": 79,
      "source_line_end": 80,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_mul_eq",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/mod-mul-eq/",
      "source_line_start": 83,
      "source_line_end": 84,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_lt_of_pos",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/mod-lt-of-pos/",
      "source_line_start": 87,
      "source_line_end": 88,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distinct_primes_coprime",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/distinct-primes-coprime/",
      "source_line_start": 95,
      "source_line_end": 107,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nth_prime_go_ge",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-go-ge/",
      "source_line_start": 114,
      "source_line_end": 131,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nth_prime_pos",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-pos/",
      "source_line_start": 134,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_pos",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/primorial-pos/",
      "source_line_start": 141,
      "source_line_end": 148,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_dvd",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/primorial-dvd/",
      "source_line_start": 156,
      "source_line_end": 169,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mul_add_mod",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/mul-add-mod/",
      "source_line_start": 176,
      "source_line_end": 182,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_mod_of_dvd",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/mod-mod-of-dvd/",
      "source_line_start": 186,
      "source_line_end": 197,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reduction_compat",
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/reduction-compat/",
      "source_line_start": 201,
      "source_line_end": 204,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l212/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l213/",
      "source_line_start": 213,
      "source_line_end": 213,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l214/",
      "source_line_start": 214,
      "source_line_end": 214,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l215/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l216/",
      "source_line_start": 216,
      "source_line_end": 216,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l219/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l221/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l223/",
      "source_line_start": 223,
      "source_line_end": 223,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l224/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l227/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l228/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l229/",
      "source_line_start": 229,
      "source_line_end": 229,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l232/",
      "source_line_start": 232,
      "source_line_end": 232,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-mod-arith/eval-l233/",
      "source_line_start": 233,
      "source_line_end": 235,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean",
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
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Polarity/ModArith.lean`
- SHA-256: `e5c59d4c4b718db4c6223ef42b8648b8abb2e476ae32eb183db5a6e59ad93965`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Coordinates.Primes`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Measure`
- `TauLib.BookI.Denotation.GrowthEscape`
- `TauLib.BookI.Holomorphy.IdentityTheorem`
- `TauLib.BookI.Holomorphy.TauHolomorphic`
- `TauLib.BookI.Polarity.ChineseRemainder`
- `TauLib.BookI.Polarity.ExtGCD`
- `TauLib.BookI.Polarity.NthPrime`
- `TauLib.BookI.Polarity.OmegaGerms`
- `TauLib.BookI.Topos.Functors`
- `TauLib.BookII.Domains.Cylinders`

## Declaration Counts

- `def`: 6
- `eval`: 17
- `theorem`: 11

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [nth_prime_go](/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-go/) | L30-L39 | defined | — |
| `def` | [nth_prime](/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime/) | L42-L44 | defined | — |
| `def` | [primorial](/verify/taulib/docs/book-i-polarity-mod-arith/primorial/) | L52-L54 | defined | — |
| `def` | [reduce](/verify/taulib/docs/book-i-polarity-mod-arith/reduce/) | L62-L62 | defined | — |
| `def` | [primorial_dvd_check](/verify/taulib/docs/book-i-polarity-mod-arith/primorial-dvd-check/) | L66-L67 | defined | — |
| `def` | [reduction_compat_check](/verify/taulib/docs/book-i-polarity-mod-arith/reduction-compat-check/) | L70-L72 | defined | — |
| `theorem` | [mod_add_eq](/verify/taulib/docs/book-i-polarity-mod-arith/mod-add-eq/) | L79-L80 | formalized | — |
| `theorem` | [mod_mul_eq](/verify/taulib/docs/book-i-polarity-mod-arith/mod-mul-eq/) | L83-L84 | formalized | — |
| `theorem` | [mod_lt_of_pos](/verify/taulib/docs/book-i-polarity-mod-arith/mod-lt-of-pos/) | L87-L88 | formalized | — |
| `theorem` | [distinct_primes_coprime](/verify/taulib/docs/book-i-polarity-mod-arith/distinct-primes-coprime/) | L95-L107 | formalized | — |
| `theorem` | [nth_prime_go_ge](/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-go-ge/) | L114-L131 | formalized | — |
| `theorem` | [nth_prime_pos](/verify/taulib/docs/book-i-polarity-mod-arith/nth-prime-pos/) | L134-L138 | formalized | — |
| `theorem` | [primorial_pos](/verify/taulib/docs/book-i-polarity-mod-arith/primorial-pos/) | L141-L148 | formalized | — |
| `theorem` | [primorial_dvd](/verify/taulib/docs/book-i-polarity-mod-arith/primorial-dvd/) | L156-L169 | formalized | — |
| `theorem` | [mul_add_mod](/verify/taulib/docs/book-i-polarity-mod-arith/mul-add-mod/) | L176-L182 | formalized | — |
| `theorem` | [mod_mod_of_dvd](/verify/taulib/docs/book-i-polarity-mod-arith/mod-mod-of-dvd/) | L186-L197 | formalized | — |
| `theorem` | [reduction_compat](/verify/taulib/docs/book-i-polarity-mod-arith/reduction-compat/) | L201-L204 | formalized | — |
| `eval` | [#eval L211](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l211/) | L211-L211 | computed | — |
| `eval` | [#eval L212](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l212/) | L212-L212 | computed | — |
| `eval` | [#eval L213](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l213/) | L213-L213 | computed | — |
| `eval` | [#eval L214](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l214/) | L214-L214 | computed | — |
| `eval` | [#eval L215](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l215/) | L215-L215 | computed | — |
| `eval` | [#eval L216](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l216/) | L216-L216 | computed | — |
| `eval` | [#eval L219](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l219/) | L219-L219 | computed | — |
| `eval` | [#eval L220](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l220/) | L220-L220 | computed | — |
| `eval` | [#eval L221](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l221/) | L221-L221 | computed | — |
| `eval` | [#eval L222](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l222/) | L222-L222 | computed | — |
| `eval` | [#eval L223](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l223/) | L223-L223 | computed | — |
| `eval` | [#eval L224](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l224/) | L224-L224 | computed | — |
| `eval` | [#eval L227](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l227/) | L227-L227 | computed | — |
| `eval` | [#eval L228](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l228/) | L228-L228 | computed | — |
| `eval` | [#eval L229](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l229/) | L229-L229 | computed | — |
| `eval` | [#eval L232](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l232/) | L232-L232 | computed | — |
| `eval` | [#eval L233](/verify/taulib/docs/book-i-polarity-mod-arith/eval-l233/) | L233-L235 | computed | — |

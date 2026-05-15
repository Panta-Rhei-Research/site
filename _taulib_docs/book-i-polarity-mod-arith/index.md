---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.ModArith",
  "permalink": "/corpus/taulib/docs/book-i-polarity-mod-arith/",
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
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime-go/",
      "source_line_start": 30,
      "source_line_end": 39,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nth_prime",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime/",
      "source_line_start": 42,
      "source_line_end": 44,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/primorial/",
      "source_line_start": 52,
      "source_line_end": 54,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "reduce",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/reduce/",
      "source_line_start": 62,
      "source_line_end": 62,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primorial_dvd_check",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/primorial-dvd-check/",
      "source_line_start": 66,
      "source_line_end": 67,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "reduction_compat_check",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/reduction-compat-check/",
      "source_line_start": 70,
      "source_line_end": 72,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_add_eq",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/mod-add-eq/",
      "source_line_start": 79,
      "source_line_end": 80,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_mul_eq",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/mod-mul-eq/",
      "source_line_start": 83,
      "source_line_end": 84,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_lt_of_pos",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/mod-lt-of-pos/",
      "source_line_start": 87,
      "source_line_end": 88,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distinct_primes_coprime",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/distinct-primes-coprime/",
      "source_line_start": 95,
      "source_line_end": 107,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nth_prime_go_ge",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime-go-ge/",
      "source_line_start": 114,
      "source_line_end": 131,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nth_prime_pos",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime-pos/",
      "source_line_start": 134,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_pos",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/primorial-pos/",
      "source_line_start": 141,
      "source_line_end": 148,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primorial_dvd",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/primorial-dvd/",
      "source_line_start": 156,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mul_add_mod",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/mul-add-mod/",
      "source_line_start": 176,
      "source_line_end": 182,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_mod_of_dvd",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/mod-mod-of-dvd/",
      "source_line_start": 186,
      "source_line_end": 197,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "reduction_compat",
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/reduction-compat/",
      "source_line_start": 201,
      "source_line_end": 204,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l212/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l213/",
      "source_line_start": 213,
      "source_line_end": 213,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l214/",
      "source_line_start": 214,
      "source_line_end": 214,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l215/",
      "source_line_start": 215,
      "source_line_end": 215,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l216/",
      "source_line_start": 216,
      "source_line_end": 216,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l219/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l221/",
      "source_line_start": 221,
      "source_line_end": 221,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l222/",
      "source_line_start": 222,
      "source_line_end": 222,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l223/",
      "source_line_start": 223,
      "source_line_end": 223,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l224/",
      "source_line_start": 224,
      "source_line_end": 224,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l227/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l228/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l229/",
      "source_line_start": 229,
      "source_line_end": 229,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l232/",
      "source_line_start": 232,
      "source_line_end": 232,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l233/",
      "source_line_start": 233,
      "source_line_end": 235,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [nth_prime_go](/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime-go/) | L30-L39 | data/computed value | data/computed value | — |
| `def` | [nth_prime](/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime/) | L42-L44 | definition | definition | — |
| `def` | [primorial](/corpus/taulib/docs/book-i-polarity-mod-arith/primorial/) | L52-L54 | definition | definition | — |
| `def` | [reduce](/corpus/taulib/docs/book-i-polarity-mod-arith/reduce/) | L62-L62 | definition | definition | — |
| `def` | [primorial_dvd_check](/corpus/taulib/docs/book-i-polarity-mod-arith/primorial-dvd-check/) | L66-L67 | data/computed value | data/computed value | — |
| `def` | [reduction_compat_check](/corpus/taulib/docs/book-i-polarity-mod-arith/reduction-compat-check/) | L70-L72 | data/computed value | data/computed value | — |
| `theorem` | [mod_add_eq](/corpus/taulib/docs/book-i-polarity-mod-arith/mod-add-eq/) | L79-L80 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mod_mul_eq](/corpus/taulib/docs/book-i-polarity-mod-arith/mod-mul-eq/) | L83-L84 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mod_lt_of_pos](/corpus/taulib/docs/book-i-polarity-mod-arith/mod-lt-of-pos/) | L87-L88 | proof obligation | formal proof obligation checked | — |
| `theorem` | [distinct_primes_coprime](/corpus/taulib/docs/book-i-polarity-mod-arith/distinct-primes-coprime/) | L95-L107 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nth_prime_go_ge](/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime-go-ge/) | L114-L131 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nth_prime_pos](/corpus/taulib/docs/book-i-polarity-mod-arith/nth-prime-pos/) | L134-L138 | proof obligation | formal proof obligation checked | — |
| `theorem` | [primorial_pos](/corpus/taulib/docs/book-i-polarity-mod-arith/primorial-pos/) | L141-L148 | proof obligation | formal proof obligation checked | — |
| `theorem` | [primorial_dvd](/corpus/taulib/docs/book-i-polarity-mod-arith/primorial-dvd/) | L156-L169 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mul_add_mod](/corpus/taulib/docs/book-i-polarity-mod-arith/mul-add-mod/) | L176-L182 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mod_mod_of_dvd](/corpus/taulib/docs/book-i-polarity-mod-arith/mod-mod-of-dvd/) | L186-L197 | proof obligation | formal proof obligation checked | — |
| `theorem` | [reduction_compat](/corpus/taulib/docs/book-i-polarity-mod-arith/reduction-compat/) | L201-L204 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L211](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l211/) | L211-L211 | computed check | computed check | — |
| `eval` | [#eval L212](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l212/) | L212-L212 | computed check | computed check | — |
| `eval` | [#eval L213](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l213/) | L213-L213 | computed check | computed check | — |
| `eval` | [#eval L214](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l214/) | L214-L214 | computed check | computed check | — |
| `eval` | [#eval L215](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l215/) | L215-L215 | computed check | computed check | — |
| `eval` | [#eval L216](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l216/) | L216-L216 | computed check | computed check | — |
| `eval` | [#eval L219](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l219/) | L219-L219 | computed check | computed check | — |
| `eval` | [#eval L220](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l220/) | L220-L220 | computed check | computed check | — |
| `eval` | [#eval L221](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l221/) | L221-L221 | computed check | computed check | — |
| `eval` | [#eval L222](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l222/) | L222-L222 | computed check | computed check | — |
| `eval` | [#eval L223](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l223/) | L223-L223 | computed check | computed check | — |
| `eval` | [#eval L224](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l224/) | L224-L224 | computed check | computed check | — |
| `eval` | [#eval L227](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l227/) | L227-L227 | computed check | computed check | — |
| `eval` | [#eval L228](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l228/) | L228-L228 | computed check | computed check | — |
| `eval` | [#eval L229](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l229/) | L229-L229 | computed check | computed check | — |
| `eval` | [#eval L232](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l232/) | L232-L232 | computed check | computed check | — |
| `eval` | [#eval L233](/corpus/taulib/docs/book-i-polarity-mod-arith/eval-l233/) | L233-L235 | computed check | computed check | — |

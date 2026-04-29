---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Sets.Operations",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Sets.Operations`.",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_slug": "book-i-sets-operations",
  "book": "BookI",
  "family": "Sets",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Sets/Operations.lean",
  "sha256": "fde934bbd166e76042a2ace1386f4880207793312863baf1b185182bc9195977",
  "imports": [
    "TauLib.BookI.Sets.Membership",
    "Mathlib.Tactic.Set",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Sets.Powerset"
  ],
  "registry_ids": [
    "I.D32",
    "I.P11"
  ],
  "declaration_counts": {
    "def": 2,
    "theorem": 25,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "def",
      "name": "tau_union",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union/",
      "source_line_start": 39,
      "source_line_end": 39,
      "formal_status": "defined",
      "registry_ids": [
        "I.D32"
      ]
    },
    {
      "kind": "def",
      "name": "tau_inter",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter/",
      "source_line_start": 42,
      "source_line_end": 42,
      "formal_status": "defined",
      "registry_ids": [
        "I.D32"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_union_comm",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-comm/",
      "source_line_start": 48,
      "source_line_end": 49,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_comm",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-comm/",
      "source_line_start": 51,
      "source_line_end": 52,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_assoc",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-assoc/",
      "source_line_start": 58,
      "source_line_end": 60,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_assoc",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-assoc/",
      "source_line_start": 62,
      "source_line_end": 64,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_self",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-self/",
      "source_line_start": 70,
      "source_line_end": 75,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_self",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-self/",
      "source_line_start": 77,
      "source_line_end": 78,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_one",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-one/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_zero",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-zero/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_zero",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-zero/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_one",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-one/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_union_left",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-mem-union-left/",
      "source_line_start": 105,
      "source_line_end": 106,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_union_right",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-mem-union-right/",
      "source_line_start": 108,
      "source_line_end": 109,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_inter_left",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-mem-inter-left/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_inter_right",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-mem-inter-right/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_dvd",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-dvd/",
      "source_line_start": 117,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_dvd",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-dvd/",
      "source_line_start": 122,
      "source_line_end": 125,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_inter_absorb",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-inter-absorb/",
      "source_line_start": 131,
      "source_line_end": 134,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_union_absorb",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-union-absorb/",
      "source_line_start": 136,
      "source_line_end": 139,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_mul_cancel",
      "url": "/verify/taulib/docs/book-i-sets-operations/nat-mul-cancel/",
      "source_line_start": 146,
      "source_line_end": 155,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_mul_dvd_cancel",
      "url": "/verify/taulib/docs/book-i-sets-operations/nat-mul-dvd-cancel/",
      "source_line_start": 158,
      "source_line_end": 160,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gcd_gcd_eq",
      "url": "/verify/taulib/docs/book-i-sets-operations/gcd-gcd-eq/",
      "source_line_start": 163,
      "source_line_end": 175,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distrib_coprime",
      "url": "/verify/taulib/docs/book-i-sets-operations/distrib-coprime/",
      "source_line_start": 182,
      "source_line_end": 241,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_gcd_distrib_lcm",
      "url": "/verify/taulib/docs/book-i-sets-operations/nat-gcd-distrib-lcm/",
      "source_line_start": 245,
      "source_line_end": 281,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_distrib_union",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-inter-distrib-union/",
      "source_line_start": 289,
      "source_line_end": 292,
      "formal_status": "formalized",
      "registry_ids": [
        "I.P11"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_union_distrib_inter",
      "url": "/verify/taulib/docs/book-i-sets-operations/tau-union-distrib-inter/",
      "source_line_start": 300,
      "source_line_end": 325,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-sets-operations/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-sets-operations/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-sets-operations/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-sets-operations/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 336,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean",
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
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Sets/Operations.lean`
- SHA-256: `fde934bbd166e76042a2ace1386f4880207793312863baf1b185182bc9195977`

## Registry Links

- `I.D32` — Set-Theoretic Operations
- `I.P11` — Distributive Lattice

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Sets.Membership`
- `Mathlib.Tactic.Set`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Sets.Powerset`

## Declaration Counts

- `def`: 2
- `eval`: 4
- `theorem`: 25

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [tau_union](/verify/taulib/docs/book-i-sets-operations/tau-union/) | L39-L39 | defined | `I.D32` |
| `def` | [tau_inter](/verify/taulib/docs/book-i-sets-operations/tau-inter/) | L42-L42 | defined | `I.D32` |
| `theorem` | [tau_union_comm](/verify/taulib/docs/book-i-sets-operations/tau-union-comm/) | L48-L49 | formalized | — |
| `theorem` | [tau_inter_comm](/verify/taulib/docs/book-i-sets-operations/tau-inter-comm/) | L51-L52 | formalized | — |
| `theorem` | [tau_union_assoc](/verify/taulib/docs/book-i-sets-operations/tau-union-assoc/) | L58-L60 | formalized | — |
| `theorem` | [tau_inter_assoc](/verify/taulib/docs/book-i-sets-operations/tau-inter-assoc/) | L62-L64 | formalized | — |
| `theorem` | [tau_union_self](/verify/taulib/docs/book-i-sets-operations/tau-union-self/) | L70-L75 | formalized | — |
| `theorem` | [tau_inter_self](/verify/taulib/docs/book-i-sets-operations/tau-inter-self/) | L77-L78 | formalized | — |
| `theorem` | [tau_union_one](/verify/taulib/docs/book-i-sets-operations/tau-union-one/) | L84-L85 | formalized | — |
| `theorem` | [tau_inter_zero](/verify/taulib/docs/book-i-sets-operations/tau-inter-zero/) | L92-L93 | formalized | — |
| `theorem` | [tau_union_zero](/verify/taulib/docs/book-i-sets-operations/tau-union-zero/) | L95-L96 | formalized | — |
| `theorem` | [tau_inter_one](/verify/taulib/docs/book-i-sets-operations/tau-inter-one/) | L98-L99 | formalized | — |
| `theorem` | [tau_mem_union_left](/verify/taulib/docs/book-i-sets-operations/tau-mem-union-left/) | L105-L106 | formalized | — |
| `theorem` | [tau_mem_union_right](/verify/taulib/docs/book-i-sets-operations/tau-mem-union-right/) | L108-L109 | formalized | — |
| `theorem` | [tau_mem_inter_left](/verify/taulib/docs/book-i-sets-operations/tau-mem-inter-left/) | L111-L112 | formalized | — |
| `theorem` | [tau_mem_inter_right](/verify/taulib/docs/book-i-sets-operations/tau-mem-inter-right/) | L114-L115 | formalized | — |
| `theorem` | [tau_union_dvd](/verify/taulib/docs/book-i-sets-operations/tau-union-dvd/) | L117-L120 | formalized | — |
| `theorem` | [tau_inter_dvd](/verify/taulib/docs/book-i-sets-operations/tau-inter-dvd/) | L122-L125 | formalized | — |
| `theorem` | [tau_union_inter_absorb](/verify/taulib/docs/book-i-sets-operations/tau-union-inter-absorb/) | L131-L134 | formalized | — |
| `theorem` | [tau_inter_union_absorb](/verify/taulib/docs/book-i-sets-operations/tau-inter-union-absorb/) | L136-L139 | formalized | — |
| `theorem` | [nat_mul_cancel](/verify/taulib/docs/book-i-sets-operations/nat-mul-cancel/) | L146-L155 | formalized | — |
| `theorem` | [nat_mul_dvd_cancel](/verify/taulib/docs/book-i-sets-operations/nat-mul-dvd-cancel/) | L158-L160 | formalized | — |
| `theorem` | [gcd_gcd_eq](/verify/taulib/docs/book-i-sets-operations/gcd-gcd-eq/) | L163-L175 | formalized | — |
| `theorem` | [distrib_coprime](/verify/taulib/docs/book-i-sets-operations/distrib-coprime/) | L182-L241 | formalized | — |
| `theorem` | [nat_gcd_distrib_lcm](/verify/taulib/docs/book-i-sets-operations/nat-gcd-distrib-lcm/) | L245-L281 | formalized | — |
| `theorem` | [tau_inter_distrib_union](/verify/taulib/docs/book-i-sets-operations/tau-inter-distrib-union/) | L289-L292 | formalized | `I.P11` |
| `theorem` | [tau_union_distrib_inter](/verify/taulib/docs/book-i-sets-operations/tau-union-distrib-inter/) | L300-L325 | formalized | — |
| `eval` | [#eval L331](/verify/taulib/docs/book-i-sets-operations/eval-l331/) | L331-L331 | computed | — |
| `eval` | [#eval L332](/verify/taulib/docs/book-i-sets-operations/eval-l332/) | L332-L332 | computed | — |
| `eval` | [#eval L333](/verify/taulib/docs/book-i-sets-operations/eval-l333/) | L333-L333 | computed | — |
| `eval` | [#eval L334](/verify/taulib/docs/book-i-sets-operations/eval-l334/) | L334-L336 | computed | — |

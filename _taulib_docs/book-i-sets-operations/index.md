---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Sets.Operations",
  "permalink": "/corpus/taulib/docs/book-i-sets-operations/",
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
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union/",
      "source_line_start": 39,
      "source_line_end": 39,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D32"
      ]
    },
    {
      "kind": "def",
      "name": "tau_inter",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter/",
      "source_line_start": 42,
      "source_line_end": 42,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D32"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_union_comm",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-comm/",
      "source_line_start": 48,
      "source_line_end": 49,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_comm",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-comm/",
      "source_line_start": 51,
      "source_line_end": 52,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_assoc",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-assoc/",
      "source_line_start": 58,
      "source_line_end": 60,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_assoc",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-assoc/",
      "source_line_start": 62,
      "source_line_end": 64,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_self",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-self/",
      "source_line_start": 70,
      "source_line_end": 75,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_self",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-self/",
      "source_line_start": 77,
      "source_line_end": 78,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_one",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-one/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_zero",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-zero/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_zero",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-zero/",
      "source_line_start": 95,
      "source_line_end": 96,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_one",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-one/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_union_left",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-mem-union-left/",
      "source_line_start": 105,
      "source_line_end": 106,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_union_right",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-mem-union-right/",
      "source_line_start": 108,
      "source_line_end": 109,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_inter_left",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-mem-inter-left/",
      "source_line_start": 111,
      "source_line_end": 112,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_mem_inter_right",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-mem-inter-right/",
      "source_line_start": 114,
      "source_line_end": 115,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_dvd",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-dvd/",
      "source_line_start": 117,
      "source_line_end": 120,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_dvd",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-dvd/",
      "source_line_start": 122,
      "source_line_end": 125,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_union_inter_absorb",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-inter-absorb/",
      "source_line_start": 131,
      "source_line_end": 134,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_union_absorb",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-union-absorb/",
      "source_line_start": 136,
      "source_line_end": 139,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_mul_cancel",
      "url": "/corpus/taulib/docs/book-i-sets-operations/nat-mul-cancel/",
      "source_line_start": 146,
      "source_line_end": 155,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_mul_dvd_cancel",
      "url": "/corpus/taulib/docs/book-i-sets-operations/nat-mul-dvd-cancel/",
      "source_line_start": 158,
      "source_line_end": 160,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gcd_gcd_eq",
      "url": "/corpus/taulib/docs/book-i-sets-operations/gcd-gcd-eq/",
      "source_line_start": 163,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "distrib_coprime",
      "url": "/corpus/taulib/docs/book-i-sets-operations/distrib-coprime/",
      "source_line_start": 182,
      "source_line_end": 241,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_gcd_distrib_lcm",
      "url": "/corpus/taulib/docs/book-i-sets-operations/nat-gcd-distrib-lcm/",
      "source_line_start": 245,
      "source_line_end": 281,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_inter_distrib_union",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-inter-distrib-union/",
      "source_line_start": 289,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.P11"
      ]
    },
    {
      "kind": "theorem",
      "name": "tau_union_distrib_inter",
      "url": "/corpus/taulib/docs/book-i-sets-operations/tau-union-distrib-inter/",
      "source_line_start": 300,
      "source_line_end": 325,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-sets-operations/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-sets-operations/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-sets-operations/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-sets-operations/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 336,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [tau_union](/corpus/taulib/docs/book-i-sets-operations/tau-union/) | L39-L39 | definition | definition | `I.D32` |
| `def` | [tau_inter](/corpus/taulib/docs/book-i-sets-operations/tau-inter/) | L42-L42 | definition | definition | `I.D32` |
| `theorem` | [tau_union_comm](/corpus/taulib/docs/book-i-sets-operations/tau-union-comm/) | L48-L49 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_comm](/corpus/taulib/docs/book-i-sets-operations/tau-inter-comm/) | L51-L52 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_union_assoc](/corpus/taulib/docs/book-i-sets-operations/tau-union-assoc/) | L58-L60 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_assoc](/corpus/taulib/docs/book-i-sets-operations/tau-inter-assoc/) | L62-L64 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_union_self](/corpus/taulib/docs/book-i-sets-operations/tau-union-self/) | L70-L75 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_self](/corpus/taulib/docs/book-i-sets-operations/tau-inter-self/) | L77-L78 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_union_one](/corpus/taulib/docs/book-i-sets-operations/tau-union-one/) | L84-L85 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_zero](/corpus/taulib/docs/book-i-sets-operations/tau-inter-zero/) | L92-L93 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_union_zero](/corpus/taulib/docs/book-i-sets-operations/tau-union-zero/) | L95-L96 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_one](/corpus/taulib/docs/book-i-sets-operations/tau-inter-one/) | L98-L99 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_mem_union_left](/corpus/taulib/docs/book-i-sets-operations/tau-mem-union-left/) | L105-L106 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_mem_union_right](/corpus/taulib/docs/book-i-sets-operations/tau-mem-union-right/) | L108-L109 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_mem_inter_left](/corpus/taulib/docs/book-i-sets-operations/tau-mem-inter-left/) | L111-L112 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_mem_inter_right](/corpus/taulib/docs/book-i-sets-operations/tau-mem-inter-right/) | L114-L115 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_union_dvd](/corpus/taulib/docs/book-i-sets-operations/tau-union-dvd/) | L117-L120 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_dvd](/corpus/taulib/docs/book-i-sets-operations/tau-inter-dvd/) | L122-L125 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_union_inter_absorb](/corpus/taulib/docs/book-i-sets-operations/tau-union-inter-absorb/) | L131-L134 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_union_absorb](/corpus/taulib/docs/book-i-sets-operations/tau-inter-union-absorb/) | L136-L139 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nat_mul_cancel](/corpus/taulib/docs/book-i-sets-operations/nat-mul-cancel/) | L146-L155 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nat_mul_dvd_cancel](/corpus/taulib/docs/book-i-sets-operations/nat-mul-dvd-cancel/) | L158-L160 | proof obligation | formal proof obligation checked | — |
| `theorem` | [gcd_gcd_eq](/corpus/taulib/docs/book-i-sets-operations/gcd-gcd-eq/) | L163-L175 | proof obligation | formal proof obligation checked | — |
| `theorem` | [distrib_coprime](/corpus/taulib/docs/book-i-sets-operations/distrib-coprime/) | L182-L241 | proof obligation | formal proof obligation checked | — |
| `theorem` | [nat_gcd_distrib_lcm](/corpus/taulib/docs/book-i-sets-operations/nat-gcd-distrib-lcm/) | L245-L281 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_inter_distrib_union](/corpus/taulib/docs/book-i-sets-operations/tau-inter-distrib-union/) | L289-L292 | proof obligation | formal proof obligation checked | `I.P11` |
| `theorem` | [tau_union_distrib_inter](/corpus/taulib/docs/book-i-sets-operations/tau-union-distrib-inter/) | L300-L325 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L331](/corpus/taulib/docs/book-i-sets-operations/eval-l331/) | L331-L331 | computed check | computed check | — |
| `eval` | [#eval L332](/corpus/taulib/docs/book-i-sets-operations/eval-l332/) | L332-L332 | computed check | computed check | — |
| `eval` | [#eval L333](/corpus/taulib/docs/book-i-sets-operations/eval-l333/) | L333-L333 | computed check | computed check | — |
| `eval` | [#eval L334](/corpus/taulib/docs/book-i-sets-operations/eval-l334/) | L334-L336 | computed check | computed check | — |

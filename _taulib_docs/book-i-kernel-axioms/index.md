---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Kernel.Axioms",
  "permalink": "/corpus/taulib/docs/book-i-kernel-axioms/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Kernel.Axioms`.",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_slug": "book-i-kernel-axioms",
  "book": "BookI",
  "family": "Kernel",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Kernel/Axioms.lean",
  "sha256": "f009556a4bfeafec4db79adc6c317e42a2ebb808e9dc7673257f6baa54eae61b",
  "imports": [
    "TauLib.BookI.Kernel.Signature"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Kernel.ActionQuantum",
    "TauLib.BookI.Kernel.Diagonal",
    "TauLib.BookI.Orbit.Generation",
    "TauLib.Tour.Foundations",
    "TauLib.Tour.GuidedTour.BookI"
  ],
  "registry_ids": [
    "I.D02",
    "I.K1",
    "I.K2",
    "I.K3",
    "I.K4",
    "I.K5",
    "I.K6",
    "I.P01",
    "I.P02"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 3,
    "theorem": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauObj",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/tau-obj/",
      "source_line_start": 49,
      "source_line_end": 54,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauObj.ofGen",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/of-gen/",
      "source_line_start": 57,
      "source_line_end": 57,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "rho",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/rho/",
      "source_line_start": 61,
      "source_line_end": 64,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.D02"
      ]
    },
    {
      "kind": "theorem",
      "name": "K1_strict_order",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/k1-strict-order/",
      "source_line_start": 75,
      "source_line_end": 80,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.K1"
      ]
    },
    {
      "kind": "theorem",
      "name": "K2_omega_fixed",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/k2-omega-fixed/",
      "source_line_start": 85,
      "source_line_end": 87,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.K2"
      ]
    },
    {
      "kind": "def",
      "name": "inOrbitRay",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/in-orbit-ray/",
      "source_line_start": 93,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "I.K3"
      ]
    },
    {
      "kind": "theorem",
      "name": "K3_orbit_seeded",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/k3-orbit-seeded/",
      "source_line_start": 97,
      "source_line_end": 99,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.K3"
      ]
    },
    {
      "kind": "theorem",
      "name": "K4_no_jump",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/k4-no-jump/",
      "source_line_start": 103,
      "source_line_end": 105,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.K4"
      ]
    },
    {
      "kind": "theorem",
      "name": "K5_beacon_non_succ",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/k5-beacon-non-succ/",
      "source_line_start": 109,
      "source_line_end": 111,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.K5"
      ]
    },
    {
      "kind": "theorem",
      "name": "K5_omega_unreachable",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/k5-omega-unreachable/",
      "source_line_start": 115,
      "source_line_end": 121,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "K6_object_closure",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/k6-object-closure/",
      "source_line_start": 128,
      "source_line_end": 135,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.K6"
      ]
    },
    {
      "kind": "theorem",
      "name": "gen_distinct",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/gen-distinct/",
      "source_line_start": 142,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.P01"
      ]
    },
    {
      "kind": "theorem",
      "name": "rho_injective",
      "url": "/corpus/taulib/docs/book-i-kernel-axioms/rho-injective/",
      "source_line_start": 149,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "I.P02"
      ]
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean",
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
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Kernel/Axioms.lean`
- SHA-256: `f009556a4bfeafec4db79adc6c317e42a2ebb808e9dc7673257f6baa54eae61b`

## Registry Links

- `I.D02` — Progression Operator rho
- `I.K1` — Strict Order (K1)
- `I.K2` — Omega Fixed Point (K2)
- `I.K3` — Orbit-Seeded Generation (K3)
- `I.K4` — No-Jump / Cover (K4)
- `I.K5` — Beacon Non-Successor (K5)
- `I.K6` — Object Closure (K6)
- `I.P01` — Generator Distinctness
- `I.P02` — rho Injectivity Per Orbit

## Construction Spine Links

- [Build the τ-Kernel](/corpus/construction-spine/build-the-kernel/)

## Imports

- `TauLib.BookI.Kernel.Signature`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Kernel.ActionQuantum`
- `TauLib.BookI.Kernel.Diagonal`
- `TauLib.BookI.Orbit.Generation`
- `TauLib.Tour.Foundations`
- `TauLib.Tour.GuidedTour.BookI`

## Declaration Counts

- `def`: 3
- `structure`: 1
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauObj](/corpus/taulib/docs/book-i-kernel-axioms/tau-obj/) | L49-L54 | type/data schema | type/data schema | — |
| `def` | [TauObj.ofGen](/corpus/taulib/docs/book-i-kernel-axioms/of-gen/) | L57-L57 | definition | definition | — |
| `def` | [rho](/corpus/taulib/docs/book-i-kernel-axioms/rho/) | L61-L64 | definition | definition | `I.D02` |
| `theorem` | [K1_strict_order](/corpus/taulib/docs/book-i-kernel-axioms/k1-strict-order/) | L75-L80 | proof obligation | formal proof obligation checked | `I.K1` |
| `theorem` | [K2_omega_fixed](/corpus/taulib/docs/book-i-kernel-axioms/k2-omega-fixed/) | L85-L87 | proof obligation | formal proof obligation checked | `I.K2` |
| `def` | [inOrbitRay](/corpus/taulib/docs/book-i-kernel-axioms/in-orbit-ray/) | L93-L94 | definition | definition | `I.K3` |
| `theorem` | [K3_orbit_seeded](/corpus/taulib/docs/book-i-kernel-axioms/k3-orbit-seeded/) | L97-L99 | proof obligation | formal proof obligation checked | `I.K3` |
| `theorem` | [K4_no_jump](/corpus/taulib/docs/book-i-kernel-axioms/k4-no-jump/) | L103-L105 | proof obligation | formal proof obligation checked | `I.K4` |
| `theorem` | [K5_beacon_non_succ](/corpus/taulib/docs/book-i-kernel-axioms/k5-beacon-non-succ/) | L109-L111 | proof obligation | formal proof obligation checked | `I.K5` |
| `theorem` | [K5_omega_unreachable](/corpus/taulib/docs/book-i-kernel-axioms/k5-omega-unreachable/) | L115-L121 | proof obligation | formal proof obligation checked | — |
| `theorem` | [K6_object_closure](/corpus/taulib/docs/book-i-kernel-axioms/k6-object-closure/) | L128-L135 | proof obligation | formal proof obligation checked | `I.K6` |
| `theorem` | [gen_distinct](/corpus/taulib/docs/book-i-kernel-axioms/gen-distinct/) | L142-L146 | proof obligation | formal proof obligation checked | `I.P01` |
| `theorem` | [rho_injective](/corpus/taulib/docs/book-i-kernel-axioms/rho-injective/) | L149-L158 | proof obligation | formal proof obligation checked | `I.P02` |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "permalink": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_slug": "book-i-boundary-bridge-tau-int-quotient",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean",
  "sha256": "0a3a239307fb52cf692c555cf87874b556f8c5b80a7383811673ec3a7cf235f0",
  "imports": [
    "TauLib.BookI.Boundary.NumberTower",
    "Mathlib.Algebra.Group.Defs",
    "Mathlib.Algebra.Ring.Defs",
    "Mathlib.Algebra.Ring.Equiv",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.Bridge.TauRatQuotient"
  ],
  "registry_ids": [
    "I.D14"
  ],
  "declaration_counts": {
    "def": 10,
    "theorem": 10
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauInt.setoid",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/setoid/",
      "source_line_start": 69,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauInt.toQ",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-q/",
      "source_line_start": 80,
      "source_line_end": 84,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.toInt",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int/",
      "source_line_start": 92,
      "source_line_end": 96,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauInt.add_respects_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/add-respects-equiv/",
      "source_line_start": 103,
      "source_line_end": 107,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauInt.mul_respects_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/mul-respects-equiv/",
      "source_line_start": 110,
      "source_line_end": 114,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauInt.negate_respects_equiv",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/negate-respects-equiv/",
      "source_line_start": 117,
      "source_line_end": 120,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.add",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/add/",
      "source_line_start": 123,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.mul",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/mul/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.neg",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/neg/",
      "source_line_start": 133,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.zero",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/zero/",
      "source_line_start": 138,
      "source_line_end": 138,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.one",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/one/",
      "source_line_start": 141,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauIntQ.toInt_add",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int-add/",
      "source_line_start": 156,
      "source_line_end": 159,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauIntQ.toInt_mul",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int-mul/",
      "source_line_start": 161,
      "source_line_end": 174,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauIntQ.eq_iff_toInt_eq",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/eq-iff-to-int-eq/",
      "source_line_start": 177,
      "source_line_end": 181,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauIntQ.lift_via_toInt",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/lift-via-to-int/",
      "source_line_start": 189,
      "source_line_end": 273,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.ofInt",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/of-int/",
      "source_line_start": 280,
      "source_line_end": 282,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauIntQ.ofInt_toInt",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/of-int-to-int/",
      "source_line_start": 284,
      "source_line_end": 295,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauIntQ.toInt_ofInt",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int-of-int/",
      "source_line_start": 297,
      "source_line_end": 298,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauIntQ.ringEquivInt",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/ring-equiv-int/",
      "source_line_start": 305,
      "source_line_end": 315,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h8_tauint_mathlib_bridge_synthesis",
      "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/h8-tauint-mathlib-bridge-synthesis/",
      "source_line_start": 335,
      "source_line_end": 352,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`
- SHA-256: `0a3a239307fb52cf692c555cf87874b556f8c5b80a7383811673ec3a7cf235f0`

## Registry Links

- `I.D14` — Program Monoid

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.NumberTower`
- `Mathlib.Algebra.Group.Defs`
- `Mathlib.Algebra.Ring.Defs`
- `Mathlib.Algebra.Ring.Equiv`
- `Mathlib.Tactic.Ring`

## Imported By

- `TauLib.BookI.Boundary.Bridge.TauRatQuotient`

## Declaration Counts

- `def`: 10
- `theorem`: 10

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `def` | [TauInt.setoid](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/setoid/) | L69-L77 | definition | definition | — |
| `def` | [TauInt.toQ](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-q/) | L80-L84 | definition | definition | — |
| `def` | [TauIntQ.toInt](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int/) | L92-L96 | definition | definition | — |
| `theorem` | [TauInt.add_respects_equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/add-respects-equiv/) | L103-L107 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauInt.mul_respects_equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/mul-respects-equiv/) | L110-L114 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauInt.negate_respects_equiv](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/negate-respects-equiv/) | L117-L120 | proof obligation | formal proof obligation checked | — |
| `def` | [TauIntQ.add](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/add/) | L123-L125 | definition | definition | — |
| `def` | [TauIntQ.mul](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/mul/) | L128-L130 | definition | definition | — |
| `def` | [TauIntQ.neg](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/neg/) | L133-L135 | definition | definition | — |
| `def` | [TauIntQ.zero](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/zero/) | L138-L138 | definition | definition | — |
| `def` | [TauIntQ.one](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/one/) | L141-L150 | definition | definition | — |
| `theorem` | [TauIntQ.toInt_add](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int-add/) | L156-L159 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauIntQ.toInt_mul](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int-mul/) | L161-L174 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauIntQ.eq_iff_toInt_eq](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/eq-iff-to-int-eq/) | L177-L181 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauIntQ.lift_via_toInt](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/lift-via-to-int/) | L189-L273 | proof obligation | formal proof obligation checked | — |
| `def` | [TauIntQ.ofInt](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/of-int/) | L280-L282 | data/computed value | data/computed value | — |
| `theorem` | [TauIntQ.ofInt_toInt](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/of-int-to-int/) | L284-L295 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TauIntQ.toInt_ofInt](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/to-int-of-int/) | L297-L298 | proof obligation | formal proof obligation checked | — |
| `def` | [TauIntQ.ringEquivInt](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/ring-equiv-int/) | L305-L315 | definition | definition | — |
| `theorem` | [h8_tauint_mathlib_bridge_synthesis](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/h8-tauint-mathlib-bridge-synthesis/) | L335-L352 | proof obligation | formal proof obligation checked | — |

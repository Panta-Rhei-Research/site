---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_slug": "book-i-boundary-bridge-tau-rat-quotient",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean",
  "sha256": "c257acf887a2c40377e19166314f8c9db942960064d560554c3d535b03c007bb",
  "imports": [
    "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
    "TauLib.BookI.Boundary.TauRatField",
    "Mathlib.Algebra.Field.Defs",
    "Mathlib.Algebra.Field.Equiv",
    "Mathlib.Tactic.FieldSimp",
    "Mathlib.Tactic.Linarith",
    "Mathlib.Tactic.Ring"
  ],
  "imported_by": [],
  "registry_ids": [
    "I.D144",
    "I.D15",
    "I.T207"
  ],
  "declaration_counts": {
    "def": 12,
    "theorem": 12
  },
  "declarations": [
    {
      "kind": "def",
      "name": "TauRat.setoid",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/setoid/",
      "source_line_start": 58,
      "source_line_end": 66,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.toQ",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-q/",
      "source_line_start": 69,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.toRat",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat/",
      "source_line_start": 80,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.add_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/add-respects-equiv/",
      "source_line_start": 90,
      "source_line_end": 94,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.mul_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/mul-respects-equiv/",
      "source_line_start": 96,
      "source_line_end": 100,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.negate_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/negate-respects-equiv/",
      "source_line_start": 102,
      "source_line_end": 105,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.add",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/add/",
      "source_line_start": 107,
      "source_line_end": 109,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.mul",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/mul/",
      "source_line_start": 111,
      "source_line_end": 113,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.neg",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/neg/",
      "source_line_start": 115,
      "source_line_end": 117,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.zero",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/zero/",
      "source_line_start": 119,
      "source_line_end": 119,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.one",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/one/",
      "source_line_start": 120,
      "source_line_end": 127,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRatQ.toRat_add",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-add/",
      "source_line_start": 133,
      "source_line_end": 136,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRatQ.toRat_mul",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-mul/",
      "source_line_start": 138,
      "source_line_end": 155,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRatQ.eq_iff_toRat_eq",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/eq-iff-to-rat-eq/",
      "source_line_start": 157,
      "source_line_end": 161,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRatQ.lift_via_toRat",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/lift-via-to-rat/",
      "source_line_start": 163,
      "source_line_end": 165,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRat.inv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv/",
      "source_line_start": 174,
      "source_line_end": 183,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "toRat_inv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-inv/",
      "source_line_start": 186,
      "source_line_end": 236,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRat.inv_respects_equiv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv-respects-equiv/",
      "source_line_start": 238,
      "source_line_end": 241,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.inv",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv-l243/",
      "source_line_start": 243,
      "source_line_end": 369,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.ofRat",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/of-rat/",
      "source_line_start": 381,
      "source_line_end": 382,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRatQ.ofRat_toRat",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/of-rat-to-rat/",
      "source_line_start": 384,
      "source_line_end": 391,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TauRatQ.toRat_ofRat",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-of-rat/",
      "source_line_start": 393,
      "source_line_end": 395,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TauRatQ.ringEquivRat",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/ring-equiv-rat/",
      "source_line_start": 401,
      "source_line_end": 411,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h8_taurat_mathlib_bridge_synthesis",
      "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/h8-taurat-mathlib-bridge-synthesis/",
      "source_line_start": 426,
      "source_line_end": 443,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`
- SHA-256: `c257acf887a2c40377e19166314f8c9db942960064d560554c3d535b03c007bb`

## Registry Links

- `I.D15` — Three-Level Equality

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.Bridge.TauIntQuotient`
- `TauLib.BookI.Boundary.TauRatField`
- `Mathlib.Algebra.Field.Defs`
- `Mathlib.Algebra.Field.Equiv`
- `Mathlib.Tactic.FieldSimp`
- `Mathlib.Tactic.Linarith`
- `Mathlib.Tactic.Ring`

## Imported By

- No TauLib module in the snapshot imports this module.

## Declaration Counts

- `def`: 12
- `theorem`: 12

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [TauRat.setoid](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/setoid/) | L58-L66 | defined | — |
| `def` | [TauRat.toQ](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-q/) | L69-L73 | defined | — |
| `def` | [TauRatQ.toRat](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat/) | L80-L84 | defined | — |
| `theorem` | [TauRat.add_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/add-respects-equiv/) | L90-L94 | formalized | — |
| `theorem` | [TauRat.mul_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/mul-respects-equiv/) | L96-L100 | formalized | — |
| `theorem` | [TauRat.negate_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/negate-respects-equiv/) | L102-L105 | formalized | — |
| `def` | [TauRatQ.add](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/add/) | L107-L109 | defined | — |
| `def` | [TauRatQ.mul](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/mul/) | L111-L113 | defined | — |
| `def` | [TauRatQ.neg](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/neg/) | L115-L117 | defined | — |
| `def` | [TauRatQ.zero](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/zero/) | L119-L119 | defined | — |
| `def` | [TauRatQ.one](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/one/) | L120-L127 | defined | — |
| `theorem` | [TauRatQ.toRat_add](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-add/) | L133-L136 | formalized | — |
| `theorem` | [TauRatQ.toRat_mul](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-mul/) | L138-L155 | formalized | — |
| `theorem` | [TauRatQ.eq_iff_toRat_eq](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/eq-iff-to-rat-eq/) | L157-L161 | formalized | — |
| `theorem` | [TauRatQ.lift_via_toRat](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/lift-via-to-rat/) | L163-L165 | formalized | — |
| `def` | [TauRat.inv](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv/) | L174-L183 | defined | — |
| `theorem` | [toRat_inv](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-inv/) | L186-L236 | formalized | — |
| `theorem` | [TauRat.inv_respects_equiv](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv-respects-equiv/) | L238-L241 | formalized | — |
| `def` | [TauRatQ.inv](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/inv-l243/) | L243-L369 | defined | — |
| `def` | [TauRatQ.ofRat](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/of-rat/) | L381-L382 | defined | — |
| `theorem` | [TauRatQ.ofRat_toRat](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/of-rat-to-rat/) | L384-L391 | formalized | — |
| `theorem` | [TauRatQ.toRat_ofRat](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-of-rat/) | L393-L395 | formalized | — |
| `def` | [TauRatQ.ringEquivRat](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/ring-equiv-rat/) | L401-L411 | defined | — |
| `theorem` | [h8_taurat_mathlib_bridge_synthesis](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/h8-taurat-mathlib-bridge-synthesis/) | L426-L443 | formalized | — |

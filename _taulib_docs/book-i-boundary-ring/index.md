---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.Ring",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.Ring`.",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_slug": "book-i-boundary-ring",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/Ring.lean",
  "sha256": "60f8fa17b6c97aa8efccc43b511eead34a6401b387042f6b73c4977ef5aae797",
  "imports": [
    "TauLib.BookI.Polarity.OmegaRing",
    "TauLib.BookI.Polarity.CRTBasis",
    "TauLib.BookI.Polarity.TeichmuellerLift"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Iota",
    "TauLib.BookI.Boundary.Measure"
  ],
  "registry_ids": [
    "I.D28"
  ],
  "declaration_counts": {
    "theorem": 14,
    "def": 5,
    "example": 13,
    "eval": 10
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "getD_eq_getElem",
      "url": "/verify/taulib/docs/book-i-boundary-ring/get-d-eq-get-elem/",
      "source_line_start": 44,
      "source_line_end": 46,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mul_succ_eq",
      "url": "/verify/taulib/docs/book-i-boundary-ring/mul-succ-eq/",
      "source_line_start": 53,
      "source_line_end": 54,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mul_sub_mod",
      "url": "/verify/taulib/docs/book-i-boundary-ring/mul-sub-mod/",
      "source_line_start": 58,
      "source_line_end": 98,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neg_mod_dvd",
      "url": "/verify/taulib/docs/book-i-boundary-ring/neg-mod-dvd/",
      "source_line_start": 102,
      "source_line_end": 114,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "omega_neg_list",
      "url": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-list/",
      "source_line_start": 120,
      "source_line_end": 122,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_neg_list_length",
      "url": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-list-length/",
      "source_line_start": 124,
      "source_line_end": 127,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mk_omega_tail_neg",
      "url": "/verify/taulib/docs/book-i-boundary-ring/mk-omega-tail-neg/",
      "source_line_start": 130,
      "source_line_end": 133,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_neg_list_getD",
      "url": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-list-get-d/",
      "source_line_start": 135,
      "source_line_end": 149,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_neg_eq_reduce",
      "url": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-eq-reduce/",
      "source_line_start": 152,
      "source_line_end": 157,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_neg_components_eq",
      "url": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-components-eq/",
      "source_line_start": 164,
      "source_line_end": 176,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "Compatible_neg",
      "url": "/verify/taulib/docs/book-i-boundary-ring/compatible-neg/",
      "source_line_start": 183,
      "source_line_end": 194,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "double_neg_mod",
      "url": "/verify/taulib/docs/book-i-boundary-ring/double-neg-mod/",
      "source_line_start": 201,
      "source_line_end": 211,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_neg_neg_eq",
      "url": "/verify/taulib/docs/book-i-boundary-ring/omega-neg-neg-eq/",
      "source_line_start": 214,
      "source_line_end": 225,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "add_neg_cancel_mod",
      "url": "/verify/taulib/docs/book-i-boundary-ring/add-neg-cancel-mod/",
      "source_line_start": 232,
      "source_line_end": 242,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "omega_add_neg_cancel",
      "url": "/verify/taulib/docs/book-i-boundary-ring/omega-add-neg-cancel/",
      "source_line_start": 245,
      "source_line_end": 263,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bdry_ring_axioms",
      "url": "/verify/taulib/docs/book-i-boundary-ring/bdry-ring-axioms/",
      "source_line_start": 270,
      "source_line_end": 292,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "neg_compat_check",
      "url": "/verify/taulib/docs/book-i-boundary-ring/neg-compat-check/",
      "source_line_start": 298,
      "source_line_end": 299,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "add_neg_check",
      "url": "/verify/taulib/docs/book-i-boundary-ring/add-neg-check/",
      "source_line_start": 301,
      "source_line_end": 303,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "double_neg_check",
      "url": "/verify/taulib/docs/book-i-boundary-ring/double-neg-check/",
      "source_line_start": 305,
      "source_line_end": 308,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/example-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l336/",
      "source_line_start": 336,
      "source_line_end": 336,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l337/",
      "source_line_start": 337,
      "source_line_end": 337,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l338/",
      "source_line_start": 338,
      "source_line_end": 338,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l339/",
      "source_line_start": 339,
      "source_line_end": 339,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l341/",
      "source_line_start": 341,
      "source_line_end": 341,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l342/",
      "source_line_start": 342,
      "source_line_end": 342,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-boundary-ring/eval-l343/",
      "source_line_start": 343,
      "source_line_end": 345,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean",
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
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/Ring.lean`
- SHA-256: `60f8fa17b6c97aa8efccc43b511eead34a6401b387042f6b73c4977ef5aae797`

## Registry Links

- `I.D28` — Boundary Local Ring

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.OmegaRing`
- `TauLib.BookI.Polarity.CRTBasis`
- `TauLib.BookI.Polarity.TeichmuellerLift`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Iota`
- `TauLib.BookI.Boundary.Measure`

## Declaration Counts

- `def`: 5
- `eval`: 10
- `example`: 13
- `theorem`: 14

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [getD_eq_getElem](/verify/taulib/docs/book-i-boundary-ring/get-d-eq-get-elem/) | L44-L46 | formalized | — |
| `theorem` | [mul_succ_eq](/verify/taulib/docs/book-i-boundary-ring/mul-succ-eq/) | L53-L54 | formalized | — |
| `theorem` | [mul_sub_mod](/verify/taulib/docs/book-i-boundary-ring/mul-sub-mod/) | L58-L98 | formalized | — |
| `theorem` | [neg_mod_dvd](/verify/taulib/docs/book-i-boundary-ring/neg-mod-dvd/) | L102-L114 | formalized | — |
| `def` | [omega_neg_list](/verify/taulib/docs/book-i-boundary-ring/omega-neg-list/) | L120-L122 | defined | — |
| `theorem` | [omega_neg_list_length](/verify/taulib/docs/book-i-boundary-ring/omega-neg-list-length/) | L124-L127 | formalized | — |
| `def` | [mk_omega_tail_neg](/verify/taulib/docs/book-i-boundary-ring/mk-omega-tail-neg/) | L130-L133 | defined | — |
| `theorem` | [omega_neg_list_getD](/verify/taulib/docs/book-i-boundary-ring/omega-neg-list-get-d/) | L135-L149 | formalized | — |
| `theorem` | [omega_neg_eq_reduce](/verify/taulib/docs/book-i-boundary-ring/omega-neg-eq-reduce/) | L152-L157 | formalized | — |
| `theorem` | [omega_neg_components_eq](/verify/taulib/docs/book-i-boundary-ring/omega-neg-components-eq/) | L164-L176 | formalized | — |
| `theorem` | [Compatible_neg](/verify/taulib/docs/book-i-boundary-ring/compatible-neg/) | L183-L194 | formalized | — |
| `theorem` | [double_neg_mod](/verify/taulib/docs/book-i-boundary-ring/double-neg-mod/) | L201-L211 | formalized | — |
| `theorem` | [omega_neg_neg_eq](/verify/taulib/docs/book-i-boundary-ring/omega-neg-neg-eq/) | L214-L225 | formalized | — |
| `theorem` | [add_neg_cancel_mod](/verify/taulib/docs/book-i-boundary-ring/add-neg-cancel-mod/) | L232-L242 | formalized | — |
| `theorem` | [omega_add_neg_cancel](/verify/taulib/docs/book-i-boundary-ring/omega-add-neg-cancel/) | L245-L263 | formalized | — |
| `theorem` | [bdry_ring_axioms](/verify/taulib/docs/book-i-boundary-ring/bdry-ring-axioms/) | L270-L292 | formalized | — |
| `def` | [neg_compat_check](/verify/taulib/docs/book-i-boundary-ring/neg-compat-check/) | L298-L299 | defined | — |
| `def` | [add_neg_check](/verify/taulib/docs/book-i-boundary-ring/add-neg-check/) | L301-L303 | defined | — |
| `def` | [double_neg_check](/verify/taulib/docs/book-i-boundary-ring/double-neg-check/) | L305-L308 | defined | — |
| `example` | [#eval L314](/verify/taulib/docs/book-i-boundary-ring/example-l314/) | L314-L314 | example | — |
| `example` | [#eval L315](/verify/taulib/docs/book-i-boundary-ring/example-l315/) | L315-L315 | example | — |
| `example` | [#eval L316](/verify/taulib/docs/book-i-boundary-ring/example-l316/) | L316-L316 | example | — |
| `example` | [#eval L317](/verify/taulib/docs/book-i-boundary-ring/example-l317/) | L317-L317 | example | — |
| `example` | [#eval L319](/verify/taulib/docs/book-i-boundary-ring/example-l319/) | L319-L319 | example | — |
| `example` | [#eval L320](/verify/taulib/docs/book-i-boundary-ring/example-l320/) | L320-L320 | example | — |
| `example` | [#eval L321](/verify/taulib/docs/book-i-boundary-ring/example-l321/) | L321-L321 | example | — |
| `example` | [#eval L322](/verify/taulib/docs/book-i-boundary-ring/example-l322/) | L322-L322 | example | — |
| `example` | [#eval L323](/verify/taulib/docs/book-i-boundary-ring/example-l323/) | L323-L323 | example | — |
| `example` | [#eval L325](/verify/taulib/docs/book-i-boundary-ring/example-l325/) | L325-L325 | example | — |
| `example` | [#eval L326](/verify/taulib/docs/book-i-boundary-ring/example-l326/) | L326-L326 | example | — |
| `example` | [#eval L327](/verify/taulib/docs/book-i-boundary-ring/example-l327/) | L327-L327 | example | — |
| `example` | [#eval L328](/verify/taulib/docs/book-i-boundary-ring/example-l328/) | L328-L328 | example | — |
| `eval` | [#eval L334](/verify/taulib/docs/book-i-boundary-ring/eval-l334/) | L334-L334 | computed | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-i-boundary-ring/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L336](/verify/taulib/docs/book-i-boundary-ring/eval-l336/) | L336-L336 | computed | — |
| `eval` | [#eval L337](/verify/taulib/docs/book-i-boundary-ring/eval-l337/) | L337-L337 | computed | — |
| `eval` | [#eval L338](/verify/taulib/docs/book-i-boundary-ring/eval-l338/) | L338-L338 | computed | — |
| `eval` | [#eval L339](/verify/taulib/docs/book-i-boundary-ring/eval-l339/) | L339-L339 | computed | — |
| `eval` | [#eval L340](/verify/taulib/docs/book-i-boundary-ring/eval-l340/) | L340-L340 | computed | — |
| `eval` | [#eval L341](/verify/taulib/docs/book-i-boundary-ring/eval-l341/) | L341-L341 | computed | — |
| `eval` | [#eval L342](/verify/taulib/docs/book-i-boundary-ring/eval-l342/) | L342-L342 | computed | — |
| `eval` | [#eval L343](/verify/taulib/docs/book-i-boundary-ring/eval-l343/) | L343-L345 | computed | — |

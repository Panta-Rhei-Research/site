---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.OmegaGerms",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Polarity.OmegaGerms`.",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_slug": "book-i-polarity-omega-germs",
  "book": "BookI",
  "family": "Polarity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Polarity/OmegaGerms.lean",
  "sha256": "a9d07b9dbe3cc6b55c28928d77b6c4853afbc6e723cb0716e6714021e5610955",
  "imports": [
    "TauLib.BookI.Polarity.ModArith"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.IotaTauStructural",
    "TauLib.BookI.Denotation.Structural",
    "TauLib.BookI.Holomorphy.IdentityTheorem",
    "TauLib.BookI.Holomorphy.TauHolomorphic",
    "TauLib.BookI.Polarity.InverseLimit",
    "TauLib.BookI.Polarity.OmegaRing",
    "TauLib.BookI.Polarity.PolarizedGerms",
    "TauLib.BookI.Sets.UniqueInfinity"
  ],
  "registry_ids": [
    "I.D25"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 17,
    "theorem": 13,
    "example": 9,
    "eval": 13
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "OmegaTail",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/omega-tail/",
      "source_line_start": 36,
      "source_line_end": 40,
      "formal_status": "defined",
      "registry_ids": [
        "I.D25"
      ]
    },
    {
      "kind": "def",
      "name": "nat_to_tail_go",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-go/",
      "source_line_start": 43,
      "source_line_end": 47,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nat_to_tail_components",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-components/",
      "source_line_start": 50,
      "source_line_end": 51,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nat_to_tail",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/nat-to-tail/",
      "source_line_start": 54,
      "source_line_end": 56,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "OmegaTail.get",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/get/",
      "source_line_start": 63,
      "source_line_end": 64,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "compat_inner",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/compat-inner/",
      "source_line_start": 74,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "compat_outer",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/compat-outer/",
      "source_line_start": 85,
      "source_line_end": 89,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "compat_check",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/compat-check/",
      "source_line_start": 91,
      "source_line_end": 92,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Compatible",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/compatible/",
      "source_line_start": 100,
      "source_line_end": 102,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tail_list",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/tail-list/",
      "source_line_start": 110,
      "source_line_end": 112,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tail_list_length",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/tail-list-length/",
      "source_line_start": 114,
      "source_line_end": 117,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mk_omega_tail",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "getD_eq_getElem",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/get-d-eq-get-elem/",
      "source_line_start": 124,
      "source_line_end": 126,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tail_list_getD",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/tail-list-get-d/",
      "source_line_start": 128,
      "source_line_end": 144,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mk_omega_tail_compat",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-compat/",
      "source_line_start": 148,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mk_omega_tail_getD",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-get-d/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l167/",
      "source_line_start": 167,
      "source_line_end": 167,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l168/",
      "source_line_start": 168,
      "source_line_end": 168,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l169/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "equiv_go",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/equiv-go/",
      "source_line_start": 176,
      "source_line_end": 183,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tail_equiv",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/tail-equiv/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "diverge_go",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go/",
      "source_line_start": 195,
      "source_line_end": 203,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "divergence_depth",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/divergence-depth/",
      "source_line_start": 207,
      "source_line_end": 209,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ultra_dist",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-dist/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diverge_go_comm",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-comm/",
      "source_line_start": 219,
      "source_line_end": 234,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_symmetric",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-symmetric/",
      "source_line_start": 237,
      "source_line_end": 242,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "agree_at_trans",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/agree-at-trans/",
      "source_line_start": 245,
      "source_line_end": 247,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ultra_symmetry_check",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-symmetry-check/",
      "source_line_start": 250,
      "source_line_end": 251,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ultra_triangle_check",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-check/",
      "source_line_start": 260,
      "source_line_end": 263,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diverge_go_zero_or_gt",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-zero-or-gt/",
      "source_line_start": 270,
      "source_line_end": 288,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diverge_go_triangle",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-triangle/",
      "source_line_start": 293,
      "source_line_end": 336,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_dist_eq_diverge",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-dist-eq-diverge/",
      "source_line_start": 339,
      "source_line_end": 342,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_triangle",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle/",
      "source_line_start": 346,
      "source_line_end": 353,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_triangle_mk",
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-mk/",
      "source_line_start": 356,
      "source_line_end": 361,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l376/",
      "source_line_start": 376,
      "source_line_end": 377,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l378/",
      "source_line_start": 378,
      "source_line_end": 379,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l380/",
      "source_line_start": 380,
      "source_line_end": 381,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l382/",
      "source_line_start": 382,
      "source_line_end": 383,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l384/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l386/",
      "source_line_start": 386,
      "source_line_end": 387,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l394/",
      "source_line_start": 394,
      "source_line_end": 394,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l395/",
      "source_line_start": 395,
      "source_line_end": 395,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l396/",
      "source_line_start": 396,
      "source_line_end": 396,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l399/",
      "source_line_start": 399,
      "source_line_end": 399,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l400/",
      "source_line_start": 400,
      "source_line_end": 400,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l401/",
      "source_line_start": 401,
      "source_line_end": 401,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l404/",
      "source_line_start": 404,
      "source_line_end": 404,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l405/",
      "source_line_start": 405,
      "source_line_end": 405,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l408/",
      "source_line_start": 408,
      "source_line_end": 408,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l409/",
      "source_line_start": 409,
      "source_line_end": 409,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l410/",
      "source_line_start": 410,
      "source_line_end": 410,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-omega-germs/eval-l414/",
      "source_line_start": 414,
      "source_line_end": 416,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean",
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
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Polarity/OmegaGerms.lean`
- SHA-256: `a9d07b9dbe3cc6b55c28928d77b6c4853afbc6e723cb0716e6714021e5610955`

## Registry Links

- `I.D25` — Omega-Tail (Compatible Tower)

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.ModArith`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.IotaTauStructural`
- `TauLib.BookI.Denotation.Structural`
- `TauLib.BookI.Holomorphy.IdentityTheorem`
- `TauLib.BookI.Holomorphy.TauHolomorphic`
- `TauLib.BookI.Polarity.InverseLimit`
- `TauLib.BookI.Polarity.OmegaRing`
- `TauLib.BookI.Polarity.PolarizedGerms`
- `TauLib.BookI.Sets.UniqueInfinity`

## Declaration Counts

- `def`: 17
- `eval`: 13
- `example`: 9
- `structure`: 1
- `theorem`: 13

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [OmegaTail](/verify/taulib/docs/book-i-polarity-omega-germs/omega-tail/) | L36-L40 | defined | `I.D25` |
| `def` | [nat_to_tail_go](/verify/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-go/) | L43-L47 | defined | — |
| `def` | [nat_to_tail_components](/verify/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-components/) | L50-L51 | defined | — |
| `def` | [nat_to_tail](/verify/taulib/docs/book-i-polarity-omega-germs/nat-to-tail/) | L54-L56 | defined | — |
| `def` | [OmegaTail.get](/verify/taulib/docs/book-i-polarity-omega-germs/get/) | L63-L64 | defined | — |
| `def` | [compat_inner](/verify/taulib/docs/book-i-polarity-omega-germs/compat-inner/) | L74-L81 | defined | — |
| `def` | [compat_outer](/verify/taulib/docs/book-i-polarity-omega-germs/compat-outer/) | L85-L89 | defined | — |
| `def` | [compat_check](/verify/taulib/docs/book-i-polarity-omega-germs/compat-check/) | L91-L92 | defined | — |
| `def` | [Compatible](/verify/taulib/docs/book-i-polarity-omega-germs/compatible/) | L100-L102 | defined | — |
| `def` | [tail_list](/verify/taulib/docs/book-i-polarity-omega-germs/tail-list/) | L110-L112 | defined | — |
| `theorem` | [tail_list_length](/verify/taulib/docs/book-i-polarity-omega-germs/tail-list-length/) | L114-L117 | formalized | — |
| `def` | [mk_omega_tail](/verify/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail/) | L120-L121 | defined | — |
| `theorem` | [getD_eq_getElem](/verify/taulib/docs/book-i-polarity-omega-germs/get-d-eq-get-elem/) | L124-L126 | formalized | — |
| `theorem` | [tail_list_getD](/verify/taulib/docs/book-i-polarity-omega-germs/tail-list-get-d/) | L128-L144 | formalized | — |
| `theorem` | [mk_omega_tail_compat](/verify/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-compat/) | L148-L158 | formalized | — |
| `theorem` | [mk_omega_tail_getD](/verify/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-get-d/) | L161-L163 | formalized | — |
| `example` | [#eval L167](/verify/taulib/docs/book-i-polarity-omega-germs/example-l167/) | L167-L167 | example | — |
| `example` | [#eval L168](/verify/taulib/docs/book-i-polarity-omega-germs/example-l168/) | L168-L168 | example | — |
| `example` | [#eval L169](/verify/taulib/docs/book-i-polarity-omega-germs/example-l169/) | L169-L169 | example | — |
| `def` | [equiv_go](/verify/taulib/docs/book-i-polarity-omega-germs/equiv-go/) | L176-L183 | defined | — |
| `def` | [tail_equiv](/verify/taulib/docs/book-i-polarity-omega-germs/tail-equiv/) | L186-L188 | defined | — |
| `def` | [diverge_go](/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go/) | L195-L203 | defined | — |
| `def` | [divergence_depth](/verify/taulib/docs/book-i-polarity-omega-germs/divergence-depth/) | L207-L209 | defined | — |
| `def` | [ultra_dist](/verify/taulib/docs/book-i-polarity-omega-germs/ultra-dist/) | L212-L212 | defined | — |
| `theorem` | [diverge_go_comm](/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-comm/) | L219-L234 | formalized | — |
| `theorem` | [ultra_symmetric](/verify/taulib/docs/book-i-polarity-omega-germs/ultra-symmetric/) | L237-L242 | formalized | — |
| `theorem` | [agree_at_trans](/verify/taulib/docs/book-i-polarity-omega-germs/agree-at-trans/) | L245-L247 | formalized | — |
| `def` | [ultra_symmetry_check](/verify/taulib/docs/book-i-polarity-omega-germs/ultra-symmetry-check/) | L250-L251 | defined | — |
| `def` | [ultra_triangle_check](/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-check/) | L260-L263 | defined | — |
| `theorem` | [diverge_go_zero_or_gt](/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-zero-or-gt/) | L270-L288 | formalized | — |
| `theorem` | [diverge_go_triangle](/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-triangle/) | L293-L336 | formalized | — |
| `theorem` | [ultra_dist_eq_diverge](/verify/taulib/docs/book-i-polarity-omega-germs/ultra-dist-eq-diverge/) | L339-L342 | formalized | — |
| `theorem` | [ultra_triangle](/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle/) | L346-L353 | formalized | — |
| `theorem` | [ultra_triangle_mk](/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-mk/) | L356-L361 | formalized | — |
| `example` | [#eval L376](/verify/taulib/docs/book-i-polarity-omega-germs/example-l376/) | L376-L377 | example | — |
| `example` | [#eval L378](/verify/taulib/docs/book-i-polarity-omega-germs/example-l378/) | L378-L379 | example | — |
| `example` | [#eval L380](/verify/taulib/docs/book-i-polarity-omega-germs/example-l380/) | L380-L381 | example | — |
| `example` | [#eval L382](/verify/taulib/docs/book-i-polarity-omega-germs/example-l382/) | L382-L383 | example | — |
| `example` | [#eval L384](/verify/taulib/docs/book-i-polarity-omega-germs/example-l384/) | L384-L385 | example | — |
| `example` | [#eval L386](/verify/taulib/docs/book-i-polarity-omega-germs/example-l386/) | L386-L387 | example | — |
| `eval` | [#eval L394](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l394/) | L394-L394 | computed | — |
| `eval` | [#eval L395](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l395/) | L395-L395 | computed | — |
| `eval` | [#eval L396](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l396/) | L396-L396 | computed | — |
| `eval` | [#eval L399](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l399/) | L399-L399 | computed | — |
| `eval` | [#eval L400](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l400/) | L400-L400 | computed | — |
| `eval` | [#eval L401](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l401/) | L401-L401 | computed | — |
| `eval` | [#eval L404](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l404/) | L404-L404 | computed | — |
| `eval` | [#eval L405](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l405/) | L405-L405 | computed | — |
| `eval` | [#eval L408](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l408/) | L408-L408 | computed | — |
| `eval` | [#eval L409](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l409/) | L409-L409 | computed | — |
| `eval` | [#eval L410](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l410/) | L410-L410 | computed | — |
| `eval` | [#eval L413](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l413/) | L413-L413 | computed | — |
| `eval` | [#eval L414](/verify/taulib/docs/book-i-polarity-omega-germs/eval-l414/) | L414-L416 | computed | — |

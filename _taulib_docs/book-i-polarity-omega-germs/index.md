---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.OmegaGerms",
  "permalink": "/corpus/taulib/docs/book-i-polarity-omega-germs/",
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
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/omega-tail/",
      "source_line_start": 36,
      "source_line_end": 40,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "I.D25"
      ]
    },
    {
      "kind": "def",
      "name": "nat_to_tail_go",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-go/",
      "source_line_start": 43,
      "source_line_end": 47,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nat_to_tail_components",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-components/",
      "source_line_start": 50,
      "source_line_end": 51,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nat_to_tail",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/nat-to-tail/",
      "source_line_start": 54,
      "source_line_end": 56,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "OmegaTail.get",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/get/",
      "source_line_start": 63,
      "source_line_end": 64,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "compat_inner",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/compat-inner/",
      "source_line_start": 74,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "compat_outer",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/compat-outer/",
      "source_line_start": 85,
      "source_line_end": 89,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "compat_check",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/compat-check/",
      "source_line_start": 91,
      "source_line_end": 92,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Compatible",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/compatible/",
      "source_line_start": 100,
      "source_line_end": 102,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tail_list",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/tail-list/",
      "source_line_start": 110,
      "source_line_end": 112,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tail_list_length",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/tail-list-length/",
      "source_line_start": 114,
      "source_line_end": 117,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mk_omega_tail",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail/",
      "source_line_start": 120,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "getD_eq_getElem",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/get-d-eq-get-elem/",
      "source_line_start": 124,
      "source_line_end": 126,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tail_list_getD",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/tail-list-get-d/",
      "source_line_start": 128,
      "source_line_end": 144,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mk_omega_tail_compat",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-compat/",
      "source_line_start": 148,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mk_omega_tail_getD",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-get-d/",
      "source_line_start": 161,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l167/",
      "source_line_start": 167,
      "source_line_end": 167,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l168/",
      "source_line_start": 168,
      "source_line_end": 168,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l169/",
      "source_line_start": 169,
      "source_line_end": 169,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "equiv_go",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/equiv-go/",
      "source_line_start": 176,
      "source_line_end": 183,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tail_equiv",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/tail-equiv/",
      "source_line_start": 186,
      "source_line_end": 188,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "diverge_go",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go/",
      "source_line_start": 195,
      "source_line_end": 203,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "divergence_depth",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/divergence-depth/",
      "source_line_start": 207,
      "source_line_end": 209,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ultra_dist",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-dist/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diverge_go_comm",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go-comm/",
      "source_line_start": 219,
      "source_line_end": 234,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_symmetric",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-symmetric/",
      "source_line_start": 237,
      "source_line_end": 242,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "agree_at_trans",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/agree-at-trans/",
      "source_line_start": 245,
      "source_line_end": 247,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ultra_symmetry_check",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-symmetry-check/",
      "source_line_start": 250,
      "source_line_end": 251,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "ultra_triangle_check",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-check/",
      "source_line_start": 260,
      "source_line_end": 263,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diverge_go_zero_or_gt",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go-zero-or-gt/",
      "source_line_start": 270,
      "source_line_end": 288,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "diverge_go_triangle",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go-triangle/",
      "source_line_start": 293,
      "source_line_end": 336,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_dist_eq_diverge",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-dist-eq-diverge/",
      "source_line_start": 339,
      "source_line_end": 342,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_triangle",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-triangle/",
      "source_line_start": 346,
      "source_line_end": 353,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ultra_triangle_mk",
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-mk/",
      "source_line_start": 356,
      "source_line_end": 361,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l376/",
      "source_line_start": 376,
      "source_line_end": 377,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l378/",
      "source_line_start": 378,
      "source_line_end": 379,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l380/",
      "source_line_start": 380,
      "source_line_end": 381,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l382/",
      "source_line_start": 382,
      "source_line_end": 383,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l384/",
      "source_line_start": 384,
      "source_line_end": 385,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/example-l386/",
      "source_line_start": 386,
      "source_line_end": 387,
      "formal_status": "example",
      "declaration_role": "example check",
      "formal_status_label": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l394/",
      "source_line_start": 394,
      "source_line_end": 394,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l395/",
      "source_line_start": 395,
      "source_line_end": 395,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l396/",
      "source_line_start": 396,
      "source_line_end": 396,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l399/",
      "source_line_start": 399,
      "source_line_end": 399,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l400/",
      "source_line_start": 400,
      "source_line_end": 400,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l401/",
      "source_line_start": 401,
      "source_line_end": 401,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l404/",
      "source_line_start": 404,
      "source_line_end": 404,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l405/",
      "source_line_start": 405,
      "source_line_end": 405,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l408/",
      "source_line_start": 408,
      "source_line_end": 408,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l409/",
      "source_line_start": 409,
      "source_line_end": 409,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l410/",
      "source_line_start": 410,
      "source_line_end": 410,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l413/",
      "source_line_start": 413,
      "source_line_end": 413,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l414/",
      "source_line_start": 414,
      "source_line_end": 416,
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

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [OmegaTail](/corpus/taulib/docs/book-i-polarity-omega-germs/omega-tail/) | L36-L40 | type/data schema | type/data schema | `I.D25` |
| `def` | [nat_to_tail_go](/corpus/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-go/) | L43-L47 | data/computed value | data/computed value | — |
| `def` | [nat_to_tail_components](/corpus/taulib/docs/book-i-polarity-omega-germs/nat-to-tail-components/) | L50-L51 | data/computed value | data/computed value | — |
| `def` | [nat_to_tail](/corpus/taulib/docs/book-i-polarity-omega-germs/nat-to-tail/) | L54-L56 | definition | definition | — |
| `def` | [OmegaTail.get](/corpus/taulib/docs/book-i-polarity-omega-germs/get/) | L63-L64 | data/computed value | data/computed value | — |
| `def` | [compat_inner](/corpus/taulib/docs/book-i-polarity-omega-germs/compat-inner/) | L74-L81 | data/computed value | data/computed value | — |
| `def` | [compat_outer](/corpus/taulib/docs/book-i-polarity-omega-germs/compat-outer/) | L85-L89 | data/computed value | data/computed value | — |
| `def` | [compat_check](/corpus/taulib/docs/book-i-polarity-omega-germs/compat-check/) | L91-L92 | data/computed value | data/computed value | — |
| `def` | [Compatible](/corpus/taulib/docs/book-i-polarity-omega-germs/compatible/) | L100-L102 | definition | definition | — |
| `def` | [tail_list](/corpus/taulib/docs/book-i-polarity-omega-germs/tail-list/) | L110-L112 | data/computed value | data/computed value | — |
| `theorem` | [tail_list_length](/corpus/taulib/docs/book-i-polarity-omega-germs/tail-list-length/) | L114-L117 | proof obligation | formal proof obligation checked | — |
| `def` | [mk_omega_tail](/corpus/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail/) | L120-L121 | definition | definition | — |
| `theorem` | [getD_eq_getElem](/corpus/taulib/docs/book-i-polarity-omega-germs/get-d-eq-get-elem/) | L124-L126 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tail_list_getD](/corpus/taulib/docs/book-i-polarity-omega-germs/tail-list-get-d/) | L128-L144 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mk_omega_tail_compat](/corpus/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-compat/) | L148-L158 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mk_omega_tail_getD](/corpus/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-get-d/) | L161-L163 | proof obligation | formal proof obligation checked | — |
| `example` | [#eval L167](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l167/) | L167-L167 | example check | example | — |
| `example` | [#eval L168](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l168/) | L168-L168 | example check | example | — |
| `example` | [#eval L169](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l169/) | L169-L169 | example check | example | — |
| `def` | [equiv_go](/corpus/taulib/docs/book-i-polarity-omega-germs/equiv-go/) | L176-L183 | data/computed value | data/computed value | — |
| `def` | [tail_equiv](/corpus/taulib/docs/book-i-polarity-omega-germs/tail-equiv/) | L186-L188 | data/computed value | data/computed value | — |
| `def` | [diverge_go](/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go/) | L195-L203 | data/computed value | data/computed value | — |
| `def` | [divergence_depth](/corpus/taulib/docs/book-i-polarity-omega-germs/divergence-depth/) | L207-L209 | definition | definition | — |
| `def` | [ultra_dist](/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-dist/) | L212-L212 | definition | definition | — |
| `theorem` | [diverge_go_comm](/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go-comm/) | L219-L234 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ultra_symmetric](/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-symmetric/) | L237-L242 | proof obligation | formal proof obligation checked | — |
| `theorem` | [agree_at_trans](/corpus/taulib/docs/book-i-polarity-omega-germs/agree-at-trans/) | L245-L247 | proof obligation | formal proof obligation checked | — |
| `def` | [ultra_symmetry_check](/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-symmetry-check/) | L250-L251 | data/computed value | data/computed value | — |
| `def` | [ultra_triangle_check](/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-check/) | L260-L263 | data/computed value | data/computed value | — |
| `theorem` | [diverge_go_zero_or_gt](/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go-zero-or-gt/) | L270-L288 | proof obligation | formal proof obligation checked | — |
| `theorem` | [diverge_go_triangle](/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go-triangle/) | L293-L336 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ultra_dist_eq_diverge](/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-dist-eq-diverge/) | L339-L342 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ultra_triangle](/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-triangle/) | L346-L353 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ultra_triangle_mk](/corpus/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-mk/) | L356-L361 | proof obligation | formal proof obligation checked | — |
| `example` | [#eval L376](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l376/) | L376-L377 | example check | example | — |
| `example` | [#eval L378](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l378/) | L378-L379 | example check | example | — |
| `example` | [#eval L380](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l380/) | L380-L381 | example check | example | — |
| `example` | [#eval L382](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l382/) | L382-L383 | example check | example | — |
| `example` | [#eval L384](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l384/) | L384-L385 | example check | example | — |
| `example` | [#eval L386](/corpus/taulib/docs/book-i-polarity-omega-germs/example-l386/) | L386-L387 | example check | example | — |
| `eval` | [#eval L394](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l394/) | L394-L394 | computed check | computed check | — |
| `eval` | [#eval L395](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l395/) | L395-L395 | computed check | computed check | — |
| `eval` | [#eval L396](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l396/) | L396-L396 | computed check | computed check | — |
| `eval` | [#eval L399](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l399/) | L399-L399 | computed check | computed check | — |
| `eval` | [#eval L400](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l400/) | L400-L400 | computed check | computed check | — |
| `eval` | [#eval L401](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l401/) | L401-L401 | computed check | computed check | — |
| `eval` | [#eval L404](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l404/) | L404-L404 | computed check | computed check | — |
| `eval` | [#eval L405](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l405/) | L405-L405 | computed check | computed check | — |
| `eval` | [#eval L408](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l408/) | L408-L408 | computed check | computed check | — |
| `eval` | [#eval L409](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l409/) | L409-L409 | computed check | computed check | — |
| `eval` | [#eval L410](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l410/) | L410-L410 | computed check | computed check | — |
| `eval` | [#eval L413](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l413/) | L413-L413 | computed check | computed check | — |
| `eval` | [#eval L414](/corpus/taulib/docs/book-i-polarity-omega-germs/eval-l414/) | L414-L416 | computed check | computed check | — |

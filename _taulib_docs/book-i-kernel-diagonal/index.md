---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Kernel.Diagonal",
  "permalink": "/verify/taulib/docs/book-i-kernel-diagonal/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Kernel.Diagonal`.",
  "module_name": "TauLib.BookI.Kernel.Diagonal",
  "module_slug": "book-i-kernel-diagonal",
  "book": "BookI",
  "family": "Kernel",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Kernel/Diagonal.lean",
  "sha256": "844b6d4ae236520eba8f9dc1f63bd78058e8d1674bd48531eacdd1ca2ff40237",
  "imports": [
    "TauLib.BookI.Kernel.Axioms"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.CF.WindowAlgebra",
    "TauLib.BookI.Holomorphy.DiagonalProtection",
    "TauLib.BookI.MetaLogic.Substrate",
    "TauLib.BookI.Orbit.Ladder",
    "TauLib.BookV.GravityField.BipolarHolonomy",
    "TauLib.Tour.Foundations"
  ],
  "registry_ids": [
    "I.D03"
  ],
  "declaration_counts": {
    "theorem": 7,
    "def": 1
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "diagonal_channel_count",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/diagonal-channel-count/",
      "source_line_start": 38,
      "source_line_end": 39,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D03"
      ]
    },
    {
      "kind": "theorem",
      "name": "nonOmega_complete",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/non-omega-complete/",
      "source_line_start": 42,
      "source_line_end": 44,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "solenoidalGenerators",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-generators/",
      "source_line_start": 52,
      "source_line_end": 52,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "solenoidal_count",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-count/",
      "source_line_start": 55,
      "source_line_end": 56,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "solenoidal_ne_alpha",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-ne-alpha/",
      "source_line_start": 59,
      "source_line_end": 62,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "solenoidal_ne_omega",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-ne-omega/",
      "source_line_start": 65,
      "source_line_end": 68,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rewiring_levels_eq_solenoidal",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/rewiring-levels-eq-solenoidal/",
      "source_line_start": 77,
      "source_line_end": 79,
      "formal_status": "formalized",
      "registry_ids": [
        "I.D03"
      ]
    },
    {
      "kind": "theorem",
      "name": "alpha_unique_scaffold",
      "url": "/verify/taulib/docs/book-i-kernel-diagonal/alpha-unique-scaffold/",
      "source_line_start": 83,
      "source_line_end": 87,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean",
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
- Source path: [`TauLib/BookI/Kernel/Diagonal.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Kernel/Diagonal.lean`
- SHA-256: `844b6d4ae236520eba8f9dc1f63bd78058e8d1674bd48531eacdd1ca2ff40237`

## Registry Links

- `I.D03` — Diagonal Discipline

## Construction Spine Links

- [Build the τ-Kernel](/corpus/construction-spine/build-the-kernel/)

## Imports

- `TauLib.BookI.Kernel.Axioms`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.CF.WindowAlgebra`
- `TauLib.BookI.Holomorphy.DiagonalProtection`
- `TauLib.BookI.MetaLogic.Substrate`
- `TauLib.BookI.Orbit.Ladder`
- `TauLib.BookV.GravityField.BipolarHolonomy`
- `TauLib.Tour.Foundations`

## Declaration Counts

- `def`: 1
- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [diagonal_channel_count](/verify/taulib/docs/book-i-kernel-diagonal/diagonal-channel-count/) | L38-L39 | formalized | `I.D03` |
| `theorem` | [nonOmega_complete](/verify/taulib/docs/book-i-kernel-diagonal/non-omega-complete/) | L42-L44 | formalized | — |
| `def` | [solenoidalGenerators](/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-generators/) | L52-L52 | defined | — |
| `theorem` | [solenoidal_count](/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-count/) | L55-L56 | formalized | — |
| `theorem` | [solenoidal_ne_alpha](/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-ne-alpha/) | L59-L62 | formalized | — |
| `theorem` | [solenoidal_ne_omega](/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-ne-omega/) | L65-L68 | formalized | — |
| `theorem` | [rewiring_levels_eq_solenoidal](/verify/taulib/docs/book-i-kernel-diagonal/rewiring-levels-eq-solenoidal/) | L77-L79 | formalized | `I.D03` |
| `theorem` | [alpha_unique_scaffold](/verify/taulib/docs/book-i-kernel-diagonal/alpha-unique-scaffold/) | L83-L87 | formalized | — |

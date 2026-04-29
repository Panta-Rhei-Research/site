---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Orbit.Rigidity",
  "permalink": "/verify/taulib/docs/book-i-orbit-rigidity/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Orbit.Rigidity`.",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_slug": "book-i-orbit-rigidity",
  "book": "BookI",
  "family": "Orbit",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Orbit/Rigidity.lean",
  "sha256": "6682e1e98b709e088ee20f9c3a28767d01cd5c2963cae8f3fd9f46c63b58bcf5",
  "imports": [
    "TauLib.BookI.Orbit.Closure"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Denotation.SolenoidPitch",
    "TauLib.BookI.Denotation.Structural",
    "TauLib.BookI.Orbit.TooMany",
    "TauLib.Meta.PrintAxioms",
    "TauLib.Tour.Foundations",
    "TauLib.Tour.VerifyItYourself"
  ],
  "registry_ids": [
    "I.T07",
    "I.T08"
  ],
  "declaration_counts": {
    "theorem": 7,
    "structure": 2,
    "def": 1
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "rho_seed_omega",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/rho-seed-omega/",
      "source_line_start": 19,
      "source_line_end": 20,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauAutomorphism",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/tau-automorphism/",
      "source_line_start": 23,
      "source_line_end": 28,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "auto_omega_to_omega",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/auto-omega-to-omega/",
      "source_line_start": 31,
      "source_line_end": 39,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "auto_non_omega",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/auto-non-omega/",
      "source_line_start": 42,
      "source_line_end": 50,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "auto_shift",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/auto-shift/",
      "source_line_start": 53,
      "source_line_end": 61,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rigidity_depth",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/rigidity-depth/",
      "source_line_start": 64,
      "source_line_end": 129,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "rigidity_non_omega",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/rigidity-non-omega/",
      "source_line_start": 132,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T07"
      ]
    },
    {
      "kind": "structure",
      "name": "TauModel",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/tau-model/",
      "source_line_start": 141,
      "source_line_end": 146,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "interpret",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/interpret/",
      "source_line_start": 149,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "categoricity_non_omega",
      "url": "/verify/taulib/docs/book-i-orbit-rigidity/categoricity-non-omega/",
      "source_line_start": 153,
      "source_line_end": 166,
      "formal_status": "formalized",
      "registry_ids": [
        "I.T08"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean",
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
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Orbit/Rigidity.lean`
- SHA-256: `6682e1e98b709e088ee20f9c3a28767d01cd5c2963cae8f3fd9f46c63b58bcf5`

## Registry Links

- `I.T07` — Rigidity of tau
- `I.T08` — Categoricity of tau_0

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Orbit.Closure`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Denotation.SolenoidPitch`
- `TauLib.BookI.Denotation.Structural`
- `TauLib.BookI.Orbit.TooMany`
- `TauLib.Meta.PrintAxioms`
- `TauLib.Tour.Foundations`
- `TauLib.Tour.VerifyItYourself`

## Declaration Counts

- `def`: 1
- `structure`: 2
- `theorem`: 7

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [rho_seed_omega](/verify/taulib/docs/book-i-orbit-rigidity/rho-seed-omega/) | L19-L20 | formalized | — |
| `structure` | [TauAutomorphism](/verify/taulib/docs/book-i-orbit-rigidity/tau-automorphism/) | L23-L28 | defined | — |
| `theorem` | [auto_omega_to_omega](/verify/taulib/docs/book-i-orbit-rigidity/auto-omega-to-omega/) | L31-L39 | formalized | — |
| `theorem` | [auto_non_omega](/verify/taulib/docs/book-i-orbit-rigidity/auto-non-omega/) | L42-L50 | formalized | — |
| `theorem` | [auto_shift](/verify/taulib/docs/book-i-orbit-rigidity/auto-shift/) | L53-L61 | formalized | — |
| `theorem` | [rigidity_depth](/verify/taulib/docs/book-i-orbit-rigidity/rigidity-depth/) | L64-L129 | formalized | — |
| `theorem` | [rigidity_non_omega](/verify/taulib/docs/book-i-orbit-rigidity/rigidity-non-omega/) | L132-L138 | formalized | `I.T07` |
| `structure` | [TauModel](/verify/taulib/docs/book-i-orbit-rigidity/tau-model/) | L141-L146 | defined | — |
| `def` | [interpret](/verify/taulib/docs/book-i-orbit-rigidity/interpret/) | L149-L150 | defined | — |
| `theorem` | [categoricity_non_omega](/verify/taulib/docs/book-i-orbit-rigidity/categoricity-non-omega/) | L153-L166 | formalized | `I.T08` |

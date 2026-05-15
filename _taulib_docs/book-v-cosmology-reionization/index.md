---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Cosmology.Reionization",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-reionization/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Cosmology.Reionization`.",
  "module_name": "TauLib.BookV.Cosmology.Reionization",
  "module_slug": "book-v-cosmology-reionization",
  "book": "BookV",
  "family": "Cosmology",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Cosmology/Reionization.lean",
  "sha256": "8feef1174aa4523bfa961e550681c5b02d8d5a97c468f2a8f3b4b39af7473e78",
  "imports": [
    "TauLib.BookV.Cosmology.NeutrinoBackground"
  ],
  "imported_by": [
    "TauLib.BookV"
  ],
  "registry_ids": [
    "V.D334",
    "V.D335",
    "V.P189",
    "V.R470",
    "V.T271"
  ],
  "declaration_counts": {
    "structure": 1,
    "inductive": 1,
    "def": 2,
    "theorem": 2
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "BrightnessTemp21cm",
      "url": "/corpus/taulib/docs/book-v-cosmology-reionization/brightness-temp21cm/",
      "source_line_start": 45,
      "source_line_end": 55,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D334"
      ]
    },
    {
      "kind": "inductive",
      "name": "SpinTempCoupling",
      "url": "/corpus/taulib/docs/book-v-cosmology-reionization/spin-temp-coupling/",
      "source_line_start": 59,
      "source_line_end": 68,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D335"
      ]
    },
    {
      "kind": "def",
      "name": "absorption_trough_z17_mK",
      "url": "/corpus/taulib/docs/book-v-cosmology-reionization/absorption-trough-z17-m-k/",
      "source_line_start": 77,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "V.T271"
      ]
    },
    {
      "kind": "def",
      "name": "z_reion",
      "url": "/corpus/taulib/docs/book-v-cosmology-reionization/z-reion/",
      "source_line_start": 81,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "z_reion_pos",
      "url": "/corpus/taulib/docs/book-v-cosmology-reionization/z-reion-pos/",
      "source_line_start": 84,
      "source_line_end": 84,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "trough_is_absorption",
      "url": "/corpus/taulib/docs/book-v-cosmology-reionization/trough-is-absorption/",
      "source_line_start": 87,
      "source_line_end": 104,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P189",
        "V.R470"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean",
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
- Source path: [`TauLib/BookV/Cosmology/Reionization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Cosmology/Reionization.lean`
- SHA-256: `8feef1174aa4523bfa961e550681c5b02d8d5a97c468f2a8f3b4b39af7473e78`

## Registry Links

- `V.D334` — 21cm Brightness Temperature
- `V.D335` — Spin Temperature Coupling Regimes
- `V.P189` — EDGES/HERA/SKA Predictions
- `V.R470` — V.OP9 Status: PARTIAL-IMPROVED
- `V.T271` — 21cm Absorption Trough from tau-Native Inputs

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Cosmology.NeutrinoBackground`

## Imported By

- `TauLib.BookV`

## Declaration Counts

- `def`: 2
- `inductive`: 1
- `structure`: 1
- `theorem`: 2

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [BrightnessTemp21cm](/corpus/taulib/docs/book-v-cosmology-reionization/brightness-temp21cm/) | L45-L55 | type/data schema | type/data schema | `V.D334` |
| `inductive` | [SpinTempCoupling](/corpus/taulib/docs/book-v-cosmology-reionization/spin-temp-coupling/) | L59-L68 | type/data schema | type/data schema | `V.D335` |
| `def` | [absorption_trough_z17_mK](/corpus/taulib/docs/book-v-cosmology-reionization/absorption-trough-z17-m-k/) | L77-L77 | data/computed value | data/computed value | `V.T271` |
| `def` | [z_reion](/corpus/taulib/docs/book-v-cosmology-reionization/z-reion/) | L81-L81 | data/computed value | data/computed value | — |
| `theorem` | [z_reion_pos](/corpus/taulib/docs/book-v-cosmology-reionization/z-reion-pos/) | L84-L84 | proof obligation | formal proof obligation checked | — |
| `theorem` | [trough_is_absorption](/corpus/taulib/docs/book-v-cosmology-reionization/trough-is-absorption/) | L87-L104 | proof obligation | formal proof obligation checked | `V.P189`, `V.R470` |

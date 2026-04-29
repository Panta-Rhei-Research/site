---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Addressability.AddressResolution",
  "permalink": "/verify/taulib/docs/book-i-addressability-address-resolution/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Addressability.AddressResolution`.",
  "module_name": "TauLib.BookI.Addressability.AddressResolution",
  "module_slug": "book-i-addressability-address-resolution",
  "book": "BookI",
  "family": "Addressability",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Addressability/AddressResolution.lean",
  "sha256": "c0b13d53f97514f497d4077ce6d7c7ea42b55d7daafe3d9cb282d3a2c18b0a35",
  "imports": [
    "TauLib.BookI.Addressability.OnticUltrametric"
  ],
  "imported_by": [
    "TauLib.BookI.Addressability.HingeIntegration"
  ],
  "registry_ids": [
    "I.D14",
    "I.L02"
  ],
  "declaration_counts": {
    "def": 3,
    "theorem": 6
  },
  "declarations": [
    {
      "kind": "def",
      "name": "normalizeSeed",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/normalize-seed/",
      "source_line_start": 63,
      "source_line_end": 70,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "normalize",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/normalize/",
      "source_line_start": 74,
      "source_line_end": 80,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tauEq",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq/",
      "source_line_start": 88,
      "source_line_end": 92,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauEq_refl",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-refl/",
      "source_line_start": 94,
      "source_line_end": 95,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauEq_symm",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-symm/",
      "source_line_start": 97,
      "source_line_end": 98,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauEq_trans",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-trans/",
      "source_line_start": 100,
      "source_line_end": 102,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "address_resolution_theorem",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/address-resolution-theorem/",
      "source_line_start": 117,
      "source_line_end": 120,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_arithmetic_is_address_resolution",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-arithmetic-is-address-resolution/",
      "source_line_start": 137,
      "source_line_end": 143,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tauEq_implies_execNF_eq",
      "url": "/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-implies-exec-nf-eq/",
      "source_line_start": 153,
      "source_line_end": 161,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean",
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
- Source path: [`TauLib/BookI/Addressability/AddressResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/AddressResolution.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Addressability/AddressResolution.lean`
- SHA-256: `c0b13d53f97514f497d4077ce6d7c7ea42b55d7daafe3d9cb282d3a2c18b0a35`

## Registry Links

- `I.D14` — Program Monoid
- `I.L02` — NF-Confluence

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Addressability.OnticUltrametric`

## Imported By

- `TauLib.BookI.Addressability.HingeIntegration`

## Declaration Counts

- `def`: 3
- `theorem`: 6

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [normalizeSeed](/verify/taulib/docs/book-i-addressability-address-resolution/normalize-seed/) | L63-L70 | defined | — |
| `def` | [normalize](/verify/taulib/docs/book-i-addressability-address-resolution/normalize/) | L74-L80 | defined | — |
| `def` | [tauEq](/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq/) | L88-L92 | defined | — |
| `theorem` | [tauEq_refl](/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-refl/) | L94-L95 | formalized | — |
| `theorem` | [tauEq_symm](/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-symm/) | L97-L98 | formalized | — |
| `theorem` | [tauEq_trans](/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-trans/) | L100-L102 | formalized | — |
| `theorem` | [address_resolution_theorem](/verify/taulib/docs/book-i-addressability-address-resolution/address-resolution-theorem/) | L117-L120 | formalized | — |
| `theorem` | [tau_arithmetic_is_address_resolution](/verify/taulib/docs/book-i-addressability-address-resolution/tau-arithmetic-is-address-resolution/) | L137-L143 | formalized | — |
| `theorem` | [tauEq_implies_execNF_eq](/verify/taulib/docs/book-i-addressability-address-resolution/tau-eq-implies-exec-nf-eq/) | L153-L161 | formalized | — |

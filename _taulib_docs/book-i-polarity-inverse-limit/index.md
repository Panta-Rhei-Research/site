---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.InverseLimit",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Polarity.InverseLimit`.",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_slug": "book-i-polarity-inverse-limit",
  "book": "BookI",
  "family": "Polarity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Polarity/InverseLimit.lean",
  "sha256": "bcf9243e2fc4f06f48f107c1a21469cbc41d5e70beca74e19919ce48b96924e8",
  "imports": [
    "TauLib.BookI.Polarity.OmegaGerms"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.DefectInverseSystem",
    "TauLib.BookI.Topos.CircularityResolution"
  ],
  "registry_ids": [
    "I.D25",
    "I.D29"
  ],
  "declaration_counts": {
    "structure": 1,
    "def": 3,
    "theorem": 8
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "OmegaInverseLimit",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/omega-inverse-limit/",
      "source_line_start": 85,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "nat_to_inverse_limit",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit/",
      "source_line_start": 99,
      "source_line_end": 108,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "coeff_list",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list/",
      "source_line_start": 118,
      "source_line_end": 120,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "coeff_list_length",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list-length/",
      "source_line_start": 122,
      "source_line_end": 126,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "getD_eq_getElem'",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/get-d-eq-get-elem/",
      "source_line_start": 128,
      "source_line_end": 130,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "coeff_list_getD",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list-get-d/",
      "source_line_start": 132,
      "source_line_end": 150,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "OmegaInverseLimit.truncate",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/truncate/",
      "source_line_start": 154,
      "source_line_end": 156,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "OmegaInverseLimit.truncate_getD",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/truncate-get-d/",
      "source_line_start": 159,
      "source_line_end": 162,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "truncate_compat",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/truncate-compat/",
      "source_line_start": 171,
      "source_line_end": 184,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_to_inverse_limit_truncate_components",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit-truncate-components/",
      "source_line_start": 193,
      "source_line_end": 199,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "OmegaInverseLimit.ext",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/ext/",
      "source_line_start": 208,
      "source_line_end": 215,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "nat_to_inverse_limit_inj_componentwise",
      "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit-inj-componentwise/",
      "source_line_start": 226,
      "source_line_end": 233,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean",
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
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Polarity/InverseLimit.lean`
- SHA-256: `bcf9243e2fc4f06f48f107c1a21469cbc41d5e70beca74e19919ce48b96924e8`

## Registry Links

- `I.D25` — Omega-Tail (Compatible Tower)
- `I.D29` — CRT Decomposition

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.OmegaGerms`

## Imported By

- `TauLib.BookI.Boundary.DefectInverseSystem`
- `TauLib.BookI.Topos.CircularityResolution`

## Declaration Counts

- `def`: 3
- `structure`: 1
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [OmegaInverseLimit](/verify/taulib/docs/book-i-polarity-inverse-limit/omega-inverse-limit/) | L85-L91 | defined | — |
| `def` | [nat_to_inverse_limit](/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit/) | L99-L108 | defined | — |
| `def` | [coeff_list](/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list/) | L118-L120 | defined | — |
| `theorem` | [coeff_list_length](/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list-length/) | L122-L126 | formalized | — |
| `theorem` | [getD_eq_getElem'](/verify/taulib/docs/book-i-polarity-inverse-limit/get-d-eq-get-elem/) | L128-L130 | formalized | — |
| `theorem` | [coeff_list_getD](/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list-get-d/) | L132-L150 | formalized | — |
| `def` | [OmegaInverseLimit.truncate](/verify/taulib/docs/book-i-polarity-inverse-limit/truncate/) | L154-L156 | defined | — |
| `theorem` | [OmegaInverseLimit.truncate_getD](/verify/taulib/docs/book-i-polarity-inverse-limit/truncate-get-d/) | L159-L162 | formalized | — |
| `theorem` | [truncate_compat](/verify/taulib/docs/book-i-polarity-inverse-limit/truncate-compat/) | L171-L184 | formalized | — |
| `theorem` | [nat_to_inverse_limit_truncate_components](/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit-truncate-components/) | L193-L199 | formalized | — |
| `theorem` | [OmegaInverseLimit.ext](/verify/taulib/docs/book-i-polarity-inverse-limit/ext/) | L208-L215 | formalized | — |
| `theorem` | [nat_to_inverse_limit_inj_componentwise](/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit-inj-componentwise/) | L226-L233 | formalized | — |

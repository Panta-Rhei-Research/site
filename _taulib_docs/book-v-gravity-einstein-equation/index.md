---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Gravity.EinsteinEquation",
  "permalink": "/verify/taulib/docs/book-v-gravity-einstein-equation/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Gravity.EinsteinEquation`.",
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_slug": "book-v-gravity-einstein-equation",
  "book": "BookV",
  "family": "Gravity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Gravity/EinsteinEquation.lean",
  "sha256": "0d3f83b9b3dbff4e31319ac352478c84ac28eae84b761122d731b2378b2c1564",
  "imports": [
    "TauLib.BookV.Gravity.GravitationalConstant",
    "TauLib.BookIV.Sectors.CouplingFormulas"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Gravity.Schwarzschild",
    "TauLib.BookV.GravityField.FrameHolonomy"
  ],
  "registry_ids": [
    "V.D03",
    "V.D04",
    "V.D05",
    "V.D06",
    "V.R01",
    "V.T02"
  ],
  "declaration_counts": {
    "structure": 5,
    "def": 5,
    "theorem": 6,
    "eval": 2
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "MatterCharacter",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/matter-character/",
      "source_line_start": 86,
      "source_line_end": 97,
      "formal_status": "defined",
      "registry_ids": [
        "V.D03"
      ]
    },
    {
      "kind": "def",
      "name": "MatterCharacter.total_numer",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/total-numer/",
      "source_line_start": 100,
      "source_line_end": 101,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "MatterCharacter.totalFloat",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/total-float/",
      "source_line_start": 104,
      "source_line_end": 105,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CurvatureCharacter",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/curvature-character/",
      "source_line_start": 119,
      "source_line_end": 126,
      "formal_status": "defined",
      "registry_ids": [
        "V.D04"
      ]
    },
    {
      "kind": "def",
      "name": "CurvatureCharacter.toFloat",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/to-float/",
      "source_line_start": 129,
      "source_line_end": 130,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GRCoupling",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/grcoupling/",
      "source_line_start": 147,
      "source_line_end": 158,
      "formal_status": "defined",
      "registry_ids": [
        "V.D05"
      ]
    },
    {
      "kind": "def",
      "name": "GRCoupling.toFloat",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/to-float-l161/",
      "source_line_start": 161,
      "source_line_end": 162,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "canonical_gr_coupling",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/canonical-gr-coupling/",
      "source_line_start": 170,
      "source_line_end": 173,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauEinstein",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/tau-einstein/",
      "source_line_start": 194,
      "source_line_end": 205,
      "formal_status": "defined",
      "registry_ids": [
        "V.D06"
      ]
    },
    {
      "kind": "structure",
      "name": "TauBianchi",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/tau-bianchi/",
      "source_line_start": 221,
      "source_line_end": 226,
      "formal_status": "defined",
      "registry_ids": [
        "V.R01"
      ]
    },
    {
      "kind": "theorem",
      "name": "kappa_unique",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/kappa-unique/",
      "source_line_start": 234,
      "source_line_end": 235,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T02"
      ]
    },
    {
      "kind": "theorem",
      "name": "kappa_sigma_fixed",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/kappa-sigma-fixed/",
      "source_line_start": 238,
      "source_line_end": 239,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "kappa_is_unique",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/kappa-is-unique/",
      "source_line_start": 242,
      "source_line_end": 243,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "matter_three_sectors",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/matter-three-sectors/",
      "source_line_start": 248,
      "source_line_end": 249,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "canonical_coupling_value",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/canonical-coupling-value/",
      "source_line_start": 252,
      "source_line_end": 255,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bianchi_is_derived",
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/bianchi-is-derived/",
      "source_line_start": 258,
      "source_line_end": 259,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/eval-l269/",
      "source_line_start": 269,
      "source_line_end": 272,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean",
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
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Gravity/EinsteinEquation.lean`
- SHA-256: `0d3f83b9b3dbff4e31319ac352478c84ac28eae84b761122d731b2378b2c1564`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Gravity.GravitationalConstant`
- `TauLib.BookIV.Sectors.CouplingFormulas`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Gravity.Schwarzschild`
- `TauLib.BookV.GravityField.FrameHolonomy`

## Declaration Counts

- `def`: 5
- `eval`: 2
- `structure`: 5
- `theorem`: 6

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [MatterCharacter](/verify/taulib/docs/book-v-gravity-einstein-equation/matter-character/) | L86-L97 | defined | `V.D03` |
| `def` | [MatterCharacter.total_numer](/verify/taulib/docs/book-v-gravity-einstein-equation/total-numer/) | L100-L101 | defined | — |
| `def` | [MatterCharacter.totalFloat](/verify/taulib/docs/book-v-gravity-einstein-equation/total-float/) | L104-L105 | defined | — |
| `structure` | [CurvatureCharacter](/verify/taulib/docs/book-v-gravity-einstein-equation/curvature-character/) | L119-L126 | defined | `V.D04` |
| `def` | [CurvatureCharacter.toFloat](/verify/taulib/docs/book-v-gravity-einstein-equation/to-float/) | L129-L130 | defined | — |
| `structure` | [GRCoupling](/verify/taulib/docs/book-v-gravity-einstein-equation/grcoupling/) | L147-L158 | defined | `V.D05` |
| `def` | [GRCoupling.toFloat](/verify/taulib/docs/book-v-gravity-einstein-equation/to-float-l161/) | L161-L162 | defined | — |
| `def` | [canonical_gr_coupling](/verify/taulib/docs/book-v-gravity-einstein-equation/canonical-gr-coupling/) | L170-L173 | defined | — |
| `structure` | [TauEinstein](/verify/taulib/docs/book-v-gravity-einstein-equation/tau-einstein/) | L194-L205 | defined | `V.D06` |
| `structure` | [TauBianchi](/verify/taulib/docs/book-v-gravity-einstein-equation/tau-bianchi/) | L221-L226 | defined | `V.R01` |
| `theorem` | [kappa_unique](/verify/taulib/docs/book-v-gravity-einstein-equation/kappa-unique/) | L234-L235 | formalized | `V.T02` |
| `theorem` | [kappa_sigma_fixed](/verify/taulib/docs/book-v-gravity-einstein-equation/kappa-sigma-fixed/) | L238-L239 | formalized | — |
| `theorem` | [kappa_is_unique](/verify/taulib/docs/book-v-gravity-einstein-equation/kappa-is-unique/) | L242-L243 | formalized | — |
| `theorem` | [matter_three_sectors](/verify/taulib/docs/book-v-gravity-einstein-equation/matter-three-sectors/) | L248-L249 | formalized | — |
| `theorem` | [canonical_coupling_value](/verify/taulib/docs/book-v-gravity-einstein-equation/canonical-coupling-value/) | L252-L255 | formalized | — |
| `theorem` | [bianchi_is_derived](/verify/taulib/docs/book-v-gravity-einstein-equation/bianchi-is-derived/) | L258-L259 | formalized | — |
| `eval` | [#eval L266](/verify/taulib/docs/book-v-gravity-einstein-equation/eval-l266/) | L266-L266 | computed | — |
| `eval` | [#eval L269](/verify/taulib/docs/book-v-gravity-einstein-equation/eval-l269/) | L269-L272 | computed | — |

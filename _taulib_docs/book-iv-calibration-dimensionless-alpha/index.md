---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "permalink": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.DimensionlessAlpha`.",
  "module_name": "TauLib.BookIV.Calibration.DimensionlessAlpha",
  "module_slug": "book-iv-calibration-dimensionless-alpha",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/DimensionlessAlpha.lean",
  "sha256": "fe0edec3f0825dbcab4121f4cfea8687513f302c47b48a428e0c0a808c6adb8b",
  "imports": [
    "TauLib.BookIV.Sectors.FineStructure",
    "TauLib.BookIV.Physics.HolonomyCorrection"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Electroweak.PhotonMode"
  ],
  "registry_ids": [
    "IV.D286",
    "IV.D287",
    "IV.D288",
    "IV.R255",
    "IV.R256",
    "IV.R257",
    "IV.R258",
    "IV.R260",
    "IV.T107"
  ],
  "declaration_counts": {
    "theorem": 2,
    "structure": 2,
    "def": 2,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "theorem",
      "name": "alpha_spec_range",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/alpha-spec-range/",
      "source_line_start": 41,
      "source_line_end": 44,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RelationalUnits",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/relational-units/",
      "source_line_start": 60,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D287"
      ]
    },
    {
      "kind": "def",
      "name": "relational_units",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/relational-units-l76/",
      "source_line_start": 76,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "holonomy_formula_ch11",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/holonomy-formula-ch11/",
      "source_line_start": 95,
      "source_line_end": 102,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T107"
      ]
    },
    {
      "kind": "structure",
      "name": "CorrectionFactor",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/correction-factor/",
      "source_line_start": 118,
      "source_line_end": 126,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D288"
      ]
    },
    {
      "kind": "def",
      "name": "correction_factor",
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/correction-factor-l129/",
      "source_line_start": 129,
      "source_line_end": 134,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l143/",
      "source_line_start": 143,
      "source_line_end": 143,
      "formal_status": "computed",
      "registry_ids": [
        "IV.R260"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l144/",
      "source_line_start": 144,
      "source_line_end": 144,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l145/",
      "source_line_start": 145,
      "source_line_end": 145,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l146/",
      "source_line_start": 146,
      "source_line_end": 148,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionlessAlpha.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionlessAlpha.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/DimensionlessAlpha.lean`
- SHA-256: `fe0edec3f0825dbcab4121f4cfea8687513f302c47b48a428e0c0a808c6adb8b`

## Registry Links

- `IV.D286` — Spectral Fine-Structure Formula
- `IV.D287` — Five Relational Units
- `IV.D288` — Holonomy Correction Factor
- `IV.R255` — The meaning of 0.6%
- `IV.R256` — Lean verification
- `IV.R257` — Origin of the formula
- `IV.R258` — The three holonomy circles
- `IV.R260` — The value of being wrong
- `IV.T107` — Holonomy Fine-Structure Formula

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Sectors.FineStructure`
- `TauLib.BookIV.Physics.HolonomyCorrection`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Electroweak.PhotonMode`

## Declaration Counts

- `def`: 2
- `eval`: 4
- `structure`: 2
- `theorem`: 2

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `theorem` | [alpha_spec_range](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/alpha-spec-range/) | L41-L44 | formalized | — |
| `structure` | [RelationalUnits](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/relational-units/) | L60-L73 | defined | `IV.D287` |
| `def` | [relational_units](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/relational-units-l76/) | L76-L84 | defined | — |
| `theorem` | [holonomy_formula_ch11](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/holonomy-formula-ch11/) | L95-L102 | formalized | `IV.T107` |
| `structure` | [CorrectionFactor](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/correction-factor/) | L118-L126 | defined | `IV.D288` |
| `def` | [correction_factor](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/correction-factor-l129/) | L129-L134 | defined | — |
| `eval` | [#eval L143](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l143/) | L143-L143 | computed | `IV.R260` |
| `eval` | [#eval L144](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l144/) | L144-L144 | computed | — |
| `eval` | [#eval L145](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l145/) | L145-L145 | computed | — |
| `eval` | [#eval L146](/verify/taulib/docs/book-iv-calibration-dimensionless-alpha/eval-l146/) | L146-L148 | computed | — |

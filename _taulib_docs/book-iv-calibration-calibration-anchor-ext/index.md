---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.CalibrationAnchorExt`.",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchorExt",
  "module_slug": "book-iv-calibration-calibration-anchor-ext",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean",
  "sha256": "819ea08fb6ebc31e6550d9635f46763fcbe560c2dc205724b7f1a5aff772e777",
  "imports": [
    "TauLib.BookIV.Calibration.CalibrationAnchor"
  ],
  "imported_by": [
    "TauLib.BookIV"
  ],
  "registry_ids": [
    "IV.D289",
    "IV.D290",
    "IV.D291",
    "IV.D292",
    "IV.P166",
    "IV.R262",
    "IV.R263",
    "IV.R264",
    "IV.R265",
    "IV.R266",
    "IV.R267",
    "IV.T108",
    "IV.T109",
    "IV.T110",
    "IV.T111"
  ],
  "declaration_counts": {
    "structure": 8,
    "def": 9,
    "theorem": 14,
    "inductive": 1,
    "eval": 12
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "RelationalUnit",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/relational-unit/",
      "source_line_start": 70,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D289"
      ]
    },
    {
      "kind": "def",
      "name": "five_relational_units",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/five-relational-units/",
      "source_line_start": 87,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_relational_units_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/five-relational-units-count/",
      "source_line_start": 96,
      "source_line_end": 96,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "CollapseStatus",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/collapse-status/",
      "source_line_start": 103,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CollapsedUnit",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/collapsed-unit/",
      "source_line_start": 110,
      "source_line_end": 115,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "collapsed_units",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/collapsed-units/",
      "source_line_start": 118,
      "source_line_end": 124,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_collapse_five_to_one",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-collapse-five-to-one/",
      "source_line_start": 130,
      "source_line_end": 138,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T108"
      ]
    },
    {
      "kind": "structure",
      "name": "Level0FormulaSummary",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-formula-summary/",
      "source_line_start": 150,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T109"
      ]
    },
    {
      "kind": "def",
      "name": "level0_summary",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-summary/",
      "source_line_start": 166,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "level0_bulk_exp",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-bulk-exp/",
      "source_line_start": 175,
      "source_line_end": 175,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "level0_range_valid",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-range-valid/",
      "source_line_start": 178,
      "source_line_end": 182,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "Level1PlusFormulaSummary",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1-plus-formula-summary/",
      "source_line_start": 194,
      "source_line_end": 207,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T110"
      ]
    },
    {
      "kind": "def",
      "name": "level1plus_summary",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-summary/",
      "source_line_start": 210,
      "source_line_end": 216,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "level1plus_ppm_sub_100",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-ppm-sub-100/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "level1plus_three_circles",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-three-circles/",
      "source_line_start": 223,
      "source_line_end": 224,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "level1plus_second_order",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-second-order/",
      "source_line_start": 227,
      "source_line_end": 228,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "UnpolarizedDefectBundle",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/unpolarized-defect-bundle/",
      "source_line_start": 241,
      "source_line_end": 248,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D290"
      ]
    },
    {
      "kind": "def",
      "name": "is_unpolarized",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/is-unpolarized/",
      "source_line_start": 251,
      "source_line_end": 252,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "unpolarized_bundle",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/unpolarized-bundle/",
      "source_line_start": 255,
      "source_line_end": 255,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "unpolarized_bundle_is_unpolarized",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/unpolarized-bundle-is-unpolarized/",
      "source_line_start": 258,
      "source_line_end": 259,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutronMinimality",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimality/",
      "source_line_start": 272,
      "source_line_end": 281,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.P166"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_minimal",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimal/",
      "source_line_start": 284,
      "source_line_end": 288,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutron_minimality",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimality-l291/",
      "source_line_start": 291,
      "source_line_end": 295,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P166"
      ]
    },
    {
      "kind": "structure",
      "name": "CalibrationAnchorExt",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/calibration-anchor-ext/",
      "source_line_start": 305,
      "source_line_end": 316,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D291"
      ]
    },
    {
      "kind": "def",
      "name": "anchor_ext",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/anchor-ext/",
      "source_line_start": 319,
      "source_line_end": 324,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "anchor_ext_positive",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/anchor-ext-positive/",
      "source_line_start": 327,
      "source_line_end": 328,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "anchor_ext_precise",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/anchor-ext-precise/",
      "source_line_start": 331,
      "source_line_end": 332,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "parameter_count_ext",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/parameter-count-ext/",
      "source_line_start": 343,
      "source_line_end": 348,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T111"
      ]
    },
    {
      "kind": "structure",
      "name": "TauToSIConversionExt",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-to-siconversion-ext/",
      "source_line_start": 359,
      "source_line_end": 368,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D292"
      ]
    },
    {
      "kind": "def",
      "name": "tau_to_si_ext",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-to-si-ext/",
      "source_line_start": 371,
      "source_line_end": 375,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "conversion_single_anchor",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/conversion-single-anchor/",
      "source_line_start": 378,
      "source_line_end": 379,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "conversion_ratios_determined",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/conversion-ratios-determined/",
      "source_line_start": 382,
      "source_line_end": 383,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l420/",
      "source_line_start": 420,
      "source_line_end": 420,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "IV.R262",
        "IV.R263",
        "IV.R264",
        "IV.R265",
        "IV.R266",
        "IV.R267"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l423/",
      "source_line_start": 423,
      "source_line_end": 423,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l424/",
      "source_line_start": 424,
      "source_line_end": 424,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l427/",
      "source_line_start": 427,
      "source_line_end": 427,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l428/",
      "source_line_start": 428,
      "source_line_end": 428,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l431/",
      "source_line_start": 431,
      "source_line_end": 431,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l432/",
      "source_line_start": 432,
      "source_line_end": 432,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l435/",
      "source_line_start": 435,
      "source_line_end": 435,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l438/",
      "source_line_start": 438,
      "source_line_end": 438,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l441/",
      "source_line_start": 441,
      "source_line_end": 441,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l442/",
      "source_line_start": 442,
      "source_line_end": 442,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l445/",
      "source_line_start": 445,
      "source_line_end": 447,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/CalibrationAnchorExt.lean`
- SHA-256: `819ea08fb6ebc31e6550d9635f46763fcbe560c2dc205724b7f1a5aff772e777`

## Registry Links

- `IV.D289` — Five Relational Units
- `IV.D290` — Unpolarized defect bundle
- `IV.D291` — Calibration Anchor
- `IV.D292` — tau-to-SI conversion
- `IV.P166` — Neutron Minimality
- `IV.R262` — What the paper got right
- `IV.R263` — Not a numerical fit
- `IV.R264` — The Planck mass in tau-physics
- `IV.R265` — One input, not zero
- `IV.R266` — Lean formalization
- `IV.R267` — Falsifiability
- `IV.T108` — tau-Collapse: Five to One
- `IV.T109` — Level~0 mass ratio formula
- `IV.T110` — Level~1+ mass ratio formula
- `IV.T111` — Parameter Count

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Calibration.CalibrationAnchor`

## Imported By

- `TauLib.BookIV`

## Declaration Counts

- `def`: 9
- `eval`: 12
- `inductive`: 1
- `structure`: 8
- `theorem`: 14

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [RelationalUnit](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/relational-unit/) | L70-L81 | type/data schema | type/data schema | `IV.D289` |
| `def` | [five_relational_units](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/five-relational-units/) | L87-L93 | data/computed value | data/computed value | — |
| `theorem` | [five_relational_units_count](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/five-relational-units-count/) | L96-L96 | proof obligation | formal proof obligation checked | — |
| `inductive` | [CollapseStatus](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/collapse-status/) | L103-L107 | type/data schema | type/data schema | — |
| `structure` | [CollapsedUnit](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/collapsed-unit/) | L110-L115 | type/data schema | type/data schema | — |
| `def` | [collapsed_units](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/collapsed-units/) | L118-L124 | data/computed value | data/computed value | — |
| `theorem` | [tau_collapse_five_to_one](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-collapse-five-to-one/) | L130-L138 | proof obligation | formal proof obligation checked | `IV.T108` |
| `structure` | [Level0FormulaSummary](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-formula-summary/) | L150-L163 | type/data schema | type/data schema | `IV.T109` |
| `def` | [level0_summary](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-summary/) | L166-L172 | definition | definition | — |
| `theorem` | [level0_bulk_exp](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-bulk-exp/) | L175-L175 | proof obligation | formal proof obligation checked | — |
| `theorem` | [level0_range_valid](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level0-range-valid/) | L178-L182 | proof obligation | formal proof obligation checked | — |
| `structure` | [Level1PlusFormulaSummary](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1-plus-formula-summary/) | L194-L207 | type/data schema | type/data schema | `IV.T110` |
| `def` | [level1plus_summary](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-summary/) | L210-L216 | definition | definition | — |
| `theorem` | [level1plus_ppm_sub_100](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-ppm-sub-100/) | L219-L220 | proof obligation | formal proof obligation checked | — |
| `theorem` | [level1plus_three_circles](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-three-circles/) | L223-L224 | proof obligation | formal proof obligation checked | — |
| `theorem` | [level1plus_second_order](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/level1plus-second-order/) | L227-L228 | proof obligation | formal proof obligation checked | — |
| `structure` | [UnpolarizedDefectBundle](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/unpolarized-defect-bundle/) | L241-L248 | type/data schema | type/data schema | `IV.D290` |
| `def` | [is_unpolarized](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/is-unpolarized/) | L251-L252 | data/computed value | data/computed value | — |
| `def` | [unpolarized_bundle](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/unpolarized-bundle/) | L255-L255 | definition | definition | — |
| `theorem` | [unpolarized_bundle_is_unpolarized](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/unpolarized-bundle-is-unpolarized/) | L258-L259 | proof obligation | formal proof obligation checked | — |
| `structure` | [NeutronMinimality](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimality/) | L272-L281 | type/data schema | type/data schema | `IV.P166` |
| `def` | [neutron_minimal](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimal/) | L284-L288 | definition | definition | — |
| `theorem` | [neutron_minimality](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/neutron-minimality-l291/) | L291-L295 | proof obligation | formal proof obligation checked | `IV.P166` |
| `structure` | [CalibrationAnchorExt](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/calibration-anchor-ext/) | L305-L316 | type/data schema | type/data schema | `IV.D291` |
| `def` | [anchor_ext](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/anchor-ext/) | L319-L324 | definition | definition | — |
| `theorem` | [anchor_ext_positive](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/anchor-ext-positive/) | L327-L328 | proof obligation | formal proof obligation checked | — |
| `theorem` | [anchor_ext_precise](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/anchor-ext-precise/) | L331-L332 | proof obligation | formal proof obligation checked | — |
| `theorem` | [parameter_count_ext](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/parameter-count-ext/) | L343-L348 | proof obligation | formal proof obligation checked | `IV.T111` |
| `structure` | [TauToSIConversionExt](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-to-siconversion-ext/) | L359-L368 | type/data schema | type/data schema | `IV.D292` |
| `def` | [tau_to_si_ext](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/tau-to-si-ext/) | L371-L375 | definition | definition | — |
| `theorem` | [conversion_single_anchor](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/conversion-single-anchor/) | L378-L379 | proof obligation | formal proof obligation checked | — |
| `theorem` | [conversion_ratios_determined](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/conversion-ratios-determined/) | L382-L383 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L420](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l420/) | L420-L420 | computed check | computed check | `IV.R262`, `IV.R263`, `IV.R264`, `IV.R265`, `IV.R266`, `IV.R267` |
| `eval` | [#eval L423](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l423/) | L423-L423 | computed check | computed check | — |
| `eval` | [#eval L424](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l424/) | L424-L424 | computed check | computed check | — |
| `eval` | [#eval L427](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l427/) | L427-L427 | computed check | computed check | — |
| `eval` | [#eval L428](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l428/) | L428-L428 | computed check | computed check | — |
| `eval` | [#eval L431](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l431/) | L431-L431 | computed check | computed check | — |
| `eval` | [#eval L432](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l432/) | L432-L432 | computed check | computed check | — |
| `eval` | [#eval L435](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l435/) | L435-L435 | computed check | computed check | — |
| `eval` | [#eval L438](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l438/) | L438-L438 | computed check | computed check | — |
| `eval` | [#eval L441](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l441/) | L441-L441 | computed check | computed check | — |
| `eval` | [#eval L442](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l442/) | L442-L442 | computed check | computed check | — |
| `eval` | [#eval L445](/corpus/taulib/docs/book-iv-calibration-calibration-anchor-ext/eval-l445/) | L445-L447 | computed check | computed check | — |

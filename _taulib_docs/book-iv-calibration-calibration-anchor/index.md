---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.CalibrationAnchor`.",
  "module_name": "TauLib.BookIV.Calibration.CalibrationAnchor",
  "module_slug": "book-iv-calibration-calibration-anchor",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/CalibrationAnchor.lean",
  "sha256": "3baf56728d6f5c15791545ab545bc4165adb45baaa5456ce0fa5ac0c0915d279",
  "imports": [
    "TauLib.BookIV.Physics.MassEnergy",
    "TauLib.BookIV.Calibration.SIReference"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.CalibrationAnchorExt",
    "TauLib.BookIV.Calibration.DimensionalBridge",
    "TauLib.Tour.GuidedTour.BookIV"
  ],
  "registry_ids": [
    "IV.D30",
    "IV.D31",
    "IV.R07",
    "IV.T05",
    "IV.T06"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 4,
    "theorem": 7,
    "inductive": 2,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "CalibrationAnchor",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/calibration-anchor/",
      "source_line_start": 64,
      "source_line_end": 75,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D30"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_anchor",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/neutron-anchor/",
      "source_line_start": 78,
      "source_line_end": 83,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "anchor_matches_si",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/anchor-matches-si/",
      "source_line_start": 86,
      "source_line_end": 89,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauToSIConversion",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/tau-to-siconversion/",
      "source_line_start": 102,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D31"
      ]
    },
    {
      "kind": "def",
      "name": "lambda_mass",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/lambda-mass/",
      "source_line_start": 116,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DimensionalFactorization",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/dimensional-factorization/",
      "source_line_start": 130,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "parameter_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/parameter-count/",
      "source_line_start": 146,
      "source_line_end": 151,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T05"
      ]
    },
    {
      "kind": "inductive",
      "name": "RelationalStatus",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/relational-status/",
      "source_line_start": 158,
      "source_line_end": 162,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RelationalQuantity",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/relational-quantity/",
      "source_line_start": 165,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "relational_quantities",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/relational-quantities/",
      "source_line_start": 175,
      "source_line_end": 181,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_collapse",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/tau-collapse/",
      "source_line_start": 186,
      "source_line_end": 190,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T06"
      ]
    },
    {
      "kind": "inductive",
      "name": "OntologicalPriority",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/ontological-priority/",
      "source_line_start": 205,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R07"
      ]
    },
    {
      "kind": "def",
      "name": "OntologicalPriority.toNat",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/to-nat/",
      "source_line_start": 213,
      "source_line_end": 217,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutron_first",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/neutron-first/",
      "source_line_start": 220,
      "source_line_end": 224,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "priority_levels",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/priority-levels/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "anchor_positive",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/anchor-positive/",
      "source_line_start": 234,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "anchor_much_heavier_than_electron",
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/anchor-much-heavier-than-electron/",
      "source_line_start": 240,
      "source_line_end": 243,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l256/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l257/",
      "source_line_start": 257,
      "source_line_end": 259,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean",
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
- Source path: [`TauLib/BookIV/Calibration/CalibrationAnchor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/CalibrationAnchor.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/CalibrationAnchor.lean`
- SHA-256: `3baf56728d6f5c15791545ab545bc4165adb45baaa5456ce0fa5ac0c0915d279`

## Registry Links

- `IV.D30` — Calibration Anchor
- `IV.D31` — τ-to-SI Conversion
- `IV.R07` — Ontological Priority
- `IV.T05` — Parameter Count
- `IV.T06` — τ-Collapse (5→1)

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.MassEnergy`
- `TauLib.BookIV.Calibration.SIReference`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.CalibrationAnchorExt`
- `TauLib.BookIV.Calibration.DimensionalBridge`
- `TauLib.Tour.GuidedTour.BookIV`

## Declaration Counts

- `def`: 4
- `eval`: 4
- `inductive`: 2
- `structure`: 4
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [CalibrationAnchor](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/calibration-anchor/) | L64-L75 | type/data schema | type/data schema | `IV.D30` |
| `def` | [neutron_anchor](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/neutron-anchor/) | L78-L83 | definition | definition | — |
| `theorem` | [anchor_matches_si](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/anchor-matches-si/) | L86-L89 | proof obligation | formal proof obligation checked | — |
| `structure` | [TauToSIConversion](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/tau-to-siconversion/) | L102-L113 | type/data schema | type/data schema | `IV.D31` |
| `def` | [lambda_mass](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/lambda-mass/) | L116-L121 | definition | definition | — |
| `structure` | [DimensionalFactorization](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/dimensional-factorization/) | L130-L141 | type/data schema | type/data schema | — |
| `theorem` | [parameter_count](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/parameter-count/) | L146-L151 | proof obligation | formal proof obligation checked | `IV.T05` |
| `inductive` | [RelationalStatus](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/relational-status/) | L158-L162 | type/data schema | type/data schema | — |
| `structure` | [RelationalQuantity](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/relational-quantity/) | L165-L172 | type/data schema | type/data schema | — |
| `def` | [relational_quantities](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/relational-quantities/) | L175-L181 | data/computed value | data/computed value | — |
| `theorem` | [tau_collapse](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/tau-collapse/) | L186-L190 | proof obligation | formal proof obligation checked | `IV.T06` |
| `inductive` | [OntologicalPriority](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/ontological-priority/) | L205-L210 | type/data schema | type/data schema | `IV.R07` |
| `def` | [OntologicalPriority.toNat](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/to-nat/) | L213-L217 | definition | definition | — |
| `theorem` | [neutron_first](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/neutron-first/) | L220-L224 | proof obligation | formal proof obligation checked | — |
| `theorem` | [priority_levels](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/priority-levels/) | L227-L227 | proof obligation | formal proof obligation checked | — |
| `theorem` | [anchor_positive](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/anchor-positive/) | L234-L236 | proof obligation | formal proof obligation checked | — |
| `theorem` | [anchor_much_heavier_than_electron](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/anchor-much-heavier-than-electron/) | L240-L243 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L250](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l250/) | L250-L250 | computed check | computed check | — |
| `eval` | [#eval L253](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l253/) | L253-L253 | computed check | computed check | — |
| `eval` | [#eval L256](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l256/) | L256-L256 | computed check | computed check | — |
| `eval` | [#eval L257](/corpus/taulib/docs/book-iv-calibration-calibration-anchor/eval-l257/) | L257-L259 | computed check | computed check | — |

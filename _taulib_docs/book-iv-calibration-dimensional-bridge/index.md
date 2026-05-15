---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Calibration.DimensionalBridge",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Calibration.DimensionalBridge`.",
  "module_name": "TauLib.BookIV.Calibration.DimensionalBridge",
  "module_slug": "book-iv-calibration-dimensional-bridge",
  "book": "BookIV",
  "family": "Calibration",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Calibration/DimensionalBridge.lean",
  "sha256": "bfcd3402bf3ca59b43e41090abd087cc186a13b669e722629f77c4c6993857c6",
  "imports": [
    "TauLib.BookIV.Calibration.CalibrationAnchor"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.ConstantsLedger",
    "TauLib.BookIV.Calibration.DimensionalBridgeExt"
  ],
  "registry_ids": [
    "IV.D32",
    "IV.D33",
    "IV.D34",
    "IV.D35",
    "IV.D36",
    "IV.D37",
    "IV.R08",
    "IV.T07",
    "IV.T08"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 11,
    "theorem": 12,
    "inductive": 1,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "DimExponents",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/dim-exponents/",
      "source_line_start": 64,
      "source_line_end": 69,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D32"
      ]
    },
    {
      "kind": "def",
      "name": "DimExponents.add",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/add/",
      "source_line_start": 72,
      "source_line_end": 73,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "DimExponents.scale",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/scale/",
      "source_line_start": 76,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "DimExponents.zero",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/zero/",
      "source_line_start": 80,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DimensionalFormula",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/dimensional-formula/",
      "source_line_start": 89,
      "source_line_end": 102,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "c_formula",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/c-formula/",
      "source_line_start": 110,
      "source_line_end": 116,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D33"
      ]
    },
    {
      "kind": "def",
      "name": "h_formula",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/h-formula/",
      "source_line_start": 120,
      "source_line_end": 126,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D34"
      ]
    },
    {
      "kind": "def",
      "name": "ke_formula",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/ke-formula/",
      "source_line_start": 130,
      "source_line_end": 136,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D35"
      ]
    },
    {
      "kind": "def",
      "name": "eps0_formula",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eps0-formula/",
      "source_line_start": 140,
      "source_line_end": 146,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D36"
      ]
    },
    {
      "kind": "def",
      "name": "mu0_formula",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/mu0-formula/",
      "source_line_start": 150,
      "source_line_end": 156,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D37"
      ]
    },
    {
      "kind": "def",
      "name": "derivation_chain",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/derivation-chain/",
      "source_line_start": 159,
      "source_line_end": 160,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "derivation_chain_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/derivation-chain-count/",
      "source_line_start": 163,
      "source_line_end": 163,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "maxwell_dimensional",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-dimensional/",
      "source_line_start": 172,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T07"
      ]
    },
    {
      "kind": "theorem",
      "name": "maxwell_prefactor",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-prefactor/",
      "source_line_start": 182,
      "source_line_end": 186,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T07"
      ]
    },
    {
      "kind": "theorem",
      "name": "maxwell_complete",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-complete/",
      "source_line_start": 191,
      "source_line_end": 200,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "coulomb_permittivity_dimensional",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/coulomb-permittivity-dimensional/",
      "source_line_start": 209,
      "source_line_end": 211,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T08"
      ]
    },
    {
      "kind": "theorem",
      "name": "coulomb_permittivity_prefactor",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/coulomb-permittivity-prefactor/",
      "source_line_start": 223,
      "source_line_end": 227,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T08"
      ]
    },
    {
      "kind": "inductive",
      "name": "SITier",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/sitier/",
      "source_line_start": 234,
      "source_line_end": 238,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TieredConstant",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/tiered-constant/",
      "source_line_start": 241,
      "source_line_end": 244,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tiered_exact_constants",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/tiered-exact-constants/",
      "source_line_start": 247,
      "source_line_end": 252,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tiered_count",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/tiered-count/",
      "source_line_start": 255,
      "source_line_end": 257,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GravityFrontier",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/gravity-frontier/",
      "source_line_start": 270,
      "source_line_end": 279,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R08"
      ]
    },
    {
      "kind": "def",
      "name": "gravity_frontier",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/gravity-frontier-l282/",
      "source_line_start": 282,
      "source_line_end": 282,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "g_is_deferred",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/g-is-deferred/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "c_is_velocity",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/c-is-velocity/",
      "source_line_start": 292,
      "source_line_end": 293,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "h_is_action",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/h-is-action/",
      "source_line_start": 296,
      "source_line_end": 297,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "eps0_mu0_inverse",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eps0-mu0-inverse/",
      "source_line_start": 300,
      "source_line_end": 303,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ke_eps0_inverse",
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/ke-eps0-inverse/",
      "source_line_start": 306,
      "source_line_end": 309,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 316,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l321/",
      "source_line_start": 321,
      "source_line_end": 321,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l322/",
      "source_line_start": 322,
      "source_line_end": 322,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l326/",
      "source_line_start": 326,
      "source_line_end": 326,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l329/",
      "source_line_start": 329,
      "source_line_end": 331,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean",
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
- Source path: [`TauLib/BookIV/Calibration/DimensionalBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/DimensionalBridge.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Calibration/DimensionalBridge.lean`
- SHA-256: `bfcd3402bf3ca59b43e41090abd087cc186a13b669e722629f77c4c6993857c6`

## Registry Links

- `IV.D32` — Tau Physical Scale
- `IV.D33` — Speed of Light
- `IV.D34` — Planck Constant
- `IV.D35` — Coulomb Constant
- `IV.D36` — Vacuum Permittivity
- `IV.D37` — Vacuum Permeability
- `IV.R08` — G Frontier
- `IV.T07` — Maxwell Relation
- `IV.T08` — Coulomb-Permittivity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Calibration.CalibrationAnchor`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.ConstantsLedger`
- `TauLib.BookIV.Calibration.DimensionalBridgeExt`

## Declaration Counts

- `def`: 11
- `eval`: 8
- `inductive`: 1
- `structure`: 4
- `theorem`: 12

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [DimExponents](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/dim-exponents/) | L64-L69 | type/data schema | type/data schema | `IV.D32` |
| `def` | [DimExponents.add](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/add/) | L72-L73 | definition | definition | — |
| `def` | [DimExponents.scale](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/scale/) | L76-L77 | data/computed value | data/computed value | — |
| `def` | [DimExponents.zero](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/zero/) | L80-L80 | definition | definition | — |
| `structure` | [DimensionalFormula](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/dimensional-formula/) | L89-L102 | type/data schema | type/data schema | — |
| `def` | [c_formula](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/c-formula/) | L110-L116 | definition | definition | `IV.D33` |
| `def` | [h_formula](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/h-formula/) | L120-L126 | definition | definition | `IV.D34` |
| `def` | [ke_formula](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/ke-formula/) | L130-L136 | definition | definition | `IV.D35` |
| `def` | [eps0_formula](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eps0-formula/) | L140-L146 | definition | definition | `IV.D36` |
| `def` | [mu0_formula](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/mu0-formula/) | L150-L156 | definition | definition | `IV.D37` |
| `def` | [derivation_chain](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/derivation-chain/) | L159-L160 | data/computed value | data/computed value | — |
| `theorem` | [derivation_chain_count](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/derivation-chain-count/) | L163-L163 | proof obligation | formal proof obligation checked | — |
| `theorem` | [maxwell_dimensional](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-dimensional/) | L172-L176 | proof obligation | formal proof obligation checked | `IV.T07` |
| `theorem` | [maxwell_prefactor](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-prefactor/) | L182-L186 | proof obligation | formal proof obligation checked | `IV.T07` |
| `theorem` | [maxwell_complete](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/maxwell-complete/) | L191-L200 | proof obligation | formal proof obligation checked | — |
| `theorem` | [coulomb_permittivity_dimensional](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/coulomb-permittivity-dimensional/) | L209-L211 | proof obligation | formal proof obligation checked | `IV.T08` |
| `theorem` | [coulomb_permittivity_prefactor](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/coulomb-permittivity-prefactor/) | L223-L227 | proof obligation | formal proof obligation checked | `IV.T08` |
| `inductive` | [SITier](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/sitier/) | L234-L238 | type/data schema | type/data schema | — |
| `structure` | [TieredConstant](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/tiered-constant/) | L241-L244 | type/data schema | type/data schema | — |
| `def` | [tiered_exact_constants](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/tiered-exact-constants/) | L247-L252 | data/computed value | data/computed value | — |
| `theorem` | [tiered_count](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/tiered-count/) | L255-L257 | proof obligation | formal proof obligation checked | — |
| `structure` | [GravityFrontier](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/gravity-frontier/) | L270-L279 | type/data schema | type/data schema | `IV.R08` |
| `def` | [gravity_frontier](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/gravity-frontier-l282/) | L282-L282 | definition | definition | — |
| `theorem` | [g_is_deferred](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/g-is-deferred/) | L285-L285 | proof obligation | formal proof obligation checked | — |
| `theorem` | [c_is_velocity](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/c-is-velocity/) | L292-L293 | proof obligation | formal proof obligation checked | — |
| `theorem` | [h_is_action](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/h-is-action/) | L296-L297 | proof obligation | formal proof obligation checked | — |
| `theorem` | [eps0_mu0_inverse](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eps0-mu0-inverse/) | L300-L303 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ke_eps0_inverse](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/ke-eps0-inverse/) | L306-L309 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l316/) | L316-L316 | computed check | computed check | — |
| `eval` | [#eval L319](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l319/) | L319-L319 | computed check | computed check | — |
| `eval` | [#eval L320](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l320/) | L320-L320 | computed check | computed check | — |
| `eval` | [#eval L321](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l321/) | L321-L321 | computed check | computed check | — |
| `eval` | [#eval L322](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l322/) | L322-L322 | computed check | computed check | — |
| `eval` | [#eval L323](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l323/) | L323-L323 | computed check | computed check | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l326/) | L326-L326 | computed check | computed check | — |
| `eval` | [#eval L329](/corpus/taulib/docs/book-iv-calibration-dimensional-bridge/eval-l329/) | L329-L331 | computed check | computed check | — |

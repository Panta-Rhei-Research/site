---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_slug": "book-v-fluid-macro-charge-obstruction",
  "book": "BookV",
  "family": "FluidMacro",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/FluidMacro/ChargeObstruction.lean",
  "sha256": "bdd4a8c443c867e6a4f03ff9e52a6ab6477c46317d3ec3b0c37d8f136e706414",
  "imports": [
    "TauLib.BookV.FluidMacro.Turbulence"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.FluidMacro.TauPlasma"
  ],
  "registry_ids": [
    "V.C10",
    "V.C11",
    "V.C12",
    "V.D101",
    "V.D102",
    "V.D103",
    "V.R149",
    "V.R150",
    "V.R151",
    "V.T73"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 7,
    "def": 6,
    "theorem": 5,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "ChargeSector",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/charge-sector/",
      "source_line_start": 58,
      "source_line_end": 65,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroCharge",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-charge/",
      "source_line_start": 72,
      "source_line_end": 79,
      "formal_status": "defined",
      "registry_ids": [
        "V.D101"
      ]
    },
    {
      "kind": "def",
      "name": "MacroCharge.isGloballyNeutral",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/is-globally-neutral/",
      "source_line_start": 82,
      "source_line_end": 83,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoIsolatedChargesThm",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-isolated-charges-thm/",
      "source_line_start": 96,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": [
        "V.T73"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_isolated_charges",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-isolated-charges/",
      "source_line_start": 106,
      "source_line_end": 107,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ChargeQuantum",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/charge-quantum/",
      "source_line_start": 118,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": [
        "V.R149"
      ]
    },
    {
      "kind": "def",
      "name": "charge_quantization",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/charge-quantization/",
      "source_line_start": 124,
      "source_line_end": 124,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sourceless_macro_flux",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/sourceless-macro-flux/",
      "source_line_start": 137,
      "source_line_end": 138,
      "formal_status": "formalized",
      "registry_ids": [
        "V.C10"
      ]
    },
    {
      "kind": "structure",
      "name": "MagneticCharge",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/magnetic-charge/",
      "source_line_start": 145,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_magnetic_monopoles",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-magnetic-monopoles/",
      "source_line_start": 157,
      "source_line_end": 158,
      "formal_status": "formalized",
      "registry_ids": [
        "V.C11"
      ]
    },
    {
      "kind": "structure",
      "name": "MacroEMField",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-emfield/",
      "source_line_start": 170,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": [
        "V.D102"
      ]
    },
    {
      "kind": "def",
      "name": "MacroEMField.standard",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/standard/",
      "source_line_start": 180,
      "source_line_end": 181,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "ConfinementLevel",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/confinement-level/",
      "source_line_start": 188,
      "source_line_end": 195,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroColorConfinement",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-color-confinement/",
      "source_line_start": 204,
      "source_line_end": 211,
      "formal_status": "defined",
      "registry_ids": [
        "V.C12"
      ]
    },
    {
      "kind": "theorem",
      "name": "macro_color_confinement",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-color-confinement-l214/",
      "source_line_start": 214,
      "source_line_end": 216,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroCurrent",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-current/",
      "source_line_start": 226,
      "source_line_end": 233,
      "formal_status": "defined",
      "registry_ids": [
        "V.D103"
      ]
    },
    {
      "kind": "theorem",
      "name": "current_conservation",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/current-conservation/",
      "source_line_start": 236,
      "source_line_end": 237,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "electron_charge",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/electron-charge/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "proton_charge",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/proton-charge/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_balance",
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/example-balance/",
      "source_line_start": 260,
      "source_line_end": 263,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/eval-l267/",
      "source_line_start": 267,
      "source_line_end": 269,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean",
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
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/FluidMacro/ChargeObstruction.lean`
- SHA-256: `bdd4a8c443c867e6a4f03ff9e52a6ab6477c46317d3ec3b0c37d8f136e706414`

## Registry Links

- `V.C10` — Sourceless macro flux
- `V.C11` — No magnetic monopoles
- `V.C12` — Macro color confinement
- `V.D101` — Macro charge
- `V.D102` — Macro EM field
- `V.D103` — Macro current
- `V.R149` — Charge quantization
- `V.R150` — Local charges still exist
- `V.R151` — Quark-gluon plasma is still confined
- `V.T73` — No Isolated Charges

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.FluidMacro.Turbulence`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.FluidMacro.TauPlasma`

## Declaration Counts

- `def`: 6
- `eval`: 3
- `inductive`: 2
- `structure`: 7
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [ChargeSector](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/charge-sector/) | L58-L65 | defined | — |
| `structure` | [MacroCharge](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-charge/) | L72-L79 | defined | `V.D101` |
| `def` | [MacroCharge.isGloballyNeutral](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/is-globally-neutral/) | L82-L83 | defined | — |
| `structure` | [NoIsolatedChargesThm](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-isolated-charges-thm/) | L96-L103 | defined | `V.T73` |
| `theorem` | [no_isolated_charges](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-isolated-charges/) | L106-L107 | formalized | — |
| `structure` | [ChargeQuantum](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/charge-quantum/) | L118-L121 | defined | `V.R149` |
| `def` | [charge_quantization](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/charge-quantization/) | L124-L124 | defined | — |
| `theorem` | [sourceless_macro_flux](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/sourceless-macro-flux/) | L137-L138 | formalized | `V.C10` |
| `structure` | [MagneticCharge](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/magnetic-charge/) | L145-L150 | defined | — |
| `theorem` | [no_magnetic_monopoles](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/no-magnetic-monopoles/) | L157-L158 | formalized | `V.C11` |
| `structure` | [MacroEMField](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-emfield/) | L170-L177 | defined | `V.D102` |
| `def` | [MacroEMField.standard](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/standard/) | L180-L181 | defined | — |
| `inductive` | [ConfinementLevel](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/confinement-level/) | L188-L195 | defined | — |
| `structure` | [MacroColorConfinement](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-color-confinement/) | L204-L211 | defined | `V.C12` |
| `theorem` | [macro_color_confinement](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-color-confinement-l214/) | L214-L216 | formalized | — |
| `structure` | [MacroCurrent](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/macro-current/) | L226-L233 | defined | `V.D103` |
| `theorem` | [current_conservation](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/current-conservation/) | L236-L237 | formalized | — |
| `def` | [electron_charge](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/electron-charge/) | L256-L256 | defined | — |
| `def` | [proton_charge](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/proton-charge/) | L257-L257 | defined | — |
| `def` | [example_balance](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/example-balance/) | L260-L263 | defined | — |
| `eval` | [#eval L265](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/eval-l265/) | L265-L265 | computed | — |
| `eval` | [#eval L266](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/eval-l266/) | L266-L266 | computed | — |
| `eval` | [#eval L267](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/eval-l267/) | L267-L269 | computed | — |

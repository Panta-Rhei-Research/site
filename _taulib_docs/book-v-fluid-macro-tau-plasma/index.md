---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.FluidMacro.TauPlasma",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.FluidMacro.TauPlasma`.",
  "module_name": "TauLib.BookV.FluidMacro.TauPlasma",
  "module_slug": "book-v-fluid-macro-tau-plasma",
  "book": "BookV",
  "family": "FluidMacro",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/FluidMacro/TauPlasma.lean",
  "sha256": "f2f4bed1fad74731f4d5b10412b39aa07b67c7e6de7eb6f19bfe270699e73622",
  "imports": [
    "TauLib.BookV.FluidMacro.ChargeObstruction"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.FluidMacro.TauMHD"
  ],
  "registry_ids": [
    "V.D104",
    "V.D105",
    "V.D106",
    "V.P46",
    "V.P47",
    "V.P48",
    "V.R152",
    "V.R153",
    "V.T74"
  ],
  "declaration_counts": {
    "structure": 10,
    "def": 5,
    "theorem": 6,
    "inductive": 1,
    "eval": 2
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TauPlasmaState",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/tau-plasma-state/",
      "source_line_start": 64,
      "source_line_end": 77,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D104"
      ]
    },
    {
      "kind": "structure",
      "name": "DebyeLength",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-length/",
      "source_line_start": 86,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "DebyeLength.toFloat",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/to-float/",
      "source_line_start": 98,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "QuasiNeutralityBound",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/quasi-neutrality-bound/",
      "source_line_start": 110,
      "source_line_end": 117,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.T74"
      ]
    },
    {
      "kind": "theorem",
      "name": "forced_quasineutrality",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/forced-quasineutrality/",
      "source_line_start": 120,
      "source_line_end": 122,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PlasmaFrequency",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-frequency/",
      "source_line_start": 130,
      "source_line_end": 139,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PlasmaOscillation",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-oscillation/",
      "source_line_start": 146,
      "source_line_end": 153,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P46"
      ]
    },
    {
      "kind": "theorem",
      "name": "plasma_oscillations",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-oscillations/",
      "source_line_start": 156,
      "source_line_end": 158,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "PlasmaWaveMode",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-wave-mode/",
      "source_line_start": 165,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PlasmaDispersion",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-dispersion/",
      "source_line_start": 176,
      "source_line_end": 186,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P47"
      ]
    },
    {
      "kind": "theorem",
      "name": "plasma_cutoff",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-cutoff/",
      "source_line_start": 189,
      "source_line_end": 191,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "IonosphericReflection",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/ionospheric-reflection/",
      "source_line_start": 201,
      "source_line_end": 206,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.R152"
      ]
    },
    {
      "kind": "def",
      "name": "ionospheric_reflection",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/ionospheric-reflection-l208/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DebyeShielding",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-shielding/",
      "source_line_start": 220,
      "source_line_end": 227,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.P48"
      ]
    },
    {
      "kind": "theorem",
      "name": "debye_shielding",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-shielding-l230/",
      "source_line_start": 230,
      "source_line_end": 232,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DebyeNumber",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-number/",
      "source_line_start": 243,
      "source_line_end": 250,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D105"
      ]
    },
    {
      "kind": "def",
      "name": "no_dark_matter_icm",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/no-dark-matter-icm/",
      "source_line_start": 260,
      "source_line_end": 262,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "V.R153"
      ]
    },
    {
      "kind": "theorem",
      "name": "no_dark_matter_icm_holds",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/no-dark-matter-icm-holds/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MHDLimitCondition",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/mhdlimit-condition/",
      "source_line_start": 276,
      "source_line_end": 285,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D106"
      ]
    },
    {
      "kind": "theorem",
      "name": "mhd_limit_valid",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/mhd-limit-valid/",
      "source_line_start": 288,
      "source_line_end": 293,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_plasma",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/example-plasma/",
      "source_line_start": 300,
      "source_line_end": 306,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "example_debye",
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/example-debye/",
      "source_line_start": 309,
      "source_line_end": 313,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/eval-l315/",
      "source_line_start": 315,
      "source_line_end": 315,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/eval-l316/",
      "source_line_start": 316,
      "source_line_end": 318,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean",
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
- Source path: [`TauLib/BookV/FluidMacro/TauPlasma.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauPlasma.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/FluidMacro/TauPlasma.lean`
- SHA-256: `f2f4bed1fad74731f4d5b10412b39aa07b67c7e6de7eb6f19bfe270699e73622`

## Registry Links

- `V.D104` — tau-plasma
- `V.D105` — Debye number
- `V.D106` — MHD limit
- `V.P46` — Plasma oscillations
- `V.P47` — Plasma cutoff
- `V.P48` — Debye shielding
- `V.R152` — Ionospheric reflection
- `V.R153` — No dark matter in the ICM
- `V.T74` — Forced Quasi-Neutrality

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.FluidMacro.ChargeObstruction`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.FluidMacro.TauMHD`

## Declaration Counts

- `def`: 5
- `eval`: 2
- `inductive`: 1
- `structure`: 10
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [TauPlasmaState](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/tau-plasma-state/) | L64-L77 | type/data schema | type/data schema | `V.D104` |
| `structure` | [DebyeLength](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-length/) | L86-L95 | type/data schema | type/data schema | — |
| `def` | [DebyeLength.toFloat](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/to-float/) | L98-L99 | data/computed value | data/computed value | — |
| `structure` | [QuasiNeutralityBound](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/quasi-neutrality-bound/) | L110-L117 | type/data schema | type/data schema | `V.T74` |
| `theorem` | [forced_quasineutrality](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/forced-quasineutrality/) | L120-L122 | proof obligation | formal proof obligation checked | — |
| `structure` | [PlasmaFrequency](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-frequency/) | L130-L139 | type/data schema | type/data schema | — |
| `structure` | [PlasmaOscillation](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-oscillation/) | L146-L153 | type/data schema | type/data schema | `V.P46` |
| `theorem` | [plasma_oscillations](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-oscillations/) | L156-L158 | proof obligation | formal proof obligation checked | — |
| `inductive` | [PlasmaWaveMode](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-wave-mode/) | L165-L172 | type/data schema | type/data schema | — |
| `structure` | [PlasmaDispersion](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-dispersion/) | L176-L186 | type/data schema | type/data schema | `V.P47` |
| `theorem` | [plasma_cutoff](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/plasma-cutoff/) | L189-L191 | proof obligation | formal proof obligation checked | — |
| `structure` | [IonosphericReflection](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/ionospheric-reflection/) | L201-L206 | type/data schema | type/data schema | `V.R152` |
| `def` | [ionospheric_reflection](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/ionospheric-reflection-l208/) | L208-L210 | definition | definition | — |
| `structure` | [DebyeShielding](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-shielding/) | L220-L227 | type/data schema | type/data schema | `V.P48` |
| `theorem` | [debye_shielding](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-shielding-l230/) | L230-L232 | proof obligation | formal proof obligation checked | — |
| `structure` | [DebyeNumber](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/debye-number/) | L243-L250 | type/data schema | type/data schema | `V.D105` |
| `def` | [no_dark_matter_icm](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/no-dark-matter-icm/) | L260-L262 | definition | definition | `V.R153` |
| `theorem` | [no_dark_matter_icm_holds](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/no-dark-matter-icm-holds/) | L264-L264 | proof obligation | formal proof obligation checked | — |
| `structure` | [MHDLimitCondition](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/mhdlimit-condition/) | L276-L285 | type/data schema | type/data schema | `V.D106` |
| `theorem` | [mhd_limit_valid](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/mhd-limit-valid/) | L288-L293 | proof obligation | formal proof obligation checked | — |
| `def` | [example_plasma](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/example-plasma/) | L300-L306 | definition | definition | — |
| `def` | [example_debye](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/example-debye/) | L309-L313 | definition | definition | — |
| `eval` | [#eval L315](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/eval-l315/) | L315-L315 | computed check | computed check | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-v-fluid-macro-tau-plasma/eval-l316/) | L316-L318 | computed check | computed check | — |

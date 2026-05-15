---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.GravityField.LinearEinstein",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.GravityField.LinearEinstein`.",
  "module_name": "TauLib.BookV.GravityField.LinearEinstein",
  "module_slug": "book-v-gravity-field-linear-einstein",
  "book": "BookV",
  "family": "GravityField",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/GravityField/LinearEinstein.lean",
  "sha256": "d8de271f97c4c0ecdcd39a32403d2b7dabb1c6a2349e47efabd367e68f4f6556",
  "imports": [
    "TauLib.BookV.GravityField.TauEinsteinEq"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.GravityField.NonlinearEinstein"
  ],
  "registry_ids": [
    "V.D52",
    "V.D53",
    "V.P14",
    "V.R70",
    "V.R71",
    "V.T28",
    "V.T29",
    "V.T30",
    "V.T31",
    "V.T32"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 5,
    "inductive": 2,
    "theorem": 6,
    "eval": 8
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "LinearizedEinstein",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/linearized-einstein/",
      "source_line_start": 82,
      "source_line_end": 93,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D52"
      ]
    },
    {
      "kind": "def",
      "name": "first_order_einstein",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/first-order-einstein/",
      "source_line_start": 96,
      "source_line_end": 101,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "GWPolarization",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/gwpolarization/",
      "source_line_start": 108,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "RadiationPattern",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/radiation-pattern/",
      "source_line_start": 116,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GravitationalWave",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/gravitational-wave/",
      "source_line_start": 133,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "V.D53"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_gw",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/canonical-gw/",
      "source_line_start": 153,
      "source_line_end": 161,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ClassicalTestResult",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/classical-test-result/",
      "source_line_start": 168,
      "source_line_end": 179,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mercury_precession_value",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/mercury-precession-value/",
      "source_line_start": 182,
      "source_line_end": 187,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "light_deflection_value",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/light-deflection-value/",
      "source_line_start": 190,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "grav_redshift_value",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-redshift-value/",
      "source_line_start": 198,
      "source_line_end": 203,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "newtonian_recovery",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/newtonian-recovery/",
      "source_line_start": 215,
      "source_line_end": 218,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T28"
      ]
    },
    {
      "kind": "theorem",
      "name": "mercury_precession",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/mercury-precession/",
      "source_line_start": 230,
      "source_line_end": 233,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T29"
      ]
    },
    {
      "kind": "theorem",
      "name": "light_deflection",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/light-deflection/",
      "source_line_start": 244,
      "source_line_end": 247,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T30"
      ]
    },
    {
      "kind": "theorem",
      "name": "grav_redshift",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-redshift/",
      "source_line_start": 258,
      "source_line_end": 259,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T31"
      ]
    },
    {
      "kind": "theorem",
      "name": "grav_wave_properties",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-wave-properties/",
      "source_line_start": 270,
      "source_line_end": 275,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.T32"
      ]
    },
    {
      "kind": "theorem",
      "name": "grav_wave_speed_c",
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-wave-speed-c/",
      "source_line_start": 287,
      "source_line_end": 288,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "V.P14"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l313/",
      "source_line_start": 313,
      "source_line_end": 313,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": [
        "V.R70",
        "V.R71"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l314/",
      "source_line_start": 314,
      "source_line_end": 314,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l316/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l317/",
      "source_line_start": 317,
      "source_line_end": 317,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l320/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l321/",
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
      "url": "/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l323/",
      "source_line_start": 323,
      "source_line_end": 327,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean",
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
- Source path: [`TauLib/BookV/GravityField/LinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LinearEinstein.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/GravityField/LinearEinstein.lean`
- SHA-256: `d8de271f97c4c0ecdcd39a32403d2b7dabb1c6a2349e47efabd367e68f4f6556`

## Registry Links

- `V.D52` — Linearized tau-Einstein equation
- `V.D53` — Gravitational wave in tau-framework
- `V.P14` — v_mathrmGW
- `V.R70` — No fitting
- `V.R71` — Two polarizations from two fiber directions
- `V.T28` — Newtonian limit recovery
- `V.T29` — Mercury precession from tau-Einstein
- `V.T30` — Light deflection from tau-Einstein
- `V.T31` — Gravitational redshift from tau-Einstein
- `V.T32` — Gravitational wave properties

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.GravityField.TauEinsteinEq`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.GravityField.NonlinearEinstein`

## Declaration Counts

- `def`: 5
- `eval`: 8
- `inductive`: 2
- `structure`: 3
- `theorem`: 6

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [LinearizedEinstein](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/linearized-einstein/) | L82-L93 | type/data schema | type/data schema | `V.D52` |
| `def` | [first_order_einstein](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/first-order-einstein/) | L96-L101 | definition | definition | — |
| `inductive` | [GWPolarization](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/gwpolarization/) | L108-L113 | type/data schema | type/data schema | — |
| `inductive` | [RadiationPattern](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/radiation-pattern/) | L116-L123 | type/data schema | type/data schema | — |
| `structure` | [GravitationalWave](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/gravitational-wave/) | L133-L150 | type/data schema | type/data schema | `V.D53` |
| `def` | [canonical_gw](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/canonical-gw/) | L153-L161 | definition | definition | — |
| `structure` | [ClassicalTestResult](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/classical-test-result/) | L168-L179 | type/data schema | type/data schema | — |
| `def` | [mercury_precession_value](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/mercury-precession-value/) | L182-L187 | definition | definition | — |
| `def` | [light_deflection_value](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/light-deflection-value/) | L190-L195 | definition | definition | — |
| `def` | [grav_redshift_value](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-redshift-value/) | L198-L203 | definition | definition | — |
| `theorem` | [newtonian_recovery](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/newtonian-recovery/) | L215-L218 | proof obligation | formal proof obligation checked | `V.T28` |
| `theorem` | [mercury_precession](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/mercury-precession/) | L230-L233 | proof obligation | formal proof obligation checked | `V.T29` |
| `theorem` | [light_deflection](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/light-deflection/) | L244-L247 | proof obligation | formal proof obligation checked | `V.T30` |
| `theorem` | [grav_redshift](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-redshift/) | L258-L259 | proof obligation | formal proof obligation checked | `V.T31` |
| `theorem` | [grav_wave_properties](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-wave-properties/) | L270-L275 | proof obligation | formal proof obligation checked | `V.T32` |
| `theorem` | [grav_wave_speed_c](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/grav-wave-speed-c/) | L287-L288 | proof obligation | formal proof obligation checked | `V.P14` |
| `eval` | [#eval L313](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l313/) | L313-L313 | computed check | computed check | `V.R70`, `V.R71` |
| `eval` | [#eval L314](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l314/) | L314-L314 | computed check | computed check | — |
| `eval` | [#eval L316](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l316/) | L316-L316 | computed check | computed check | — |
| `eval` | [#eval L317](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l317/) | L317-L317 | computed check | computed check | — |
| `eval` | [#eval L318](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l318/) | L318-L318 | computed check | computed check | — |
| `eval` | [#eval L320](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l320/) | L320-L320 | computed check | computed check | — |
| `eval` | [#eval L321](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l321/) | L321-L321 | computed check | computed check | — |
| `eval` | [#eval L323](/corpus/taulib/docs/book-v-gravity-field-linear-einstein/eval-l323/) | L323-L327 | computed check | computed check | — |

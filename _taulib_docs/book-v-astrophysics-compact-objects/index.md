---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookV.Astrophysics.CompactObjects",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookV.Astrophysics.CompactObjects`.",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_slug": "book-v-astrophysics-compact-objects",
  "book": "BookV",
  "family": "Astrophysics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookV/Astrophysics/CompactObjects.lean",
  "sha256": "9b00331c225107646a47e8ff45a52fa77e54958333428eb6b109a0624694be5a",
  "imports": [
    "TauLib.BookV.Astrophysics.RotationCurves"
  ],
  "imported_by": [
    "TauLib.BookV",
    "TauLib.BookV.Astrophysics.Supernovae"
  ],
  "registry_ids": [
    "V.D124",
    "V.D125",
    "V.P71",
    "V.P72",
    "V.R177",
    "V.R178",
    "V.R179",
    "V.R180",
    "V.T86",
    "V.T87",
    "V.T88"
  ],
  "declaration_counts": {
    "inductive": 2,
    "structure": 2,
    "def": 6,
    "theorem": 5,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "CompactObjectType",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/compact-object-type/",
      "source_line_start": 66,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": [
        "V.D124"
      ]
    },
    {
      "kind": "structure",
      "name": "CompactObjectData",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/compact-object-data/",
      "source_line_start": 78,
      "source_line_end": 91,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "chandrasekhar_mass_limit",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/chandrasekhar-mass-limit/",
      "source_line_start": 98,
      "source_line_end": 98,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "wd_mass_limit",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/wd-mass-limit/",
      "source_line_start": 110,
      "source_line_end": 112,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T86"
      ]
    },
    {
      "kind": "theorem",
      "name": "ns_eos_from_defect",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/ns-eos-from-defect/",
      "source_line_start": 125,
      "source_line_end": 127,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P71"
      ]
    },
    {
      "kind": "def",
      "name": "tov_mass_lower",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/tov-mass-lower/",
      "source_line_start": 134,
      "source_line_end": 134,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "tov_mass_upper",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/tov-mass-upper/",
      "source_line_start": 135,
      "source_line_end": 135,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tov_maximum_mass",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/tov-maximum-mass/",
      "source_line_start": 144,
      "source_line_end": 145,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T87"
      ]
    },
    {
      "kind": "inductive",
      "name": "PulsarType",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/pulsar-type/",
      "source_line_start": 152,
      "source_line_end": 159,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PulsarData",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/pulsar-data/",
      "source_line_start": 166,
      "source_line_end": 179,
      "formal_status": "defined",
      "registry_ids": [
        "V.D125"
      ]
    },
    {
      "kind": "def",
      "name": "mass_gap_lower",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/mass-gap-lower/",
      "source_line_start": 186,
      "source_line_end": 186,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mass_gap_upper",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/mass-gap-upper/",
      "source_line_start": 188,
      "source_line_end": 188,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mass_gap_prediction",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/mass-gap-prediction/",
      "source_line_start": 201,
      "source_line_end": 202,
      "formal_status": "formalized",
      "registry_ids": [
        "V.T88"
      ]
    },
    {
      "kind": "theorem",
      "name": "magnetar_from_vortex",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/magnetar-from-vortex/",
      "source_line_start": 214,
      "source_line_end": 216,
      "formal_status": "formalized",
      "registry_ids": [
        "V.P72"
      ]
    },
    {
      "kind": "def",
      "name": "crab_pulsar",
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/crab-pulsar/",
      "source_line_start": 247,
      "source_line_end": 260,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 268,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean",
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
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookV/Astrophysics/CompactObjects.lean`
- SHA-256: `9b00331c225107646a47e8ff45a52fa77e54958333428eb6b109a0624694be5a`

## Registry Links

- `V.D124` — Degeneracy Pressure Character --- V.D57
- `V.D125` — Black Hole as Maximal Topological Defect --- V.D58
- `V.P71` — Neutron Star EOS Structure --- V.P35
- `V.P72` — Hulse--Taylor Agreement --- V.P36
- `V.R177` — White dwarf mass--radius relation
- `V.R178` — The mass gap
- `V.R179` — No primordial black holes
- `V.R180` — Pulsars probe the strong-field regime
- `V.T86` — Chandrasekhar Mass from tau-Framework --- V.T38
- `V.T87` — TOV Mass Limit --- V.T39
- `V.T88` — Compact-Object Classification --- V.T40

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookV.Astrophysics.RotationCurves`

## Imported By

- `TauLib.BookV`
- `TauLib.BookV.Astrophysics.Supernovae`

## Declaration Counts

- `def`: 6
- `eval`: 5
- `inductive`: 2
- `structure`: 2
- `theorem`: 5

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [CompactObjectType](/verify/taulib/docs/book-v-astrophysics-compact-objects/compact-object-type/) | L66-L75 | defined | `V.D124` |
| `structure` | [CompactObjectData](/verify/taulib/docs/book-v-astrophysics-compact-objects/compact-object-data/) | L78-L91 | defined | — |
| `def` | [chandrasekhar_mass_limit](/verify/taulib/docs/book-v-astrophysics-compact-objects/chandrasekhar-mass-limit/) | L98-L98 | defined | — |
| `theorem` | [wd_mass_limit](/verify/taulib/docs/book-v-astrophysics-compact-objects/wd-mass-limit/) | L110-L112 | formalized | `V.T86` |
| `theorem` | [ns_eos_from_defect](/verify/taulib/docs/book-v-astrophysics-compact-objects/ns-eos-from-defect/) | L125-L127 | formalized | `V.P71` |
| `def` | [tov_mass_lower](/verify/taulib/docs/book-v-astrophysics-compact-objects/tov-mass-lower/) | L134-L134 | defined | — |
| `def` | [tov_mass_upper](/verify/taulib/docs/book-v-astrophysics-compact-objects/tov-mass-upper/) | L135-L135 | defined | — |
| `theorem` | [tov_maximum_mass](/verify/taulib/docs/book-v-astrophysics-compact-objects/tov-maximum-mass/) | L144-L145 | formalized | `V.T87` |
| `inductive` | [PulsarType](/verify/taulib/docs/book-v-astrophysics-compact-objects/pulsar-type/) | L152-L159 | defined | — |
| `structure` | [PulsarData](/verify/taulib/docs/book-v-astrophysics-compact-objects/pulsar-data/) | L166-L179 | defined | `V.D125` |
| `def` | [mass_gap_lower](/verify/taulib/docs/book-v-astrophysics-compact-objects/mass-gap-lower/) | L186-L186 | defined | — |
| `def` | [mass_gap_upper](/verify/taulib/docs/book-v-astrophysics-compact-objects/mass-gap-upper/) | L188-L188 | defined | — |
| `theorem` | [mass_gap_prediction](/verify/taulib/docs/book-v-astrophysics-compact-objects/mass-gap-prediction/) | L201-L202 | formalized | `V.T88` |
| `theorem` | [magnetar_from_vortex](/verify/taulib/docs/book-v-astrophysics-compact-objects/magnetar-from-vortex/) | L214-L216 | formalized | `V.P72` |
| `def` | [crab_pulsar](/verify/taulib/docs/book-v-astrophysics-compact-objects/crab-pulsar/) | L247-L260 | defined | — |
| `eval` | [#eval L262](/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l262/) | L262-L262 | computed | — |
| `eval` | [#eval L263](/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l263/) | L263-L263 | computed | — |
| `eval` | [#eval L264](/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l264/) | L264-L264 | computed | — |
| `eval` | [#eval L265](/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l265/) | L265-L265 | computed | — |
| `eval` | [#eval L266](/verify/taulib/docs/book-v-astrophysics-compact-objects/eval-l266/) | L266-L268 | computed | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.MassEnergy",
  "permalink": "/corpus/taulib/docs/book-iv-physics-mass-energy/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.MassEnergy`.",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_slug": "book-iv-physics-mass-energy",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/MassEnergy.lean",
  "sha256": "4d8cdc93d16bf603eee0334ccd45647b3a2c510aed6c55cba8e893593231765d",
  "imports": [
    "TauLib.BookIV.Physics.QuantityFramework",
    "TauLib.BookIV.Sectors.CouplingFormulas"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Calibration.CalibrationAnchor",
    "TauLib.BookIV.Physics.NucleonMassSplitting",
    "TauLib.BookV.Prologue.ExportContract"
  ],
  "registry_ids": [
    "IV.D20",
    "IV.D21",
    "IV.D22",
    "IV.D23",
    "IV.R04"
  ],
  "declaration_counts": {
    "structure": 7,
    "def": 3,
    "theorem": 3,
    "eval": 2
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "MassIndex",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/mass-index/",
      "source_line_start": 75,
      "source_line_end": 86,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D20"
      ]
    },
    {
      "kind": "def",
      "name": "MassIndex.toFloat",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/to-float/",
      "source_line_start": 89,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "EnergyIndex",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/energy-index/",
      "source_line_start": 101,
      "source_line_end": 110,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D21"
      ]
    },
    {
      "kind": "def",
      "name": "EnergyIndex.toFloat",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/to-float-l113/",
      "source_line_start": 113,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SpeedConstant",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/speed-constant/",
      "source_line_start": 126,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D22"
      ]
    },
    {
      "kind": "def",
      "name": "SpeedConstant.toFloat",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/to-float-l136/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MassEnergyRelation",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/mass-energy-relation/",
      "source_line_start": 151,
      "source_line_end": 162,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D23"
      ]
    },
    {
      "kind": "structure",
      "name": "OnticParticle",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/ontic-particle/",
      "source_line_start": 169,
      "source_line_end": 176,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "RadiationCarrier",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/radiation-carrier/",
      "source_line_start": 179,
      "source_line_end": 184,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutronRole",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/neutron-role/",
      "source_line_start": 201,
      "source_line_end": 208,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R04"
      ]
    },
    {
      "kind": "theorem",
      "name": "ontic_has_fiber",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/ontic-has-fiber/",
      "source_line_start": 215,
      "source_line_end": 216,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "ontic_is_persistent",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/ontic-is-persistent/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mass_energy_positive",
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/mass-energy-positive/",
      "source_line_start": 224,
      "source_line_end": 228,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/eval-l238/",
      "source_line_start": 238,
      "source_line_end": 240,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean",
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
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/MassEnergy.lean`
- SHA-256: `4d8cdc93d16bf603eee0334ccd45647b3a2c510aed6c55cba8e893593231765d`

## Registry Links

- `IV.D20` — Mass Index
- `IV.D21` — Energy Index
- `IV.D22` — Speed Constant
- `IV.D23` — Mass-Energy Relation
- `IV.R04` — Neutron First Ontic Particle

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.QuantityFramework`
- `TauLib.BookIV.Sectors.CouplingFormulas`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Calibration.CalibrationAnchor`
- `TauLib.BookIV.Physics.NucleonMassSplitting`
- `TauLib.BookV.Prologue.ExportContract`

## Declaration Counts

- `def`: 3
- `eval`: 2
- `structure`: 7
- `theorem`: 3

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [MassIndex](/corpus/taulib/docs/book-iv-physics-mass-energy/mass-index/) | L75-L86 | type/data schema | type/data schema | `IV.D20` |
| `def` | [MassIndex.toFloat](/corpus/taulib/docs/book-iv-physics-mass-energy/to-float/) | L89-L90 | data/computed value | data/computed value | — |
| `structure` | [EnergyIndex](/corpus/taulib/docs/book-iv-physics-mass-energy/energy-index/) | L101-L110 | type/data schema | type/data schema | `IV.D21` |
| `def` | [EnergyIndex.toFloat](/corpus/taulib/docs/book-iv-physics-mass-energy/to-float-l113/) | L113-L114 | data/computed value | data/computed value | — |
| `structure` | [SpeedConstant](/corpus/taulib/docs/book-iv-physics-mass-energy/speed-constant/) | L126-L133 | type/data schema | type/data schema | `IV.D22` |
| `def` | [SpeedConstant.toFloat](/corpus/taulib/docs/book-iv-physics-mass-energy/to-float-l136/) | L136-L137 | data/computed value | data/computed value | — |
| `structure` | [MassEnergyRelation](/corpus/taulib/docs/book-iv-physics-mass-energy/mass-energy-relation/) | L151-L162 | type/data schema | type/data schema | `IV.D23` |
| `structure` | [OnticParticle](/corpus/taulib/docs/book-iv-physics-mass-energy/ontic-particle/) | L169-L176 | type/data schema | type/data schema | — |
| `structure` | [RadiationCarrier](/corpus/taulib/docs/book-iv-physics-mass-energy/radiation-carrier/) | L179-L184 | type/data schema | type/data schema | — |
| `structure` | [NeutronRole](/corpus/taulib/docs/book-iv-physics-mass-energy/neutron-role/) | L201-L208 | type/data schema | type/data schema | `IV.R04` |
| `theorem` | [ontic_has_fiber](/corpus/taulib/docs/book-iv-physics-mass-energy/ontic-has-fiber/) | L215-L216 | proof obligation | formal proof obligation checked | — |
| `theorem` | [ontic_is_persistent](/corpus/taulib/docs/book-iv-physics-mass-energy/ontic-is-persistent/) | L219-L220 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mass_energy_positive](/corpus/taulib/docs/book-iv-physics-mass-energy/mass-energy-positive/) | L224-L228 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L235](/corpus/taulib/docs/book-iv-physics-mass-energy/eval-l235/) | L235-L235 | computed check | computed check | — |
| `eval` | [#eval L238](/corpus/taulib/docs/book-iv-physics-mass-energy/eval-l238/) | L238-L240 | computed check | computed check | — |

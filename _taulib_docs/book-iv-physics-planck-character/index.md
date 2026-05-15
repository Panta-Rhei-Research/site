---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.PlanckCharacter",
  "permalink": "/corpus/taulib/docs/book-iv-physics-planck-character/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.PlanckCharacter`.",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_slug": "book-iv-physics-planck-character",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/PlanckCharacter.lean",
  "sha256": "bff610f462ff10dad68d370b5e9aeabf6597f0adae178625a8c8f367b4fbd620",
  "imports": [
    "TauLib.BookIV.Physics.QuantityFramework",
    "TauLib.BookIV.Sectors.SectorParameters"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.ActorsDynamics",
    "TauLib.BookIV.QuantumMechanics.Quantization",
    "TauLib.BookIV.QuantumMechanics.QuantumCharacters"
  ],
  "registry_ids": [
    "IV.D13",
    "IV.D14",
    "IV.D15",
    "IV.R03",
    "IV.T03"
  ],
  "declaration_counts": {
    "structure": 4,
    "def": 11,
    "theorem": 7,
    "eval": 6
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "PlanckCharacter",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/planck-character/",
      "source_line_start": 70,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D13"
      ]
    },
    {
      "kind": "def",
      "name": "PlanckCharacter.toFloat",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/to-float/",
      "source_line_start": 84,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SectorLift",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/sector-lift/",
      "source_line_start": 101,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D15"
      ]
    },
    {
      "kind": "def",
      "name": "SectorLift.toFloat",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/to-float-l117/",
      "source_line_start": 117,
      "source_line_end": 125,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "lift_em",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/lift-em/",
      "source_line_start": 132,
      "source_line_end": 136,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "lift_weak",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/lift-weak/",
      "source_line_start": 139,
      "source_line_end": 143,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "lift_strong",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/lift-strong/",
      "source_line_start": 146,
      "source_line_end": 150,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "lift_gravity",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/lift-gravity/",
      "source_line_start": 153,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "lift_higgs",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/lift-higgs/",
      "source_line_start": 160,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_sector_lifts",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/all-sector-lifts/",
      "source_line_start": 167,
      "source_line_end": 168,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "UncertaintyProduct",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/uncertainty-product/",
      "source_line_start": 182,
      "source_line_end": 194,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D14"
      ]
    },
    {
      "kind": "def",
      "name": "UncertaintyProduct.product_numer",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/product-numer/",
      "source_line_start": 197,
      "source_line_end": 198,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "UncertaintyProduct.product_denom",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/product-denom/",
      "source_line_start": 201,
      "source_line_end": 202,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "PhysicalConstantsCore",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/physical-constants-core/",
      "source_line_start": 219,
      "source_line_end": 228,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R03"
      ]
    },
    {
      "kind": "def",
      "name": "physical_constants_core",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/physical-constants-core-l231/",
      "source_line_start": 231,
      "source_line_end": 231,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "planck_sigma_fixed",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/planck-sigma-fixed/",
      "source_line_start": 238,
      "source_line_end": 239,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T03"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_lifts_sigma_equivariant",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/all-lifts-sigma-equivariant/",
      "source_line_start": 242,
      "source_line_end": 244,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_sector_lifts",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/five-sector-lifts/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_lifts_ring_hom",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/all-lifts-ring-hom/",
      "source_line_start": 250,
      "source_line_end": 252,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "uncertainty_product_denom_pos",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/uncertainty-product-denom-pos/",
      "source_line_start": 255,
      "source_line_end": 257,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weak_lift_is_master",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/weak-lift-is-master/",
      "source_line_start": 260,
      "source_line_end": 262,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "em_lift_is_iota_squared",
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/em-lift-is-iota-squared/",
      "source_line_start": 265,
      "source_line_end": 268,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/eval-l274/",
      "source_line_start": 274,
      "source_line_end": 274,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/eval-l275/",
      "source_line_start": 275,
      "source_line_end": 275,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/eval-l276/",
      "source_line_start": 276,
      "source_line_end": 276,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/eval-l277/",
      "source_line_start": 277,
      "source_line_end": 277,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/eval-l278/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-planck-character/eval-l279/",
      "source_line_start": 279,
      "source_line_end": 281,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean",
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
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/PlanckCharacter.lean`
- SHA-256: `bff610f462ff10dad68d370b5e9aeabf6597f0adae178625a8c8f367b4fbd620`

## Registry Links

- `IV.D13` — Planck Character
- `IV.D14` — Uncertainty Product
- `IV.D15` — Sector Lift Functor
- `IV.R03` — Physical Constants Core
- `IV.T03` — Sector Lifts σ-Equivariant

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.QuantityFramework`
- `TauLib.BookIV.Sectors.SectorParameters`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.ActorsDynamics`
- `TauLib.BookIV.QuantumMechanics.Quantization`
- `TauLib.BookIV.QuantumMechanics.QuantumCharacters`

## Declaration Counts

- `def`: 11
- `eval`: 6
- `structure`: 4
- `theorem`: 7

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [PlanckCharacter](/corpus/taulib/docs/book-iv-physics-planck-character/planck-character/) | L70-L81 | type/data schema | type/data schema | `IV.D13` |
| `def` | [PlanckCharacter.toFloat](/corpus/taulib/docs/book-iv-physics-planck-character/to-float/) | L84-L85 | data/computed value | data/computed value | — |
| `structure` | [SectorLift](/corpus/taulib/docs/book-iv-physics-planck-character/sector-lift/) | L101-L114 | type/data schema | type/data schema | `IV.D15` |
| `def` | [SectorLift.toFloat](/corpus/taulib/docs/book-iv-physics-planck-character/to-float-l117/) | L117-L125 | data/computed value | data/computed value | — |
| `def` | [lift_em](/corpus/taulib/docs/book-iv-physics-planck-character/lift-em/) | L132-L136 | definition | definition | — |
| `def` | [lift_weak](/corpus/taulib/docs/book-iv-physics-planck-character/lift-weak/) | L139-L143 | definition | definition | — |
| `def` | [lift_strong](/corpus/taulib/docs/book-iv-physics-planck-character/lift-strong/) | L146-L150 | definition | definition | — |
| `def` | [lift_gravity](/corpus/taulib/docs/book-iv-physics-planck-character/lift-gravity/) | L153-L157 | definition | definition | — |
| `def` | [lift_higgs](/corpus/taulib/docs/book-iv-physics-planck-character/lift-higgs/) | L160-L164 | definition | definition | — |
| `def` | [all_sector_lifts](/corpus/taulib/docs/book-iv-physics-planck-character/all-sector-lifts/) | L167-L168 | data/computed value | data/computed value | — |
| `structure` | [UncertaintyProduct](/corpus/taulib/docs/book-iv-physics-planck-character/uncertainty-product/) | L182-L194 | type/data schema | type/data schema | `IV.D14` |
| `def` | [UncertaintyProduct.product_numer](/corpus/taulib/docs/book-iv-physics-planck-character/product-numer/) | L197-L198 | data/computed value | data/computed value | — |
| `def` | [UncertaintyProduct.product_denom](/corpus/taulib/docs/book-iv-physics-planck-character/product-denom/) | L201-L202 | data/computed value | data/computed value | — |
| `structure` | [PhysicalConstantsCore](/corpus/taulib/docs/book-iv-physics-planck-character/physical-constants-core/) | L219-L228 | type/data schema | type/data schema | `IV.R03` |
| `def` | [physical_constants_core](/corpus/taulib/docs/book-iv-physics-planck-character/physical-constants-core-l231/) | L231-L231 | definition | definition | — |
| `theorem` | [planck_sigma_fixed](/corpus/taulib/docs/book-iv-physics-planck-character/planck-sigma-fixed/) | L238-L239 | proof obligation | formal proof obligation checked | `IV.T03` |
| `theorem` | [all_lifts_sigma_equivariant](/corpus/taulib/docs/book-iv-physics-planck-character/all-lifts-sigma-equivariant/) | L242-L244 | proof obligation | formal proof obligation checked | — |
| `theorem` | [five_sector_lifts](/corpus/taulib/docs/book-iv-physics-planck-character/five-sector-lifts/) | L247-L247 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_lifts_ring_hom](/corpus/taulib/docs/book-iv-physics-planck-character/all-lifts-ring-hom/) | L250-L252 | proof obligation | formal proof obligation checked | — |
| `theorem` | [uncertainty_product_denom_pos](/corpus/taulib/docs/book-iv-physics-planck-character/uncertainty-product-denom-pos/) | L255-L257 | proof obligation | formal proof obligation checked | — |
| `theorem` | [weak_lift_is_master](/corpus/taulib/docs/book-iv-physics-planck-character/weak-lift-is-master/) | L260-L262 | proof obligation | formal proof obligation checked | — |
| `theorem` | [em_lift_is_iota_squared](/corpus/taulib/docs/book-iv-physics-planck-character/em-lift-is-iota-squared/) | L265-L268 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L274](/corpus/taulib/docs/book-iv-physics-planck-character/eval-l274/) | L274-L274 | computed check | computed check | — |
| `eval` | [#eval L275](/corpus/taulib/docs/book-iv-physics-planck-character/eval-l275/) | L275-L275 | computed check | computed check | — |
| `eval` | [#eval L276](/corpus/taulib/docs/book-iv-physics-planck-character/eval-l276/) | L276-L276 | computed check | computed check | — |
| `eval` | [#eval L277](/corpus/taulib/docs/book-iv-physics-planck-character/eval-l277/) | L277-L277 | computed check | computed check | — |
| `eval` | [#eval L278](/corpus/taulib/docs/book-iv-physics-planck-character/eval-l278/) | L278-L278 | computed check | computed check | — |
| `eval` | [#eval L279](/corpus/taulib/docs/book-iv-physics-planck-character/eval-l279/) | L279-L281 | computed check | computed check | — |

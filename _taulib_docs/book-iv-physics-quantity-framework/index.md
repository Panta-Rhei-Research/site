---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.QuantityFramework",
  "permalink": "/corpus/taulib/docs/book-iv-physics-quantity-framework/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.QuantityFramework`.",
  "module_name": "TauLib.BookIV.Physics.QuantityFramework",
  "module_slug": "book-iv-physics-quantity-framework",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/QuantityFramework.lean",
  "sha256": "db7f84fbb4ede9bf2e40e99be1e39a2b72be794ae1c89caab7d02932bc26e698",
  "imports": [
    "TauLib.BookIII.Sectors.Decomposition",
    "TauLib.BookI.Boundary.Iota"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.ActorsDynamics",
    "TauLib.BookIV.Physics.DefectFunctional",
    "TauLib.BookIV.Physics.MassEnergy",
    "TauLib.BookIV.Physics.PlanckCharacter",
    "TauLib.BookIV.Physics.TickUnits",
    "TauLib.BookV.Temporal.MacroReadout"
  ],
  "registry_ids": [
    "IV.D09",
    "IV.D10",
    "IV.D11",
    "IV.D12"
  ],
  "declaration_counts": {
    "inductive": 3,
    "structure": 2,
    "def": 14,
    "theorem": 8,
    "eval": 5
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "PrimaryInvariant",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/primary-invariant/",
      "source_line_start": 50,
      "source_line_end": 66,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D09"
      ]
    },
    {
      "kind": "inductive",
      "name": "CarrierType",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/carrier-type/",
      "source_line_start": 74,
      "source_line_end": 81,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D10"
      ]
    },
    {
      "kind": "structure",
      "name": "PhysicalQuantity",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/physical-quantity/",
      "source_line_start": 90,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D11"
      ]
    },
    {
      "kind": "inductive",
      "name": "ParticleKind",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/particle-kind/",
      "source_line_start": 111,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D12"
      ]
    },
    {
      "kind": "def",
      "name": "PrimaryInvariant.carrier",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/carrier/",
      "source_line_start": 128,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "PrimaryInvariant.sector",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/sector/",
      "source_line_start": 136,
      "source_line_end": 141,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "entropy_quantity",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/entropy-quantity/",
      "source_line_start": 148,
      "source_line_end": 154,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "time_quantity",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/time-quantity/",
      "source_line_start": 157,
      "source_line_end": 163,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "energy_quantity",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/energy-quantity/",
      "source_line_start": 166,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mass_quantity",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/mass-quantity/",
      "source_line_start": 175,
      "source_line_end": 181,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_quantity",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/gravity-quantity/",
      "source_line_start": 184,
      "source_line_end": 190,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_quantities",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/all-quantities/",
      "source_line_start": 193,
      "source_line_end": 194,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_invariants_exhaust",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/five-invariants-exhaust/",
      "source_line_start": 201,
      "source_line_end": 203,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_carriers_exhaust",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/three-carriers-exhaust/",
      "source_line_start": 206,
      "source_line_end": 208,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_particle_kinds",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/three-particle-kinds/",
      "source_line_start": 211,
      "source_line_end": 213,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gravity_unique_sigma_fixed_base",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/gravity-unique-sigma-fixed-base/",
      "source_line_start": 217,
      "source_line_end": 221,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "energy_mass_fiber",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/energy-mass-fiber/",
      "source_line_start": 224,
      "source_line_end": 226,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_quantities_distinct",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/all-quantities-distinct/",
      "source_line_start": 229,
      "source_line_end": 240,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l248/",
      "source_line_start": 248,
      "source_line_end": 248,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l249/",
      "source_line_start": 249,
      "source_line_end": 249,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InternalQuantity",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/internal-quantity/",
      "source_line_start": 264,
      "source_line_end": 279,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "time_internal",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/time-internal/",
      "source_line_start": 282,
      "source_line_end": 288,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "energy_internal",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/energy-internal/",
      "source_line_start": 291,
      "source_line_end": 297,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mass_internal",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/mass-internal/",
      "source_line_start": 300,
      "source_line_end": 306,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_internal",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/gravity-internal/",
      "source_line_start": 309,
      "source_line_end": 315,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "entropy_internal",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/entropy-internal/",
      "source_line_start": 318,
      "source_line_end": 324,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_internal_quantities",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/all-internal-quantities/",
      "source_line_start": 327,
      "source_line_end": 328,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "categorical_consistent_with_metadata",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/categorical-consistent-with-metadata/",
      "source_line_start": 332,
      "source_line_end": 338,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "internal_generators_distinct",
      "url": "/corpus/taulib/docs/book-iv-physics-quantity-framework/internal-generators-distinct/",
      "source_line_start": 341,
      "source_line_end": 354,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean",
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
- Source path: [`TauLib/BookIV/Physics/QuantityFramework.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/QuantityFramework.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/QuantityFramework.lean`
- SHA-256: `db7f84fbb4ede9bf2e40e99be1e39a2b72be794ae1c89caab7d02932bc26e698`

## Registry Links

- `IV.D09` — Primary Invariant
- `IV.D10` — Carrier Type
- `IV.D11` — Physical Quantity Template
- `IV.D12` — Particle Kind

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Sectors.Decomposition`
- `TauLib.BookI.Boundary.Iota`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.ActorsDynamics`
- `TauLib.BookIV.Physics.DefectFunctional`
- `TauLib.BookIV.Physics.MassEnergy`
- `TauLib.BookIV.Physics.PlanckCharacter`
- `TauLib.BookIV.Physics.TickUnits`
- `TauLib.BookV.Temporal.MacroReadout`

## Declaration Counts

- `def`: 14
- `eval`: 5
- `inductive`: 3
- `structure`: 2
- `theorem`: 8

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [PrimaryInvariant](/corpus/taulib/docs/book-iv-physics-quantity-framework/primary-invariant/) | L50-L66 | type/data schema | type/data schema | `IV.D09` |
| `inductive` | [CarrierType](/corpus/taulib/docs/book-iv-physics-quantity-framework/carrier-type/) | L74-L81 | type/data schema | type/data schema | `IV.D10` |
| `structure` | [PhysicalQuantity](/corpus/taulib/docs/book-iv-physics-quantity-framework/physical-quantity/) | L90-L103 | type/data schema | type/data schema | `IV.D11` |
| `inductive` | [ParticleKind](/corpus/taulib/docs/book-iv-physics-quantity-framework/particle-kind/) | L111-L121 | type/data schema | type/data schema | `IV.D12` |
| `def` | [PrimaryInvariant.carrier](/corpus/taulib/docs/book-iv-physics-quantity-framework/carrier/) | L128-L133 | definition | definition | — |
| `def` | [PrimaryInvariant.sector](/corpus/taulib/docs/book-iv-physics-quantity-framework/sector/) | L136-L141 | definition | definition | — |
| `def` | [entropy_quantity](/corpus/taulib/docs/book-iv-physics-quantity-framework/entropy-quantity/) | L148-L154 | definition | definition | — |
| `def` | [time_quantity](/corpus/taulib/docs/book-iv-physics-quantity-framework/time-quantity/) | L157-L163 | definition | definition | — |
| `def` | [energy_quantity](/corpus/taulib/docs/book-iv-physics-quantity-framework/energy-quantity/) | L166-L172 | definition | definition | — |
| `def` | [mass_quantity](/corpus/taulib/docs/book-iv-physics-quantity-framework/mass-quantity/) | L175-L181 | definition | definition | — |
| `def` | [gravity_quantity](/corpus/taulib/docs/book-iv-physics-quantity-framework/gravity-quantity/) | L184-L190 | definition | definition | — |
| `def` | [all_quantities](/corpus/taulib/docs/book-iv-physics-quantity-framework/all-quantities/) | L193-L194 | data/computed value | data/computed value | — |
| `theorem` | [five_invariants_exhaust](/corpus/taulib/docs/book-iv-physics-quantity-framework/five-invariants-exhaust/) | L201-L203 | proof obligation | formal proof obligation checked | — |
| `theorem` | [three_carriers_exhaust](/corpus/taulib/docs/book-iv-physics-quantity-framework/three-carriers-exhaust/) | L206-L208 | proof obligation | formal proof obligation checked | — |
| `theorem` | [three_particle_kinds](/corpus/taulib/docs/book-iv-physics-quantity-framework/three-particle-kinds/) | L211-L213 | proof obligation | formal proof obligation checked | — |
| `theorem` | [gravity_unique_sigma_fixed_base](/corpus/taulib/docs/book-iv-physics-quantity-framework/gravity-unique-sigma-fixed-base/) | L217-L221 | proof obligation | formal proof obligation checked | — |
| `theorem` | [energy_mass_fiber](/corpus/taulib/docs/book-iv-physics-quantity-framework/energy-mass-fiber/) | L224-L226 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_quantities_distinct](/corpus/taulib/docs/book-iv-physics-quantity-framework/all-quantities-distinct/) | L229-L240 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L246](/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l246/) | L246-L246 | computed check | computed check | — |
| `eval` | [#eval L247](/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l247/) | L247-L247 | computed check | computed check | — |
| `eval` | [#eval L248](/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l248/) | L248-L248 | computed check | computed check | — |
| `eval` | [#eval L249](/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l249/) | L249-L249 | computed check | computed check | — |
| `eval` | [#eval L250](/corpus/taulib/docs/book-iv-physics-quantity-framework/eval-l250/) | L250-L250 | computed check | computed check | — |
| `structure` | [InternalQuantity](/corpus/taulib/docs/book-iv-physics-quantity-framework/internal-quantity/) | L264-L279 | type/data schema | type/data schema | — |
| `def` | [time_internal](/corpus/taulib/docs/book-iv-physics-quantity-framework/time-internal/) | L282-L288 | data/computed value | data/computed value | — |
| `def` | [energy_internal](/corpus/taulib/docs/book-iv-physics-quantity-framework/energy-internal/) | L291-L297 | data/computed value | data/computed value | — |
| `def` | [mass_internal](/corpus/taulib/docs/book-iv-physics-quantity-framework/mass-internal/) | L300-L306 | data/computed value | data/computed value | — |
| `def` | [gravity_internal](/corpus/taulib/docs/book-iv-physics-quantity-framework/gravity-internal/) | L309-L315 | data/computed value | data/computed value | — |
| `def` | [entropy_internal](/corpus/taulib/docs/book-iv-physics-quantity-framework/entropy-internal/) | L318-L324 | data/computed value | data/computed value | — |
| `def` | [all_internal_quantities](/corpus/taulib/docs/book-iv-physics-quantity-framework/all-internal-quantities/) | L327-L328 | data/computed value | data/computed value | — |
| `theorem` | [categorical_consistent_with_metadata](/corpus/taulib/docs/book-iv-physics-quantity-framework/categorical-consistent-with-metadata/) | L332-L338 | proof obligation | formal proof obligation checked | — |
| `theorem` | [internal_generators_distinct](/corpus/taulib/docs/book-iv-physics-quantity-framework/internal-generators-distinct/) | L341-L354 | proof obligation | formal proof obligation checked | — |

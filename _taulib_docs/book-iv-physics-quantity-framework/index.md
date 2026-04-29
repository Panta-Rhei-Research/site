---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.QuantityFramework",
  "permalink": "/verify/taulib/docs/book-iv-physics-quantity-framework/",
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
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/primary-invariant/",
      "source_line_start": 50,
      "source_line_end": 66,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D09"
      ]
    },
    {
      "kind": "inductive",
      "name": "CarrierType",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/carrier-type/",
      "source_line_start": 74,
      "source_line_end": 81,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D10"
      ]
    },
    {
      "kind": "structure",
      "name": "PhysicalQuantity",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/physical-quantity/",
      "source_line_start": 90,
      "source_line_end": 103,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D11"
      ]
    },
    {
      "kind": "inductive",
      "name": "ParticleKind",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/particle-kind/",
      "source_line_start": 111,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D12"
      ]
    },
    {
      "kind": "def",
      "name": "PrimaryInvariant.carrier",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/carrier/",
      "source_line_start": 128,
      "source_line_end": 133,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "PrimaryInvariant.sector",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/sector/",
      "source_line_start": 136,
      "source_line_end": 141,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "entropy_quantity",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/entropy-quantity/",
      "source_line_start": 148,
      "source_line_end": 154,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "time_quantity",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/time-quantity/",
      "source_line_start": 157,
      "source_line_end": 163,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "energy_quantity",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/energy-quantity/",
      "source_line_start": 166,
      "source_line_end": 172,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mass_quantity",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/mass-quantity/",
      "source_line_start": 175,
      "source_line_end": 181,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_quantity",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/gravity-quantity/",
      "source_line_start": 184,
      "source_line_end": 190,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_quantities",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/all-quantities/",
      "source_line_start": 193,
      "source_line_end": 194,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_invariants_exhaust",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/five-invariants-exhaust/",
      "source_line_start": 201,
      "source_line_end": 203,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_carriers_exhaust",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/three-carriers-exhaust/",
      "source_line_start": 206,
      "source_line_end": 208,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "three_particle_kinds",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/three-particle-kinds/",
      "source_line_start": 211,
      "source_line_end": 213,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gravity_unique_sigma_fixed_base",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/gravity-unique-sigma-fixed-base/",
      "source_line_start": 217,
      "source_line_end": 221,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "energy_mass_fiber",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/energy-mass-fiber/",
      "source_line_start": 224,
      "source_line_end": 226,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_quantities_distinct",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/all-quantities-distinct/",
      "source_line_start": 229,
      "source_line_end": 240,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l248/",
      "source_line_start": 248,
      "source_line_end": 248,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l249/",
      "source_line_start": 249,
      "source_line_end": 249,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InternalQuantity",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/internal-quantity/",
      "source_line_start": 264,
      "source_line_end": 279,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "time_internal",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/time-internal/",
      "source_line_start": 282,
      "source_line_end": 288,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "energy_internal",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/energy-internal/",
      "source_line_start": 291,
      "source_line_end": 297,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mass_internal",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/mass-internal/",
      "source_line_start": 300,
      "source_line_end": 306,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_internal",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/gravity-internal/",
      "source_line_start": 309,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "entropy_internal",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/entropy-internal/",
      "source_line_start": 318,
      "source_line_end": 324,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_internal_quantities",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/all-internal-quantities/",
      "source_line_start": 327,
      "source_line_end": 328,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "categorical_consistent_with_metadata",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/categorical-consistent-with-metadata/",
      "source_line_start": 332,
      "source_line_end": 338,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "internal_generators_distinct",
      "url": "/verify/taulib/docs/book-iv-physics-quantity-framework/internal-generators-distinct/",
      "source_line_start": 341,
      "source_line_end": 354,
      "formal_status": "formalized",
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `inductive` | [PrimaryInvariant](/verify/taulib/docs/book-iv-physics-quantity-framework/primary-invariant/) | L50-L66 | defined | `IV.D09` |
| `inductive` | [CarrierType](/verify/taulib/docs/book-iv-physics-quantity-framework/carrier-type/) | L74-L81 | defined | `IV.D10` |
| `structure` | [PhysicalQuantity](/verify/taulib/docs/book-iv-physics-quantity-framework/physical-quantity/) | L90-L103 | defined | `IV.D11` |
| `inductive` | [ParticleKind](/verify/taulib/docs/book-iv-physics-quantity-framework/particle-kind/) | L111-L121 | defined | `IV.D12` |
| `def` | [PrimaryInvariant.carrier](/verify/taulib/docs/book-iv-physics-quantity-framework/carrier/) | L128-L133 | defined | — |
| `def` | [PrimaryInvariant.sector](/verify/taulib/docs/book-iv-physics-quantity-framework/sector/) | L136-L141 | defined | — |
| `def` | [entropy_quantity](/verify/taulib/docs/book-iv-physics-quantity-framework/entropy-quantity/) | L148-L154 | defined | — |
| `def` | [time_quantity](/verify/taulib/docs/book-iv-physics-quantity-framework/time-quantity/) | L157-L163 | defined | — |
| `def` | [energy_quantity](/verify/taulib/docs/book-iv-physics-quantity-framework/energy-quantity/) | L166-L172 | defined | — |
| `def` | [mass_quantity](/verify/taulib/docs/book-iv-physics-quantity-framework/mass-quantity/) | L175-L181 | defined | — |
| `def` | [gravity_quantity](/verify/taulib/docs/book-iv-physics-quantity-framework/gravity-quantity/) | L184-L190 | defined | — |
| `def` | [all_quantities](/verify/taulib/docs/book-iv-physics-quantity-framework/all-quantities/) | L193-L194 | defined | — |
| `theorem` | [five_invariants_exhaust](/verify/taulib/docs/book-iv-physics-quantity-framework/five-invariants-exhaust/) | L201-L203 | formalized | — |
| `theorem` | [three_carriers_exhaust](/verify/taulib/docs/book-iv-physics-quantity-framework/three-carriers-exhaust/) | L206-L208 | formalized | — |
| `theorem` | [three_particle_kinds](/verify/taulib/docs/book-iv-physics-quantity-framework/three-particle-kinds/) | L211-L213 | formalized | — |
| `theorem` | [gravity_unique_sigma_fixed_base](/verify/taulib/docs/book-iv-physics-quantity-framework/gravity-unique-sigma-fixed-base/) | L217-L221 | formalized | — |
| `theorem` | [energy_mass_fiber](/verify/taulib/docs/book-iv-physics-quantity-framework/energy-mass-fiber/) | L224-L226 | formalized | — |
| `theorem` | [all_quantities_distinct](/verify/taulib/docs/book-iv-physics-quantity-framework/all-quantities-distinct/) | L229-L240 | formalized | — |
| `eval` | [#eval L246](/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l246/) | L246-L246 | computed | — |
| `eval` | [#eval L247](/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l247/) | L247-L247 | computed | — |
| `eval` | [#eval L248](/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l248/) | L248-L248 | computed | — |
| `eval` | [#eval L249](/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l249/) | L249-L249 | computed | — |
| `eval` | [#eval L250](/verify/taulib/docs/book-iv-physics-quantity-framework/eval-l250/) | L250-L250 | computed | — |
| `structure` | [InternalQuantity](/verify/taulib/docs/book-iv-physics-quantity-framework/internal-quantity/) | L264-L279 | defined | — |
| `def` | [time_internal](/verify/taulib/docs/book-iv-physics-quantity-framework/time-internal/) | L282-L288 | defined | — |
| `def` | [energy_internal](/verify/taulib/docs/book-iv-physics-quantity-framework/energy-internal/) | L291-L297 | defined | — |
| `def` | [mass_internal](/verify/taulib/docs/book-iv-physics-quantity-framework/mass-internal/) | L300-L306 | defined | — |
| `def` | [gravity_internal](/verify/taulib/docs/book-iv-physics-quantity-framework/gravity-internal/) | L309-L315 | defined | — |
| `def` | [entropy_internal](/verify/taulib/docs/book-iv-physics-quantity-framework/entropy-internal/) | L318-L324 | defined | — |
| `def` | [all_internal_quantities](/verify/taulib/docs/book-iv-physics-quantity-framework/all-internal-quantities/) | L327-L328 | defined | — |
| `theorem` | [categorical_consistent_with_metadata](/verify/taulib/docs/book-iv-physics-quantity-framework/categorical-consistent-with-metadata/) | L332-L338 | formalized | — |
| `theorem` | [internal_generators_distinct](/verify/taulib/docs/book-iv-physics-quantity-framework/internal-generators-distinct/) | L341-L354 | formalized | — |

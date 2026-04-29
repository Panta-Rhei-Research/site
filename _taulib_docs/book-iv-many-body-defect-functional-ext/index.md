---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_slug": "book-iv-many-body-defect-functional-ext",
  "book": "BookIV",
  "family": "ManyBody",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean",
  "sha256": "51087c9e28d1c5e135ff1c7c93c2d16e66ba15afdc195d6b16004a95d986105b",
  "imports": [
    "TauLib.BookIV.Strong.VacuumCatastrophe"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.ManyBody.DefectFunctionalExt2"
  ],
  "registry_ids": [
    "IV.D210",
    "IV.D211",
    "IV.D212",
    "IV.D213",
    "IV.D214",
    "IV.D215",
    "IV.D216",
    "IV.D217",
    "IV.D218",
    "IV.D219",
    "IV.D220",
    "IV.D221",
    "IV.P133",
    "IV.P134",
    "IV.P135",
    "IV.R155",
    "IV.R156",
    "IV.R157",
    "IV.R158",
    "IV.R159",
    "IV.R160",
    "IV.T89",
    "IV.T90"
  ],
  "declaration_counts": {
    "structure": 17,
    "def": 11,
    "theorem": 11,
    "eval": 11
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "TopologicalIntegralityOfTheta",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-integrality-of-theta/",
      "source_line_start": 66,
      "source_line_end": 73,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P133"
      ]
    },
    {
      "kind": "def",
      "name": "topological_integrality",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-integrality/",
      "source_line_start": 75,
      "source_line_end": 75,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "theta_integer_valued",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/theta-integer-valued/",
      "source_line_start": 77,
      "source_line_end": 78,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "remark_euler_budget_recap",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/remark-euler-budget-recap/",
      "source_line_start": 88,
      "source_line_end": 90,
      "formal_status": "defined",
      "registry_ids": [
        "IV.R155"
      ]
    },
    {
      "kind": "structure",
      "name": "MacroscopicDefectTuple",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-defect-tuple/",
      "source_line_start": 104,
      "source_line_end": 123,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D210"
      ]
    },
    {
      "kind": "def",
      "name": "MacroscopicDefectTuple.effectiveMobility",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/effective-mobility/",
      "source_line_start": 126,
      "source_line_end": 127,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "MacroscopicMobility",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-mobility/",
      "source_line_start": 136,
      "source_line_end": 141,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D211"
      ]
    },
    {
      "kind": "structure",
      "name": "MacroscopicVorticity",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-vorticity/",
      "source_line_start": 146,
      "source_line_end": 153,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D212"
      ]
    },
    {
      "kind": "structure",
      "name": "MacroscopicCompression",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-compression/",
      "source_line_start": 158,
      "source_line_end": 165,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D213"
      ]
    },
    {
      "kind": "structure",
      "name": "TotalTopologicalCharge",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/total-topological-charge/",
      "source_line_start": 170,
      "source_line_end": 179,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D214"
      ]
    },
    {
      "kind": "theorem",
      "name": "topological_charge_no_interaction",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-charge-no-interaction/",
      "source_line_start": 181,
      "source_line_end": 183,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "topological_charge_no_averaging",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-charge-no-averaging/",
      "source_line_start": 185,
      "source_line_end": 187,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TopologicalChargeConservation",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-charge-conservation/",
      "source_line_start": 197,
      "source_line_end": 204,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P134"
      ]
    },
    {
      "kind": "structure",
      "name": "ClopenCylinderAtDepthN",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/clopen-cylinder-at-depth-n/",
      "source_line_start": 214,
      "source_line_end": 225,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D215"
      ]
    },
    {
      "kind": "structure",
      "name": "LevelnDefectFunctional",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/leveln-defect-functional/",
      "source_line_start": 239,
      "source_line_end": 248,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D216"
      ]
    },
    {
      "kind": "structure",
      "name": "TowerCompatibility",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/tower-compatibility/",
      "source_line_start": 264,
      "source_line_end": 271,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T89"
      ]
    },
    {
      "kind": "def",
      "name": "tower_compatibility",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/tower-compatibility-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tower_restriction_recovers",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/tower-restriction-recovers/",
      "source_line_start": 275,
      "source_line_end": 276,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SectorAdditivity",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/sector-additivity/",
      "source_line_start": 289,
      "source_line_end": 298,
      "formal_status": "defined",
      "registry_ids": [
        "IV.T90"
      ]
    },
    {
      "kind": "def",
      "name": "sector_additivity",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/sector-additivity-l300/",
      "source_line_start": 300,
      "source_line_end": 300,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "five_sector_summands",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/five-sector-summands/",
      "source_line_start": 302,
      "source_line_end": 303,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_additivity_count",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/sector-additivity-count/",
      "source_line_start": 305,
      "source_line_end": 306,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "UniversalDefectFunctional",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/universal-defect-functional/",
      "source_line_start": 320,
      "source_line_end": 329,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D217"
      ]
    },
    {
      "kind": "def",
      "name": "universal_defect_functional",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/universal-defect-functional-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ExistenceAndUniquenessOfLimit",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/existence-and-uniqueness-of-limit/",
      "source_line_start": 341,
      "source_line_end": 348,
      "formal_status": "defined",
      "registry_ids": [
        "IV.P135"
      ]
    },
    {
      "kind": "def",
      "name": "existence_uniqueness",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/existence-uniqueness/",
      "source_line_start": 350,
      "source_line_end": 350,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "limit_exists",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/limit-exists/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "limit_unique",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/limit-unique/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "DefectTupleSpace",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/defect-tuple-space/",
      "source_line_start": 364,
      "source_line_end": 375,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D218"
      ]
    },
    {
      "kind": "def",
      "name": "defect_tuple_space",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/defect-tuple-space-l377/",
      "source_line_start": 377,
      "source_line_end": 377,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_tuple_components",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/four-tuple-components/",
      "source_line_start": 379,
      "source_line_end": 380,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CriticalMobilityThreshold",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/critical-mobility-threshold/",
      "source_line_start": 390,
      "source_line_end": 399,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D219"
      ]
    },
    {
      "kind": "def",
      "name": "critical_mobility",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/critical-mobility/",
      "source_line_start": 401,
      "source_line_end": 401,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CrystalRegime",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/crystal-regime/",
      "source_line_start": 410,
      "source_line_end": 421,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D220"
      ]
    },
    {
      "kind": "def",
      "name": "crystal_regime",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/crystal-regime-l423/",
      "source_line_start": 423,
      "source_line_end": 423,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GlassRegime",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/glass-regime/",
      "source_line_start": 429,
      "source_line_end": 440,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D221"
      ]
    },
    {
      "kind": "def",
      "name": "glass_regime",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/glass-regime-l442/",
      "source_line_start": 442,
      "source_line_end": 442,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "crystal_all_arrested",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/crystal-all-arrested/",
      "source_line_start": 444,
      "source_line_end": 448,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "glass_compression_unfrozen",
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/glass-compression-unfrozen/",
      "source_line_start": 450,
      "source_line_end": 451,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l457/",
      "source_line_start": 457,
      "source_line_end": 457,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l458/",
      "source_line_start": 458,
      "source_line_end": 458,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l459/",
      "source_line_start": 459,
      "source_line_end": 459,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l460/",
      "source_line_start": 460,
      "source_line_end": 460,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l461/",
      "source_line_start": 461,
      "source_line_end": 461,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l462/",
      "source_line_start": 462,
      "source_line_end": 462,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l463/",
      "source_line_start": 463,
      "source_line_end": 463,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l464/",
      "source_line_start": 464,
      "source_line_end": 464,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l465/",
      "source_line_start": 465,
      "source_line_end": 465,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l466/",
      "source_line_start": 466,
      "source_line_end": 466,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l467/",
      "source_line_start": 467,
      "source_line_end": 469,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`
- SHA-256: `51087c9e28d1c5e135ff1c7c93c2d16e66ba15afdc195d6b16004a95d986105b`

## Registry Links

- `IV.D210` — Macroscopic defect tuple
- `IV.D211` — Macroscopic mobility
- `IV.D212` — Macroscopic vorticity
- `IV.D213` — Macroscopic compression
- `IV.D214` — Total topological charge
- `IV.D215` — Clopen cylinder at depth n
- `IV.D216` — Level-n defect functional
- `IV.D217` — Universal defect functional
- `IV.D218` — Defect tuple space
- `IV.D219` — Critical mobility threshold
- `IV.D220` — Crystal regime
- `IV.D221` — Glass regime
- `IV.P133` — Topological integrality of theta
- `IV.P134` — Topological charge conservation
- `IV.P135` — Existence and uniqueness of limit
- `IV.R155` — Euler budget recap
- `IV.R156` — Why interaction corrections matter
- `IV.R157` — Why clopen matters
- `IV.R158` — Finitely specified at each depth
- `IV.R159` — Ultrametric locality
- `IV.R160` — No continuum limit needed
- `IV.T89` — Tower compatibility
- `IV.T90` — Sector additivity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Strong.VacuumCatastrophe`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.ManyBody.DefectFunctionalExt2`

## Declaration Counts

- `def`: 11
- `eval`: 11
- `structure`: 17
- `theorem`: 11

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [TopologicalIntegralityOfTheta](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-integrality-of-theta/) | L66-L73 | defined | `IV.P133` |
| `def` | [topological_integrality](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-integrality/) | L75-L75 | defined | — |
| `theorem` | [theta_integer_valued](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/theta-integer-valued/) | L77-L78 | formalized | — |
| `def` | [remark_euler_budget_recap](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/remark-euler-budget-recap/) | L88-L90 | defined | `IV.R155` |
| `structure` | [MacroscopicDefectTuple](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-defect-tuple/) | L104-L123 | defined | `IV.D210` |
| `def` | [MacroscopicDefectTuple.effectiveMobility](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/effective-mobility/) | L126-L127 | defined | — |
| `structure` | [MacroscopicMobility](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-mobility/) | L136-L141 | defined | `IV.D211` |
| `structure` | [MacroscopicVorticity](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-vorticity/) | L146-L153 | defined | `IV.D212` |
| `structure` | [MacroscopicCompression](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-compression/) | L158-L165 | defined | `IV.D213` |
| `structure` | [TotalTopologicalCharge](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/total-topological-charge/) | L170-L179 | defined | `IV.D214` |
| `theorem` | [topological_charge_no_interaction](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-charge-no-interaction/) | L181-L183 | formalized | — |
| `theorem` | [topological_charge_no_averaging](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-charge-no-averaging/) | L185-L187 | formalized | — |
| `structure` | [TopologicalChargeConservation](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/topological-charge-conservation/) | L197-L204 | defined | `IV.P134` |
| `structure` | [ClopenCylinderAtDepthN](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/clopen-cylinder-at-depth-n/) | L214-L225 | defined | `IV.D215` |
| `structure` | [LevelnDefectFunctional](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/leveln-defect-functional/) | L239-L248 | defined | `IV.D216` |
| `structure` | [TowerCompatibility](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/tower-compatibility/) | L264-L271 | defined | `IV.T89` |
| `def` | [tower_compatibility](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/tower-compatibility-l273/) | L273-L273 | defined | — |
| `theorem` | [tower_restriction_recovers](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/tower-restriction-recovers/) | L275-L276 | formalized | — |
| `structure` | [SectorAdditivity](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/sector-additivity/) | L289-L298 | defined | `IV.T90` |
| `def` | [sector_additivity](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/sector-additivity-l300/) | L300-L300 | defined | — |
| `theorem` | [five_sector_summands](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/five-sector-summands/) | L302-L303 | formalized | — |
| `theorem` | [sector_additivity_count](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/sector-additivity-count/) | L305-L306 | formalized | — |
| `structure` | [UniversalDefectFunctional](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/universal-defect-functional/) | L320-L329 | defined | `IV.D217` |
| `def` | [universal_defect_functional](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/universal-defect-functional-l331/) | L331-L331 | defined | — |
| `structure` | [ExistenceAndUniquenessOfLimit](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/existence-and-uniqueness-of-limit/) | L341-L348 | defined | `IV.P135` |
| `def` | [existence_uniqueness](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/existence-uniqueness/) | L350-L350 | defined | — |
| `theorem` | [limit_exists](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/limit-exists/) | L352-L352 | formalized | — |
| `theorem` | [limit_unique](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/limit-unique/) | L353-L353 | formalized | — |
| `structure` | [DefectTupleSpace](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/defect-tuple-space/) | L364-L375 | defined | `IV.D218` |
| `def` | [defect_tuple_space](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/defect-tuple-space-l377/) | L377-L377 | defined | — |
| `theorem` | [four_tuple_components](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/four-tuple-components/) | L379-L380 | formalized | — |
| `structure` | [CriticalMobilityThreshold](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/critical-mobility-threshold/) | L390-L399 | defined | `IV.D219` |
| `def` | [critical_mobility](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/critical-mobility/) | L401-L401 | defined | — |
| `structure` | [CrystalRegime](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/crystal-regime/) | L410-L421 | defined | `IV.D220` |
| `def` | [crystal_regime](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/crystal-regime-l423/) | L423-L423 | defined | — |
| `structure` | [GlassRegime](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/glass-regime/) | L429-L440 | defined | `IV.D221` |
| `def` | [glass_regime](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/glass-regime-l442/) | L442-L442 | defined | — |
| `theorem` | [crystal_all_arrested](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/crystal-all-arrested/) | L444-L448 | formalized | — |
| `theorem` | [glass_compression_unfrozen](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/glass-compression-unfrozen/) | L450-L451 | formalized | — |
| `eval` | [#eval L457](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l457/) | L457-L457 | computed | — |
| `eval` | [#eval L458](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l458/) | L458-L458 | computed | — |
| `eval` | [#eval L459](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l459/) | L459-L459 | computed | — |
| `eval` | [#eval L460](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l460/) | L460-L460 | computed | — |
| `eval` | [#eval L461](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l461/) | L461-L461 | computed | — |
| `eval` | [#eval L462](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l462/) | L462-L462 | computed | — |
| `eval` | [#eval L463](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l463/) | L463-L463 | computed | — |
| `eval` | [#eval L464](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l464/) | L464-L464 | computed | — |
| `eval` | [#eval L465](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l465/) | L465-L465 | computed | — |
| `eval` | [#eval L466](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l466/) | L466-L466 | computed | — |
| `eval` | [#eval L467](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/eval-l467/) | L467-L469 | computed | — |

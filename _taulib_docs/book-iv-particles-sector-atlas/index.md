---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Particles.SectorAtlas",
  "permalink": "/corpus/taulib/docs/book-iv-particles-sector-atlas/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Particles.SectorAtlas`.",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_slug": "book-iv-particles-sector-atlas",
  "book": "BookIV",
  "family": "Particles",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Particles/SectorAtlas.lean",
  "sha256": "4c2fbc774b1a86e0867539b5d86c05e75cde32bb947a5340ce3f5dd3f470bf55",
  "imports": [
    "TauLib.BookIV.Strong.VacuumCatastrophe"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Particles.StrongCP",
    "TauLib.BookIV.Particles.ThreeGenerations"
  ],
  "registry_ids": [
    "IV.D194",
    "IV.D195",
    "IV.R106",
    "IV.R107",
    "IV.R108",
    "IV.R109",
    "IV.R110",
    "IV.T80",
    "IV.T81",
    "IV.T82"
  ],
  "declaration_counts": {
    "structure": 9,
    "def": 8,
    "theorem": 15,
    "inductive": 1,
    "eval": 9
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "ExactlyFourPrimitive",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-four-primitive/",
      "source_line_start": 56,
      "source_line_end": 65,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T80"
      ]
    },
    {
      "kind": "def",
      "name": "exactly_four_primitive_forces",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-four-primitive-forces/",
      "source_line_start": 67,
      "source_line_end": 67,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_primitive_count",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/four-primitive-count/",
      "source_line_start": 69,
      "source_line_end": 70,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "four_primitive_sectors",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/four-primitive-sectors/",
      "source_line_start": 72,
      "source_line_end": 73,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ExactlyOneDerived",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-one-derived/",
      "source_line_start": 86,
      "source_line_end": 97,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T81"
      ]
    },
    {
      "kind": "def",
      "name": "exactly_one_derived_sector",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-one-derived-sector/",
      "source_line_start": 99,
      "source_line_end": 99,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "one_derived_count",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/one-derived-count/",
      "source_line_start": 101,
      "source_line_end": 102,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "total_sector_count",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/total-sector-count/",
      "source_line_start": 105,
      "source_line_end": 107,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "GeneratorGroup",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/generator-group/",
      "source_line_start": 114,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CanonicalGenerator",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/canonical-generator/",
      "source_line_start": 128,
      "source_line_end": 135,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D194"
      ]
    },
    {
      "kind": "def",
      "name": "canonical_generator_set",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/canonical-generator-set/",
      "source_line_start": 138,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "IV.D194"
      ]
    },
    {
      "kind": "theorem",
      "name": "nine_generators",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/nine-generators/",
      "source_line_start": 153,
      "source_line_end": 153,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GeneratorAdequacy",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/generator-adequacy/",
      "source_line_start": 163,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.T82"
      ]
    },
    {
      "kind": "def",
      "name": "generator_adequacy",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/generator-adequacy-l174/",
      "source_line_start": 174,
      "source_line_end": 174,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "adequacy_count",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/adequacy-count/",
      "source_line_start": 176,
      "source_line_end": 176,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "is_adequate",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/is-adequate/",
      "source_line_start": 177,
      "source_line_end": 177,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "is_minimal",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/is-minimal/",
      "source_line_start": 178,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TauYukawaCoupling",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/tau-yukawa-coupling/",
      "source_line_start": 191,
      "source_line_end": 206,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D195"
      ]
    },
    {
      "kind": "structure",
      "name": "YukawaReadout",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-readout/",
      "source_line_start": 216,
      "source_line_end": 225,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R108"
      ]
    },
    {
      "kind": "def",
      "name": "yukawa_is_readout",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-is-readout/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "yukawa_span",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-span/",
      "source_line_start": 229,
      "source_line_end": 229,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "yukawa_not_free",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-not-free/",
      "source_line_start": 230,
      "source_line_end": 230,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ParameterComparison",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/parameter-comparison/",
      "source_line_start": 243,
      "source_line_end": 252,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R109"
      ]
    },
    {
      "kind": "def",
      "name": "sm_parameter_comparison",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/sm-parameter-comparison/",
      "source_line_start": 254,
      "source_line_end": 254,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sm_has_19",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/sm-has-19/",
      "source_line_start": 256,
      "source_line_end": 256,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "tau_one_constant",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/tau-one-constant/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "structural_plus_numerical",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/structural-plus-numerical/",
      "source_line_start": 258,
      "source_line_end": 261,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NoBSM",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/no-bsm/",
      "source_line_start": 272,
      "source_line_end": 283,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.R110"
      ]
    },
    {
      "kind": "def",
      "name": "no_bsm_particles",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/no-bsm-particles/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bsm_all_excluded",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/bsm-all-excluded/",
      "source_line_start": 287,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AtlasEntry",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/atlas-entry/",
      "source_line_start": 299,
      "source_line_end": 308,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sector_atlas",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/sector-atlas/",
      "source_line_start": 312,
      "source_line_end": 318,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "atlas_five_entries",
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/atlas-five-entries/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l326/",
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
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l327/",
      "source_line_start": 327,
      "source_line_end": 327,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l328/",
      "source_line_start": 328,
      "source_line_end": 328,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l329/",
      "source_line_start": 329,
      "source_line_end": 329,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l330/",
      "source_line_start": 330,
      "source_line_end": 330,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l331/",
      "source_line_start": 331,
      "source_line_end": 331,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 336,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean",
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
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Particles/SectorAtlas.lean`
- SHA-256: `4c2fbc774b1a86e0867539b5d86c05e75cde32bb947a5340ce3f5dd3f470bf55`

## Registry Links

- `IV.D194` — 9-element canonical generator set
- `IV.D195` — tau-Yukawa coupling
- `IV.R106` — Book III template vs Book IV instantiation
- `IV.R107` — Topological rigidity
- `IV.R108` — Yukawa as readout not parameter
- `IV.R109` — SM parameter count comparison
- `IV.R110` — No BSM particles
- `IV.T80` — Exactly four primitive forces (physical reading)
- `IV.T81` — Exactly one derived sector
- `IV.T82` — Generator adequacy and minimality

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Strong.VacuumCatastrophe`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Particles.StrongCP`
- `TauLib.BookIV.Particles.ThreeGenerations`

## Declaration Counts

- `def`: 8
- `eval`: 9
- `inductive`: 1
- `structure`: 9
- `theorem`: 15

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [ExactlyFourPrimitive](/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-four-primitive/) | L56-L65 | type/data schema | type/data schema | `IV.T80` |
| `def` | [exactly_four_primitive_forces](/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-four-primitive-forces/) | L67-L67 | definition | definition | — |
| `theorem` | [four_primitive_count](/corpus/taulib/docs/book-iv-particles-sector-atlas/four-primitive-count/) | L69-L70 | proof obligation | formal proof obligation checked | — |
| `theorem` | [four_primitive_sectors](/corpus/taulib/docs/book-iv-particles-sector-atlas/four-primitive-sectors/) | L72-L73 | proof obligation | formal proof obligation checked | — |
| `structure` | [ExactlyOneDerived](/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-one-derived/) | L86-L97 | type/data schema | type/data schema | `IV.T81` |
| `def` | [exactly_one_derived_sector](/corpus/taulib/docs/book-iv-particles-sector-atlas/exactly-one-derived-sector/) | L99-L99 | definition | definition | — |
| `theorem` | [one_derived_count](/corpus/taulib/docs/book-iv-particles-sector-atlas/one-derived-count/) | L101-L102 | proof obligation | formal proof obligation checked | — |
| `theorem` | [total_sector_count](/corpus/taulib/docs/book-iv-particles-sector-atlas/total-sector-count/) | L105-L107 | proof obligation | formal proof obligation checked | — |
| `inductive` | [GeneratorGroup](/corpus/taulib/docs/book-iv-particles-sector-atlas/generator-group/) | L114-L121 | type/data schema | type/data schema | — |
| `structure` | [CanonicalGenerator](/corpus/taulib/docs/book-iv-particles-sector-atlas/canonical-generator/) | L128-L135 | type/data schema | type/data schema | `IV.D194` |
| `def` | [canonical_generator_set](/corpus/taulib/docs/book-iv-particles-sector-atlas/canonical-generator-set/) | L138-L151 | data/computed value | data/computed value | `IV.D194` |
| `theorem` | [nine_generators](/corpus/taulib/docs/book-iv-particles-sector-atlas/nine-generators/) | L153-L153 | proof obligation | formal proof obligation checked | — |
| `structure` | [GeneratorAdequacy](/corpus/taulib/docs/book-iv-particles-sector-atlas/generator-adequacy/) | L163-L172 | type/data schema | type/data schema | `IV.T82` |
| `def` | [generator_adequacy](/corpus/taulib/docs/book-iv-particles-sector-atlas/generator-adequacy-l174/) | L174-L174 | definition | definition | — |
| `theorem` | [adequacy_count](/corpus/taulib/docs/book-iv-particles-sector-atlas/adequacy-count/) | L176-L176 | proof obligation | formal proof obligation checked | — |
| `theorem` | [is_adequate](/corpus/taulib/docs/book-iv-particles-sector-atlas/is-adequate/) | L177-L177 | proof obligation | formal proof obligation checked | — |
| `theorem` | [is_minimal](/corpus/taulib/docs/book-iv-particles-sector-atlas/is-minimal/) | L178-L178 | proof obligation | formal proof obligation checked | — |
| `structure` | [TauYukawaCoupling](/corpus/taulib/docs/book-iv-particles-sector-atlas/tau-yukawa-coupling/) | L191-L206 | type/data schema | type/data schema | `IV.D195` |
| `structure` | [YukawaReadout](/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-readout/) | L216-L225 | type/data schema | type/data schema | `IV.R108` |
| `def` | [yukawa_is_readout](/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-is-readout/) | L227-L227 | definition | definition | — |
| `theorem` | [yukawa_span](/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-span/) | L229-L229 | proof obligation | formal proof obligation checked | — |
| `theorem` | [yukawa_not_free](/corpus/taulib/docs/book-iv-particles-sector-atlas/yukawa-not-free/) | L230-L230 | proof obligation | formal proof obligation checked | — |
| `structure` | [ParameterComparison](/corpus/taulib/docs/book-iv-particles-sector-atlas/parameter-comparison/) | L243-L252 | type/data schema | type/data schema | `IV.R109` |
| `def` | [sm_parameter_comparison](/corpus/taulib/docs/book-iv-particles-sector-atlas/sm-parameter-comparison/) | L254-L254 | definition | definition | — |
| `theorem` | [sm_has_19](/corpus/taulib/docs/book-iv-particles-sector-atlas/sm-has-19/) | L256-L256 | proof obligation | formal proof obligation checked | — |
| `theorem` | [tau_one_constant](/corpus/taulib/docs/book-iv-particles-sector-atlas/tau-one-constant/) | L257-L257 | proof obligation | formal proof obligation checked | — |
| `theorem` | [structural_plus_numerical](/corpus/taulib/docs/book-iv-particles-sector-atlas/structural-plus-numerical/) | L258-L261 | proof obligation | formal proof obligation checked | — |
| `structure` | [NoBSM](/corpus/taulib/docs/book-iv-particles-sector-atlas/no-bsm/) | L272-L283 | type/data schema | type/data schema | `IV.R110` |
| `def` | [no_bsm_particles](/corpus/taulib/docs/book-iv-particles-sector-atlas/no-bsm-particles/) | L285-L285 | definition | definition | — |
| `theorem` | [bsm_all_excluded](/corpus/taulib/docs/book-iv-particles-sector-atlas/bsm-all-excluded/) | L287-L292 | proof obligation | formal proof obligation checked | — |
| `structure` | [AtlasEntry](/corpus/taulib/docs/book-iv-particles-sector-atlas/atlas-entry/) | L299-L308 | type/data schema | type/data schema | — |
| `def` | [sector_atlas](/corpus/taulib/docs/book-iv-particles-sector-atlas/sector-atlas/) | L312-L318 | data/computed value | data/computed value | — |
| `theorem` | [atlas_five_entries](/corpus/taulib/docs/book-iv-particles-sector-atlas/atlas-five-entries/) | L320-L320 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L326](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l326/) | L326-L326 | computed check | computed check | — |
| `eval` | [#eval L327](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l327/) | L327-L327 | computed check | computed check | — |
| `eval` | [#eval L328](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l328/) | L328-L328 | computed check | computed check | — |
| `eval` | [#eval L329](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l329/) | L329-L329 | computed check | computed check | — |
| `eval` | [#eval L330](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l330/) | L330-L330 | computed check | computed check | — |
| `eval` | [#eval L331](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l331/) | L331-L331 | computed check | computed check | — |
| `eval` | [#eval L332](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l332/) | L332-L332 | computed check | computed check | — |
| `eval` | [#eval L333](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l333/) | L333-L333 | computed check | computed check | — |
| `eval` | [#eval L334](/corpus/taulib/docs/book-iv-particles-sector-atlas/eval-l334/) | L334-L336 | computed check | computed check | — |

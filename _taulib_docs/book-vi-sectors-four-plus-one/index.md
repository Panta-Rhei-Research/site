---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVI.Sectors.FourPlusOne",
  "permalink": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVI.Sectors.FourPlusOne`.",
  "module_name": "TauLib.BookVI.Sectors.FourPlusOne",
  "module_slug": "book-vi-sectors-four-plus-one",
  "book": "BookVI",
  "family": "Sectors",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVI/Sectors/FourPlusOne.lean",
  "sha256": "ba72c148e554ee3f3b8fb097f97a87596d786299c2f5a33c831dbb14169faedc",
  "imports": [
    "TauLib.BookVI.Sectors.LifeLoop"
  ],
  "imported_by": [
    "TauLib.BookVI",
    "TauLib.BookVI.Agency.AgencySector",
    "TauLib.BookVI.Closure.ClosureSector",
    "TauLib.BookVI.Consumer.ConsumerMixer",
    "TauLib.BookVI.Persistence.PersistenceSector",
    "TauLib.BookVI.Sectors.Hallmarks",
    "TauLib.BookVI.Source.SourceSector",
    "TauLib.Tour.GuidedTour.BookVI",
    "TauLib.Tour.LifeFromPhysics"
  ],
  "registry_ids": [
    "VI.D15",
    "VI.D16",
    "VI.D17",
    "VI.D18",
    "VI.D19",
    "VI.D20",
    "VI.L05",
    "VI.T07"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 9,
    "theorem": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "LifeSector",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/life-sector/",
      "source_line_start": 22,
      "source_line_end": 26,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.D15"
      ]
    },
    {
      "kind": "def",
      "name": "persistence_sector",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/persistence-sector/",
      "source_line_start": 29,
      "source_line_end": 32,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "VI.D16"
      ]
    },
    {
      "kind": "def",
      "name": "agency_sector",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/agency-sector/",
      "source_line_start": 35,
      "source_line_end": 38,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "VI.D17"
      ]
    },
    {
      "kind": "def",
      "name": "source_sector",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/source-sector/",
      "source_line_start": 41,
      "source_line_end": 44,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "VI.D18"
      ]
    },
    {
      "kind": "def",
      "name": "closure_sector",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/closure-sector/",
      "source_line_start": 47,
      "source_line_end": 50,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "VI.D19"
      ]
    },
    {
      "kind": "def",
      "name": "consumer_sector",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/consumer-sector/",
      "source_line_start": 53,
      "source_line_end": 56,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "VI.D20"
      ]
    },
    {
      "kind": "def",
      "name": "all_sectors",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/all-sectors/",
      "source_line_start": 58,
      "source_line_end": 59,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "sector_count",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/sector-count/",
      "source_line_start": 61,
      "source_line_end": 61,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "primitive_sectors",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/primitive-sectors/",
      "source_line_start": 63,
      "source_line_end": 64,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "primitive_count",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/primitive-count/",
      "source_line_start": 66,
      "source_line_end": 66,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "GeneratorAdequacy",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/generator-adequacy/",
      "source_line_start": 69,
      "source_line_end": 74,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.T07"
      ]
    },
    {
      "kind": "def",
      "name": "gen_adequacy",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/gen-adequacy/",
      "source_line_start": 76,
      "source_line_end": 78,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "generator_adequacy_e2",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/generator-adequacy-e2/",
      "source_line_start": 80,
      "source_line_end": 84,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NeutronNoDist",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/neutron-no-dist/",
      "source_line_start": 87,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VI.L05"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_nd",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/neutron-nd/",
      "source_line_start": 92,
      "source_line_end": 94,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "neutron_nodist",
      "url": "/corpus/taulib/docs/book-vi-sectors-four-plus-one/neutron-nodist/",
      "source_line_start": 96,
      "source_line_end": 98,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean",
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
- Source path: [`TauLib/BookVI/Sectors/FourPlusOne.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVI/Sectors/FourPlusOne.lean`
- SHA-256: `ba72c148e554ee3f3b8fb097f97a87596d786299c2f5a33c831dbb14169faedc`

## Registry Links

- `VI.D15` — Life Sector
- `VI.D16` — Persistence Sector (α-base)
- `VI.D17` — Agency Sector (π-base)
- `VI.D18` — Source Sector (γ-fiber)
- `VI.D19` — Closure Sector (η-fiber)
- `VI.D20` — Consumer Mixed Sector (γ,η)
- `VI.L05` — Neutron NoDist
- `VI.T07` — Generator Adequacy at E₂

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVI.Sectors.LifeLoop`

## Imported By

- `TauLib.BookVI`
- `TauLib.BookVI.Agency.AgencySector`
- `TauLib.BookVI.Closure.ClosureSector`
- `TauLib.BookVI.Consumer.ConsumerMixer`
- `TauLib.BookVI.Persistence.PersistenceSector`
- `TauLib.BookVI.Sectors.Hallmarks`
- `TauLib.BookVI.Source.SourceSector`
- `TauLib.Tour.GuidedTour.BookVI`
- `TauLib.Tour.LifeFromPhysics`

## Declaration Counts

- `def`: 9
- `structure`: 3
- `theorem`: 4

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [LifeSector](/corpus/taulib/docs/book-vi-sectors-four-plus-one/life-sector/) | L22-L26 | type/data schema | type/data schema | `VI.D15` |
| `def` | [persistence_sector](/corpus/taulib/docs/book-vi-sectors-four-plus-one/persistence-sector/) | L29-L32 | definition | definition | `VI.D16` |
| `def` | [agency_sector](/corpus/taulib/docs/book-vi-sectors-four-plus-one/agency-sector/) | L35-L38 | definition | definition | `VI.D17` |
| `def` | [source_sector](/corpus/taulib/docs/book-vi-sectors-four-plus-one/source-sector/) | L41-L44 | definition | definition | `VI.D18` |
| `def` | [closure_sector](/corpus/taulib/docs/book-vi-sectors-four-plus-one/closure-sector/) | L47-L50 | definition | definition | `VI.D19` |
| `def` | [consumer_sector](/corpus/taulib/docs/book-vi-sectors-four-plus-one/consumer-sector/) | L53-L56 | definition | definition | `VI.D20` |
| `def` | [all_sectors](/corpus/taulib/docs/book-vi-sectors-four-plus-one/all-sectors/) | L58-L59 | data/computed value | data/computed value | — |
| `theorem` | [sector_count](/corpus/taulib/docs/book-vi-sectors-four-plus-one/sector-count/) | L61-L61 | proof obligation | formal proof obligation checked | — |
| `def` | [primitive_sectors](/corpus/taulib/docs/book-vi-sectors-four-plus-one/primitive-sectors/) | L63-L64 | data/computed value | data/computed value | — |
| `theorem` | [primitive_count](/corpus/taulib/docs/book-vi-sectors-four-plus-one/primitive-count/) | L66-L66 | proof obligation | formal proof obligation checked | — |
| `structure` | [GeneratorAdequacy](/corpus/taulib/docs/book-vi-sectors-four-plus-one/generator-adequacy/) | L69-L74 | type/data schema | type/data schema | `VI.T07` |
| `def` | [gen_adequacy](/corpus/taulib/docs/book-vi-sectors-four-plus-one/gen-adequacy/) | L76-L78 | definition | definition | — |
| `theorem` | [generator_adequacy_e2](/corpus/taulib/docs/book-vi-sectors-four-plus-one/generator-adequacy-e2/) | L80-L84 | proof obligation | formal proof obligation checked | — |
| `structure` | [NeutronNoDist](/corpus/taulib/docs/book-vi-sectors-four-plus-one/neutron-no-dist/) | L87-L90 | type/data schema | type/data schema | `VI.L05` |
| `def` | [neutron_nd](/corpus/taulib/docs/book-vi-sectors-four-plus-one/neutron-nd/) | L92-L94 | definition | definition | — |
| `theorem` | [neutron_nodist](/corpus/taulib/docs/book-vi-sectors-four-plus-one/neutron-nodist/) | L96-L98 | proof obligation | formal proof obligation checked | — |

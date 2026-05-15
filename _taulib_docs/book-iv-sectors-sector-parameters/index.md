---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Sectors.SectorParameters",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Sectors.SectorParameters`.",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_slug": "book-iv-sectors-sector-parameters",
  "book": "BookIV",
  "family": "Sectors",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Sectors/SectorParameters.lean",
  "sha256": "aaf5ac6254d50720f3edcd3c643fc89ac1e924d9ab6c15d1cfbf6605a48d7a28",
  "imports": [
    "TauLib.BookIII.Sectors.Decomposition",
    "TauLib.BookI.Boundary.Iota"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.CoherenceKernel",
    "TauLib.BookIV.Arena.Tau3Arena",
    "TauLib.BookIV.Physics.LemniscateCapacity",
    "TauLib.BookIV.Physics.PlanckCharacter",
    "TauLib.BookIV.Sectors.BoundaryFiltration",
    "TauLib.BookIV.Sectors.CouplingFormulas",
    "TauLib.BookV.Gravity.GravitationalConstant",
    "TauLib.BookV.GravityField.FrameHolonomy",
    "TauLib.BookV.Temporal.MacroReadout"
  ],
  "registry_ids": [
    "IV.D01",
    "IV.D02",
    "IV.D03",
    "IV.D04",
    "IV.D05",
    "IV.D06"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 1,
    "def": 12,
    "theorem": 5,
    "eval": 19
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "PolaritySign",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/polarity-sign/",
      "source_line_start": 57,
      "source_line_end": 66,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D01"
      ]
    },
    {
      "kind": "structure",
      "name": "SectorPhysics",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/sector-physics/",
      "source_line_start": 75,
      "source_line_end": 104,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D01"
      ]
    },
    {
      "kind": "def",
      "name": "iota_sq_numer",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-sq-numer/",
      "source_line_start": 107,
      "source_line_end": 107,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_sq_denom",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-sq-denom/",
      "source_line_start": 110,
      "source_line_end": 110,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_cu_numer",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-cu-numer/",
      "source_line_start": 113,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "iota_cu_denom",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-cu-denom/",
      "source_line_start": 116,
      "source_line_end": 116,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "em_sector",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/em-sector/",
      "source_line_start": 127,
      "source_line_end": 134,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D02"
      ]
    },
    {
      "kind": "def",
      "name": "strong_sector",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/strong-sector/",
      "source_line_start": 141,
      "source_line_end": 151,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D03"
      ]
    },
    {
      "kind": "def",
      "name": "higgs_sector",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/higgs-sector/",
      "source_line_start": 158,
      "source_line_end": 166,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D04"
      ]
    },
    {
      "kind": "def",
      "name": "gravity_sector",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/gravity-sector/",
      "source_line_start": 172,
      "source_line_end": 179,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D05"
      ]
    },
    {
      "kind": "def",
      "name": "weak_sector",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/weak-sector/",
      "source_line_start": 186,
      "source_line_end": 193,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.D06"
      ]
    },
    {
      "kind": "def",
      "name": "all_sectors",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/all-sectors/",
      "source_line_start": 199,
      "source_line_end": 200,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "sector_physics",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/sector-physics-l203/",
      "source_line_start": 203,
      "source_line_end": 209,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "gen_sector_injective",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/gen-sector-injective/",
      "source_line_start": 216,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "all_couplings_pos",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/all-couplings-pos/",
      "source_line_start": 223,
      "source_line_end": 230,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_depth_one",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/temporal-depth-one/",
      "source_line_start": 233,
      "source_line_end": 235,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "spatial_depth_ge_two",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/spatial-depth-ge-two/",
      "source_line_start": 237,
      "source_line_end": 239,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "weak_unique_balanced",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/weak-unique-balanced/",
      "source_line_start": 242,
      "source_line_end": 248,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "SectorPhysics.coupling_float",
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/coupling-float/",
      "source_line_start": 255,
      "source_line_end": 256,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l263/",
      "source_line_start": 263,
      "source_line_end": 263,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l266/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l267/",
      "source_line_start": 267,
      "source_line_end": 267,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l270/",
      "source_line_start": 270,
      "source_line_end": 270,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l271/",
      "source_line_start": 271,
      "source_line_end": 271,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l272/",
      "source_line_start": 272,
      "source_line_end": 272,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l274/",
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
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l277/",
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
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l278/",
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
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l279/",
      "source_line_start": 279,
      "source_line_end": 279,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l283/",
      "source_line_start": 283,
      "source_line_end": 283,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l284/",
      "source_line_start": 284,
      "source_line_end": 284,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l285/",
      "source_line_start": 285,
      "source_line_end": 285,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l286/",
      "source_line_start": 286,
      "source_line_end": 286,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l287/",
      "source_line_start": 287,
      "source_line_end": 289,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean",
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
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Sectors/SectorParameters.lean`
- SHA-256: `aaf5ac6254d50720f3edcd3c643fc89ac1e924d9ab6c15d1cfbf6605a48d7a28`

## Registry Links

- `IV.D01` — Sector Physics Template
- `IV.D02` — EM Sector at E₁
- `IV.D03` — Strong Sector at E₁
- `IV.D04` — Higgs Sector at E₁
- `IV.D05` — Gravity Sector at E₁
- `IV.D06` — Weak Sector at E₁

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIII.Sectors.Decomposition`
- `TauLib.BookI.Boundary.Iota`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.CoherenceKernel`
- `TauLib.BookIV.Arena.Tau3Arena`
- `TauLib.BookIV.Physics.LemniscateCapacity`
- `TauLib.BookIV.Physics.PlanckCharacter`
- `TauLib.BookIV.Sectors.BoundaryFiltration`
- `TauLib.BookIV.Sectors.CouplingFormulas`
- `TauLib.BookV.Gravity.GravitationalConstant`
- `TauLib.BookV.GravityField.FrameHolonomy`
- `TauLib.BookV.Temporal.MacroReadout`

## Declaration Counts

- `def`: 12
- `eval`: 19
- `inductive`: 1
- `structure`: 1
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [PolaritySign](/corpus/taulib/docs/book-iv-sectors-sector-parameters/polarity-sign/) | L57-L66 | type/data schema | type/data schema | `IV.D01` |
| `structure` | [SectorPhysics](/corpus/taulib/docs/book-iv-sectors-sector-parameters/sector-physics/) | L75-L104 | type/data schema | type/data schema | `IV.D01` |
| `def` | [iota_sq_numer](/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-sq-numer/) | L107-L107 | data/computed value | data/computed value | — |
| `def` | [iota_sq_denom](/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-sq-denom/) | L110-L110 | data/computed value | data/computed value | — |
| `def` | [iota_cu_numer](/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-cu-numer/) | L113-L113 | data/computed value | data/computed value | — |
| `def` | [iota_cu_denom](/corpus/taulib/docs/book-iv-sectors-sector-parameters/iota-cu-denom/) | L116-L116 | data/computed value | data/computed value | — |
| `def` | [em_sector](/corpus/taulib/docs/book-iv-sectors-sector-parameters/em-sector/) | L127-L134 | definition | definition | `IV.D02` |
| `def` | [strong_sector](/corpus/taulib/docs/book-iv-sectors-sector-parameters/strong-sector/) | L141-L151 | definition | definition | `IV.D03` |
| `def` | [higgs_sector](/corpus/taulib/docs/book-iv-sectors-sector-parameters/higgs-sector/) | L158-L166 | definition | definition | `IV.D04` |
| `def` | [gravity_sector](/corpus/taulib/docs/book-iv-sectors-sector-parameters/gravity-sector/) | L172-L179 | definition | definition | `IV.D05` |
| `def` | [weak_sector](/corpus/taulib/docs/book-iv-sectors-sector-parameters/weak-sector/) | L186-L193 | definition | definition | `IV.D06` |
| `def` | [all_sectors](/corpus/taulib/docs/book-iv-sectors-sector-parameters/all-sectors/) | L199-L200 | data/computed value | data/computed value | — |
| `def` | [sector_physics](/corpus/taulib/docs/book-iv-sectors-sector-parameters/sector-physics-l203/) | L203-L209 | definition | definition | — |
| `theorem` | [gen_sector_injective](/corpus/taulib/docs/book-iv-sectors-sector-parameters/gen-sector-injective/) | L216-L220 | proof obligation | formal proof obligation checked | — |
| `theorem` | [all_couplings_pos](/corpus/taulib/docs/book-iv-sectors-sector-parameters/all-couplings-pos/) | L223-L230 | proof obligation | formal proof obligation checked | — |
| `theorem` | [temporal_depth_one](/corpus/taulib/docs/book-iv-sectors-sector-parameters/temporal-depth-one/) | L233-L235 | proof obligation | formal proof obligation checked | — |
| `theorem` | [spatial_depth_ge_two](/corpus/taulib/docs/book-iv-sectors-sector-parameters/spatial-depth-ge-two/) | L237-L239 | proof obligation | formal proof obligation checked | — |
| `theorem` | [weak_unique_balanced](/corpus/taulib/docs/book-iv-sectors-sector-parameters/weak-unique-balanced/) | L242-L248 | proof obligation | formal proof obligation checked | — |
| `def` | [SectorPhysics.coupling_float](/corpus/taulib/docs/book-iv-sectors-sector-parameters/coupling-float/) | L255-L256 | data/computed value | data/computed value | — |
| `eval` | [#eval L263](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l263/) | L263-L263 | computed check | computed check | — |
| `eval` | [#eval L264](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l264/) | L264-L264 | computed check | computed check | — |
| `eval` | [#eval L265](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l265/) | L265-L265 | computed check | computed check | — |
| `eval` | [#eval L266](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l266/) | L266-L266 | computed check | computed check | — |
| `eval` | [#eval L267](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l267/) | L267-L267 | computed check | computed check | — |
| `eval` | [#eval L270](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l270/) | L270-L270 | computed check | computed check | — |
| `eval` | [#eval L271](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l271/) | L271-L271 | computed check | computed check | — |
| `eval` | [#eval L272](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l272/) | L272-L272 | computed check | computed check | — |
| `eval` | [#eval L273](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l273/) | L273-L273 | computed check | computed check | — |
| `eval` | [#eval L274](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l274/) | L274-L274 | computed check | computed check | — |
| `eval` | [#eval L277](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l277/) | L277-L277 | computed check | computed check | — |
| `eval` | [#eval L278](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l278/) | L278-L278 | computed check | computed check | — |
| `eval` | [#eval L279](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l279/) | L279-L279 | computed check | computed check | — |
| `eval` | [#eval L280](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l280/) | L280-L280 | computed check | computed check | — |
| `eval` | [#eval L283](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l283/) | L283-L283 | computed check | computed check | — |
| `eval` | [#eval L284](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l284/) | L284-L284 | computed check | computed check | — |
| `eval` | [#eval L285](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l285/) | L285-L285 | computed check | computed check | — |
| `eval` | [#eval L286](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l286/) | L286-L286 | computed check | computed check | — |
| `eval` | [#eval L287](/corpus/taulib/docs/book-iv-sectors-sector-parameters/eval-l287/) | L287-L289 | computed check | computed check | — |

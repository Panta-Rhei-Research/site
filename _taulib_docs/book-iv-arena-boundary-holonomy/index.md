---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "permalink": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Arena.BoundaryHolonomy`.",
  "module_name": "TauLib.BookIV.Arena.BoundaryHolonomy",
  "module_slug": "book-iv-arena-boundary-holonomy",
  "book": "BookIV",
  "family": "Arena",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Arena/BoundaryHolonomy.lean",
  "sha256": "7492b2621b4ce37e2e4530d231b15bd9b9adfb7189c6dd8505dceff7481e22ce",
  "imports": [
    "TauLib.BookIV.Arena.Tau3Arena"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Arena.FiveSectors",
    "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
    "TauLib.Tour.VerifyItYourself"
  ],
  "registry_ids": [
    "IV.D258",
    "IV.D259",
    "IV.D260",
    "IV.D261",
    "IV.D262",
    "IV.D263",
    "IV.P152",
    "IV.P153",
    "IV.R221",
    "IV.R222",
    "IV.T96",
    "IV.T97"
  ],
  "declaration_counts": {
    "structure": 6,
    "def": 3,
    "inductive": 1,
    "theorem": 3,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "YonedaSelfImage",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/yoneda-self-image/",
      "source_line_start": 42,
      "source_line_end": 49,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D258"
      ]
    },
    {
      "kind": "def",
      "name": "yoneda_self",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/yoneda-self/",
      "source_line_start": 52,
      "source_line_end": 91,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "IV.T96"
      ]
    },
    {
      "kind": "inductive",
      "name": "CharacterType",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/character-type/",
      "source_line_start": 100,
      "source_line_end": 103,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D259"
      ]
    },
    {
      "kind": "structure",
      "name": "BoundaryCharacter",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/boundary-character/",
      "source_line_start": 106,
      "source_line_end": 113,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BipolarDecomposition",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/bipolar-decomposition/",
      "source_line_start": 122,
      "source_line_end": 129,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D260"
      ]
    },
    {
      "kind": "theorem",
      "name": "sigma_fixed",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/sigma-fixed/",
      "source_line_start": 139,
      "source_line_end": 139,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P152"
      ]
    },
    {
      "kind": "structure",
      "name": "PhysConstCore",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/phys-const-core/",
      "source_line_start": 148,
      "source_line_end": 153,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D261"
      ]
    },
    {
      "kind": "def",
      "name": "phys_const_core",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/phys-const-core-l155/",
      "source_line_start": 155,
      "source_line_end": 158,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SectorLift",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/sector-lift/",
      "source_line_start": 166,
      "source_line_end": 172,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D262"
      ]
    },
    {
      "kind": "def",
      "name": "all_sector_lifts",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/all-sector-lifts/",
      "source_line_start": 175,
      "source_line_end": 177,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BoundaryChartReadout",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/boundary-chart-readout/",
      "source_line_start": 187,
      "source_line_end": 194,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D263"
      ]
    },
    {
      "kind": "theorem",
      "name": "smooth_from_coherent",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/smooth-from-coherent/",
      "source_line_start": 203,
      "source_line_end": 205,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P153"
      ]
    },
    {
      "kind": "theorem",
      "name": "boundary_triad",
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/boundary-triad/",
      "source_line_start": 217,
      "source_line_end": 226,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T97"
      ]
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l232/",
      "source_line_start": 232,
      "source_line_end": 232,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l233/",
      "source_line_start": 233,
      "source_line_end": 233,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l235/",
      "source_line_start": 235,
      "source_line_end": 237,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean",
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
- Source path: [`TauLib/BookIV/Arena/BoundaryHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/BoundaryHolonomy.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Arena/BoundaryHolonomy.lean`
- SHA-256: `7492b2621b4ce37e2e4530d231b15bd9b9adfb7189c6dd8505dceff7481e22ce`

## Registry Links

- `IV.D258` — Yoneda self-image
- `IV.D259` — Boundary character
- `IV.D260` — Bipolar decomposition of characters
- `IV.D261` — Physical-constants core
- `IV.D262` — Canonical sector lifts
- `IV.D263` — Chart readout homomorphism
- `IV.P152` — Master constant is sigma-fixed
- `IV.P153` — Smooth manifold from coherent readouts
- `IV.R221` — Why all lifts are rational
- `IV.R222` — Why 2 + 2 gives 1+
- `IV.T96` — Central Theorem --- physical form
- `IV.T97` — Boundary Triad Theorem

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Arena.Tau3Arena`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Arena.FiveSectors`
- `TauLib.BookIV.QuantumMechanics.CRAddressSpace`
- `TauLib.Tour.VerifyItYourself`

## Declaration Counts

- `def`: 3
- `eval`: 4
- `inductive`: 1
- `structure`: 6
- `theorem`: 3

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [YonedaSelfImage](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/yoneda-self-image/) | L42-L49 | type/data schema | type/data schema | `IV.D258` |
| `def` | [yoneda_self](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/yoneda-self/) | L52-L91 | definition | definition | `IV.T96` |
| `inductive` | [CharacterType](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/character-type/) | L100-L103 | type/data schema | type/data schema | `IV.D259` |
| `structure` | [BoundaryCharacter](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/boundary-character/) | L106-L113 | type/data schema | type/data schema | — |
| `structure` | [BipolarDecomposition](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/bipolar-decomposition/) | L122-L129 | type/data schema | type/data schema | `IV.D260` |
| `theorem` | [sigma_fixed](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/sigma-fixed/) | L139-L139 | proof obligation | formal proof obligation checked | `IV.P152` |
| `structure` | [PhysConstCore](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/phys-const-core/) | L148-L153 | type/data schema | type/data schema | `IV.D261` |
| `def` | [phys_const_core](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/phys-const-core-l155/) | L155-L158 | definition | definition | — |
| `structure` | [SectorLift](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/sector-lift/) | L166-L172 | type/data schema | type/data schema | `IV.D262` |
| `def` | [all_sector_lifts](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/all-sector-lifts/) | L175-L177 | data/computed value | data/computed value | — |
| `structure` | [BoundaryChartReadout](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/boundary-chart-readout/) | L187-L194 | type/data schema | type/data schema | `IV.D263` |
| `theorem` | [smooth_from_coherent](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/smooth-from-coherent/) | L203-L205 | proof obligation | formal proof obligation checked | `IV.P153` |
| `theorem` | [boundary_triad](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/boundary-triad/) | L217-L226 | proof obligation | formal proof obligation checked | `IV.T97` |
| `eval` | [#eval L232](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l232/) | L232-L232 | computed check | computed check | — |
| `eval` | [#eval L233](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l233/) | L233-L233 | computed check | computed check | — |
| `eval` | [#eval L234](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l234/) | L234-L234 | computed check | computed check | — |
| `eval` | [#eval L235](/corpus/taulib/docs/book-iv-arena-boundary-holonomy/eval-l235/) | L235-L237 | computed check | computed check | — |

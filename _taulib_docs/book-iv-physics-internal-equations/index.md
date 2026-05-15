---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.InternalEquations",
  "permalink": "/corpus/taulib/docs/book-iv-physics-internal-equations/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.InternalEquations`.",
  "module_name": "TauLib.BookIV.Physics.InternalEquations",
  "module_slug": "book-iv-physics-internal-equations",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/InternalEquations.lean",
  "sha256": "a3b5b28630161491bd9af9a5c1644f1ccb189b024e791ee647d3e2c245fd7761",
  "imports": [
    "TauLib.BookIV.Physics.TickUnits",
    "TauLib.BookIV.Calibration.MassRatioFormula"
  ],
  "imported_by": [
    "TauLib.BookIV",
    "TauLib.BookIV.Physics.ReadoutFunctor"
  ],
  "registry_ids": [
    "IV.D323",
    "IV.D324",
    "IV.P176",
    "IV.T127"
  ],
  "declaration_counts": {
    "inductive": 1,
    "structure": 1,
    "def": 5,
    "theorem": 5,
    "eval": 3
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "EquationLayer",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/equation-layer/",
      "source_line_start": 55,
      "source_line_end": 69,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D324"
      ]
    },
    {
      "kind": "structure",
      "name": "InternalIdentity",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/internal-identity/",
      "source_line_start": 82,
      "source_line_end": 95,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D323"
      ]
    },
    {
      "kind": "def",
      "name": "mass_ratio_identity",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/mass-ratio-identity/",
      "source_line_start": 104,
      "source_line_end": 110,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_identity",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/alpha-identity/",
      "source_line_start": 115,
      "source_line_end": 121,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_coupling_identity",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/gravity-coupling-identity/",
      "source_line_start": 127,
      "source_line_end": 133,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "temporal_complement_identity",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/temporal-complement-identity/",
      "source_line_start": 138,
      "source_line_end": 144,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "confinement_identity",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/confinement-identity/",
      "source_line_start": 149,
      "source_line_end": 155,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "internal_identity_dimensionless",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/internal-identity-dimensionless/",
      "source_line_start": 163,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P176"
      ]
    },
    {
      "kind": "theorem",
      "name": "mass_ratio_internal",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/mass-ratio-internal/",
      "source_line_start": 173,
      "source_line_end": 174,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T127"
      ]
    },
    {
      "kind": "theorem",
      "name": "all_from_iota",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/all-from-iota/",
      "source_line_start": 177,
      "source_line_end": 183,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mass_ratio_strong_sector",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/mass-ratio-strong-sector/",
      "source_line_start": 186,
      "source_line_end": 189,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "alpha_em_sector",
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/alpha-em-sector/",
      "source_line_start": 192,
      "source_line_end": 195,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/eval-l201/",
      "source_line_start": 201,
      "source_line_end": 201,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/eval-l202/",
      "source_line_start": 202,
      "source_line_end": 202,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-internal-equations/eval-l203/",
      "source_line_start": 203,
      "source_line_end": 205,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean",
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
- Source path: [`TauLib/BookIV/Physics/InternalEquations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/InternalEquations.lean`
- SHA-256: `a3b5b28630161491bd9af9a5c1644f1ccb189b024e791ee647d3e2c245fd7761`

## Registry Links

- `IV.D323` — Internal Identity
- `IV.D324` — Equation Layer
- `IV.P176` — Internal Equations Dimensionless
- `IV.T127` — Mass Ratio as Internal Identity

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.TickUnits`
- `TauLib.BookIV.Calibration.MassRatioFormula`

## Imported By

- `TauLib.BookIV`
- `TauLib.BookIV.Physics.ReadoutFunctor`

## Declaration Counts

- `def`: 5
- `eval`: 3
- `inductive`: 1
- `structure`: 1
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [EquationLayer](/corpus/taulib/docs/book-iv-physics-internal-equations/equation-layer/) | L55-L69 | type/data schema | type/data schema | `IV.D324` |
| `structure` | [InternalIdentity](/corpus/taulib/docs/book-iv-physics-internal-equations/internal-identity/) | L82-L95 | type/data schema | type/data schema | `IV.D323` |
| `def` | [mass_ratio_identity](/corpus/taulib/docs/book-iv-physics-internal-equations/mass-ratio-identity/) | L104-L110 | data/computed value | data/computed value | — |
| `def` | [alpha_identity](/corpus/taulib/docs/book-iv-physics-internal-equations/alpha-identity/) | L115-L121 | data/computed value | data/computed value | — |
| `def` | [gravity_coupling_identity](/corpus/taulib/docs/book-iv-physics-internal-equations/gravity-coupling-identity/) | L127-L133 | data/computed value | data/computed value | — |
| `def` | [temporal_complement_identity](/corpus/taulib/docs/book-iv-physics-internal-equations/temporal-complement-identity/) | L138-L144 | data/computed value | data/computed value | — |
| `def` | [confinement_identity](/corpus/taulib/docs/book-iv-physics-internal-equations/confinement-identity/) | L149-L155 | data/computed value | data/computed value | — |
| `theorem` | [internal_identity_dimensionless](/corpus/taulib/docs/book-iv-physics-internal-equations/internal-identity-dimensionless/) | L163-L169 | proof obligation | formal proof obligation checked | `IV.P176` |
| `theorem` | [mass_ratio_internal](/corpus/taulib/docs/book-iv-physics-internal-equations/mass-ratio-internal/) | L173-L174 | proof obligation | formal proof obligation checked | `IV.T127` |
| `theorem` | [all_from_iota](/corpus/taulib/docs/book-iv-physics-internal-equations/all-from-iota/) | L177-L183 | proof obligation | formal proof obligation checked | — |
| `theorem` | [mass_ratio_strong_sector](/corpus/taulib/docs/book-iv-physics-internal-equations/mass-ratio-strong-sector/) | L186-L189 | proof obligation | formal proof obligation checked | — |
| `theorem` | [alpha_em_sector](/corpus/taulib/docs/book-iv-physics-internal-equations/alpha-em-sector/) | L192-L195 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L201](/corpus/taulib/docs/book-iv-physics-internal-equations/eval-l201/) | L201-L201 | computed check | computed check | — |
| `eval` | [#eval L202](/corpus/taulib/docs/book-iv-physics-internal-equations/eval-l202/) | L202-L202 | computed check | computed check | — |
| `eval` | [#eval L203](/corpus/taulib/docs/book-iv-physics-internal-equations/eval-l203/) | L203-L205 | computed check | computed check | — |

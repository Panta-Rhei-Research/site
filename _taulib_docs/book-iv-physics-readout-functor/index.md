---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.ReadoutFunctor",
  "permalink": "/corpus/taulib/docs/book-iv-physics-readout-functor/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookIV.Physics.ReadoutFunctor`.",
  "module_name": "TauLib.BookIV.Physics.ReadoutFunctor",
  "module_slug": "book-iv-physics-readout-functor",
  "book": "BookIV",
  "family": "Physics",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookIV/Physics/ReadoutFunctor.lean",
  "sha256": "f7f359be0e1c9614d232e8b68ff3c313c36b9ef5510ab3d843979d7940d6caee",
  "imports": [
    "TauLib.BookIV.Physics.InternalEquations",
    "TauLib.BookIV.Calibration.SIReference"
  ],
  "imported_by": [
    "TauLib.BookIV"
  ],
  "registry_ids": [
    "IV.D325",
    "IV.D326",
    "IV.D327",
    "IV.P177",
    "IV.T128",
    "IV.T129"
  ],
  "declaration_counts": {
    "structure": 3,
    "def": 8,
    "theorem": 5,
    "eval": 4
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "MeasurementProcedure",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/measurement-procedure/",
      "source_line_start": 72,
      "source_line_end": 85,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D325"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutFunctor",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/readout-functor/",
      "source_line_start": 101,
      "source_line_end": 114,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D326"
      ]
    },
    {
      "kind": "def",
      "name": "readout",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/readout/",
      "source_line_start": 117,
      "source_line_end": 123,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReadoutAnchor",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/readout-anchor/",
      "source_line_start": 137,
      "source_line_end": 148,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "IV.D327"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_procedure",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/neutron-procedure/",
      "source_line_start": 151,
      "source_line_end": 157,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "readout_anchor",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/readout-anchor-l160/",
      "source_line_start": 160,
      "source_line_end": 165,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "electron_procedure",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/electron-procedure/",
      "source_line_start": 172,
      "source_line_end": 178,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_procedure",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/alpha-procedure/",
      "source_line_start": 181,
      "source_line_end": 187,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_procedure",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/gravity-procedure/",
      "source_line_start": 190,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "speed_of_light_procedure",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/speed-of-light-procedure/",
      "source_line_start": 199,
      "source_line_end": 205,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_procedures",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/all-procedures/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_preserves_identities",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/readout-preserves-identities/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T128"
      ]
    },
    {
      "kind": "theorem",
      "name": "single_anchor_sufficiency",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/single-anchor-sufficiency/",
      "source_line_start": 224,
      "source_line_end": 226,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.T129"
      ]
    },
    {
      "kind": "theorem",
      "name": "codomain_operational",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/codomain-operational/",
      "source_line_start": 230,
      "source_line_end": 235,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "IV.P177"
      ]
    },
    {
      "kind": "theorem",
      "name": "unique_anchor",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/unique-anchor/",
      "source_line_start": 238,
      "source_line_end": 241,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "anchor_is_neutron",
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/anchor-is-neutron/",
      "source_line_start": 244,
      "source_line_end": 245,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l251/",
      "source_line_start": 251,
      "source_line_end": 251,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l252/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "computed",
      "declaration_role": "computed check",
      "formal_status_label": "computed check",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 256,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean",
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
- Source path: [`TauLib/BookIV/Physics/ReadoutFunctor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookIV/Physics/ReadoutFunctor.lean`
- SHA-256: `f7f359be0e1c9614d232e8b68ff3c313c36b9ef5510ab3d843979d7940d6caee`

## Registry Links

- `IV.D325` — Measurement Procedure
- `IV.D326` — Readout Functor
- `IV.D327` — Readout Anchor
- `IV.P177` — Codomain Is Operational
- `IV.T128` — Readout Preserves Identities
- `IV.T129` — Single-Anchor Sufficiency

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookIV.Physics.InternalEquations`
- `TauLib.BookIV.Calibration.SIReference`

## Imported By

- `TauLib.BookIV`

## Declaration Counts

- `def`: 8
- `eval`: 4
- `structure`: 3
- `theorem`: 5

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [MeasurementProcedure](/corpus/taulib/docs/book-iv-physics-readout-functor/measurement-procedure/) | L72-L85 | type/data schema | type/data schema | `IV.D325` |
| `structure` | [ReadoutFunctor](/corpus/taulib/docs/book-iv-physics-readout-functor/readout-functor/) | L101-L114 | type/data schema | type/data schema | `IV.D326` |
| `def` | [readout](/corpus/taulib/docs/book-iv-physics-readout-functor/readout/) | L117-L123 | definition | definition | — |
| `structure` | [ReadoutAnchor](/corpus/taulib/docs/book-iv-physics-readout-functor/readout-anchor/) | L137-L148 | type/data schema | type/data schema | `IV.D327` |
| `def` | [neutron_procedure](/corpus/taulib/docs/book-iv-physics-readout-functor/neutron-procedure/) | L151-L157 | definition | definition | — |
| `def` | [readout_anchor](/corpus/taulib/docs/book-iv-physics-readout-functor/readout-anchor-l160/) | L160-L165 | definition | definition | — |
| `def` | [electron_procedure](/corpus/taulib/docs/book-iv-physics-readout-functor/electron-procedure/) | L172-L178 | definition | definition | — |
| `def` | [alpha_procedure](/corpus/taulib/docs/book-iv-physics-readout-functor/alpha-procedure/) | L181-L187 | definition | definition | — |
| `def` | [gravity_procedure](/corpus/taulib/docs/book-iv-physics-readout-functor/gravity-procedure/) | L190-L196 | definition | definition | — |
| `def` | [speed_of_light_procedure](/corpus/taulib/docs/book-iv-physics-readout-functor/speed-of-light-procedure/) | L199-L205 | definition | definition | — |
| `def` | [all_procedures](/corpus/taulib/docs/book-iv-physics-readout-functor/all-procedures/) | L208-L210 | data/computed value | data/computed value | — |
| `theorem` | [readout_preserves_identities](/corpus/taulib/docs/book-iv-physics-readout-functor/readout-preserves-identities/) | L219-L220 | proof obligation | formal proof obligation checked | `IV.T128` |
| `theorem` | [single_anchor_sufficiency](/corpus/taulib/docs/book-iv-physics-readout-functor/single-anchor-sufficiency/) | L224-L226 | proof obligation | formal proof obligation checked | `IV.T129` |
| `theorem` | [codomain_operational](/corpus/taulib/docs/book-iv-physics-readout-functor/codomain-operational/) | L230-L235 | proof obligation | formal proof obligation checked | `IV.P177` |
| `theorem` | [unique_anchor](/corpus/taulib/docs/book-iv-physics-readout-functor/unique-anchor/) | L238-L241 | proof obligation | formal proof obligation checked | — |
| `theorem` | [anchor_is_neutron](/corpus/taulib/docs/book-iv-physics-readout-functor/anchor-is-neutron/) | L244-L245 | proof obligation | formal proof obligation checked | — |
| `eval` | [#eval L251](/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l251/) | L251-L251 | computed check | computed check | — |
| `eval` | [#eval L252](/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l252/) | L252-L252 | computed check | computed check | — |
| `eval` | [#eval L253](/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l253/) | L253-L253 | computed check | computed check | — |
| `eval` | [#eval L254](/corpus/taulib/docs/book-iv-physics-readout-functor/eval-l254/) | L254-L256 | computed check | computed check | — |

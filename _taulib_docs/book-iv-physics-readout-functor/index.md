---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookIV.Physics.ReadoutFunctor",
  "permalink": "/verify/taulib/docs/book-iv-physics-readout-functor/",
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
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/measurement-procedure/",
      "source_line_start": 72,
      "source_line_end": 85,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D325"
      ]
    },
    {
      "kind": "structure",
      "name": "ReadoutFunctor",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/readout-functor/",
      "source_line_start": 101,
      "source_line_end": 114,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D326"
      ]
    },
    {
      "kind": "def",
      "name": "readout",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/readout/",
      "source_line_start": 117,
      "source_line_end": 123,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ReadoutAnchor",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/readout-anchor/",
      "source_line_start": 137,
      "source_line_end": 148,
      "formal_status": "defined",
      "registry_ids": [
        "IV.D327"
      ]
    },
    {
      "kind": "def",
      "name": "neutron_procedure",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/neutron-procedure/",
      "source_line_start": 151,
      "source_line_end": 157,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "readout_anchor",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/readout-anchor-l160/",
      "source_line_start": 160,
      "source_line_end": 165,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "electron_procedure",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/electron-procedure/",
      "source_line_start": 172,
      "source_line_end": 178,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "alpha_procedure",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/alpha-procedure/",
      "source_line_start": 181,
      "source_line_end": 187,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "gravity_procedure",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/gravity-procedure/",
      "source_line_start": 190,
      "source_line_end": 196,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "speed_of_light_procedure",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/speed-of-light-procedure/",
      "source_line_start": 199,
      "source_line_end": 205,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "all_procedures",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/all-procedures/",
      "source_line_start": 208,
      "source_line_end": 210,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "readout_preserves_identities",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/readout-preserves-identities/",
      "source_line_start": 219,
      "source_line_end": 220,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T128"
      ]
    },
    {
      "kind": "theorem",
      "name": "single_anchor_sufficiency",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/single-anchor-sufficiency/",
      "source_line_start": 224,
      "source_line_end": 226,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.T129"
      ]
    },
    {
      "kind": "theorem",
      "name": "codomain_operational",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/codomain-operational/",
      "source_line_start": 230,
      "source_line_end": 235,
      "formal_status": "formalized",
      "registry_ids": [
        "IV.P177"
      ]
    },
    {
      "kind": "theorem",
      "name": "unique_anchor",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/unique-anchor/",
      "source_line_start": 238,
      "source_line_end": 241,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "anchor_is_neutron",
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/anchor-is-neutron/",
      "source_line_start": 244,
      "source_line_end": 245,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/eval-l251/",
      "source_line_start": 251,
      "source_line_end": 251,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/eval-l252/",
      "source_line_start": 252,
      "source_line_end": 252,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/eval-l253/",
      "source_line_start": 253,
      "source_line_end": 253,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-iv-physics-readout-functor/eval-l254/",
      "source_line_start": 254,
      "source_line_end": 256,
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

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `structure` | [MeasurementProcedure](/verify/taulib/docs/book-iv-physics-readout-functor/measurement-procedure/) | L72-L85 | defined | `IV.D325` |
| `structure` | [ReadoutFunctor](/verify/taulib/docs/book-iv-physics-readout-functor/readout-functor/) | L101-L114 | defined | `IV.D326` |
| `def` | [readout](/verify/taulib/docs/book-iv-physics-readout-functor/readout/) | L117-L123 | defined | — |
| `structure` | [ReadoutAnchor](/verify/taulib/docs/book-iv-physics-readout-functor/readout-anchor/) | L137-L148 | defined | `IV.D327` |
| `def` | [neutron_procedure](/verify/taulib/docs/book-iv-physics-readout-functor/neutron-procedure/) | L151-L157 | defined | — |
| `def` | [readout_anchor](/verify/taulib/docs/book-iv-physics-readout-functor/readout-anchor-l160/) | L160-L165 | defined | — |
| `def` | [electron_procedure](/verify/taulib/docs/book-iv-physics-readout-functor/electron-procedure/) | L172-L178 | defined | — |
| `def` | [alpha_procedure](/verify/taulib/docs/book-iv-physics-readout-functor/alpha-procedure/) | L181-L187 | defined | — |
| `def` | [gravity_procedure](/verify/taulib/docs/book-iv-physics-readout-functor/gravity-procedure/) | L190-L196 | defined | — |
| `def` | [speed_of_light_procedure](/verify/taulib/docs/book-iv-physics-readout-functor/speed-of-light-procedure/) | L199-L205 | defined | — |
| `def` | [all_procedures](/verify/taulib/docs/book-iv-physics-readout-functor/all-procedures/) | L208-L210 | defined | — |
| `theorem` | [readout_preserves_identities](/verify/taulib/docs/book-iv-physics-readout-functor/readout-preserves-identities/) | L219-L220 | formalized | `IV.T128` |
| `theorem` | [single_anchor_sufficiency](/verify/taulib/docs/book-iv-physics-readout-functor/single-anchor-sufficiency/) | L224-L226 | formalized | `IV.T129` |
| `theorem` | [codomain_operational](/verify/taulib/docs/book-iv-physics-readout-functor/codomain-operational/) | L230-L235 | formalized | `IV.P177` |
| `theorem` | [unique_anchor](/verify/taulib/docs/book-iv-physics-readout-functor/unique-anchor/) | L238-L241 | formalized | — |
| `theorem` | [anchor_is_neutron](/verify/taulib/docs/book-iv-physics-readout-functor/anchor-is-neutron/) | L244-L245 | formalized | — |
| `eval` | [#eval L251](/verify/taulib/docs/book-iv-physics-readout-functor/eval-l251/) | L251-L251 | computed | — |
| `eval` | [#eval L252](/verify/taulib/docs/book-iv-physics-readout-functor/eval-l252/) | L252-L252 | computed | — |
| `eval` | [#eval L253](/verify/taulib/docs/book-iv-physics-readout-functor/eval-l253/) | L253-L253 | computed | — |
| `eval` | [#eval L254](/verify/taulib/docs/book-iv-physics-readout-functor/eval-l254/) | L254-L256 | computed | — |

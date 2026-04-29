---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Addressability.CayleyMetric",
  "permalink": "/verify/taulib/docs/book-i-addressability-cayley-metric/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Addressability.CayleyMetric`.",
  "module_name": "TauLib.BookI.Addressability.CayleyMetric",
  "module_slug": "book-i-addressability-cayley-metric",
  "book": "BookI",
  "family": "Addressability",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Addressability/CayleyMetric.lean",
  "sha256": "d809e90b232bee5c9fba07b7ff99429a292d701452b61ab85f7673b66fe0359d",
  "imports": [
    "TauLib.BookI.Denotation.ProgramMonoid"
  ],
  "imported_by": [
    "TauLib.BookI.Addressability.HingeIntegration",
    "TauLib.BookI.Addressability.OnticUltrametric"
  ],
  "registry_ids": [
    "I.D14",
    "I.L02"
  ],
  "declaration_counts": {
    "def": 2,
    "theorem": 8
  },
  "declarations": [
    {
      "kind": "def",
      "name": "natAbsDiff",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff/",
      "source_line_start": 56,
      "source_line_end": 59,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "natAbsDiff_comm",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff-comm/",
      "source_line_start": 61,
      "source_line_end": 62,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "natAbsDiff_eq_zero_iff",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff-eq-zero-iff/",
      "source_line_start": 64,
      "source_line_end": 69,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "natAbsDiff_triangle",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff-triangle/",
      "source_line_start": 71,
      "source_line_end": 73,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "CayleyDist",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist/",
      "source_line_start": 80,
      "source_line_end": 84,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CayleyDist_symm",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-symm/",
      "source_line_start": 86,
      "source_line_end": 89,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CayleyDist_eq_zero_iff_rhoCount",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-eq-zero-iff-rho-count/",
      "source_line_start": 95,
      "source_line_end": 98,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CayleyDist_triangle",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-triangle/",
      "source_line_start": 101,
      "source_line_end": 104,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CayleyDist_compose_right",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-compose-right/",
      "source_line_start": 113,
      "source_line_end": 118,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "CayleyDist_compose_left",
      "url": "/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-compose-left/",
      "source_line_start": 121,
      "source_line_end": 128,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean",
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
- Source path: [`TauLib/BookI/Addressability/CayleyMetric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Addressability/CayleyMetric.lean`
- SHA-256: `d809e90b232bee5c9fba07b7ff99429a292d701452b61ab85f7673b66fe0359d`

## Registry Links

- `I.D14` — Program Monoid
- `I.L02` — NF-Confluence

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Denotation.ProgramMonoid`

## Imported By

- `TauLib.BookI.Addressability.HingeIntegration`
- `TauLib.BookI.Addressability.OnticUltrametric`

## Declaration Counts

- `def`: 2
- `theorem`: 8

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [natAbsDiff](/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff/) | L56-L59 | defined | — |
| `theorem` | [natAbsDiff_comm](/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff-comm/) | L61-L62 | formalized | — |
| `theorem` | [natAbsDiff_eq_zero_iff](/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff-eq-zero-iff/) | L64-L69 | formalized | — |
| `theorem` | [natAbsDiff_triangle](/verify/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff-triangle/) | L71-L73 | formalized | — |
| `def` | [CayleyDist](/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist/) | L80-L84 | defined | — |
| `theorem` | [CayleyDist_symm](/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-symm/) | L86-L89 | formalized | — |
| `theorem` | [CayleyDist_eq_zero_iff_rhoCount](/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-eq-zero-iff-rho-count/) | L95-L98 | formalized | — |
| `theorem` | [CayleyDist_triangle](/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-triangle/) | L101-L104 | formalized | — |
| `theorem` | [CayleyDist_compose_right](/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-compose-right/) | L113-L118 | formalized | — |
| `theorem` | [CayleyDist_compose_left](/verify/taulib/docs/book-i-addressability-cayley-metric/cayley-dist-compose-left/) | L121-L128 | formalized | — |

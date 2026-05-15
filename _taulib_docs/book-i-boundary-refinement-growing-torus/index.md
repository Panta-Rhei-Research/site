---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "permalink": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_slug": "book-i-boundary-refinement-growing-torus",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/RefinementGrowingTorus.lean",
  "sha256": "5189e9e6bbb438e11483c24bf7c195be0245a72ad6401d895bd9feeca3df6647",
  "imports": [
    "TauLib.BookI.Boundary.TorusDefectSystem"
  ],
  "imported_by": [],
  "registry_ids": [
    "I.D125",
    "I.D127",
    "I.T75",
    "I.T76"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 8,
    "theorem": 9
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "RefinedTorusDefect",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refined-torus-defect/",
      "source_line_start": 94,
      "source_line_end": 98,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "RefinedTorusDefect.sigmaSwap",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-swap/",
      "source_line_start": 106,
      "source_line_end": 122,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "RefinedTorusDefect.sigmaSwap_involutive",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-swap-involutive/",
      "source_line_start": 125,
      "source_line_end": 128,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "RefinedTorusDefect.sigma_fixed_iff_crossing",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-fixed-iff-crossing/",
      "source_line_start": 131,
      "source_line_end": 146,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "RefinedTorusDefect.proj",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/proj/",
      "source_line_start": 161,
      "source_line_end": 167,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "RefinedTorusDefect.proj_commutes_sigma",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/proj-commutes-sigma/",
      "source_line_start": 171,
      "source_line_end": 178,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "refinementGrowingTorusSystem",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-growing-torus-system/",
      "source_line_start": 190,
      "source_line_end": 197,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "refinementCrossingThread",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-crossing-thread/",
      "source_line_start": 205,
      "source_line_end": 209,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "refinement_sigma_fixed_thread_pointwise_crossing",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-sigma-fixed-thread-pointwise-crossing/",
      "source_line_start": 221,
      "source_line_end": 227,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "refinement_sigma_fixed_thread_is_crossing",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-sigma-fixed-thread-is-crossing/",
      "source_line_start": 230,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "refinementAnchor",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-anchor/",
      "source_line_start": 244,
      "source_line_end": 245,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "refinementMwd",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-mwd/",
      "source_line_start": 248,
      "source_line_end": 250,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "refinement_singleton_uniqueness",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-singleton-uniqueness/",
      "source_line_start": 255,
      "source_line_end": 261,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "refinementCrossingThread_is_crossingPoint",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-crossing-thread-is-crossing-point/",
      "source_line_start": 264,
      "source_line_end": 271,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "RefinementIdentity",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-identity/",
      "source_line_start": 278,
      "source_line_end": 280,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "RefinementIdentityFull",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-identity-full/",
      "source_line_start": 283,
      "source_line_end": 290,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "RefinementIdentity.universal_fixed_unconditional",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/universal-fixed-unconditional/",
      "source_line_start": 297,
      "source_line_end": 302,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "RefinementIdentity.fixes_crossing_thread",
      "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/fixes-crossing-thread/",
      "source_line_start": 306,
      "source_line_end": 313,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean",
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
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/RefinementGrowingTorus.lean`
- SHA-256: `5189e9e6bbb438e11483c24bf7c195be0245a72ad6401d895bd9feeca3df6647`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.TorusDefectSystem`

## Imported By

- No TauLib module in the snapshot imports this module.

## Declaration Counts

- `def`: 8
- `inductive`: 1
- `theorem`: 9

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [RefinedTorusDefect](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refined-torus-defect/) | L94-L98 | type/data schema | type/data schema | — |
| `def` | [RefinedTorusDefect.sigmaSwap](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-swap/) | L106-L122 | data/computed value | data/computed value | — |
| `theorem` | [RefinedTorusDefect.sigmaSwap_involutive](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-swap-involutive/) | L125-L128 | proof obligation | formal proof obligation checked | — |
| `theorem` | [RefinedTorusDefect.sigma_fixed_iff_crossing](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-fixed-iff-crossing/) | L131-L146 | proof obligation | formal proof obligation checked | — |
| `def` | [RefinedTorusDefect.proj](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/proj/) | L161-L167 | data/computed value | data/computed value | — |
| `theorem` | [RefinedTorusDefect.proj_commutes_sigma](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/proj-commutes-sigma/) | L171-L178 | proof obligation | formal proof obligation checked | — |
| `def` | [refinementGrowingTorusSystem](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-growing-torus-system/) | L190-L197 | definition | definition | — |
| `def` | [refinementCrossingThread](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-crossing-thread/) | L205-L209 | definition | definition | — |
| `theorem` | [refinement_sigma_fixed_thread_pointwise_crossing](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-sigma-fixed-thread-pointwise-crossing/) | L221-L227 | proof obligation | formal proof obligation checked | — |
| `theorem` | [refinement_sigma_fixed_thread_is_crossing](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-sigma-fixed-thread-is-crossing/) | L230-L236 | proof obligation | formal proof obligation checked | — |
| `def` | [refinementAnchor](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-anchor/) | L244-L245 | definition | definition | — |
| `def` | [refinementMwd](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-mwd/) | L248-L250 | definition | definition | — |
| `theorem` | [refinement_singleton_uniqueness](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-singleton-uniqueness/) | L255-L261 | proof obligation | formal proof obligation checked | — |
| `theorem` | [refinementCrossingThread_is_crossingPoint](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-crossing-thread-is-crossing-point/) | L264-L271 | proof obligation | formal proof obligation checked | — |
| `def` | [RefinementIdentity](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-identity/) | L278-L280 | definition | definition | — |
| `def` | [RefinementIdentityFull](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-identity-full/) | L283-L290 | definition | definition | — |
| `theorem` | [RefinementIdentity.universal_fixed_unconditional](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/universal-fixed-unconditional/) | L297-L302 | proof obligation | formal proof obligation checked | — |
| `theorem` | [RefinementIdentity.fixes_crossing_thread](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/fixes-crossing-thread/) | L306-L313 | proof obligation | formal proof obligation checked | — |

---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Boundary.TorusDefectSystem",
  "permalink": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_slug": "book-i-boundary-torus-defect-system",
  "book": "BookI",
  "family": "Boundary",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Boundary/TorusDefectSystem.lean",
  "sha256": "beed5d844a239b8fbc652acac95a9e40c0addf6d9d53b0680eb8abae869ede12",
  "imports": [
    "TauLib.BookI.Boundary.UniversalFixedScalar"
  ],
  "imported_by": [
    "TauLib.BookI.Boundary.RefinementGrowingTorus"
  ],
  "registry_ids": [
    "I.D125",
    "I.D126",
    "I.T72",
    "I.T73"
  ],
  "declaration_counts": {
    "inductive": 1,
    "def": 7,
    "theorem": 10
  },
  "declarations": [
    {
      "kind": "inductive",
      "name": "TorusDefect",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-defect/",
      "source_line_start": 141,
      "source_line_end": 145,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TorusDefect.sigmaSwap",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-swap/",
      "source_line_start": 152,
      "source_line_end": 164,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusDefect.sigmaSwap_involutive",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-swap-involutive/",
      "source_line_start": 167,
      "source_line_end": 169,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusDefect.sigma_fixed_iff_crossing",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-fixed-iff-crossing/",
      "source_line_start": 177,
      "source_line_end": 179,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TorusDefectSystem",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-defect-system/",
      "source_line_start": 191,
      "source_line_end": 196,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TorusDefectSystem.crossingThread",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/crossing-thread/",
      "source_line_start": 206,
      "source_line_end": 210,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusDefectSystem.sigma_fixed_thread_pointwise_crossing",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-fixed-thread-pointwise-crossing/",
      "source_line_start": 222,
      "source_line_end": 227,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "DefectInverseSystem.SigmaFixedThread.ext",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/ext/",
      "source_line_start": 236,
      "source_line_end": 244,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusDefectSystem.sigma_fixed_thread_is_crossing",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-fixed-thread-is-crossing/",
      "source_line_start": 252,
      "source_line_end": 258,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torusAnchor",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-anchor/",
      "source_line_start": 266,
      "source_line_end": 267,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "torusMwd",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-mwd/",
      "source_line_start": 273,
      "source_line_end": 275,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "torusSingletonUniqueness",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-singleton-uniqueness/",
      "source_line_start": 283,
      "source_line_end": 289,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusDefectSystem.crossingThread_is_crossingPoint",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/crossing-thread-is-crossing-point/",
      "source_line_start": 296,
      "source_line_end": 303,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TorusIdentity",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-identity/",
      "source_line_start": 311,
      "source_line_end": 313,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "TorusIdentityFull",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-identity-full/",
      "source_line_start": 317,
      "source_line_end": 326,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusIdentity.universal_fixed_unconditional",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/universal-fixed-unconditional/",
      "source_line_start": 344,
      "source_line_end": 348,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusIdentity.universal_fixed_scalar_unconditional",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/universal-fixed-scalar-unconditional/",
      "source_line_start": 353,
      "source_line_end": 361,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "TorusIdentity.fixes_crossing_thread",
      "url": "/corpus/taulib/docs/book-i-boundary-torus-defect-system/fixes-crossing-thread/",
      "source_line_start": 370,
      "source_line_end": 378,
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean",
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
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Boundary/TorusDefectSystem.lean`
- SHA-256: `beed5d844a239b8fbc652acac95a9e40c0addf6d9d53b0680eb8abae869ede12`

## Registry Links

- No Registry IDs were detected in this module.

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Boundary.UniversalFixedScalar`

## Imported By

- `TauLib.BookI.Boundary.RefinementGrowingTorus`

## Declaration Counts

- `def`: 7
- `inductive`: 1
- `theorem`: 10

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `inductive` | [TorusDefect](/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-defect/) | L141-L145 | type/data schema | type/data schema | — |
| `def` | [TorusDefect.sigmaSwap](/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-swap/) | L152-L164 | definition | definition | — |
| `theorem` | [TorusDefect.sigmaSwap_involutive](/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-swap-involutive/) | L167-L169 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TorusDefect.sigma_fixed_iff_crossing](/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-fixed-iff-crossing/) | L177-L179 | proof obligation | formal proof obligation checked | — |
| `def` | [TorusDefectSystem](/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-defect-system/) | L191-L196 | definition | definition | — |
| `def` | [TorusDefectSystem.crossingThread](/corpus/taulib/docs/book-i-boundary-torus-defect-system/crossing-thread/) | L206-L210 | definition | definition | — |
| `theorem` | [TorusDefectSystem.sigma_fixed_thread_pointwise_crossing](/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-fixed-thread-pointwise-crossing/) | L222-L227 | proof obligation | formal proof obligation checked | — |
| `theorem` | [DefectInverseSystem.SigmaFixedThread.ext](/corpus/taulib/docs/book-i-boundary-torus-defect-system/ext/) | L236-L244 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TorusDefectSystem.sigma_fixed_thread_is_crossing](/corpus/taulib/docs/book-i-boundary-torus-defect-system/sigma-fixed-thread-is-crossing/) | L252-L258 | proof obligation | formal proof obligation checked | — |
| `def` | [torusAnchor](/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-anchor/) | L266-L267 | definition | definition | — |
| `def` | [torusMwd](/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-mwd/) | L273-L275 | definition | definition | — |
| `theorem` | [torusSingletonUniqueness](/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-singleton-uniqueness/) | L283-L289 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TorusDefectSystem.crossingThread_is_crossingPoint](/corpus/taulib/docs/book-i-boundary-torus-defect-system/crossing-thread-is-crossing-point/) | L296-L303 | proof obligation | formal proof obligation checked | — |
| `def` | [TorusIdentity](/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-identity/) | L311-L313 | definition | definition | — |
| `def` | [TorusIdentityFull](/corpus/taulib/docs/book-i-boundary-torus-defect-system/torus-identity-full/) | L317-L326 | definition | definition | — |
| `theorem` | [TorusIdentity.universal_fixed_unconditional](/corpus/taulib/docs/book-i-boundary-torus-defect-system/universal-fixed-unconditional/) | L344-L348 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TorusIdentity.universal_fixed_scalar_unconditional](/corpus/taulib/docs/book-i-boundary-torus-defect-system/universal-fixed-scalar-unconditional/) | L353-L361 | proof obligation | formal proof obligation checked | — |
| `theorem` | [TorusIdentity.fixes_crossing_thread](/corpus/taulib/docs/book-i-boundary-torus-defect-system/fixes-crossing-thread/) | L370-L378 | proof obligation | formal proof obligation checked | — |

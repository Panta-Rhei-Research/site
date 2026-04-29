---
{
  "projection_kind": "taulib_declaration",
  "title": "SCVFeature",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/scvfeature/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::SCVFeature",
  "declaration_slug": "scvfeature",
  "kind": "inductive",
  "name": "SCVFeature",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 98,
  "source_line_end": 111,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L98-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L98-L111",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "status": "defined"
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
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/verify/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L98-L111)
- Source range: L98-L111
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Qualitative features of orthodox SCV, classified by the dimension
    at which they first appear. -/
```

## Source Excerpt

```lean
inductive SCVFeature where
  | RiemannMapping         -- C1: simply connected domains ≅ disk
  | RichAutomorphisms      -- C1: large automorphism group
  | Monodromy              -- C1: nontrivial analytic continuation
  | CauchyIntegral         -- C1: boundary determines interior
  | IsolatedSingularities  -- C1: singularities can be isolated
  | HartogsExtension       -- C2: extension across compact sets
  | BidiscBallSplit        -- C2: bidisc ≠ ball biholomorphically
  | DistinguishedBoundary  -- C2: non-smooth boundary in products
  | FullHartogs            -- C3: extension across codim ≥ 2
  | LeviProblem            -- C3: pseudoconvexity characterization
  | NoRiemannMapping       -- C3: Riemann mapping fails completely
  | GrauertVarieties       -- C3: complex varieties in boundary
  deriving DecidableEq, Repr
```

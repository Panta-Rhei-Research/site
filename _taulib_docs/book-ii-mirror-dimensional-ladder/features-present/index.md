---
{
  "projection_kind": "taulib_declaration",
  "title": "features_present",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/features-present/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::features_present",
  "declaration_slug": "features-present",
  "kind": "def",
  "name": "features_present",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 133,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L133-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L133-L146",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L133-L146)
- Source range: L133-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Features present at each rung of the orthodox SCV ladder. -/
```

## Source Excerpt

```lean
def features_present : SCVDimension → List SCVFeature
  | .C1     => [.RiemannMapping, .RichAutomorphisms, .Monodromy,
                .CauchyIntegral, .IsolatedSingularities]
  | .C2     => [.RiemannMapping, .RichAutomorphisms, .Monodromy,
                .CauchyIntegral, .IsolatedSingularities,
                .HartogsExtension, .BidiscBallSplit, .DistinguishedBoundary]
  | .C3     => [.RiemannMapping, .RichAutomorphisms, .Monodromy,
                .CauchyIntegral, .IsolatedSingularities,
                .HartogsExtension, .BidiscBallSplit, .DistinguishedBoundary,
                .FullHartogs, .LeviProblem, .NoRiemannMapping, .GrauertVarieties]
  | .C4plus => [.RiemannMapping, .RichAutomorphisms, .Monodromy,
                .CauchyIntegral, .IsolatedSingularities,
                .HartogsExtension, .BidiscBallSplit, .DistinguishedBoundary,
                .FullHartogs, .LeviProblem, .NoRiemannMapping, .GrauertVarieties]
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_violates_monotone_acquisition",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/tau-violates-monotone-acquisition/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::tau_violates_monotone_acquisition",
  "declaration_slug": "tau-violates-monotone-acquisition",
  "kind": "theorem",
  "name": "tau_violates_monotone_acquisition",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 259,
  "source_line_end": 266,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L259-L266",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L259-L266",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L259-L266)
- Source range: L259-L266
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- On the orthodox ladder, no single dimension has features from 3 rungs
    that aren't already subsumed. τ³ violates the monotone acquisition
    pattern by having C3 features (FullHartogs) while lacking C1 features
    (RiemannMapping, Monodromy, IsolatedSingularities). -/
```

## Source Excerpt

```lean
theorem tau_violates_monotone_acquisition :
    -- τ has a C3 feature
    (tau_features.map feature_origin).elem .C3 = true ∧
    -- but lacks C1 features
    tau_absent.elem .RiemannMapping = true ∧
    tau_absent.elem .Monodromy = true ∧
    tau_absent.elem .IsolatedSingularities = true := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> native_decide
```

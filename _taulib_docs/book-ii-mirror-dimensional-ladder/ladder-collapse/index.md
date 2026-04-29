---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_collapse",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/ladder-collapse/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::ladder_collapse",
  "declaration_slug": "ladder-collapse",
  "kind": "theorem",
  "name": "ladder_collapse",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 329,
  "source_line_end": 334,
  "registry_ids": [
    "II.T48"
  ],
  "related_registry_items": [
    {
      "id": "II.T48",
      "title": "Fourth Quadrant Ladder Collapse",
      "url": "/registry/object/II.T48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L329-L334",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L329-L334",
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
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L329-L334)
- Source range: L329-L334
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T48` — Fourth Quadrant Ladder Collapse

## Immediate Comment / Docstring

```lean
/-- [II.T48] Fourth Quadrant Ladder Collapse: the dimensional ladder does not
    exist in the (Hyperbolic, Non-Archimedean) quadrant because the engine
    that generates it is absent. -/
```

## Source Excerpt

```lean
theorem ladder_collapse :
    engine_active tau_quadrant = false ∧
    tau_quadrant.pde = .Hyperbolic ∧
    tau_quadrant.metric = .NonArchimedean := by
  refine ⟨?_, rfl, rfl⟩
  native_decide
```

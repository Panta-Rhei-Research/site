---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusDefectSystem.crossingThread_is_crossingPoint",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/crossing-thread-is-crossing-point/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::TorusDefectSystem.crossingThread_is_crossingPoint",
  "declaration_slug": "crossing-thread-is-crossing-point",
  "kind": "theorem",
  "name": "TorusDefectSystem.crossingThread_is_crossingPoint",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 296,
  "source_line_end": 303,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L296-L303",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TorusDefectSystem",
        "url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L296-L303",
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

- Module: [TauLib.BookI.Boundary.TorusDefectSystem](/verify/taulib/docs/book-i-boundary-torus-defect-system/)
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L296-L303)
- Source range: L296-L303
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The crossing thread is a crossing-point** (IsCrossingPoint
    predicate holds for it):
    - IsNonPolar: the constant-`none` thread is at the anchor from
      depth 0.
    - IsOmegaApproaching: mwd is 0 which is ≤ any bound.  -/
```

## Source Excerpt

```lean
theorem TorusDefectSystem.crossingThread_is_crossingPoint :
    DefectInverseSystem.IsCrossingPoint torusAnchor torusMwd
      TorusDefectSystem.crossingThread := by
  refine ⟨?_, ?_⟩
  · -- IsNonPolar: ∃ maturity_depth, ∀ n ≥ maturity_depth, anchor n (point n)
    exact ⟨0, fun _ _ => rfl⟩
  · -- IsOmegaApproaching: ∃ bound, mwd t ≤ bound
    exact ⟨0, Nat.le_refl 0⟩
```

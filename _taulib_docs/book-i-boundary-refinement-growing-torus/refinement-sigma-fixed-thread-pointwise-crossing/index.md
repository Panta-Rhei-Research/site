---
{
  "projection_kind": "taulib_declaration",
  "title": "refinement_sigma_fixed_thread_pointwise_crossing",
  "permalink": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-sigma-fixed-thread-pointwise-crossing/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "declaration_id": "TauLib.BookI.Boundary.RefinementGrowingTorus::refinement_sigma_fixed_thread_pointwise_crossing",
  "declaration_slug": "refinement-sigma-fixed-thread-pointwise-crossing",
  "kind": "theorem",
  "name": "refinement_sigma_fixed_thread_pointwise_crossing",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_url": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "source_line_start": 221,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L221-L227",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.RefinementGrowingTorus",
        "url": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L221-L227",
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

- Module: [TauLib.BookI.Boundary.RefinementGrowingTorus](/verify/taulib/docs/book-i-boundary-refinement-growing-torus/)
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L221-L227)
- Source range: L221-L227
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ-fixed thread is pointwise crossing** (analogue of Wave 14
    `sigma_fixed_thread_pointwise_crossing`).

    Because σ-fixedness on `RefinedTorusDefect n` forces every point
    to be `crossing` (by `sigma_fixed_iff_crossing`), every σ-fixed
    thread is constantly `crossing`. -/
```

## Source Excerpt

```lean
theorem refinement_sigma_fixed_thread_pointwise_crossing
    (t : DefectInverseSystem.SigmaFixedThread refinementGrowingTorusSystem)
    (n : Nat) :
    t.point n = RefinedTorusDefect.crossing := by
  have h_sigma := t.sigma_fixed n
  show t.point n = _
  exact (RefinedTorusDefect.sigma_fixed_iff_crossing (t.point n)).mp h_sigma
```

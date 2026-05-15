---
{
  "projection_kind": "taulib_declaration",
  "title": "refinement_sigma_fixed_thread_is_crossing",
  "permalink": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-sigma-fixed-thread-is-crossing/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "declaration_id": "TauLib.BookI.Boundary.RefinementGrowingTorus::refinement_sigma_fixed_thread_is_crossing",
  "declaration_slug": "refinement-sigma-fixed-thread-is-crossing",
  "kind": "theorem",
  "name": "refinement_sigma_fixed_thread_is_crossing",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "source_line_start": 230,
  "source_line_end": 236,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L230-L236",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.RefinementGrowingTorus",
        "url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L230-L236",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.RefinementGrowingTorus](/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/)
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L230-L236)
- Source range: L230-L236
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Every σ-fixed thread is the crossing thread**. -/
```

## Source Excerpt

```lean
theorem refinement_sigma_fixed_thread_is_crossing
    (t : DefectInverseSystem.SigmaFixedThread refinementGrowingTorusSystem) :
    t = refinementCrossingThread := by
  apply DefectInverseSystem.SigmaFixedThread.ext
  intro n
  rw [refinement_sigma_fixed_thread_pointwise_crossing t n]
  rfl
```

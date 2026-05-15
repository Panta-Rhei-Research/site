---
{
  "projection_kind": "taulib_declaration",
  "title": "refinement_singleton_uniqueness",
  "permalink": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/refinement-singleton-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "declaration_id": "TauLib.BookI.Boundary.RefinementGrowingTorus::refinement_singleton_uniqueness",
  "declaration_slug": "refinement-singleton-uniqueness",
  "kind": "theorem",
  "name": "refinement_singleton_uniqueness",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_url": "/corpus/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "source_line_start": 255,
  "source_line_end": 261,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L255-L261",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L255-L261",
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
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L255-L261)
- Source range: L255-L261
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Singleton uniqueness on the refinement-growing torus**
    (Wave 13 hypothesis discharged unconditionally — second
    instance after Wave 14's `torusSingletonUniqueness`). -/
```

## Source Excerpt

```lean
theorem refinement_singleton_uniqueness
    (t₁ t₂ : DefectInverseSystem.SigmaFixedThread refinementGrowingTorusSystem)
    (_h₁ : DefectInverseSystem.IsCrossingPoint refinementAnchor refinementMwd t₁)
    (_h₂ : DefectInverseSystem.IsCrossingPoint refinementAnchor refinementMwd t₂) :
    t₁ = t₂ := by
  rw [refinement_sigma_fixed_thread_is_crossing t₁,
      refinement_sigma_fixed_thread_is_crossing t₂]
```

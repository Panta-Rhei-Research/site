---
{
  "projection_kind": "taulib_declaration",
  "title": "complete_means_six",
  "permalink": "/corpus/taulib/docs/book-ii-closure-forward-book3/complete-means-six/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.ForwardBook3`.",
  "declaration_id": "TauLib.BookII.Closure.ForwardBook3::complete_means_six",
  "declaration_slug": "complete-means-six",
  "kind": "theorem",
  "name": "complete_means_six",
  "module_name": "TauLib.BookII.Closure.ForwardBook3",
  "module_url": "/corpus/taulib/docs/book-ii-closure-forward-book3/",
  "source_line_start": 192,
  "source_line_end": 205,
  "registry_ids": [
    "II.D66"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L192-L205",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.ForwardBook3",
        "url": "/corpus/taulib/docs/book-ii-closure-forward-book3/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L192-L205",
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

- Module: [TauLib.BookII.Closure.ForwardBook3](/corpus/taulib/docs/book-ii-closure-forward-book3/)
- Source path: [`TauLib/BookII/Closure/ForwardBook3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/ForwardBook3.lean#L192-L205)
- Source range: L192-L205
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.D66] A complete export package has all 6 components.
    This is the structural statement that completeness implies count = 6. -/
```

## Source Excerpt

```lean
theorem complete_means_six (pkg : E1ExportPackage) :
    export_package_complete pkg = true ->
    export_component_count pkg = 6 := by
  intro h
  simp only [export_package_complete] at h
  simp only [export_component_count]
  revert h
  cases pkg.e1_layer_complete <;>
  cases pkg.central_theorem_verified <;>
  cases pkg.categoricity_verified <;>
  cases pkg.enrichment_ladder_verified <;>
  cases pkg.tau_manifold_verified <;>
  cases pkg.proto_rationality_verified <;>
  simp
```

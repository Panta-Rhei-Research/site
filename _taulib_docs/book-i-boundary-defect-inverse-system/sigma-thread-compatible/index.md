---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.sigma_thread_compatible",
  "permalink": "/corpus/taulib/docs/book-i-boundary-defect-inverse-system/sigma-thread-compatible/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.sigma_thread_compatible",
  "declaration_slug": "sigma-thread-compatible",
  "kind": "theorem",
  "name": "DefectInverseSystem.sigma_thread_compatible",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/corpus/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 208,
  "source_line_end": 213,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L208-L213",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.DefectInverseSystem",
        "url": "/corpus/taulib/docs/book-i-boundary-defect-inverse-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L208-L213",
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

- Module: [TauLib.BookI.Boundary.DefectInverseSystem](/corpus/taulib/docs/book-i-boundary-defect-inverse-system/)
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L208-L213)
- Source range: L208-L213
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ-commutes-with-projection preserves thread compatibility**
    (structural form of paper §4.2's closing line: "passage to
    the inverse limit preserves this invariance since projections
    commute with σ"). -/
```

## Source Excerpt

```lean
theorem DefectInverseSystem.sigma_thread_compatible
    (D : DefectInverseSystem) (t : D.Thread) (n : Nat) :
    D.proj n (D.sigma_level (n + 1) (t.point (n + 1)))
      = D.sigma_level n (t.point n) := by
  rw [D.sigma_commutes_proj]
  rw [t.compat]
```

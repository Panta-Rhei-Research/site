---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.sigma_invariance",
  "permalink": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/sigma-invariance/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.sigma_invariance",
  "declaration_slug": "sigma-invariance",
  "kind": "theorem",
  "name": "DefectInverseSystem.sigma_invariance",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 199,
  "source_line_end": 202,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L199-L202",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.DefectInverseSystem",
        "url": "/verify/taulib/docs/book-i-boundary-defect-inverse-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L199-L202",
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

- Module: [TauLib.BookI.Boundary.DefectInverseSystem](/verify/taulib/docs/book-i-boundary-defect-inverse-system/)
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L199-L202)
- Source range: L199-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ-invariance of the defect germ at the abstract level**
    (paper Thm 4.2 / `thm:defect-sigma-inv`).

    Given a thread with σ-fixed points at every depth, the entire
    thread is preserved by σ — a structural manifestation of the
    paper's "passage to the inverse limit preserves σ-invariance"
    claim.  Concretely: applying σ levelwise to a σ-fixed thread
    yields the same thread, which is the inverse-limit-level
    σ-fixedness. -/
```

## Source Excerpt

```lean
theorem DefectInverseSystem.sigma_invariance
    (D : DefectInverseSystem) (t : D.SigmaFixedThread) :
    ∀ n, D.sigma_level n (t.point n) = t.point n :=
  t.sigma_fixed
```

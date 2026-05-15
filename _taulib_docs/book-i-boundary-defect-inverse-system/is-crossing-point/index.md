---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.IsCrossingPoint",
  "permalink": "/corpus/taulib/docs/book-i-boundary-defect-inverse-system/is-crossing-point/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.DefectInverseSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.DefectInverseSystem::DefectInverseSystem.IsCrossingPoint",
  "declaration_slug": "is-crossing-point",
  "kind": "def",
  "name": "DefectInverseSystem.IsCrossingPoint",
  "module_name": "TauLib.BookI.Boundary.DefectInverseSystem",
  "module_url": "/corpus/taulib/docs/book-i-boundary-defect-inverse-system/",
  "source_line_start": 255,
  "source_line_end": 261,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L255-L261",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L255-L261",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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
- Source path: [`TauLib/BookI/Boundary/DefectInverseSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/DefectInverseSystem.lean#L255-L261)
- Source range: L255-L261
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Crossing-point characterisation** (paper Thm 5.5
    intersection).  A thread is a "crossing-point germ" if it
    lies in both NP and OA. -/
```

## Source Excerpt

```lean
def DefectInverseSystem.IsCrossingPoint
    {D : DefectInverseSystem}
    (anchor : ∀ n, D.defect_level n → Prop)
    (mwd : D.SigmaFixedThread → Nat)
    (t : D.SigmaFixedThread) : Prop :=
  DefectInverseSystem.IsNonPolar anchor t ∧
  DefectInverseSystem.IsOmegaApproaching mwd t
```

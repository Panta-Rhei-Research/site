---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectInverseSystem.SigmaFixedThread.ext",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/ext/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::DefectInverseSystem.SigmaFixedThread.ext",
  "declaration_slug": "ext",
  "kind": "theorem",
  "name": "DefectInverseSystem.SigmaFixedThread.ext",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 236,
  "source_line_end": 244,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L236-L244",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L236-L244",
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
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L236-L244)
- Source range: L236-L244
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Structural extensionality for `SigmaFixedThread`**: two
    σ-fixed threads with pointwise-equal `point` functions are
    equal.

    Proof: destructure both threads, use `funext` on the `point`
    field, and appeal to proof irrelevance of the Prop-valued
    fields. -/
```

## Source Excerpt

```lean
theorem DefectInverseSystem.SigmaFixedThread.ext
    {D : DefectInverseSystem}
    (t₁ t₂ : DefectInverseSystem.SigmaFixedThread D)
    (h : ∀ n, t₁.point n = t₂.point n) : t₁ = t₂ := by
  obtain ⟨⟨p₁, c₁⟩, sf₁⟩ := t₁
  obtain ⟨⟨p₂, c₂⟩, sf₂⟩ := t₂
  have hp : p₁ = p₂ := funext h
  subst hp
  rfl
```

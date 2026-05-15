---
{
  "projection_kind": "taulib_declaration",
  "title": "modal_collapse_prevention",
  "permalink": "/corpus/taulib/docs/book-vii-ethics-ciproof/modal-collapse-prevention/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::modal_collapse_prevention",
  "declaration_slug": "modal-collapse-prevention",
  "kind": "theorem",
  "name": "modal_collapse_prevention",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/corpus/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 850,
  "source_line_end": 854,
  "registry_ids": [
    "VII.L09"
  ],
  "related_registry_items": [
    {
      "id": "VII.L09",
      "title": "Modal Collapse Prevention",
      "url": "/registry/object/VII.L09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L850-L854",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/corpus/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L850-L854",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/corpus/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L850-L854)
- Source range: L850-L854
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `VII.L09` — Modal Collapse Prevention

## Immediate Comment / Docstring

```lean
/-- [VII.L09] Modal Collapse Prevention (ch43). The internal modal
    frame prevents modal collapse (□φ → φ without ◇φ → φ) because
    accessibility is not symmetric in general: admissible
    transformations are directed. -/
```

## Source Excerpt

```lean
theorem modal_collapse_prevention :
    accessibility.reflexive = true ∧
    accessibility.transitive = true ∧
    accessibility.kernel_morphism = true :=
  ⟨rfl, rfl, rfl⟩
```

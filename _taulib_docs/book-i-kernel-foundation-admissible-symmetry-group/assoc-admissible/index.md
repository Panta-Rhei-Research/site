---
{
  "projection_kind": "taulib_declaration",
  "title": "assoc_admissible",
  "permalink": "/corpus/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/assoc-admissible/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup::assoc_admissible",
  "declaration_slug": "assoc-admissible",
  "kind": "theorem",
  "name": "assoc_admissible",
  "module_name": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
  "module_url": "/corpus/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/",
  "source_line_start": 154,
  "source_line_end": 156,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L154-L156",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
        "url": "/corpus/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L154-L156",
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

- Module: [TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup](/corpus/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/)
- Source path: [`TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L154-L156)
- Source range: L154-L156
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Associativity law**: `(φ ∘ ψ) ∘ χ = φ ∘ (ψ ∘ χ)` (pointwise). -/
```

## Source Excerpt

```lean
theorem assoc_admissible (φ ψ χ : AdmissibleSymmetry) (p : Program) :
    (comp_admissible (comp_admissible φ ψ) χ).apply p =
    (comp_admissible φ (comp_admissible ψ χ)).apply p := rfl
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "comp_admissible",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/comp-admissible/",
  "summary_short": "`def` declaration in `TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup::comp_admissible",
  "declaration_slug": "comp-admissible",
  "kind": "def",
  "name": "comp_admissible",
  "module_name": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/",
  "source_line_start": 132,
  "source_line_end": 139,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L132-L139",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L132-L139",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup](/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/)
- Source path: [`TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L132-L139)
- Source range: L132-L139
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Composition of admissible symmetries**: φ ∘ ψ is admissible
    whenever both are.  Preserves NF by transitivity:
    `normalize ((φ ∘ ψ) p) = normalize (ψ p) = normalize p`. -/
```

## Source Excerpt

```lean
def comp_admissible (φ ψ : AdmissibleSymmetry) : AdmissibleSymmetry where
  apply := fun p => φ.apply (ψ.apply p)
  preserves_nf := fun p => by
    rw [φ.preserves_nf (ψ.apply p), ψ.preserves_nf p]

@[simp] theorem comp_admissible_apply (φ ψ : AdmissibleSymmetry)
    (p : Program) :
    (comp_admissible φ ψ).apply p = φ.apply (ψ.apply p) := rfl
```

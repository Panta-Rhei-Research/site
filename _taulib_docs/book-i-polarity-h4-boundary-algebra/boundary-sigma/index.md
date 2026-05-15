---
{
  "projection_kind": "taulib_declaration",
  "title": "boundarySigma",
  "permalink": "/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/boundary-sigma/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::boundarySigma",
  "declaration_slug": "boundary-sigma",
  "kind": "def",
  "name": "boundarySigma",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 128,
  "source_line_end": 137,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L128-L137",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
        "url": "/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L128-L137",
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

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/corpus/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L128-L137)
- Source range: L128-L137
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ-involution on D**: paper §10 `def:sigma-sublattice`.  The
    R_bd-algebra involution `σ(j) = -j`, equivalently the swap
    `e_+ ↔ e_-`.  Realised at the SplitComplex level by negating
    the imaginary component. -/
```

## Source Excerpt

```lean
def boundarySigma (z : SplitComplex) : SplitComplex :=
  ⟨z.re, -z.im⟩

@[simp] theorem boundarySigma_one : boundarySigma SplitComplex.one = SplitComplex.one := by
  unfold boundarySigma SplitComplex.one
  simp

@[simp] theorem boundarySigma_zero : boundarySigma SplitComplex.zero = SplitComplex.zero := by
  unfold boundarySigma SplitComplex.zero
  simp
```

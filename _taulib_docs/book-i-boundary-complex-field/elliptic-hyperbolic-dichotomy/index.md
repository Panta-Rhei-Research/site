---
{
  "projection_kind": "taulib_declaration",
  "title": "elliptic_hyperbolic_dichotomy",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/elliptic-hyperbolic-dichotomy/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::elliptic_hyperbolic_dichotomy",
  "declaration_slug": "elliptic-hyperbolic-dichotomy",
  "kind": "theorem",
  "name": "elliptic_hyperbolic_dichotomy",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 279,
  "source_line_end": 287,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L279-L287",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ComplexField",
        "url": "/verify/taulib/docs/book-i-boundary-complex-field/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L279-L287",
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

- Module: [TauLib.BookI.Boundary.ComplexField](/verify/taulib/docs/book-i-boundary-complex-field/)
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L279-L287)
- Source range: L279-L287
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The dichotomy: i² = -1 AND j² = +1 AND SplitComplex has zero divisors. -/
```

## Source Excerpt

```lean
theorem elliptic_hyperbolic_dichotomy :
    -- i² = -1 (elliptic)
    TauComplex.equiv (TauComplex.mul TauComplex.i_unit TauComplex.i_unit)
                     (TauComplex.negate TauComplex.one) ∧
    -- j² = +1 (hyperbolic)
    SplitComplex.mul ⟨0, 1⟩ ⟨0, 1⟩ = SplitComplex.one ∧
    -- SplitComplex has zero divisors: (1+j)(1-j) = 0
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero :=
  ⟨taucomplex_i_squared, sc_j_squared, by simp [SplitComplex.mul, SplitComplex.zero]⟩
```

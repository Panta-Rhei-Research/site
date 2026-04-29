---
{
  "projection_kind": "taulib_declaration",
  "title": "sc_j_squared",
  "permalink": "/verify/taulib/docs/book-i-boundary-complex-field/sc-j-squared/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::sc_j_squared",
  "declaration_slug": "sc-j-squared",
  "kind": "theorem",
  "name": "sc_j_squared",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/verify/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 274,
  "source_line_end": 276,
  "registry_ids": [
    "I.D86"
  ],
  "related_registry_items": [
    {
      "id": "I.D86",
      "title": "Elliptic-Hyperbolic Dichotomy",
      "url": "/registry/object/I.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L274-L276",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L274-L276",
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L274-L276)
- Source range: L274-L276
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D86` — Elliptic-Hyperbolic Dichotomy

## Immediate Comment / Docstring

```lean
/-- [I.D86] The elliptic-hyperbolic dichotomy:
    - TauComplex has i² = -1 (elliptic sign), yielding a field with no zero divisors.
    - SplitComplex has j² = +1 (hyperbolic sign), yielding a ring WITH zero divisors.

    We witness the dichotomy by showing:
    1. i² = -1 in TauComplex (taucomplex_i_squared)
    2. j² = +1 in SplitComplex (sc_j_squared, proved below)
    3. SplitComplex has zero divisors (zero_divisor_witness_b from SplitComplex.lean) -/
```

## Source Excerpt

```lean
theorem sc_j_squared :
    SplitComplex.mul ⟨0, 1⟩ ⟨0, 1⟩ = SplitComplex.one := by
  simp [SplitComplex.mul, SplitComplex.one]
```

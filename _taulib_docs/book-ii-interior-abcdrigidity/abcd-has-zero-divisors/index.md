---
{
  "projection_kind": "taulib_declaration",
  "title": "abcd_has_zero_divisors",
  "permalink": "/verify/taulib/docs/book-ii-interior-abcdrigidity/abcd-has-zero-divisors/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Interior.ABCDRigidity`.",
  "declaration_id": "TauLib.BookII.Interior.ABCDRigidity::abcd_has_zero_divisors",
  "declaration_slug": "abcd-has-zero-divisors",
  "kind": "theorem",
  "name": "abcd_has_zero_divisors",
  "module_name": "TauLib.BookII.Interior.ABCDRigidity",
  "module_url": "/verify/taulib/docs/book-ii-interior-abcdrigidity/",
  "source_line_start": 107,
  "source_line_end": 114,
  "registry_ids": [
    "II.R04"
  ],
  "related_registry_items": [
    {
      "id": "II.R04",
      "title": "ABCD vs Quaternions",
      "url": "/registry/object/II.R04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L107-L114",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.ABCDRigidity",
        "url": "/verify/taulib/docs/book-ii-interior-abcdrigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L107-L114",
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

- Module: [TauLib.BookII.Interior.ABCDRigidity](/verify/taulib/docs/book-ii-interior-abcdrigidity/)
- Source path: [`TauLib/BookII/Interior/ABCDRigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L107-L114)
- Source range: L107-L114
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.R04` — ABCD vs Quaternions

## Immediate Comment / Docstring

```lean
/-- [II.R04] Split-complex has zero divisors; quaternions don't.
    This is the key algebraic difference: H_τ admits bipolar sectors
    via e₊ · e₋ = 0, while ℍ is a division algebra. -/
```

## Source Excerpt

```lean
theorem abcd_has_zero_divisors :
    ∃ z w : SplitComplex,
    z ≠ ⟨0, 0⟩ ∧ w ≠ ⟨0, 0⟩ ∧
    SplitComplex.mul z w = ⟨0, 0⟩ := by
  refine ⟨⟨1, 1⟩, ⟨1, -1⟩, ?_, ?_, ?_⟩
  · intro h; have := congrArg SplitComplex.re h; simp at this
  · intro h; have := congrArg SplitComplex.re h; simp at this
  · unfold SplitComplex.mul; ext <;> simp
```

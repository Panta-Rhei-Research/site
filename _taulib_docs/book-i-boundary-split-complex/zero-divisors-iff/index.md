---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_divisors_iff",
  "permalink": "/verify/taulib/docs/book-i-boundary-split-complex/zero-divisors-iff/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.SplitComplex`.",
  "declaration_id": "TauLib.BookI.Boundary.SplitComplex::zero_divisors_iff",
  "declaration_slug": "zero-divisors-iff",
  "kind": "theorem",
  "name": "zero_divisors_iff",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_url": "/verify/taulib/docs/book-i-boundary-split-complex/",
  "source_line_start": 295,
  "source_line_end": 314,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L295-L314",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.SplitComplex",
        "url": "/verify/taulib/docs/book-i-boundary-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L295-L314",
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

- Module: [TauLib.BookI.Boundary.SplitComplex](/verify/taulib/docs/book-i-boundary-split-complex/)
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L295-L314)
- Source range: L295-L314
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The zero divisors of SplitComplex are exactly the elements with a vanishing sector. -/
```

## Source Excerpt

```lean
theorem zero_divisors_iff (z : SplitComplex) (hz : z ≠ SplitComplex.zero) :
    (∃ w : SplitComplex, w ≠ SplitComplex.zero ∧ SplitComplex.mul z w = SplitComplex.zero) ↔
    (z.re + z.im = 0 ∨ z.re - z.im = 0) := by
  constructor
  · -- Forward: z * w = 0 with w ≠ 0 implies sector vanishes
    intro ⟨w, hw_ne, hw_zero⟩
    rcases zero_divisor_sector z w hw_zero with ⟨hb, hc⟩
    -- Int integral domain: for each factor product = 0, one factor is 0
    rcases mul_eq_zero.mp hb with hzb | hwb
    · left; exact hzb
    · rcases mul_eq_zero.mp hc with hzc | hwc
      · right; exact hzc
      · -- Both w.re+w.im = 0 and w.re-w.im = 0, so w.re = 0 and w.im = 0
        exfalso; apply hw_ne
        ext <;> simp [SplitComplex.zero] <;> omega
  · -- Backward: sector vanishes implies zero divisor exists
    intro h_or
    rcases h_or with hb | hc
    · exact ⟨⟨1, 1⟩, by simp [SplitComplex.zero], zero_divisor_witness_b z hb⟩
    · exact ⟨⟨1, -1⟩, by simp [SplitComplex.zero], zero_divisor_witness_c z hc⟩
```

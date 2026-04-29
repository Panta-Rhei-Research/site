---
{
  "projection_kind": "taulib_declaration",
  "title": "int_no_zero_div",
  "permalink": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/int-no-zero-div/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.BipolarAlgebra::int_no_zero_div",
  "declaration_slug": "int-no-zero-div",
  "kind": "theorem",
  "name": "int_no_zero_div",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/",
  "source_line_start": 181,
  "source_line_end": 191,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L181-L191",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.BipolarAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L181-L191",
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

- Module: [TauLib.BookI.Polarity.BipolarAlgebra](/verify/taulib/docs/book-i-polarity-bipolar-algebra/)
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L181-L191)
- Source range: L181-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: Int is an integral domain (proved via natAbs). -/
```

## Source Excerpt

```lean
private theorem int_no_zero_div {a b : Int} (h : a * b = 0) : a = 0 ∨ b = 0 := by
  rcases Nat.eq_zero_or_pos a.natAbs with ha | ha
  · left; exact Int.natAbs_eq_zero.mp ha
  · right
    have h_abs : a.natAbs * b.natAbs = 0 := by
      rw [← Int.natAbs_mul]; exact Int.natAbs_eq_zero.mpr h
    have hb : b.natAbs = 0 := by
      rcases Nat.eq_zero_or_pos b.natAbs with hb | hb
      · exact hb
      · exfalso; have := Nat.mul_pos ha hb; omega
    exact Int.natAbs_eq_zero.mp hb
```

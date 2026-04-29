---
{
  "projection_kind": "taulib_declaration",
  "title": "tauIdx_no_ring_negation",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/tau-idx-no-ring-negation/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::tauIdx_no_ring_negation",
  "declaration_slug": "tau-idx-no-ring-negation",
  "kind": "theorem",
  "name": "tauIdx_no_ring_negation",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 68,
  "source_line_end": 82,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L68-L82",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Structural",
        "url": "/verify/taulib/docs/book-i-denotation-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L68-L82",
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

- Module: [TauLib.BookI.Denotation.Structural](/verify/taulib/docs/book-i-denotation-structural/)
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L68-L82)
- Source range: L68-L82
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- There exists no negation function on τ-Idx.
    This is the precise statement that τ-Idx is a semiring, not a ring.
    Additive inverses are first earned at Part IX via TauInt formal differences. -/
```

## Source Excerpt

```lean
theorem tauIdx_no_ring_negation :
    ¬∃ neg : TauIdx → TauIdx, ∀ n, idx_add n (neg n) = 0 := by
  intro ⟨neg, h⟩
  have h1 := h 1
  simp only [idx_add_eq_nat_add, TauIdx] at *; omega

-- ============================================================
-- SECTION 2: THE POSITIVE CORE — N⁺ IS CLOSED
-- ============================================================

/-! ## Section 2: The Positive Core — N⁺ is Closed

N⁺ = {n : τ-Idx | n > 0} is closed under all four earned arithmetic operations.
This means the positive elements form an autonomous sub-structure: arithmetic
never "falls" into zero unless it starts there. -/
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "tauIdx_zero_vacuous_divisor",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/tau-idx-zero-vacuous-divisor/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::tauIdx_zero_vacuous_divisor",
  "declaration_slug": "tau-idx-zero-vacuous-divisor",
  "kind": "theorem",
  "name": "tauIdx_zero_vacuous_divisor",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 163,
  "source_line_end": 180,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L163-L180",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L163-L180",
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
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L163-L180)
- Source range: L163-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Zero is divisible by everything (vacuously): every a divides 0.
    This is a restatement of idx_divides_zero for emphasis:
    divisibility into zero is *trivial*, not informative. -/
```

## Source Excerpt

```lean
theorem tauIdx_zero_vacuous_divisor (a : TauIdx) : idx_divides a 0 :=
  idx_divides_zero a

-- ============================================================
-- SECTION 4: UNIVERSAL VS. GUARDED — THE SINGLE FAILURE LOCUS
-- ============================================================

/-! ## Section 4: Universal vs. Guarded — The Single Failure Locus

The dramatic structural fact of τ-Idx: almost every algebraic property holds
*universally* (no "for n ≠ 0" guard).  The single exception is multiplicative
cancellation, which fails exactly at zero.

In ring theory, "for a ≠ 0" qualifications appear everywhere.  In τ-Idx:
- Addition: fully cancellative, universal (Theorem 13)
- Multiplication: cancellative ↔ n > 0 (Theorem 16)
- Divisibility: reflexive, transitive, antisymmetric — all universal
- Well-ordering: universal, no qualification needed -/
```

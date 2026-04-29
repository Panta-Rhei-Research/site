---
{
  "projection_kind": "taulib_declaration",
  "title": "tauIdx_succ_always_pos",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/tau-idx-succ-always-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::tauIdx_succ_always_pos",
  "declaration_slug": "tau-idx-succ-always-pos",
  "kind": "theorem",
  "name": "tauIdx_succ_always_pos",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 106,
  "source_line_end": 118,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L106-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L106-L118",
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
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L106-L118)
- Source range: L106-L118
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Every successor is positive: n + 1 > 0 always holds.
    No guard needed — this is universal over τ-Idx. -/
```

## Source Excerpt

```lean
theorem tauIdx_succ_always_pos (n : TauIdx) :
    idx_add n 1 > 0 := by
  simp only [idx_add_eq_nat_add, TauIdx] at *; omega

-- ============================================================
-- SECTION 3: ZERO AS NON-PARTICIPANT
-- ============================================================

/-! ## Section 3: Zero as Non-Participant

Zero in τ-Idx is *vacuous*, not destructive.  It is the unique degenerate
element: it absorbs multiplication and has no prime factorization.  But its
degeneracy is passive — it doesn't participate in the generative dynamics of ρ. -/
```

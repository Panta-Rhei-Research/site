---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.lt_trans",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-order/lt-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.lt_trans",
  "declaration_slug": "lt-trans",
  "kind": "theorem",
  "name": "TauReal.lt_trans",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 191,
  "source_line_end": 212,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L191-L212",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealOrder",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L191-L212",
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

- Module: [TauLib.BookI.Boundary.TauRealOrder](/verify/taulib/docs/book-i-boundary-tau-real-order/)
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L191-L212)
- Source range: L191-L212
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `lt` is transitive.

    Strategy: chain the two witnessed gaps.  Take `k = k₁` (we only need
    the first gap, since `b < c` implies `b < b + 1/(k₂+1) + something`). -/
```

## Source Excerpt

```lean
theorem TauReal.lt_trans {a b c : TauReal}
    (hab : TauReal.lt a b) (hbc : TauReal.lt b c) : TauReal.lt a c := by
  obtain ⟨k₁, N₁, h₁⟩ := hab
  obtain ⟨k₂, N₂, h₂⟩ := hbc
  refine ⟨k₁, max N₁ N₂, fun n hn => ?_⟩
  have hn₁ : N₁ ≤ n := le_of_max_le_left hn
  have hn₂ : N₂ ≤ n := le_of_max_le_right hn
  have h_ab := h₁ n hn₁
  have h_bc := h₂ n hn₂
  unfold TauRat.lt at h_ab h_bc ⊢
  rw [toRat_add, TauRat.ofNatRecip_toRat] at h_ab h_bc
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  -- h_ab : a + 1/(k₁+1) < b
  -- h_bc : b + 1/(k₂+1) < c
  -- Goal : a + 1/(k₁+1) < c.  Chain:
  --        a + 1/(k₁+1) < b < b + 1/(k₂+1) < c.
  have h_pos_k₂ : (0 : Rat) < 1 / ((k₂ : Rat) + 1) := by
    have : (0 : Rat) < (k₂ : Rat) + 1 := by
      have : (0 : Rat) ≤ (k₂ : Rat) := by exact_mod_cast Nat.zero_le k₂
      linarith
    exact div_pos (by norm_num) this
  linarith
```

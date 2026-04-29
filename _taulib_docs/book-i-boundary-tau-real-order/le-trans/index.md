---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.le_trans",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-order/le-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.le_trans",
  "declaration_slug": "le-trans",
  "kind": "theorem",
  "name": "TauReal.le_trans",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 161,
  "source_line_end": 181,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L161-L181",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L161-L181",
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
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L161-L181)
- Source range: L161-L181
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `le` is transitive.

    Strategy: at tolerance level `k`, split the budget — use tolerance
    `2k+1` for each half (giving `1/(2k+2)` each), sum to `1/(k+1)`. -/
```

## Source Excerpt

```lean
theorem TauReal.le_trans {a b c : TauReal}
    (hab : TauReal.le a b) (hbc : TauReal.le b c) : TauReal.le a c := by
  intro k
  obtain ⟨N₁, h₁⟩ := hab (2 * k + 1)
  obtain ⟨N₂, h₂⟩ := hbc (2 * k + 1)
  refine ⟨max N₁ N₂, fun n hn => ?_⟩
  have hn₁ : N₁ ≤ n := le_of_max_le_left hn
  have hn₂ : N₂ ≤ n := le_of_max_le_right hn
  have h_ab := h₁ n hn₁
  have h_bc := h₂ n hn₂
  unfold TauRat.lt at h_ab h_bc ⊢
  rw [toRat_add, TauRat.ofNatRecip_toRat] at h_ab h_bc
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  -- h_ab : a.approx n .toRat < b.approx n .toRat + 1/(2k+2)
  -- h_bc : b.approx n .toRat < c.approx n .toRat + 1/(2k+2)
  -- Goal : a.approx n .toRat < c.approx n .toRat + 1/(k+1)
  -- Since 1/(2k+2) + 1/(2k+2) = 1/(k+1), the two half-tolerances sum cleanly.
  have h_eq : (1 : Rat) / ((2 * k + 1 : Nat) + 1) + 1 / ((2 * k + 1 : Nat) + 1)
              = 1 / ((k : Rat) + 1) := by
    push_cast; field_simp; ring
  linarith
```

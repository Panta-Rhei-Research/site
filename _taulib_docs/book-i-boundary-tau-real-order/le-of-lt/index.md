---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.le_of_lt",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-order/le-of-lt/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.le_of_lt",
  "declaration_slug": "le-of-lt",
  "kind": "theorem",
  "name": "TauReal.le_of_lt",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 128,
  "source_line_end": 151,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L128-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L128-L151",
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
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L128-L151)
- Source range: L128-L151
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `lt` implies `le`. -/
```

## Source Excerpt

```lean
theorem TauReal.le_of_lt {a b : TauReal} (h : TauReal.lt a b) : TauReal.le a b := by
  obtain ⟨k₀, N₀, h_lt⟩ := h
  -- At any tolerance level k, past index N₀ we have
  --   a + 1/(k₀+1) < b
  -- which gives the weaker  a < b + 1/(k+1)  for any k (since 1/(k₀+1) > 0).
  intro k
  refine ⟨N₀, fun n hn => ?_⟩
  have h0 := h_lt n hn
  unfold TauRat.lt at h0 ⊢
  rw [toRat_add, TauRat.ofNatRecip_toRat] at h0
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  -- h0 : (a.approx n).toRat + 1/(k₀+1) < (b.approx n).toRat
  -- Goal: (a.approx n).toRat < (b.approx n).toRat + 1/(k+1)
  have h_pos_k : (0 : Rat) < 1 / ((k : Rat) + 1) := by
    have : (0 : Rat) < (k : Rat) + 1 := by
      have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
      linarith
    exact div_pos (by norm_num) this
  have h_pos_k0 : (0 : Rat) < 1 / ((k₀ : Rat) + 1) := by
    have : (0 : Rat) < (k₀ : Rat) + 1 := by
      have : (0 : Rat) ≤ (k₀ : Rat) := by exact_mod_cast Nat.zero_le k₀
      linarith
    exact div_pos (by norm_num) this
  linarith
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.abs_triangle",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-triangle/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAbs::TauReal.abs_triangle",
  "declaration_slug": "abs-triangle",
  "kind": "theorem",
  "name": "TauReal.abs_triangle",
  "module_name": "TauLib.BookI.Boundary.TauRealAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/",
  "source_line_start": 146,
  "source_line_end": 172,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L146-L172",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealAbs",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L146-L172",
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

- Module: [TauLib.BookI.Boundary.TauRealAbs](/verify/taulib/docs/book-i-boundary-tau-real-abs/)
- Source path: [`TauLib/BookI/Boundary/TauRealAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L146-L172)
- Source range: L146-L172
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Triangle inequality on TauReal: `(a + b).abs ≤ a.abs + b.abs` in the
    `TauReal.le` sense.

    At each index, `TauRat.abs_triangle` (Wave 1c) gives the pointwise
    bound `(a.approx n + b.approx n).abs.toRat
      ≤ (a.approx n).abs.toRat + (b.approx n).abs.toRat`.
    The difference is therefore ≤ 0 pointwise, hence strictly less than
    any positive tolerance. -/
```

## Source Excerpt

```lean
theorem TauReal.abs_triangle (a b : TauReal) :
    TauReal.le ((a.add b).abs) ((a.abs).add (b.abs)) := by
  intro k
  refine ⟨0, fun n _ => ?_⟩
  -- Goal: ((a.add b).abs.approx n) .lt  ((a.abs.add b.abs).approx n + 1/(k+1))
  unfold TauRat.lt
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  -- LHS.toRat = ((a.approx n).add (b.approx n)).abs.toRat
  -- The inner structural `.add` on TauReal unfolds to TauRat.add at each n.
  show ((a.add b).abs.approx n).toRat
         < ((a.abs.add b.abs).approx n).toRat + 1 / ((k : Rat) + 1)
  have h_LHS : ((a.add b).abs.approx n).toRat
                 = ((a.approx n).add (b.approx n)).abs.toRat := rfl
  have h_RHS : ((a.abs.add b.abs).approx n).toRat
                 = (a.approx n).abs.toRat + (b.approx n).abs.toRat := by
    show ((a.approx n).abs.add (b.approx n).abs).toRat = _
    rw [toRat_add]
  rw [h_LHS, h_RHS]
  have h_tri := TauRat.abs_triangle (a.approx n) (b.approx n)
  have h_recip : (0 : Rat) < 1 / ((k : Rat) + 1) := by
    have : (0 : Rat) < (k : Rat) + 1 := by
      have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
      linarith
    exact div_pos (by norm_num) this
  linarith

end Tau.Boundary
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.sumFromTo_abs_le",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to-abs-le/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealSum`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealSum::TauRat.sumFromTo_abs_le",
  "declaration_slug": "sum-from-to-abs-le",
  "kind": "theorem",
  "name": "TauRat.sumFromTo_abs_le",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/",
  "source_line_start": 158,
  "source_line_end": 192,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L158-L192",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealSum",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L158-L192",
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

- Module: [TauLib.BookI.Boundary.TauRealSum](/verify/taulib/docs/book-i-boundary-tau-real-sum/)
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L158-L192)
- Source range: L158-L192
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Triangle inequality on a ranged sum at the toRat level:
    `|sumFromTo f n m .toRat| ≤ sumFromTo |f| n m .toRat`.

    Stated with `TauRat.abs` on `f` composed at each index (wrapped into
    a function `fun k => (f k).abs`). -/
```

## Source Excerpt

```lean
theorem TauRat.sumFromTo_abs_le (f : Nat → TauRat) (n : Nat) :
    ∀ m,
    |(TauRat.sumFromTo f n m).toRat|
      ≤ (TauRat.sumFromTo (fun k => (f k).abs) n m).toRat := by
  intro m
  induction m with
  | zero =>
    simp [TauRat.sumFromTo_zero, toRat_zero]
  | succ m ih =>
    by_cases h : n ≤ m
    · -- Both branches take the recursive case
      have h_abs_rec : TauRat.sumFromTo (fun k => (f k).abs) n (m + 1) =
            (TauRat.sumFromTo (fun k => (f k).abs) n m).add (f m).abs := by
        show (if n ≤ m then _ else _) = _; rw [if_pos h]
      have h_f_rec : TauRat.sumFromTo f n (m + 1) =
            (TauRat.sumFromTo f n m).add (f m) := by
        show (if n ≤ m then _ else _) = _; rw [if_pos h]
      rw [h_f_rec, h_abs_rec, toRat_add, toRat_add]
      -- goal: |(SFT f n m).toRat + (f m).toRat|
      --       ≤ (SFT |f| n m).toRat + (f m).abs.toRat
      have h_tri :
          |(TauRat.sumFromTo f n m).toRat + (f m).toRat|
            ≤ |(TauRat.sumFromTo f n m).toRat| + |(f m).toRat| := abs_add_le _ _
      have h_fm_abs : (f m).abs.toRat = |(f m).toRat| := TauRat.toRat_abs _
      rw [h_fm_abs]
      linarith [ih]
    · -- m < n: both sums are zero
      have h_abs_rec : TauRat.sumFromTo (fun k => (f k).abs) n (m + 1) = TauRat.zero := by
        show (if n ≤ m then _ else _) = _; rw [if_neg h]
      have h_f_rec : TauRat.sumFromTo f n (m + 1) = TauRat.zero := by
        show (if n ≤ m then _ else _) = _; rw [if_neg h]
      rw [h_f_rec, h_abs_rec, toRat_zero]
      simp

end Tau.Boundary
```

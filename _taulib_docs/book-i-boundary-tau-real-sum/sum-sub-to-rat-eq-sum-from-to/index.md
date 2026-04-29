---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.sum_sub_toRat_eq_sumFromTo",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-sum/sum-sub-to-rat-eq-sum-from-to/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealSum`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealSum::TauRat.sum_sub_toRat_eq_sumFromTo",
  "declaration_slug": "sum-sub-to-rat-eq-sum-from-to",
  "kind": "theorem",
  "name": "TauRat.sum_sub_toRat_eq_sumFromTo",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/",
  "source_line_start": 122,
  "source_line_end": 147,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L122-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L122-L147",
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
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L122-L147)
- Source range: L122-L147
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Telescoping identity at the `toRat` level: the difference of two
    partial sums equals the ranged sum between them. -/
```

## Source Excerpt

```lean
theorem TauRat.sum_sub_toRat_eq_sumFromTo (f : Nat → TauRat) (n : Nat) :
    ∀ m, n ≤ m →
    (TauRat.sum f m).toRat - (TauRat.sum f n).toRat
      = (TauRat.sumFromTo f n m).toRat := by
  intro m hnm
  induction m with
  | zero =>
    -- n ≤ 0 forces n = 0
    have hn : n = 0 := Nat.le_zero.mp hnm
    subst hn
    simp [TauRat.sum_zero, toRat_zero, TauRat.sumFromTo_zero]
  | succ m ih =>
    by_cases h_eq : n = m + 1
    · subst h_eq
      simp [TauRat.sumFromTo_self, toRat_zero]
    · have hnm' : n ≤ m := by omega
      specialize ih hnm'
      rw [TauRat.sum_succ, toRat_add]
      show (TauRat.sum f m).toRat + (f m).toRat - (TauRat.sum f n).toRat =
             (TauRat.sumFromTo f n (m + 1)).toRat
      have h_rec : TauRat.sumFromTo f n (m + 1) =
                   (TauRat.sumFromTo f n m).add (f m) := by
        show (if n ≤ m then _ else _) = _
        rw [if_pos hnm']
      rw [h_rec, toRat_add]
      linarith [ih]
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.abs_nonneg",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-nonneg/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAbs::TauReal.abs_nonneg",
  "declaration_slug": "abs-nonneg",
  "kind": "theorem",
  "name": "TauReal.abs_nonneg",
  "module_name": "TauLib.BookI.Boundary.TauRealAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/",
  "source_line_start": 68,
  "source_line_end": 88,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L68-L88",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L68-L88",
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
- Source path: [`TauLib/BookI/Boundary/TauRealAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L68-L88)
- Source range: L68-L88
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `0 ≤ a.abs` under `TauReal.le` — at every tolerance level, zero is
    strictly less than `|a.approx n| + 1/(k+1)` regardless of `n`. -/
```

## Source Excerpt

```lean
theorem TauReal.abs_nonneg (a : TauReal) : TauReal.le TauReal.zero a.abs := by
  intro k
  refine ⟨0, fun n _ => ?_⟩
  -- Goal: TauRat.lt ((zero.approx n)) ((a.abs.approx n).add (ofNatRecip k))
  unfold TauRat.lt
  rw [toRat_add, TauRat.ofNatRecip_toRat]
  -- (zero.approx n).toRat = 0, (a.abs.approx n).toRat = (a.approx n).abs.toRat ≥ 0
  show (TauReal.zero.approx n).toRat < (a.abs.approx n).toRat + 1 / ((k : Rat) + 1)
  have h_zero : (TauReal.zero.approx n).toRat = 0 := by
    show ((TauRat.zero).toRat) = 0
    exact toRat_zero
  have h_abs_nonneg : 0 ≤ (a.abs.approx n).toRat := by
    show 0 ≤ ((a.approx n).abs).toRat
    exact TauRat.abs_nonneg (a.approx n)
  have h_recip : (0 : Rat) < 1 / ((k : Rat) + 1) := by
    have : (0 : Rat) < (k : Rat) + 1 := by
      have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
      linarith
    exact div_pos (by norm_num) this
  rw [h_zero]
  linarith
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.is_nonzero_of_bounded_away",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-inv/is-nonzero-of-bounded-away/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealInv::TauReal.is_nonzero_of_bounded_away",
  "declaration_slug": "is-nonzero-of-bounded-away",
  "kind": "theorem",
  "name": "TauReal.is_nonzero_of_bounded_away",
  "module_name": "TauLib.BookI.Boundary.TauRealInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/",
  "source_line_start": 74,
  "source_line_end": 100,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L74-L100",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L74-L100",
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

- Module: [TauLib.BookI.Boundary.TauRealInv](/verify/taulib/docs/book-i-boundary-tau-real-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRealInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L74-L100)
- Source range: L74-L100
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If `a` is bounded away from zero past some index `N`, every
    `a.approx n` with `n ≥ N` is nonzero in the TauRat sense. -/
```

## Source Excerpt

```lean
theorem TauReal.is_nonzero_of_bounded_away {a : TauReal} {k N : Nat}
    (hN : ∀ n : Nat, N ≤ n → TauRat.lt (TauRat.ofNatRecip k) (a.approx n).abs)
    (n : Nat) (hn : N ≤ n) : (a.approx n).is_nonzero := by
  have h := hN n hn
  -- h : (ofNatRecip k).toRat < (a.approx n).abs.toRat
  unfold TauRat.lt at h
  rw [TauRat.ofNatRecip_toRat, TauRat.toRat_abs] at h
  -- h : 1/(k+1) < |(a.approx n).toRat|
  -- Conclude (a.approx n).toRat ≠ 0
  have h_recip : (0 : Rat) < 1 / ((k : Rat) + 1) := by
    have : (0 : Rat) < (k : Rat) + 1 := by
      have : (0 : Rat) ≤ (k : Rat) := by exact_mod_cast Nat.zero_le k
      linarith
    exact div_pos (by norm_num) this
  rw [(TauRat.is_nonzero_iff_toRat_ne_zero _)]
  intro h_zero
  rw [h_zero, abs_zero] at h
  linarith

-- ============================================================
-- PART 2: INVERSE (total function, good under BoundedAwayFromZero)
-- ============================================================

/-- Decidability of `TauRat.is_nonzero`: delegated to `Int` decidable
    equality via the `q.num.toInt ≠ 0` unfolding. -/
instance (q : TauRat) : Decidable q.is_nonzero := by
  unfold TauRat.is_nonzero; infer_instance
```

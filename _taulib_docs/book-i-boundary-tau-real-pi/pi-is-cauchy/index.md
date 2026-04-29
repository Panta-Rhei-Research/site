---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.pi_isCauchy",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi/pi-is-cauchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::TauReal.pi_isCauchy",
  "declaration_slug": "pi-is-cauchy",
  "kind": "theorem",
  "name": "TauReal.pi_isCauchy",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 271,
  "source_line_end": 300,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L271-L300",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPi",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L271-L300",
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

- Module: [TauLib.BookI.Boundary.TauRealPi](/verify/taulib/docs/book-i-boundary-tau-real-pi/)
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L271-L300)
- Source range: L271-L300
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `TauReal.pi` is Cauchy with explicit modulus `λ k => k + 3`. -/
```

## Source Excerpt

```lean
theorem TauReal.pi_isCauchy : TauReal.pi.IsCauchy := by
  refine ⟨fun k => k + 3, ?_⟩
  intro k m n hm hn
  change k + 3 ≤ m at hm
  change k + 3 ≤ n at hn
  unfold TauRat.lt
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat]
  show |((TauRat.pi_partial m).toRat - (TauRat.pi_partial n).toRat)|
         < 1 / ((k : Rat) + 1)
  by_cases h_le : n ≤ m
  · have h_n_ge : 1 ≤ n := by omega
    have h_bound := TauReal.pi_partial_cauchy_bound m n h_n_ge h_le
    have h_lt_final : (1 : Rat) / (2 * (n : Rat)) < 1 / ((k : Rat) + 1) :=
      Rat.one_div_two_n_lt_recip k n hn
    linarith
  · push_neg at h_le
    have h_m_ge : 1 ≤ m := by omega
    have h_swap_abs :
        |((TauRat.pi_partial m).toRat - (TauRat.pi_partial n).toRat)|
          = |((TauRat.pi_partial n).toRat - (TauRat.pi_partial m).toRat)| := by
      rw [show (TauRat.pi_partial m).toRat - (TauRat.pi_partial n).toRat
            = -((TauRat.pi_partial n).toRat - (TauRat.pi_partial m).toRat) from by ring,
          abs_neg]
    rw [h_swap_abs]
    have h_bound := TauReal.pi_partial_cauchy_bound n m h_m_ge (Nat.le_of_lt h_le)
    have h_lt_final : (1 : Rat) / (2 * (m : Rat)) < 1 / ((k : Rat) + 1) :=
      Rat.one_div_two_n_lt_recip k m hm
    linarith

end Tau.Boundary
```

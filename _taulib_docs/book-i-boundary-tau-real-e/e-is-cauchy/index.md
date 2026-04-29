---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.e_isCauchy",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-e/e-is-cauchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealE::TauReal.e_isCauchy",
  "declaration_slug": "e-is-cauchy",
  "kind": "theorem",
  "name": "TauReal.e_isCauchy",
  "module_name": "TauLib.BookI.Boundary.TauRealE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-e/",
  "source_line_start": 178,
  "source_line_end": 208,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L178-L208",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L178-L208",
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

- Module: [TauLib.BookI.Boundary.TauRealE](/verify/taulib/docs/book-i-boundary-tau-real-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L178-L208)
- Source range: L178-L208
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `TauReal.e` is Cauchy with explicit modulus `λ k => k + 3`. -/
```

## Source Excerpt

```lean
theorem TauReal.e_isCauchy : TauReal.e.IsCauchy := by
  refine ⟨fun k => k + 3, ?_⟩
  intro k m n hm hn
  -- After beta-reduction, hm : k + 3 ≤ m and hn : k + 3 ≤ n
  change k + 3 ≤ m at hm
  change k + 3 ≤ n at hn
  unfold TauRat.lt
  rw [TauRat.toRat_abs, toRat_sub, TauRat.ofNatRecip_toRat]
  show |((TauRat.e_partial m).toRat - (TauRat.e_partial n).toRat)|
         < 1 / ((k : Rat) + 1)
  by_cases h_le : n ≤ m
  · have h_n_ge : 1 ≤ n := by omega
    have h_bound := TauReal.e_partial_cauchy_bound m n h_n_ge h_le
    have h_lt_final : (4 : Rat) / (2 : Rat) ^ n < 1 / ((k : Rat) + 1) :=
      Rat.four_div_two_pow_lt_recip k n hn
    linarith
  · push_neg at h_le
    have h_m_ge : 1 ≤ m := by omega
    have h_swap_abs :
        |((TauRat.e_partial m).toRat - (TauRat.e_partial n).toRat)|
          = |((TauRat.e_partial n).toRat - (TauRat.e_partial m).toRat)| := by
      rw [show (TauRat.e_partial m).toRat - (TauRat.e_partial n).toRat
            = -((TauRat.e_partial n).toRat - (TauRat.e_partial m).toRat) from by ring,
          abs_neg]
    rw [h_swap_abs]
    have h_bound := TauReal.e_partial_cauchy_bound n m h_m_ge (Nat.le_of_lt h_le)
    have h_lt_final : (4 : Rat) / (2 : Rat) ^ m < 1 / ((k : Rat) + 1) :=
      Rat.four_div_two_pow_lt_recip k m hm
    linarith

end Tau.Boundary
```

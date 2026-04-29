---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.mul_inv_cancel",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-inv/mul-inv-cancel/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealInv::TauReal.mul_inv_cancel",
  "declaration_slug": "mul-inv-cancel",
  "kind": "theorem",
  "name": "TauReal.mul_inv_cancel",
  "module_name": "TauLib.BookI.Boundary.TauRealInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/",
  "source_line_start": 132,
  "source_line_end": 156,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L132-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L132-L156",
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
- Source path: [`TauLib/BookI/Boundary/TauRealInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L132-L156)
- Source range: L132-L156
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `a * a.inv ≡ 1` up to `TauReal.equiv`, when `a` is bounded away
    from zero.

    Strategy: past the `BoundedAwayFromZero` modulus `N`, every
    `a.approx n` is nonzero, so `a.inv.approx n` takes the
    `TauRat.inv` branch and `a.approx n * a.inv.approx n = 1` by
    `TauRat.mul_inv_cancel`.  The pointwise difference with
    `TauReal.one.approx n = TauRat.one` is then equivalence to zero. -/
```

## Source Excerpt

```lean
theorem TauReal.mul_inv_cancel (a : TauReal) (h : a.BoundedAwayFromZero) :
    TauReal.equiv (a.mul a.inv) TauReal.one := by
  obtain ⟨k₀, N₀, hN₀⟩ := h
  refine ⟨fun _ => N₀, fun k n hn => ?_⟩
  have h_nz := TauReal.is_nonzero_of_bounded_away hN₀ n hn
  -- Goal: the Cauchy bound on |(a.mul a.inv).approx n - 1|
  unfold TauRat.lt
  rw [TauRat.toRat_abs, toRat_sub]
  -- Compute (a.mul a.inv).approx n = a.approx n * a.inv.approx n
  -- With h_nz : (a.approx n).is_nonzero, a.inv.approx n = (a.approx n).inv h_nz
  have h_inv_val : (a.inv).approx n = TauRat.inv (a.approx n) h_nz := by
    show (if h : (a.approx n).is_nonzero then TauRat.inv (a.approx n) h
          else TauRat.one) = TauRat.inv (a.approx n) h_nz
    rw [dif_pos h_nz]
  have h_prod : ((a.mul a.inv).approx n).toRat = 1 := by
    show ((a.approx n).mul (a.inv.approx n)).toRat = 1
    rw [h_inv_val, toRat_mul, toRat_inv]
    have h_toRat_ne := (TauRat.is_nonzero_iff_toRat_ne_zero (a.approx n)).mp h_nz
    field_simp
  have h_one : (TauReal.one.approx n).toRat = 1 := by
    show TauRat.one.toRat = 1
    exact toRat_one
  rw [h_prod, h_one]
  simp
  exact TauRat.ofNatRecip_pos k
```

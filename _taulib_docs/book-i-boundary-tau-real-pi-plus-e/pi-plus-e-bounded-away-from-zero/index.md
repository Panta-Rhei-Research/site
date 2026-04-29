---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.pi_plus_e_boundedAwayFromZero",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/pi-plus-e-bounded-away-from-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauReal.pi_plus_e_boundedAwayFromZero",
  "declaration_slug": "pi-plus-e-bounded-away-from-zero",
  "kind": "theorem",
  "name": "TauReal.pi_plus_e_boundedAwayFromZero",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 145,
  "source_line_end": 169,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L145-L169",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPiPlusE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L145-L169",
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

- Module: [TauLib.BookI.Boundary.TauRealPiPlusE](/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L145-L169)
- Source range: L145-L169
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `TauReal.pi + TauReal.e` is bounded away from zero — the sum
    exceeds `1/(0+1) = 1` at every index `n ≥ 1`, and with room to
    spare (we could use any tolerance `1/(k+1)` for small `k` by
    taking `N = 1`).  We pick the minimal witness:
    `modulus = 0`, `N = 1`. -/
```

## Source Excerpt

```lean
theorem TauReal.pi_plus_e_boundedAwayFromZero :
    (TauReal.pi.add TauReal.e).BoundedAwayFromZero := by
  refine ⟨0, 1, fun n hn => ?_⟩
  -- Goal: TauRat.lt (ofNatRecip 0) ((pi.add e).approx n).abs
  unfold TauRat.lt
  rw [TauRat.ofNatRecip_toRat]
  -- ofNatRecip 0 .toRat = 1 / (0 + 1) = 1
  show (1 : Rat) / ((0 : Nat) + 1) < ((TauReal.pi.add TauReal.e).approx n).abs.toRat
  -- (pi.add e).approx n = (pi.approx n).add (e.approx n) = pi_partial n + e_partial n  (as TauRat)
  have h_add_approx :
      ((TauReal.pi.add TauReal.e).approx n).toRat
        = (TauRat.pi_partial n).toRat + (TauRat.e_partial n).toRat := by
    show ((TauReal.pi.approx n).add (TauReal.e.approx n)).toRat = _
    rw [toRat_add]
    rfl
  -- The value is positive; abs = value at toRat level.
  have h_pos : 0 < ((TauReal.pi.add TauReal.e).approx n).toRat := by
    rw [h_add_approx]
    have h_bound := TauReal.pi_plus_e_partial_lower_bound n hn
    linarith
  rw [TauRat.toRat_abs, abs_of_pos h_pos, h_add_approx]
  -- Goal: 1 / (0 + 1) < pi_partial n .toRat + e_partial n .toRat
  have h_bound := TauReal.pi_plus_e_partial_lower_bound n hn
  push_cast
  linarith
```

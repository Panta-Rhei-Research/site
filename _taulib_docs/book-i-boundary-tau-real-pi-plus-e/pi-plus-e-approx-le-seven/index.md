---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.pi_plus_e_approx_le_seven",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/pi-plus-e-approx-le-seven/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauReal.pi_plus_e_approx_le_seven",
  "declaration_slug": "pi-plus-e-approx-le-seven",
  "kind": "theorem",
  "name": "TauReal.pi_plus_e_approx_le_seven",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 319,
  "source_line_end": 330,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L319-L330",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L319-L330",
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
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L319-L330)
- Source range: L319-L330
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Master upper bound**: `(π + e).approx n .toRat ≤ 7` for every
    `n`.  Combines `pi_partial_le_19_div_6` and `e_partial_le_three`:
    `19/6 + 3 = 19/6 + 18/6 = 37/6 ≈ 6.17 ≤ 7`. -/
```

## Source Excerpt

```lean
theorem TauReal.pi_plus_e_approx_le_seven (n : Nat) :
    ((TauReal.pi.add TauReal.e).approx n).toRat ≤ 7 := by
  show ((TauReal.pi.approx n).add (TauReal.e.approx n)).toRat ≤ 7
  rw [toRat_add]
  have h_pi := TauRat.pi_partial_le_19_div_6 n
  have h_e := TauRat.e_partial_le_three n
  -- pi.approx n = pi_partial n, e.approx n = e_partial n (definitional)
  show (TauReal.pi.approx n).toRat + (TauReal.e.approx n).toRat ≤ 7
  have h_pi_unfold : (TauReal.pi.approx n).toRat = (TauRat.pi_partial n).toRat := rfl
  have h_e_unfold : (TauReal.e.approx n).toRat = (TauRat.e_partial n).toRat := rfl
  rw [h_pi_unfold, h_e_unfold]
  linarith
```

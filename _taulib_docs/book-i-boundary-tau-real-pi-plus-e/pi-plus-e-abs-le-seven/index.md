---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.pi_plus_e_abs_le_seven",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/pi-plus-e-abs-le-seven/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauReal.pi_plus_e_abs_le_seven",
  "declaration_slug": "pi-plus-e-abs-le-seven",
  "kind": "theorem",
  "name": "TauReal.pi_plus_e_abs_le_seven",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 337,
  "source_line_end": 344,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L337-L344",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPiPlusE",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L337-L344",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.TauRealPiPlusE](/corpus/taulib/docs/book-i-boundary-tau-real-pi-plus-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L337-L344)
- Source range: L337-L344
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The bound theorem consumed by `coupling_identity`**: for every
    `n`, the absolute value of `(π + e).approx n` is bounded above
    by `7`.  Since the approximation is non-negative
    (`pi_plus_e_approx_nonneg`), `abs = value`, and the bound is the
    pointwise `≤ 7` established above. -/
```

## Source Excerpt

```lean
theorem TauReal.pi_plus_e_abs_le_seven (n : Nat) :
    ((TauReal.pi.add TauReal.e).approx n).abs.toRat ≤ 7 := by
  rw [TauRat.toRat_abs]
  have h_nonneg := TauReal.pi_plus_e_approx_nonneg n
  rw [abs_of_nonneg h_nonneg]
  exact TauReal.pi_plus_e_approx_le_seven n

end Tau.Boundary
```

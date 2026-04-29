---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.abs_of_equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-of-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAbs::TauReal.abs_of_equiv",
  "declaration_slug": "abs-of-equiv",
  "kind": "theorem",
  "name": "TauReal.abs_of_equiv",
  "module_name": "TauLib.BookI.Boundary.TauRealAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/",
  "source_line_start": 103,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L103-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L103-L114",
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
- Source path: [`TauLib/BookI/Boundary/TauRealAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L103-L114)
- Source range: L103-L114
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `abs` is well-defined modulo `TauReal.equiv`: if `a ≡ b` then
    `a.abs ≡ b.abs`. -/
```

## Source Excerpt

```lean
theorem TauReal.abs_of_equiv {a b : TauReal} (h : TauReal.equiv a b) :
    TauReal.equiv a.abs b.abs := by
  obtain ⟨μ, h_mod⟩ := h
  refine ⟨μ, fun k n hn => ?_⟩
  have h_orig := h_mod k n hn
  unfold TauRat.lt at h_orig ⊢
  rw [TauRat.toRat_abs, toRat_sub] at h_orig
  rw [TauRat.toRat_abs, toRat_sub]
  have h_rev := TauRat.abs_sub_abs_le_abs_sub_toRat (a.approx n) (b.approx n)
  -- Normalize `a.abs.approx n` to `(a.approx n).abs` for linarith
  show |((a.approx n).abs).toRat - ((b.approx n).abs).toRat| < (TauRat.ofNatRecip k).toRat
  linarith
```

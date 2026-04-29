---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.abs_preserves_cauchy",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs-preserves-cauchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAbs::TauReal.abs_preserves_cauchy",
  "declaration_slug": "abs-preserves-cauchy",
  "kind": "theorem",
  "name": "TauReal.abs_preserves_cauchy",
  "module_name": "TauLib.BookI.Boundary.TauRealAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/",
  "source_line_start": 122,
  "source_line_end": 132,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L122-L132",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L122-L132",
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
- Source path: [`TauLib/BookI/Boundary/TauRealAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L122-L132)
- Source range: L122-L132
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `abs` preserves the Cauchy property: if `a` is Cauchy with modulus
    `μ`, so is `a.abs` with the same modulus. -/
```

## Source Excerpt

```lean
theorem TauReal.abs_preserves_cauchy {a : TauReal}
    (h : TauReal.IsCauchy a) : TauReal.IsCauchy a.abs := by
  obtain ⟨μ, h_mod⟩ := h
  refine ⟨μ, fun k m n hm hn => ?_⟩
  have h_orig := h_mod k m n hm hn
  unfold TauRat.lt at h_orig ⊢
  rw [TauRat.toRat_abs, toRat_sub] at h_orig
  rw [TauRat.toRat_abs, toRat_sub]
  have h_rev := TauRat.abs_sub_abs_le_abs_sub_toRat (a.approx m) (a.approx n)
  show |((a.approx m).abs).toRat - ((a.approx n).abs).toRat| < (TauRat.ofNatRecip k).toRat
  linarith
```

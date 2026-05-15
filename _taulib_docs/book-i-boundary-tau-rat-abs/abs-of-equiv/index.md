---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.abs_of_equiv",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/abs-of-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatAbs::TauRat.abs_of_equiv",
  "declaration_slug": "abs-of-equiv",
  "kind": "theorem",
  "name": "TauRat.abs_of_equiv",
  "module_name": "TauLib.BookI.Boundary.TauRatAbs",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/",
  "source_line_start": 151,
  "source_line_end": 160,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L151-L160",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatAbs",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-abs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L151-L160",
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

- Module: [TauLib.BookI.Boundary.TauRatAbs](/corpus/taulib/docs/book-i-boundary-tau-rat-abs/)
- Source path: [`TauLib/BookI/Boundary/TauRatAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L151-L160)
- Source range: L151-L160
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `abs` respects `TauRat.equiv`. -/
```

## Source Excerpt

```lean
theorem TauRat.abs_of_equiv {a b : TauRat} (h : TauRat.equiv a b) :
    TauRat.equiv a.abs b.abs := by
  rw [equiv_iff_toRat_eq] at h
  rw [equiv_iff_toRat_eq]
  by_cases ha : 0 ≤ a.toRat
  · have hb : 0 ≤ b.toRat := h ▸ ha
    rw [toRat_abs_of_nonneg ha, toRat_abs_of_nonneg hb, h]
  · push_neg at ha
    have hb : b.toRat < 0 := h ▸ ha
    rw [toRat_abs_of_neg ha, toRat_abs_of_neg hb, h]
```

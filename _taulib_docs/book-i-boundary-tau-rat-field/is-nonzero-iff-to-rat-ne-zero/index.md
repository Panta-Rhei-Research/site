---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.is_nonzero_iff_toRat_ne_zero",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/is-nonzero-iff-to-rat-ne-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatField`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatField::TauRat.is_nonzero_iff_toRat_ne_zero",
  "declaration_slug": "is-nonzero-iff-to-rat-ne-zero",
  "kind": "theorem",
  "name": "TauRat.is_nonzero_iff_toRat_ne_zero",
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/",
  "source_line_start": 186,
  "source_line_end": 201,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L186-L201",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatField",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L186-L201",
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

- Module: [TauLib.BookI.Boundary.TauRatField](/corpus/taulib/docs/book-i-boundary-tau-rat-field/)
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L186-L201)
- Source range: L186-L201
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- is_nonzero iff toRat is nonzero. -/
```

## Source Excerpt

```lean
theorem TauRat.is_nonzero_iff_toRat_ne_zero (q : TauRat) :
    q.is_nonzero ↔ q.toRat ≠ 0 := by
  unfold TauRat.is_nonzero
  simp only [TauRat.toRat, ne_eq, div_eq_zero_iff]
  constructor
  · intro h_int
    push_neg
    refine ⟨?_, q.den_ne_zero_rat⟩
    intro h_zero
    apply h_int
    exact_mod_cast h_zero
  · intro h
    push_neg at h
    intro h_int
    apply h.1
    exact_mod_cast h_int
```

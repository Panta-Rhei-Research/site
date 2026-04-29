---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.equiv_symm",
  "permalink": "/verify/taulib/docs/book-i-boundary-constructive-reals/equiv-symm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ConstructiveReals`.",
  "declaration_id": "TauLib.BookI.Boundary.ConstructiveReals::TauReal.equiv_symm",
  "declaration_slug": "equiv-symm",
  "kind": "theorem",
  "name": "TauReal.equiv_symm",
  "module_name": "TauLib.BookI.Boundary.ConstructiveReals",
  "module_url": "/verify/taulib/docs/book-i-boundary-constructive-reals/",
  "source_line_start": 236,
  "source_line_end": 246,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L236-L246",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ConstructiveReals",
        "url": "/verify/taulib/docs/book-i-boundary-constructive-reals/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L236-L246",
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

- Module: [TauLib.BookI.Boundary.ConstructiveReals](/verify/taulib/docs/book-i-boundary-constructive-reals/)
- Source path: [`TauLib/BookI/Boundary/ConstructiveReals.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ConstructiveReals.lean#L236-L246)
- Source range: L236-L246
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauReal equivalence is symmetric. -/
```

## Source Excerpt

```lean
theorem TauReal.equiv_symm {a b : TauReal} (h : TauReal.equiv a b) :
    TauReal.equiv b a := by
  obtain ⟨modulus, hmod⟩ := h
  refine ⟨modulus, fun k n hn => ?_⟩
  have h_orig := hmod k n hn
  unfold TauRat.lt at h_orig ⊢
  rw [TauRat.toRat_abs, toRat_sub] at h_orig
  rw [TauRat.toRat_abs, toRat_sub]
  rw [show (b.approx n).toRat - (a.approx n).toRat =
         -((a.approx n).toRat - (b.approx n).toRat) from by ring, abs_neg]
  exact h_orig
```

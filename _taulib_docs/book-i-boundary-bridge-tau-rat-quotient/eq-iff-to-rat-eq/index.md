---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRatQ.eq_iff_toRat_eq",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/eq-iff-to-rat-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRatQ.eq_iff_toRat_eq",
  "declaration_slug": "eq-iff-to-rat-eq",
  "kind": "theorem",
  "name": "TauRatQ.eq_iff_toRat_eq",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 157,
  "source_line_end": 161,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L157-L161",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L157-L161",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L157-L161)
- Source range: L157-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem TauRatQ.eq_iff_toRat_eq (x y : TauRatQ) :
    x = y ↔ x.toRat = y.toRat := by
  refine Quotient.inductionOn₂ x y (fun a b => ?_)
  show (a.toQ = b.toQ) ↔ (a.toRat = b.toRat)
  rw [TauRat.toQ_eq_iff, equiv_iff_toRat_eq]
```

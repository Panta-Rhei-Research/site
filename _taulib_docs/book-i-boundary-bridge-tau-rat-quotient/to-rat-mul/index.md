---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRatQ.toRat_mul",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat-mul/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRatQ.toRat_mul",
  "declaration_slug": "to-rat-mul",
  "kind": "theorem",
  "name": "TauRatQ.toRat_mul",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 138,
  "source_line_end": 155,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L138-L155",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L138-L155",
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
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L138-L155)
- Source range: L138-L155
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
theorem TauRatQ.toRat_mul (x y : TauRatQ) :
    (TauRatQ.mul x y).toRat = x.toRat * y.toRat := by
  refine Quotient.inductionOn₂ x y (fun a b => ?_)
  exact Tau.Boundary.toRat_mul a b

@[simp] theorem TauRatQ.toRat_neg (x : TauRatQ) :
    (TauRatQ.neg x).toRat = -x.toRat := by
  refine Quotient.inductionOn x (fun a => ?_)
  show a.negate.toRat = -a.toRat
  exact toRat_negate a

@[simp] theorem TauRatQ.toRat_zero : TauRatQ.zero.toRat = 0 := by
  show TauRat.zero.toRat = 0
  exact Tau.Boundary.toRat_zero

@[simp] theorem TauRatQ.toRat_one : TauRatQ.one.toRat = 1 := by
  show TauRat.one.toRat = 1
  exact Tau.Boundary.toRat_one
```

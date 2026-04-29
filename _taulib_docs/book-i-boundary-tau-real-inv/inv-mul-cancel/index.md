---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.inv_mul_cancel",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-inv/inv-mul-cancel/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealInv::TauReal.inv_mul_cancel",
  "declaration_slug": "inv-mul-cancel",
  "kind": "theorem",
  "name": "TauReal.inv_mul_cancel",
  "module_name": "TauLib.BookI.Boundary.TauRealInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/",
  "source_line_start": 160,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L160-L163",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L160-L163",
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

- Module: [TauLib.BookI.Boundary.TauRealInv](/verify/taulib/docs/book-i-boundary-tau-real-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRealInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L160-L163)
- Source range: L160-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `a.inv * a ≡ 1` up to `TauReal.equiv`, when `a` is bounded away
    from zero.  Corollary of `mul_inv_cancel` via commutativity. -/
```

## Source Excerpt

```lean
theorem TauReal.inv_mul_cancel (a : TauReal) (h : a.BoundedAwayFromZero) :
    TauReal.equiv (a.inv.mul a) TauReal.one := by
  apply TauReal.equiv_trans _ (TauReal.mul_inv_cancel a h)
  exact taureal_mul_comm a.inv a
```

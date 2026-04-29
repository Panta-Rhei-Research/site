---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.div_self",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-inv/div-self/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealInv::TauReal.div_self",
  "declaration_slug": "div-self",
  "kind": "theorem",
  "name": "TauReal.div_self",
  "module_name": "TauLib.BookI.Boundary.TauRealInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/",
  "source_line_start": 166,
  "source_line_end": 170,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L166-L170",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L166-L170",
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
- Source path: [`TauLib/BookI/Boundary/TauRealInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L166-L170)
- Source range: L166-L170
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `a / a ≡ 1` up to `TauReal.equiv`, when `a` is bounded away from zero. -/
```

## Source Excerpt

```lean
theorem TauReal.div_self (a : TauReal) (h : a.BoundedAwayFromZero) :
    TauReal.equiv (a.div a) TauReal.one :=
  TauReal.mul_inv_cancel a h

end Tau.Boundary
```

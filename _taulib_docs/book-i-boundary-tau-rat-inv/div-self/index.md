---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.div_self",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-inv/div-self/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::TauRat.div_self",
  "declaration_slug": "div-self",
  "kind": "theorem",
  "name": "TauRat.div_self",
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 163,
  "source_line_end": 166,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L163-L166",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatInv",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L163-L166",
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

- Module: [TauLib.BookI.Boundary.TauRatInv](/corpus/taulib/docs/book-i-boundary-tau-rat-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L163-L166)
- Source range: L163-L166
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `q / q ≡ 1` up to `TauRat.equiv`, assuming `q` is nonzero. -/
```

## Source Excerpt

```lean
theorem TauRat.div_self (q : TauRat) (h : q.is_nonzero) :
    TauRat.equiv (q.div q h) TauRat.one := by
  rw [equiv_iff_toRat_eq, toRat_div, toRat_one]
  exact _root_.div_self ((TauRat.is_nonzero_iff_toRat_ne_zero q).mp h)
```

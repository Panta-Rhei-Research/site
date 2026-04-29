---
{
  "projection_kind": "taulib_declaration",
  "title": "toRat_div",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/to-rat-div/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::toRat_div",
  "declaration_slug": "to-rat-div",
  "kind": "theorem",
  "name": "toRat_div",
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 134,
  "source_line_end": 138,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L134-L138",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L134-L138",
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

- Module: [TauLib.BookI.Boundary.TauRatInv](/verify/taulib/docs/book-i-boundary-tau-rat-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L134-L138)
- Source range: L134-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `toRat` is a homomorphism with respect to division. -/
```

## Source Excerpt

```lean
theorem toRat_div (a b : TauRat) (hb : b.is_nonzero) :
    (a.div b hb).toRat = a.toRat / b.toRat := by
  unfold TauRat.div
  rw [toRat_mul, toRat_inv]
  rw [div_eq_mul_inv]
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.inv_num_toInt_pos",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/inv-num-to-int-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::TauRat.inv_num_toInt_pos",
  "declaration_slug": "inv-num-to-int-pos",
  "kind": "theorem",
  "name": "TauRat.inv_num_toInt_pos",
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 77,
  "source_line_end": 79,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L77-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L77-L79",
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
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L77-L79)
- Source range: L77-L79
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: `(⟨q.den, 0⟩ : TauInt).toInt = q.den`. -/
```

## Source Excerpt

```lean
private theorem TauRat.inv_num_toInt_pos (q : TauRat) :
    (⟨q.den, 0⟩ : TauInt).toInt = (q.den : Int) := by
  show (q.den : Int) - 0 = (q.den : Int); ring
```

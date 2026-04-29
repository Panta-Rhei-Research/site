---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.e_term_toRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-e/e-term-to-rat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealE::TauRat.e_term_toRat",
  "declaration_slug": "e-term-to-rat",
  "kind": "theorem",
  "name": "TauRat.e_term_toRat",
  "module_name": "TauLib.BookI.Boundary.TauRealE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-e/",
  "source_line_start": 50,
  "source_line_end": 53,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L50-L53",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L50-L53",
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

- Module: [TauLib.BookI.Boundary.TauRealE](/verify/taulib/docs/book-i-boundary-tau-real-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealE.lean#L50-L53)
- Source range: L50-L53
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
theorem TauRat.e_term_toRat (k : Nat) :
    (TauRat.e_term k).toRat = 1 / (Nat.factorial k : Rat) := by
  unfold TauRat.e_term TauRat.toRat TauInt.toInt
  push_cast; ring
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "denom_not_square_at_7",
  "permalink": "/verify/taulib/docs/book-i-coordinates-iterated-prime/denom-not-square-at-7/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.IteratedPrime`.",
  "declaration_id": "TauLib.BookI.Coordinates.IteratedPrime::denom_not_square_at_7",
  "declaration_slug": "denom-not-square-at-7",
  "kind": "theorem",
  "name": "denom_not_square_at_7",
  "module_name": "TauLib.BookI.Coordinates.IteratedPrime",
  "module_url": "/verify/taulib/docs/book-i-coordinates-iterated-prime/",
  "source_line_start": 308,
  "source_line_end": 309,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L308-L309",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.IteratedPrime",
        "url": "/verify/taulib/docs/book-i-coordinates-iterated-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L308-L309",
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

- Module: [TauLib.BookI.Coordinates.IteratedPrime](/verify/taulib/docs/book-i-coordinates-iterated-prime/)
- Source path: [`TauLib/BookI/Coordinates/IteratedPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L308-L309)
- Source range: L308-L309
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- For N = 7: 15·7! = 75600 is NOT a perfect square.
    Verified: no m ∈ {0,...,274} satisfies m² = 75600 (and m ≥ 275 ⟹ m² ≥ 75625 > 75600). -/
```

## Source Excerpt

```lean
theorem denom_not_square_at_7 :
    (List.range 275).all (fun m => m * m != 75600) = true := by native_decide
```

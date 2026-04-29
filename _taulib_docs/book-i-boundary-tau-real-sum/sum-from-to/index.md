---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.sumFromTo",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealSum`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealSum::TauRat.sumFromTo",
  "declaration_slug": "sum-from-to",
  "kind": "def",
  "name": "TauRat.sumFromTo",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/",
  "source_line_start": 99,
  "source_line_end": 106,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L99-L106",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealSum",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L99-L106",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Boundary.TauRealSum](/verify/taulib/docs/book-i-boundary-tau-real-sum/)
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L99-L106)
- Source range: L99-L106
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ranged sum `sumFromTo f n m = Σ_{k=n}^{m-1} f k`, by recursion on
    the upper bound.  When `m ≤ n` the sum is zero. -/
```

## Source Excerpt

```lean
def TauRat.sumFromTo (f : Nat → TauRat) (n : Nat) : Nat → TauRat
  | 0 => TauRat.zero
  | m + 1 =>
    if n ≤ m then (TauRat.sumFromTo f n m).add (f m)
    else TauRat.zero

@[simp] theorem TauRat.sumFromTo_zero (f : Nat → TauRat) (n : Nat) :
    TauRat.sumFromTo f n 0 = TauRat.zero := rfl
```

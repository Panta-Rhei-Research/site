---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.sum",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-sum/sum/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealSum`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealSum::TauRat.sum",
  "declaration_slug": "sum",
  "kind": "def",
  "name": "TauRat.sum",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-sum/",
  "source_line_start": 83,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L83-L91",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L83-L91",
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
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L83-L91)
- Source range: L83-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Partial sum from 0: `sum f n = Σ_{k=0}^{n-1} f k`. -/
```

## Source Excerpt

```lean
def TauRat.sum (f : Nat → TauRat) : Nat → TauRat
  | 0 => TauRat.zero
  | n + 1 => (TauRat.sum f n).add (f n)

@[simp] theorem TauRat.sum_zero (f : Nat → TauRat) :
    TauRat.sum f 0 = TauRat.zero := rfl

@[simp] theorem TauRat.sum_succ (f : Nat → TauRat) (n : Nat) :
    TauRat.sum f (n + 1) = (TauRat.sum f n).add (f n) := rfl
```

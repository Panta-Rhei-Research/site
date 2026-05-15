---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.sumFromTo_self",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/sum-from-to-self/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealSum`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealSum::TauRat.sumFromTo_self",
  "declaration_slug": "sum-from-to-self",
  "kind": "theorem",
  "name": "TauRat.sumFromTo_self",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/",
  "source_line_start": 108,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L108-L114",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealSum",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L108-L114",
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

- Module: [TauLib.BookI.Boundary.TauRealSum](/corpus/taulib/docs/book-i-boundary-tau-real-sum/)
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L108-L114)
- Source range: L108-L114
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem TauRat.sumFromTo_self (f : Nat → TauRat) (n : Nat) :
    TauRat.sumFromTo f n n = TauRat.zero := by
  induction n with
  | zero => rfl
  | succ n _ =>
    show (if n + 1 ≤ n then _ else _) = _
    rw [if_neg (by omega)]
```

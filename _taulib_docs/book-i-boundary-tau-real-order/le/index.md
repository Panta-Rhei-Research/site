---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.le",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-order/le/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealOrder`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealOrder::TauReal.le",
  "declaration_slug": "le",
  "kind": "def",
  "name": "TauReal.le",
  "module_name": "TauLib.BookI.Boundary.TauRealOrder",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/",
  "source_line_start": 105,
  "source_line_end": 107,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L105-L107",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealOrder",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L105-L107",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Boundary.TauRealOrder](/corpus/taulib/docs/book-i-boundary-tau-real-order/)
- Source path: [`TauLib/BookI/Boundary/TauRealOrder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealOrder.lean#L105-L107)
- Source range: L105-L107
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Less-than-or-equal on `TauReal`: `a ≤ b` says that for every
    tolerance `1/(k+1)`, eventually `a.approx n < b.approx n + 1/(k+1)`.
    Equivalent to saying: `a − b` is ≤ any positive rational. -/
```

## Source Excerpt

```lean
def TauReal.le (a b : TauReal) : Prop :=
  ∀ k : Nat, ∃ N : Nat, ∀ n : Nat, N ≤ n →
    TauRat.lt (a.approx n) ((b.approx n).add (TauRat.ofNatRecip k))
```

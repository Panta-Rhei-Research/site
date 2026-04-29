---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_zero_minimum",
  "permalink": "/verify/taulib/docs/book-i-denotation-order/alpha-zero-minimum/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Order`.",
  "declaration_id": "TauLib.BookI.Denotation.Order::alpha_zero_minimum",
  "declaration_slug": "alpha-zero-minimum",
  "kind": "theorem",
  "name": "alpha_zero_minimum",
  "module_name": "TauLib.BookI.Denotation.Order",
  "module_url": "/verify/taulib/docs/book-i-denotation-order/",
  "source_line_start": 100,
  "source_line_end": 113,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L100-L113",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Order",
        "url": "/verify/taulib/docs/book-i-denotation-order/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L100-L113",
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

- Module: [TauLib.BookI.Denotation.Order](/verify/taulib/docs/book-i-denotation-order/)
- Source path: [`TauLib/BookI/Denotation/Order.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L100-L113)
- Source range: L100-L113
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- ⟨α, 0⟩ is the minimum element. -/
```

## Source Excerpt

```lean
theorem alpha_zero_minimum (x : TauObj) (hx : x ≠ ⟨alpha, 0⟩) :
    denotational_lt ⟨alpha, 0⟩ x := by
  cases x with | mk sx dx =>
  simp only [denotational_lt]
  cases sx with
  | alpha =>
    right; constructor; · rfl
    · cases dx with
      | zero => exact absurd rfl hx
      | succ d => omega
  | pi => left; decide
  | gamma => left; decide
  | eta => left; decide
  | omega => left; decide
```

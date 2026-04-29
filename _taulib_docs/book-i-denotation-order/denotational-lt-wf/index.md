---
{
  "projection_kind": "taulib_declaration",
  "title": "denotational_lt_wf",
  "permalink": "/verify/taulib/docs/book-i-denotation-order/denotational-lt-wf/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Order`.",
  "declaration_id": "TauLib.BookI.Denotation.Order::denotational_lt_wf",
  "declaration_slug": "denotational-lt-wf",
  "kind": "theorem",
  "name": "denotational_lt_wf",
  "module_name": "TauLib.BookI.Denotation.Order",
  "module_url": "/verify/taulib/docs/book-i-denotation-order/",
  "source_line_start": 154,
  "source_line_end": 159,
  "registry_ids": [
    "I.P07"
  ],
  "related_registry_items": [
    {
      "id": "I.P07",
      "title": "Well-Ordering of Obj(tau)",
      "url": "/registry/object/I.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L154-L159",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L154-L159",
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
- Source path: [`TauLib/BookI/Denotation/Order.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Order.lean#L154-L159)
- Source range: L154-L159
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P07` — Well-Ordering of Obj(tau)

## Immediate Comment / Docstring

```lean
/-- [I.P07] Well-foundedness of the denotational order:
    denotational_lt is a subrelation of the lexicographic order on (Nat, Nat),
    which is well-founded since Nat is well-ordered. -/
```

## Source Excerpt

```lean
theorem denotational_lt_wf : WellFounded denotational_lt :=
  Subrelation.wf
    (fun h => denotational_lt_sub_lex h)
    (InvImage.wf lex_measure WellFoundedRelation.wf)

end Tau.Denotation
```

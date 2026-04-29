---
{
  "projection_kind": "taulib_declaration",
  "title": "no_unearned_decimal_diagonal",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/no-unearned-decimal-diagonal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::no_unearned_decimal_diagonal",
  "declaration_slug": "no-unearned-decimal-diagonal",
  "kind": "theorem",
  "name": "no_unearned_decimal_diagonal",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 68,
  "source_line_end": 72,
  "registry_ids": [
    "I.P34"
  ],
  "related_registry_items": [
    {
      "id": "I.P34",
      "title": "No Unearned Decimal Diagonal",
      "url": "/registry/object/I.P34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L68-L72",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.CantorRefutation",
        "url": "/verify/taulib/docs/book-i-sets-cantor-refutation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L68-L72",
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

- Module: [TauLib.BookI.Sets.CantorRefutation](/verify/taulib/docs/book-i-sets-cantor-refutation/)
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L68-L72)
- Source range: L68-L72
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P34` — No Unearned Decimal Diagonal

## Immediate Comment / Docstring

```lean
/-- [I.P34] No Unearned Decimal Diagonal: no extractor can have its
    diagonal avoid all rows.

    Proof: the avoidance condition diagonal(n) != extract(n, n) directly
    contradicts diagonal_def which says diagonal(n) = extract(n, n).
    This is the liar-paradox core of the diagonal argument, and tau
    blocks it by making diagonal extraction self-referential. -/
```

## Source Excerpt

```lean
theorem no_unearned_decimal_diagonal :
    ¬ exists (E : DecimalDiagonalExtractor),
      forall n, E.diagonal n ≠ E.extract n n := by
  intro ⟨E, h⟩
  exact h 0 (E.diagonal_def 0)
```

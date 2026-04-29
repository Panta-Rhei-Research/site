---
{
  "projection_kind": "taulib_declaration",
  "title": "cantor_inapplicable",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/cantor-inapplicable/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::cantor_inapplicable",
  "declaration_slug": "cantor-inapplicable",
  "kind": "theorem",
  "name": "cantor_inapplicable",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 163,
  "source_line_end": 166,
  "registry_ids": [
    "I.T35"
  ],
  "related_registry_items": [
    {
      "id": "I.T35",
      "title": "Cantor Diagonal Inapplicability",
      "url": "/registry/object/I.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L163-L166",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L163-L166",
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
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L163-L166)
- Source range: L163-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T35` — Cantor Diagonal Inapplicability

## Immediate Comment / Docstring

```lean
/-- [I.T35] Cantor Diagonal Inapplicability Theorem:
    No CantorDiagonalApparatus can exist in Category tau.

    The proof is immediate from any ONE of the three failures:
    - P34: avoidance contradicts diagonal_def
    - P35: comprehension contradicts no_russell_set
    - P36: self-pairing contradicts divisibility at 0

    We use P34 (the simplest). The three failures are independent
    and each individually blocks the diagonal argument. -/
```

## Source Excerpt

```lean
theorem cantor_inapplicable :
    ¬ exists (_ : CantorDiagonalApparatus), True := by
  intro ⟨A, _⟩
  exact A.avoids 0 (A.extractor.diagonal_def 0)
```

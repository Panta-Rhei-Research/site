---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_tetration_eq",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-tetration-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::idx_tetration_eq",
  "declaration_slug": "idx-tetration-eq",
  "kind": "theorem",
  "name": "idx_tetration_eq",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 101,
  "source_line_end": 106,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L101-L106",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Arithmetic",
        "url": "/verify/taulib/docs/book-i-denotation-arithmetic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L101-L106",
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

- Module: [TauLib.BookI.Denotation.Arithmetic](/verify/taulib/docs/book-i-denotation-arithmetic/)
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L101-L106)
- Source range: L101-L106
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Bridge lemma: idx_tetration matches the Nat tetration from Ladder. -/
```

## Source Excerpt

```lean
theorem idx_tetration_eq (n m : TauIdx) :
    idx_tetration n m = tetration n m := by
  induction m with
  | zero => simp [idx_tetration, tetration]
  | succ m ih =>
    simp only [idx_tetration, tetration, idx_exp_eq_nat_pow, ih]
```

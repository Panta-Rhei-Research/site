---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_tetration",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-tetration/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::idx_tetration",
  "declaration_slug": "idx-tetration",
  "kind": "def",
  "name": "idx_tetration",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 95,
  "source_line_end": 98,
  "registry_ids": [
    "I.D13"
  ],
  "related_registry_items": [
    {
      "id": "I.D13",
      "title": "Index Tetration",
      "url": "/registry/object/I.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L95-L98",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L95-L98",
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

- Module: [TauLib.BookI.Denotation.Arithmetic](/verify/taulib/docs/book-i-denotation-arithmetic/)
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L95-L98)
- Source range: L95-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D13` — Index Tetration

## Immediate Comment / Docstring

```lean
/-- [I.D13] Index tetration: iterated exponentiation (right-associative tower).
    ⁿm means n^(n^(n^...)) with m copies of n. -/
```

## Source Excerpt

```lean
def idx_tetration (n m : TauIdx) : TauIdx :=
  match m with
  | 0 => 1
  | m + 1 => idx_exp n (idx_tetration n m)
```

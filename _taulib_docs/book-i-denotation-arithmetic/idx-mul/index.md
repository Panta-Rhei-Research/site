---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_mul",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-mul/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::idx_mul",
  "declaration_slug": "idx-mul",
  "kind": "def",
  "name": "idx_mul",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 58,
  "source_line_end": 61,
  "registry_ids": [
    "I.D11"
  ],
  "related_registry_items": [
    {
      "id": "I.D11",
      "title": "Index Multiplication",
      "url": "/registry/object/I.D11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L58-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L58-L61",
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
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L58-L61)
- Source range: L58-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D11` — Index Multiplication

## Immediate Comment / Docstring

```lean
/-- [I.D11] Index multiplication: iterated addition. -/
```

## Source Excerpt

```lean
def idx_mul (n m : TauIdx) : TauIdx :=
  match m with
  | 0 => 0
  | m + 1 => idx_add (idx_mul n m) n
```

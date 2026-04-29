---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_exp",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-exp/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::idx_exp",
  "declaration_slug": "idx-exp",
  "kind": "def",
  "name": "idx_exp",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 76,
  "source_line_end": 79,
  "registry_ids": [
    "I.D12"
  ],
  "related_registry_items": [
    {
      "id": "I.D12",
      "title": "Index Exponentiation",
      "url": "/registry/object/I.D12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L76-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L76-L79",
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
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L76-L79)
- Source range: L76-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D12` — Index Exponentiation

## Immediate Comment / Docstring

```lean
/-- [I.D12] Index exponentiation: iterated multiplication. -/
```

## Source Excerpt

```lean
def idx_exp (n m : TauIdx) : TauIdx :=
  match m with
  | 0 => 1
  | m + 1 => idx_mul (idx_exp n m) n
```

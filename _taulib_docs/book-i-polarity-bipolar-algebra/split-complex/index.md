---
{
  "projection_kind": "taulib_declaration",
  "title": "SplitComplex",
  "permalink": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/split-complex/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.BipolarAlgebra::SplitComplex",
  "declaration_slug": "split-complex",
  "kind": "structure",
  "name": "SplitComplex",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/",
  "source_line_start": 53,
  "source_line_end": 58,
  "registry_ids": [
    "I.D27"
  ],
  "related_registry_items": [
    {
      "id": "I.D27",
      "title": "Bipolar Spectral Algebra",
      "url": "/registry/object/I.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L53-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.BipolarAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-bipolar-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L53-L58",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.Polarity.BipolarAlgebra](/verify/taulib/docs/book-i-polarity-bipolar-algebra/)
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L53-L58)
- Source range: L53-L58
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D27` — Bipolar Spectral Algebra

## Immediate Comment / Docstring

```lean
/-- [I.D27] Split-complex number: a + bj where j² = +1.
    Represented as a pair of integers. -/
```

## Source Excerpt

```lean
structure SplitComplex where
  re : Int
  im : Int
  deriving DecidableEq, Repr

instance : Inhabited SplitComplex := ⟨⟨0, 0⟩⟩
```

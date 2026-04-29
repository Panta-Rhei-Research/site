---
{
  "projection_kind": "taulib_declaration",
  "title": "NFStep",
  "permalink": "/verify/taulib/docs/book-i-coordinates-normal-form/nfstep/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Coordinates.NormalForm`.",
  "declaration_id": "TauLib.BookI.Coordinates.NormalForm::NFStep",
  "declaration_slug": "nfstep",
  "kind": "structure",
  "name": "NFStep",
  "module_name": "TauLib.BookI.Coordinates.NormalForm",
  "module_url": "/verify/taulib/docs/book-i-coordinates-normal-form/",
  "source_line_start": 36,
  "source_line_end": 41,
  "registry_ids": [
    "I.D16"
  ],
  "related_registry_items": [
    {
      "id": "I.D16",
      "title": "NF Address Encoding",
      "url": "/registry/object/I.D16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L36-L41",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NormalForm",
        "url": "/verify/taulib/docs/book-i-coordinates-normal-form/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L36-L41",
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

- Module: [TauLib.BookI.Coordinates.NormalForm](/verify/taulib/docs/book-i-coordinates-normal-form/)
- Source path: [`TauLib/BookI/Coordinates/NormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NormalForm.lean#L36-L41)
- Source range: L36-L41
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D16` — NF Address Encoding

## Immediate Comment / Docstring

```lean
/-- [I.D16] A normal form step: (A, B, C, D) decomposing X = T(A,B,C) · D. -/
```

## Source Excerpt

```lean
structure NFStep where
  A : TauIdx
  B : TauIdx
  C : TauIdx
  D : TauIdx
  deriving Repr, DecidableEq
```

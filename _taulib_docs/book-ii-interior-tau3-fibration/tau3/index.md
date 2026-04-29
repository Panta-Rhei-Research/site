---
{
  "projection_kind": "taulib_declaration",
  "title": "Tau3",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau3-fibration/tau3/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Interior.Tau3Fibration`.",
  "declaration_id": "TauLib.BookII.Interior.Tau3Fibration::Tau3",
  "declaration_slug": "tau3",
  "kind": "structure",
  "name": "Tau3",
  "module_name": "TauLib.BookII.Interior.Tau3Fibration",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/",
  "source_line_start": 72,
  "source_line_end": 75,
  "registry_ids": [
    "II.D07"
  ],
  "related_registry_items": [
    {
      "id": "II.D07",
      "title": "Fibered Product tau^3",
      "url": "/registry/object/II.D07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L72-L75",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.Tau3Fibration",
        "url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L72-L75",
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

- Module: [TauLib.BookII.Interior.Tau3Fibration](/verify/taulib/docs/book-ii-interior-tau3-fibration/)
- Source path: [`TauLib/BookII/Interior/Tau3Fibration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L72-L75)
- Source range: L72-L75
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D07` — Fibered Product tau^3

## Immediate Comment / Docstring

```lean
/-- [II.D07] τ³ = τ¹ ×_f T²: the fibered product.
    A τ-admissible quadruple viewed as base + fiber. -/
```

## Source Excerpt

```lean
structure Tau3 where
  base  : BaseTau1
  fiber : FiberT2
  deriving Repr, DecidableEq
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberT2",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau3-fibration/fiber-t2/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Interior.Tau3Fibration`.",
  "declaration_id": "TauLib.BookII.Interior.Tau3Fibration::FiberT2",
  "declaration_slug": "fiber-t2",
  "kind": "structure",
  "name": "FiberT2",
  "module_name": "TauLib.BookII.Interior.Tau3Fibration",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/",
  "source_line_start": 61,
  "source_line_end": 64,
  "registry_ids": [
    "II.D06"
  ],
  "related_registry_items": [
    {
      "id": "II.D06",
      "title": "Fiber T^2",
      "url": "/registry/object/II.D06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L61-L64",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L61-L64",
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
- Source path: [`TauLib/BookII/Interior/Tau3Fibration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L61-L64)
- Source range: L61-L64
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D06` — Fiber T^2

## Immediate Comment / Docstring

```lean
/-- [II.D06] Fiber T²: the (B, C) coordinate space.
    B = exponent (γ-channel), C = tetration height (η-channel).
    Both non-negative (automatic for ℕ).
    Notation T² anticipates torus-like winding structure (Book II Part III). -/
```

## Source Excerpt

```lean
structure FiberT2 where
  b : TauIdx  -- exponent
  c : TauIdx  -- tetration height
  deriving Repr, DecidableEq
```

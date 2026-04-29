---
{
  "projection_kind": "taulib_declaration",
  "title": "TernaryDecomposition",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/ternary-decomposition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::TernaryDecomposition",
  "declaration_slug": "ternary-decomposition",
  "kind": "structure",
  "name": "TernaryDecomposition",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 48,
  "source_line_end": 55,
  "registry_ids": [
    "IV.P88"
  ],
  "related_registry_items": [
    {
      "id": "IV.P88",
      "title": "Ternary Decomposition of the η-Circle",
      "url": "/registry/object/IV.P88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L48-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.ColorHolonomy",
        "url": "/verify/taulib/docs/book-iv-strong-color-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L48-L55",
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

- Module: [TauLib.BookIV.Strong.ColorHolonomy](/verify/taulib/docs/book-iv-strong-color-holonomy/)
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L48-L55)
- Source range: L48-L55
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P88` — Ternary Decomposition of the η-Circle

## Immediate Comment / Docstring

```lean
/-- [IV.P88] At primorial depth 3, winding classes on the eta-circle
    decompose into exactly three equivalence classes modulo the strong
    vacuum normalization: color(n) = n mod 3 in {0, 1, 2}. -/
```

## Source Excerpt

```lean
structure TernaryDecomposition where
  /-- Number of color classes. -/
  num_classes : Nat := 3
  /-- Primorial depth that forces ternary structure. -/
  depth : Nat := 3
  /-- The classification is mod-3 reduction of eta-winding. -/
  classification : String := "n mod 3"
  deriving Repr
```

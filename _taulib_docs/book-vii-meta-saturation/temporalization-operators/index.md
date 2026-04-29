---
{
  "projection_kind": "taulib_declaration",
  "title": "TemporalizationOperators",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/temporalization-operators/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::TemporalizationOperators",
  "declaration_slug": "temporalization-operators",
  "kind": "structure",
  "name": "TemporalizationOperators",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 647,
  "source_line_end": 656,
  "registry_ids": [
    "VII.D53"
  ],
  "related_registry_items": [
    {
      "id": "VII.D53",
      "title": "Temporalization Operators",
      "url": "/registry/object/VII.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L647-L656",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L647-L656",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L647-L656)
- Source range: L647-L656
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D53` — Temporalization Operators

## Immediate Comment / Docstring

```lean
/-- [VII.D53] Temporalization Operators (ch61). Past/present/future
    operators acting on predications:
    Past(φ): φ was the case
    Present(φ): φ is the case
    Future(φ): φ will be the case
    These are internal modal operators in τ at E₃. -/
```

## Source Excerpt

```lean
structure TemporalizationOperators where
  /-- Past operator. -/
  has_past : Bool := true
  /-- Present operator. -/
  has_present : Bool := true
  /-- Future operator. -/
  has_future : Bool := true
  /-- Three temporal operators. -/
  operator_count : Nat := 3
  deriving Repr
```

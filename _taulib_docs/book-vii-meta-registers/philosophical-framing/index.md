---
{
  "projection_kind": "taulib_declaration",
  "title": "PhilosophicalFraming",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/philosophical-framing/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::PhilosophicalFraming",
  "declaration_slug": "philosophical-framing",
  "kind": "structure",
  "name": "PhilosophicalFraming",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 705,
  "source_line_end": 712,
  "registry_ids": [
    "VII.D29"
  ],
  "related_registry_items": [
    {
      "id": "VII.D29",
      "title": "τ³ Philosophical Framing",
      "url": "/registry/object/VII.D29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L705-L712",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L705-L712",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L705-L712)
- Source range: L705-L712
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D29` — τ³ Philosophical Framing

## Immediate Comment / Docstring

```lean
/-- [VII.D29] τ³ Philosophical Framing (ch21). The central object
    τ³ = τ¹ ×_f T² read philosophically: fiber T² = internal
    (microcosm), base τ¹ = external (macrocosm), fibered product =
    their structural unity. -/
```

## Source Excerpt

```lean
structure PhilosophicalFraming where
  /-- Fiber = internal (microcosm). -/
  fiber_internal : Bool := true
  /-- Base = external (macrocosm). -/
  base_external : Bool := true
  /-- Fibered product = unity. -/
  fibered_unity : Bool := true
  deriving Repr
```

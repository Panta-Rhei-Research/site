---
{
  "projection_kind": "taulib_declaration",
  "title": "Tau3Arena",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/tau3-arena/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::Tau3Arena",
  "declaration_slug": "tau3-arena",
  "kind": "structure",
  "name": "Tau3Arena",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 102,
  "source_line_end": 110,
  "registry_ids": [
    "IV.D254"
  ],
  "related_registry_items": [
    {
      "id": "IV.D254",
      "title": "Fibered product arena tau^3",
      "url": "/registry/object/IV.D254/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L102-L110",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.Tau3Arena",
        "url": "/verify/taulib/docs/book-iv-arena-tau3-arena/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L102-L110",
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

- Module: [TauLib.BookIV.Arena.Tau3Arena](/verify/taulib/docs/book-iv-arena-tau3-arena/)
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L102-L110)
- Source range: L102-L110
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D254` — Fibered product arena tau^3

## Immediate Comment / Docstring

```lean
/-- [IV.D254] The arena τ³ = τ¹ ×_f T²: fibered product of base and fiber.
    Total generators: 2 + 3 = 5. Total physical dimensions: 1 + 3 = 4. -/
```

## Source Excerpt

```lean
structure Tau3Arena where
  /-- The temporal base. -/
  base : Tau1Base
  /-- The spatial fiber. -/
  fiber : FiberT2
  /-- Total generator count. -/
  total_gens : Nat
  total_eq : total_gens = base.gen_count + fiber.gen_count
  deriving Repr
```

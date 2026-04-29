---
{
  "projection_kind": "taulib_declaration",
  "title": "QuarkGenerations",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/quark-generations/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::QuarkGenerations",
  "declaration_slug": "quark-generations",
  "kind": "structure",
  "name": "QuarkGenerations",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 168,
  "source_line_end": 177,
  "registry_ids": [
    "IV.D189"
  ],
  "related_registry_items": [
    {
      "id": "IV.D189",
      "title": "Quark generations from \\Lemniscate",
      "url": "/registry/object/IV.D189/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L168-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L168-L177",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L168-L177)
- Source range: L168-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D189` — Quark generations from \Lemniscate

## Immediate Comment / Docstring

```lean
/-- [IV.D189] Three quark generations from three lemniscate mode classes:
    Gen 1 (u,d) = crossing-point modes
    Gen 2 (c,s) = single-lobe modes
    Gen 3 (t,b) = full-lemniscate modes -/
```

## Source Excerpt

```lean
structure QuarkGenerations where
  /-- Number of generations. -/
  num_generations : Nat := 3
  /-- Generation 1: crossing-point. -/
  gen1_class : LemniscateModeClass := .crossing
  /-- Generation 2: single-lobe. -/
  gen2_class : LemniscateModeClass := .singleLobe
  /-- Generation 3: full-lemniscate. -/
  gen3_class : LemniscateModeClass := .fullL
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "SU2Generator",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/su2-generator/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::SU2Generator",
  "declaration_slug": "su2-generator",
  "kind": "structure",
  "name": "SU2Generator",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 66,
  "source_line_end": 73,
  "registry_ids": [
    "IV.D116"
  ],
  "related_registry_items": [
    {
      "id": "IV.D116",
      "title": "Weak Isospin Generators",
      "url": "/registry/object/IV.D116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L66-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L66-L73",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L66-L73)
- Source range: L66-L73
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D116` — Weak Isospin Generators

## Immediate Comment / Docstring

```lean
/-- [IV.D116] The three SU(2) generators (Pauli matrices sigma_1, sigma_2, sigma_3).
    Each generator is a 2x2 traceless Hermitian matrix.
    In the tau-framework, these arise as the tangent directions
    at the crossing point of L. -/
```

## Source Excerpt

```lean
structure SU2Generator where
  /-- Generator index: 1, 2, or 3. -/
  index : Fin 3
  /-- Name label. -/
  name : String
  /-- Physical boson association. -/
  boson : String
  deriving Repr
```

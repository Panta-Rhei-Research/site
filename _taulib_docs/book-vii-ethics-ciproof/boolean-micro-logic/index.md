---
{
  "projection_kind": "taulib_declaration",
  "title": "BooleanMicroLogic",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/boolean-micro-logic/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::BooleanMicroLogic",
  "declaration_slug": "boolean-micro-logic",
  "kind": "structure",
  "name": "BooleanMicroLogic",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 588,
  "source_line_end": 595,
  "registry_ids": [
    "VII.D57"
  ],
  "related_registry_items": [
    {
      "id": "VII.D57",
      "title": "Boolean Micro-Logic",
      "url": "/registry/object/VII.D57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L588-L595",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L588-L595",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L588-L595)
- Source range: L588-L595
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D57` — Boolean Micro-Logic

## Immediate Comment / Docstring

```lean
/-- [VII.D57] Boolean Micro-Logic (ch39). Single-address classical
    logic: at a single NF-address, propositions are 2-valued and
    decidable. Boolean algebra of propositions applies. -/
```

## Source Excerpt

```lean
structure BooleanMicroLogic where
  /-- Single NF-address scope. -/
  single_address : Bool := true
  /-- 2-valued (true/false). -/
  two_valued : Bool := true
  /-- Decidable propositions. -/
  decidable : Bool := true
  deriving Repr
```

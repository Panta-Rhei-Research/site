---
{
  "projection_kind": "taulib_declaration",
  "title": "InternalSetOntology",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/internal-set-ontology/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::InternalSetOntology",
  "declaration_slug": "internal-set-ontology",
  "kind": "structure",
  "name": "InternalSetOntology",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 600,
  "source_line_end": 605,
  "registry_ids": [
    "VII.D25"
  ],
  "related_registry_items": [
    {
      "id": "VII.D25",
      "title": "Internal Set Ontology",
      "url": "/registry/object/VII.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L600-L605",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L600-L605",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L600-L605)
- Source range: L600-L605
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D25` — Internal Set Ontology

## Immediate Comment / Docstring

```lean
/-- [VII.D25] Internal Set Ontology (ch18). NF-addressability = existence:
    to exist is to have an NF-address in the kernel. No object exists
    outside the NF-address space. -/
```

## Source Excerpt

```lean
structure InternalSetOntology where
  /-- NF-addressability as existence criterion. -/
  nf_is_existence : Bool := true
  /-- No objects outside NF-space. -/
  exhaustive : Bool := true
  deriving Repr
```

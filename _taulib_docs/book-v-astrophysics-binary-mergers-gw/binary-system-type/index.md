---
{
  "projection_kind": "taulib_declaration",
  "title": "BinarySystemType",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/binary-system-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::BinarySystemType",
  "declaration_slug": "binary-system-type",
  "kind": "inductive",
  "name": "BinarySystemType",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 70,
  "source_line_end": 79,
  "registry_ids": [
    "V.D133"
  ],
  "related_registry_items": [
    {
      "id": "V.D133",
      "title": "Binary Coherent-Instance System",
      "url": "/registry/object/V.D133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L70-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L70-L79",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L70-L79)
- Source range: L70-L79
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D133` — Binary Coherent-Instance System

## Immediate Comment / Docstring

```lean
/-- [V.D133] Binary system type: classification of compact binary
    systems by component types. -/
```

## Source Excerpt

```lean
inductive BinarySystemType where
  /-- BH-BH binary. -/
  | BHBH
  /-- NS-NS binary. -/
  | NSNS
  /-- BH-NS binary. -/
  | BHNS
  /-- WD-WD binary (Type Ia progenitor). -/
  | WDWD
  deriving Repr, DecidableEq, BEq
```

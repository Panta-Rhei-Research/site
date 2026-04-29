---
{
  "projection_kind": "taulib_declaration",
  "title": "ModalFrameTau",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/modal-frame-tau/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::ModalFrameTau",
  "declaration_slug": "modal-frame-tau",
  "kind": "structure",
  "name": "ModalFrameTau",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 796,
  "source_line_end": 803,
  "registry_ids": [
    "VII.D62"
  ],
  "related_registry_items": [
    {
      "id": "VII.D62",
      "title": "Modal Frame in τ",
      "url": "/registry/object/VII.D62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L796-L803",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L796-L803",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L796-L803)
- Source range: L796-L803
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D62` — Modal Frame in τ

## Immediate Comment / Docstring

```lean
/-- [VII.D62] Modal Frame in τ (ch43). Kripke frame (W, R) realized
    internally: worlds = NF-addresses, accessibility R = admissible
    transformations between addresses. No external possible worlds. -/
```

## Source Excerpt

```lean
structure ModalFrameTau where
  /-- Worlds = NF-addresses. -/
  worlds_as_addresses : Bool := true
  /-- Accessibility = admissible transformations. -/
  accessibility_admissible : Bool := true
  /-- Internal to τ. -/
  internal : Bool := true
  deriving Repr
```

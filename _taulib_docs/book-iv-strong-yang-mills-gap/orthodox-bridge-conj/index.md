---
{
  "projection_kind": "taulib_declaration",
  "title": "OrthodoxBridgeConj",
  "permalink": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/orthodox-bridge-conj/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.YangMillsGap`.",
  "declaration_id": "TauLib.BookIV.Strong.YangMillsGap::OrthodoxBridgeConj",
  "declaration_slug": "orthodox-bridge-conj",
  "kind": "structure",
  "name": "OrthodoxBridgeConj",
  "module_name": "TauLib.BookIV.Strong.YangMillsGap",
  "module_url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/",
  "source_line_start": 365,
  "source_line_end": 376,
  "registry_ids": [
    "IV.D179"
  ],
  "related_registry_items": [
    {
      "id": "IV.D179",
      "title": "Orthodox Bridge Conjecture",
      "url": "/registry/object/IV.D179/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L365-L376",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.YangMillsGap",
        "url": "/verify/taulib/docs/book-iv-strong-yang-mills-gap/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L365-L376",
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

- Module: [TauLib.BookIV.Strong.YangMillsGap](/verify/taulib/docs/book-iv-strong-yang-mills-gap/)
- Source path: [`TauLib/BookIV/Strong/YangMillsGap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/YangMillsGap.lean#L365-L376)
- Source range: L365-L376
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D179` — Orthodox Bridge Conjecture

## Immediate Comment / Docstring

```lean
/-- [IV.D179] Orthodox Bridge Conjecture: a readout functor satisfying
    gap preservation, spectral ordering, and multiplicity conditions
    exists, so tau-gap > 0 implies orthodox-gap > 0.

    This is the conjectural link between the tau-internal result
    (which IS proved) and the Millennium Problem (which requires
    the bridge to be established). -/
```

## Source Excerpt

```lean
structure OrthodoxBridgeConj where
  /-- Asserts existence of suitable readout functor. -/
  functor_exists : Bool := true
  /-- Gap preservation. -/
  gap_preserving : Bool := true
  /-- Spectral ordering. -/
  ordering : Bool := true
  /-- Multiplicity conditions. -/
  multiplicity : Bool := true
  /-- Scope: conjectural. -/
  scope : String := "conjectural"
  deriving Repr
```

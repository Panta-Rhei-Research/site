---
{
  "projection_kind": "taulib_declaration",
  "title": "MetaphysicsLoopClass",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/metaphysics-loop-class/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::MetaphysicsLoopClass",
  "declaration_slug": "metaphysics-loop-class",
  "kind": "structure",
  "name": "MetaphysicsLoopClass",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 226,
  "source_line_end": 231,
  "registry_ids": [
    "VII.D06"
  ],
  "related_registry_items": [
    {
      "id": "VII.D06",
      "title": "Metaphysics Loop Class",
      "url": "/registry/object/VII.D06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L226-L231",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L226-L231",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L226-L231)
- Source range: L226-L231
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D06` — Metaphysics Loop Class

## Immediate Comment / Docstring

```lean
/-- [VII.D06] Metaphysics Loop Class: internal loops γ ∈ π₁(X) where
    MetaDecode(γ) = γ. Law-predicate towers: each level governs below
    and is recognized above. -/
```

## Source Excerpt

```lean
structure MetaphysicsLoopClass where
  /-- Loops are fixed under MetaDecode. -/
  metadecode_fixed : Bool := true
  /-- Tower structure: each level governs level below. -/
  hierarchical : Bool := true
  deriving Repr
```

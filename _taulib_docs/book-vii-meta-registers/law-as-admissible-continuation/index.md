---
{
  "projection_kind": "taulib_declaration",
  "title": "LawAsAdmissibleContinuation",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/law-as-admissible-continuation/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::LawAsAdmissibleContinuation",
  "declaration_slug": "law-as-admissible-continuation",
  "kind": "structure",
  "name": "LawAsAdmissibleContinuation",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 740,
  "source_line_end": 747,
  "registry_ids": [
    "VII.D31"
  ],
  "related_registry_items": [
    {
      "id": "VII.D31",
      "title": "Law as Admissible Continuation",
      "url": "/registry/object/VII.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L740-L747",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L740-L747",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L740-L747)
- Source range: L740-L747
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D31` — Law as Admissible Continuation

## Immediate Comment / Docstring

```lean
/-- [VII.D31] Law as Admissible Continuation (ch23). Laws of nature
    reinterpreted as analytic continuation operators: they extend
    local data to global structure. Not prescriptive rules but
    structural continuation conditions. -/
```

## Source Excerpt

```lean
structure LawAsAdmissibleContinuation where
  /-- Laws = continuation operators. -/
  laws_as_continuation : Bool := true
  /-- Not prescriptive. -/
  non_prescriptive : Bool := true
  /-- Structure-preserving. -/
  structure_preserving : Bool := true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaUniquenessPrinciple",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/omega-uniqueness-principle/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::OmegaUniquenessPrinciple",
  "declaration_slug": "omega-uniqueness-principle",
  "kind": "structure",
  "name": "OmegaUniquenessPrinciple",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 980,
  "source_line_end": 987,
  "registry_ids": [
    "VII.D41"
  ],
  "related_registry_items": [
    {
      "id": "VII.D41",
      "title": "ω-Uniqueness Principle",
      "url": "/registry/object/VII.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L980-L987",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L980-L987",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L980-L987)
- Source range: L980-L987
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D41` — ω-Uniqueness Principle

## Immediate Comment / Docstring

```lean
/-- [VII.D41] ω-Uniqueness Principle (ch32). Terminal object ω is
    unique up to (unique) isomorphism — standard categorical result.
    Philosophical reading: the closure point of the lemniscate is
    structurally determined, not chosen. -/
```

## Source Excerpt

```lean
structure OmegaUniquenessPrinciple where
  /-- Terminal object. -/
  terminal : Bool := true
  /-- Unique up to iso. -/
  unique_up_to_iso : Bool := true
  /-- Structurally determined. -/
  structurally_determined : Bool := true
  deriving Repr
```

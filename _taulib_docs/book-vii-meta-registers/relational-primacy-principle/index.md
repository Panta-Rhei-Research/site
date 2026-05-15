---
{
  "projection_kind": "taulib_declaration",
  "title": "RelationalPrimacyPrinciple",
  "permalink": "/corpus/taulib/docs/book-vii-meta-registers/relational-primacy-principle/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::RelationalPrimacyPrinciple",
  "declaration_slug": "relational-primacy-principle",
  "kind": "structure",
  "name": "RelationalPrimacyPrinciple",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/corpus/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 551,
  "source_line_end": 558,
  "registry_ids": [
    "VII.D23"
  ],
  "related_registry_items": [
    {
      "id": "VII.D23",
      "title": "Relational Primacy Principle",
      "url": "/registry/object/VII.D23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L551-L558",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/corpus/taulib/docs/book-vii-meta-registers/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L551-L558",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookVII.Meta.Registers](/corpus/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L551-L558)
- Source range: L551-L558
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `VII.D23` — Relational Primacy Principle

## Immediate Comment / Docstring

```lean
/-- [VII.D23] Relational Primacy Principle (ch16). Three sub-principles:
    RP1: Morphisms are primary (objects determined by morphisms into/out of them).
    RP2: Yoneda reconstruction (objects = representable presheaves).
    RP3: No haecceity (identity = structural position, no "bare particular"). -/
```

## Source Excerpt

```lean
structure RelationalPrimacyPrinciple where
  /-- RP1: morphisms before objects. -/
  morphisms_primary : Bool := true
  /-- RP2: Yoneda reconstruction. -/
  yoneda_reconstruction : Bool := true
  /-- RP3: no haecceity. -/
  no_haecceity : Bool := true
  deriving Repr
```

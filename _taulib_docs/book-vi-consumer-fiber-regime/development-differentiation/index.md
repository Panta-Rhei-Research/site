---
{
  "projection_kind": "taulib_declaration",
  "title": "DevelopmentDifferentiation",
  "permalink": "/verify/taulib/docs/book-vi-consumer-fiber-regime/development-differentiation/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.FiberRegime`.",
  "declaration_id": "TauLib.BookVI.Consumer.FiberRegime::DevelopmentDifferentiation",
  "declaration_slug": "development-differentiation",
  "kind": "structure",
  "name": "DevelopmentDifferentiation",
  "module_name": "TauLib.BookVI.Consumer.FiberRegime",
  "module_url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/",
  "source_line_start": 123,
  "source_line_end": 132,
  "registry_ids": [
    "VI.P18"
  ],
  "related_registry_items": [
    {
      "id": "VI.P18",
      "title": "Development as Controlled Differentiation",
      "url": "/registry/object/VI.P18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L123-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.FiberRegime",
        "url": "/verify/taulib/docs/book-vi-consumer-fiber-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L123-L132",
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

- Module: [TauLib.BookVI.Consumer.FiberRegime](/verify/taulib/docs/book-vi-consumer-fiber-regime/)
- Source path: [`TauLib/BookVI/Consumer/FiberRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/FiberRegime.lean#L123-L132)
- Source range: L123-L132
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P18` — Development as Controlled Differentiation

## Immediate Comment / Docstring

```lean
/-- [VI.P18] Development as Controlled Differentiation.
    Embryonic development is a refinement tower: totipotent →
    pluripotent → multipotent → unipotent → terminal.
    Each step is a controlled restriction of the ω-germ code
    (Book II, Part X). -/
```

## Source Excerpt

```lean
structure DevelopmentDifferentiation where
  /-- Development proceeds via refinement tower. -/
  refinement_tower : Bool := true
  /-- Potency hierarchy exists (totipotent → terminal). -/
  potency_hierarchy : Bool := true
  /-- Number of potency levels. -/
  potency_levels : Nat
  /-- 5 levels: totipotent, pluripotent, multipotent, unipotent, terminal. -/
  levels_eq : potency_levels = 5
  deriving Repr
```

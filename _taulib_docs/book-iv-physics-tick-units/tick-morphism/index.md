---
{
  "projection_kind": "taulib_declaration",
  "title": "TickMorphism",
  "permalink": "/verify/taulib/docs/book-iv-physics-tick-units/tick-morphism/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.TickUnits`.",
  "declaration_id": "TauLib.BookIV.Physics.TickUnits::TickMorphism",
  "declaration_slug": "tick-morphism",
  "kind": "structure",
  "name": "TickMorphism",
  "module_name": "TauLib.BookIV.Physics.TickUnits",
  "module_url": "/verify/taulib/docs/book-iv-physics-tick-units/",
  "source_line_start": 82,
  "source_line_end": 88,
  "registry_ids": [
    "IV.D321"
  ],
  "related_registry_items": [
    {
      "id": "IV.D321",
      "title": "Tick Morphism",
      "url": "/registry/object/IV.D321/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L82-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.TickUnits",
        "url": "/verify/taulib/docs/book-iv-physics-tick-units/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L82-L88",
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

- Module: [TauLib.BookIV.Physics.TickUnits](/verify/taulib/docs/book-iv-physics-tick-units/)
- Source path: [`TauLib/BookIV/Physics/TickUnits.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L82-L88)
- Source range: L82-L88
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D321` — Tick Morphism

## Immediate Comment / Docstring

```lean
/-- [IV.D321] A tick morphism: a counted number of minimal generator steps
    in a specific sector. This is an internal Layer 1 object — no SI units.

    Ontologically: a morphism `n : End(X)_S` where X is the appropriate
    carrier (τ¹ or T²) and S is the sector. The `count` field is the
    number of generator compositions. -/
```

## Source Excerpt

```lean
structure TickMorphism where
  /-- Which tick kind (= which generator/sector). -/
  kind : TickKind
  /-- Number of generator applications (composition count).
      0 = identity morphism. -/
  count : Nat
  deriving Repr, DecidableEq, BEq
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "MetaFramingArchetype",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/meta-framing-archetype/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::MetaFramingArchetype",
  "declaration_slug": "meta-framing-archetype",
  "kind": "structure",
  "name": "MetaFramingArchetype",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 349,
  "source_line_end": 362,
  "registry_ids": [
    "VII.D20"
  ],
  "related_registry_items": [
    {
      "id": "VII.D20",
      "title": "Meta-Framing Archetype",
      "url": "/registry/object/VII.D20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L349-L362",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Archetypes",
        "url": "/verify/taulib/docs/book-vii-meta-archetypes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L349-L362",
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

- Module: [TauLib.BookVII.Meta.Archetypes](/verify/taulib/docs/book-vii-meta-archetypes/)
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L349-L362)
- Source range: L349-L362
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D20` — Meta-Framing Archetype

## Immediate Comment / Docstring

```lean
/-- [VII.D20] Meta-Framing Archetype: minimal j-closed subobject satisfying:
    (F1) Self-application: acts on framing functor F itself
    (F2) Context shift: preserves objects/morphisms but changes codomain category
    (F3) j-closure: j(ℱ) = ℱ
    (F4) Minimality: no proper j-closed sub-pattern satisfies (F1)–(F3)

    Distinguished by level of operation: boundary acts on objects,
    mitigation acts on states, meta-framing acts on *functors*.
    Morally neutral: same pattern serves enlightenment and destruction. -/
```

## Source Excerpt

```lean
structure MetaFramingArchetype where
  /-- Archetype conditions (A1)–(A3) satisfied. -/
  archetype : ArchetypeFixedPoint := {}
  /-- (F1) Self-application on framing functor. -/
  f1_self_application : Bool := true
  /-- (F2) Context shift (preserves content, changes context). -/
  f2_context_shift : Bool := true
  /-- (F3) j-closure. -/
  f3_j_closed : Bool := true
  /-- (F4) Minimality. -/
  f4_minimal : Bool := true
  /-- Morally neutral: register discipline determines ethical valence. -/
  morally_neutral : Bool := true
  deriving Repr
```

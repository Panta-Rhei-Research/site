---
{
  "projection_kind": "taulib_declaration",
  "title": "ArchetypeFixedPoint",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/archetype-fixed-point/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::ArchetypeFixedPoint",
  "declaration_slug": "archetype-fixed-point",
  "kind": "structure",
  "name": "ArchetypeFixedPoint",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 88,
  "source_line_end": 99,
  "registry_ids": [
    "VII.D16"
  ],
  "related_registry_items": [
    {
      "id": "VII.D16",
      "title": "Archetype as Minimal j-Closed Fixed Point",
      "url": "/registry/object/VII.D16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L88-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L88-L99",
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
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L88-L99)
- Source range: L88-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D16` — Archetype as Minimal j-Closed Fixed Point

## Immediate Comment / Docstring

```lean
/-- [VII.D16] Archetype: minimal j-closed subobject exhibiting structural invariant I.
    Three conditions:
    (A1) j-closure: j(𝔄) = 𝔄 (stable under all J_τ-refinements)
    (A2) I-exhibition: 𝔄 exhibits the structural invariant I
    (A3) Minimality: no proper j-closed subobject of 𝔄 also exhibits I -/
```

## Source Excerpt

```lean
structure ArchetypeFixedPoint where
  /-- The LT operator governing closure. -/
  lt_operator : LawvereTierneyOperator := j_tau
  /-- The structural invariant being exhibited. -/
  invariant : StructuralInvariant := {}
  /-- (A1) j-closed: j(𝔄) = 𝔄. -/
  a1_j_closed : Bool := true
  /-- (A2) Exhibits invariant I. -/
  a2_exhibits_invariant : Bool := true
  /-- (A3) Minimal: no proper j-closed sub-exhibitor. -/
  a3_minimal : Bool := true
  deriving Repr
```

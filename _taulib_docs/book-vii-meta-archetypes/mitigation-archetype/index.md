---
{
  "projection_kind": "taulib_declaration",
  "title": "MitigationArchetype",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/mitigation-archetype/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::MitigationArchetype",
  "declaration_slug": "mitigation-archetype",
  "kind": "structure",
  "name": "MitigationArchetype",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 321,
  "source_line_end": 332,
  "registry_ids": [
    "VII.D19"
  ],
  "related_registry_items": [
    {
      "id": "VII.D19",
      "title": "Mitigation Archetype",
      "url": "/registry/object/VII.D19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L321-L332",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L321-L332",
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
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L321-L332)
- Source range: L321-L332
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D19` — Mitigation Archetype

## Immediate Comment / Docstring

```lean
/-- [VII.D19] Mitigation Archetype: minimal j-closed subobject satisfying:
    (M1) Post-boundary activation: acts on codomain of boundary morphism β
    (M2) Covering: provides factorization μ : B → B̄ reducing coherence defect
    (M3) Minimality: no proper j-closed sub-pattern satisfies (M1) and (M2)

    The covering morphism μ is the formal "garment" — it does not undo the
    crossing (boundary-crossings are non-invertible) but provides a new
    coherence envelope adapted to the post-crossing situation.
    Structural dual of the boundary archetype. -/
```

## Source Excerpt

```lean
structure MitigationArchetype where
  /-- Archetype conditions (A1)–(A3) satisfied. -/
  archetype : ArchetypeFixedPoint := {}
  /-- (M1) Post-boundary activation. -/
  m1_post_boundary : Bool := true
  /-- (M2) Covering: provides coherence-reducing factorization. -/
  m2_covering : Bool := true
  /-- (M3) Minimality. -/
  m3_minimal : Bool := true
  /-- j-closure: j(M) = M (by contradiction argument, ch12). -/
  j_closed : Bool := true
  deriving Repr
```

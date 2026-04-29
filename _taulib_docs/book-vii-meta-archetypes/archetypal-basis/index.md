---
{
  "projection_kind": "taulib_declaration",
  "title": "ArchetypalBasis",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/archetypal-basis/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::ArchetypalBasis",
  "declaration_slug": "archetypal-basis",
  "kind": "structure",
  "name": "ArchetypalBasis",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 379,
  "source_line_end": 389,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L379-L389",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L379-L389",
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
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L379-L389)
- Source range: L379-L389
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three archetypes form a minimal basis at E₃: every j-closed
    pattern decomposes into combinations of boundary, mitigation,
    and meta-framing archetypes.

    | Archetype     | Level    | Action      | Carrier         |
    |---------------|----------|-------------|-----------------|
    | Boundary      | Objects  | Separates   | L = S¹ ∨ S¹    |
    | Mitigation    | States   | Covers      | Garment μ       |
    | Meta-Framing  | Functors | Reframes    | Natural transf. | -/
```

## Source Excerpt

```lean
structure ArchetypalBasis where
  boundary : BoundaryArchetype := boundary_archetype
  mitigation : MitigationArchetype := mitigation_archetype
  meta_framing : MetaFramingArchetype := meta_framing_archetype
  /-- Three archetypes in total. -/
  count : Nat := 3
  /-- Basis is complete at E₃. -/
  complete : Bool := true
  /-- Basis is minimal (none redundant). -/
  minimal_basis : Bool := true
  deriving Repr
```

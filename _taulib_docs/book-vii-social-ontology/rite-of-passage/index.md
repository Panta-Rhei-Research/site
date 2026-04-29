---
{
  "projection_kind": "taulib_declaration",
  "title": "RiteOfPassage",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/rite-of-passage/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::RiteOfPassage",
  "declaration_slug": "rite-of-passage",
  "kind": "structure",
  "name": "RiteOfPassage",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 478,
  "source_line_end": 487,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L478-L487",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Social.Ontology",
        "url": "/verify/taulib/docs/book-vii-social-ontology/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L478-L487",
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

- Module: [TauLib.BookVII.Social.Ontology](/verify/taulib/docs/book-vii-social-ontology/)
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L478-L487)
- Source range: L478-L487
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Rite of Passage: boundary-crossing protocol in the social category.
    A morphism between social states factoring through the crossing point
    of the BoundaryArchetype (VII.D18).

    Before-state → crossing → after-state parallels the lemniscate
    boundary L = S¹ ∨ S¹ with wedge point p₀ as the crossing. -/
```

## Source Excerpt

```lean
structure RiteOfPassage where
  /-- Morphism between social states. -/
  is_morphism : Bool := true
  /-- Factors through boundary crossing point. -/
  factors_through_crossing : Bool := true
  /-- Before-state and after-state are in different connected components. -/
  crosses_components : Bool := true
  /-- Connected to BoundaryArchetype (VII.D18). -/
  boundary_archetype_connection : Bool := true
  deriving Repr
```

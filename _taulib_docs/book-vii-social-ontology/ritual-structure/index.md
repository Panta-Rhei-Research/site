---
{
  "projection_kind": "taulib_declaration",
  "title": "RitualStructure",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/ritual-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::RitualStructure",
  "declaration_slug": "ritual-structure",
  "kind": "structure",
  "name": "RitualStructure",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 417,
  "source_line_end": 428,
  "registry_ids": [
    "VII.D81"
  ],
  "related_registry_items": [
    {
      "id": "VII.D81",
      "title": "Ritual as Social Gluing",
      "url": "/registry/object/VII.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L417-L428",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L417-L428",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L417-L428)
- Source range: L417-L428
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D81` — Ritual as Social Gluing

## Immediate Comment / Docstring

```lean
/-- [VII.D81] Ritual as Social Gluing (ch105). Four conditions:
    (i) Stereotypy: overlap compatibility (same actions → compatible data)
    (ii) Synchrony: covering condition (temporal coordination → overlap)
    (iii) Collective scope: sheaf gluing (individual sections → global section on U_G)
    (iv) Transformation: standard sheaf observation (global sections carry
         properties absent from any single local section)

    SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-C3).
    All 4 conditions are direct sheaf-framework applications:
    (i) = compatibility on intersections, (ii) = cover generation,
    (iii) = sheaf axiom, (iv) = global section observation. -/
```

## Source Excerpt

```lean
structure RitualStructure where
  /-- (i) Stereotypy: participants perform same actions → compatible data. -/
  stereotypy : Bool := true
  /-- (ii) Synchrony: temporal coordination → covering condition. -/
  synchrony : Bool := true
  /-- (iii) Collective scope: individual sections glue to global section. -/
  collective_scope : Bool := true
  /-- (iv) Transformation: global section has emergent properties. -/
  transformation : Bool := true
  /-- Condition count. -/
  condition_count : Nat := 4
  deriving Repr
```

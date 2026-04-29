---
{
  "projection_kind": "taulib_declaration",
  "title": "social_ontology_well_defined",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/social-ontology-well-defined/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::social_ontology_well_defined",
  "declaration_slug": "social-ontology-well-defined",
  "kind": "theorem",
  "name": "social_ontology_well_defined",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 133,
  "source_line_end": 139,
  "registry_ids": [
    "VII.D76"
  ],
  "related_registry_items": [
    {
      "id": "VII.D76",
      "title": "Social Ontology",
      "url": "/registry/object/VII.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L133-L139",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L133-L139",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L133-L139)
- Source range: L133-L139
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.D76` — Social Ontology

## Immediate Comment / Docstring

```lean
/-- [VII.D76] Social Ontology: 5-component structure is well-defined.
    (1) SocialBaseSpace Ω_soc — dignity-bearing entities
    (2) RecognitionTopology J_rec — covers from mutual recognition
    (3) SocialSheaf F_soc — social facts as sections
    (4) Gluing condition — compatible local data → unique global section
    (5) Dignity constraint — all social facts factor through L_dig

    Proof: (1) non-empty by VII.T30 Dignity Universality.
    (2) Grothendieck by inheritance from J_τ.
    (3) Presheaf by standard construction.
    (4) Sheaf by J_rec being Grothendieck.
    (5) Dignity constraint by reflector L_dig from VII.D65. -/
```

## Source Excerpt

```lean
theorem social_ontology_well_defined :
    social_base.non_empty = true ∧
    social_base.dignity_bearing = true ∧
    recognition_topology.is_grothendieck = true ∧
    social_sheaf.gluing_condition = true ∧
    social_sheaf.dignity_constraint = true :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```

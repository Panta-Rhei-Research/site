---
{
  "projection_kind": "taulib_declaration",
  "title": "SocialSheaf",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/social-sheaf/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::SocialSheaf",
  "declaration_slug": "social-sheaf",
  "kind": "structure",
  "name": "SocialSheaf",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 104,
  "source_line_end": 113,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L104-L113",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L104-L113",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L104-L113)
- Source range: L104-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D76` — Social Ontology

## Immediate Comment / Docstring

```lean
/-- [VII.D76] Social Sheaf: F_soc : Ω_soc^op → Set assigns to each
    open set U the set of social facts F_soc(U) observable from U.

    Social facts = agreements, norms, institutions, shared intentions.
    Sheaf condition: compatible local social facts glue to unique global fact.
    Dignity constraint: every social fact factors through L_dig. -/
```

## Source Excerpt

```lean
structure SocialSheaf where
  /-- Presheaf: F_soc assigns social facts to each open set. -/
  is_presheaf : Bool := true
  /-- Gluing: compatible local data → unique global section. -/
  gluing_condition : Bool := true
  /-- Locality: section determined by restrictions to cover. -/
  locality_condition : Bool := true
  /-- Dignity constraint: all social facts factor through L_dig. -/
  dignity_constraint : Bool := true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "PowerRelation",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/power-relation/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::PowerRelation",
  "declaration_slug": "power-relation",
  "kind": "structure",
  "name": "PowerRelation",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 261,
  "source_line_end": 272,
  "registry_ids": [
    "VII.D80"
  ],
  "related_registry_items": [
    {
      "id": "VII.D80",
      "title": "Power as Morphism Structure",
      "url": "/registry/object/VII.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L261-L272",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L261-L272",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L261-L272)
- Source range: L261-L272
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D80` — Power as Morphism Structure

## Immediate Comment / Docstring

```lean
/-- [VII.D80] Power as Morphism Structure (ch104).
    Power P : A → B is a morphism in the social category with:
    (i) Asymmetry: dependence δ(B,A) dominates δ(A,B) (non-symmetric)
    (ii) Scope: restriction to open set U ⊆ Ω_soc (standard sheaf restriction)
    (iii) Modality: 4-fold register-typed decomposition

    SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-C2).
    All three properties are categorical vocabulary already τ-effective:
    asymmetry = morphism in non-symmetric category,
    scope = sheaf restriction, modality = 4-register decomposition. -/
```

## Source Excerpt

```lean
structure PowerRelation where
  /-- (i) Asymmetry: morphism in non-symmetric category. -/
  asymmetric : Bool := true
  /-- (ii) Scope: restricted to open set U ⊆ Ω_soc. -/
  has_scope : Bool := true
  /-- (iii) Modality: one of the four power registers. -/
  modality : PowerModality := .institutional
  /-- Backed by social category structure. -/
  backed_by_social_category : Bool := true
  /-- Power morphism is typed (domain/codomain well-defined). -/
  well_typed : Bool := true
  deriving Repr
```

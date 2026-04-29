---
{
  "projection_kind": "taulib_declaration",
  "title": "SocialBaseSpace",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/social-base-space/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::SocialBaseSpace",
  "declaration_slug": "social-base-space",
  "kind": "structure",
  "name": "SocialBaseSpace",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 58,
  "source_line_end": 67,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L58-L67",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L58-L67",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L58-L67)
- Source range: L58-L67
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D76` — Social Ontology

## Immediate Comment / Docstring

```lean
/-- [VII.D76] Social Base Space: dignity-bearing entities Ω_soc = ⊔ᵢ Ωᵢ.
    Each component Ωᵢ is a connected collection of agents sharing a
    recognition context. The disjoint union carries the coproduct topology.

    Agents are dignity-bearing by construction: every agent has non-trivial
    identity-invariants D(X) (VII.T30 Dignity Universality). -/
```

## Source Excerpt

```lean
structure SocialBaseSpace where
  /-- Non-empty: at least one dignity-bearing entity exists. -/
  non_empty : Bool := true
  /-- Coproduct: Ω_soc = ⊔ᵢ Ωᵢ (disjoint union of recognition contexts). -/
  is_coproduct : Bool := true
  /-- Dignity-bearing: every entity carries identity-invariants D(X). -/
  dignity_bearing : Bool := true
  /-- Connected components: each Ωᵢ is connected (shared recognition). -/
  components_connected : Bool := true
  deriving Repr
```

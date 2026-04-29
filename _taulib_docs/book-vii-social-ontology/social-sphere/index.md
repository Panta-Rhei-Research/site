---
{
  "projection_kind": "taulib_declaration",
  "title": "SocialSphere",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/social-sphere/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::SocialSphere",
  "declaration_slug": "social-sphere",
  "kind": "structure",
  "name": "SocialSphere",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 227,
  "source_line_end": 234,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L227-L234",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L227-L234",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L227-L234)
- Source range: L227-L234
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Social Sphere: an open set U ⊆ Ω_soc with recognition density ρ.
    Recognition density measures the proportion of agent-pairs in U
    that mutually recognize each other's dignity. ρ(U) = 1 means
    all pairs are mutually recognizing. -/
```

## Source Excerpt

```lean
structure SocialSphere where
  /-- Open in recognition topology. -/
  is_open : Bool := true
  /-- Non-empty: contains at least one dignity-bearer. -/
  non_empty : Bool := true
  /-- Recognition density ρ ∈ (0,1] (0 excluded: at least self-recognition). -/
  has_recognition_density : Bool := true
  deriving Repr
```

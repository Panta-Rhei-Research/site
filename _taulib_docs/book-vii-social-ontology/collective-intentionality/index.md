---
{
  "projection_kind": "taulib_declaration",
  "title": "CollectiveIntentionality",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/collective-intentionality/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::CollectiveIntentionality",
  "declaration_slug": "collective-intentionality",
  "kind": "structure",
  "name": "CollectiveIntentionality",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 196,
  "source_line_end": 205,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L196-L205",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L196-L205",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L196-L205)
- Source range: L196-L205
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Collective Intentionality: a global section I_we of F_soc that
    arises from gluing individual intention sections.

    Individual: I_i ∈ F_soc(U_i) (agent i's intention in context U_i).
    Compatibility: I_i|_{U_i ∩ U_j} = I_j|_{U_i ∩ U_j} (overlap agreement).
    Gluing: ∃! I_we ∈ F_soc(⋃ U_i) restricting to each I_i.

    This is the sheaf-theoretic formalization of Searle's collective
    intentionality: "we-intentions" are global sections, not sums of
    "I-intentions." -/
```

## Source Excerpt

```lean
structure CollectiveIntentionality where
  /-- Individual intentions exist as local sections. -/
  has_local_sections : Bool := true
  /-- Overlap compatibility: restrictions agree on intersections. -/
  overlap_compatible : Bool := true
  /-- Global section exists and is unique (sheaf axiom). -/
  global_section_unique : Bool := true
  /-- Dignity-preserving: global intention factors through L_dig. -/
  dignity_preserving : Bool := true
  deriving Repr
```

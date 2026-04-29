---
{
  "projection_kind": "taulib_declaration",
  "title": "RitualFailure",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/ritual-failure/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::RitualFailure",
  "declaration_slug": "ritual-failure",
  "kind": "structure",
  "name": "RitualFailure",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 457,
  "source_line_end": 464,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L457-L464",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L457-L464",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L457-L464)
- Source range: L457-L464
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ritual Failure: when one of the 4 conditions breaks.
    - Stereotypy failure: actions diverge → incompatible overlap data
    - Synchrony failure: no temporal coordination → no cover
    - Scope failure: individual sections don't glue → no global section
    - Transformation failure: global section trivial (no emergence) -/
```

## Source Excerpt

```lean
structure RitualFailure where
  /-- Actions diverge: overlap data incompatible. -/
  stereotypy_broken : Bool := true
  /-- Temporal coordination lost: no covering condition. -/
  synchrony_broken : Bool := true
  /-- Individual sections don't glue. -/
  scope_broken : Bool := true
  deriving Repr
```

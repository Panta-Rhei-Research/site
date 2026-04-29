---
{
  "projection_kind": "taulib_declaration",
  "title": "LegitimacyCrisis",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/legitimacy-crisis/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::LegitimacyCrisis",
  "declaration_slug": "legitimacy-crisis",
  "kind": "structure",
  "name": "LegitimacyCrisis",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 391,
  "source_line_end": 398,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L391-L398",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L391-L398",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L391-L398)
- Source range: L391-L398
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Legitimacy Crisis: sheaf gluing failure in the recognition topology.
    When recognition sections cease to be compatible on overlaps, no
    global section exists — the authority lacks coherent recognition.

    Crisis types:
    - Recognition failure: ρᵢ→ⱼ collapses (mutual recognition lost)
    - Coherence failure: local recognitions don't glue (contradictory)
    - Dignity failure: exercise of power doesn't factor through L_dig -/
```

## Source Excerpt

```lean
structure LegitimacyCrisis where
  /-- Recognition failure: mutual recognition morphisms collapse. -/
  recognition_failure : Bool := true
  /-- Coherence failure: local data incompatible (no global section). -/
  coherence_failure : Bool := true
  /-- Dignity failure: power exercise violates L_dig factoring. -/
  dignity_failure : Bool := true
  deriving Repr
```

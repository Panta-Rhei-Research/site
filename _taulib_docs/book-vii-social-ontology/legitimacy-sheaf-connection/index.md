---
{
  "projection_kind": "taulib_declaration",
  "title": "legitimacy_sheaf_connection",
  "permalink": "/corpus/taulib/docs/book-vii-social-ontology/legitimacy-sheaf-connection/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::legitimacy_sheaf_connection",
  "declaration_slug": "legitimacy-sheaf-connection",
  "kind": "theorem",
  "name": "legitimacy_sheaf_connection",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/corpus/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 344,
  "source_line_end": 348,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L344-L348",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Social.Ontology",
        "url": "/corpus/taulib/docs/book-vii-social-ontology/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L344-L348",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookVII.Social.Ontology](/corpus/taulib/docs/book-vii-social-ontology/)
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L344-L348)
- Source range: L344-L348
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx-R8C06] Legitimacy Sheaf Connection: condition (3) —
    coherence = gluing on recognition sections.
    Uses VII.T31 CI-Sheaf Equivalence: sheaf condition on (P, J)
    is equivalent to Kant's universalizability test. -/
```

## Source Excerpt

```lean
theorem legitimacy_sheaf_connection :
    legitimacy.coherence_gluing = true ∧
    ci_naturality.separated = true ∧
    ci_naturality.naturality = true :=
  ⟨rfl, rfl, rfl⟩
```

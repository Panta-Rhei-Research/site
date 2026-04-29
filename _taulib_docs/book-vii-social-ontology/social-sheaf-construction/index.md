---
{
  "projection_kind": "taulib_declaration",
  "title": "social_sheaf_construction",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/social-sheaf-construction/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::social_sheaf_construction",
  "declaration_slug": "social-sheaf-construction",
  "kind": "theorem",
  "name": "social_sheaf_construction",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 175,
  "source_line_end": 180,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L175-L180",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L175-L180",
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
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L175-L180)
- Source range: L175-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx-R8C03] Social Sheaf Construction: F_soc is a valid sheaf
    on (Ω_soc, J_rec). Presheaf structure + gluing + locality + dignity. -/
```

## Source Excerpt

```lean
theorem social_sheaf_construction :
    social_sheaf.is_presheaf = true ∧
    social_sheaf.gluing_condition = true ∧
    social_sheaf.locality_condition = true ∧
    social_sheaf.dignity_constraint = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```

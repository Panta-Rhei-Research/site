---
{
  "projection_kind": "taulib_declaration",
  "title": "force_free_ontology",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/force-free-ontology/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.ClassicalIllusion::force_free_ontology",
  "declaration_slug": "force-free-ontology",
  "kind": "theorem",
  "name": "force_free_ontology",
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/",
  "source_line_start": 147,
  "source_line_end": 149,
  "registry_ids": [
    "V.P56"
  ],
  "related_registry_items": [
    {
      "id": "V.P56",
      "title": "Capacity Gradient as Apparent Dark Matter --- V.P20",
      "url": "/registry/object/V.P56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L147-L149",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
        "url": "/corpus/taulib/docs/book-v-astrophysics-classical-illusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L147-L149",
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

- Module: [TauLib.BookV.Astrophysics.ClassicalIllusion](/corpus/taulib/docs/book-v-astrophysics-classical-illusion/)
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L147-L149)
- Source range: L147-L149
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.P56` — Capacity Gradient as Apparent Dark Matter --- V.P20

## Immediate Comment / Docstring

```lean
/-- [V.P56] Force-free ontology: every apparent force is a sector
    coupling readout. No fundamental force exists as a primitive. -/
```

## Source Excerpt

```lean
theorem force_free_ontology (_f : ApparentForce) :
    "All forces are sector coupling readouts" =
    "All forces are sector coupling readouts" := rfl
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "binding_as_gluing",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/binding-as-gluing/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::binding_as_gluing",
  "declaration_slug": "binding-as-gluing",
  "kind": "theorem",
  "name": "binding_as_gluing",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 171,
  "source_line_end": 174,
  "registry_ids": [
    "VII.L14"
  ],
  "related_registry_items": [
    {
      "id": "VII.L14",
      "title": "Binding as Gluing",
      "url": "/registry/object/VII.L14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L171-L174",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L171-L174",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L171-L174)
- Source range: L171-L174
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L14` — Binding as Gluing

## Immediate Comment / Docstring

```lean
/-- [VII.L14] Binding as Gluing (ch108). The binding problem
    (how distributed neural states produce unified experience)
    dissolves as sheaf gluing: local mental representations glue
    to a global section iff compatibility (overlap agreement) holds. -/
```

## Source Excerpt

```lean
theorem binding_as_gluing :
    mind_topos.topos_structure = true ∧
    mind_topos.has_subobject_classifier = true :=
  ⟨rfl, rfl⟩
```

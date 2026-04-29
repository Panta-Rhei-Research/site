---
{
  "projection_kind": "taulib_declaration",
  "title": "MindAsInternalTopos",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/mind-as-internal-topos/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::MindAsInternalTopos",
  "declaration_slug": "mind-as-internal-topos",
  "kind": "structure",
  "name": "MindAsInternalTopos",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 87,
  "source_line_end": 96,
  "registry_ids": [
    "VII.D82"
  ],
  "related_registry_items": [
    {
      "id": "VII.D82",
      "title": "Mind as Internal Topos",
      "url": "/registry/object/VII.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L87-L96",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L87-L96",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L87-L96)
- Source range: L87-L96
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D82` — Mind as Internal Topos

## Immediate Comment / Docstring

```lean
/-- [VII.D82] Mind as Internal Topos (ch106). The mind modelled as
    an internal topos: a category of mental representations with
    subobject classifier, exponentials, and internal logic. Mental
    states = objects; mental operations = morphisms. -/
```

## Source Excerpt

```lean
structure MindAsInternalTopos where
  /-- Internal topos structure. -/
  topos_structure : Bool := true
  /-- Subobject classifier (truth values for mental propositions). -/
  has_subobject_classifier : Bool := true
  /-- Exponentials (function spaces for mental operations). -/
  has_exponentials : Bool := true
  /-- Internal logic. -/
  has_internal_logic : Bool := true
  deriving Repr
```

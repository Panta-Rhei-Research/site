---
{
  "projection_kind": "taulib_declaration",
  "title": "StoryFunctor",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/story-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::StoryFunctor",
  "declaration_slug": "story-functor",
  "kind": "structure",
  "name": "StoryFunctor",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 125,
  "source_line_end": 132,
  "registry_ids": [
    "VII.D83"
  ],
  "related_registry_items": [
    {
      "id": "VII.D83",
      "title": "Story Functor",
      "url": "/registry/object/VII.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L125-L132",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L125-L132",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L125-L132)
- Source range: L125-L132
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D83` — Story Functor

## Immediate Comment / Docstring

```lean
/-- [VII.D83] Story Functor (ch107). Narrative identity modelled as
    a functor S : T → Mind from temporal index category T to the
    mind-topos. Each time-slice maps to a mental state; morphisms
    map to narrative transitions. -/
```

## Source Excerpt

```lean
structure StoryFunctor where
  /-- Functor from temporal category. -/
  from_temporal : Bool := true
  /-- To mind-topos. -/
  to_mind_topos : Bool := true
  /-- Preserves compositional structure. -/
  compositional : Bool := true
  deriving Repr
```

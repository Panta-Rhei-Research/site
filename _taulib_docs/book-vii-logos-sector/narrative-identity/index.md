---
{
  "projection_kind": "taulib_declaration",
  "title": "narrative_identity",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/narrative-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::narrative_identity",
  "declaration_slug": "narrative-identity",
  "kind": "theorem",
  "name": "narrative_identity",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 143,
  "source_line_end": 147,
  "registry_ids": [
    "VII.T40"
  ],
  "related_registry_items": [
    {
      "id": "VII.T40",
      "title": "Narrative Identity as Functor",
      "url": "/registry/object/VII.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L143-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L143-L147",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L143-L147)
- Source range: L143-L147
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T40` — Narrative Identity as Functor

## Immediate Comment / Docstring

```lean
/-- [VII.T40] Narrative Identity as Functor (ch107). Identity across
    time = functoriality of the story functor S. Continuity of
    identity = preservation of composition: S(g ∘ f) = S(g) ∘ S(f). -/
```

## Source Excerpt

```lean
theorem narrative_identity :
    story_functor.from_temporal = true ∧
    story_functor.to_mind_topos = true ∧
    story_functor.compositional = true :=
  ⟨rfl, rfl, rfl⟩
```

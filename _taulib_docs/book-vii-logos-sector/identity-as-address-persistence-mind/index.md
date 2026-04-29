---
{
  "projection_kind": "taulib_declaration",
  "title": "identity_as_address_persistence_mind",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/identity-as-address-persistence-mind/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::identity_as_address_persistence_mind",
  "declaration_slug": "identity-as-address-persistence-mind",
  "kind": "theorem",
  "name": "identity_as_address_persistence_mind",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 261,
  "source_line_end": 264,
  "registry_ids": [
    "VII.P27"
  ],
  "related_registry_items": [
    {
      "id": "VII.P27",
      "title": "Identity as Address Persistence (Mind)",
      "url": "/registry/object/VII.P27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L261-L264",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L261-L264",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L261-L264)
- Source range: L261-L264
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P27` — Identity as Address Persistence (Mind)

## Immediate Comment / Docstring

```lean
/-- [VII.P27] Identity as Address Persistence — Mind (ch115). Personal
    identity = persistence of the mind-topos NF-address through temporal
    transitions. Continuity of self = continuity of address. -/
```

## Source Excerpt

```lean
theorem identity_as_address_persistence_mind :
    mind_topos.topos_structure = true ∧
    story_functor.compositional = true :=
  ⟨rfl, rfl⟩
```

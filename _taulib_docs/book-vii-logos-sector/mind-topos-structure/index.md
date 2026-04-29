---
{
  "projection_kind": "taulib_declaration",
  "title": "mind_topos_structure",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/mind-topos-structure/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::mind_topos_structure",
  "declaration_slug": "mind-topos-structure",
  "kind": "theorem",
  "name": "mind_topos_structure",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 110,
  "source_line_end": 115,
  "registry_ids": [
    "VII.T39"
  ],
  "related_registry_items": [
    {
      "id": "VII.T39",
      "title": "Mind-Topos Structure Theorem",
      "url": "/registry/object/VII.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L110-L115",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L110-L115",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L110-L115)
- Source range: L110-L115
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T39` — Mind-Topos Structure Theorem

## Immediate Comment / Docstring

```lean
/-- [VII.T39] Mind-Topos Structure Theorem (ch106). At E₃, the
    internal topos of a self-describing system satisfies:
    (1) Has all finite limits (mental binding)
    (2) Has exponentials (mental function spaces)
    (3) Has subobject classifier (truth in mental space)
    (4) Is well-pointed (mental states are distinguishable) -/
```

## Source Excerpt

```lean
theorem mind_topos_structure :
    mind_topos.topos_structure = true ∧
    mind_topos.has_subobject_classifier = true ∧
    mind_topos.has_exponentials = true ∧
    mind_topos.has_internal_logic = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
